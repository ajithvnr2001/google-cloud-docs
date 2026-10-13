---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/recommend/
title: Method: projects.locations.collections.dataStores.servingConfigs.recommend \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:09.948001+00:00
---

# Method: projects.locations.collections.dataStores.servingConfigs.recommend  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/recommend/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Reference ](https://docs.cloud.google.com/generative-ai-app-builder/docs/apis)



Send feedback 

#  Method: projects.locations.collections.dataStores.servingConfigs.recommend Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Makes a recommendation, which requires a contextual user event.

### HTTP request

Choose an endpoint:

globalus

  
`POST https://discoveryengine.googleapis.com/v1/{servingConfig=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}:recommend`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`servingConfig` |  `string` Required. Full resource name of a `[ServingConfig](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs#ServingConfig)`: `projects/*/locations/global/collections/*/engines/*/servingConfigs/*`, or `projects/*/locations/global/collections/*/dataStores/*/servingConfigs/*`One default serving config is created along with your recommendation engine creation. The engine ID is used as the ID of the default serving config. For example, for Engine `projects/*/locations/global/collections/*/engines/my-engine`, you can use `projects/*/locations/global/collections/*/engines/my-engine/servingConfigs/my-engine` for your `[RecommendationService.Recommend](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/recommend#google.cloud.discoveryengine.v1.RecommendationService.Recommend)` requests.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "userEvent": {
        object ([UserEvent](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent))
      },
      "pageSize": integer,
      "filter": string,
      "validateOnly": boolean,
      "params": {
        string: value,
        ...
      },
      "userLabels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`userEvent` |  `object (`[UserEvent](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent)`)` Required. Context about the user, what they are looking at and what action they took to trigger the servingConfigs.recommend request. Note that this user event detail won't be ingested to userEvent logs. Thus, a separate userEvent write request is required for event logging.Don't set `[UserEvent.user_pseudo_id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent.FIELDS.user_pseudo_id)` or `[UserEvent.user_info.user_id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserInfo.FIELDS.user_id)` to the same fixed ID for different users. If you are trying to receive non-personalized recommendations (not recommended; this can negatively impact model performance), instead set `[UserEvent.user_pseudo_id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent.FIELDS.user_pseudo_id)` to a random unique ID and leave `[UserEvent.user_info.user_id](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserInfo.FIELDS.user_id)` unset.  
`pageSize` |  `integer` Maximum number of results to return. Set this property to the number of recommendation results needed. If zero, the service chooses a reasonable default. The maximum allowed value is 100. Values above 100 are set to 100.  
`filter` |  `string` Filter for restricting recommendation results with a length limit of 5,000 characters. Currently, only filter expressions on the `filterTags` attribute is supported.Examples:

  * `(filterTags: ANY("Red", "Blue") OR filterTags: ANY("Hot", "Cold"))`
  * `(filterTags: ANY("Red", "Blue")) AND NOT (filterTags: ANY("Green"))`

If `attributeFilteringSyntax` is set to true under the `params` field, then attribute-based expressions are expected instead of the above described tag-based syntax. Examples:

  * (language: ANY("en", "es")) AND NOT (categories: ANY("Movie"))
  * (available: true) AND (language: ANY("en", "es")) OR (categories: ANY("Movie"))

If your filter blocks all results, the API returns generic (unfiltered) popular Documents. If you only want results strictly matching the filters, set `strictFiltering` to `true` in `[RecommendRequest.params](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/recommend#body.request_body.FIELDS.params)` to receive empty results instead.Note that the API never returns `[Document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents#Document)`s with `storageStatus` as `EXPIRED` or `DELETED` regardless of filter choices.  
`validateOnly` |  `boolean` Use validate only mode for this recommendation query. If set to `true`, a fake model is used that returns arbitrary Document IDs. Note that the validate only mode should only be used for testing the API, or if the model is not ready.  
`params` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Additional domain specific parameters for the recommendations.Allowed values:

  * `returnDocument`: Boolean. If set to `true`, the associated Document object is returned in `[RecommendResponse.RecommendationResult.document](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/RecommendResponse#RecommendationResult.FIELDS.document)`.
  * `returnScore`: Boolean. If set to true, the recommendation score corresponding to each returned Document is set in `[RecommendResponse.RecommendationResult.metadata](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/RecommendResponse#RecommendationResult.FIELDS.metadata)`. The given score indicates the probability of a Document conversion given the user's context and history.
  * `strictFiltering`: Boolean. True by default. If set to `false`, the service returns generic (unfiltered) popular Documents instead of empty if your filter blocks all recommendation results.
  * `diversityLevel`: String. Default empty. If set to be non-empty, then it needs to be one of: 
    * `no-diversity`
    * `low-diversity`
    * `medium-diversity`
    * `high-diversity`
    * `auto-diversity` This gives request-level control and adjusts recommendation results based on Document category.
  * `attributeFilteringSyntax`: Boolean. False by default. If set to true, the `filter` field is interpreted according to the new, attribute-based syntax.

  
`userLabels` |  `map (key: string, value: string)` The user labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique. However, you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.

See [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details.  
  
### Response body

If successful, the response body contains an instance of `[RecommendResponse](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/RecommendResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `servingConfig` resource:

  * `discoveryengine.servingConfigs.recommend`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
