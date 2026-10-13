---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.DestinationDetails
title: Audit Manager v1 API - Class DestinationDetails (1.3.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:38.139436+00:00
---

# Audit Manager v1 API - Class DestinationDetails (1.3.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.DestinationDetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Audit Manager v1 API - Class DestinationDetails (1.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.0 (latest)  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class DestinationDetails : IMessage<DestinationDetails>, IEquatable<DestinationDetails>, IDeepCloneable<DestinationDetails>, IBufferMessage, IMessage

Reference documentation and code samples for the Audit Manager v1 API class DestinationDetails.

Cloud Storage bucket where the audit report is uploaded to.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DestinationDetails

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DestinationDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.DestinationDetails), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DestinationDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.DestinationDetails), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DestinationDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.DestinationDetails), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AuditManager.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1)

## Assembly

Google.Cloud.AuditManager.V1.dll

## Constructors 

### DestinationDetails()
    
    
    public DestinationDetails()

### DestinationDetails(DestinationDetails)
    
    
    public DestinationDetails(DestinationDetails other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DestinationDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.DestinationDetails)`  
  
  
## Properties 

### DestinationCase
    
    
    public DestinationDetails.DestinationOneofCase DestinationCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[DestinationDetails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.DestinationDetails)[DestinationOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AuditManager.V1/latest/Google.Cloud.AuditManager.V1.DestinationDetails.DestinationOneofCase)` |   
  
### GcsBucketUri
    
    
    public string GcsBucketUri { get; set; }

URI for the Cloud Storage bucket, in the format `gs://{bucket_name}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasGcsBucketUri
    
    
    public bool HasGcsBucketUri { get; }

Gets whether the "gcs_bucket_uri" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
