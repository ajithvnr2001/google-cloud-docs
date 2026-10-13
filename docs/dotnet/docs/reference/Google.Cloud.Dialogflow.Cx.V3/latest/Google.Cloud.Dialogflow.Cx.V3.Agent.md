---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent
title: Dialogflow v3 API - Class Agent (3.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:44.032035+00:00
---

# Dialogflow v3 API - Class Agent (3.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dialogflow v3 API - Class Agent (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class Agent : IMessage<Agent>, IEquatable<Agent>, IDeepCloneable<Agent>, IBufferMessage, IMessage

Reference documentation and code samples for the Dialogflow v3 API class Agent.

Agents are best described as Natural Language Understanding (NLU) modules that transform user requests into actionable data. You can include agents in your app, product, or service to determine user intent and respond to the user in a natural way.

After you create an agent, you can add [Intents][google.cloud.dialogflow.cx.v3.Intent], [Entity Types][google.cloud.dialogflow.cx.v3.EntityType], [Flows][google.cloud.dialogflow.cx.v3.Flow], [Fulfillments][google.cloud.dialogflow.cx.v3.Fulfillment], [Webhooks][google.cloud.dialogflow.cx.v3.Webhook], [TransitionRouteGroups][google.cloud.dialogflow.cx.v3.TransitionRouteGroup] and so on to manage the conversation flows.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Agent

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dialogflow.Cx.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3)

## Assembly

Google.Cloud.Dialogflow.Cx.V3.dll

## Constructors 

### Agent()
    
    
    public Agent()

### Agent(Agent)
    
    
    public Agent(Agent other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)`  
  
  
## Properties 

### AdvancedSettings
    
    
    public AdvancedSettings AdvancedSettings { get; set; }

Hierarchical advanced settings for this agent. The settings exposed at the lower level overrides the settings exposed at the higher level.

**Property Value**  
---  
**Type** | **Description**  
`[AdvancedSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AdvancedSettings)` |   
  
### AgentName
    
    
    public AgentName AgentName { get; set; }

[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent#Google_Cloud_Dialogflow_Cx_V3_Agent_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)` |   
  
### AnswerFeedbackSettings
    
    
    public Agent.Types.AnswerFeedbackSettings AnswerFeedbackSettings { get; set; }

Optional. Answer feedback collection settings.

**Property Value**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types)[AnswerFeedbackSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.AnswerFeedbackSettings)` |   
  
### AvatarUri
    
    
    public string AvatarUri { get; set; }

The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ClientCertificateSettings
    
    
    public Agent.Types.ClientCertificateSettings ClientCertificateSettings { get; set; }

Optional. Settings for custom client certificates.

**Property Value**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types)[ClientCertificateSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.ClientCertificateSettings)` |   
  
### DefaultLanguageCode
    
    
    public string DefaultLanguageCode { get; set; }

Required. Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the [Agents.UpdateAgent][google.cloud.dialogflow.cx.v3.Agents.UpdateAgent] method.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Description
    
    
    public string Description { get; set; }

The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

Required. The human-readable name of the agent, unique within the location.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EnableMultiLanguageTraining
    
    
    public bool EnableMultiLanguageTraining { get; set; }

Optional. Enable training multi-lingual models for this agent. These models will be trained on all the languages supported by the agent.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnableSpellCorrection
    
    
    public bool EnableSpellCorrection { get; set; }

Indicates if automatic spell correction is enabled in detect intent requests.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### EnableStackdriverLogging
    
    
    [Obsolete]
    public bool EnableStackdriverLogging { get; set; }

Indicates if stackdriver logging is enabled for the agent. Please use [agent.advanced_settings][google.cloud.dialogflow.cx.v3.AdvancedSettings.LoggingSettings] instead.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### GenAppBuilderSettings
    
    
    public Agent.Types.GenAppBuilderSettings GenAppBuilderSettings { get; set; }

Gen App Builder-related agent-level settings.

**Property Value**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types)[GenAppBuilderSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.GenAppBuilderSettings)` |   
  
### GitIntegrationSettings
    
    
    public Agent.Types.GitIntegrationSettings GitIntegrationSettings { get; set; }

Git integration settings for this agent.

**Property Value**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types)[GitIntegrationSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.GitIntegrationSettings)` |   
  
