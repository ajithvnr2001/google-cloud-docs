---
url: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ResourceTypes
title: REST Resource: customers.v2.ResourceTypes \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:59.180880+00:00
---

# REST Resource: customers.v2.ResourceTypes  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ResourceTypes

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: customers.v2.ResourceTypes Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: ResourceType

From [RFC 7643 section 6](https://datatracker.ietf.org/doc/html/rfc7643#section-6). Specifies the metadata about a resource type.

JSON representation  
---  
      
    
    {
      "schemas": [
        string
      ],
      "schemaExtensions": [
        {
          object ([SchemaExtension](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ResourceTypes#SchemaExtension))
        }
      ],
      "name": string,
      "id": string,
      "description": string,
      "endpoint": string,
      "schema": string,
      "meta": {
        object ([Meta](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/Meta))
      }
    }  
  
Fields  
---  
`schemas[]` |  `string` Output only. The `schemas` attribute contains URIs that are used to indicate the namespaces of the SCIM schemas that define the attributes present in the current JSON structure.  
`schemaExtensions[]` |  `object (`[SchemaExtension](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ResourceTypes#SchemaExtension)`)` Output only. A list of schema extensions for this resource type.  
`name` |  `string` Output only. The resource type name. For example, `User` or `Group`.  
`id` |  `string` Identifier. The resource type's unique ID. This is the same value as the `name` attribute.  
`description` |  `string` Output only. The resource type's human-readable description.  
`endpoint` |  `string` Output only. The resource type's HTTP-addressable endpoint relative to the base URL.  
`schema` |  `string` Output only. The resource type's primary/base schema URI.  
`meta` |  `object (`[Meta](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/Meta)`)` Output only. Resource metadata assigned by the service provider.  
  
## SchemaExtension

From [RFC 7643 Section 6](https://datatracker.ietf.org/doc/html/rfc7643#section-6:~:text=Schema%22%20resource.%0A%20%20%20%20%20%20REQUIRED.-,schemaExtensions,-A%20list%20of). Defines a schema extension supported or required for a SCIM resource type.

JSON representation  
---  
      
    
    {
      "schema": string,
      "required": boolean
    }  
  
Fields  
---  
`schema` |  `string` Required. The URI of an extended schema, for example, `urn:edu:2.0:Staff`. This must be equal to the `id` attribute of a `Schema` resource.  
`required` |  `boolean` Required. Specifies whether or not the schema extension is required for the resource type. If `true`, a resource of this type must include this schema extension and also include any attributes declared as required in this schema extension. If `false`, a resource of this type may omit this schema extension.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ResourceTypes/get)`

|  Retrieves a specific resource type.  
  
### `[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1/customers.v2.ResourceTypes/list)`

|  Retrieves all resource types.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-08 UTC."],[],[]] 
