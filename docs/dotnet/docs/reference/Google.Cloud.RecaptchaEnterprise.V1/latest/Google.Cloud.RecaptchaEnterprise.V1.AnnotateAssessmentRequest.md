---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest
title: Google Cloud reCAPTCHA Enterprise v1 API - Class AnnotateAssessmentRequest (2.21.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:35.824256+00:00
---

# Google Cloud reCAPTCHA Enterprise v1 API - Class AnnotateAssessmentRequest (2.21.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud reCAPTCHA Enterprise v1 API - Class AnnotateAssessmentRequest (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0 
    
    
    public sealed class AnnotateAssessmentRequest : IMessage<AnnotateAssessmentRequest>, IEquatable<AnnotateAssessmentRequest>, IDeepCloneable<AnnotateAssessmentRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud reCAPTCHA Enterprise v1 API class AnnotateAssessmentRequest.

The request message to annotate an Assessment.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnnotateAssessmentRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AnnotateAssessmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AnnotateAssessmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AnnotateAssessmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.RecaptchaEnterprise.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1)

## Assembly

Google.Cloud.RecaptchaEnterprise.V1.dll

## Constructors 

### AnnotateAssessmentRequest()
    
    
    public AnnotateAssessmentRequest()

### AnnotateAssessmentRequest(AnnotateAssessmentRequest)
    
    
    public AnnotateAssessmentRequest(AnnotateAssessmentRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AnnotateAssessmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest)`  
  
  
## Properties 

### AccountId
    
    
    public string AccountId { get; set; }

Optional. A stable account identifier to apply to the assessment. This is an alternative to setting `account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Annotation
    
    
    public AnnotateAssessmentRequest.Types.Annotation Annotation { get; set; }

Optional. The annotation that is assigned to the Event. This field can be left empty to provide reasons that apply to an event without concluding whether the event is legitimate or fraudulent.

**Property Value**  
---  
**Type** | **Description**  
`[AnnotateAssessmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest.Types)[Annotation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest.Types.Annotation)` |   
  
### AssessmentName
    
    
    public AssessmentName AssessmentName { get; set; }

[AssessmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AssessmentName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest#Google_Cloud_RecaptchaEnterprise_V1_AnnotateAssessmentRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AssessmentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AssessmentName)` |   
  
### HashedAccountId
    
    
    public ByteString HashedAccountId { get; set; }

Optional. A stable hashed account identifier to apply to the assessment. This is an alternative to setting `hashed_account_id` in `CreateAssessment`, for example when a stable account identifier is not yet known in the initial request.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The resource name of the Assessment, in the format `projects/{project}/assessments/{assessment}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PhoneAuthenticationEvent
    
    
    public PhoneAuthenticationEvent PhoneAuthenticationEvent { get; set; }

Optional. If using an external multi-factor authentication provider, provide phone authentication details for fraud detection purposes.

**Property Value**  
---  
**Type** | **Description**  
`[PhoneAuthenticationEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.PhoneAuthenticationEvent)` |   
  
### Reasons
    
    
    public RepeatedField<AnnotateAssessmentRequest.Types.Reason> Reasons { get; }

Optional. Reasons for the annotation that are assigned to the event.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AnnotateAssessmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest.Types)[Reason](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.AnnotateAssessmentRequest.Types.Reason)` |   
  
### TransactionEvent
    
    
    public TransactionEvent TransactionEvent { get; set; }

Optional. If the assessment is part of a payment transaction, provide details on payment lifecycle events that occur in the transaction.

**Property Value**  
---  
**Type** | **Description**  
`[TransactionEvent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1/latest/Google.Cloud.RecaptchaEnterprise.V1.TransactionEvent)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-18 UTC."],[],[]] 
