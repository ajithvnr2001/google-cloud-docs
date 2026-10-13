---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.OperationOrBuilder
title: Interface OperationOrBuilder (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:43:18.598977+00:00
---

# Interface OperationOrBuilder (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.OperationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface OperationOrBuilder (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.1.10 
    
    
    public interface OperationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Labels describing the operation. Only the following labels are allowed:

  * Labels describing monitored resources as defined in the service configuration.
  * Default labels of metric values. When specified, labels defined in the metric value override these default.
  * The following labels defined by Google Cloud Platform:
  * `cloud.googleapis.com/location` describing the location where the operation happened,
  * `servicecontrol.googleapis.com/user_agent` describing the user agent of the API request,
  * `servicecontrol.googleapis.com/service_agent` describing the service used to handle the API request (e.g. ESP),
  * `servicecontrol.googleapis.com/platform` describing the platform where the API is served, such as App Engine, Compute Engine, or Kubernetes Engine.



`map<string, string> labels = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### containsUserLabels(String key)
    
    
    public abstract boolean containsUserLabels(String key)

Private Preview. This feature is only available for approved services.

User defined labels for the resource that this operation is associated with.

`map<string, string> user_labels = 12;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getConsumerId()
    
    
    public abstract String getConsumerId()

Identity of the consumer who is using the service. This field should be filled in for the operations initiated by a consumer, but not for service-initiated operations that are not related to a specific consumer.

  * This can be in one of the following formats:
  * project:PROJECT_ID,
  * project`_`number:PROJECT_NUMBER,
  * projects/PROJECT_ID or PROJECT_NUMBER,
  * folders/FOLDER_NUMBER,
  * organizations/ORGANIZATION_NUMBER,
  * api`_`key:API_KEY.



`string consumer_id = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The consumerId.  
  
### getConsumerIdBytes()
    
    
    public abstract ByteString getConsumerIdBytes()

Identity of the consumer who is using the service. This field should be filled in for the operations initiated by a consumer, but not for service-initiated operations that are not related to a specific consumer.

  * This can be in one of the following formats:
  * project:PROJECT_ID,
  * project`_`number:PROJECT_NUMBER,
  * projects/PROJECT_ID or PROJECT_NUMBER,
  * folders/FOLDER_NUMBER,
  * organizations/ORGANIZATION_NUMBER,
  * api`_`key:API_KEY.



`string consumer_id = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for consumerId.  
  
### getEndTime()
    
    
    public abstract Timestamp getEndTime()

End time of the operation. Required when the operation is used in ServiceController.Report, but optional when the operation is used in ServiceController.Check.

`.google.protobuf.Timestamp end_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The endTime.  
  
### getEndTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getEndTimeOrBuilder()

End time of the operation. Required when the operation is used in ServiceController.Report, but optional when the operation is used in ServiceController.Check.

`.google.protobuf.Timestamp end_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getExtensions(int index)
    
    
    public abstract Any getExtensions(int index)

Unimplemented.

`repeated .google.protobuf.Any extensions = 16;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Any](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Any.html)` |   
  
### getExtensionsCount()
    
    
    public abstract int getExtensionsCount()

Unimplemented.

`repeated .google.protobuf.Any extensions = 16;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExtensionsList()
    
    
    public abstract List<Any> getExtensionsList()

Unimplemented.

`repeated .google.protobuf.Any extensions = 16;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Any](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Any.html)>` |   
  
### getExtensionsOrBuilder(int index)
    
    
    public abstract AnyOrBuilder getExtensionsOrBuilder(int index)

Unimplemented.

`repeated .google.protobuf.Any extensions = 16;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AnyOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AnyOrBuilder.html)` |   
  
### getExtensionsOrBuilderList()
    
    
    public abstract List<? extends AnyOrBuilder> getExtensionsOrBuilderList()

Unimplemented.

`repeated .google.protobuf.Any extensions = 16;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.protobuf.AnyOrBuilder>` |   
  
### getImportance()
    
    
    public abstract Operation.Importance getImportance()

DO NOT USE. This is an experimental field.

`.google.api.servicecontrol.v1.Operation.Importance importance = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Operation.Importance](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.Operation.Importance)` | The importance.  
  
### getImportanceValue()
    
    
    public abstract int getImportanceValue()

DO NOT USE. This is an experimental field.

`.google.api.servicecontrol.v1.Operation.Importance importance = 11;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for importance.  
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.OperationOrBuilder#com_google_api_servicecontrol_v1_OperationOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Labels describing the operation. Only the following labels are allowed:

  * Labels describing monitored resources as defined in the service configuration.
  * Default labels of metric values. When specified, labels defined in the metric value override these default.
  * The following labels defined by Google Cloud Platform:
  * `cloud.googleapis.com/location` describing the location where the operation happened,
  * `servicecontrol.googleapis.com/user_agent` describing the user agent of the API request,
  * `servicecontrol.googleapis.com/service_agent` describing the service used to handle the API request (e.g. ESP),
  * `servicecontrol.googleapis.com/platform` describing the platform where the API is served, such as App Engine, Compute Engine, or Kubernetes Engine.



