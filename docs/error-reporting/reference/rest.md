---
url: https://docs.cloud.google.com/error-reporting/reference/rest/
title: Error Reporting API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:29:10.580196+00:00
---

# Error Reporting API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  Error Reporting API Stay organized with collections  Save and categorize content based on your preferences. 

Groups and counts similar errors from cloud services and applications, reports new errors, and provides access to error groups and their associated errors.

  * REST Resource: v1beta1.projects
  * REST Resource: v1beta1.projects.events
  * REST Resource: v1beta1.projects.groupStats
  * REST Resource: v1beta1.projects.groups
  * REST Resource: v1beta1.projects.locations
  * REST Resource: v1beta1.projects.locations.events
  * REST Resource: v1beta1.projects.locations.groupStats
  * REST Resource: v1beta1.projects.locations.groups



## Service: clouderrorreporting.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://clouderrorreporting.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://clouderrorreporting.googleapis.com`



### Regional service endpoint

A regional service endpoint is a base URL that specifies the network address of an API service in a single region. A service that is available in multiple regions might have multiple regional endpoints. Select a location to see its regional service endpoint for this service. 

global us africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 asia-southeast3 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-north2 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 northamerica-south1 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4

  

* `https://clouderrorreporting.googleapis.com`

## REST Resource: [v1beta1.projects](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects)

Methods  
---  
`[deleteEvents](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects/deleteEvents)` |  `DELETE /v1beta1/{projectName=projects/*}/events`   
Deletes all error events of a given project.  
  
## REST Resource: [v1beta1.projects.events](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events)

Methods  
---  
`[list](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/list)` |  `GET /v1beta1/{projectName=projects/*}/events`   
Lists the specified events.  
`[report](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report)` |  `POST /v1beta1/{projectName=projects/*}/events:report`   
Report an individual error event and record the event to a log.  
  
## REST Resource: [v1beta1.projects.groupStats](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groupStats)

Methods  
---  
`[list](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groupStats/list)` |  `GET /v1beta1/{projectName=projects/*}/groupStats`   
Lists the specified groups.  
  
## REST Resource: [v1beta1.projects.groups](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups)

Methods  
---  
`[get](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups/get)` |  `GET /v1beta1/{groupName=projects/*/groups/*}`   
Get the specified group.  
`[update](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.groups/update)` |  `PUT /v1beta1/{group.name=projects/*/groups/*}`   
Replace the data for the specified group.  
  
## REST Resource: [v1beta1.projects.locations](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.locations)

Methods  
---  
`[deleteEvents](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.locations/deleteEvents)` |  `DELETE /v1beta1/{projectName=projects/*/locations/*}/events`   
Deletes all error events of a given project.  
  
## REST Resource: [v1beta1.projects.locations.events](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.locations.events)

Methods  
---  
`[list](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.locations.events/list)` |  `GET /v1beta1/{projectName=projects/*/locations/*}/events`   
Lists the specified events.  
  
## REST Resource: [v1beta1.projects.locations.groupStats](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.locations.groupStats)

Methods  
---  
`[list](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.locations.groupStats/list)` |  `GET /v1beta1/{projectName=projects/*/locations/*}/groupStats`   
Lists the specified groups.  
  
## REST Resource: [v1beta1.projects.locations.groups](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.locations.groups)

Methods  
---  
`[get](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.locations.groups/get)` |  `GET /v1beta1/{groupName=projects/*/locations/*/groups/*}`   
Get the specified group.  
`[update](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.locations.groups/update)` |  `PUT /v1beta1/{group.name=projects/*/locations/*/groups/*}`   
Replace the data for the specified group.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-28 UTC."],[],[]] 
