---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.OAuthConfig
title: Dataform v1 API - Class OAuthConfig (1.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:02.142273+00:00
---

# Dataform v1 API - Class OAuthConfig (1.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.OAuthConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataform v1 API - Class OAuthConfig (1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0 
    
    
    public sealed class OAuthConfig : IMessage<OAuthConfig>, IEquatable<OAuthConfig>, IDeepCloneable<OAuthConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataform v1 API class OAuthConfig.

OAuth configuration for end user authentication.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > OAuthConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[OAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.OAuthConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[OAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.OAuthConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[OAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.OAuthConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataform.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1)

## Assembly

Google.Cloud.Dataform.V1.dll

## Constructors 

### OAuthConfig()
    
    
    public OAuthConfig()

### OAuthConfig(OAuthConfig)
    
    
    public OAuthConfig(OAuthConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[OAuthConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataform.V1/latest/Google.Cloud.Dataform.V1.OAuthConfig)`  
  
  
## Properties 

### AdditionalOauthScopes
    
    
    public RepeatedField<string> AdditionalOauthScopes { get; }

Optional. Additional OAuth scopes to use for BigQuery executions. Scopes always in use: `https://www.googleapis.com/auth/bigquery`

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
