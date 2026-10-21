---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1
title: Package google.monitoring.prometheus.v1 \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:22.678959+00:00
---

# Package google.monitoring.prometheus.v1  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Package google.monitoring.prometheus.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[PrometheusUpstream](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.PrometheusUpstream)` (interface)
  * `[LabelValuesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.LabelValuesRequest)` (message)
  * `[ListMetricMetadataRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.ListMetricMetadataRequest)` (message)
  * `[QueryExemplarsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.QueryExemplarsRequest)` (message)
  * `[QueryInstantRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.QueryInstantRequest)` (message)
  * `[QueryLabelsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.QueryLabelsRequest)` (message)
  * `[QueryRangeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.QueryRangeRequest)` (message)
  * `[QuerySeriesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.QuerySeriesRequest)` (message)



## PrometheusUpstream

A service that exposes selected endpoints of the HTTP v1 API of the open source Prometheus monitoring system (<https://prometheus.io)>.

The service and its associated types are suffixed with Upstream to later allow for a native protobuf API under the name Prometheus. Since this API only makes sense to expose over JSON over HTTP, end users are never exposed to the service name.

LabelValues  
---  
` rpc LabelValues(`[LabelValuesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.LabelValuesRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.HttpBody)`) ` Lists possible values for a given label name.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListMetricMetadata  
---  
` rpc ListMetricMetadata(`[ListMetricMetadataRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.ListMetricMetadataRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.HttpBody)`) ` Lists metadata for metrics.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
QueryExemplars  
---  
` rpc QueryExemplars(`[QueryExemplarsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.QueryExemplarsRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.HttpBody)`) ` Lists exemplars relevant to a given PromQL query,

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
QueryInstant  
---  
` rpc QueryInstant(`[QueryInstantRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.QueryInstantRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.HttpBody)`) ` Evaluate a PromQL query at a single point in time.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
QueryLabels  
---  
` rpc QueryLabels(`[QueryLabelsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.QueryLabelsRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.HttpBody)`) ` Lists labels for metrics.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
QueryRange  
---  
` rpc QueryRange(`[QueryRangeRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.QueryRangeRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.HttpBody)`) ` Evaluate a PromQL query with [start, end] time range.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
QuerySeries  
---  
` rpc QuerySeries(`[QuerySeriesRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.prometheus.v1#google.monitoring.prometheus.v1.QuerySeriesRequest)`) returns (`[HttpBody](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.HttpBody)`) ` Lists metadata for metrics.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## LabelValuesRequest

LabelValuesRequests holds all parameters of the Prometheus upstream API for querying label values plus GCM-specific parameters.

Fields  
---  
`name` |  `string` Required. The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/[PROJECT_ID_OR_NUMBER].  
`location` |  `string` Location of the resource information. Has to be "global" now.  
`label` |  `string` The label name for which values are queried.  
`start` |  `string` The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.  
`end` |  `string` The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.  
`match` |  `string` A list of matchers encoded in the Prometheus label matcher format to constrain the values to series that satisfy them.  
  
## ListMetricMetadataRequest

ListMetadataRequest holds all parameters of the Prometheus upstream API for querying metric metadata plus GCM-specific parameters.

Fields  
---  
`name` |  `string` Required. The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/[PROJECT_ID_OR_NUMBER].  
`location` |  `string` Location of the resource information. Has to be "global" for now.  
`metric` |  `string` The metric name for which to query metadata. If unset, all metric metadata is returned.  
`limit` |  `int64` Maximum number of metrics to return.  
  
## QueryExemplarsRequest

QueryExemplarsRequest holds all parameters of the Prometheus upstream API for querying exemplars.

Fields  
---  
`name` |  `string` Required. The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/[PROJECT_ID_OR_NUMBER]. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.  
`query` |  `string` A PromQL query string. Query language documentation: <https://prometheus.io/docs/prometheus/latest/querying/basics/>.  
`start` |  `string` The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.  
`end` |  `string` The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.  
`location` |  `string` Location of the resource information. Has to be "global" now.  
  
## QueryInstantRequest

QueryInstantRequest holds all parameters of the Prometheus upstream instant query API plus GCM specific parameters.

Fields  
---  
`name` |  `string` Required. The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/[PROJECT_ID_OR_NUMBER]. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.  
`query` |  `string` A PromQL query string. Query language documentation: <https://prometheus.io/docs/prometheus/latest/querying/basics/>.  
`time` |  `string` The single point in time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.  
`timeout` |  `string` An upper bound timeout for the query. Either a Prometheus duration string (<https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations>) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.  
`location` |  `string` Location of the resource information. Has to be "global" now.  
  
## QueryLabelsRequest

QueryLabelsRequest holds all parameters of the Prometheus upstream API for returning a list of label names.

Fields  
---  
`name` |  `string` Required. The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/[PROJECT_ID_OR_NUMBER].  
`location` |  `string` Location of the resource information. Has to be "global" now.  
`start` |  `string` The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.  
`end` |  `string` The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.  
`match` |  `string` A list of matchers encoded in the Prometheus label matcher format to constrain the values to series that satisfy them.  
  
## QueryRangeRequest

QueryRangeRequest holds all parameters of the Prometheus upstream range query API plus GCM specific parameters.

Fields  
---  
`name` |  `string` Required. The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/[PROJECT_ID_OR_NUMBER]. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.  
`query` |  `string` A PromQL query string. Query language documentation: <https://prometheus.io/docs/prometheus/latest/querying/basics/>.  
`start` |  `string` The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.  
`end` |  `string` The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.  
`step` |  `string` The resolution of query result. Either a Prometheus duration string (<https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations>) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.  
`timeout` |  `string` An upper bound timeout for the query. Either a Prometheus duration string (<https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations>) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.  
`location` |  `string` Location of the resource information. Has to be "global" now.  
  
## QuerySeriesRequest

QuerySeries holds all parameters of the Prometheus upstream API for querying series.

Fields  
---  
`name` |  `string` Required. The workspace on which to execute the request. It is not part of the open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine. The format is: projects/[PROJECT_ID_OR_NUMBER].  
`location` |  `string` Location of the resource information. Has to be "global" for now.  
`start` |  `string` The start time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.  
`end` |  `string` The end time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
