---
url: https://docs.cloud.google.com/spanner/docs/audit-logging-request-latency-guide/
title: Calculate Spanner streaming and partition request latency \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:28.575914+00:00
---

# Calculate Spanner streaming and partition request latency  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/audit-logging-request-latency-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Calculate Spanner streaming and partition request latency Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can calculate the Spanner API request latency of streaming and partition requests.

You can calculate Spanner API streaming and partition request latencies with the fields in the `metadata` struct object of an [`AuditLog`](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog). The metadata is of type `QueryPerformanceMetadata`. For streaming and partition requests, the `metadata` does not contain a `processingSecondsDuration` field. For information on how to use `processingSecondsDuration` to calculate request latencies for all other request types, see [Processing duration](https://docs.cloud.google.com/spanner/docs/audit-logging#processing-duration).

## Request latencies for streaming requests

When a client sends a [streaming request](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeStreamingSql) and as the Spanner API returns partial result sets, [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) records audit logs for the first and last responses. The request latency for a streaming request is the time elapsed between when the Spanner API receives the request and when the client receives the last response.

### Recognize streaming requests audit log entries

To calculate the request latency of a streaming request, you need to identify the log entries related to the request. The log entries have the `protoPayload.methodName` set to either `google.spanner.v1.Spanner.ExecuteStreamingSql` or `google.spanner.v1.Spanner.StreamingRead`. For each streaming request, there are two log entries, which are grouped by `operation.id`. The first entry has `operation.first` set to `true` and the last entry has `operation.last` set to `true`. The `protoPayload.metadata.responseTimestamp` object is also populated.

### Calculate request latency for streaming requests

To calculate the request latency of a streaming request, filter the audit logs by `operation.id`. The difference between the latest `protoPayload.metadata.responseTimestamp` and the earliest `protoPayload.requestMetadata.requestAttributes.time` is the request latency.

### Sample audit logs for streaming requests

To find all log entries for a streaming request, run the following query in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), replacing the OPERATION_ID variable with the desired value:
    
    
    operation.id="OPERATION_ID"
    

The following example finds log entries for a streaming request with the `operation.id` of `15327696495839874591`:
    
    
    operation.id="15327696495839874591"
    

#### Returned first log
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {...},
        "requestMetadata": {
          "requestAttributes": {
            **"time" : "2023-02-27T16:57:40.552952297Z",**
          },
          "destinationAttributes": {}
        },
        "serviceName": "spanner.googleapis.com",
        "methodName": "google.spanner.v1.Spanner.ExecuteStreamingSql",
        "authorizationInfo": [{...}],
        "resourceName": "projects/example-project/instances/example-instance/databases/example-database/sessions/example-session",
        "request": {
          "session": "projects/example-project/instances/example-instance/databases/example-database/sessions/example-session",
          "requestOptions": {},
          "sql": "SELECT COUNT(*) as count FROM Example_table WHERE Example_Column > @timestamp",
          "@type": "type.googleapis.com/google.spanner.v1.ExecuteSqlRequest",
          "queryOptions": {}
        },
        **"metadata" : {
          "@type": "type.googleapis.com/spanner.cloud.instance_v1.QueryPerformanceMetadata",
          "responseTimestamp": "2023-02-27T16:57:40.555730699Z"
        }**
      },
      "insertId": "h7fj0jei6597",
      "resource": {...},
      "timestamp": "2023-02-27T16:57:40.552391554Z",
      "severity": "INFO",
      "logName": "projects/example-project/logs/cloudaudit.googleapis.com%2Fdata_access",
      "operation": {
        **"id" : "15327696495839874591",**
        "producer": "spanner.googleapis.com",
        "first": true
      },
      "receiveTimestamp": "2023-02-27T16:57:41.507770020Z"
    }
    

#### Returned last log
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {...},
        "requestMetadata": {
          "requestAttributes": {
            **"time" : "2023-02-27T16:57:40.552952297Z",**
          },
          "destinationAttributes": {}
        },
        "serviceName": "spanner.googleapis.com",
        "methodName": "google.spanner.v1.Spanner.ExecuteStreamingSql",
        "authorizationInfo": [{...}],
        "resourceName": "projects/example-project/instances/example-instance/databases/example-database/sessions/example-session",
       **** "metadata": {
          "responseTimestamp": "2023-02-27T16:57:40.556138125Z",
          "@type": "type.googleapis.com/spanner.cloud.instance_v1.QueryPerformanceMetadata"
        }
      },
      "insertId": "h7fj0jei6598",
      "resource": {...},
      "timestamp": "2023-02-27T16:57:40.552391554Z",
      "severity": "INFO",
      "logName": "projects/example-project/logs/cloudaudit.googleapis.com%2Fdata_access",
      "operation": {
        **"id" : "15327696495839874591",**
        "producer": "spanner.googleapis.com",
        "last": true
      },
      "receiveTimestamp": "2023-02-27T16:57:41.507770020Z"
    }
    

The request latency is the latest `metadata.responseTimestamp` minus the earliest `requestAttributes.time`. The result is 2023-02-27T16:57:40.556138125Z-2023-02 - 2023-02-27T16:57:40.552952297Z, which equals 0.003185828 seconds.

## Request latencies for partition requests

