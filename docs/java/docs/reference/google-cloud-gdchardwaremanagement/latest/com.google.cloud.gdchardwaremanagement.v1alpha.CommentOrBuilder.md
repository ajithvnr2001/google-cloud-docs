---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CommentOrBuilder
title: Interface CommentOrBuilder (0.54.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:27.889888+00:00
---

# Interface CommentOrBuilder (0.54.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CommentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CommentOrBuilder (0.54.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.54.0 (latest)  0.50.0  0.49.0  0.48.0  0.46.0  0.43.0  0.42.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.19.0  0.18.0  0.17.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface CommentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. Labels associated with this comment as key value pairs. For more information about labels, see [Create and manage labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels).

`map<string, string> labels = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAuthor()
    
    
    public abstract String getAuthor()

Output only. Username of the author of this comment. This is auto-populated from the credentials used during creation of the comment.

`string author = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The author.  
  
### getAuthorBytes()
    
    
    public abstract ByteString getAuthorBytes()

Output only. Username of the author of this comment. This is auto-populated from the credentials used during creation of the comment.

`string author = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for author.  
  
### getAuthorEntity()
    
    
    public abstract Entity getAuthorEntity()

Output only. The entity the author belongs to.

` .google.cloud.gdchardwaremanagement.v1alpha.Entity author_entity = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Entity](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.Entity)` | The authorEntity.  
  
### getAuthorEntityValue()
    
    
    public abstract int getAuthorEntityValue()

Output only. The entity the author belongs to.

` .google.cloud.gdchardwaremanagement.v1alpha.Entity author_entity = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for authorEntity.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Time when this comment was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Time when this comment was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCustomerViewedTime()
    
    
    public abstract Timestamp getCustomerViewedTime()

Output only. Timestamp of the first time this comment was viewed by the customer. If the comment wasn't viewed then this timestamp will be unset.

` .google.protobuf.Timestamp customer_viewed_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The customerViewedTime.  
  
### getCustomerViewedTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCustomerViewedTimeOrBuilder()

Output only. Timestamp of the first time this comment was viewed by the customer. If the comment wasn't viewed then this timestamp will be unset.

` .google.protobuf.Timestamp customer_viewed_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-gdchardwaremanagement/latest/com.google.cloud.gdchardwaremanagement.v1alpha.CommentOrBuilder#com_google_cloud_gdchardwaremanagement_v1alpha_CommentOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. Labels associated with this comment as key value pairs. For more information about labels, see [Create and manage labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels).

`map<string, string> labels = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. Labels associated with this comment as key value pairs. For more information about labels, see [Create and manage labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels).

`map<string, string> labels = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. Labels associated with this comment as key value pairs. For more information about labels, see [Create and manage labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels).

`map<string, string> labels = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Optional. Labels associated with this comment as key value pairs. For more information about labels, see [Create and manage labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels).

`map<string, string> labels = 3 [(.google.api.field_behavior) = OPTIONAL];`

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

Identifier. Name of this comment. Format: `projects/{project}/locations/{location}/orders/{order}/comments/{comment}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. Name of this comment. Format: `projects/{project}/locations/{location}/orders/{order}/comments/{comment}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getText()
    
    
    public abstract String getText()

Required. Text of this comment. The length of text must be <= 1000 characters.

`string text = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The text.  
  
### getTextBytes()
    
    
    public abstract ByteString getTextBytes()

Required. Text of this comment. The length of text must be <= 1000 characters.

`string text = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for text.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Time when this comment was created.

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasCustomerViewedTime()
    
    
    public abstract boolean hasCustomerViewedTime()

Output only. Timestamp of the first time this comment was viewed by the customer. If the comment wasn't viewed then this timestamp will be unset.

` .google.protobuf.Timestamp customer_viewed_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customerViewedTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
