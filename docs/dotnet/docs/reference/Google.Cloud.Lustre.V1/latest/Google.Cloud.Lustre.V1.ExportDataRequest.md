---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest
title: Google Cloud Managed Lustre v1 API - Class ExportDataRequest (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:24.124904+00:00
---

# Google Cloud Managed Lustre v1 API - Class ExportDataRequest (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Managed Lustre v1 API - Class ExportDataRequest (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class ExportDataRequest : IMessage<ExportDataRequest>, IEquatable<ExportDataRequest>, IDeepCloneable<ExportDataRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Managed Lustre v1 API class ExportDataRequest.

Export data from Managed Lustre to a Cloud Storage bucket.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ExportDataRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ExportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ExportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ExportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Lustre.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1)

## Assembly

Google.Cloud.Lustre.V1.dll

## Constructors 

### ExportDataRequest()
    
    
    public ExportDataRequest()

### ExportDataRequest(ExportDataRequest)
    
    
    public ExportDataRequest(ExportDataRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ExportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest)`  
  
  
## Properties 

### DestinationCase
    
    
    public ExportDataRequest.DestinationOneofCase DestinationCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ExportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest)[DestinationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest.DestinationOneofCase)` |   
  
### GcsPath
    
    
    public GcsPath GcsPath { get; set; }

The URI to a Cloud Storage bucket, or a path within a bucket, using the format `gs://<bucket_name>/<optional_path_inside_bucket>/`. If a path inside the bucket is specified, it must end with a forward slash (`/`).

**Property Value**  
---  
**Type** | **Description**  
`[GcsPath](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.GcsPath)` |   
  
### InstanceName
    
    
    public InstanceName InstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest#Google_Cloud_Lustre_V1_ExportDataRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.InstanceName)` |   
  
### LustrePath
    
    
    public LustrePath LustrePath { get; set; }

The root directory path to the Managed Lustre file system. Must start with `/`. Default is `/`.

**Property Value**  
---  
**Type** | **Description**  
`[LustrePath](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.LustrePath)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The name of the Managed Lustre instance in the format `projects/{project}/locations/{location}/instances/{instance}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RequestId
    
    
    public string RequestId { get; set; }

Optional. UUID to identify requests.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceAccount
    
    
    public string ServiceAccount { get; set; }

Optional. User-specified service account used to perform the transfer. If unspecified, the Managed Lustre service agent is used.

Use one of the following formats:

  * `{EMAIL_ADDRESS_OR_UNIQUE_ID}`
  * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}`
  * `projects/-/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}`



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServiceAccountAsServiceAccountName
    
    
    public ServiceAccountName ServiceAccountAsServiceAccountName { get; set; }

[ServiceAccountName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ServiceAccountName)-typed view over the [ServiceAccount](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest#Google_Cloud_Lustre_V1_ExportDataRequest_ServiceAccount) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceAccountName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ServiceAccountName)` |   
  
### SourceCase
    
    
    public ExportDataRequest.SourceOneofCase SourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ExportDataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest)[SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Lustre.V1/latest/Google.Cloud.Lustre.V1.ExportDataRequest.SourceOneofCase)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
