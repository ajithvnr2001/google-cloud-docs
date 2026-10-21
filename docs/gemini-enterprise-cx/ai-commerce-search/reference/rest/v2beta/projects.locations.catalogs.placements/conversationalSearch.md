---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.placements/conversationalSearch/
title: Method: projects.locations.catalogs.placements.conversationalSearch \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:43:52.282748+00:00
---

# Method: projects.locations.catalogs.placements.conversationalSearch  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.placements/conversationalSearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.placements.conversationalSearch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Performs a conversational search.

This feature is only available for users who have Conversational placements.search enabled.

### HTTP request

`POST https://retail.googleapis.com/v2beta/{placement=projects/*/locations/*/catalogs/*/placements/*}:conversationalSearch`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`placement` |  `string` Required. The resource name of the search engine placement, such as `projects/*/locations/global/catalogs/default_catalog/placements/default_search` or `projects/*/locations/global/catalogs/default_catalog/servingConfigs/default_serving_config` This field is used to identify the serving config name and the set of models that will be used to make the search.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "branch": string,
      "query": string,
      "pageCategories": [
        string
      ],
      "conversationId": string,
      "searchParams": {
        object ([SearchParams](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SearchParams))
      },
      "visitorId": string,
      "userInfo": {
        object ([UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents#UserInfo))
      },
      "conversationalFilteringSpec": {
        object ([ConversationalFilteringSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalFilteringSpec))
      },
      "userLabels": {
        string: string,
        ...
      },
      "safetySettings": [
        {
          object ([SafetySetting](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SafetySetting))
        }
      ],
      "suggestConversationQuery": boolean
    }  
  
Fields  
---  
`branch` |  `string` Required. The branch resource name, such as `projects/*/locations/global/catalogs/default_catalog/branches/0`.Use "default_branch" as the branch ID or leave this field empty, to search products under the default branch.  
`query` |  `string` Optional. Raw search query to be searched for.If this field is empty, the request is considered a category browsing request.  
`pageCategories[]` |  `string` Optional. The categories associated with a category page. Must be set for category navigation queries to achieve good search quality. The format should be the same as `[UserEvent.page_categories](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents#UserEvent.FIELDS.page_categories)`;To represent the full path of category, use the '>' sign, with one space on each side, to separate different hierarchies. If '>' is part of the category name, replace it with other character(s).Category pages include special pages such as sales or promotions. For instance, a special sale page may have the category hierarchy: "pageCategories" : ["Sales > 2017 Black Friday Deals"].  
`conversationId` |  `string` Optional. This field specifies the conversation id, which maintains the state of the conversation between client side and server side. Use the value from the previous `[ConversationalSearchResponse.conversation_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalSearchResponse#FIELDS.conversation_id)`. For the initial request, this should be empty.  
`searchParams` |  `object (`[SearchParams](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SearchParams)`)` Optional. placements.search parameters.  
`visitorId` |  `string` Required. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.This should be the same identifier as `[UserEvent.visitor_id](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents#UserEvent.FIELDS.visitor_id)`.The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned.  
`userInfo` |  `object (`[UserInfo](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents#UserInfo)`)` Optional. User information.  
`conversationalFilteringSpec` |  `object (`[ConversationalFilteringSpec](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalFilteringSpec)`)` Optional. This field specifies all conversational filtering related parameters.  
`userLabels` |  `map (key: string, value: string)` Optional. The user labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique. However, you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details.  
`safetySettings[]` |  `object (`[SafetySetting](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/SafetySetting)`)` Optional. The safety settings to be applied to the generated content.  
`suggestConversationQuery` |  `boolean` Optional. If set to true, the service will suggest conversation queries based on the user query.  
  
### Response body

If successful, the response body contains a stream of `[ConversationalSearchResponse](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/ConversationalSearchResponse)` instances.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