When a client sends a [partitioned request](https://docs.cloud.google.com/spanner/docs/dml-partitioned), Spanner creates multiple audit logs. To calculate the request latency of an end-to-end partition request and subsequent calls to the partitions, identify the audit logs associated with the parent request.

### Recognize partition requests audit log entries

When you make a `PartitionRead` or a `PartitionQuery` request, a set of partitions are returned in the [`PartitionResponse`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartitionResponse). As you make `Read`, `ExecuteSql` or `ExecuteStreaming` calls respectively for each partition, Spanner records audit logs for these methods. Each of these logs contains an identifier to group them together, called `protoPayload.metadata.partitionBatchIdentifier`. The `protoPayload.metadata.responseTimestamp` object is also populated.

### Calculate request latency for partition requests

To calculate the request latency of a partition request, you can filter the audit logs by `metadata.partitionBatchIdentifier`. The difference between the latest `metadata.responseTimestamp` and the earliest `protoPayload.requestMetadata.requestAttributes.time` is the request latency.

### Sample audit logs for partition requests

To find all log entries for a partition request, run the following query in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), replacing the PARTITION_BATCH_ID variable with the desired value:
    
    
    metadata.partitionBatchIdentifier="PARTITION_BATCH_ID"
    

The following example finds log entries for a partition request with the `metadata.partitionBatchIdentifier` of `15327696495839874591`:
    
    
    metadata.partitionBatchIdentifier="15327696495839874591"
    

#### Returned first log
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {...},
        "requestMetadata": {
          "requestAttributes": {
            **"time" : "2023-02-15T18:13:39.341584693Z",**
            },
        },
        "serviceName": "spanner.googleapis.com",
        "methodName": "google.spanner.v1.Spanner.ExecuteStreamingSql",
        "authorizationInfo": [{...}],
        "resourceName": "projects/example-project/instances/example-instance/databases/example-db/sessions/example-session",
        "request": {...},
        **"metadata" : {
          "@type": "type.googleapis.com/spanner.cloud.instance_v1.QueryPerformanceMetadata",
          "partitionBatchIdentifier": "4841471066190013455",
          "responseTimestamp": "2023-02-15T18:13:39.343693061Z"
        }**
      },
      "insertId": "4fug42dqke5",
      "resource": {...},
      "timestamp": "2023-02-15T18:13:39.341069413Z",
      "severity": "INFO",
      "logName": "projects/example-project/logs/cloudaudit.googleapis.com%2Fdata_access",
      "operation": {...},
      "receiveTimestamp": "2023-02-15T18:13:39.983812511Z"
    }
    
    

#### Returned second log
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {...},
        "requestMetadata": {
          "requestAttributes": {
            **"time" : "2023-02-15T18:13:39.341584693Z",**
            },
          },
        "serviceName": "spanner.googleapis.com",
        "methodName": "google.spanner.v1.Spanner.ExecuteStreamingSql",
        "authorizationInfo": [{...}],
        "resourceName": "projects/example-project/instances/example-instance/databases/example-db/sessions/example-session",
        **"metadata" : {
          "responseTimestamp": "2023-02-15T18:13:39.344256101Z",
          "partitionBatchIdentifier": "4841471066190013455",
          "@type": "type.googleapis.com/spanner.cloud.instance_v1.QueryPerformanceMetadata"
        }**
      },
      "insertId": "4fug42dqke6",
      "resource": {...},
      "timestamp": "2023-02-15T18:13:39.341069413Z",
      "severity": "INFO",
      "logName": "projects/example-project/logs/cloudaudit.googleapis.com%2Fdata_access",
      "operation": {...},
      "receiveTimestamp": "2023-02-15T18:13:39.983812511Z"
    }
    

Depending on the number of partitions, Spanner might record more logs than in this example.

#### Returned last log
    
    
    {
      "protoPayload": {
        "@type": "type.googleapis.com/google.cloud.audit.AuditLog",
        "authenticationInfo": {...},
        "requestMetadata": {
          "requestAttributes": {
            **"time" : "2023-02-15T18:13:39.439207331Z",**
            },
        },
        "serviceName": "spanner.googleapis.com",
        "methodName": "google.spanner.v1.Spanner.ExecuteStreamingSql",
        "authorizationInfo": [{...}],
        "resourceName": "projects/example-project/instances/example-instance/databases/example-db/sessions/example-session",
        **"metadata" : {
          "partitionBatchIdentifier": "4841471066190013455",
          "@type": "type.googleapis.com/spanner.cloud.instance_v1.QueryPerformanceMetadata",
          "responseTimestamp": "2023-02-15T18:13:39.441692339Z"
        }**
      },
      "insertId": "4fug42dqkec",
      "resource": {...},
      "timestamp": "2023-02-15T18:13:39.438607931Z",
      "severity": "INFO",
      "logName": "projects/example-project/logs/cloudaudit.googleapis.com%2Fdata_access",
      "operation": {...},
      "receiveTimestamp": "2023-02-15T18:13:39.983812511Z"
    }
    

The request latency is the latest `metadata.responseTimestamp` minus the earliest `requestAttributes.time`. The result is 2023-02-15T18:13:39.441692339Z \- 2023-02-15T18:13:39.341584693Z, which equals 0.100107646 seconds.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
