---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.MessageOrBuilder
title: Interface MessageOrBuilder (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:36.358277+00:00
---

# Interface MessageOrBuilder (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.MessageOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface MessageOrBuilder (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 
    
    
    public interface MessageOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getContent()
    
    
    public abstract String getContent()

Required. The message content.

`string content = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The content.  
  
### getContentBytes()
    
    
    public abstract ByteString getContentBytes()

Required. The message content.

`string content = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for content.  
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. The time when the message was created in Contact Center AI.

`.google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. The time when the message was created in Contact Center AI.

`.google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getLanguageCode()
    
    
    public abstract String getLanguageCode()

Optional. The message language. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US".

`string language_code = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageCode.  
  
### getLanguageCodeBytes()
    
    
    public abstract ByteString getLanguageCodeBytes()

Optional. The message language. This should be a [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. Example: "en-US".

`string language_code = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for languageCode.  
  
### getMessageAnnotation()
    
    
    public abstract MessageAnnotation getMessageAnnotation()

Output only. The annotation for the message.

` .google.cloud.dialogflow.v2beta1.MessageAnnotation message_annotation = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MessageAnnotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.MessageAnnotation)` | The messageAnnotation.  
  
### getMessageAnnotationOrBuilder()
    
    
    public abstract MessageAnnotationOrBuilder getMessageAnnotationOrBuilder()

Output only. The annotation for the message.

` .google.cloud.dialogflow.v2beta1.MessageAnnotation message_annotation = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[MessageAnnotationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.MessageAnnotationOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Optional. The unique identifier of the message. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`.

`string name = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Optional. The unique identifier of the message. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>`.

`string name = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getParticipant()
    
    
    public abstract String getParticipant()

Output only. The participant that sends this message.

`string participant = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The participant.  
  
### getParticipantBytes()
    
    
    public abstract ByteString getParticipantBytes()

Output only. The participant that sends this message.

`string participant = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for participant.  
  
### getParticipantRole()
    
    
    public abstract Participant.Role getParticipantRole()

Output only. The role of the participant.

` .google.cloud.dialogflow.v2beta1.Participant.Role participant_role = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Participant.Role](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.Participant.Role)` | The participantRole.  
  
### getParticipantRoleValue()
    
    
    public abstract int getParticipantRoleValue()

Output only. The role of the participant.

` .google.cloud.dialogflow.v2beta1.Participant.Role participant_role = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for participantRole.  
  
### getResponseMessages(int index)
    
    
    public abstract ResponseMessage getResponseMessages(int index)

Optional. Automated agent responses.

` repeated .google.cloud.dialogflow.v2beta1.ResponseMessage response_messages = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResponseMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ResponseMessage)` |   
  
### getResponseMessagesCount()
    
    
    public abstract int getResponseMessagesCount()

Optional. Automated agent responses.

` repeated .google.cloud.dialogflow.v2beta1.ResponseMessage response_messages = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResponseMessagesList()
    
    
    public abstract List<ResponseMessage> getResponseMessagesList()

Optional. Automated agent responses.

` repeated .google.cloud.dialogflow.v2beta1.ResponseMessage response_messages = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ResponseMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ResponseMessage)>` |   
  
### getResponseMessagesOrBuilder(int index)
    
    
    public abstract ResponseMessageOrBuilder getResponseMessagesOrBuilder(int index)

Optional. Automated agent responses.

` repeated .google.cloud.dialogflow.v2beta1.ResponseMessage response_messages = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResponseMessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.ResponseMessageOrBuilder)` |   
  
### getResponseMessagesOrBuilderList()
    
    
    public abstract List<? extends ResponseMessageOrBuilder> getResponseMessagesOrBuilderList()

Optional. Automated agent responses.

` repeated .google.cloud.dialogflow.v2beta1.ResponseMessage response_messages = 11 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.v2beta1.ResponseMessageOrBuilder>` |   
  
### getSendTime()
    
    
    public abstract Timestamp getSendTime()

Optional. The time when the message was sent. For voice messages, this is the time when an utterance started.

`.google.protobuf.Timestamp send_time = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The sendTime.  
  
### getSendTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getSendTimeOrBuilder()

Optional. The time when the message was sent. For voice messages, this is the time when an utterance started.

`.google.protobuf.Timestamp send_time = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getSentimentAnalysis()
    
    
    public abstract SentimentAnalysisResult getSentimentAnalysis()

Output only. The sentiment analysis result for the message.

` .google.cloud.dialogflow.v2beta1.SentimentAnalysisResult sentiment_analysis = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SentimentAnalysisResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SentimentAnalysisResult)` | The sentimentAnalysis.  
  
### getSentimentAnalysisOrBuilder()
    
    
    public abstract SentimentAnalysisResultOrBuilder getSentimentAnalysisOrBuilder()

Output only. The sentiment analysis result for the message.

` .google.cloud.dialogflow.v2beta1.SentimentAnalysisResult sentiment_analysis = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SentimentAnalysisResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2beta1.SentimentAnalysisResultOrBuilder)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. The time when the message was created in Contact Center AI.

`.google.protobuf.Timestamp create_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasMessageAnnotation()
    
    
    public abstract boolean hasMessageAnnotation()

Output only. The annotation for the message.

` .google.cloud.dialogflow.v2beta1.MessageAnnotation message_annotation = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the messageAnnotation field is set.  
  
### hasSendTime()
    
    
    public abstract boolean hasSendTime()

Optional. The time when the message was sent. For voice messages, this is the time when an utterance started.

`.google.protobuf.Timestamp send_time = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sendTime field is set.  
  
### hasSentimentAnalysis()
    
    
    public abstract boolean hasSentimentAnalysis()

Output only. The sentiment analysis result for the message.

` .google.cloud.dialogflow.v2beta1.SentimentAnalysisResult sentiment_analysis = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sentimentAnalysis field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
