---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-admin/latest/com.google.analytics.admin.v1alpha.ConversionEventOrBuilder
title: Interface ConversionEventOrBuilder (0.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:37.529244+00:00
---

# Interface ConversionEventOrBuilder (0.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-admin/latest/com.google.analytics.admin.v1alpha.ConversionEventOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ConversionEventOrBuilder (0.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.109.0 (latest)  0.105.0  0.104.0  0.103.0  0.101.0  0.98.0  0.97.0  0.95.0  0.93.0  0.92.0  0.91.0  0.90.0  0.88.0  0.86.0  0.85.0  0.84.0  0.83.0  0.82.0  0.80.0  0.78.0  0.77.0  0.74.0  0.73.0  0.72.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0 
    
    
    public interface ConversionEventOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCountingMethod()
    
    
    public abstract ConversionEvent.ConversionCountingMethod getCountingMethod()

Optional. The method by which conversions will be counted across multiple events within a session. If this value is not provided, it will be set to `ONCE_PER_EVENT`.

` .google.analytics.admin.v1alpha.ConversionEvent.ConversionCountingMethod counting_method = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConversionEvent.ConversionCountingMethod](https://docs.cloud.google.com/java/docs/reference/google-analytics-admin/latest/com.google.analytics.admin.v1alpha.ConversionEvent.ConversionCountingMethod)` | The countingMethod.  
  
### getCountingMethodValue()
    
    
    public abstract int getCountingMethodValue()

Optional. The method by which conversions will be counted across multiple events within a session. If this value is not provided, it will be set to `ONCE_PER_EVENT`.

` .google.analytics.admin.v1alpha.ConversionEvent.ConversionCountingMethod counting_method = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for countingMethod.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Time when this conversion event was created in the property.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Time when this conversion event was created in the property.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCustom()
    
    
    public abstract boolean getCustom()

Output only. If set to true, this conversion event refers to a custom event. If set to false, this conversion event refers to a default event in GA. Default events typically have special meaning in GA. Default events are usually created for you by the GA system, but in some cases can be created by property admins. Custom events count towards the maximum number of custom conversion events that may be created per property.

`bool custom = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The custom.  
  
### getDefaultConversionValue()
    
    
    public abstract ConversionEvent.DefaultConversionValue getDefaultConversionValue()

Optional. Defines a default value/currency for a conversion event.

` optional .google.analytics.admin.v1alpha.ConversionEvent.DefaultConversionValue default_conversion_value = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConversionEvent.DefaultConversionValue](https://docs.cloud.google.com/java/docs/reference/google-analytics-admin/latest/com.google.analytics.admin.v1alpha.ConversionEvent.DefaultConversionValue)` | The defaultConversionValue.  
  
### getDefaultConversionValueOrBuilder()
    
    
    public abstract ConversionEvent.DefaultConversionValueOrBuilder getDefaultConversionValueOrBuilder()

Optional. Defines a default value/currency for a conversion event.

` optional .google.analytics.admin.v1alpha.ConversionEvent.DefaultConversionValue default_conversion_value = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ConversionEvent.DefaultConversionValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-admin/latest/com.google.analytics.admin.v1alpha.ConversionEvent.DefaultConversionValueOrBuilder)` |   
  
### getDeletable()
    
    
    public abstract boolean getDeletable()

Output only. If set, this event can currently be deleted with DeleteConversionEvent.

`bool deletable = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The deletable.  
  
### getEventName()
    
    
    public abstract String getEventName()

Immutable. The event name for this conversion event. Examples: 'click', 'purchase'

`string event_name = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The eventName.  
  
### getEventNameBytes()
    
    
    public abstract ByteString getEventNameBytes()

Immutable. The event name for this conversion event. Examples: 'click', 'purchase'

`string event_name = 2 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for eventName.  
  
### getName()
    
    
    public abstract String getName()

Identifier. Resource name of this conversion event. Format: properties/{property}/conversionEvents/{conversion_event}

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. Resource name of this conversion event. Format: properties/{property}/conversionEvents/{conversion_event}

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Time when this conversion event was created in the property.

`.google.protobuf.Timestamp create_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasDefaultConversionValue()
    
    
    public abstract boolean hasDefaultConversionValue()

Optional. Defines a default value/currency for a conversion event.

` optional .google.analytics.admin.v1alpha.ConversionEvent.DefaultConversionValue default_conversion_value = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the defaultConversionValue field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
