---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies/
title: REST Resource: policies \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:57.310502+00:00
---

# REST Resource: policies  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: policies Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Policy

A Policy resource binds an instance of a single Setting with the scope of a PolicyQuery. The Setting instance will be applied to all entities that satisfy the query.

JSON representation  
---  
      
    
    {
      "name": string,
      "customer": string,
      "policyQuery": {
        object ([PolicyQuery](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies#PolicyQuery))
      },
      "setting": {
        object ([Setting](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies#Setting))
      },
      "type": enum ([PolicyType](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies#PolicyType))
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The [resource name](https://cloud.google.com/apis/design/resource_names) of the Policy. Format: policies/{policy}.  
`customer` |  `string` Immutable. Customer that the Policy belongs to. The value is in the format 'customers/{customerId}'. The `customerId` must begin with "C" To find your customer ID in Admin Console see <https://support.google.com/a/answer/10070793>.  
`policyQuery` |  `object (`[PolicyQuery](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies#PolicyQuery)`)` Required. The PolicyQuery the Setting applies to.  
`setting` |  `object (`[Setting](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies#Setting)`)` Required. The Setting configured by this Policy.  
`type` |  `enum (`[PolicyType](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies#PolicyType)`)` Output only. The type of the policy.  
  
## PolicyQuery

PolicyQuery

JSON representation  
---  
      
    
    {
      "query": string,
      "orgUnit": string,
      "group": string,
      "sortOrder": number
    }  
  
Fields  
---  
`query` |  `string` Immutable. The CEL query that defines which entities the Policy applies to (ex. a User entity).For details about CEL see <https://opensource.google.com/projects/cel>.The OrgUnits the Policy applies to are represented by a clause like so: entity.org_units.exists(orgUnit, orgUnit.org_unit_id == orgUnitId('{orgUnitId}'))The Group the Policy applies to are represented by a clause like so: entity.groups.exists(group, group.group_id == groupId('{groupId}'))The Licenses the Policy applies to are represented by a clause like so: entity.licenses.exists(license, license in ['/product/{productId}/sku/{skuId}'])**Note:** The licenses clause is not supported in mutate endpoints.The above clauses can be present in any combination, and used in conjunction with the &&, || and ! operators.The orgUnit and group fields below are helper fields that contain the corresponding value(s) as the query to make the query easier to use.  
`orgUnit` |  `string` Required. Immutable. Non-empty default. The OrgUnit the query applies to. This field is only set if there is a single value for orgUnit that satisfies all clauses of the query.  
`group` |  `string` Immutable. The group that the query applies to. This field is only set if there is a single value for group that satisfies all clauses of the query. If no group applies, this will be the empty string.  
`sortOrder` |  `number` Output only. The decimal sort order of this PolicyQuery. The value is relative to all other policies with the same setting type for the customer. (There are no duplicates within this set).  
  
## Setting

Setting

JSON representation  
---  
      
    
    {
      "type": string,
      "value": {
        object
      }
    }  
  
Fields  
---  
`type` |  `string` Required. Immutable. The type of the Setting. .  
`value` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. The value of the Setting.  
  
## PolicyType

The type of the policy. This denotes whether the policy is system-configured or admin-configurable.

Enums  
---  
`POLICY_TYPE_UNSPECIFIED` | Unspecified policy type.  
`SYSTEM` | Policy type denoting the system-configured policies.  
`ADMIN` | Policy type denoting the admin-configurable policies.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies/create)`

|  Create a policy.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies/delete)`

|  Delete a policy.  
  
### `[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies/get)`

|  Get a policy.  
  
### `[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies/list)`

|  List policies.  
  
### `[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies/patch)`

|  Update a policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-22 UTC."],[],[]] 
