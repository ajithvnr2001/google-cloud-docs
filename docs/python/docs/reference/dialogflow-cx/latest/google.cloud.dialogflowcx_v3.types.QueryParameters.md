---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.QueryParameters
title: Class QueryParameters (2.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:51.277589+00:00
---

# Class QueryParameters (2.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.QueryParameters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class QueryParameters (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.0  2.6.0  2.1.0  2.0.0  1.43.0  1.42.0  1.41.1  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.1  1.31.1  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.1  1.19.0  1.18.0  1.17.1  1.16.0  1.15.0  1.14.1  1.13.5  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.2  1.2.0  1.1.1  1.0.0  0.8.2  0.7.1  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 
    
    
    QueryParameters(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Represents the parameters of a conversational query.

## Attributes  
  
---  
**Name** | **Description**  
`time_zone` |  `str`   
The time zone of this conversational query from the `time zone database   
`geo_location` |  `google.type.latlng_pb2.LatLng`   
The geo location of this conversational query.   
`session_entity_types` |  `MutableSequence[[google.cloud.dialogflowcx_v3.types.SessionEntityType](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SessionEntityType)]`   
Additional session entity types to replace or extend developer entity types with. The entity synonyms apply to all languages and persist for the session of this query.   
`payload` |  `google.protobuf.struct_pb2.Struct`   
This field can be used to pass custom data into the webhook associated with the agent. Arbitrary JSON objects are supported. Some integrations that query a Dialogflow agent may provide additional information in the payload. In particular, for the Dialogflow Phone Gateway integration, this field has the form: :: { "telephony": { "caller_id": "+18558363987" } }   
`parameters` |  `google.protobuf.struct_pb2.Struct`   
Additional parameters to be put into [session parameters][SessionInfo.parameters]. To remove a parameter from the session, clients should explicitly set the parameter value to null. You can reference the session parameters in the agent with the following format: $session.params.parameter-id. Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs: \- MapKey type: string \- MapKey value: parameter name \- MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map. \- MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.   
`parameter_scope` |  `str`   
Scope for the parameters. If not specified, parameters will be treated as session parameters. Parameters with custom scope will not be put into [session parameters][google.cloud.dialogflow.cx.v3.SessionInfo.parameters]. You can reference the parameters with custom scope in the agent with the following format: $parameter-scope.params.parameter-id.   
`current_page` |  `str`   
The unique identifier of the page to override the `current page][QueryResult.current_page]` in the session. Format: `projects/`. If `current_page` is specified, the previous state of the session will be ignored by Dialogflow, including the `previous page][QueryResult.current_page]` and the [previous session parameters][QueryResult.parameters]. In most cases, current_page and parameters should be configured together to direct a session to a specific state.   
`disable_webhook` |  `bool`   
Whether to disable webhook calls for this request.   
`analyze_query_text_sentiment` |  `bool`   
Configures whether sentiment analysis should be performed. If not provided, sentiment analysis is not performed.   
`webhook_headers` |  `MutableMapping[str, str]`   
This field can be used to pass HTTP headers for a webhook call. These headers will be sent to webhook along with the headers that have been configured through Dialogflow web console. The headers defined within this field will overwrite the headers configured through Dialogflow console if there is a conflict. Header names are case-insensitive. Google's specified headers are not allowed. Including: "Host", "Content-Length", "Connection", "From", "User-Agent", "Accept-Encoding", "If-Modified-Since", "If-None-Match", "X-Forwarded-For", etc.   
`flow_versions` |  `MutableSequence[str]`   
A list of flow versions to override for the request. Format: `projects/`. If version 1 of flow X is included in this list, the traffic of flow X will go through version 1 regardless of the version configuration in the environment. Each flow can have at most one version specified in this list.   
`current_playbook` |  `str`   
Optional. The unique identifier of the playbook to start or continue the session with. If `current_playbook` is specified, the previous state of the session will be ignored by Dialogflow. Format: `projects/`.   
`llm_model_settings` |  `[google.cloud.dialogflowcx_v3.types.LlmModelSettings](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.LlmModelSettings)`   
Optional. Use the specified LLM model settings for processing the request.   
`channel` |  `str`   
The channel which this query is for. If specified, only the ResponseMessage associated with the channel will be returned. If no ResponseMessage is associated with the channel, it falls back to the ResponseMessage with unspecified channel. If unspecified, the ResponseMessage with unspecified channel will be returned.   
`session_ttl` |  `google.protobuf.duration_pb2.Duration`   
Optional. Configure lifetime of the Dialogflow session. By default, a Dialogflow session remains active and its data is stored for 30 minutes after the last request is sent for the session. This value should be no longer than 1 day.   
`end_user_metadata` |  `google.protobuf.struct_pb2.Struct`   
Optional. Information about the end-user to improve the relevance and accuracy of generative answers. This will be interpreted and used by a language model, so, for good results, the data should be self-descriptive, and in a simple structure. Example: .. code:: json { "subscription plan": "Business Premium Plus", "devices owned": [ {"model": "Google Pixel 7"}, {"model": "Google Pixel Tablet"} ] }   
`search_config` |  `[google.cloud.dialogflowcx_v3.types.SearchConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.SearchConfig)`   
Optional. Search configuration for UCS search queries.   
`populate_data_store_connection_signals` |  `bool`   
Optional. If set to true and data stores are involved in serving the request then DetectIntentResponse.query_result.data_store_connection_signals will be filled with data that can help evaluations.   
  
## Classes 

### WebhookHeadersEntry
    
    
    WebhookHeadersEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
