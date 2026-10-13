---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/
title: Assured Workloads API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:24.830745+00:00
---

# Assured Workloads API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  Assured Workloads API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1beta1.organizations.locations.operations
  * REST Resource: v1beta1.organizations.locations.workloads
  * REST Resource: v1beta1.organizations.locations.workloads.updates
  * REST Resource: v1beta1.organizations.locations.workloads.violations
  * REST Resource: v1.organizations.locations.operations
  * REST Resource: v1.organizations.locations.workloads
  * REST Resource: v1.organizations.locations.workloads.updates
  * REST Resource: v1.organizations.locations.workloads.violations



## Service: assuredworkloads.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://assuredworkloads.googleapis.com/$discovery/rest?version=v1>
  * <https://assuredworkloads.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoints and all URIs below are relative to these service endpoints:

  * `https://us-central1-assuredworkloads.googleapis.com`
  * `https://us-east1-assuredworkloads.googleapis.com`
  * `https://us-east4-assuredworkloads.googleapis.com`
  * `https://us-east5-assuredworkloads.googleapis.com`
  * `https://us-east7-assuredworkloads.googleapis.com`
  * `https://us-south1-assuredworkloads.googleapis.com`
  * `https://us-west1-assuredworkloads.googleapis.com`
  * `https://us-west2-assuredworkloads.googleapis.com`
  * `https://us-west3-assuredworkloads.googleapis.com`
  * `https://us-west4-assuredworkloads.googleapis.com`
  * `https://europe-west1-assuredworkloads.googleapis.com`
  * `https://europe-west2-assuredworkloads.googleapis.com`
  * `https://europe-west3-assuredworkloads.googleapis.com`
  * `https://europe-west4-assuredworkloads.googleapis.com`
  * `https://europe-west6-assuredworkloads.googleapis.com`
  * `https://europe-west8-assuredworkloads.googleapis.com`
  * `https://europe-west9-assuredworkloads.googleapis.com`
  * `https://europe-west10-assuredworkloads.googleapis.com`
  * `https://europe-west12-assuredworkloads.googleapis.com`
  * `https://europe-southwest1-assuredworkloads.googleapis.com`
  * `https://europe-north1-assuredworkloads.googleapis.com`
  * `https://europe-north2-assuredworkloads.googleapis.com`
  * `https://europe-central2-assuredworkloads.googleapis.com`
  * `https://me-west1-assuredworkloads.googleapis.com`
  * `https://me-central1-assuredworkloads.googleapis.com`
  * `https://me-central2-assuredworkloads.googleapis.com`
  * `https://northamerica-northeast1-assuredworkloads.googleapis.com`
  * `https://northamerica-northeast2-assuredworkloads.googleapis.com`
  * `https://australia-southeast1-assuredworkloads.googleapis.com`
  * `https://australia-southeast2-assuredworkloads.googleapis.com`
  * `https://africa-south1-assuredworkloads.googleapis.com`
  * `https://asia-east1-assuredworkloads.googleapis.com`
  * `https://asia-east2-assuredworkloads.googleapis.com`
  * `https://asia-northeast1-assuredworkloads.googleapis.com`
  * `https://asia-northeast2-assuredworkloads.googleapis.com`
  * `https://asia-northeast3-assuredworkloads.googleapis.com`
  * `https://asia-south1-assuredworkloads.googleapis.com`
  * `https://asia-south2-assuredworkloads.googleapis.com`
  * `https://asia-southeast1-assuredworkloads.googleapis.com`
  * `https://asia-southeast2-assuredworkloads.googleapis.com`
  * `https://southamerica-east1-assuredworkloads.googleapis.com`
  * `https://southamerica-west1-assuredworkloads.googleapis.com`
  * `https://assuredworkloads.googleapis.com`



## REST Resource: [v1beta1.organizations.locations.operations](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.operations/get)` |  `GET /v1beta1/{name=organizations/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.operations/list)` |  `GET /v1beta1/{name=organizations/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1beta1.organizations.locations.workloads](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads)

Methods  
---  
`[analyzeWorkloadMove](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/analyzeWorkloadMove)` |  `GET /v1beta1/{target=organizations/*/locations/*/workloads/*}:analyzeWorkloadMove`   
Analyzes a hypothetical move of a source resource to a target workload to surface compliance risks.  
`[create](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/create)` |  `POST /v1beta1/{parent=organizations/*/locations/*}/workloads`   
Creates Assured Workload.  
`[delete](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/delete)` |  `DELETE /v1beta1/{name=organizations/*/locations/*/workloads/*}`   
Deletes the workload.  
`[enableComplianceUpdates](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/enableComplianceUpdates)` |  `PUT /v1beta1/{name=organizations/*/locations/*/workloads/*}:enableComplianceUpdates`   
This endpoint enables Assured Workloads service to offer compliance updates for the folder based assured workload.  
`[enableResourceMonitoring](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/enableResourceMonitoring)` |  `POST /v1beta1/{name=organizations/*/locations/*/workloads/*}:enableResourceMonitoring`   
Enable resource violation monitoring for a workload.  
`[get](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/get)` |  `GET /v1beta1/{name=organizations/*/locations/*/workloads/*}`   
Gets Assured Workload associated with a CRM Node  
`[list](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/list)` |  `GET /v1beta1/{parent=organizations/*/locations/*}/workloads`   
Lists Assured Workloads under a CRM Node.  
`[patch](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/patch)` |  `PATCH /v1beta1/{workload.name=organizations/*/locations/*/workloads/*}`   
Updates an existing workload.  
`[restrictAllowedResources](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/restrictAllowedResources)` |  `POST /v1beta1/{name=organizations/*/locations/*/workloads/*}:restrictAllowedResources`   
Restrict the list of resources allowed in the Workload environment.  
  
