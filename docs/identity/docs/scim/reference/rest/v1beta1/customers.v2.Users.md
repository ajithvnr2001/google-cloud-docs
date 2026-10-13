---
url: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users
title: REST Resource: customers.v2.Users \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:05.303736+00:00
---

# REST Resource: customers.v2.Users  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: customers.v2.Users Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: User

SCIM representation of a user.

JSON representation  
---  
      
    
    {
      "schemas": [
        string
      ],
      "emails": [
        {
          object ([Email](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Email))
        }
      ],
      "addresses": [
        {
          object ([Address](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Address))
        }
      ],
      "phoneNumbers": [
        {
          object ([Phone](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Phone))
        }
      ],
      "groups": [
        {
          object ([GroupReference](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#GroupReference))
        }
      ],
      "id": string,
      "externalId": string,
      "meta": {
        object ([Meta](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/Meta))
      },
      "userName": string,
      "name": {
        object ([Name](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Name))
      },
      "displayName": string,
      "active": boolean,
      "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
        object ([EnterpriseUserExtension](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#EnterpriseUserExtension))
      }
    }  
  
Fields  
---  
`schemas[]` |  `string` Required. A list of URIs which indicate the namespaces of the SCIM schemas that define the attributes present in the current JSON structure. Must only contain values defined as `schema` and `schemaExtensions` for the User ResourceType.  
`emails[]` |  `object (`[Email](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Email)`)` Optional. The list of the user's email addresses. The maximum allowed data size is 10KB. The email corresponding to `userName` will automatically be added to this list with its `primary` sub-attribute set to `true`. This primary email entry is read-only and cannot be modified through this attribute.  
`addresses[]` |  `object (`[Address](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Address)`)` Optional. The list of the user's physical addresses. The maximum allowed data size is 10KB.  
`phoneNumbers[]` |  `object (`[Phone](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Phone)`)` Optional. A list of the user's phone numbers. The maximum allowed data size is 1KB.  
`groups[]` |  `object (`[GroupReference](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#GroupReference)`)` Output only. The list of groups the user has direct membership in, truncated to a maximum of 1000 groups.This attribute is not returned by default and must be requested using the `attributes` query parameter. Reading this attribute requires customer allowlisting. Please contact support to explain your use case and request access.  
`id` |  `string` Identifier. The unique ID for the user. The attribute characteristics are `caseExact` as `true`, a mutability of `readOnly`, and a `returned` characteristic of `always`.  
`externalId` |  `string` Optional. A client-defined identifier for the SCIM user. This field is case-sensitive and mutable. The client is responsible for ensuring uniqueness, as the server does not enforce it.  
`meta` |  `object (`[Meta](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/Meta)`)` Output only. A complex attribute containing resource metadata. All `meta` sub-attributes are assigned by the service provider (have a `mutability` of `readOnly`), and all of these sub-attributes have a `returned` characteristic of `default`. This attribute is ignored when provided by clients.  
`userName` |  `string` Required. The user's primary email address. Used as the unique identifier for the user.  
`name` |  `object (`[Name](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#Name)`)` Required. The user's name.  
`displayName` |  `string` Optional. The user's display name. Limit: 256 characters.  
`active` |  `boolean` Optional. The user's account status (`false` means the account is suspended). Default: `true`.  
`urn:ietf:params:scim:schemas:extension:enterprise:2.0:User` |  `object (`[EnterpriseUserExtension](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users#EnterpriseUserExtension)`)` Optional. SCIM Enterprise User extension attributes.  
  
## Name

SCIM representation of a User's name.

JSON representation  
---  
      
    
    {
      "familyName": string,
      "givenName": string
    }  
  
Fields  
---  
`familyName` |  `string` Required. The user's family name.  
`givenName` |  `string` Required. The user's given name.  
  
## Email

SCIM representation of a user's email.

JSON representation  
---  
      
    
    {
      "value": string,
      "type": string,
      "primary": boolean
    }  
  
Fields  
---  
`value` |  `string` Required. The user's email address.  
`type` |  `string` The type of the email account. Valid values are `home`, `work`, and `other`.  
`primary` |  `boolean` Output only. Indicates if this is the user's primary email. This value is set to `true` only for the email which corresponds to `userName`.  
  
## Address

SCIM representation of a user's address.

JSON representation  
---  
      
    
    {
      "formatted": string,
      "streetAddress": string,
      "locality": string,
      "region": string,
      "postalCode": string,
      "country": string,
      "type": string,
      "primary": boolean
    }  
  
Fields  
---  
`formatted` |  `string` Full address, formatted for display.  
`streetAddress` |  `string` The street address.  
`locality` |  `string` The city or locality.  
`region` |  `string` The region or state.  
`postalCode` |  `string` The postal code or zip code.  
`country` |  `string` The country.  
`type` |  `string` The type of the address. Valid values are `home`, `work`, and `other`.  
`primary` |  `boolean` Indicates if this is the user's primary address.  
  
## Phone

SCIM representation of a user's phone number.

JSON representation  
---  
      
    
    {
      "value": string,
      "type": string,
      "primary": boolean
    }  
  
Fields  
---  
`value` |  `string` Required. The phone number.  
`type` |  `string` The type of the phone number. Valid values are `home`, `work`, `mobile`, `fax`, `pager`, and `other`.  
`primary` |  `boolean` Indicates if this is the user's primary phone number.  
  
## EnterpriseUserExtension

Defines the attributes for the SCIM Enterprise User extension. The schema URN for this extension is: `urn:ietf:params:scim:schemas:extension:enterprise:2.0:User`. See [RFC 7643 Section 4.3](https://datatracker.ietf.org/doc/html/rfc7643#section-4.3) for more details.

JSON representation  
---  
      
    
    {
      "employeeNumber": string,
      "costCenter": string,
      "organization": string,
      "department": string
    }  
  
Fields  
---  
`employeeNumber` |  `string` Optional. Identifier, typically assigned by the organization, used to identify the user inside the organization.  
`costCenter` |  `string` Optional. Identifier for the cost center to which the user's expenditures are attributed.  
`organization` |  `string` Optional. The name of an organization a user belongs to.  
`department` |  `string` Optional. The name of a department user belongs to in the text format.  
  
## GroupReference

SCIM representation of a user's group membership.

JSON representation  
---  
      
    
    {
      "value": string,
      "$ref": string,
      "type": string
    }  
  
Fields  
---  
`value` |  `string` Output only. The `id` of the SCIM resource representing the group.  
`$ref` |  `string` Output only. The URI of the SCIM resource representing the group.  
`type` |  `string` Output only. The type of group membership. Valid values are `direct` and `indirect`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/create)`

|  Creates a User.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/delete)`

|  Deletes a User.  
  
### `[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/get)`

|  Retrieves a User.  
  
### `[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/list)`

|  Retrieves a list of Users.  
  
### `[patch](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Users/patch)`

|  Updates a User using SCIM patch semantics.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-08 UTC."],[],[]] 
