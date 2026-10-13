---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships/move/
title: Method: orgUnits.memberships.move \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:56.864950+00:00
---

# Method: orgUnits.memberships.move  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships/move/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: orgUnits.memberships.move Stay organized with collections  Save and categorize content based on your preferences. 

Move an `[OrgMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#OrgMembership)` to a new OrgUnit.

NOTE: This is an atomic copy-and-delete. The resource will have a new copy under the destination OrgUnit and be deleted from the source OrgUnit. The resource can only be searched under the destination OrgUnit afterwards.

### HTTP request

`POST https://cloudidentity.googleapis.com/v1beta1/{name=orgUnits/*/memberships/*}:move`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Immutable. The [resource name](https://cloud.google.com/apis/design/resource_names) of the `[OrgMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#OrgMembership)`.Format: orgUnits/{$orgUnitId}/memberships/{$membership}The `$orgUnitId` is the `orgUnitId` from the [Admin SDK `OrgUnit` resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits). To manage a Membership without specifying source `orgUnitId`, this API also supports the wildcard character '-' for `$orgUnitId` per <https://google.aip.dev/159>.The `$membership` shall be of the form `{$entityType};{$memberId}`, where `$entityType` is the enum value of `[OrgMembership.EntityType](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#EntityType)`, and `memberId` is the `id` from [Drive API (V3) `Drive` resource](https://developers.google.com/drive/api/v3/reference/drives#resource) for `[OrgMembership.EntityType.SHARED_DRIVE](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#EntityType.ENUM_VALUES.SHARED_DRIVE)`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "customer": string,
      "destinationOrgUnit": string
    }  
  
Fields  
---  
`customer` |  `string` Required. Immutable. Customer on whose membership change is made.All authorization will happen on the role assignments of this customer.Format: customers/{$customerId}where `$customerId` is the `id` from the [Admin SDK `Customer` resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/customers).You may also use `customers/my_customer` to specify your own organization.  
`destinationOrgUnit` |  `string` Required. Immutable. OrgUnit where the membership will be moved to.Format: orgUnits/{$orgUnitId}where `$orgUnitId` is the `orgUnitId` from the [Admin SDK `OrgUnit` resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits).  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/identity/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-identity.orgunits`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
