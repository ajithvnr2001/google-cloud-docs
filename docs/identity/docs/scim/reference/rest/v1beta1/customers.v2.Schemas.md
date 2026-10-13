---
url: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Schemas
title: REST Resource: customers.v2.Schemas \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:39:04.062614+00:00
---

# REST Resource: customers.v2.Schemas  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Schemas

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: customers.v2.Schemas Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Schema

From [RFC 7643 Section 7](https://datatracker.ietf.org/doc/html/rfc7643#section-7). Specifies the metadata about a schema.

JSON representation  
---  
      
    
    {
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Schemas#Attribute))
        }
      ],
      "id": string,
      "name": string,
      "description": string
    }  
  
Fields  
---  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Schemas#Attribute)`)` Required. The schema's list of attributes.  
`id` |  `string` Required. The unique URI of the schema. When applicable, service providers must specify the URI, for example, `urn:ietf:params:scim:schemas:core:2.0:User`. Unlike most other schemas, which use some sort of Globally Unique Identifier (GUID) for the `id`, the schema `id` is a URI so that it can be registered and is portable between different service providers and clients.  
`name` |  `string` Optional. The schema's human-readable name. When applicable, service providers must specify the name, for example, `User` or `Group`.  
`description` |  `string` Optional. The schema's human-readable description. When applicable, service providers must specify the description.  
  
## Attribute

From [RFC 7643 Section 7](https://datatracker.ietf.org/doc/html/rfc7643#section-7:~:text=attribute%20is%20defined%3A-,attributes,-A%20complex%20type). Defines the characteristics of an attribute.

JSON representation  
---  
      
    
    {
      "subAttributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Schemas#Attribute))
        }
      ],
      "canonicalValues": [
        string
      ],
      "referenceTypes": [
        string
      ],
      "name": string,
      "type": string,
      "multiValued": boolean,
      "description": string,
      "required": boolean,
      "caseExact": boolean,
      "mutability": string,
      "returned": string,
      "uniqueness": string
    }  
  
Fields  
---  
`subAttributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Schemas#Attribute)`)` When an attribute is of type `complex`, `subAttributes` defines a set of sub-attributes. `subAttributes` has the same schema sub-attributes as `attributes`.  
`canonicalValues[]` |  `string` Optional. A collection of suggested canonical values that can be used (for example, `work` and `home`). In some cases, service providers might choose to ignore unsupported values.  
`referenceTypes[]` |  `string` A multi-valued array of JSON strings that indicate the SCIM resource types that can be referenced. Valid values are as follows:

  * A SCIM resource type (for example, `User` or `Group`),
  * `external` \- indicating that the resource is an external resource (for example, a photo), or
  * `uri` \- indicating that the reference is to a service endpoint or an identifier (for example, a schema URN).

This attribute is only applicable for attributes that are of type `reference` (Section 2.3.7).  
`name` |  `string` The attribute's name.  
`type` |  `string` The attribute's data type. Valid values are `string`, `boolean`, `decimal`, `integer`, `dateTime`, `reference`, and `complex`. When an attribute is of type `complex`, there should be a corresponding schema attribute `subAttributes` defined, listing the sub-attributes of the attribute.  
`multiValued` |  `boolean` Indicates the attribute's plurality.  
`description` |  `string` The attribute's human-readable description. When applicable, service providers must specify the description.  
`required` |  `boolean` Specifies whether or not the attribute is required.  
`caseExact` |  `boolean` Specifies whether or not a string attribute is case sensitive. The server uses case sensitivity when evaluating filters. For attributes that are case exact, the server preserves case for any value submitted. If the attribute is case-insensitive, the server might alter case for a submitted value. Case sensitivity also impacts how attribute values might be compared against filter values (see [RFC 7644 Section 3.4.2.2](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)).As per [RFC 7643 Section 2.3.6](https://datatracker.ietf.org/doc/html/rfc7643#section-2.3.6) and [RFC 7643 Section 2.3.7](https://datatracker.ietf.org/doc/html/rfc7643#section-2.3.7), `binary` and `reference` types are `caseExact`.  
`mutability` |  `string` A single keyword indicating the circumstances under which the value of the attribute can be (re)defined:

  * `readOnly`: The attribute is not modifiable.
  * `readWrite`: Default. The attribute can be updated and read at any time.
  * `immutable`: The attribute can be defined at resource creation (for example, POST) or at record replacement via a request (for example, a PUT). The attribute is not modifiable after initial definition.
  * `writeOnly`: The attribute can be updated at any time. Attribute values are not returned (for example, because the value is a stored hash). Note: An attribute with a mutability of `writeOnly` usually also has a returned setting of `never`.

  
`returned` |  `string` A single keyword that indicates when an attribute and associated values are returned in response to a GET request or in response to a PUT, POST, or PATCH request. Valid keywords are as follows:

  * `always`: The attribute is always returned, regardless of the contents of the `attributes` parameter. For example, `id` is always returned to identify a SCIM resource.
  * `never`: The attribute is never returned. This might occur because the original attribute value (for example, a hashed value) is not retained by the service provider. A service provider can allow attributes to be used in a search filter.
  * `default`: Default. The attribute is returned by default in all SCIM operation responses where attribute values are returned. If the GET request `attributes` parameter is specified, attribute values are only returned if the attribute is named in the `attributes` parameter.
  * `request`: The attribute is returned in response to any PUT, POST, or PATCH operations if the attribute was specified by the client (for example, the attribute was modified). The attribute is returned in a SCIM query operation only if specified in the `attributes` parameter.

  
`uniqueness` |  `string` A single keyword value that specifies how the service provider enforces uniqueness of attribute values. A server might reject an invalid value based on uniqueness by returning HTTP response code `400 Bad Request`. A client can enforce uniqueness on the client side to a greater degree than the service provider enforces. For example, a client could make a value unique while the server has uniqueness of `none`. Valid keywords are as follows:

  * `none`: Default. The values are not intended to be unique in any way.
  * `server`: The value should be unique within the context of the current SCIM endpoint (or tenancy) and might be globally unique (for example, a user name, email address, or other server-generated key or counter). No two resources on the same server should possess the same value.
  * `global`: The value should be globally unique (for example, an email address, a GUID, or other value). No two resources on any server should possess the same value.

As specified in [RFC 7643 Section 2.3](https://datatracker.ietf.org/doc/html/rfc7643#section-2.3), `Boolean`, `DateTime`, `Binary`, and `Complex` data types do not have uniqueness.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Schemas/get)`

|  Retrieves a Schema.  
  
### `[list](https://docs.cloud.google.com/identity/docs/scim/reference/rest/v1beta1/customers.v2.Schemas/list)`

|  Retrieves all Schemas.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-08 UTC."],[],[]] 
