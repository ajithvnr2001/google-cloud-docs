---
url: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services
title: REST Resource: projects.locations.services \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:39:14.829732+00:00
---

# REST Resource: projects.locations.services  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ APIs and Reference ](https://docs.cloud.google.com/marketplace/docs/partners/commerce-procurement-api/reference)



Send feedback 

#  REST Resource: projects.locations.services Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Service
    * JSON representation
  * DocumentRequirement
    * JSON representation
  * DocumentTypeRequirement
    * JSON representation
  * RequirementLevel
  * ProductType
  * Methods



## Resource: Service

Message describing Service resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "documentRequirement": {
        object ([DocumentRequirement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services#DocumentRequirement))
      },
      "productType": enum ([ProductType](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services#ProductType))
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of resource.  
`title` |  `string` Output only. Title of the service.Not included for `SERVICE_VIEW_BASIC`.  
`documentRequirement` |  `object (`[DocumentRequirement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services#DocumentRequirement)`)` Output only. Document requirement for private offers on this service.Constraints that apply to every service, such as the restriction against attaching both a standard and a custom EULA, are documented on `PrivateOfferDocument` and are not represented here.  
`productType` |  `enum (`[ProductType](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services#ProductType)`)` Output only. Type of the product this service commercializes.  
  
## DocumentRequirement

Requirements and constraints for documents attached to private offers.

JSON representation  
---  
      
    
    {
      "documentTypeRequirements": [
        {
          object ([DocumentTypeRequirement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services#DocumentTypeRequirement))
        }
      ]
    }  
  
Fields  
---  
`documentTypeRequirements[]` |  `object (`[DocumentTypeRequirement](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services#DocumentTypeRequirement)`)` Document requirements for private offers on this service.Each document type appears at most once. The order of entries is not significant. A document type that is not present in this list is not permitted for private offers on this service.  
  
## DocumentTypeRequirement

Requirement specification for a specific document type.

JSON representation  
---  
      
    
    {
      "documentType": enum ([DocumentType](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/DocumentType)),
      "requirementLevel": enum ([RequirementLevel](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services#RequirementLevel))
    }  
  
Fields  
---  
`documentType` |  `enum (`[DocumentType](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/DocumentType)`)` The document type.  
`requirementLevel` |  `enum (`[RequirementLevel](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services#RequirementLevel)`)` The requirement level for this document type.  
  
## RequirementLevel

Requirement level for the document type.

Enums  
---  
`REQUIREMENT_LEVEL_UNSPECIFIED` | Unspecified requirement level. Do not use.  
`REQUIRED` | The document type is mandatory for private offers on this service. Exactly one document of this type must be attached.  
`OPTIONAL` | The document type is optional for private offers on this service. At most one document of this type may be attached.  
`NOT_ALLOWED` | The document type is not permitted for private offers on this service. No document of this type may be attached.A document type omitted from `documentTypeRequirements` is also not permitted. This value is used to state the restriction explicitly.  
  
## ProductType

The type of the product this service commercializes.

Every service has a type, but only the types listed below are exposed. A service whose type is not one of the listed values reports `PRODUCT_TYPE_UNSPECIFIED`.

Values may be added over time. Clients must handle unrecognized values. When new values are added, the ProductType for an existing service may change. Clients must also be able to handle a change in ProductType.

Enums  
---  
`PRODUCT_TYPE_UNSPECIFIED` | The service has a type, but it is not one of the types exposed below.  
`SOFTWARE_AS_A_SERVICE` | Represents a software-as-a-service product. See <https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas>  
`ANALYTICS_HUB_LISTING` | Represents a data product on BigQuery sharing (formerly Analytics Hub). See <https://docs.cloud.google.com/marketplace/docs/partners/data>  
`PROFESSIONAL_SERVICES` | Represents a professional services product. See <https://docs.cloud.google.com/marketplace/docs/partners/professional-services>  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services/get)`

|  Gets details of a single Service.  
  
### `[list](https://docs.cloud.google.com/marketplace/docs/partners/commerce-producer-api/reference/rest/v1beta/projects.locations.services/list)`

|  Lists Services in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
