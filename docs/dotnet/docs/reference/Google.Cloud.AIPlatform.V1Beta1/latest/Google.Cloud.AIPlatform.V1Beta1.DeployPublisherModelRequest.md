---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelRequest
title: Vertex AI v1beta1 API - Class DeployPublisherModelRequest (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:40.593729+00:00
---

# Vertex AI v1beta1 API - Class DeployPublisherModelRequest (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class DeployPublisherModelRequest (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    [Obsolete]
    public sealed class DeployPublisherModelRequest : IMessage<DeployPublisherModelRequest>, IEquatable<DeployPublisherModelRequest>, IDeepCloneable<DeployPublisherModelRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class DeployPublisherModelRequest.

Request message for [ModelGardenService.DeployPublisherModel][google.cloud.aiplatform.v1beta1.ModelGardenService.DeployPublisherModel].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeployPublisherModelRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeployPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeployPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeployPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### DeployPublisherModelRequest()
    
    
    public DeployPublisherModelRequest()

### DeployPublisherModelRequest(DeployPublisherModelRequest)
    
    
    public DeployPublisherModelRequest(DeployPublisherModelRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeployPublisherModelRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelRequest)`  
  
  
## Properties 

### AcceptEula
    
    
    public bool AcceptEula { get; set; }

Optional. Whether the user accepts the End User License Agreement (EULA) for the model.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### DedicatedResources
    
    
    public DedicatedResources DedicatedResources { get; set; }

Optional. The dedicated resources to use for the endpoint. If not set, the default resources will be used.

**Property Value**  
---  
**Type** | **Description**  
`[DedicatedResources](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DedicatedResources)` |   
  
### Destination
    
    
    public string Destination { get; set; }

Required. The resource name of the Location to deploy the model in. Format: `projects/{project}/locations/{location}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DestinationAsLocationName
    
    
    [Obsolete]
    public LocationName DestinationAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Destination](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeployPublisherModelRequest#Google_Cloud_AIPlatform_V1Beta1_DeployPublisherModelRequest_Destination) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### EndpointDisplayName
    
    
    public string EndpointDisplayName { get; set; }

Optional. The user-specified display name of the endpoint. If not set, a default name will be used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HuggingFaceAccessToken
    
    
    public string HuggingFaceAccessToken { get; set; }

Optional. The Hugging Face read access token used to access the model artifacts of gated models.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Model
    
    
    public string Model { get; set; }

Required. The model to deploy. Format:

  1. `publishers/{publisher}/models/{publisher_model}@{version_id}`, or `publishers/hf-{hugging-face-author}/models/{hugging-face-model-name}@001`.
  2. Hugging Face model ID like `google/gemma-2-2b-it`.
  3. Custom model Google Cloud Storage URI like `gs://bucket`.
  4. Custom model zip file like `https://example.com/a.zip`.



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ModelDisplayName
    
    
    public string ModelDisplayName { get; set; }

Optional. The user-specified display name of the uploaded model. If not set, a default name will be used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
