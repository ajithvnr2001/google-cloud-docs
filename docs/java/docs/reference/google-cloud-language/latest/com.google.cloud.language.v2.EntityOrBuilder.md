---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityOrBuilder
title: Interface EntityOrBuilder (2.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:46:00.192050+00:00
---

# Interface EntityOrBuilder (2.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EntityOrBuilder (2.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.100.0 (latest)  2.96.0  2.95.0  2.94.0  2.92.0  2.89.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.79.0  2.77.0  2.76.0  2.75.0  2.74.0  2.73.0  2.71.0  2.69.0  2.68.0  2.65.0  2.64.0  2.63.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.1  2.3.4  2.2.0  2.1.10 
    
    
    public interface EntityOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsMetadata(String key)
    
    
    public abstract boolean containsMetadata(String key)

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMentions(int index)
    
    
    public abstract EntityMention getMentions(int index)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntityMention](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention)` |   
  
### getMentionsCount()
    
    
    public abstract int getMentionsCount()

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMentionsList()
    
    
    public abstract List<EntityMention> getMentionsList()

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[EntityMention](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMention)>` |   
  
### getMentionsOrBuilder(int index)
    
    
    public abstract EntityMentionOrBuilder getMentionsOrBuilder(int index)

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[EntityMentionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityMentionOrBuilder)` |   
  
### getMentionsOrBuilderList()
    
    
    public abstract List<? extends EntityMentionOrBuilder> getMentionsOrBuilderList()

The mentions of this entity in the input document. The API currently supports proper noun mentions.

`repeated .google.cloud.language.v2.EntityMention mentions = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.language.v2.EntityMentionOrBuilder>` |   
  
### getMetadata() (deprecated)
    
    
    public abstract Map<String,String> getMetadata()

Use [#getMetadataMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.EntityOrBuilder#com_google_cloud_language_v2_EntityOrBuilder_getMetadataMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMetadataCount()
    
    
    public abstract int getMetadataCount()

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMetadataMap()
    
    
    public abstract Map<String,String> getMetadataMap()

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getMetadataOrDefault(String key, String defaultValue)
    
    
    public abstract String getMetadataOrDefault(String key, String defaultValue)

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMetadataOrThrow(String key)
    
    
    public abstract String getMetadataOrThrow(String key)

Metadata associated with the entity.

For the metadata associated with other entity types, see the Type table below.

`map<string, string> metadata = 3;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getName()
    
    
    public abstract String getName()

The representative name for the entity.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

The representative name for the entity.

`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getSentiment()
    
    
    public abstract Sentiment getSentiment()

For calls to [AnalyzeEntitySentiment][] or if AnnotateTextRequest.Features.extract_entity_sentiment is set to true, this field will contain the aggregate sentiment expressed for this entity in the provided document.

`.google.cloud.language.v2.Sentiment sentiment = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Sentiment](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Sentiment)` | The sentiment.  
  
### getSentimentOrBuilder()
    
    
    public abstract SentimentOrBuilder getSentimentOrBuilder()

For calls to [AnalyzeEntitySentiment][] or if AnnotateTextRequest.Features.extract_entity_sentiment is set to true, this field will contain the aggregate sentiment expressed for this entity in the provided document.

`.google.cloud.language.v2.Sentiment sentiment = 6;`

**Returns**  
---  
**Type** | **Description**  
`[SentimentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.SentimentOrBuilder)` |   
  
### getType()
    
    
    public abstract Entity.Type getType()

The entity type.

`.google.cloud.language.v2.Entity.Type type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Entity.Type](https://docs.cloud.google.com/java/docs/reference/google-cloud-language/latest/com.google.cloud.language.v2.Entity.Type)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

The entity type.

`.google.cloud.language.v2.Entity.Type type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### hasSentiment()
    
    
    public abstract boolean hasSentiment()

For calls to [AnalyzeEntitySentiment][] or if AnnotateTextRequest.Features.extract_entity_sentiment is set to true, this field will contain the aggregate sentiment expressed for this entity in the provided document.

`.google.cloud.language.v2.Sentiment sentiment = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sentiment field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
