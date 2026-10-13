---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlResponse
title: Cloud Functions v2beta API - Class GenerateUploadUrlResponse (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:25.397507+00:00
---

# Cloud Functions v2beta API - Class GenerateUploadUrlResponse (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Functions v2beta API - Class GenerateUploadUrlResponse (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlResponse)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/1.0.0-beta07/Google.Cloud.Functions.V2Beta.GenerateUploadUrlResponse)


    
    
    public sealed class GenerateUploadUrlResponse : IMessage<GenerateUploadUrlResponse>, IEquatable<GenerateUploadUrlResponse>, IDeepCloneable<GenerateUploadUrlResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Functions v2beta API class GenerateUploadUrlResponse.

Response of `GenerateSourceUploadUrl` method.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GenerateUploadUrlResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GenerateUploadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GenerateUploadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GenerateUploadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Functions.V2Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta)

## Assembly

Google.Cloud.Functions.V2Beta.dll

## Constructors 

### GenerateUploadUrlResponse()
    
    
    public GenerateUploadUrlResponse()

### GenerateUploadUrlResponse(GenerateUploadUrlResponse)
    
    
    public GenerateUploadUrlResponse(GenerateUploadUrlResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GenerateUploadUrlResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.GenerateUploadUrlResponse)`  
  
  
## Properties 

### StorageSource
    
    
    public StorageSource StorageSource { get; set; }

The location of the source code in the upload bucket.

Once the archive is uploaded using the `upload_url` use this field to set the `function.build_config.source.storage_source` during CreateFunction and UpdateFunction.

Generation defaults to 0, as Cloud Storage provides a new generation only upon uploading a new object or version of an object.

**Property Value**  
---  
**Type** | **Description**  
`[StorageSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Functions.V2Beta/latest/Google.Cloud.Functions.V2Beta.StorageSource)` |   
  
### UploadUrl
    
    
    public string UploadUrl { get; set; }

The generated Google Cloud Storage signed URL that should be used for a function source code upload. The uploaded file should be a zip archive which contains a function.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