### HasSatisfiesPzi
    
    
    public bool HasSatisfiesPzi { get; }

Gets whether the "satisfies_pzi" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSatisfiesPzs
    
    
    public bool HasSatisfiesPzs { get; }

Gets whether the "satisfies_pzs" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStartFlow
    
    
    public bool HasStartFlow { get; }

Gets whether the "start_flow" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStartPlaybook
    
    
    public bool HasStartPlaybook { get; }

Gets whether the "start_playbook" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Locked
    
    
    public bool Locked { get; set; }

Indicates whether the agent is locked for changes. If the agent is locked, modifications to the agent will be rejected except for [RestoreAgent][].

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Name
    
    
    public string Name { get; set; }

The unique identifier of the agent. Required for the [Agents.UpdateAgent][google.cloud.dialogflow.cx.v3.Agents.UpdateAgent] method. [Agents.CreateAgent][google.cloud.dialogflow.cx.v3.Agents.CreateAgent] populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### PersonalizationSettings
    
    
    public Agent.Types.PersonalizationSettings PersonalizationSettings { get; set; }

Optional. Settings for end user personalization.

**Property Value**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types)[PersonalizationSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.Types.PersonalizationSettings)` |   
  
### SatisfiesPzi
    
    
    public bool SatisfiesPzi { get; set; }

Optional. Output only. A read only boolean field reflecting Zone Isolation status of the agent.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SatisfiesPzs
    
    
    public bool SatisfiesPzs { get; set; }

Optional. Output only. A read only boolean field reflecting Zone Separation status of the agent.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SecuritySettings
    
    
    public string SecuritySettings { get; set; }

Name of the [SecuritySettings][google.cloud.dialogflow.cx.v3.SecuritySettings] reference for the agent. Format: `projects/<ProjectID>/locations/<LocationID>/securitySettings/<SecuritySettingsID>`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SecuritySettingsAsSecuritySettingsName
    
    
    public SecuritySettingsName SecuritySettingsAsSecuritySettingsName { get; set; }

[SecuritySettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsName)-typed view over the [SecuritySettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent#Google_Cloud_Dialogflow_Cx_V3_Agent_SecuritySettings) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SecuritySettingsName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SecuritySettingsName)` |   
  
### SessionEntryResourceCase
    
    
    public Agent.SessionEntryResourceOneofCase SessionEntryResourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Agent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent)[SessionEntryResourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent.SessionEntryResourceOneofCase)` |   
  
### SpeechToTextSettings
    
    
    public SpeechToTextSettings SpeechToTextSettings { get; set; }

Speech recognition related settings.

**Property Value**  
---  
**Type** | **Description**  
`[SpeechToTextSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.SpeechToTextSettings)` |   
  
### StartFlow
    
    
    public string StartFlow { get; set; }

Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`. Currently only the default start flow with id "00000000-0000-0000-0000-000000000000" is allowed.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StartFlowAsFlowName
    
    
    public FlowName StartFlowAsFlowName { get; set; }

[FlowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowName)-typed view over the [StartFlow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent#Google_Cloud_Dialogflow_Cx_V3_Agent_StartFlow) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[FlowName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.FlowName)` |   
  
### StartPlaybook
    
    
    public string StartPlaybook { get; set; }

Name of the start playbook in this agent. A start playbook will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`. Currently only the default playbook with id "00000000-0000-0000-0000-000000000000" is allowed.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### StartPlaybookAsPlaybookName
    
    
    public PlaybookName StartPlaybookAsPlaybookName { get; set; }

[PlaybookName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookName)-typed view over the [StartPlaybook](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Agent#Google_Cloud_Dialogflow_Cx_V3_Agent_StartPlaybook) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[PlaybookName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.PlaybookName)` |   
  
### SupportedLanguageCodes
    
    
    public RepeatedField<string> SupportedLanguageCodes { get; }

The list of all languages supported by the agent (except for the `default_language_code`).

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TextToSpeechSettings
    
    
    public TextToSpeechSettings TextToSpeechSettings { get; set; }

Settings on instructing the speech synthesizer on how to generate the output audio content.

**Property Value**  
---  
**Type** | **Description**  
`[TextToSpeechSettings](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.TextToSpeechSettings)` |   
  
### TimeZone
    
    
    public string TimeZone { get; set; }

Required. The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
