---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Tool.ParallelAiSearchOrBuilder
title: Interface Tool.ParallelAiSearchOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:36.289504+00:00
---

# Interface Tool.ParallelAiSearchOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Tool.ParallelAiSearchOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Tool.ParallelAiSearchOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public static interface Tool.ParallelAiSearchOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getApiKey()
    
    
    public abstract String getApiKey()

Optional. The API key for ParallelAiSearch. If an API key is not provided, the system will attempt to verify access by checking for an active Parallel.ai subscription through the Google Cloud Marketplace. See <https://docs.parallel.ai/search/search-quickstart> for more details.

`string api_key = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The apiKey.  
  
### getApiKeyBytes()
    
    
    public abstract ByteString getApiKeyBytes()

Optional. The API key for ParallelAiSearch. If an API key is not provided, the system will attempt to verify access by checking for an active Parallel.ai subscription through the Google Cloud Marketplace. See <https://docs.parallel.ai/search/search-quickstart> for more details.

`string api_key = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for apiKey.  
  
### getCustomConfigs()
    
    
    public abstract Struct getCustomConfigs()

Optional. Custom configs for ParallelAiSearch. This field can be used to pass any parameter from the Parallel.ai Search API. See the Parallel.ai documentation for the full list of available parameters and their usage: <https://docs.parallel.ai/api-reference/search-beta/search> Currently only `source_policy`, `excerpts`, `max_results`, `mode`, `fetch_policy` can be set via this field. For example: { "source_policy": { "include_domains": ["google.com", "wikipedia.org"], "exclude_domains": ["example.com"] }, "fetch_policy": { "max_age_seconds": 3600 } }

`.google.protobuf.Struct custom_configs = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The customConfigs.  
  
### getCustomConfigsOrBuilder()
    
    
    public abstract StructOrBuilder getCustomConfigsOrBuilder()

Optional. Custom configs for ParallelAiSearch. This field can be used to pass any parameter from the Parallel.ai Search API. See the Parallel.ai documentation for the full list of available parameters and their usage: <https://docs.parallel.ai/api-reference/search-beta/search> Currently only `source_policy`, `excerpts`, `max_results`, `mode`, `fetch_policy` can be set via this field. For example: { "source_policy": { "include_domains": ["google.com", "wikipedia.org"], "exclude_domains": ["example.com"] }, "fetch_policy": { "max_age_seconds": 3600 } }

`.google.protobuf.Struct custom_configs = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getEnableZeroDataRetention()
    
    
    public abstract boolean getEnableZeroDataRetention()

Optional. Instructs Vertex Grounding to use Parallel's Zero Data Retention Marketplace product. If this value is "false" or omitted, the Parallel Web Search for Grounding standard subscription will be used. If this value is "true", the Parallel Web Search for Grounding - ZDR subscription will be used.

`bool enable_zero_data_retention = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableZeroDataRetention.  
  
### hasCustomConfigs()
    
    
    public abstract boolean hasCustomConfigs()

Optional. Custom configs for ParallelAiSearch. This field can be used to pass any parameter from the Parallel.ai Search API. See the Parallel.ai documentation for the full list of available parameters and their usage: <https://docs.parallel.ai/api-reference/search-beta/search> Currently only `source_policy`, `excerpts`, `max_results`, `mode`, `fetch_policy` can be set via this field. For example: { "source_policy": { "include_domains": ["google.com", "wikipedia.org"], "exclude_domains": ["example.com"] }, "fetch_policy": { "max_age_seconds": 3600 } }

`.google.protobuf.Struct custom_configs = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customConfigs field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