`map<string, string> labels = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Labels describing the operation. Only the following labels are allowed:

  * Labels describing monitored resources as defined in the service configuration.
  * Default labels of metric values. When specified, labels defined in the metric value override these default.
  * The following labels defined by Google Cloud Platform:
  * `cloud.googleapis.com/location` describing the location where the operation happened,
  * `servicecontrol.googleapis.com/user_agent` describing the user agent of the API request,
  * `servicecontrol.googleapis.com/service_agent` describing the service used to handle the API request (e.g. ESP),
  * `servicecontrol.googleapis.com/platform` describing the platform where the API is served, such as App Engine, Compute Engine, or Kubernetes Engine.



`map<string, string> labels = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Labels describing the operation. Only the following labels are allowed:

  * Labels describing monitored resources as defined in the service configuration.
  * Default labels of metric values. When specified, labels defined in the metric value override these default.
  * The following labels defined by Google Cloud Platform:
  * `cloud.googleapis.com/location` describing the location where the operation happened,
  * `servicecontrol.googleapis.com/user_agent` describing the user agent of the API request,
  * `servicecontrol.googleapis.com/service_agent` describing the service used to handle the API request (e.g. ESP),
  * `servicecontrol.googleapis.com/platform` describing the platform where the API is served, such as App Engine, Compute Engine, or Kubernetes Engine.



`map<string, string> labels = 6;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Labels describing the operation. Only the following labels are allowed:

  * Labels describing monitored resources as defined in the service configuration.
  * Default labels of metric values. When specified, labels defined in the metric value override these default.
  * The following labels defined by Google Cloud Platform:
  * `cloud.googleapis.com/location` describing the location where the operation happened,
  * `servicecontrol.googleapis.com/user_agent` describing the user agent of the API request,
  * `servicecontrol.googleapis.com/service_agent` describing the service used to handle the API request (e.g. ESP),
  * `servicecontrol.googleapis.com/platform` describing the platform where the API is served, such as App Engine, Compute Engine, or Kubernetes Engine.



`map<string, string> labels = 6;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLogEntries(int index)
    
    
    public abstract LogEntry getLogEntries(int index)

Represents information to be logged.

`repeated .google.api.servicecontrol.v1.LogEntry log_entries = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.LogEntry)` |   
  
### getLogEntriesCount()
    
    
    public abstract int getLogEntriesCount()

Represents information to be logged.

`repeated .google.api.servicecontrol.v1.LogEntry log_entries = 8;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLogEntriesList()
    
    
    public abstract List<LogEntry> getLogEntriesList()

Represents information to be logged.

`repeated .google.api.servicecontrol.v1.LogEntry log_entries = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.LogEntry)>` |   
  
### getLogEntriesOrBuilder(int index)
    
    
    public abstract LogEntryOrBuilder getLogEntriesOrBuilder(int index)

Represents information to be logged.

`repeated .google.api.servicecontrol.v1.LogEntry log_entries = 8;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogEntryOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.LogEntryOrBuilder)` |   
  
### getLogEntriesOrBuilderList()
    
    
    public abstract List<? extends LogEntryOrBuilder> getLogEntriesOrBuilderList()

Represents information to be logged.

`repeated .google.api.servicecontrol.v1.LogEntry log_entries = 8;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.api.servicecontrol.v1.LogEntryOrBuilder>` |   
  
### getMetricValueSets(int index)
    
    
    public abstract MetricValueSet getMetricValueSets(int index)

Represents information about this operation. Each MetricValueSet corresponds to a metric defined in the service configuration. The data type used in the MetricValueSet must agree with the data type specified in the metric definition.

Within a single operation, it is not allowed to have more than one MetricValue instances that have the same metric names and identical label value combinations. If a request has such duplicated MetricValue instances, the entire request is rejected with an invalid argument error.

`repeated .google.api.servicecontrol.v1.MetricValueSet metric_value_sets = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricValueSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.MetricValueSet)` |   
  
### getMetricValueSetsCount()
    
    
    public abstract int getMetricValueSetsCount()

Represents information about this operation. Each MetricValueSet corresponds to a metric defined in the service configuration. The data type used in the MetricValueSet must agree with the data type specified in the metric definition.

Within a single operation, it is not allowed to have more than one MetricValue instances that have the same metric names and identical label value combinations. If a request has such duplicated MetricValue instances, the entire request is rejected with an invalid argument error.

`repeated .google.api.servicecontrol.v1.MetricValueSet metric_value_sets = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetricValueSetsList()
    
    
    public abstract List<MetricValueSet> getMetricValueSetsList()

Represents information about this operation. Each MetricValueSet corresponds to a metric defined in the service configuration. The data type used in the MetricValueSet must agree with the data type specified in the metric definition.

