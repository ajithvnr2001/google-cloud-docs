---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks
title: REST Resource: projects.locations.instances.contentHub.contentPacks \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:30.022672+00:00
---

# REST Resource: projects.locations.instances.contentHub.contentPacks  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.contentHub.contentPacks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ContentPack
    * JSON representation
  * ContentPackIntegrationItem
    * JSON representation
  * ContentPackItem
    * JSON representation
  * ContentPackType
  * Methods



## Resource: ContentPack

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. ContentPack - Chronicle SOAR Content Pack.

JSON representation  
---  
      
    
    {
      "name": string,
      "title": string,
      "categories": [
        string
      ],
      "description": string,
      "videoUri": string,
      "uploader": string,
      "integrations": [
        {
          object ([ContentPackIntegrationItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackIntegrationItem))
        }
      ],
      "connectorDefinitions": [
        {
          object ([ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem))
        }
      ],
      "connectorInstances": [
        {
          object ([ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem))
        }
      ],
      "testCases": [
        {
          object ([ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem))
        }
      ],
      "playbooks": [
        {
          object ([ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem))
        }
      ],
      "detectionRules": [
        {
          object ([ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem))
        }
      ],
      "searchQueries": [
        {
          object ([ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem))
        }
      ],
      "dashboards": [
        {
          object ([ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem))
        }
      ],
      "type": enum ([ContentPackType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackType)),
      "identifier": string,
      "ruleSets": [
        {
          object ([ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem))
        }
      ],
      "sourceType": enum ([ContentSourceType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/ContentSourceType)),
      "custom": boolean,
      "highlighted": boolean,
      "ontology": boolean,
      "conflicts": boolean,
      "deployed": boolean,
      "preInstallationGuidance": string,
      "postInstallationGuidance": string,
      "community": boolean,
      "image": string,
      "externalLinkUrl": string,
      "requiresIngestion": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the content pack. Format: projects/{project}/locations/{location}/instances/{instance}/contentHub/content-packs/{content-pack}  
`title` |  `string` Output only. The title of the content pack, limited to 200 characters.  
`categories[]` |  `string` Output only. Categories used for filtering. Each category name is limited to 50 characters.  
`description` |  `string` Output only. Provides a detailed description of the content-pack, suitable for display in a list view. Limited to 200 characters.  
`videoUri` |  `string` Output only. URL of e video associated with this content pack. Must be a valid URL with a maximum length of 2048 characters.  
`uploader` |  `string` Output only. The uploader of the content pack, might not be a registered user of the platform.  
`integrations[]` |  `object (`[ContentPackIntegrationItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackIntegrationItem)`)` Output only. The integrations of the content pack  
`connectorDefinitions[]` |  `object (`[ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem)`)` Output only. The connectors definitions of the content pack  
`connectorInstances[]` |  `object (`[ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem)`)` Output only. The connectors instances of the content pack  
`testCases[]` |  `object (`[ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem)`)` Output only. The test cases of the content pack  
`playbooks[]` |  `object (`[ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem)`)` Output only. The playbooks of the content pack  
`detectionRules[]` |  `object (`[ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem)`)` Output only. The detection rules of the content pack  
`searchQueries[]` |  `object (`[ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem)`)` Output only. The search query records of the content pack  
`dashboards[]` |  `object (`[ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem)`)` Output only. The dashboards records of the content pack  
`type` |  `enum (`[ContentPackType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackType)`)` Output only. Enum type of content pack  
`identifier` |  `string` Output only. The identifier of the content pack.  
`ruleSets[]` |  `object (`[ContentPackItem](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks#ContentPackItem)`)` Output only. The rule sets of the content pack  
`sourceType` |  `enum (`[ContentSourceType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/ContentSourceType)`)` Output only. The source type of the content pack.  
`custom` |  `boolean` Output only. Determines if the content-pack is custom or commercial.  
`highlighted` |  `boolean` Output only. Represent if the content pack is marked as highlighted. Used by a client.  
`ontology` |  `boolean` Output only. Represents if Content Pack has ontology  
`conflicts` |  `boolean` Output only. Represents if Content Pack has ontology conflicts  
`deployed` |  `boolean` Output only. Represents if Content Pack is deployed  
`preInstallationGuidance` |  `string` Output only. a guidance for the customer before installing the content pack.  
`postInstallationGuidance` |  `string` Output only. a guidance for the customer after installing the content pack.  
`community` |  `boolean` Output only. Represents if Content Pack is available in community  
`image` |  `string` Output only. The image of the content pack.  
`externalLinkUrl` |  `string` Output only. The external link of the content pack.  
`requiresIngestion` |  `boolean` Output only. Represents if the content pack requires data ingestion.  
  
## ContentPackIntegrationItem

ContentPackIntegrationItem - Represents an integration item of a content pack.

JSON representation  
---  
      
    
    {
      "id": string,
      "title": string,
      "version": string,
      "custom": boolean,
      "iconSvg": string,
      "ontology": boolean,
      "conflicts": boolean
    }  
  
Fields  
---  
`id` |  `string` Output only. The unique ID of the content pack item.  
`title` |  `string` Output only. The display name of the item  
`version` |  `string` Output only. Represents the integration version  
`custom` |  `boolean` Output only. Represent if the content item is custom or commercial  
`iconSvg` |  `string` Output only. SVG icon for representation, limited to 1MB.  
`ontology` |  `boolean` Output only. Represents if integration has ontology  
`conflicts` |  `boolean` Output only. Represents if integration ontology has conflicts  
  
## ContentPackItem

ContentPackItem - Represents a content pack item.

JSON representation  
---  
      
    
    {
      "id": string,
      "title": string,
      "custom": boolean
    }  
  
Fields  
---  
`id` |  `string` Output only. The unique ID of the content pack item.  
`title` |  `string` Output only. The display name of the item  
`custom` |  `boolean` Output only. Represent if the content item is custom or commercial  
  
## ContentPackType

content pack type enum

Enums  
---  
`CONTENT_PACK_TYPE_UNSPECIFIED` | Unspecified content pack type  
`SOAR_LEGACY` | Soar legacy content pack  
`SEC_OPS_USE_CASE` | SecOps use case content pack  
`PRODUCT` | Product content pack  
`ONBOARDING` | Onboarding content pack  
`EXTERNAL` | External content pack  
  
## Methods  
  
---  
  
### `[add](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks/add)`

|  Creates a new custom ContentPack.  
  
### `[alignPlaybooks](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks/alignPlaybooks)`

|  Aligns playbooks in a content pack with configured integration instances.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks/delete)`

|  Deletes a specific ContentPack.  
  
### `[deployConnectorInstances](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks/deployConnectorInstances)`

|  Deploys connector instances from a content pack.  
  
### `[deployPlaybooks](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks/deployPlaybooks)`

|  Deploys playbooks contained within a content pack.  
  
### `[deployTestCases](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks/deployTestCases)`

|  Deploys test cases from a content pack into the SecOps instance.  
  
### `[download](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks/download)`

|  Exports a content pack as a ZIP file.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks/get)`

|  Gets a single `ContentPack` by its resource name.  
  
### `[installIntegration](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks/installIntegration)`

|  Installs a specific integration from a content pack.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks/list)`

|  Lists `ContentPacks` available in the Content Hub.  
  
### `[markAsDeployed](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks/markAsDeployed)`

|  Marks a content pack as fully deployed.  
  
### `[upload](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.contentHub.contentPacks/upload)`

|  Imports a content pack from a ZIP file (up to 500MB).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-18 UTC."],[],[]] 
