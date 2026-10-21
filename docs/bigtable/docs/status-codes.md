---
url: https://docs.cloud.google.com/bigtable/docs/status-codes/
title: Bigtable Status Codes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:36:26.195802+00:00
---

# Bigtable Status Codes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/status-codes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Bigtable Status Codes

## Returned codes

The Cloud Bigtable API (Data API) returns the following gRPC status codes.

**Code** | **Status** | **Category** | **Description**  
---|---|---|---  
  
  1. Not included in the **system error rate** metrics reported on the [ Google Cloud console system insights page](https://docs.cloud.google.com/bigtable/docs/monitoring-instance). 
  2. Not included in the **user error rate** metrics reported on the [ Google Cloud console system insights page](https://docs.cloud.google.com/bigtable/docs/monitoring-instance). 

  
0 | OK | Not an error | Success.  
1 | CANCELLED | System error1 | The operation was cancelled, typically by the caller. An operation that exceeds its deadline may return with a CANCELLED or DEADLINE_EXCEEDED error depending on whether the client library or server cancelled the operation. See the DEADLINE_EXCEEDED description for additional troubleshooting information.   
2 | UNKNOWN | System error | Unknown.  
3 | INVALID_ARGUMENT | User error | The client specified an invalid argument.  
4 | DEADLINE_EXCEEDED | System error1 | The deadline expired before the operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a server could delay a successful response long enough for the deadline to expire.  
5 | NOT_FOUND | User error | Some requested entity was not found.  
6 | ALREADY_EXISTS | User error2 | The entity that a client attempted to create already exists.  
7 | PERMISSION_DENIED | User error | The caller does not have permission to execute the specified operation. This error code _does not_ imply the following: 

  * Request is valid
  * Requested entity exists
  * Request satisfies other pre-conditions

  
8 | RESOURCE_EXHAUSTED | User error | A resource has been exhausted. This can indicate that your application has exhausted a project-level admin API quota, node limit, or node storage limit.   
9 | FAILED PRECONDITION2 | User error | The operation was rejected because the system is not in a state required for the operation's execution. Depending on the circumstance, you might want to retry. For example, you can encounter this error if you attempt to perform operations on a table while it is still being created.  
10 | ABORTED | System error | The operation was aborted, typically due to a concurrency issue, such as a sequencer check failure or transaction abort, or if a read takes too long.  
11 | OUT_OF_RANGE | User error | The operation was attempted past the valid range.  
12 | UNIMPLEMENTED | System error | The operation is not implemented or is not supported/enabled in this service.  
13 | INTERNAL | System error | Internal errors.   
14 | UNAVAILABLE | System error | The service might be down or temporarily overloaded.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
