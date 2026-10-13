---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UserEvent
title: Class UserEvent (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:27.148271+00:00
---

# Class UserEvent (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UserEvent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class UserEvent (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    UserEvent(mapping=None, *, ignore_unknown_fields=False, **kwargs)

UserEvent captures all metadata information Discovery Engine API needs to know about how end users interact with your website.

## Attributes  
  
---  
**Name** | **Description**  
`event_type` |  `str`   
Required. User event type. Allowed values are: Generic values: \- `search`: Search for Documents. \- `view-item`: Detailed page view of a Document. \- `view-item-list`: View of a panel or ordered list of Documents. \- `view-home-page`: View of the home page. \- `view-category-page`: View of a category page, e.g. Home > Men > Jeans \- `add-feedback`: Add a user feedback. Retail-related values: \- `add-to-cart`: Add an item(s) to cart, e.g. in Retail online shopping \- `purchase`: Purchase an item(s) Media-related values: \- `media-play`: Start/resume watching a video, playing a song, etc. \- `media-complete`: Finished or stopped midway through a video, song, etc. Custom conversion value: \- `conversion`: Customer defined conversion event.   
`conversion_type` |  `str`   
Optional. Conversion type. Required if UserEvent.event_type is `conversion`. This is a customer-defined conversion name in lowercase letters or numbers separated by "-", such as "watch", "good-visit" etc. Do not set the field if UserEvent.event_type is not `conversion`. This mixes the custom conversion event with predefined events like `search`, `view-item` etc.   
`user_pseudo_id` |  `str`   
Required. A unique identifier for tracking visitors. For example, this could be implemented with an HTTP cookie, which should be able to uniquely identify a visitor on a single device. This unique identifier should not change if the visitor log in/out of the website. Do not set the field to the same fixed ID for different users. This mixes the event history of those users together, which results in degraded model quality. The field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned. The field should not contain PII or user-data. We recommend to use Google Analytics `Client ID   
`engine` |  `str`   
The Engine resource name, in the form of `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. Optional. Only required for Engine produced user events. For example, user events from blended search.   
`data_store` |  `str`   
The DataStore resource full name, of the form `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}`. Optional. Only required for user events whose data store can't by determined by UserEvent.engine or UserEvent.documents. If data store is set in the parent of write/import/collect user event requests, this field can be omitted.   
`event_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Only required for UserEventService.ImportUserEvents method. Timestamp of when the user event happened.   
`user_info` |  `[google.cloud.discoveryengine_v1.types.UserInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.UserInfo)`   
Information about the end user.   
`direct_user_request` |  `bool`   
Should set to true if the request is made directly from the end user, in which case the UserEvent.user_info.user_agent can be populated from the HTTP request. This flag should be set only if the API request is made directly from the end user such as a mobile app (and not if a gateway or a server is processing and pushing the user events). This should not be set when using the JavaScript tag in UserEventService.CollectUserEvent.   
`session_id` |  `str`   
A unique identifier for tracking a visitor session with a length limit of 128 bytes. A session is an aggregation of an end user behavior in a time span. A general guideline to populate the session_id: 1\. If user has no activity for 30 min, a new session_id should be assigned. 2\. The session_id should be unique across users, suggest use uuid or add UserEvent.user_pseudo_id as prefix.   
`page_info` |  `[google.cloud.discoveryengine_v1.types.PageInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PageInfo)`   
Page metadata such as categories and other critical information for certain event types such as `view-category-page`.   
`attribution_token` |  `str`   
Token to attribute an API response to user action(s) to trigger the event. Highly recommended for user events that are the result of RecommendationService.Recommend. This field enables accurate attribution of recommendation model performance. The value must be one of: \- RecommendResponse.attribution_token for events that are the result of RecommendationService.Recommend. \- SearchResponse.attribution_token for events that are the result of SearchService.Search. This token enables us to accurately attribute page view or conversion completion back to the event and the particular predict response containing this clicked/purchased product. If user clicks on product K in the recommendation results, pass RecommendResponse.attribution_token as a URL parameter to product K's page. When recording events on product K's page, log the RecommendResponse.attribution_token to this field.   
`filter` |  `str`   
The filter syntax consists of an expression language for constructing a predicate from one or more fields of the documents being filtered. One example is for `search` events, the associated SearchRequest may contain a filter expression in SearchRequest.filter conforming to https://google.aip.dev/160#filtering. Similarly, for `view-item-list` events that are generated from a RecommendRequest, this field may be populated directly from RecommendRequest.filter conforming to https://google.aip.dev/160#filtering. The value must be a UTF-8 encoded string with a length limit of 1,000 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.   
`documents` |  `MutableSequence[[google.cloud.discoveryengine_v1.types.DocumentInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.DocumentInfo)]`   
List of Documents associated with this user event. This field is optional except for the following event types: \- `view-item` \- `add-to-cart` \- `purchase` \- `media-play` \- `media-complete` In a `search` event, this field represents the documents returned to the end user on the current page (the end user may have not finished browsing the whole page yet). When a new page is returned to the end user, after pagination/filtering/ordering even for the same query, a new `search` event with different UserEvent.documents is desired.   
`panel` |  `[google.cloud.discoveryengine_v1.types.PanelInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PanelInfo)`   
Panel metadata associated with this user event.   
`search_info` |  `[google.cloud.discoveryengine_v1.types.SearchInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SearchInfo)`   
SearchService.Search details related to the event. This field should be set for `search` event.   
`completion_info` |  `[google.cloud.discoveryengine_v1.types.CompletionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CompletionInfo)`   
CompletionService.CompleteQuery details related to the event. This field should be set for `search` event when autocomplete function is enabled and the user clicks a suggestion for search.   
`transaction_info` |  `[google.cloud.discoveryengine_v1.types.TransactionInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.TransactionInfo)`   
The transaction metadata (if any) associated with this user event.   
`tag_ids` |  `MutableSequence[str]`   
A list of identifiers for the independent experiment groups this user event belongs to. This is used to distinguish between user events associated with different experiment setups.   
`promotion_ids` |  `MutableSequence[str]`   
The promotion IDs if this is an event associated with promotions. Currently, this field is restricted to at most one ID.   
`attributes` |  `MutableMapping[str, [google.cloud.discoveryengine_v1.types.CustomAttribute](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.CustomAttribute)]`   
Extra user event features to include in the recommendation model. These attributes must NOT contain data that needs to be parsed or processed further, e.g. JSON or other encodings. If you provide custom attributes for ingested user events, also include them in the user events that you associate with prediction requests. Custom attribute formatting must be consistent between imported events and events provided with prediction requests. This lets the Discovery Engine API use those custom attributes when training models and serving predictions, which helps improve recommendation quality. This field needs to pass all below criteria, otherwise an `INVALID_ARGUMENT` error is returned: \- The key must be a UTF-8 encoded string with a length limit of 5,000 characters. \- For text attributes, at most 400 values are allowed. Empty values are not allowed. Each value must be a UTF-8 encoded string with a length limit of 256 characters. \- For number attributes, at most 400 values are allowed. For product recommendations, an example of extra user information is `traffic_channel`, which is how a user arrives at the site. Users can arrive at the site by coming to the site directly, coming through Google search, or in other ways.   
`media_info` |  `[google.cloud.discoveryengine_v1.types.MediaInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.MediaInfo)`   
Media-specific info.   
`panels` |  `MutableSequence[[google.cloud.discoveryengine_v1.types.PanelInfo](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.PanelInfo)]`   
Optional. List of panels associated with this event. Used for page-level impression data.   
  
## Classes 

### AttributesEntry
    
    
    AttributesEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
