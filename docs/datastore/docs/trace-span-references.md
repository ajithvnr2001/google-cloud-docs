---
url: https://docs.cloud.google.com/datastore/docs/trace-span-references/
title: Trace span attributes and events \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:10.763967+00:00
---

# Trace span attributes and events  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/trace-span-references/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)



Send feedback 

#  Trace span attributes and events Stay organized with collections  Save and categorize content based on your preferences. 

[Client-side traces](https://docs.cloud.google.com/datastore/docs/client-side-traces), which are collected by executing RPCs, provide several pieces of information for every request from a client, including spans with timestamps of when the client sent the RPC request and when the client received the RPC response. The spans include latency introduced by the network and client system.

Client-side traces can include the following information:

## Span metadata

Span ID | Unique ID of this span  
---|---  
Parent Span ID | ID of the parent span, not set for root span  
Project ID | Google Cloud project ID that ingested the trace  
Start Time | Span start time  
End Time | Span end time  
  
## Span attributes

**Client Version**  
---  
otel.scope.version | String  
**Client Environment**  
gcp.datastore.memory_utilization | double (percentage)  
**Client Connection Properties**  
gcp.datastore.settings.channel.needs_credentials | boolean  
gcp.datastore.settings.channel.needs_endpoint | boolean  
gcp.datastore.settings.channel.needs_headers | boolean  
gcp.datastore.settings.channel.should_auto_close | boolean  
gcp.datastore.settings.channel.transport_name | string Ex. "grpc"  
gcp.datastore.settings.credentials.authentication_type | string Ex. "OAuth2"  
gcp.datastore.settings.host | string Ex. "datastore.googleapis.com:443"  
**Database Properties**  
gcp.datastore.settings.project_id | string  
Google Cloud project ID that contains the Datastore database  
gcp.datastore.settings.database_id | string  
Database external ID (name)  
**Client RPC Retry Settings**  
gcp.datastore.settings.retrySettings.initial_retry_delay | string  
Duration in seconds Ex. 0.01s  
gcp.datastore.settings.retrySettings.initial_rpc_timeout  
gcp.datastore.settings.retrySettings.max_attempts | integer (count)  
gcp.datastore.settings.retrySettings.max_retry_delay | string  
Duration in seconds Ex. 0.1s  
gcp.datastore.settings.retrySettings.max_rpc_timeout  
gcp.datastore.settings.retrySettings.retry_delay_multiplier | double  
gcp.datastore.settings.retrySettings.rpc_timeout_multiplier | double  
gcp.datastore.settings.retrySettings.total_timeout | string  
Duration in seconds  
**OpenTelemetry Configuration**  
otel.scope.name | string Ex. "com.google.cloud.datastore"  
service.name | Sparky  
telemetry.sdk.language | string Ex. "java"  
telemetry.sdk.name | opentelemetry  
telemetry.sdk.version | Ex. 1.29.0  
  
## Logs and events

Client-side traces provide the following logs and events.

### Lookup events

**Event:**  
**"Lookup complete"**  
**"Transaction.Lookup complete"**  
---  
Received | Integer  
Missing | Integer  
Deferred | Integer  
transactional | Boolean  
transaction_id | String  
  
### Commit Events

**Event:**  
**"Commit complete"**  
**"Transaction.Commit complete"**  
---  
doc_count | Integer  
transactional | Boolean  
transaction_id | String  
  
### RunQuery Events

**Event:**  
**"RunQuery complete"**  
**"Transaction.RunQuery complete"**  
---  
doc_count | Integer  
transactional | Boolean  
transaction_id | String  
read_conistencey | `STRONG` or `EVENTUAL`  
more_results | One of: 

  * `NOT_FINISHED`
  * `MORE_RESULTS_AFTER_LIMIT`
  * `MORE_RESULTS_AFTER_CURSOR`
  * `NO_MORE_RESULTS`

  
  
## What's next

  * [Learn how to configure client-side traces](https://docs.cloud.google.com/datastore/docs/client-side-traces)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
