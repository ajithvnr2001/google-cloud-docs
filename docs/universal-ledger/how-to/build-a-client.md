---
url: https://docs.cloud.google.com/universal-ledger/how-to/build-a-client/
title: Build your own client \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:18.960226+00:00
---

# Build your own client  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/how-to/build-a-client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Guides ](https://docs.cloud.google.com/universal-ledger/overview)



Send feedback 

#  Build your own client Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://cloud.google.com/application/web3/universal-ledger). 

This guide provides recommendations to ensure Universal Ledger client implementations interact with a network securely and reliably. Learn how to:

  * Leverage the network topology for high availability.
  * Submit transactions and understand execution outcomes.
  * Implement polling, timeouts, and retry strategies.



## Network topology and high availability

A Universal Ledger network comprises of a number of validators distributed amongst multiple zones and regions, thus ensuring a high availability for the network as a whole.

  * **Zone failures:** If a single validator fails within a Cloud zone, other validators within the same region will seamlessly continue to process requests.

  * **Regional outages:** If an entire region becomes unavailable, validators in other regions remain operational. To continue submitting transactions, it is safe for your client to fall back and attempt to resubmit transactions through a different endpoint.


**Note:** For a list of supported regions, see [Available networks and regions](https://docs.cloud.google.com/universal-ledger/preview-onboarding#available_networks_and_regions).

## Transaction execution characteristics

  * **Atomic execution:** Transactions either succeed entirely or fail entirely. Partial transaction execution—such as transferring only a portion of the requested funds because of an insufficient balance—never occurs. This includes [transaction chains](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#transactionchain), allowing you to combine multiple arbitrary transactions into a single atomic sequence.

  * **No automatic retries:** The network attempts to execute a submitted transaction exactly once. If execution fails, the ledger does not queue or retry the transaction automatically.

  * **Idempotent resubmission:** Every submitted transaction generates a unique transaction ID based on its exact serialized payload (including sequence number and sender). Submitting the exact same payload multiple times produces the same transaction ID. The ledger ensures a transaction is executed at most once, making it safe to resubmit the same transaction payload to a different endpoint if one of them appears unavailable.

For more details, see the [`SubmitTransactionRequest`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SubmitTransactionRequest) reference page.




### Latency, polling, and retry strategy

When you submit a transaction, the validator will first perform a quick check ensuring its signatures and sequence numbers are valid. If successful, the Universal Ledger API will immediately respond with a [`SubmitTransactionResponse`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.SubmitTransactionResponse) including its assigned transaction ID.

Most transactions are finalized within 3 seconds. To check the transaction status, poll the [`QueryTransactionState`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#google.cloud.universalledger.v1.UniversalLedger.QueryTransactionState) method using the provided transaction ID.

  * If the transaction status is still `PENDING`, retrieve the status again using an exponential backoff strategy. For example, query at intervals of **3 seconds, 9 seconds, 27 seconds, and 60 seconds**.

  * If `QueryTransactionState` returns `NOT_FOUND`, resubmit the transaction.




Once a transaction attempt is `FINALIZED`, the response will also include a [`TransactionCertificate`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#transactioncertificate) with various details such as:

  * The round ID at which the transaction was finalized.
  * The execution status (OK or failed).
  * Transaction events, including any transaction outputs.



#### Timeout protocol

In the unlikely event that a transaction remains in a `PENDING` or `NOT_FOUND` state after 60 seconds, assume that the validator serving your requests is failing to catch up with other validators in the network. Complete the following steps:

  1. Select a different endpoint in a different network region.
  2. Resubmit the exact same signed transaction payload.
  3. Report the issue using the 'Send feedback' button at the top of this page for the Universal Ledger team to investigate.



When checking transaction status, the response might include multiple [`TransactionAttempt`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#transactionattempt) messages if you submitted the same payload multiple times. At most one attempt will be finalized with an OK transaction status, found in the [`TransactionEffects`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#transactioneffects), whereas other attempts will either be pending or have a failed status. This is expected behavior; the ledger successfully executed one of the transaction submissions and correctly rejected, or will eventually reject, the duplicated resubmissions.

### Network consistency

  * **Finalized transactions:** Once a transaction is reported as finalized by one validator, all other validators on the same network are expected to eventually process the transaction and reproduce exactly the same outcomes. Submitting a [`QueryAccountRequest`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#queryaccountrequest) using the round ID at which the transaction was finalized, as it can be found in its [`TransactionCertificate`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#transactioncertificate), yields identical results on all synchronized validators.

  * **Non-finalized transactions:** Because transactions propagate across the network asynchronously, whether a transaction is reported as finalized can vary across different validators.

A validator recovering from an outage or experiencing synchronization lag might temporarily report a finalized transaction as `PENDING` or `NOT_FOUND`. The transaction status will resolve once the validator catches up.




### Client responsibilities and error handling

  * **Transaction tracking:** Client applications must track the state of all submitted transactions until they are finalized.

  * **Error handling:** If a transaction fails, retrieve and inspect the failure details included in the [`TransactionCertificate`](https://docs.cloud.google.com/universal-ledger/reference/rpc/google.cloud.universalledger.v1#transactioncertificate) to trigger the appropriate business-level remediation.




## What's next

  * Learn [how to send RPC requests](https://docs.cloud.google.com/universal-ledger/tutorial/send-rpc-request-py) to the Universal Ledger API.
  * Consult the [Universal Ledger API reference](https://docs.cloud.google.com/universal-ledger/reference/rpc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
