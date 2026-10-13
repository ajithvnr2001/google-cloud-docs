---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Deployment
title: Gemini Enterprise for Customer Experience v1 API - Class Deployment (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:36.798713+00:00
---

# Gemini Enterprise for Customer Experience v1 API - Class Deployment (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Deployment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1 API - Class Deployment (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta04 
    
    
    public sealed class Deployment : IMessage<Deployment>, IEquatable<Deployment>, IDeepCloneable<Deployment>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1 API class Deployment.

A deployment represents an immutable, queryable version of the app. It is used to deploy an app version with a specific channel profile.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Deployment

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Deployment), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Deployment), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Deployment), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1)

## Assembly

Google.Cloud.Ces.V1.dll

## Constructors 

### Deployment()
    
    
    public Deployment()

### Deployment(Deployment)
    
    
    public Deployment(Deployment other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Deployment](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Deployment)`  
  
  
## Properties 

### AppVersion
    
    
    public string AppVersion { get; set; }

Optional. The resource name of the app version to deploy. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}` Use `projects/{project}/locations/{location}/apps/{app}/versions/-` to use the draft app.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AppVersionAsAppVersionName
    
    
    public AppVersionName AppVersionAsAppVersionName { get; set; }

[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.AppVersionName)-typed view over the [AppVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Deployment#Google_Cloud_Ces_V1_Deployment_AppVersion) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AppVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.AppVersionName)` |   
  
### ChannelProfile
    
    
    public ChannelProfile ChannelProfile { get; set; }

Required. The channel profile used in the deployment.

**Property Value**  
---  
**Type** | **Description**  
`[ChannelProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.ChannelProfile)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Timestamp when this deployment was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DeploymentName
    
    
    public DeploymentName DeploymentName { get; set; }

[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DeploymentName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.Deployment#Google_Cloud_Ces_V1_Deployment_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[DeploymentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.DeploymentName)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Required. Display name of the deployment.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ExperimentConfig
    
    
    public ExperimentConfig ExperimentConfig { get; set; }

Optional. Experiment configuration for the deployment.

**Property Value**  
---  
**Type** | **Description**  
`[ExperimentConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.ExperimentConfig)` |   
  
### InstagramCredentials
    
    
    public InstagramCredentials InstagramCredentials { get; set; }

Optional. Input only. Ephemeral Instagram credentials required when configuring a Instagram channel profile.

**Property Value**  
---  
**Type** | **Description**  
`[InstagramCredentials](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.InstagramCredentials)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The resource name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Timestamp when this deployment was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### WhatsappCredentials
    
    
    public WhatsAppCredentials WhatsappCredentials { get; set; }

Optional. Input only. Ephemeral WhatsApp credentials required when configuring a WhatsApp channel profile.

**Property Value**  
---  
**Type** | **Description**  
`[WhatsAppCredentials](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1/latest/Google.Cloud.Ces.V1.WhatsAppCredentials)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
