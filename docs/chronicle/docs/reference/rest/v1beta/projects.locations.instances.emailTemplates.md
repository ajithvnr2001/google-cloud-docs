---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates
title: REST Resource: projects.locations.instances.emailTemplates \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:53.560310+00:00
---

# REST Resource: projects.locations.instances.emailTemplates  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.emailTemplates Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EmailTemplate
    * JSON representation
  * EmailTemplateType
  * Methods



## Resource: EmailTemplate

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. EmailTemplate resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "templateType": enum ([EmailTemplateType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates#EmailTemplateType)),
      "content": string,
      "displayName": string,
      "author": string,
      "environments": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the EmailTemplate. Format: projects/{project}/locations/{location}/instances/{instance}/emailTemplates/{emailTemplate}  
`templateType` |  `enum (`[EmailTemplateType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates#EmailTemplateType)`)` Required. Type of the content  
`content` |  `string` Required. Content of the EmailTemplate.  
`displayName` |  `string` Required. Display name of the EmailTemplate.  
`author` |  `string` Output only. Name of creator user.  
`environments` |  `string` Required. The environments to which the custom list is associated.  
  
## EmailTemplateType

The resource inner type of the EmailTemplate.

Enums  
---  
`EMAIL_TEMPLATE_TYPE_UNSPECIFIED` | unspecified value  
`TEMPLATE` | simple text content  
`HTML_FORMAT` | text content in HTML format  
  
## Methods  
  
---  
  
### `[batchDelete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates/batchDelete)`

|  Deletes multiple email templates in a single operation.  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates/create)`

|  Creates a new EmailTemplate.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates/delete)`

|  Deletes a specific EmailTemplate.  
  
### `[export](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates/export)`

|  Exports selected email templates as a CSV file.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates/get)`

|  Gets a single EmailTemplate by its resource name.  
  
### `[import](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates/import)`

|  Imports multiple email templates from a CSV file.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates/list)`

|  Lists all EmailTemplates available in the instance.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.emailTemplates/patch)`

|  Updates an existing EmailTemplate.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-20 UTC."],[],[]] 
