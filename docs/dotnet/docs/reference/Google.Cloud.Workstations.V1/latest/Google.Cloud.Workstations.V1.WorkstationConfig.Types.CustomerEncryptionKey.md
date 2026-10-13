---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig.Types.CustomerEncryptionKey
title: Cloud Workstations v1 API - Class WorkstationConfig.Types.CustomerEncryptionKey (1.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:04:13.660022+00:00
---

# Cloud Workstations v1 API - Class WorkstationConfig.Types.CustomerEncryptionKey (1.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig.Types.CustomerEncryptionKey

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Workstations v1 API - Class WorkstationConfig.Types.CustomerEncryptionKey (1.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.0 (latest)  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class WorkstationConfig.Types.CustomerEncryptionKey : IMessage<WorkstationConfig.Types.CustomerEncryptionKey>, IEquatable<WorkstationConfig.Types.CustomerEncryptionKey>, IDeepCloneable<WorkstationConfig.Types.CustomerEncryptionKey>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Workstations v1 API class WorkstationConfig.Types.CustomerEncryptionKey.

A customer-managed encryption key (CMEK) for the Compute Engine resources of the associated workstation configuration. Specify the name of your Cloud KMS encryption key and the default service account. We recommend that you use a separate service account and follow [Cloud KMS best practices](https://cloud.google.com/kms/docs/separation-of-duties).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > WorkstationConfig.Types.CustomerEncryptionKey

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[WorkstationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig.Types)[CustomerEncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig.Types.CustomerEncryptionKey), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[WorkstationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig.Types)[CustomerEncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig.Types.CustomerEncryptionKey), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[WorkstationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig.Types)[CustomerEncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig.Types.CustomerEncryptionKey), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Workstations.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1)

## Assembly

Google.Cloud.Workstations.V1.dll

## Constructors 

### CustomerEncryptionKey()
    
    
    public CustomerEncryptionKey()

### CustomerEncryptionKey(CustomerEncryptionKey)
    
    
    public CustomerEncryptionKey(WorkstationConfig.Types.CustomerEncryptionKey other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[WorkstationConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig.Types)[CustomerEncryptionKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Workstations.V1/latest/Google.Cloud.Workstations.V1.WorkstationConfig.Types.CustomerEncryptionKey)`  
  
  
## Properties 

### KmsKey
    
    
    public string KmsKey { get; set; }

Immutable. The name of the Google Cloud KMS encryption key. For example, `"projects/PROJECT_ID/locations/REGION/keyRings/KEY_RING/cryptoKeys/KEY_NAME"`. The key must be in the same region as the workstation configuration.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KmsKeyServiceAccount
    
    
    public string KmsKeyServiceAccount { get; set; }

Immutable. The service account to use with the specified KMS key. We recommend that you use a separate service account and follow KMS best practices. For more information, see [Separation of duties](https://cloud.google.com/kms/docs/separation-of-duties) and `gcloud kms keys add-iam-policy-binding` [`--member`](https://cloud.google.com/sdk/gcloud/reference/kms/keys/add-iam-policy-binding#--member).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-08 UTC."],[],[]] 
