---
url: https://docs.cloud.google.com/database-center/docs/reference/rest/
title: Database Center API \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:27.786626+00:00
---

# Database Center API  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/rest/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  Database Center API Stay organized with collections  Save and categorize content based on your preferences. 

Database Center offers a comprehensive, organization-wide platform for monitoring database fleet health across various products. It simplifies management and reduces risk by automatically aggregating and summarizing key health signals, removing the need for custom dashboards. The platform provides a unified view through its dashboard and API, enabling teams focused on reliability, compliance, security, cost, and administration to quickly identify and address relevant issues within their database fleets.

  * REST Resource: v1beta



## Service: databasecenter.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://databasecenter.googleapis.com/$discovery/rest?version=v1beta>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://databasecenter.googleapis.com`



## REST Resource: [v1beta](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel)

Methods  
---  
`[aggregateFleet](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateFleet)` |  `GET /v1beta:aggregateFleet`   
AggregateFleet provides statistics about the fleet grouped by various fields.  
`[aggregateIssueStats](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/aggregateIssueStats)` |  `POST /v1beta:aggregateIssueStats`   
AggregateIssueStats provides database resource issues statistics.  
`[queryDatabaseResourceGroups](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryDatabaseResourceGroups)` |  `POST /v1beta:queryDatabaseResourceGroups`   
QueryDatabaseResourceGroups returns paginated results of database groups.  
`[queryIssues](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryIssues)` |  `POST /v1beta:queryIssues`   
QueryIssues provides a list of issues and recommendations that a user has access to and that are within the requested scope.  
`[queryProducts](https://docs.cloud.google.com/database-center/docs/reference/rest/v1beta/TopLevel/queryProducts)` |  `GET /v1beta:queryProducts`   
QueryProducts provides a list of all possible products which can be used to filter database resources.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
