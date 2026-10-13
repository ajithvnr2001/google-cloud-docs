---
url: https://docs.cloud.google.com/dns/docs/reference/rest/
title: Cloud DNS API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:17.079187+00:00
---

# Cloud DNS API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  Cloud DNS API Stay organized with collections  Save and categorize content based on your preferences. 

  * REST Resource: v1beta2.changes
  * REST Resource: v1beta2.dnsKeys
  * REST Resource: v1beta2.managedZoneOperations
  * REST Resource: v1beta2.managedZones
  * REST Resource: v1beta2.policies
  * REST Resource: v1beta2.projects
  * REST Resource: v1beta2.resourceRecordSets
  * REST Resource: v1beta2.responsePolicies
  * REST Resource: v1beta2.responsePolicyRules
  * REST Resource: v1.changes
  * REST Resource: v1.dnsKeys
  * REST Resource: v1.managedZoneOperations
  * REST Resource: v1.managedZones
  * REST Resource: v1.policies
  * REST Resource: v1.projects
  * REST Resource: v1.resourceRecordSets
  * REST Resource: v1.responsePolicies
  * REST Resource: v1.responsePolicyRules



## Service: dns.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://dns.googleapis.com/$discovery/rest?version=v1>
  * <https://dns.googleapis.com/$discovery/rest?version=v1beta2>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://dns.googleapis.com`



## REST Resource: [v1beta2.changes](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/changes)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/changes/create)` |  `POST /dns/v1beta2/projects/{project}/managedZones/{managedZone}/changes`   
Atomically updates the ResourceRecordSet collection.  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/changes/get)` |  `GET /dns/v1beta2/projects/{project}/managedZones/{managedZone}/changes/{changeId}`   
Fetches the representation of an existing Change.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/changes/list)` |  `GET /dns/v1beta2/projects/{project}/managedZones/{managedZone}/changes`   
Enumerates Changes to a ResourceRecordSet collection.  
  
## REST Resource: [v1beta2.dnsKeys](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/dnsKeys)

Methods  
---  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/dnsKeys/get)` |  `GET /dns/v1beta2/projects/{project}/managedZones/{managedZone}/dnsKeys/{dnsKeyId}`   
Fetches the representation of an existing DnsKey.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/dnsKeys/list)` |  `GET /dns/v1beta2/projects/{project}/managedZones/{managedZone}/dnsKeys`   
Enumerates DnsKeys to a ResourceRecordSet collection.  
  
## REST Resource: [v1beta2.managedZoneOperations](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZoneOperations)

Methods  
---  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZoneOperations/get)` |  `GET /dns/v1beta2/projects/{project}/managedZones/{managedZone}/operations/{operation}`   
Fetches the representation of an existing Operation.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZoneOperations/list)` |  `GET /dns/v1beta2/projects/{project}/managedZones/{managedZone}/operations`   
Enumerates Operations for the given ManagedZone.  
  
