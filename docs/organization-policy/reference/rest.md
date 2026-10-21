---
url: https://docs.cloud.google.com/organization-policy/reference/rest/
title: Organization Policy API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:38.335038+00:00
---

# Organization Policy API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  Organization Policy API Stay organized with collections  Save and categorize content based on your preferences. 

The Organization Policy API allows users to configure governance rules on their Google Cloud resources across the resource hierarchy.

  * REST Resource: v2.folders.constraints
  * REST Resource: v2.folders.policies
  * REST Resource: v2.organizations.constraints
  * REST Resource: v2.organizations.customConstraints
  * REST Resource: v2.organizations.policies
  * REST Resource: v2.projects.constraints
  * REST Resource: v2.projects.policies



## Service: orgpolicy.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://orgpolicy.googleapis.com/$discovery/rest?version=v2>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://orgpolicy.googleapis.com`



## REST Resource: [v2.folders.constraints](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.constraints)

Methods  
---  
`[list](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.constraints/list)` |  `GET /v2/{parent=folders/*}/constraints`   
Lists constraints that could be applied on the specified resource.  
  
## REST Resource: [v2.folders.policies](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies)

Methods  
---  
`[create](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies/create)` |  `POST /v2/{parent=folders/*}/policies`   
Creates a policy.  
`[delete](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies/delete)` |  `DELETE /v2/{name=folders/*/policies/*}`   
Deletes a policy.  
`[get](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies/get)` |  `GET /v2/{name=folders/*/policies/*}`   
Gets a policy on a resource.  
`[getEffectivePolicy](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies/getEffectivePolicy)` |  `GET /v2/{name=folders/*/policies/*}:getEffectivePolicy`   
Gets the effective policy on a resource.  
`[list](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies/list)` |  `GET /v2/{parent=folders/*}/policies`   
Retrieves all of the policies that exist on a particular resource.  
`[patch](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies/patch)` |  `PATCH /v2/{policy.name=folders/*/policies/*}`   
Updates a policy.  
  
## REST Resource: [v2.organizations.constraints](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.constraints)

Methods  
---  
`[list](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.constraints/list)` |  `GET /v2/{parent=organizations/*}/constraints`   
Lists constraints that could be applied on the specified resource.  
  
## REST Resource: [v2.organizations.customConstraints](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints)

Methods  
---  
`[create](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/create)` |  `POST /v2/{parent=organizations/*}/customConstraints`   
Creates a custom constraint.  
`[delete](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/delete)` |  `DELETE /v2/{name=organizations/*/customConstraints/*}`   
Deletes a custom constraint.  
`[get](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/get)` |  `GET /v2/{name=organizations/*/customConstraints/*}`   
Gets a custom or managed constraint.  
`[list](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/list)` |  `GET /v2/{parent=organizations/*}/customConstraints`   
Retrieves all of the custom constraints that exist on a particular organization resource.  
`[patch](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.customConstraints/patch)` |  `PATCH /v2/{customConstraint.name=organizations/*/customConstraints/*}`   
Updates a custom constraint.  
  
## REST Resource: [v2.organizations.policies](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.policies)

Methods  
---  
`[create](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.policies/create)` |  `POST /v2/{parent=organizations/*}/policies`   
Creates a policy.  
`[delete](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.policies/delete)` |  `DELETE /v2/{name=organizations/*/policies/*}`   
Deletes a policy.  
`[get](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.policies/get)` |  `GET /v2/{name=organizations/*/policies/*}`   
Gets a policy on a resource.  
`[getEffectivePolicy](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.policies/getEffectivePolicy)` |  `GET /v2/{name=organizations/*/policies/*}:getEffectivePolicy`   
Gets the effective policy on a resource.  
`[list](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.policies/list)` |  `GET /v2/{parent=organizations/*}/policies`   
Retrieves all of the policies that exist on a particular resource.  
`[patch](https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.policies/patch)` |  `PATCH /v2/{policy.name=organizations/*/policies/*}`   
Updates a policy.  
  
## REST Resource: [v2.projects.constraints](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.constraints)

Methods  
---  
`[list](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.constraints/list)` |  `GET /v2/{parent=projects/*}/constraints`   
Lists constraints that could be applied on the specified resource.  
  
## REST Resource: [v2.projects.policies](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies)

Methods  
---  
`[create](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/create)` |  `POST /v2/{parent=projects/*}/policies`   
Creates a policy.  
`[delete](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/delete)` |  `DELETE /v2/{name=projects/*/policies/*}`   
Deletes a policy.  
`[get](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/get)` |  `GET /v2/{name=projects/*/policies/*}`   
Gets a policy on a resource.  
`[getEffectivePolicy](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/getEffectivePolicy)` |  `GET /v2/{name=projects/*/policies/*}:getEffectivePolicy`   
Gets the effective policy on a resource.  
`[list](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/list)` |  `GET /v2/{parent=projects/*}/policies`   
Retrieves all of the policies that exist on a particular resource.  
`[patch](https://docs.cloud.google.com/organization-policy/reference/rest/v2/projects.policies/patch)` |  `PATCH /v2/{policy.name=projects/*/policies/*}`   
Updates a policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-18 UTC."],[],[]] 
