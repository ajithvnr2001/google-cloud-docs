---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.StartEnvironmentRequest
title: Cloud Shell v1 API - Class StartEnvironmentRequest (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:38.240705+00:00
---

# Cloud Shell v1 API - Class StartEnvironmentRequest (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.StartEnvironmentRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Shell v1 API - Class StartEnvironmentRequest (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.StartEnvironmentRequest)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/2.5.0/Google.Cloud.Shell.V1.StartEnvironmentRequest)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/2.4.0/Google.Cloud.Shell.V1.StartEnvironmentRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/2.3.0/Google.Cloud.Shell.V1.StartEnvironmentRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/2.2.0/Google.Cloud.Shell.V1.StartEnvironmentRequest)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/2.1.0/Google.Cloud.Shell.V1.StartEnvironmentRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/2.0.0/Google.Cloud.Shell.V1.StartEnvironmentRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/1.1.0/Google.Cloud.Shell.V1.StartEnvironmentRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/1.0.0/Google.Cloud.Shell.V1.StartEnvironmentRequest)


    
    
    public sealed class StartEnvironmentRequest : IMessage<StartEnvironmentRequest>, IEquatable<StartEnvironmentRequest>, IDeepCloneable<StartEnvironmentRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Shell v1 API class StartEnvironmentRequest.

Request message for [StartEnvironment][google.cloud.shell.v1.CloudShellService.StartEnvironment].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StartEnvironmentRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[StartEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.StartEnvironmentRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[StartEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.StartEnvironmentRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[StartEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.StartEnvironmentRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Shell.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1)

## Assembly

Google.Cloud.Shell.V1.dll

## Constructors 

### StartEnvironmentRequest()
    
    
    public StartEnvironmentRequest()

### StartEnvironmentRequest(StartEnvironmentRequest)
    
    
    public StartEnvironmentRequest(StartEnvironmentRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StartEnvironmentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Shell.V1/latest/Google.Cloud.Shell.V1.StartEnvironmentRequest)`  
  
  
## Properties 

### AccessToken
    
    
    public string AccessToken { get; set; }

The initial access token passed to the environment. If this is present and valid, the environment will be pre-authenticated with gcloud so that the user can run gcloud commands in Cloud Shell without having to log in. This code can be updated later by calling AuthorizeEnvironment.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Name of the resource that should be started, for example `users/me/environments/default` or `users/someone@example.com/environments/default`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PublicKeys
    
    
    public RepeatedField<string> PublicKeys { get; }

Public keys that should be added to the environment before it is started.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
