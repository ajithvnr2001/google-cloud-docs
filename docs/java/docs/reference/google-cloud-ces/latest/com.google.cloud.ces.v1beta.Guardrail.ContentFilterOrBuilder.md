---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail.ContentFilterOrBuilder
title: Interface Guardrail.ContentFilterOrBuilder (0.15.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:47.197725+00:00
---

# Interface Guardrail.ContentFilterOrBuilder (0.15.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail.ContentFilterOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Guardrail.ContentFilterOrBuilder (0.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.0 (latest)  0.11.0  0.10.0  0.9.0  0.7.0  0.4.0  0.3.0  0.1.0 
    
    
    public static interface Guardrail.ContentFilterOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBannedContents(int index)
    
    
    public abstract String getBannedContents(int index)

Optional. List of banned phrases. Applies to both user inputs and agent responses.

`repeated string banned_contents = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The bannedContents at the given index.  
  
### getBannedContentsBytes(int index)
    
    
    public abstract ByteString getBannedContentsBytes(int index)

Optional. List of banned phrases. Applies to both user inputs and agent responses.

`repeated string banned_contents = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the bannedContents at the given index.  
  
### getBannedContentsCount()
    
    
    public abstract int getBannedContentsCount()

Optional. List of banned phrases. Applies to both user inputs and agent responses.

`repeated string banned_contents = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of bannedContents.  
  
### getBannedContentsInAgentResponse(int index)
    
    
    public abstract String getBannedContentsInAgentResponse(int index)

Optional. List of banned phrases. Applies only to agent responses.

` repeated string banned_contents_in_agent_response = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The bannedContentsInAgentResponse at the given index.  
  
### getBannedContentsInAgentResponseBytes(int index)
    
    
    public abstract ByteString getBannedContentsInAgentResponseBytes(int index)

Optional. List of banned phrases. Applies only to agent responses.

` repeated string banned_contents_in_agent_response = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the bannedContentsInAgentResponse at the given index.  
  
### getBannedContentsInAgentResponseCount()
    
    
    public abstract int getBannedContentsInAgentResponseCount()

Optional. List of banned phrases. Applies only to agent responses.

` repeated string banned_contents_in_agent_response = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of bannedContentsInAgentResponse.  
  
### getBannedContentsInAgentResponseList()
    
    
    public abstract List<String> getBannedContentsInAgentResponseList()

Optional. List of banned phrases. Applies only to agent responses.

` repeated string banned_contents_in_agent_response = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the bannedContentsInAgentResponse.  
  
### getBannedContentsInUserInput(int index)
    
    
    public abstract String getBannedContentsInUserInput(int index)

Optional. List of banned phrases. Applies only to user inputs.

` repeated string banned_contents_in_user_input = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The bannedContentsInUserInput at the given index.  
  
### getBannedContentsInUserInputBytes(int index)
    
    
    public abstract ByteString getBannedContentsInUserInputBytes(int index)

Optional. List of banned phrases. Applies only to user inputs.

` repeated string banned_contents_in_user_input = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the bannedContentsInUserInput at the given index.  
  
### getBannedContentsInUserInputCount()
    
    
    public abstract int getBannedContentsInUserInputCount()

Optional. List of banned phrases. Applies only to user inputs.

` repeated string banned_contents_in_user_input = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of bannedContentsInUserInput.  
  
### getBannedContentsInUserInputList()
    
    
    public abstract List<String> getBannedContentsInUserInputList()

Optional. List of banned phrases. Applies only to user inputs.

` repeated string banned_contents_in_user_input = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the bannedContentsInUserInput.  
  
### getBannedContentsList()
    
    
    public abstract List<String> getBannedContentsList()

Optional. List of banned phrases. Applies to both user inputs and agent responses.

`repeated string banned_contents = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the bannedContents.  
  
### getDisregardDiacritics()
    
    
    public abstract boolean getDisregardDiacritics()

Optional. If true, diacritics are ignored during matching.

`bool disregard_diacritics = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disregardDiacritics.  
  
### getMatchType()
    
    
    public abstract Guardrail.ContentFilter.MatchType getMatchType()

Required. Match type for the content filter.

` .google.cloud.ces.v1beta.Guardrail.ContentFilter.MatchType match_type = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Guardrail.ContentFilter.MatchType](https://docs.cloud.google.com/java/docs/reference/google-cloud-ces/latest/com.google.cloud.ces.v1beta.Guardrail.ContentFilter.MatchType)` | The matchType.  
  
### getMatchTypeValue()
    
    
    public abstract int getMatchTypeValue()

Required. Match type for the content filter.

` .google.cloud.ces.v1beta.Guardrail.ContentFilter.MatchType match_type = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for matchType.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
