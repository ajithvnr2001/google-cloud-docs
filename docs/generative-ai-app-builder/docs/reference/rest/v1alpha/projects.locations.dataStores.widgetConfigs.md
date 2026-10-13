---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.widgetConfigs
title: REST Resource: projects.locations.dataStores.widgetConfigs \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:02:30.887101+00:00
---

# REST Resource: projects.locations.dataStores.widgetConfigs  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.widgetConfigs

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  REST Resource: projects.locations.dataStores.widgetConfigs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WidgetConfig
    * JSON representation
  * Methods



## Resource: WidgetConfig

WidgetConfig captures configs at the Widget level.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "enableAutocomplete": boolean,
      "fieldsUiComponentsMap": {
        string: {
          object ([UIComponentField](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.UIComponentField))
        },
        ...
      },
      "facetField": [
        {
          object ([FacetField](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.FacetField))
        }
      ],
      "dataStoreType": enum ([DataStoreType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.DataStoreType)),
      "contentSearchSpec": {
        object ([ContentSearchSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ContentSearchSpec))
      },
      "enableSummarization": boolean,
      "enableSnippetResultSummary": boolean,
      "configId": string,
      "enableQualityFeedback": boolean,
      "solutionType": enum ([SolutionType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SolutionType)),
      "industryVertical": enum ([IndustryVertical](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/IndustryVertical)),
      "allowPublicAccess": boolean,
      "allowlistedDomains": [
        string
      ],
      "enableSafeSearch": boolean,
      "enableConversationalSearch": boolean,
      "llmEnabled": boolean,
      "enableResultScore": boolean,
      "resultDisplayType": enum ([ResultDisplayType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.ResultDisplayType)),
      "minimumDataTermAccepted": boolean,
      "enableWebApp": boolean,
      "dataStoreUiConfigs": [
        {
          object ([DataStoreUiConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.DataStoreUiConfig))
        }
      ],
      "collectionComponents": [
        {
          object ([CollectionComponent](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.CollectionComponent))
        }
      ],
      "enableSearchAsYouType": boolean,
      "defaultSearchRequestOrderBy": string,
      "uiSettings": {
        object ([UiSettings](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.UiSettings))
      },
      "accessSettings": {
        object ([AccessSettings](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.AccessSettings))
      },
      "uiBranding": {
        object ([UiBrandingSettings](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.UiBrandingSettings))
      },
      "homepageSetting": {
        object ([HomepageSetting](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.HomepageSetting))
      },
      "assistantSettings": {
        object ([AssistantSettings](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.AssistantSettings))
      },
      "customerProvidedConfig": {
        object ([CustomerProvidedConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.CustomerProvidedConfig))
      },
      "enablePrivateKnowledgeGraph": boolean,
      "geminiBundle": boolean,
      "batchAuthStatuses": [
        {
          object ([BatchAuthStatus](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.BatchAuthStatus))
        }
      ],
      "nodes": [
        {
          object ([Node](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.Node))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Immutable. The full resource name of the widget config. Format: `projects/{project}/locations/{location}/collections/{collectionId}/dataStores/{dataStoreId}/widgetConfigs/{widgetConfigId}`.This field must be a UTF-8 encoded string with a length limit of 1024 characters.  
`displayName` |  `string` Required. The human readable widget config display name. Used in Discovery UI.This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp the `[WidgetConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig)` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp the `[WidgetConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig)` was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`enableAutocomplete  
**(deprecated)**` |  `boolean` This item is deprecated!Whether or not to enable autocomplete.  
`fieldsUiComponentsMap  
**(deprecated)**` |  `map (key: string, value: object (`[UIComponentField](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.UIComponentField)`))` This item is deprecated!The key is the UI component. Mock. Currently supported `title`, `thumbnail`, `url`, `custom1`, `custom2`, `custom3`.The value is the name of the field along with its device visibility.The 3 custom fields are optional and can be added or removed. `title`, `thumbnail`, `url` are required UI components that cannot be removed.  
`facetField[]  
**(deprecated)**` |  `object (`[FacetField](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.FacetField)`)` This item is deprecated!The configuration and appearance of facets in the end user view.  
`dataStoreType` |  `enum (`[DataStoreType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.DataStoreType)`)` Output only. The type of the parent data store.  
`contentSearchSpec  
**(deprecated)**` |  `object (`[ContentSearchSpec](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/ContentSearchSpec)`)` This item is deprecated!The content search spec that configs the desired behavior of content search.  
`enableSummarization  
**(deprecated)**` |  `boolean` This item is deprecated!Turn on or off summarization for the search response.  
`enableSnippetResultSummary  
**(deprecated)**` |  `boolean` This item is deprecated!Turn on or off summary for each snippets result.  
`configId` |  `string` Output only. Unique obfuscated identifier of a `[WidgetConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig)`.  
`enableQualityFeedback  
**(deprecated)**` |  `boolean` This item is deprecated!Turn on or off collecting the search result quality feedback from end users.  
`solutionType` |  `enum (`[SolutionType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/SolutionType)`)` Required. Immutable. Specifies the solution type that this WidgetConfig can be used for.  
`industryVertical` |  `enum (`[IndustryVertical](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/IndustryVertical)`)` Output only. The industry vertical that the WidgetConfig registers. The WidgetConfig industry vertical is based on the associated `[Engine](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.engines#Engine)`.  
`allowPublicAccess  
**(deprecated)**` |  `boolean` This item is deprecated!Whether allow no-auth integration with widget. If set true, public access to search or other solutions from widget is allowed without authenication token provided by customer hosted backend server.  
`allowlistedDomains[]  
**(deprecated)**` |  `string` This item is deprecated!Allowlisted domains that can load this widget.  
`enableSafeSearch  
**(deprecated)**` |  `boolean` This item is deprecated!Whether to enable safe search.  
`enableConversationalSearch  
**(deprecated)**` |  `boolean` This item is deprecated!Whether to allow conversational search (LLM, multi-turn) or not (non-LLM, single-turn).  
`llmEnabled` |  `boolean` Output only. Whether LLM is enabled in the corresponding data store.  
`enableResultScore` |  `boolean` Whether to show the result score.  
`resultDisplayType  
**(deprecated)**` |  `enum (`[ResultDisplayType](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.ResultDisplayType)`)` This item is deprecated!The type of snippet to display in UCS widget.

  * RESULT_DISPLAY_TYPE_UNSPECIFIED for existing users.
  * SNIPPET for new non-enterprise search users.
  * EXTRACTIVE_ANSWER for new enterprise search users.

  
`minimumDataTermAccepted` |  `boolean` Output only. Whether the customer accepted data use terms.  
`enableWebApp  
**(deprecated)**` |  `boolean` This item is deprecated!Whether to enable standalone web app.  
`dataStoreUiConfigs[]  
**(deprecated)**` |  `object (`[DataStoreUiConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.DataStoreUiConfig)`)` This item is deprecated!Configurable UI configurations per data store.  
`collectionComponents[]` |  `object (`[CollectionComponent](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.CollectionComponent)`)` Output only. Collection components that lists all collections and child data stores associated with the widget config, those data sources can be used for filtering in widget service APIs, users can return results that from selected data sources.For SaaS / Business engines, when `LookupWidgetConfig` is called with `view = WITH_AVAILABLE_CONNECTORS`, this list is additionally augmented with synthetic placeholder entries for connectors the caller may attach but has not yet attached (see `CollectionComponent` for the placeholder contract). The frontend can therefore render a unified list of already-attached and available-to-attach sources by iterating this single field. For Enterprise engines and for the default `view`, only already-attached connectors are returned (today's behavior).  
`enableSearchAsYouType  
**(deprecated)**` |  `boolean` This item is deprecated!Whether to enable search-as-you-type behavior for the search widget  
`defaultSearchRequestOrderBy  
**(deprecated)**` |  `string` This item is deprecated!The default ordering for search results if specified.Used to set SearchRequest#orderBy on applicable requests. <https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.servingConfigs/search#request-body>  
`uiSettings` |  `object (`[UiSettings](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.UiSettings)`)` Describes general widget search settings as seen in cloud console widget configuration page. Replaces top deprecated top level properties.  
`accessSettings` |  `object (`[AccessSettings](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.AccessSettings)`)` Will be used for all widget access settings seen in cloud console integration page. Replaces top deprecated top level properties.  
`uiBranding` |  `object (`[UiBrandingSettings](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.UiBrandingSettings)`)` Describes search widget UI branding settings, such as the widget title, logo, favicons, and colors.  
`homepageSetting` |  `object (`[HomepageSetting](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.HomepageSetting)`)` Optional. Describes the homepage settings of the widget.  
`assistantSettings` |  `object (`[AssistantSettings](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.AssistantSettings)`)` Optional. Output only. Describes the assistant settings of the widget.  
`customerProvidedConfig` |  `object (`[CustomerProvidedConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.CustomerProvidedConfig)`)` Optional. Output only. Describes the customer related configurations, currently only used for government customers. This field cannot be modified after project onboarding.  
`enablePrivateKnowledgeGraph` |  `boolean` Optional. Output only. Whether to enable private knowledge graph.  
`geminiBundle` |  `boolean` Output only. Whether the subscription is gemini bundle or not.  
`batchAuthStatuses[]` |  `object (`[BatchAuthStatus](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.BatchAuthStatus)`)` Output only. The batch authorization statuses for the widget's connectors.  
`nodes[]` |  `object (`[Node](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig.Node)`)` Output only. The nodes associated with the Widget Config.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.widgetConfigs/get)`

|  Gets a `[WidgetConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.widgetConfigs#WidgetConfig)`.  
  
### `[patch](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1alpha/projects.locations.dataStores.widgetConfigs/patch)`

|  Update a WidgetConfig.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
