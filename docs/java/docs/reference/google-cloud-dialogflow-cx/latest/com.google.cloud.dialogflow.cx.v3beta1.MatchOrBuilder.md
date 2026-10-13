---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.MatchOrBuilder
title: Interface MatchOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:53.157591+00:00
---

# Interface MatchOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.MatchOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MatchOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public interface MatchOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConfidence()
    
    
    public abstract float getConfidence()

The confidence of this match. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). This value is for informational purpose only and is only used to help match the best intent within the classification threshold. This value may change for the same end-user expression at any time due to a model retraining or change in implementation.

`float confidence = 5;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The confidence.  
  
### getEvent()
    
    
    public abstract String getEvent()

The event that matched the query. Filled for `EVENT`, `NO_MATCH` and `NO_INPUT` match types.

`string event = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The event.  
  
### getEventBytes()
    
    
    public abstract ByteString getEventBytes()

The event that matched the query. Filled for `EVENT`, `NO_MATCH` and `NO_INPUT` match types.

`string event = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for event.  
  
### getIntent()
    
    
    public abstract Intent getIntent()

The Intent that matched the query. Some, not all fields are filled in this message, including but not limited to: `name` and `display_name`. Only filled for `INTENT` match type.

`.google.cloud.dialogflow.cx.v3beta1.Intent intent = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.Intent)` | The intent.  
  
### getIntentOrBuilder()
    
    
    public abstract IntentOrBuilder getIntentOrBuilder()

The Intent that matched the query. Some, not all fields are filled in this message, including but not limited to: `name` and `display_name`. Only filled for `INTENT` match type.

`.google.cloud.dialogflow.cx.v3beta1.Intent intent = 1;`

**Returns**  
---  
**Type** | **Description**  
`[IntentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.IntentOrBuilder)` |   
  
### getMatchType()
    
    
    public abstract Match.MatchType getMatchType()

Type of this Match.

`.google.cloud.dialogflow.cx.v3beta1.Match.MatchType match_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Match.MatchType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.Match.MatchType)` | The matchType.  
  
### getMatchTypeValue()
    
    
    public abstract int getMatchTypeValue()

Type of this Match.

`.google.cloud.dialogflow.cx.v3beta1.Match.MatchType match_type = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for matchType.  
  
### getParameters()
    
    
    public abstract Struct getParameters()

The collection of parameters extracted from the query.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

  * MapKey type: string
  * MapKey value: parameter name
  * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
  * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



`.google.protobuf.Struct parameters = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The parameters.  
  
### getParametersOrBuilder()
    
    
    public abstract StructOrBuilder getParametersOrBuilder()

The collection of parameters extracted from the query.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

  * MapKey type: string
  * MapKey value: parameter name
  * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
  * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



`.google.protobuf.Struct parameters = 2;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getResolvedInput()
    
    
    public abstract String getResolvedInput()

Final text input which was matched during MatchIntent. This value can be different from original input sent in request because of spelling correction or other processing.

`string resolved_input = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The resolvedInput.  
  
### getResolvedInputBytes()
    
    
    public abstract ByteString getResolvedInputBytes()

Final text input which was matched during MatchIntent. This value can be different from original input sent in request because of spelling correction or other processing.

`string resolved_input = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for resolvedInput.  
  
### hasIntent()
    
    
    public abstract boolean hasIntent()

The Intent that matched the query. Some, not all fields are filled in this message, including but not limited to: `name` and `display_name`. Only filled for `INTENT` match type.

`.google.cloud.dialogflow.cx.v3beta1.Intent intent = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the intent field is set.  
  
### hasParameters()
    
    
    public abstract boolean hasParameters()

The collection of parameters extracted from the query.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

  * MapKey type: string
  * MapKey value: parameter name
  * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
  * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



`.google.protobuf.Struct parameters = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the parameters field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
