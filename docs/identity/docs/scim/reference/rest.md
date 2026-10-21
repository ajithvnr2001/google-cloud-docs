---
url: https://docs.cloud.google.com/identity/docs/scim/reference/rest/
title: Cloud Identity SCIM API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:58.897861+00:00
---

# Cloud Identity SCIM API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/scim/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Cloud Identity SCIM API Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Identity SCIM API uses the open System for Cross-domain Identity Management (SCIM) standard to automate user and group management between your Identity Provider (IdP) and Google Cloud Identity. It standardizes how users and groups are provisioned, updated, and deprovisioned by implementing a subset of SCIM RFCs [7643](https://datatracker.ietf.org/doc/html/rfc7643) and [7644](https://datatracker.ietf.org/doc/html/rfc7644).

## Additional features

  * **Automatic group locking:** If your organization has set up a SCIM connection, groups synced using the connection's authentication methods can be automatically locked by enabling the **Lock synced groups** setting. This prevents manual modifications in other Google interfaces (such as the Admin console), ensuring your IdP remains the authoritative source. For details on this feature, see [How locking synced groups works](https://knowledge.workspace.google.com/p/inbound-scim-get-started#lock-synced-groups).



## Unsupported SCIM features

  * **Sorting:** Described in [RFC 7644 Section 3.4.2.3](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.3).
  * **Pagination:** Neither index-based ([RFC 7644 Section 3.4.2.4](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.4)) nor cursor-based ([RFC 9865](https://datatracker.ietf.org/doc/rfc9865/)) pagination is supported.
  * **Bulk operations:** Described in [RFC 7644 Section 3.7](https://datatracker.ietf.org/doc/html/rfc7644#section-3.7).
  * **ETags:** Described in [RFC 7644 Section 3.14](https://datatracker.ietf.org/doc/html/rfc7644#section-3.14).



## Service: cloudidentityscim.googleapis.com

### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://cloudidentityscim.googleapis.com`



## REST Resource: [v1beta1.customers.v2.Groups](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups/create)` |  `POST /v1beta1/customers/{customerId}/v2/Groups`   
Creates a Group.  
`[delete](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups/delete)` |  `DELETE /v1beta1/customers/{customerId}/v2/Groups/{groupId}`   
Deletes a Group.  
`[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups/get)` |  `GET /v1beta1/customers/{customerId}/v2/Groups/{groupId}`   
Retrieves a Group.  
`[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups/list)` |  `GET /v1beta1/customers/{customerId}/v2/Groups`   
Retrieves a list of Groups.  
`[patch](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups/patch)` |  `PATCH /v1beta1/customers/{customerId}/v2/Groups/{groupId}`   
Updates a Group using SCIM patch semantics.  
  
## REST Resource: [v1beta1.customers.v2.ResourceTypes](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.ResourceTypes)

Methods  
---  
`[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.ResourceTypes/get)` |  `GET /v1beta1/customers/{customerId}/v2/ResourceTypes/{resourceTypeId}`   
Retrieves a specific resource type.  
`[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.ResourceTypes/list)` |  `GET /v1beta1/customers/{customerId}/v2/ResourceTypes`   
Retrieves all resource types.  
  
## REST Resource: [v1beta1.customers.v2.Schemas](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Schemas)

Methods  
---  
`[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Schemas/get)` |  `GET /v1beta1/customers/{customerId}/v2/Schemas/{schemaId}`   
Retrieves a Schema.  
`[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Schemas/list)` |  `GET /v1beta1/customers/{customerId}/v2/Schemas`   
Retrieves all Schemas.  
  
## REST Resource: [v1beta1.customers.v2.ServiceProviderConfig](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.ServiceProviderConfig)

Methods  
---  
`[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.ServiceProviderConfig/get)` |  `GET /v1beta1/customers/{customerId}/v2/ServiceProviderConfig`   
Retrieves the Service Provider Configuration.  
  
## REST Resource: [v1beta1.customers.v2.Users](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/create)` |  `POST /v1beta1/customers/{customerId}/v2/Users`   
Creates a User.  
`[delete](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/delete)` |  `DELETE /v1beta1/customers/{customerId}/v2/Users/{userId}`   
Deletes a User.  
`[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/get)` |  `GET /v1beta1/customers/{customerId}/v2/Users/{userId}`   
Retrieves a User.  
`[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/list)` |  `GET /v1beta1/customers/{customerId}/v2/Users`   
Retrieves a list of Users.  
`[patch](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/patch)` |  `PATCH /v1beta1/customers/{customerId}/v2/Users/{userId}`   
Updates a User using SCIM patch semantics.  
  
## REST Resource: [v1.customers.v2.Groups](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Groups)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Groups/create)` |  `POST /v1/customers/{customerId}/v2/Groups`   
Creates a Group.  
`[delete](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Groups/delete)` |  `DELETE /v1/customers/{customerId}/v2/Groups/{groupId}`   
Deletes a Group.  
`[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Groups/get)` |  `GET /v1/customers/{customerId}/v2/Groups/{groupId}`   
Retrieves a Group.  
`[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Groups/list)` |  `GET /v1/customers/{customerId}/v2/Groups`   
Retrieves a list of Groups.  
`[patch](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Groups/patch)` |  `PATCH /v1/customers/{customerId}/v2/Groups/{groupId}`   
Updates a Group using SCIM patch semantics.  
  
## REST Resource: [v1.customers.v2.ResourceTypes](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ResourceTypes)

Methods  
---  
`[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ResourceTypes/get)` |  `GET /v1/customers/{customerId}/v2/ResourceTypes/{resourceTypeId}`   
Retrieves a specific resource type.  
`[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ResourceTypes/list)` |  `GET /v1/customers/{customerId}/v2/ResourceTypes`   
Retrieves all resource types.  
  
## REST Resource: [v1.customers.v2.Schemas](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Schemas)

Methods  
---  
`[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Schemas/get)` |  `GET /v1/customers/{customerId}/v2/Schemas/{schemaId}`   
Retrieves a Schema.  
`[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Schemas/list)` |  `GET /v1/customers/{customerId}/v2/Schemas`   
Retrieves all Schemas.  
  
## REST Resource: [v1.customers.v2.ServiceProviderConfig](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig)

Methods  
---  
`[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig/get)` |  `GET /v1/customers/{customerId}/v2/ServiceProviderConfig`   
Retrieves the Service Provider Configuration.  
  
## REST Resource: [v1.customers.v2.Users](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Users)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Users/create)` |  `POST /v1/customers/{customerId}/v2/Users`   
Creates a User.  
`[delete](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Users/delete)` |  `DELETE /v1/customers/{customerId}/v2/Users/{userId}`   
Deletes a User.  
`[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Users/get)` |  `GET /v1/customers/{customerId}/v2/Users/{userId}`   
Retrieves a User.  
`[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Users/list)` |  `GET /v1/customers/{customerId}/v2/Users`   
Retrieves a list of Users.  
`[patch](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.Users/patch)` |  `PATCH /v1/customers/{customerId}/v2/Users/{userId}`   
Updates a User using SCIM patch semantics.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-08 UTC."],[],[]] 
