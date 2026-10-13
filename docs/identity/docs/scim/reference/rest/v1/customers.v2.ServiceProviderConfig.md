---
url: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig
title: REST Resource: customers.v2.ServiceProviderConfig \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:00.240808+00:00
---

# REST Resource: customers.v2.ServiceProviderConfig  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: customers.v2.ServiceProviderConfig Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: ServiceProviderConfig

From [RFC 7643 section 5](https://datatracker.ietf.org/doc/html/rfc7643#section-5). The service provider configuration resource enables a service provider to discover SCIM specification features in a standardized form as well as provide additional implementation details to clients.

JSON representation  
---  
      
    
    {
      "schemas": [
        string
      ],
      "authenticationSchemes": [
        {
          object ([AuthenticationScheme](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#AuthenticationScheme))
        }
      ],
      "documentationUri": string,
      "patch": {
        object ([PatchFeature](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#PatchFeature))
      },
      "bulk": {
        object ([BulkFeature](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#BulkFeature))
      },
      "filter": {
        object ([FilterFeature](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#FilterFeature))
      },
      "changePassword": {
        object ([ChangePasswordFeature](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#ChangePasswordFeature))
      },
      "sort": {
        object ([SortFeature](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#SortFeature))
      },
      "etag": {
        object ([EtagFeature](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#EtagFeature))
      },
      "meta": {
        object ([Meta](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/Meta))
      }
    }  
  
Fields  
---  
`schemas[]` |  `string` Output only. The `schemas` attribute contains URIs that are used to indicate the namespaces of the SCIM schemas that define the attributes present in the current JSON structure.  
`authenticationSchemes[]` |  `object (`[AuthenticationScheme](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#AuthenticationScheme)`)` Output only. A multi-valued complex type that specifies supported authentication schemes.  
`documentationUri` |  `string` Output only. An HTTP-addressable URL pointing to the service provider's human-consumable help documentation.  
`patch` |  `object (`[PatchFeature](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#PatchFeature)`)` Output only. A complex type that specifies PATCH feature support.  
`bulk` |  `object (`[BulkFeature](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#BulkFeature)`)` Output only. A complex type that specifies bulk operation support.  
`filter` |  `object (`[FilterFeature](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#FilterFeature)`)` Output only. A complex type that specifies filter support.  
`changePassword` |  `object (`[ChangePasswordFeature](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#ChangePasswordFeature)`)` Output only. A complex type that specifies change password support.  
`sort` |  `object (`[SortFeature](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#SortFeature)`)` Output only. A complex type that specifies sort support.  
`etag` |  `object (`[EtagFeature](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig#EtagFeature)`)` Output only. A complex type that specifies ETag support.  
`meta` |  `object (`[Meta](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/Meta)`)` Output only. Resource metadata assigned by the service provider.  
  
## PatchFeature

A complex type that specifies PATCH feature support.

JSON representation  
---  
      
    
    {
      "supported": boolean
    }  
  
Fields  
---  
`supported` |  `boolean` Output only. Specifies whether or not the operation is supported.  
  
## BulkFeature

A complex type that specifies bulk operation support.

JSON representation  
---  
      
    
    {
      "supported": boolean,
      "maxOperations": integer,
      "maxPayloadSize": integer
    }  
  
Fields  
---  
`supported` |  `boolean` Output only. Specifies whether or not the operation is supported.  
`maxOperations` |  `integer` Output only. Specifies the maximum number of operations.  
`maxPayloadSize` |  `integer` Output only. Specifies the maximum payload size in bytes.  
  
## FilterFeature

A complex type that specifies filter support.

JSON representation  
---  
      
    
    {
      "supported": boolean,
      "maxResults": integer
    }  
  
Fields  
---  
`supported` |  `boolean` Output only. Specifies whether or not the operation is supported.  
`maxResults` |  `integer` Output only. Specifies the maximum number of results.  
  
## ChangePasswordFeature

A complex type that specifies change password support.

JSON representation  
---  
      
    
    {
      "supported": boolean
    }  
  
Fields  
---  
`supported` |  `boolean` Output only. Specifies whether or not the operation is supported.  
  
## SortFeature

A complex type that specifies sort support.

JSON representation  
---  
      
    
    {
      "supported": boolean
    }  
  
Fields  
---  
`supported` |  `boolean` Output only. Specifies whether or not the operation is supported.  
  
## EtagFeature

A complex type that specifies ETag support.

JSON representation  
---  
      
    
    {
      "supported": boolean
    }  
  
Fields  
---  
`supported` |  `boolean` Output only. Specifies whether or not the operation is supported.  
  
## AuthenticationScheme

A multi-valued complex type that specifies supported authentication schemes.

JSON representation  
---  
      
    
    {
      "type": string,
      "name": string,
      "description": string,
      "specUri": string,
      "documentationUri": string,
      "primary": boolean
    }  
  
Fields  
---  
`type` |  `string` Output only. The authentication scheme type.  
`name` |  `string` Output only. The name of the authentication scheme.  
`description` |  `string` Output only. A description of the authentication scheme.  
`specUri` |  `string` Output only. An HTTP-addressable URL pointing to the authentication scheme's specification.  
`documentationUri` |  `string` Output only. An HTTP-addressable URL pointing to the authentication scheme's documentation.  
`primary` |  `boolean` Output only. Indicates the `primary` or preferred authentication scheme.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ServiceProviderConfig/get)`

|  Retrieves the Service Provider Configuration.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-08 UTC."],[],[]] 
