---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1
title: Package goog.gdc.logging.v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:13:32.219178+00:00
---

# Package goog.gdc.logging.v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Package goog.gdc.logging.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Logs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.Logs)` (interface)
  * `[ListLabelValuesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLabelValuesRequest)` (message)
  * `[ListLabelValuesResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLabelValuesResponse)` (message)
  * `[ListLabelsRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLabelsRequest)` (message)
  * `[ListLabelsResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLabelsResponse)` (message)
  * `[ListLogsFilter](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLogsFilter)` (message)
  * `[ListLogsRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLogsRequest)` (message)
  * `[ListLogsResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLogsResponse)` (message)
  * `[Log](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.Log)` (message)



## Logs

Provides operations for logs in the time series database.

ListLabelValues  
---  
` rpc ListLabelValues(`[ListLabelValuesRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLabelValuesRequest)`) returns (`[ListLabelValuesResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLabelValuesResponse)`) ` Lists all label values in the time series database that match the request conditions.  
ListLabels  
---  
` rpc ListLabels(`[ListLabelsRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLabelsRequest)`) returns (`[ListLabelsResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLabelsResponse)`) ` Lists all the labels for log streams in the time series database that match the request conditions.  
ListLogs  
---  
` rpc ListLogs(`[ListLogsRequest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLogsRequest)`) returns (`[ListLogsResponse](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLogsResponse)`) ` Lists all logs across all times series that match the request conditions.  
  
## ListLabelValuesRequest

Request message to list all values of a given label.

Fields  
---  
`parent` |  `string` Required. The name of the project from which labels are listed.  
`label` |  `string` Required. The name of the label from which values are listed.  
`page_size` |  `int32` The maximum number of values to return. The service might return fewer values than what this field specifies.If unspecified, at most 100 logs are returned. The maximum value is `1000`. Values above `1000` are limited to `1000`.  
`page_token` |  `string` A page token, received from a previous `ListLabelValues` call. Provide this value to retrieve the subsequent page.When paginating, all other parameters provided to `ListLabelValues` must match the call that provided the page token.  
`start_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The earliest timestamp from which to list labels.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The latest timestamp from which to list labels.  
  
## ListLabelValuesResponse

Response message to list all values of a given label.

Fields  
---  
`values[]` |  `string` A list of all values for the given label.  
`next_page_token` |  `string` A page token, received from a previous `ListLogs` call. Provide this value to retrieve the subsequent page.When paginating, all other parameters provided to `ListLogs` must match the call that provided the page token.  
  
## ListLabelsRequest

Request message to get a list of log stream labels.

Fields  
---  
`parent` |  `string` Required. The project from which to list labels from.  
`page_size` |  `int32` The maximum number of values to return. The service might return fewer than what this field specifies.If unspecified, at most 100 labels are returned. The maximum value is `1000`. Values above `1000` are limited to `1000`.  
`page_token` |  `string` A page token, received from a previous `ListLabels` call. Provide this value to retrieve the subsequent page.When paginating, all other parameters provided to `ListLabels` must match the call that provided the page token.  
`start_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The earliest timestamp from which to list log stream labels.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The latest timestamp from which to list log stream labels.  
  
## ListLabelsResponse

Response message for getting list of log stream labels.

Fields  
---  
`labels[]` |  `string` The labels found in the time series database.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, then no subsequent pages exist.  
  
## ListLogsFilter

Message representing the filtering conditions on which log streams must be returned from the `ListLogs` request.

Fields  
---  
`labels_equal` |  `map<string, string>` The values to which each log stream returned must have the labels set.   
`labels_not_equal` |  `map<string, string>` The values to which each log stream returned must not have the labels set.   
`labels_match_regex` |  `map<string, string>` The regular expression to which each log stream returned must have the labels matched.  
`order_ascending` |  `bool` An indicator determining whether logs must be returned in ascending (oldest first) order.  
`start_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The earliest timestamp from which to start collecting logs.  
`end_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The latest timestamp from which to start collecting logs.  
  
## ListLogsRequest

Request message to list logs in a given log stream.

Fields  
---  
`parent` |  `string` Required. The project from which to list logs.  
`logs_filter` |  ``[ListLogsFilter](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.ListLogsFilter)`` Filter to limit the scope of the logs based on Loki labels and times.  
`page_size` |  `int32` The maximum number of values to return. The service might return fewer values than what this field specifies.If unspecified, at most 100 logs are returned. The maximum value is `1000`. Values above `1000` are limited to `1000`.  
`page_token` |  `string` A page token, received from a previous `ListLogs` call. Provide this value to retrieve the subsequent page.When paginating, all other parameters provided to `ListLogs` must match the call that provided the page token.  
  
## ListLogsResponse

Response method from the `ListLogs` function returning logs that match the request conditions.

Fields  
---  
`logs[]` |  ``[Log](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/logging/v1/goog.gdc.logging.v1#goog.gdc.logging.v1.Log)`` The logs found in the time series database.  
`next_page_token` |  `string` A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, then no subsequent pages exist.  
  
## Log

Message representing one log message.

Fields  
---  
`produced_time` |  ``[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)`` The time at which this log was produced.  
`labels` |  `map<string, string>` The labels associated with the time series this log came from.  
`log` |  `string` The log message, which is a key-value map.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
