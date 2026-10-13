---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorOrBuilder
title: Interface RuleExecutionErrorOrBuilder (0.37.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:02.305206+00:00
---

# Interface RuleExecutionErrorOrBuilder (0.37.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionErrorOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RuleExecutionErrorOrBuilder (0.37.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.37.0 (latest)  0.33.0  0.32.0  0.31.0  0.29.0  0.26.0  0.25.0  0.23.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.2.0  0.1.0 
    
    
    public interface RuleExecutionErrorOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCuratedRule()
    
    
    public abstract String getCuratedRule()

Output only. The resource name of the curated rule that generated the rule execution error.

` string curated_rule = 5 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The curatedRule.  
  
### getCuratedRuleBytes()
    
    
    public abstract ByteString getCuratedRuleBytes()

Output only. The resource name of the curated rule that generated the rule execution error.

` string curated_rule = 5 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for curatedRule.  
  
### getError()
    
    
    public abstract Status getError()

Output only. The error status corresponding with the rule execution error.

`.google.rpc.Status error = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The error.  
  
### getErrorOrBuilder()
    
    
    public abstract StatusOrBuilder getErrorOrBuilder()

Output only. The error status corresponding with the rule execution error.

`.google.rpc.Status error = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getName()
    
    
    public abstract String getName()

Output only. The resource name of the rule execution error. Format: projects/{project}/locations/{location}/instances/{instance}/ruleExecutionErrors/{rule_execution_error}

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. The resource name of the rule execution error. Format: projects/{project}/locations/{location}/instances/{instance}/ruleExecutionErrors/{rule_execution_error}

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRule()
    
    
    public abstract String getRule()

Output only. The resource name of the rule that generated the rule execution error.

` string rule = 4 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The rule.  
  
### getRuleBytes()
    
    
    public abstract ByteString getRuleBytes()

Output only. The resource name of the rule that generated the rule execution error.

` string rule = 4 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for rule.  
  
### getSourceCase()
    
    
    public abstract RuleExecutionError.SourceCase getSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[RuleExecutionError.SourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-chronicle/latest/com.google.cloud.chronicle.v1.RuleExecutionError.SourceCase)` |   
  
### getTimeRange()
    
    
    public abstract Interval getTimeRange()

Output only. The event time range that the rule execution error corresponds with.

`.google.type.Interval time_range = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Interval` | The timeRange.  
  
### getTimeRangeOrBuilder()
    
    
    public abstract IntervalOrBuilder getTimeRangeOrBuilder()

Output only. The event time range that the rule execution error corresponds with.

`.google.type.Interval time_range = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.IntervalOrBuilder` |   
  
### hasCuratedRule()
    
    
    public abstract boolean hasCuratedRule()

Output only. The resource name of the curated rule that generated the rule execution error.

` string curated_rule = 5 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the curatedRule field is set.  
  
### hasError()
    
    
    public abstract boolean hasError()

Output only. The error status corresponding with the rule execution error.

`.google.rpc.Status error = 2 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the error field is set.  
  
### hasRule()
    
    
    public abstract boolean hasRule()

Output only. The resource name of the rule that generated the rule execution error.

` string rule = 4 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rule field is set.  
  
### hasTimeRange()
    
    
    public abstract boolean hasTimeRange()

Output only. The event time range that the rule execution error corresponds with.

`.google.type.Interval time_range = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timeRange field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
