---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App
title: Gemini Enterprise for Customer Experience v1beta API - Class App (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:39:53.060980+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class App (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class App (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public sealed class App : IMessage<App>, IEquatable<App>, IDeepCloneable<App>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class App.

An app serves as a top-level container for a group of agents, including the root agent and its sub-agents, along with their associated configurations. These agents work together to achieve specific goals within the app's context.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > App

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Constructors 

### App()
    
    
    public App()

### App(App)
    
    
    public App(App other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)`  
  
  
## Properties 

### AppName
    
    
    public AppName AppName { get; set; }

[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App#Google_Cloud_Ces_V1Beta_App_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AppName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AppName)` |   
  
### AudioProcessingConfig
    
    
    public AudioProcessingConfig AudioProcessingConfig { get; set; }

Optional. Audio processing configuration of the app.

**Property Value**  
---  
**Type** | **Description**  
`[AudioProcessingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AudioProcessingConfig)` |   
  
### ClientCertificateSettings
    
    
    public ClientCertificateSettings ClientCertificateSettings { get; set; }

Optional. The default client certificate settings for the app.

**Property Value**  
---  
**Type** | **Description**  
`[ClientCertificateSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ClientCertificateSettings)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Timestamp when the app was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DataStoreSettings
    
    
    public DataStoreSettings DataStoreSettings { get; set; }

Optional. The data store settings for the app.

**Property Value**  
---  
**Type** | **Description**  
`[DataStoreSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.DataStoreSettings)` |   
  
### DefaultChannelProfile
    
    
    public ChannelProfile DefaultChannelProfile { get; set; }

Optional. The default channel profile used by the app.

**Property Value**  
---  
**Type** | **Description**  
`[ChannelProfile](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ChannelProfile)` |   
  
### DeploymentCount
    
    
    public int DeploymentCount { get; set; }

Output only. Number of deployments in the app.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Description
    
    
    public string Description { get; set; }

Optional. Human-readable description of the app.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Required. Display name of the app.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ErrorHandlingSettings
    
    
    public ErrorHandlingSettings ErrorHandlingSettings { get; set; }

Optional. Error handling settings of the app.

**Property Value**  
---  
**Type** | **Description**  
`[ErrorHandlingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ErrorHandlingSettings)` |   
  
### Etag
    
    
    public string Etag { get; set; }

Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EvaluationMetricsThresholds
    
    
    public EvaluationMetricsThresholds EvaluationMetricsThresholds { get; set; }

Optional. The evaluation thresholds for the app.

**Property Value**  
---  
**Type** | **Description**  
`[EvaluationMetricsThresholds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationMetricsThresholds)` |   
  
### EvaluationPersonas
    
    
    public RepeatedField<EvaluationPersona> EvaluationPersonas { get; }

Optional. The evaluation personas for the app. This field is used to define the personas that can be used for evaluation. Maximum of 30 personas can be defined.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[EvaluationPersona](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationPersona)` |   
  
### EvaluationSettings
    
    
    public EvaluationSettings EvaluationSettings { get; set; }

Optional. The evaluation settings for the app.

**Property Value**  
---  
**Type** | **Description**  
`[EvaluationSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.EvaluationSettings)` |   
  
### GlobalInstruction
    
    
    public string GlobalInstruction { get; set; }

Optional. Instructions for all the agents in the app. You can use this instruction to set up a stable identity or personality across all the agents.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Guardrails
    
    
    public RepeatedField<string> Guardrails { get; }

Optional. List of guardrails for the app. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### GuardrailsAsGuardrailNames
    
    
    public ResourceNameList<GuardrailName> GuardrailsAsGuardrailNames { get; }

[GuardrailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GuardrailName)-typed view over the [Guardrails](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App#Google_Cloud_Ces_V1Beta_App_Guardrails) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ResourceNameList](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNameList-1.html)[GuardrailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GuardrailName)` |   
  
### LanguageSettings
    
    
    public LanguageSettings LanguageSettings { get; set; }

Optional. Language settings of the app.

**Property Value**  
---  
**Type** | **Description**  
`[LanguageSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.LanguageSettings)` |   
  
### Locked
    
    
    public bool Locked { get; set; }

Optional. Indicates whether the app is locked for changes. If the app is locked, modifications to the app resources will be rejected.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### LoggingSettings
    
    
    public LoggingSettings LoggingSettings { get; set; }

Optional. Logging settings of the app.

**Property Value**  
---  
**Type** | **Description**  
`[LoggingSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.LoggingSettings)` |   
  
### Metadata
    
    
    public MapField<string, string> Metadata { get; }

Optional. Metadata about the app. This field can be used to store additional information relevant to the app's details or intended usages.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ModelSettings
    
    
    public ModelSettings ModelSettings { get; set; }

Optional. The default LLM model settings for the app. Individual resources (e.g. agents, guardrails) can override these configurations as needed.

**Property Value**  
---  
**Type** | **Description**  
`[ModelSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ModelSettings)` |   
  
### Name
    
    
    public string Name { get; set; }

Identifier. The unique identifier of the app. Format: `projects/{project}/locations/{location}/apps/{app}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Pinned
    
    
    public bool Pinned { get; set; }

Optional. Whether the app is pinned in the app list.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### PredefinedVariableDeclarations
    
    
    public RepeatedField<App.Types.VariableDeclaration> PredefinedVariableDeclarations { get; }

Output only. The declarations of predefined variables for the app.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App.Types)[VariableDeclaration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App.Types.VariableDeclaration)` |   
  
### RootAgent
    
    
    public string RootAgent { get; set; }

Optional. The root agent is the entry point of the app. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RootAgentAsAgentName
    
    
    public AgentName RootAgentAsAgentName { get; set; }

[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName)-typed view over the [RootAgent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App#Google_Cloud_Ces_V1Beta_App_RootAgent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentName)` |   
  
### TimeZoneSettings
    
    
    public TimeZoneSettings TimeZoneSettings { get; set; }

Optional. TimeZone settings of the app.

**Property Value**  
---  
**Type** | **Description**  
`[TimeZoneSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.TimeZoneSettings)` |   
  
### ToolExecutionMode
    
    
    public App.Types.ToolExecutionMode ToolExecutionMode { get; set; }

Optional. The tool execution mode for the app. If not provided, will default to PARALLEL.

**Property Value**  
---  
**Type** | **Description**  
`[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App.Types)[ToolExecutionMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App.Types.ToolExecutionMode)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Timestamp when the app was last updated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### ValidationErrors
    
    
    public RepeatedField<string> ValidationErrors { get; }

Output only. Misconfigurations or warnings in the app.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### VariableDeclarations
    
    
    public RepeatedField<App.Types.VariableDeclaration> VariableDeclarations { get; }

Optional. The declarations of the variables.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[App](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App.Types)[VariableDeclaration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.App.Types.VariableDeclaration)` |   
  
### VpcScSettings
    
    
    public VpcScSettings VpcScSettings { get; set; }

Optional. VPC-SC settings for the app.

**Property Value**  
---  
**Type** | **Description**  
`[VpcScSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.VpcScSettings)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
