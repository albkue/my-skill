# Example: backend-job

## Request
> "Review this Spring Boot Kafka consumer for retry handling, idempotency, and dead-letter queue behavior."

Fictional consumer Sothy could paste from the backend part-time job (Spring Boot 3, Kotlin/Java, single-topic):

```java
@KafkaListener(topics = "orders.paid", groupId = "billing-svc")
public void onOrderPaid(OrderPaidEvent event) {
    orderService.markPaid(event.orderId());
    invoiceClient.createInvoice(event.orderId());   // HTTP call
    ledgerClient.post(event.orderId(), event.amount());
}
```

## What the plugin does

**Route:** `backend-job` (states the context: "Using `backend-job` — backend part-time job context"), pulls `references/backend-checklist.md` Kafka + code-review sections.

**Output (abridged)**

**Summary:** Consumer handles happy path only; offsets commit automatically; no idempotency or DLQ.

**Blocking issues**
1. **Duplicate processing guaranteed, unhandled.** At-least-once delivery + auto-commit can replay events after a rebalance/crash → double `ledgerClient.post()`. Why it matters: billing correctness.
   Fix: make the handler idempotent (natural key upsert or `processed_events` table keyed by `event.orderId()`), commit only after processing.
2. **Poison pill = infinite loop / lag explosion.** Malformed message → exception → seek back → replay forever (no DLQ configured). Fix: wrap per-record try/catch, route to `orders.paid.dlq` after N attempts with the failure reason metadata.

**Important improvements**
- `invoiceClient` call inside the listener blocks the poll thread; check `max.poll.interval.ms` headroom or move to an async unit with circuit breaking.
- Log at we record start/end with `orderId` for traceability; add a metrics counter per outcome (processed / retried / dlq’d).

**Optional:** consider `spring-kafka` `DeadLetterPublishingRecoverer` + `DefaultErrorHandler` instead of hand-rolling.

**Security concerns:** none in the snippet; check the event payload before it reaches logs.

**Test gaps:** duplicate delivery test, malformed-payload test, invoice-500 test.

**Verdict: `request changes`** — duplicate posting to the ledger is a money-correctness bug.

**Follow-up offered (route):** "These handler changes need tests → `backend-testing`? And you mentioned this ships next sprint → `backend-deployment` for the rollout plan?"
