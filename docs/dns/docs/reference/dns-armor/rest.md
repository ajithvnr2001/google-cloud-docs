---
url: https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/
title: Network Security API \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:32.422090+00:00
---

# Network Security API  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  Network Security API Stay organized with collections  Save and categorize content based on your preferences. 

## Service: networksecurity.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://networksecurity.googleapis.com/$discovery/rest?version=v1>
  * <https://networksecurity.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://networksecurity.googleapis.com`



## REST Resource: [v1beta1.projects.locations.dnsThreatDetectors](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1beta1/projects.locations.dnsThreatDetectors)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1beta1/projects.locations.dnsThreatDetectors/create)` |  `POST /v1beta1/{parent=projects/*/locations/*}/dnsThreatDetectors`   
Creates a new DnsThreatDetector in a given project and location.  
`[delete](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1beta1/projects.locations.dnsThreatDetectors/delete)` |  `DELETE /v1beta1/{name=projects/*/locations/*/dnsThreatDetectors/*}`   
Deletes a single DnsThreatDetector.  
`[get](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1beta1/projects.locations.dnsThreatDetectors/get)` |  `GET /v1beta1/{name=projects/*/locations/*/dnsThreatDetectors/*}`   
Gets the details of a single DnsThreatDetector.  
`[list](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1beta1/projects.locations.dnsThreatDetectors/list)` |  `GET /v1beta1/{parent=projects/*/locations/*}/dnsThreatDetectors`   
Lists DnsThreatDetectors in a given project and location.  
`[patch](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1beta1/projects.locations.dnsThreatDetectors/patch)` |  `PATCH /v1beta1/{dnsThreatDetector.name=projects/*/locations/*/dnsThreatDetectors/*}`   
Updates a single DnsThreatDetector.  
  
## REST Resource: [v1.projects.locations.dnsThreatDetectors](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors/create)` |  `POST /v1/{parent=projects/*/locations/*}/dnsThreatDetectors`   
Creates a new DnsThreatDetector in a given project and location.  
`[delete](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors/delete)` |  `DELETE /v1/{name=projects/*/locations/*/dnsThreatDetectors/*}`   
Deletes a single DnsThreatDetector.  
`[get](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors/get)` |  `GET /v1/{name=projects/*/locations/*/dnsThreatDetectors/*}`   
Gets the details of a single DnsThreatDetector.  
`[list](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors/list)` |  `GET /v1/{parent=projects/*/locations/*}/dnsThreatDetectors`   
Lists DnsThreatDetectors in a given project and location.  
`[patch](https://docs.cloud.google.com/dns/docs/reference/dns-armor/rest/v1/projects.locations.dnsThreatDetectors/patch)` |  `PATCH /v1/{dnsThreatDetector.name=projects/*/locations/*/dnsThreatDetectors/*}`   
Updates a single DnsThreatDetector.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-15 UTC."],[],[]] 
