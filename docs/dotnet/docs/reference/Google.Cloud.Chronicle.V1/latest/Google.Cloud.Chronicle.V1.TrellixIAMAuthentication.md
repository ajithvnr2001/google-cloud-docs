---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.TrellixIAMAuthentication
title: Chronicle v1 API - Class TrellixIAMAuthentication (1.1.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:08.542744+00:00
---

# Chronicle v1 API - Class TrellixIAMAuthentication (1.1.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.TrellixIAMAuthentication

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Chronicle v1 API - Class TrellixIAMAuthentication (1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.0 
    
    
    public sealed class TrellixIAMAuthentication : IMessage<TrellixIAMAuthentication>, IEquatable<TrellixIAMAuthentication>, IDeepCloneable<TrellixIAMAuthentication>, IBufferMessage, IMessage

Reference documentation and code samples for the Chronicle v1 API class TrellixIAMAuthentication.

Settings for TrellixIAMAuthentication.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TrellixIAMAuthentication

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[TrellixIAMAuthentication](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.TrellixIAMAuthentication), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TrellixIAMAuthentication](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.TrellixIAMAuthentication), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[TrellixIAMAuthentication](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.TrellixIAMAuthentication), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Chronicle.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1)

## Assembly

Google.Cloud.Chronicle.V1.dll

## Constructors 

### TrellixIAMAuthentication()
    
    
    public TrellixIAMAuthentication()

### TrellixIAMAuthentication(TrellixIAMAuthentication)
    
    
    public TrellixIAMAuthentication(TrellixIAMAuthentication other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TrellixIAMAuthentication](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Chronicle.V1/latest/Google.Cloud.Chronicle.V1.TrellixIAMAuthentication)`  
  
  
## Properties 

### ClientId
    
    
    public string ClientId { get; set; }

Required. Client ID generated in Trellix IAM. This is a unique identifier for the user that is generated in Trellix IAM. It has no default, specifically enforced min / max length or character set. It is assumed that the Client ID generated in Trellix IAM is internally consistent with Trellix IAM authentication requirements / validation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ClientSecret
    
    
    public string ClientSecret { get; set; }

Required. Secret associated with the Client ID. This is the secret generated in Trellix IAM for the Client ID. It has no default, specifically enforced min / max length or character set. It is assumed that the secret generated in Trellix IAM is internally consistent with Trellix IAM authentication requirements / validation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Scope
    
    
    public string Scope { get; set; }

Required. OAUTH 2 scope to request for the authentication token. This is the OAUTH 2 scope to request for the authentication token. It has no default, specifically enforced min / max length or character set. It is assumed that the scope provided is internally consistent with Trellix IAM authentication requirements / validation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