Within a single operation, it is not allowed to have more than one MetricValue instances that have the same metric names and identical label value combinations. If a request has such duplicated MetricValue instances, the entire request is rejected with an invalid argument error.

`repeated .google.api.servicecontrol.v1.MetricValueSet metric_value_sets = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MetricValueSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.MetricValueSet)>` |   
  
### getMetricValueSetsOrBuilder(int index)
    
    
    public abstract MetricValueSetOrBuilder getMetricValueSetsOrBuilder(int index)

Represents information about this operation. Each MetricValueSet corresponds to a metric defined in the service configuration. The data type used in the MetricValueSet must agree with the data type specified in the metric definition.

Within a single operation, it is not allowed to have more than one MetricValue instances that have the same metric names and identical label value combinations. If a request has such duplicated MetricValue instances, the entire request is rejected with an invalid argument error.

`repeated .google.api.servicecontrol.v1.MetricValueSet metric_value_sets = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MetricValueSetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.MetricValueSetOrBuilder)` |   
  
### getMetricValueSetsOrBuilderList()
    
    
    public abstract List<? extends MetricValueSetOrBuilder> getMetricValueSetsOrBuilderList()

Represents information about this operation. Each MetricValueSet corresponds to a metric defined in the service configuration. The data type used in the MetricValueSet must agree with the data type specified in the metric definition.

Within a single operation, it is not allowed to have more than one MetricValue instances that have the same metric names and identical label value combinations. If a request has such duplicated MetricValue instances, the entire request is rejected with an invalid argument error.

`repeated .google.api.servicecontrol.v1.MetricValueSet metric_value_sets = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.api.servicecontrol.v1.MetricValueSetOrBuilder>` |   
  
### getOperationId()
    
    
    public abstract String getOperationId()

Identity of the operation. This must be unique within the scope of the service that generated the operation. If the service calls Check() and Report() on the same operation, the two calls should carry the same id.

UUID version 4 is recommended, though not required. In scenarios where an operation is computed from existing information and an idempotent id is desirable for deduplication purpose, UUID version 5 is recommended. See RFC 4122 for details.

`string operation_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The operationId.  
  
### getOperationIdBytes()
    
    
    public abstract ByteString getOperationIdBytes()

Identity of the operation. This must be unique within the scope of the service that generated the operation. If the service calls Check() and Report() on the same operation, the two calls should carry the same id.

UUID version 4 is recommended, though not required. In scenarios where an operation is computed from existing information and an idempotent id is desirable for deduplication purpose, UUID version 5 is recommended. See RFC 4122 for details.

`string operation_id = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for operationId.  
  
### getOperationName()
    
    
    public abstract String getOperationName()

Fully qualified name of the operation. Reserved for future use.

`string operation_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The operationName.  
  
### getOperationNameBytes()
    
    
    public abstract ByteString getOperationNameBytes()

Fully qualified name of the operation. Reserved for future use.

`string operation_name = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for operationName.  
  
### getStartTime()
    
    
    public abstract Timestamp getStartTime()

Required. Start time of the operation.

`.google.protobuf.Timestamp start_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The startTime.  
  
### getStartTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getStartTimeOrBuilder()

Required. Start time of the operation.

`.google.protobuf.Timestamp start_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getUserLabels() (deprecated)
    
    
    public abstract Map<String,String> getUserLabels()

Use [#getUserLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-service-control/latest/com.google.api.servicecontrol.v1.OperationOrBuilder#com_google_api_servicecontrol_v1_OperationOrBuilder_getUserLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getUserLabelsCount()
    
    
    public abstract int getUserLabelsCount()

Private Preview. This feature is only available for approved services.

User defined labels for the resource that this operation is associated with.

`map<string, string> user_labels = 12;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getUserLabelsMap()
    
    
    public abstract Map<String,String> getUserLabelsMap()

Private Preview. This feature is only available for approved services.

User defined labels for the resource that this operation is associated with.

`map<string, string> user_labels = 12;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getUserLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getUserLabelsOrDefault(String key, String defaultValue)

Private Preview. This feature is only available for approved services.

User defined labels for the resource that this operation is associated with.

`map<string, string> user_labels = 12;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getUserLabelsOrThrow(String key)
    
    
    public abstract String getUserLabelsOrThrow(String key)

Private Preview. This feature is only available for approved services.

User defined labels for the resource that this operation is associated with.

`map<string, string> user_labels = 12;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### hasEndTime()
    
    
    public abstract boolean hasEndTime()

End time of the operation. Required when the operation is used in ServiceController.Report, but optional when the operation is used in ServiceController.Check.

`.google.protobuf.Timestamp end_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endTime field is set.  
  
### hasStartTime()
    
    
    public abstract boolean hasStartTime()

Required. Start time of the operation.

`.google.protobuf.Timestamp start_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
