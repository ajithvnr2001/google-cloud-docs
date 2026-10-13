---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.completionConfig/removeSuggestion/
title: Method: projects.locations.collections.engines.completionConfig.removeSuggestion \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:30:04.290472+00:00
---

# Method: projects.locations.collections.engines.completionConfig.removeSuggestion  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.completionConfig/removeSuggestion/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.collections.engines.completionConfig.removeSuggestion Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Removes the search history suggestion in an engine for a user. This will remove the suggestion from being returned in the `[AdvancedCompleteQueryResponse.recent_search_suggestions](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/AdvancedCompleteQueryResponse#FIELDS.recent_search_suggestions)` for this user. If the user searches the same suggestion again, the new history will override and suggest this suggestion again.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1alpha/{completionConfig=projects/*/locations/*/collections/*/engines/*/completionConfig}:removeSuggestion`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`completionConfig` |  `string` Required. The completionConfig of the parent engine resource name for which the search history suggestion is to be removed, such as `projects/*/locations/global/collections/default_collection/engines/*/completionConfig`.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "userPseudoId": string,
      "userInfo": {
        object ([UserInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/UserInfo))
      },
      "removeTime": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "searchHistorySuggestion": string,
      "removeAllSearchHistorySuggestions": boolean
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`userPseudoId` |  `string` Required. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor logs in or out of the website.This field should NOT have a fixed value such as `unknown_visitor`.This should be the same identifier as `[UserEvent.user_pseudo_id](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.userEvents#UserEvent.FIELDS.user_pseudo_id)` and `[SearchRequest.user_pseudo_id](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.user_pseudo_id)`.The field must be a UTF-8 encoded string with a length limit of 128.  
`userInfo` |  `object (`[UserInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/UserInfo)`)` Optional. Information about the end user.This should be the same identifier information as `[UserEvent.user_info](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.userEvents#UserEvent.FIELDS.user_info)` and `[SearchRequest.user_info](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.evaluations#SearchRequest.FIELDS.user_info)`.  
`removeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. Time at which the suggestion was removed. If not set, the current time will be used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
The suggestion to be removed. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`searchHistorySuggestion` |  `string` The search history suggestion to be removed.  
`removeAllSearchHistorySuggestions` |  `boolean` Remove all search history suggestions for the user.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body is empty.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.assist.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `completionConfig` resource:

  * `discoveryengine.completionConfigs.removeSuggestion`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
