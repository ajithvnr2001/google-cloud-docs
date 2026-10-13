---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ConverseConversationRequestOrBuilder
title: Interface ConverseConversationRequestOrBuilder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:55:06.557353+00:00
---

# Interface ConverseConversationRequestOrBuilder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ConverseConversationRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ConverseConversationRequestOrBuilder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ConverseConversationRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsUserLabels(String key)
    
    
    public abstract boolean containsUserLabels(String key)

The user labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique. However, you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details.




`map<string, string> user_labels = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBoostSpec()
    
    
    public abstract SearchRequest.BoostSpec getBoostSpec()

Boost specification to boost certain documents in search results which may affect the converse response. For more information on boosting, see [Boosting](https://cloud.google.com/retail/docs/boosting#boost)

`.google.cloud.discoveryengine.v1beta.SearchRequest.BoostSpec boost_spec = 10;`

**Returns**  
---  
**Type** | **Description**  
`[SearchRequest.BoostSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.SearchRequest.BoostSpec)` | The boostSpec.  
  
### getBoostSpecOrBuilder()
    
    
    public abstract SearchRequest.BoostSpecOrBuilder getBoostSpecOrBuilder()

Boost specification to boost certain documents in search results which may affect the converse response. For more information on boosting, see [Boosting](https://cloud.google.com/retail/docs/boosting#boost)

`.google.cloud.discoveryengine.v1beta.SearchRequest.BoostSpec boost_spec = 10;`

**Returns**  
---  
**Type** | **Description**  
`[SearchRequest.BoostSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.SearchRequest.BoostSpecOrBuilder)` |   
  
### getConversation()
    
    
    public abstract Conversation getConversation()

The conversation to be used by auto session only. The name field will be ignored as we automatically assign new name for the conversation in auto session.

`.google.cloud.discoveryengine.v1beta.Conversation conversation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.Conversation)` | The conversation.  
  
### getConversationOrBuilder()
    
    
    public abstract ConversationOrBuilder getConversationOrBuilder()

The conversation to be used by auto session only. The name field will be ignored as we automatically assign new name for the conversation in auto session.

`.google.cloud.discoveryengine.v1beta.Conversation conversation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ConversationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ConversationOrBuilder)` |   
  
### getFilter()
    
    
    public abstract String getFilter()

The filter syntax consists of an expression language for constructing a predicate from one or more fields of the documents being filtered. Filter expression is case-sensitive. This will be used to filter search results which may affect the summary response.

If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.

Filtering in Vertex AI Search is done by mapping the LHS filter key to a key property defined in the Vertex AI Search backend -- this mapping is defined by the customer in their schema. For example a media customer might have a field 'name' in their schema. In this case the filter would look like this: filter --> name:'ANY("king kong")'

For more information about filtering including syntax and filter operators, see [Filter](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)

`string filter = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The filter.  
  
### getFilterBytes()
    
    
    public abstract ByteString getFilterBytes()

The filter syntax consists of an expression language for constructing a predicate from one or more fields of the documents being filtered. Filter expression is case-sensitive. This will be used to filter search results which may affect the summary response.

If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.

Filtering in Vertex AI Search is done by mapping the LHS filter key to a key property defined in the Vertex AI Search backend -- this mapping is defined by the customer in their schema. For example a media customer might have a field 'name' in their schema. In this case the filter would look like this: filter --> name:'ANY("king kong")'

For more information about filtering including syntax and filter operators, see [Filter](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)

`string filter = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for filter.  
  
### getName()
    
    
    public abstract String getName()

Required. The resource name of the Conversation to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`. Use `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/-` to activate auto session mode, which automatically creates a new conversation inside a ConverseConversation session.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The resource name of the Conversation to get. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/{conversation_id}`. Use `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/conversations/-` to activate auto session mode, which automatically creates a new conversation inside a ConverseConversation session.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getQuery()
    
    
    public abstract TextInput getQuery()

Required. Current user input.

` .google.cloud.discoveryengine.v1beta.TextInput query = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[TextInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.TextInput)` | The query.  
  
### getQueryOrBuilder()
    
    
    public abstract TextInputOrBuilder getQueryOrBuilder()

Required. Current user input.

` .google.cloud.discoveryengine.v1beta.TextInput query = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[TextInputOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.TextInputOrBuilder)` |   
  
### getSafeSearch()
    
    
    public abstract boolean getSafeSearch()

Whether to turn on safe search.

`bool safe_search = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The safeSearch.  
  
