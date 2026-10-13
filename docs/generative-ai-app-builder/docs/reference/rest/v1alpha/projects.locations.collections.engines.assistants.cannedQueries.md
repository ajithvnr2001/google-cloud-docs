---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries
title: REST Resource: projects.locations.collections.engines.assistants.cannedQueries \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:22.762961+00:00
---

# REST Resource: projects.locations.collections.engines.assistants.cannedQueries  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  REST Resource: projects.locations.collections.engines.assistants.cannedQueries Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CannedQuery
    * JSON representation
  * CannedQueryTexts
    * JSON representation
  * SuggestedPrompt
    * JSON representation
  * AssistantCapability
    * JSON representation
  * Methods



## Resource: CannedQuery

Canned query resource of `[Assistant](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#Assistant)`. It represents a short-cut to a predefined conversation start.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "defaultTexts": {
        object ([CannedQueryTexts](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#CannedQueryTexts))
      },
      "localizedTexts": {
        string: {
          object ([CannedQueryTexts](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#CannedQueryTexts))
        },
        ...
      },
      "requiredCapabilities": [
        {
          object ([AssistantCapability](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#AssistantCapability))
        }
      ],
      "enabled": boolean,
      "googleDefined": boolean
    }  
  
Fields  
---  
`name` |  `string` Immutable. Resource name of the canned query. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}/cannedQueries/{cannedQuery}`It must be a UTF-8 encoded string with a length limit of 1024 characters.  
`displayName` |  `string` The display name of the canned query. It must be a UTF-8 encoded string with a length limit of 128 characters.  
`defaultTexts` |  `object (`[CannedQueryTexts](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#CannedQueryTexts)`)` Required. The default (non-localized) values for the text attributes.  
`localizedTexts` |  `map (key: string, value: object (`[CannedQueryTexts](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#CannedQueryTexts)`))` Optional. The translations of the text attributes. The keys should be BCP-47 language codes.  
`requiredCapabilities[]` |  `object (`[AssistantCapability](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#AssistantCapability)`)` Optional. The capabilities the Assistant needs to have to use this canned query.  
`enabled` |  `boolean` Whether this canned query is enabled.  
`googleDefined` |  `boolean` Output only. Whether this is a Google-defined, read-only canned query.  
  
## CannedQueryTexts

The text pieces for the canned query, which can be localized.

JSON representation  
---  
      
    
    {
      "title": string,
      "prefix": string,
      "suggestedPrompts": [
        {
          object ([SuggestedPrompt](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#SuggestedPrompt))
        }
      ]
    }  
  
Fields  
---  
`title` |  `string` Required. The title that is for the end user.  
`prefix` |  `string` Optional. The prefix that `suggestedPrompts` should start with.  
`suggestedPrompts[]` |  `object (`[SuggestedPrompt](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#SuggestedPrompt)`)` Required. The prompts the canned query will offer to the user.  
  
## SuggestedPrompt

A suggested prompt for the canned query.

JSON representation  
---  
      
    
    {
      "promptText": string
    }  
  
Fields  
---  
`promptText` |  `string` Required. The text of the suggested prompt.  
  
## AssistantCapability

Capability of an assistant needed to use this canned query.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "actionName": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Capability of an assistant, either an action or a tool. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`actionName` |  `string` The name of the action that the Assistant needs to have set up to use this canned query.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries/create)`

|  Creates a `[CannedQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#CannedQuery)`.  
  
### `[delete](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries/delete)`

|  Deletes a `[CannedQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#CannedQuery)`.  
  
### `[get](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries/get)`

|  Gets a `[CannedQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#CannedQuery)`.  
  
### `[list](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries/list)`

|  Lists all `[CannedQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#CannedQuery)`s under an `[Assistant](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants#Assistant)`.  
  
### `[listActiveCannedQueryUserViews](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries/listActiveCannedQueryUserViews)`

|  Lists the `[CannedQueryUserView](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries/listActiveCannedQueryUserViews#CannedQueryUserView)`s for all active `[CannedQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#CannedQuery)`s.  
  
### `[patch](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries/patch)`

|  Updates a `[CannedQuery](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines.assistants.cannedQueries#CannedQuery)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-14 UTC."],[],[]] 
