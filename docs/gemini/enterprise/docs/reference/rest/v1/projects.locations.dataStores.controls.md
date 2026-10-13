---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.controls
title: REST Resource: projects.locations.dataStores.controls \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:52.105350+00:00
---

# REST Resource: projects.locations.dataStores.controls  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.controls

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  REST Resource: projects.locations.dataStores.controls Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Control
    * JSON representation
  * Methods



## Resource: Control

Defines a conditioned behavior to employ during serving. Must be attached to a `[ServingConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs#ServingConfig)` to be considered at serving time. Permitted actions dependent on `SolutionType`.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "associatedServingConfigIds": [
        string
      ],
      "solutionType": enum ([SolutionType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SolutionType)),
      "useCases": [
        enum ([SearchUseCase](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.SearchUseCase))
      ],
      "conditions": [
        {
          object ([Condition](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.Condition))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "boostAction": {
        object ([BoostAction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.BoostAction))
      },
      "filterAction": {
        object ([FilterAction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.FilterAction))
      },
      "redirectAction": {
        object ([RedirectAction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.RedirectAction))
      },
      "synonymsAction": {
        object ([SynonymsAction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.SynonymsAction))
      },
      "promoteAction": {
        object ([PromoteAction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.PromoteAction))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Immutable. Fully qualified name `projects/*/locations/global/dataStore/*/controls/*`  
`displayName` |  `string` Required. Human readable name. The identifier used in UI views.Must be UTF-8 encoded string. Length limit is 128 characters. Otherwise an INVALID ARGUMENT error is thrown.  
`associatedServingConfigIds[]` |  `string` Output only. List of all `[ServingConfig](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs#ServingConfig)` IDs this control is attached to. May take up to 10 minutes to update after changes.  
`solutionType` |  `enum (`[SolutionType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SolutionType)`)` Required. Immutable. What solution the control belongs to.Must be compatible with vertical of resource. Otherwise an INVALID ARGUMENT error is thrown.  
`useCases[]` |  `enum (`[SearchUseCase](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.SearchUseCase)`)` Specifies the use case for the control. Affects what condition fields can be set. Only applies to `[SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`. Currently only allow one use case per control. Must be set when solutionType is `[SolutionType.SOLUTION_TYPE_SEARCH](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SolutionType#ENUM_VALUES.SOLUTION_TYPE_SEARCH)`.  
`conditions[]` |  `object (`[Condition](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.Condition)`)` Determines when the associated action will trigger.Omit to always apply the action. Currently only a single condition may be specified. Otherwise an INVALID ARGUMENT error is thrown.  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`boostAction` |  `object (`[BoostAction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.BoostAction)`)` Defines a boost-type control  
`filterAction` |  `object (`[FilterAction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.FilterAction)`)` Defines a filter-type control Currently not supported by Recommendation  
`redirectAction` |  `object (`[RedirectAction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.RedirectAction)`)` Defines a redirect-type control.  
`synonymsAction` |  `object (`[SynonymsAction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.SynonymsAction)`)` Treats a group of terms as synonyms of one another.  
`promoteAction` |  `object (`[PromoteAction](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#Control.PromoteAction)`)` Promote certain links based on predefined trigger queries.  
End of mutually exclusive fields.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.controls/create)`

|  Creates a Control.  
  
### `[delete](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.controls/delete)`

|  Deletes a Control.  
  
### `[get](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.controls/get)`

|  Gets a Control.  
  
### `[list](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.controls/list)`

|  Lists all Controls by their parent `[DataStore](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores#DataStore)`.  
  
### `[patch](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.controls/patch)`

|  Updates a Control.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
