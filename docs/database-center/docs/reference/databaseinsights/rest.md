---
url: https://docs.cloud.google.com/database-center/docs/reference/databaseinsights/rest/
title: Database Insights API \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:30.867539+00:00
---

# Database Insights API  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/databaseinsights/rest/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  Database Insights API Stay organized with collections  Save and categorize content based on your preferences. 

Database Insights API is a regional service that provides deep performance diagnostics and monitoring for cloud databases. It exposes tools like Query Insights, which helps you detect, diagnose, and prevent query performance problems, and System Insights, which provides comprehensive telemetry and monitoring for system-level instance metrics.

## Service: databaseinsights.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://databaseinsights.googleapis.com/$discovery/rest?version=v1beta>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://databaseinsights.googleapis.com`



## REST Resource: [v1beta.projects.locations.queryMetrics](https://docs.cloud.google.com/database-center/docs/reference/databaseinsights/rest/v1beta/projects.locations.queryMetrics)

Methods  
---  
`[fetch](https://docs.cloud.google.com/database-center/docs/reference/databaseinsights/rest/v1beta/projects.locations.queryMetrics/fetch)` |  `POST /v1beta/{parent=projects/*/locations/*}/queryMetrics:fetch`   
FetchQueryMetrics fetches the given database query level metrics.  
  
## REST Resource: [v1beta.projects.locations.systemMetrics](https://docs.cloud.google.com/database-center/docs/reference/databaseinsights/rest/v1beta/projects.locations.systemMetrics)

Methods  
---  
`[fetch](https://docs.cloud.google.com/database-center/docs/reference/databaseinsights/rest/v1beta/projects.locations.systemMetrics/fetch)` |  `POST /v1beta/{parent=projects/*/locations/*}/systemMetrics:fetch`   
FetchSystemMetrics fetches the given system level metrics.  
  
## REST Resource: [v1beta.projects.locations.virtualDbxAgent](https://docs.cloud.google.com/database-center/docs/reference/databaseinsights/rest/v1beta/projects.locations.virtualDbxAgent)

Methods  
---  
`[query](https://docs.cloud.google.com/database-center/docs/reference/databaseinsights/rest/v1beta/projects.locations.virtualDbxAgent/query)` |  `POST /v1beta/{parent=projects/*/locations/*}/virtualDbxAgent:query`   
RunAgent runs the agent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