## REST Resource: [v1beta2.managedZones](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZones)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZones/create)` |  `POST /dns/v1beta2/projects/{project}/managedZones`   
Creates a new ManagedZone.  
`[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZones/delete)` |  `DELETE /dns/v1beta2/projects/{project}/managedZones/{managedZone}`   
Deletes a previously created ManagedZone.  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZones/get)` |  `GET /dns/v1beta2/projects/{project}/managedZones/{managedZone}`   
Fetches the representation of an existing ManagedZone.  
`[getIamPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZones/getIamPolicy)` |  `POST /dns/v1beta2/{resource=projects/*/managedZones/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZones/list)` |  `GET /dns/v1beta2/projects/{project}/managedZones`   
Enumerates ManagedZones that have been created but not yet deleted.  
`[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZones/patch)` |  `PATCH /dns/v1beta2/projects/{project}/managedZones/{managedZone}`   
Applies a partial update to an existing ManagedZone.  
`[setIamPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZones/setIamPolicy)` |  `POST /dns/v1beta2/{resource=projects/*/managedZones/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZones/testIamPermissions)` |  `POST /dns/v1beta2/{resource=projects/*/managedZones/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[update](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/managedZones/update)` |  `PUT /dns/v1beta2/projects/{project}/managedZones/{managedZone}`   
Updates an existing ManagedZone.  
  
## REST Resource: [v1beta2.policies](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/policies)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/policies/create)` |  `POST /dns/v1beta2/projects/{project}/policies`   
Creates a new policy.  
`[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/policies/delete)` |  `DELETE /dns/v1beta2/projects/{project}/policies/{policy}`   
Deletes a previously created policy.  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/policies/get)` |  `GET /dns/v1beta2/projects/{project}/policies/{policy}`   
Fetches the representation of an existing policy.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/policies/list)` |  `GET /dns/v1beta2/projects/{project}/policies`   
Enumerates all policies associated with a project.  
`[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/policies/patch)` |  `PATCH /dns/v1beta2/projects/{project}/policies/{policy}`   
Applies a partial update to an existing policy.  
`[update](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/policies/update)` |  `PUT /dns/v1beta2/projects/{project}/policies/{policy}`   
Updates an existing policy.  
  
## REST Resource: [v1beta2.projects](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/projects)

Methods  
---  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/projects/get)` |  `GET /dns/v1beta2/projects/{project}`   
Fetches the representation of an existing Project.  
  
## REST Resource: [v1beta2.resourceRecordSets](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/resourceRecordSets)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/resourceRecordSets/create)` |  `POST /dns/v1beta2/projects/{project}/managedZones/{managedZone}/rrsets`   
Creates a new ResourceRecordSet.  
`[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/resourceRecordSets/delete)` |  `DELETE /dns/v1beta2/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}`   
Deletes a previously created ResourceRecordSet.  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/resourceRecordSets/get)` |  `GET /dns/v1beta2/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}`   
Fetches the representation of an existing ResourceRecordSet.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/resourceRecordSets/list)` |  `GET /dns/v1beta2/projects/{project}/managedZones/{managedZone}/rrsets`   
Enumerates ResourceRecordSets that you have created but not yet deleted.  
`[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/resourceRecordSets/patch)` |  `PATCH /dns/v1beta2/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}`   
Applies a partial update to an existing ResourceRecordSet.  
  
## REST Resource: [v1beta2.responsePolicies](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/create)` |  `POST /dns/v1beta2/projects/{project}/responsePolicies`   
Creates a new Response Policy  
`[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/delete)` |  `DELETE /dns/v1beta2/projects/{project}/responsePolicies/{responsePolicy}`   
Deletes a previously created Response Policy.  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/get)` |  `GET /dns/v1beta2/projects/{project}/responsePolicies/{responsePolicy}`   
Fetches the representation of an existing Response Policy.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/list)` |  `GET /dns/v1beta2/projects/{project}/responsePolicies`   
Enumerates all Response Policies associated with a project.  
`[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/patch)` |  `PATCH /dns/v1beta2/projects/{project}/responsePolicies/{responsePolicy}`   
Applies a partial update to an existing Response Policy.  
`[update](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicies/update)` |  `PUT /dns/v1beta2/projects/{project}/responsePolicies/{responsePolicy}`   
Updates an existing Response Policy.  
  
## REST Resource: [v1beta2.responsePolicyRules](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicyRules)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicyRules/create)` |  `POST /dns/v1beta2/projects/{project}/responsePolicies/{responsePolicy}/rules`   
Creates a new Response Policy Rule.  
`[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicyRules/delete)` |  `DELETE /dns/v1beta2/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}`   
Deletes a previously created Response Policy Rule.  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicyRules/get)` |  `GET /dns/v1beta2/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}`   
Fetches the representation of an existing Response Policy Rule.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicyRules/list)` |  `GET /dns/v1beta2/projects/{project}/responsePolicies/{responsePolicy}/rules`   
Enumerates all Response Policy Rules associated with a project.  
`[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicyRules/patch)` |  `PATCH /dns/v1beta2/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}`   
Applies a partial update to an existing Response Policy Rule.  
`[update](https://docs.cloud.google.com/dns/docs/reference/rest/v1beta2/responsePolicyRules/update)` |  `PUT /dns/v1beta2/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}`   
Updates an existing Response Policy Rule.  
  
## REST Resource: [v1.changes](https://docs.cloud.google.com/dns/docs/reference/rest/v1/changes)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1/changes/create)` |  `POST /dns/v1/projects/{project}/managedZones/{managedZone}/changes`   
Atomically updates the ResourceRecordSet collection.  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/changes/get)` |  `GET /dns/v1/projects/{project}/managedZones/{managedZone}/changes/{changeId}`   
Fetches the representation of an existing Change.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/changes/list)` |  `GET /dns/v1/projects/{project}/managedZones/{managedZone}/changes`   
Enumerates Changes to a ResourceRecordSet collection.  
  
## REST Resource: [v1.dnsKeys](https://docs.cloud.google.com/dns/docs/reference/rest/v1/dnsKeys)

Methods  
---  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/dnsKeys/get)` |  `GET /dns/v1/projects/{project}/managedZones/{managedZone}/dnsKeys/{dnsKeyId}`   
Fetches the representation of an existing DnsKey.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/dnsKeys/list)` |  `GET /dns/v1/projects/{project}/managedZones/{managedZone}/dnsKeys`   
Enumerates DnsKeys to a ResourceRecordSet collection.  
  
## REST Resource: [v1.managedZoneOperations](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZoneOperations)

Methods  
---  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZoneOperations/get)` |  `GET /dns/v1/projects/{project}/managedZones/{managedZone}/operations/{operation}`   
Fetches the representation of an existing Operation.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZoneOperations/list)` |  `GET /dns/v1/projects/{project}/managedZones/{managedZone}/operations`   
Enumerates Operations for the given ManagedZone.  
  
## REST Resource: [v1.managedZones](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/create)` |  `POST /dns/v1/projects/{project}/managedZones`   
Creates a new ManagedZone.  
`[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/delete)` |  `DELETE /dns/v1/projects/{project}/managedZones/{managedZone}`   
Deletes a previously created ManagedZone.  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/get)` |  `GET /dns/v1/projects/{project}/managedZones/{managedZone}`   
Fetches the representation of an existing ManagedZone.  
`[getIamPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/getIamPolicy)` |  `POST /dns/v1/{resource=projects/*/managedZones/*}:getIamPolicy`   
Gets the access control policy for a resource.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/list)` |  `GET /dns/v1/projects/{project}/managedZones`   
Enumerates ManagedZones that have been created but not yet deleted.  
`[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/patch)` |  `PATCH /dns/v1/projects/{project}/managedZones/{managedZone}`   
Applies a partial update to an existing ManagedZone.  
`[setIamPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/setIamPolicy)` |  `POST /dns/v1/{resource=projects/*/managedZones/*}:setIamPolicy`   
Sets the access control policy on the specified resource.  
`[testIamPermissions](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/testIamPermissions)` |  `POST /dns/v1/{resource=projects/*/managedZones/*}:testIamPermissions`   
Returns permissions that a caller has on the specified resource.  
`[update](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/update)` |  `PUT /dns/v1/projects/{project}/managedZones/{managedZone}`   
Updates an existing ManagedZone.  
  
## REST Resource: [v1.policies](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/create)` |  `POST /dns/v1/projects/{project}/policies`   
Creates a new policy.  
`[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/delete)` |  `DELETE /dns/v1/projects/{project}/policies/{policy}`   
Deletes a previously created policy.  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/get)` |  `GET /dns/v1/projects/{project}/policies/{policy}`   
Fetches the representation of an existing policy.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/list)` |  `GET /dns/v1/projects/{project}/policies`   
Enumerates all policies associated with a project.  
`[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/patch)` |  `PATCH /dns/v1/projects/{project}/policies/{policy}`   
Applies a partial update to an existing policy.  
`[update](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/update)` |  `PUT /dns/v1/projects/{project}/policies/{policy}`   
Updates an existing policy.  
  
## REST Resource: [v1.projects](https://docs.cloud.google.com/dns/docs/reference/rest/v1/projects)

Methods  
---  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/projects/get)` |  `GET /dns/v1/projects/{project}`   
Fetches the representation of an existing Project.  
  
## REST Resource: [v1.resourceRecordSets](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/create)` |  `POST /dns/v1/projects/{project}/managedZones/{managedZone}/rrsets`   
Creates a new ResourceRecordSet.  
`[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/delete)` |  `DELETE /dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}`   
Deletes a previously created ResourceRecordSet.  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/get)` |  `GET /dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}`   
Fetches the representation of an existing ResourceRecordSet.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/list)` |  `GET /dns/v1/projects/{project}/managedZones/{managedZone}/rrsets`   
Enumerates ResourceRecordSets that you have created but not yet deleted.  
`[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/patch)` |  `PATCH /dns/v1/projects/{project}/managedZones/{managedZone}/rrsets/{name}/{type}`   
Applies a partial update to an existing ResourceRecordSet.  
  
## REST Resource: [v1.responsePolicies](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicies)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicies/create)` |  `POST /dns/v1/projects/{project}/responsePolicies`   
Creates a new Response Policy  
`[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicies/delete)` |  `DELETE /dns/v1/projects/{project}/responsePolicies/{responsePolicy}`   
Deletes a previously created Response Policy.  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicies/get)` |  `GET /dns/v1/projects/{project}/responsePolicies/{responsePolicy}`   
Fetches the representation of an existing Response Policy.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicies/list)` |  `GET /dns/v1/projects/{project}/responsePolicies`   
Enumerates all Response Policies associated with a project.  
`[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicies/patch)` |  `PATCH /dns/v1/projects/{project}/responsePolicies/{responsePolicy}`   
Applies a partial update to an existing Response Policy.  
`[update](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicies/update)` |  `PUT /dns/v1/projects/{project}/responsePolicies/{responsePolicy}`   
Updates an existing Response Policy.  
  
## REST Resource: [v1.responsePolicyRules](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules)

Methods  
---  
`[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/create)` |  `POST /dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules`   
Creates a new Response Policy Rule.  
`[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/delete)` |  `DELETE /dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}`   
Deletes a previously created Response Policy Rule.  
`[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/get)` |  `GET /dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}`   
Fetches the representation of an existing Response Policy Rule.  
`[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/list)` |  `GET /dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules`   
Enumerates all Response Policy Rules associated with a project.  
`[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/patch)` |  `PATCH /dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}`   
Applies a partial update to an existing Response Policy Rule.  
`[update](https://docs.cloud.google.com/dns/docs/reference/rest/v1/responsePolicyRules/update)` |  `PUT /dns/v1/projects/{project}/responsePolicies/{responsePolicy}/rules/{responsePolicyRule}`   
Updates an existing Response Policy Rule.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
