---
url: https://docs.cloud.google.com/compute/docs/licensemanager/rest/
title: License Manager API \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:38:13.315423+00:00
---

# License Manager API  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/licensemanager/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  License Manager API Stay organized with collections  Save and categorize content based on your preferences. 

License Manager is a tool to manage and track third-party licenses on Google Cloud.

  * REST Resource: v1.projects.locations
  * REST Resource: v1.projects.locations.configurations
  * REST Resource: v1.projects.locations.instances
  * REST Resource: v1.projects.locations.operations
  * REST Resource: v1.projects.locations.products



## Service: licensemanager.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://licensemanager.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://licensemanager.googleapis.com`



## REST Resource: [v1.projects.locations](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations)

Methods  
---  
`[get](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations/get)` |  `GET /v1/{name=projects/*/locations/*}`   
Gets information about a location.  
`[list](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations/list)` |  `GET /v1/{name=projects/*}/locations`   
Lists information about the supported locations for this service.  
  
## REST Resource: [v1.projects.locations.configurations](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations)

Methods  
---  
`[aggregateUsage](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/aggregateUsage)` |  `GET /v1/{name=projects/*/locations/*/configurations/*}:aggregateUsage`   
Aggregates Usage per Instance for a Configuration.  
`[create](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/create)` |  `POST /v1/{parent=projects/*/locations/*}/configurations`   
Creates a new Configuration in a given project and location.  
`[deactivate](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/deactivate)` |  `POST /v1/{name=projects/*/locations/*/configurations/*}:deactivate`   
Deactivates the given configuration.  
`[delete](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/configurations/*}`   
Deletes a single Configuration.  
`[get](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/get)` |  `GET /v1/{name=projects/*/locations/*/configurations/*}`   
Gets details of a single Configuration.  
`[list](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/list)` |  `GET /v1/{parent=projects/*/locations/*}/configurations`   
Lists Configurations in a given project and location.  
`[patch](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/patch)` |  `PATCH /v1/{configuration.name=projects/*/locations/*/configurations/*}`   
Updates the parameters of a single Configuration.  
`[queryLicenseUsage](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/queryLicenseUsage)` |  `GET /v1/{name=projects/*/locations/*/configurations/*}:queryLicenseUsage`   
License Usage information for a Configuration.  
`[reactivate](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.configurations/reactivate)` |  `POST /v1/{name=projects/*/locations/*/configurations/*}:reactivate`   
Reactivates the given configuration.  
  
## REST Resource: [v1.projects.locations.instances](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances)

Methods  
---  
`[get](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances/get)` |  `GET /v1/{name=projects/*/locations/*/instances/*}`   
Gets details of a single Instance.  
`[list](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.instances/list)` |  `GET /v1/{parent=projects/*/locations/*}/instances`   
Lists Instances in a given project and location.  
  
## REST Resource: [v1.projects.locations.operations](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.operations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.operations/cancel)` |  `POST /v1/{name=projects/*/locations/*/operations/*}:cancel`   
Starts asynchronous cancellation on a long-running operation.  
`[delete](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.operations/delete)` |  `DELETE /v1/{name=projects/*/locations/*/operations/*}`   
Deletes a long-running operation.  
`[get](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.operations/get)` |  `GET /v1/{name=projects/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.operations/list)` |  `GET /v1/{name=projects/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.projects.locations.products](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.products)

Methods  
---  
`[get](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.products/get)` |  `GET /v1/{name=projects/*/locations/*/products/*}`   
Gets details of a single Product.  
`[list](https://docs.cloud.google.com/compute/docs/licensemanager/rest/v1/projects.locations.products/list)` |  `GET /v1/{parent=projects/*/locations/*}/products`   
Lists Products in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
