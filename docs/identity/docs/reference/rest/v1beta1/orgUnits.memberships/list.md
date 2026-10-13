---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships/list/
title: Method: orgUnits.memberships.list \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:56.570717+00:00
---

# Method: orgUnits.memberships.list  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: orgUnits.memberships.list Stay organized with collections  Save and categorize content based on your preferences. 

List `[OrgMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#OrgMembership)` resources in an OrgUnit treated as 'parent'.

Parent format: orgUnits/{$orgUnitId}

where `$orgUnitId` is the `orgUnitId` from the [Admin SDK `OrgUnit` resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits)

### HTTP request

`GET https://cloudidentity.googleapis.com/v1beta1/{parent=orgUnits/*}/memberships`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Immutable. OrgUnit which is queried for a list of memberships.Format: orgUnits/{$orgUnitId}where `$orgUnitId` is the `orgUnitId` from the [Admin SDK `OrgUnit` resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits).  
  
### Query parameters

Parameters  
---  
`customer` |  `string` Required. Immutable. Customer that this `[OrgMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#OrgMembership)` belongs to.All authorization will happen on the role assignments of this customer.Format: customers/{$customerId}where `$customerId` is the `id` from the [Admin SDK `Customer` resource](https://developers.google.com/admin-sdk/directory/reference/rest/v1/customers).You may also use `customers/my_customer` to specify your own organization.  
`filter` |  `string` The search query.Must be specified in [Common Expression Language](https://opensource.google/projects/cel). May only contain equality operators on the `type` (e.g., `type == 'shared_drive'`).  
`pageSize` |  `integer` The maximum number of results to return.The service may return fewer than this value.If omitted (or defaulted to zero) the server will default to 50.The maximum allowed value is 100, though requests with pageSize greater than that will be silently interpreted as 100.  
`pageToken` |  `string` A page token, received from a previous `OrgMembershipsService.ListOrgMemberships` call.Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListOrgMembershipsRequest` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[OrgMembershipsService.ListOrgMemberships](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships/list#google.apps.cloudidentity.orgunits.v1beta1.OrgMembershipsService.ListOrgMemberships)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "orgMemberships": [
        {
          object ([OrgMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#OrgMembership))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`orgMemberships[]` |  `object (`[OrgMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#OrgMembership)`)` The non-vacuous membership in an orgUnit.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page.If this field is empty, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.orgunits.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.orgunits`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
