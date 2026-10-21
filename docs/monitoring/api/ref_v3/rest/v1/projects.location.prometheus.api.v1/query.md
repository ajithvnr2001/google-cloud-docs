---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1/query/
title: Method: projects.location.prometheus.api.v1.query \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:20.216595+00:00
---

# Method: projects.location.prometheus.api.v1.query  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/projects.location.prometheus.api.v1/query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: projects.location.prometheus.api.v1.query Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Evaluate a PromQL query at a single point in time.

### HTTP request

`GET https://monitoring.googleapis.com/v1/{name}/location/{location}/prometheus/api/v1/query`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The project on which to execute the request. Data associcated with the project's workspace stored under the The format is: projects/[PROJECT_ID_OR_NUMBER]. Open source API but used as a request path prefix to distinguish different virtual Prometheus instances of Google Prometheus Engine.  
`location` |  `string` Location of the resource information. Has to be "global" now.  
  
### Query parameters

Parameters  
---  
`query` |  `string` A PromQL query string. Query language documentation: <https://prometheus.io/docs/prometheus/latest/querying/basics/>.  
`time` |  `string` The single point in time to evaluate the query for. Either floating point UNIX seconds or RFC3339 formatted timestamp.  
`timeout` |  `string` An upper bound timeout for the query. Either a Prometheus duration string (<https://prometheus.io/docs/prometheus/latest/querying/basics/#time-durations>) or floating point seconds. This non-standard encoding must be used for compatibility with the open source API. Clients may still implement timeouts at the connection level while ignoring this field.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response is a generic HTTP response whose format is defined by the method.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
