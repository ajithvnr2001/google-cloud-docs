---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates
title: REST Resource: projects.locations.deidentifyTemplates \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:29:33.243302+00:00
---

# REST Resource: projects.locations.deidentifyTemplates  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Reference ](https://docs.cloud.google.com/sensitive-data-protection/docs/apis)



Send feedback 

#  REST Resource: projects.locations.deidentifyTemplates Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DeidentifyTemplate
    * JSON representation
  * Methods



## Resource: DeidentifyTemplate

DeidentifyTemplates contains instructions on how to de-identify content. See <https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-templates> to learn more.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "deidentifyConfig": {
        object ([DeidentifyConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.DeidentifyConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The template name.The template will have one of the following formats: `projects/PROJECT_ID/deidentifyTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/deidentifyTemplates/TEMPLATE_ID`  
`displayName` |  `string` Display name (max 256 chars).  
`description` |  `string` Short description (max 256 chars).  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation timestamp of an inspectTemplate.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update timestamp of an inspectTemplate.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deidentifyConfig` |  `object (`[DeidentifyConfig](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.DeidentifyConfig)`)` The core content of the template.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates/create)`

|  Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage.  
  
### `[delete](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates/delete)`

|  Deletes a DeidentifyTemplate.  
  
### `[get](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates/get)`

|  Gets a DeidentifyTemplate.  
  
### `[list](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates/list)`

|  Lists DeidentifyTemplates.  
  
### `[patch](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.locations.deidentifyTemplates/patch)`

|  Updates the DeidentifyTemplate.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