### getServingConfig()
    
    
    public abstract String getServingConfig()

The resource name of the Serving Config to use. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/servingConfigs/{serving_config_id}` If this is not set, the default serving config will be used.

`string serving_config = 3 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The servingConfig.  
  
### getServingConfigBytes()
    
    
    public abstract ByteString getServingConfigBytes()

The resource name of the Serving Config to use. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/servingConfigs/{serving_config_id}` If this is not set, the default serving config will be used.

`string serving_config = 3 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for servingConfig.  
  
### getSummarySpec()
    
    
    public abstract SearchRequest.ContentSearchSpec.SummarySpec getSummarySpec()

A specification for configuring the summary returned in the response.

` .google.cloud.discoveryengine.v1beta.SearchRequest.ContentSearchSpec.SummarySpec summary_spec = 8; `

**Returns**  
---  
**Type** | **Description**  
`[SearchRequest.ContentSearchSpec.SummarySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.SearchRequest.ContentSearchSpec.SummarySpec)` | The summarySpec.  
  
### getSummarySpecOrBuilder()
    
    
    public abstract SearchRequest.ContentSearchSpec.SummarySpecOrBuilder getSummarySpecOrBuilder()

A specification for configuring the summary returned in the response.

` .google.cloud.discoveryengine.v1beta.SearchRequest.ContentSearchSpec.SummarySpec summary_spec = 8; `

**Returns**  
---  
**Type** | **Description**  
`[SearchRequest.ContentSearchSpec.SummarySpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.SearchRequest.ContentSearchSpec.SummarySpecOrBuilder)` |   
  
### getUserLabels() (deprecated)
    
    
    public abstract Map<String,String> getUserLabels()

Use [#getUserLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.ConverseConversationRequestOrBuilder#com_google_cloud_discoveryengine_v1beta_ConverseConversationRequestOrBuilder_getUserLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getUserLabelsCount()
    
    
    public abstract int getUserLabelsCount()

The user labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique. However, you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details.




`map<string, string> user_labels = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getUserLabelsMap()
    
    
    public abstract Map<String,String> getUserLabelsMap()

The user labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique. However, you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details.




`map<string, string> user_labels = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getUserLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getUserLabelsOrDefault(String key, String defaultValue)

The user labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique. However, you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details.




`map<string, string> user_labels = 7;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getUserLabelsOrThrow(String key)
    
    
    public abstract String getUserLabelsOrThrow(String key)

The user labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding, and international characters are allowed.
  * The key portion of a label must be unique. However, you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.

See [Google Cloud Document](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements) for more details.




`map<string, string> user_labels = 7;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### hasBoostSpec()
    
    
    public abstract boolean hasBoostSpec()

Boost specification to boost certain documents in search results which may affect the converse response. For more information on boosting, see [Boosting](https://cloud.google.com/retail/docs/boosting#boost)

`.google.cloud.discoveryengine.v1beta.SearchRequest.BoostSpec boost_spec = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the boostSpec field is set.  
  
### hasConversation()
    
    
    public abstract boolean hasConversation()

The conversation to be used by auto session only. The name field will be ignored as we automatically assign new name for the conversation in auto session.

`.google.cloud.discoveryengine.v1beta.Conversation conversation = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the conversation field is set.  
  
### hasQuery()
    
    
    public abstract boolean hasQuery()

Required. Current user input.

` .google.cloud.discoveryengine.v1beta.TextInput query = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the query field is set.  
  
### hasSummarySpec()
    
    
    public abstract boolean hasSummarySpec()

A specification for configuring the summary returned in the response.

` .google.cloud.discoveryengine.v1beta.SearchRequest.ContentSearchSpec.SummarySpec summary_spec = 8; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the summarySpec field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
