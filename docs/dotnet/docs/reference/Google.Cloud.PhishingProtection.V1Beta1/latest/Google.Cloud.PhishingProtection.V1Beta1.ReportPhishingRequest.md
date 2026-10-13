---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest
title: Cloud Phishing Protection v1beta1 API - Class ReportPhishingRequest (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:20.276300+00:00
---

# Cloud Phishing Protection v1beta1 API - Class ReportPhishingRequest (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Phishing Protection v1beta1 API - Class ReportPhishingRequest (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/2.0.0-beta05/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest)
  * [ 1.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/1.0.0-beta05/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest)


    
    
    public sealed class ReportPhishingRequest : IMessage<ReportPhishingRequest>, IEquatable<ReportPhishingRequest>, IDeepCloneable<ReportPhishingRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Phishing Protection v1beta1 API class ReportPhishingRequest.

The ReportPhishing request message.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReportPhishingRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ReportPhishingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReportPhishingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ReportPhishingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.PhishingProtection.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1)

## Assembly

Google.Cloud.PhishingProtection.V1Beta1.dll

## Constructors 

### ReportPhishingRequest()
    
    
    public ReportPhishingRequest()

### ReportPhishingRequest(ReportPhishingRequest)
    
    
    public ReportPhishingRequest(ReportPhishingRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReportPhishingRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. The name of the project for which the report will be created, in the format "projects/{project_number}".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsProjectName
    
    
    public ProjectName ParentAsProjectName { get; set; }

[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PhishingProtection.V1Beta1/latest/Google.Cloud.PhishingProtection.V1Beta1.ReportPhishingRequest#Google_Cloud_PhishingProtection_V1Beta1_ReportPhishingRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)` |   
  
### Uri
    
    
    public string Uri { get; set; }

Required. The URI that is being reported for phishing content to be analyzed.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
