---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes/listMetricsScopesByMonitoredProject/
title: Method: locations.global.metricsScopes.listMetricsScopesByMonitoredProject \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:19.828507+00:00
---

# Method: locations.global.metricsScopes.listMetricsScopesByMonitoredProject  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes/listMetricsScopesByMonitoredProject/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Method: locations.global.metricsScopes.listMetricsScopesByMonitoredProject Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Returns a list of every `Metrics Scope` that a specific `MonitoredProject` has been added to. The metrics scope representing the specified monitored project will always be the first entry in the response.

### HTTP request

`GET https://monitoring.googleapis.com/v1/locations/global/metricsScopes:listMetricsScopesByMonitoredProject`

### Query parameters

Parameters  
---  
`monitoredResourceContainer` |  `string` Required. The resource name of the `Monitored Project` being requested. Example: `projects/{MONITORED_PROJECT_ID_OR_NUMBER}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `monitoredResourceContainer`:

  * `resourcemanager.projects.get`

  
  
### Request body

The request body must be empty.

### Response body

Response for the `metricsScopes.listMetricsScopesByMonitoredProject` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "metricsScopes": [
        {
          object ([MetricsScope](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes#MetricsScope))
        }
      ]
    }  
  
Fields  
---  
`metricsScopes[]` |  `object (`[MetricsScope](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v1/locations.global.metricsScopes#MetricsScope)`)` A set of all metrics scopes that the specified monitored project has been added to.  
  
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
