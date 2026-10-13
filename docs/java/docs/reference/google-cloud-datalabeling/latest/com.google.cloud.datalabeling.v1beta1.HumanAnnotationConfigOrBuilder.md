---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.HumanAnnotationConfigOrBuilder
title: Interface HumanAnnotationConfigOrBuilder (0.215.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:05.882008+00:00
---

# Interface HumanAnnotationConfigOrBuilder (0.215.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datalabeling/latest/com.google.cloud.datalabeling.v1beta1.HumanAnnotationConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface HumanAnnotationConfigOrBuilder (0.215.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.215.0 (latest)  0.214.0  0.213.0  0.211.0  0.208.0  0.207.0  0.205.0  0.203.0  0.202.0  0.201.0  0.200.0  0.198.0  0.196.0  0.195.0  0.194.0  0.193.0  0.192.0  0.190.0  0.188.0  0.187.0  0.184.0  0.183.0  0.182.0  0.180.0  0.179.0  0.178.0  0.177.0  0.176.0  0.175.0  0.174.0  0.173.0  0.172.0  0.171.0  0.169.0  0.168.0  0.167.0  0.166.0  0.165.0  0.164.0  0.163.0  0.162.0  0.161.0  0.160.0  0.159.0  0.157.0  0.156.0  0.155.0  0.154.0  0.153.0  0.152.0  0.151.0  0.150.0  0.149.0  0.148.0  0.147.0  0.144.0  0.143.0  0.142.0  0.141.0  0.140.0  0.139.0  0.138.0  0.137.0  0.136.0  0.135.0  0.134.0  0.133.0  0.132.0  0.131.0  0.129.0  0.128.0  0.127.0  0.126.0  0.125.0  0.124.0  0.123.7  0.122.11 
    
    
    public interface HumanAnnotationConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAnnotatedDatasetDescription()
    
    
    public abstract String getAnnotatedDatasetDescription()

Optional. A human-readable description for AnnotatedDataset. The description can be up to 10000 characters long.

`string annotated_dataset_description = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The annotatedDatasetDescription.  
  
### getAnnotatedDatasetDescriptionBytes()
    
    
    public abstract ByteString getAnnotatedDatasetDescriptionBytes()

Optional. A human-readable description for AnnotatedDataset. The description can be up to 10000 characters long.

`string annotated_dataset_description = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for annotatedDatasetDescription.  
  
### getAnnotatedDatasetDisplayName()
    
    
    public abstract String getAnnotatedDatasetDisplayName()

Required. A human-readable name for AnnotatedDataset defined by users. Maximum of 64 characters .

`string annotated_dataset_display_name = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The annotatedDatasetDisplayName.  
  
### getAnnotatedDatasetDisplayNameBytes()
    
    
    public abstract ByteString getAnnotatedDatasetDisplayNameBytes()

Required. A human-readable name for AnnotatedDataset defined by users. Maximum of 64 characters .

`string annotated_dataset_display_name = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for annotatedDatasetDisplayName.  
  
### getContributorEmails(int index)
    
    
    public abstract String getContributorEmails(int index)

Optional. If you want your own labeling contributors to manage and work on this labeling request, you can set these contributors here. We will give them access to the question types in crowdcompute. Note that these emails must be registered in crowdcompute worker UI: <https://crowd-compute.appspot.com/>

`repeated string contributor_emails = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The contributorEmails at the given index.  
  
### getContributorEmailsBytes(int index)
    
    
    public abstract ByteString getContributorEmailsBytes(int index)

Optional. If you want your own labeling contributors to manage and work on this labeling request, you can set these contributors here. We will give them access to the question types in crowdcompute. Note that these emails must be registered in crowdcompute worker UI: <https://crowd-compute.appspot.com/>

`repeated string contributor_emails = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the contributorEmails at the given index.  
  
### getContributorEmailsCount()
    
    
    public abstract int getContributorEmailsCount()

Optional. If you want your own labeling contributors to manage and work on this labeling request, you can set these contributors here. We will give them access to the question types in crowdcompute. Note that these emails must be registered in crowdcompute worker UI: <https://crowd-compute.appspot.com/>

`repeated string contributor_emails = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of contributorEmails.  
  
### getContributorEmailsList()
    
    
    public abstract List<String> getContributorEmailsList()

Optional. If you want your own labeling contributors to manage and work on this labeling request, you can set these contributors here. We will give them access to the question types in crowdcompute. Note that these emails must be registered in crowdcompute worker UI: <https://crowd-compute.appspot.com/>

`repeated string contributor_emails = 9 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the contributorEmails.  
  
### getInstruction()
    
    
    public abstract String getInstruction()

Required. Instruction resource name.

`string instruction = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The instruction.  
  
### getInstructionBytes()
    
    
    public abstract ByteString getInstructionBytes()

Required. Instruction resource name.

`string instruction = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for instruction.  
  
### getLabelGroup()
    
    
    public abstract String getLabelGroup()

Optional. A human-readable label used to logically group labeling tasks. This string must match the regular expression `[a-zA-Z\\d_-]{0,128}`.

`string label_group = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The labelGroup.  
  
### getLabelGroupBytes()
    
    
    public abstract ByteString getLabelGroupBytes()

Optional. A human-readable label used to logically group labeling tasks. This string must match the regular expression `[a-zA-Z\\d_-]{0,128}`.

`string label_group = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for labelGroup.  
  
### getLanguageCode()
    
    
    public abstract String getLanguageCode()

Optional. The Language of this question, as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). Default value is en-US. Only need to set this when task is language related. For example, French text classification.

`string language_code = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageCode.  
  
### getLanguageCodeBytes()
    
    
    public abstract ByteString getLanguageCodeBytes()

Optional. The Language of this question, as a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). Default value is en-US. Only need to set this when task is language related. For example, French text classification.

`string language_code = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for languageCode.  
  
### getQuestionDuration()
    
    
    public abstract Duration getQuestionDuration()

Optional. Maximum duration for contributors to answer a question. Maximum is 3600 seconds. Default is 3600 seconds.

` .google.protobuf.Duration question_duration = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The questionDuration.  
  
### getQuestionDurationOrBuilder()
    
    
    public abstract DurationOrBuilder getQuestionDurationOrBuilder()

Optional. Maximum duration for contributors to answer a question. Maximum is 3600 seconds. Default is 3600 seconds.

` .google.protobuf.Duration question_duration = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getReplicaCount()
    
    
    public abstract int getReplicaCount()

Optional. Replication of questions. Each question will be sent to up to this number of contributors to label. Aggregated answers will be returned. Default is set to 1. For image related labeling, valid values are 1, 3, 5.

`int32 replica_count = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The replicaCount.  
  
### getUserEmailAddress()
    
    
    public abstract String getUserEmailAddress()

Email of the user who started the labeling task and should be notified by email. If empty no notification will be sent.

`string user_email_address = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The userEmailAddress.  
  
### getUserEmailAddressBytes()
    
    
    public abstract ByteString getUserEmailAddressBytes()

Email of the user who started the labeling task and should be notified by email. If empty no notification will be sent.

`string user_email_address = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for userEmailAddress.  
  
### hasQuestionDuration()
    
    
    public abstract boolean hasQuestionDuration()

Optional. Maximum duration for contributors to answer a question. Maximum is 3600 seconds. Default is 3600 seconds.

` .google.protobuf.Duration question_duration = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the questionDuration field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
