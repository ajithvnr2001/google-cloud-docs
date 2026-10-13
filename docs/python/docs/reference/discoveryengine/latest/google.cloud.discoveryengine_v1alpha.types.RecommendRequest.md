---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecommendRequest
title: Class RecommendRequest (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:34:48.438795+00:00
---

# Class RecommendRequest (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.RecommendRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RecommendRequest (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    RecommendRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for Recommend method.

## Attributes  
  
---  
**Name** | **Description**  
`serving_config` |  `str`   
Required. Full resource name of a ServingConfig: `projects/*/locations/global/collections/*/engines/*/servingConfigs/*`, or `projects/*/locations/global/collections/*/dataStores/*/servingConfigs/*` One default serving config is created along with your recommendation engine creation. The engine ID is used as the ID of the default serving config. For example, for Engine `projects/*/locations/global/collections/*/engines/my-engine`, you can use `projects/*/locations/global/collections/*/engines/my-engine/servingConfigs/my-engine` for your RecommendationService.Recommend requests.   
`user_event` |  `[google.cloud.discoveryengine_v1alpha.types.UserEvent](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1alpha.types.UserEvent)`   
Required. Context about the user, what they are looking at and what action they took to trigger the Recommend request. Note that this user event detail won't be ingested to userEvent logs. Thus, a separate userEvent write request is required for event logging. Don't set UserEvent.user_pseudo_id or UserEvent.user_info.user_id to the same fixed ID for different users. If you are trying to receive non-personalized recommendations (not recommended; this can negatively impact model performance), instead set UserEvent.user_pseudo_id to a random unique ID and leave UserEvent.user_info.user_id unset.   
`page_size` |  `int`   
Maximum number of results to return. Set this property to the number of recommendation results needed. If zero, the service chooses a reasonable default. The maximum allowed value is 100\. Values above 100 are set to 100.   
`filter` |  `str`   
Filter for restricting recommendation results with a length limit of 5,000 characters. Currently, only filter expressions on the `filter_tags` attribute is supported. Examples: \- `(filter_tags: ANY("Red", "Blue") OR filter_tags: ANY("Hot", "Cold"))` \- `(filter_tags: ANY("Red", "Blue")) AND NOT (filter_tags: ANY("Green"))` If `attributeFilteringSyntax` is set to true under the `params` field, then attribute-based expressions are expected instead of the above described tag-based syntax. Examples: \- (launguage: ANY("en", "es")) AND NOT (categories: ANY("Movie")) \- (available: true) AND (launguage: ANY("en", "es")) OR (categories: ANY("Movie")) If your filter blocks all results, the API returns generic (unfiltered) popular Documents. If you only want results strictly matching the filters, set `strictFiltering` to `true` in RecommendRequest.params to receive empty results instead. Note that the API never returns Documents with `storageStatus` as `EXPIRED` or `DELETED` regardless of filter choices.   
`validate_only` |  `bool`   
Use validate only mode for this recommendation query. If set to `true`, a fake model is used that returns arbitrary Document IDs. Note that the validate only mode should only be used for testing the API, or if the model is not ready.   
`params` |  `MutableMapping[str, google.protobuf.struct_pb2.Value]`   
Additional domain specific parameters for the recommendations. Allowed values: \- `returnDocument`: Boolean. If set to `true`, the associated Document object is returned in RecommendResponse.RecommendationResult.document. \- `returnScore`: Boolean. If set to true, the recommendation score corresponding to each returned Document is set in RecommendResponse.RecommendationResult.metadata. The given score indicates the probability of a Document conversion given the user's context and history. \- `strictFiltering`: Boolean. True by default. If set to `false`, the service returns generic (unfiltered) popular Documents instead of empty if your filter blocks all recommendation results. \- `diversityLevel`: String. Default empty. If set to be non-empty, then it needs to be one of: \- `no-diversity` \- `low-diversity` \- `medium-diversity` \- `high-diversity` \- `auto-diversity` This gives request-level control and adjusts recommendation results based on Document category. \- `attributeFilteringSyntax`: Boolean. False by default. If set to true, the `filter` field is interpreted according to the new, attribute-based syntax.   
`user_labels` |  `MutableMapping[str, str]`   
The user labels applied to a resource must meet the following requirements: \- Each resource can have multiple labels, up to a maximum of 64\. \- Each label must be a key-value pair. \- Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters. \- Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed. \- The key portion of a label must be unique. However, you can use the same key with multiple resources. \- Keys must start with a lowercase letter or international character. See `Requirements for labels   
  
## Classes 

### ParamsEntry
    
    
    ParamsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### UserLabelsEntry
    
    
    UserLabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
