---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1Beta1/latest/Google.Cloud.RecaptchaEnterprise.V1Beta1.RecaptchaEnterpriseServiceV1Beta1.RecaptchaEnterpriseServiceV1Beta1Base
title: Google Cloud reCAPTCHA Enterprise v1beta1 API - Class RecaptchaEnterpriseServiceV1Beta1.RecaptchaEnterpriseServiceV1Beta1Base (2.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:24.719107+00:00
---

# Google Cloud reCAPTCHA Enterprise v1beta1 API - Class RecaptchaEnterpriseServiceV1Beta1.RecaptchaEnterpriseServiceV1Beta1Base (2.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1Beta1/latest/Google.Cloud.RecaptchaEnterprise.V1Beta1.RecaptchaEnterpriseServiceV1Beta1.RecaptchaEnterpriseServiceV1Beta1Base

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud reCAPTCHA Enterprise v1beta1 API - Class RecaptchaEnterpriseServiceV1Beta1.RecaptchaEnterpriseServiceV1Beta1Base (2.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta10 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1Beta1/latest/Google.Cloud.RecaptchaEnterprise.V1Beta1.RecaptchaEnterpriseServiceV1Beta1.RecaptchaEnterpriseServiceV1Beta1Base)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1Beta1/2.0.0-beta09/Google.Cloud.RecaptchaEnterprise.V1Beta1.RecaptchaEnterpriseServiceV1Beta1.RecaptchaEnterpriseServiceV1Beta1Base)
  * [ 1.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1Beta1/1.0.0-beta06/Google.Cloud.RecaptchaEnterprise.V1Beta1.RecaptchaEnterpriseServiceV1Beta1.RecaptchaEnterpriseServiceV1Beta1Base)


    
    
    [BindServiceMethod(typeof(RecaptchaEnterpriseServiceV1Beta1), "BindService")]
    public abstract class RecaptchaEnterpriseServiceV1Beta1.RecaptchaEnterpriseServiceV1Beta1Base

Reference documentation and code samples for the Google Cloud reCAPTCHA Enterprise v1beta1 API class RecaptchaEnterpriseServiceV1Beta1.RecaptchaEnterpriseServiceV1Beta1Base.

Base class for server-side implementations of RecaptchaEnterpriseServiceV1Beta1

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RecaptchaEnterpriseServiceV1Beta1.RecaptchaEnterpriseServiceV1Beta1Base

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.RecaptchaEnterprise.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1Beta1/latest/Google.Cloud.RecaptchaEnterprise.V1Beta1)

## Assembly

Google.Cloud.RecaptchaEnterprise.V1Beta1.dll

## Methods 

### AnnotateAssessment(AnnotateAssessmentRequest, ServerCallContext)
    
    
    public virtual Task<AnnotateAssessmentResponse> AnnotateAssessment(AnnotateAssessmentRequest request, ServerCallContext context)

Annotates a previously created Assessment to provide additional information on whether the event turned out to be authentic or fradulent.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AnnotateAssessmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1Beta1/latest/Google.Cloud.RecaptchaEnterprise.V1Beta1.AnnotateAssessmentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AnnotateAssessmentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1Beta1/latest/Google.Cloud.RecaptchaEnterprise.V1Beta1.AnnotateAssessmentResponse)` | The response to send back to the client (wrapped by a task).  
  
### CreateAssessment(CreateAssessmentRequest, ServerCallContext)
    
    
    public virtual Task<Assessment> CreateAssessment(CreateAssessmentRequest request, ServerCallContext context)

Creates an Assessment of the likelihood an event is legitimate.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAssessmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1Beta1/latest/Google.Cloud.RecaptchaEnterprise.V1Beta1.CreateAssessmentRequest)`  
The request received from the client.  
`context` | `[ServerCallContext](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerCallContext.html)`  
The context of the server-side call handler being invoked.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Assessment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecaptchaEnterprise.V1Beta1/latest/Google.Cloud.RecaptchaEnterprise.V1Beta1.Assessment)` | The response to send back to the client (wrapped by a task).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
