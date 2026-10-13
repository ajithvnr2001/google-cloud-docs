---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.CreateQuotaPreferenceRequestOrBuilder
title: Interface CreateQuotaPreferenceRequestOrBuilder (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:10:13.360743+00:00
---

# Interface CreateQuotaPreferenceRequestOrBuilder (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.CreateQuotaPreferenceRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreateQuotaPreferenceRequestOrBuilder (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface CreateQuotaPreferenceRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIgnoreSafetyChecks(int index)
    
    
    public abstract QuotaSafetyCheck getIgnoreSafetyChecks(int index)

The list of quota safety checks to be ignored.

`repeated .google.api.cloudquotas.v1.QuotaSafetyCheck ignore_safety_checks = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[QuotaSafetyCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaSafetyCheck)` | The ignoreSafetyChecks at the given index.  
  
### getIgnoreSafetyChecksCount()
    
    
    public abstract int getIgnoreSafetyChecksCount()

The list of quota safety checks to be ignored.

`repeated .google.api.cloudquotas.v1.QuotaSafetyCheck ignore_safety_checks = 4;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of ignoreSafetyChecks.  
  
### getIgnoreSafetyChecksList()
    
    
    public abstract List<QuotaSafetyCheck> getIgnoreSafetyChecksList()

The list of quota safety checks to be ignored.

`repeated .google.api.cloudquotas.v1.QuotaSafetyCheck ignore_safety_checks = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[QuotaSafetyCheck](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaSafetyCheck)>` | A list containing the ignoreSafetyChecks.  
  
### getIgnoreSafetyChecksValue(int index)
    
    
    public abstract int getIgnoreSafetyChecksValue(int index)

The list of quota safety checks to be ignored.

`repeated .google.api.cloudquotas.v1.QuotaSafetyCheck ignore_safety_checks = 4;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of ignoreSafetyChecks at the given index.  
  
### getIgnoreSafetyChecksValueList()
    
    
    public abstract List<Integer> getIgnoreSafetyChecksValueList()

The list of quota safety checks to be ignored.

`repeated .google.api.cloudquotas.v1.QuotaSafetyCheck ignore_safety_checks = 4;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for ignoreSafetyChecks.  
  
### getParent()
    
    
    public abstract String getParent()

Required. Identifier. Value for parent.

Example: `projects/123/locations/global`

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IDENTIFIER, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. Identifier. Value for parent.

Example: `projects/123/locations/global`

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.field_behavior) = IDENTIFIER, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getQuotaPreference()
    
    
    public abstract QuotaPreference getQuotaPreference()

Required. The resource being created

` .google.api.cloudquotas.v1.QuotaPreference quota_preference = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreference](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaPreference)` | The quotaPreference.  
  
### getQuotaPreferenceId()
    
    
    public abstract String getQuotaPreferenceId()

Optional. Id of the requesting object, must be unique under its parent. If client does not set this field, the service will generate one.

`string quota_preference_id = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The quotaPreferenceId.  
  
### getQuotaPreferenceIdBytes()
    
    
    public abstract ByteString getQuotaPreferenceIdBytes()

Optional. Id of the requesting object, must be unique under its parent. If client does not set this field, the service will generate one.

`string quota_preference_id = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for quotaPreferenceId.  
  
### getQuotaPreferenceOrBuilder()
    
    
    public abstract QuotaPreferenceOrBuilder getQuotaPreferenceOrBuilder()

Required. The resource being created

` .google.api.cloudquotas.v1.QuotaPreference quota_preference = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaPreferenceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaPreferenceOrBuilder)` |   
  
### hasQuotaPreference()
    
    
    public abstract boolean hasQuotaPreference()

Required. The resource being created

` .google.api.cloudquotas.v1.QuotaPreference quota_preference = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the quotaPreference field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
