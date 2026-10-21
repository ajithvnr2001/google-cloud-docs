---
url: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups
title: REST Resource: customers.v2.Groups \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:02.420359+00:00
---

# REST Resource: customers.v2.Groups  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: customers.v2.Groups Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Group

SCIM representation of a group.

JSON representation  
---  
      
    
    {
      "schemas": [
        string
      ],
      "members": [
        {
          object ([Member](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups#Member))
        }
      ],
      "id": string,
      "externalId": string,
      "meta": {
        object ([Meta](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/Meta))
      },
      "displayName": string,
      "urn:ietf:params:scim:schemas:extension:google:2.0:CloudIdentityGroup": {
        object ([CloudIdentityGroupExtension](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups#CloudIdentityGroupExtension))
      }
    }  
  
Fields  
---  
`schemas[]` |  `string` Required. A list of URIs which indicate the namespaces of the SCIM schemas that define the attributes present in the current JSON structure. Must only contain values defined as `schema` and `schemaExtensions` for the Group ResourceType.  
`members[]` |  `object (`[Member](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups#Member)`)` Optional. The list of members in this group. This attribute is not currently returned. Group memberships can be modified through PATCH requests.  
`id` |  `string` Identifier. The unique ID for the group. The attribute characteristics are `caseExact` as `true`, a mutability of `readOnly`, and a `returned` characteristic of `always`.  
`externalId` |  `string` Optional. An identifier for the resource as defined by the provisioning client.  
`meta` |  `object (`[Meta](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/Meta)`)` Output only. Resource metadata. All sub-attributes have a mutability of `readOnly` and a `returned` characteristic of `default`.  
`displayName` |  `string` Required. The group's display name.  
`urn:ietf:params:scim:schemas:extension:google:2.0:CloudIdentityGroup` |  `object (`[CloudIdentityGroupExtension](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups#CloudIdentityGroupExtension)`)` Required. Cloud Identity specific group attributes.  
  
## Member

SCIM representation of a group member.

JSON representation  
---  
      
    
    {
      "value": string,
      "$ref": string
    }  
  
Fields  
---  
`value` |  `string` Immutable. Identifier of the member of this Group.  
`$ref` |  `string` Immutable. The URI for the member.  
  
## CloudIdentityGroupExtension

Defines the attributes for the Google Cloud Identity Group extension. The schema URN for this extension is: `urn:ietf:params:scim:schemas:extension:google:2.0:CloudIdentityGroup`.

JSON representation  
---  
      
    
    {
      "email": string,
      "description": string
    }  
  
Fields  
---  
`email` |  `string` Required. The group's email address. If your account has multiple domains, select the appropriate domain for the email address. The `email` must be unique. Group email addresses are subject to the same character usage rules as usernames. For details, see the [help center documentation](https://support.google.com/a/answer/9193374).  
`description` |  `string` Optional. An extended description to help users determine the purpose of a `Group`.Limit: 4,096 characters.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups/create)`

|  Creates a Group.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups/delete)`

|  Deletes a Group.  
  
### `[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups/get)`

|  Retrieves a Group.  
  
### `[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups/list)`

|  Retrieves a list of Groups.  
  
### `[patch](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Groups/patch)`

|  Updates a Group using SCIM patch semantics.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-08 UTC."],[],[]] 
