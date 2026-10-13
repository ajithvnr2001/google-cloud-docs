---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequestOrBuilder
title: Interface AnnotateAssessmentRequestOrBuilder (3.96.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:46:33.997584+00:00
---

# Interface AnnotateAssessmentRequestOrBuilder (3.96.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AnnotateAssessmentRequestOrBuilder (3.96.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.96.0 (latest)  3.92.0  3.91.0  3.90.0  3.88.0  3.85.0  3.84.0  3.82.0  3.80.0  3.79.0  3.77.0  3.75.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.67.0  3.65.0  3.64.0  3.61.0  3.60.0  3.59.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.12  2.6.1  2.5.0  2.4.10  2.3.1 
    
    
    public interface AnnotateAssessmentRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccountId()
    
    
    public abstract String getAccountId()

Optional. A stable account identifier to apply to the assessment. This is an alternative to setting `account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request.

`string account_id = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The accountId.  
  
### getAccountIdBytes()
    
    
    public abstract ByteString getAccountIdBytes()

Optional. A stable account identifier to apply to the assessment. This is an alternative to setting `account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request.

`string account_id = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for accountId.  
  
### getAnnotation()
    
    
    public abstract AnnotateAssessmentRequest.Annotation getAnnotation()

Optional. The annotation that is assigned to the Event. This field can be left empty to provide reasons that apply to an event without concluding whether the event is legitimate or fraudulent.

` .google.cloud.recaptchaenterprise.v1.AnnotateAssessmentRequest.Annotation annotation = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AnnotateAssessmentRequest.Annotation](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.Annotation)` | The annotation.  
  
### getAnnotationValue()
    
    
    public abstract int getAnnotationValue()

Optional. The annotation that is assigned to the Event. This field can be left empty to provide reasons that apply to an event without concluding whether the event is legitimate or fraudulent.

` .google.cloud.recaptchaenterprise.v1.AnnotateAssessmentRequest.Annotation annotation = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for annotation.  
  
### getHashedAccountId()
    
    
    public abstract ByteString getHashedAccountId()

Optional. A stable hashed account identifier to apply to the assessment. This is an alternative to setting `hashed_account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request.

`bytes hashed_account_id = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The hashedAccountId.  
  
### getName()
    
    
    public abstract String getName()

Required. The resource name of the Assessment, in the format `projects/{project}/assessments/{assessment}`.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The resource name of the Assessment, in the format `projects/{project}/assessments/{assessment}`.

` string name = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPhoneAuthenticationEvent()
    
    
    public abstract PhoneAuthenticationEvent getPhoneAuthenticationEvent()

Optional. If using an external multi-factor authentication provider, provide phone authentication details for fraud detection purposes.

` .google.cloud.recaptchaenterprise.v1.PhoneAuthenticationEvent phone_authentication_event = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PhoneAuthenticationEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PhoneAuthenticationEvent)` | The phoneAuthenticationEvent.  
  
### getPhoneAuthenticationEventOrBuilder()
    
    
    public abstract PhoneAuthenticationEventOrBuilder getPhoneAuthenticationEventOrBuilder()

Optional. If using an external multi-factor authentication provider, provide phone authentication details for fraud detection purposes.

` .google.cloud.recaptchaenterprise.v1.PhoneAuthenticationEvent phone_authentication_event = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[PhoneAuthenticationEventOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.PhoneAuthenticationEventOrBuilder)` |   
  
### getReasons(int index)
    
    
    public abstract AnnotateAssessmentRequest.Reason getReasons(int index)

Optional. Reasons for the annotation that are assigned to the event.

` repeated .google.cloud.recaptchaenterprise.v1.AnnotateAssessmentRequest.Reason reasons = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[AnnotateAssessmentRequest.Reason](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.Reason)` | The reasons at the given index.  
  
### getReasonsCount()
    
    
    public abstract int getReasonsCount()

Optional. Reasons for the annotation that are assigned to the event.

` repeated .google.cloud.recaptchaenterprise.v1.AnnotateAssessmentRequest.Reason reasons = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of reasons.  
  
### getReasonsList()
    
    
    public abstract List<AnnotateAssessmentRequest.Reason> getReasonsList()

Optional. Reasons for the annotation that are assigned to the event.

` repeated .google.cloud.recaptchaenterprise.v1.AnnotateAssessmentRequest.Reason reasons = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Reason](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.AnnotateAssessmentRequest.Reason)>` | A list containing the reasons.  
  
### getReasonsValue(int index)
    
    
    public abstract int getReasonsValue(int index)

Optional. Reasons for the annotation that are assigned to the event.

` repeated .google.cloud.recaptchaenterprise.v1.AnnotateAssessmentRequest.Reason reasons = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of reasons at the given index.  
  
### getReasonsValueList()
    
    
    public abstract List<Integer> getReasonsValueList()

Optional. Reasons for the annotation that are assigned to the event.

` repeated .google.cloud.recaptchaenterprise.v1.AnnotateAssessmentRequest.Reason reasons = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for reasons.  
  
### getTransactionEvent()
    
    
    public abstract TransactionEvent getTransactionEvent()

Optional. If the assessment is part of a payment transaction, provide details on payment lifecycle events that occur in the transaction.

` .google.cloud.recaptchaenterprise.v1.TransactionEvent transaction_event = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TransactionEvent](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TransactionEvent)` | The transactionEvent.  
  
### getTransactionEventOrBuilder()
    
    
    public abstract TransactionEventOrBuilder getTransactionEventOrBuilder()

Optional. If the assessment is part of a payment transaction, provide details on payment lifecycle events that occur in the transaction.

` .google.cloud.recaptchaenterprise.v1.TransactionEvent transaction_event = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TransactionEventOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-recaptchaenterprise/latest/com.google.recaptchaenterprise.v1.TransactionEventOrBuilder)` |   
  
### hasPhoneAuthenticationEvent()
    
    
    public abstract boolean hasPhoneAuthenticationEvent()

Optional. If using an external multi-factor authentication provider, provide phone authentication details for fraud detection purposes.

` .google.cloud.recaptchaenterprise.v1.PhoneAuthenticationEvent phone_authentication_event = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the phoneAuthenticationEvent field is set.  
  
### hasTransactionEvent()
    
    
    public abstract boolean hasTransactionEvent()

Optional. If the assessment is part of a payment transaction, provide details on payment lifecycle events that occur in the transaction.

` .google.cloud.recaptchaenterprise.v1.TransactionEvent transaction_event = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the transactionEvent field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