## REST Resource: [v1beta1.organizations.locations.workloads.updates](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads.updates)

Methods  
---  
`[apply](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads.updates/apply)` |  `POST /v1beta1/{name=organizations/*/locations/*/workloads/*/updates/*}:apply`   
This endpoint creates a new operation to apply the given update.  
`[list](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads.updates/list)` |  `GET /v1beta1/{parent=organizations/*/locations/*/workloads/*}/updates`   
This endpoint lists all updates for the given workload.  
  
## REST Resource: [v1beta1.organizations.locations.workloads.violations](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads.violations)

Methods  
---  
`[acknowledge](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads.violations/acknowledge)` |  `POST /v1beta1/{name=organizations/*/locations/*/workloads/*/violations/*}:acknowledge`   
Acknowledges an existing violation.  
`[get](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads.violations/get)` |  `GET /v1beta1/{name=organizations/*/locations/*/workloads/*/violations/*}`   
Retrieves Assured Workload Violation based on ID.  
`[list](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads.violations/list)` |  `GET /v1beta1/{parent=organizations/*/locations/*/workloads/*}/violations`   
Lists the Violations in the AssuredWorkload Environment.  
  
## REST Resource: [v1.organizations.locations.operations](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.operations)

Methods  
---  
`[get](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.operations/get)` |  `GET /v1/{name=organizations/*/locations/*/operations/*}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.operations/list)` |  `GET /v1/{name=organizations/*/locations/*}/operations`   
Lists operations that match the specified filter in the request.  
  
## REST Resource: [v1.organizations.locations.workloads](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads)

Methods  
---  
`[analyzeWorkloadMove](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/analyzeWorkloadMove)` |  `GET /v1/{target=organizations/*/locations/*/workloads/*}:analyzeWorkloadMove`   
Analyzes a hypothetical move of a source resource to a target workload to surface compliance risks.  
`[create](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/create)` |  `POST /v1/{parent=organizations/*/locations/*}/workloads`   
Creates Assured Workload.  
`[delete](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/delete)` |  `DELETE /v1/{name=organizations/*/locations/*/workloads/*}`   
Deletes the workload.  
`[enableComplianceUpdates](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/enableComplianceUpdates)` |  `PUT /v1/{name=organizations/*/locations/*/workloads/*}:enableComplianceUpdates`   
This endpoint enables Assured Workloads service to offer compliance updates for the folder based assured workload.  
`[enableResourceMonitoring](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/enableResourceMonitoring)` |  `POST /v1/{name=organizations/*/locations/*/workloads/*}:enableResourceMonitoring`   
Enable resource violation monitoring for a workload.  
`[get](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/get)` |  `GET /v1/{name=organizations/*/locations/*/workloads/*}`   
Gets Assured Workload associated with a CRM Node  
`[list](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/list)` |  `GET /v1/{parent=organizations/*/locations/*}/workloads`   
Lists Assured Workloads under a CRM Node.  
`[mutatePartnerPermissions](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/mutatePartnerPermissions)` |  `PATCH /v1/{name=organizations/*/locations/*/workloads/*}:mutatePartnerPermissions`   
Update the permissions settings for an existing partner workload.  
`[patch](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/patch)` |  `PATCH /v1/{workload.name=organizations/*/locations/*/workloads/*}`   
Updates an existing workload.  
`[restrictAllowedResources](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads/restrictAllowedResources)` |  `POST /v1/{name=organizations/*/locations/*/workloads/*}:restrictAllowedResources`   
Restrict the list of resources allowed in the Workload environment.  
  
## REST Resource: [v1.organizations.locations.workloads.updates](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.updates)

Methods  
---  
`[apply](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.updates/apply)` |  `POST /v1/{name=organizations/*/locations/*/workloads/*/updates/*}:apply`   
This endpoint creates a new operation to apply the given update.  
`[list](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.updates/list)` |  `GET /v1/{parent=organizations/*/locations/*/workloads/*}/updates`   
This endpoint lists all updates for the given workload.  
  
## REST Resource: [v1.organizations.locations.workloads.violations](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations)

Methods  
---  
`[acknowledge](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations/acknowledge)` |  `POST /v1/{name=organizations/*/locations/*/workloads/*/violations/*}:acknowledge`   
Acknowledges an existing violation.  
`[get](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations/get)` |  `GET /v1/{name=organizations/*/locations/*/workloads/*/violations/*}`   
Retrieves Assured Workload Violation based on ID.  
`[list](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.violations/list)` |  `GET /v1/{parent=organizations/*/locations/*/workloads/*}/violations`   
Lists the Violations in the AssuredWorkload Environment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-22 UTC."],[],[]] 
