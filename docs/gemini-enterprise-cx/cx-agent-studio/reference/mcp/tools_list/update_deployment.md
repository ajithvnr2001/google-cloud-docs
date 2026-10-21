---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_deployment/
title: MCP Tools Reference: ces.googleapis.com \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:48:22.637236+00:00
---

# MCP Tools Reference: ces.googleapis.com  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/update_deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP Tools Reference: ces.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `update_deployment`

Updates the specified deployment. Make sure to always pass an update mask in the input.

The following code sample shows how to use `curl` to call the `update_deployment` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://ces.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "update_deployment",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `AgentService.UpdateDeployment`.

### UpdateDeploymentRequest

JSON representation  
---  
      
    
    {
      "deployment": {
        object ([Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.Deployment))
      },
      "updateMask": string
    }  
  
Fields  
---  
`deployment` |  `object (`[Deployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.Deployment)`)` Required. The deployment to update.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The list of fields to update.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Deployment

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "appVersion": string,
      "channelProfile": {
        object ([ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelProfile))
      },
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "experimentConfig": {
        object ([ExperimentConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.ExperimentConfig))
      },
      "whatsappCredentials": {
        object ([WhatsAppCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.WhatsAppCredentials))
      },
      "instagramCredentials": {
        object ([InstagramCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.InstagramCredentials))
      },
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "modality": enum ([Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.Modality_1)),
      "agentRegistryDeployment": {
        object ([AgentRegistryDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.AgentRegistryDeployment))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`displayName` |  `string` Required. Display name of the deployment.  
`appVersion` |  `string` Optional. The resource name of the app version to deploy. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}` Use `projects/{project}/locations/{location}/apps/{app}/versions/-` to use the draft app.  
`channelProfile` |  `object (`[ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelProfile)`)` Required. The channel profile used in the deployment.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this deployment was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this deployment was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`experimentConfig` |  `object (`[ExperimentConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.ExperimentConfig)`)` Optional. Experiment configuration for the deployment.  
`whatsappCredentials` |  `object (`[WhatsAppCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.WhatsAppCredentials)`)` Optional. Input only. Ephemeral WhatsApp credentials required when configuring a WhatsApp channel profile.  
`instagramCredentials` |  `object (`[InstagramCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.InstagramCredentials)`)` Optional. Input only. Ephemeral Instagram credentials required when configuring a Instagram channel profile.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. Model settings for the deployment. Overrides model settings configured at the app/agent levels. Note: Deployment-level model settings override is gated behind an allowlist. Contact the CXAS team to enable this field.  
`modality` |  `enum (`[Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.Modality_1)`)` Optional. The modality of the deployment. Note: Deployment-level modality override is gated behind an allowlist. Contact the CXAS team to enable this field.  
`agentRegistryDeployment` |  `object (`[AgentRegistryDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.AgentRegistryDeployment)`)` Optional. Configuration for deploying this deployment to Agent Registry. If present, this deployment will be published to Agent Registry.  
  
### ChannelProfile

JSON representation  
---  
      
    
    {
      "profileId": string,
      "channelType": enum ([ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelType)),
      "personaProperty": {
        object ([PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.PersonaProperty))
      },
      "webWidgetConfig": {
        object ([WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WebWidgetConfig))
      },
      "whatsappConfig": {
        object ([WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WhatsAppConfig))
      },
      "instagramConfig": {
        object ([InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.InstagramConfig))
      },
    
      // Union field _disable_dtmf can be only one of the following:
      "disableDtmf": boolean
      // End of list of possible types for union field _disable_dtmf.
    
      // Union field _disable_barge_in_control can be only one of the following:
      "disableBargeInControl": boolean
      // End of list of possible types for union field _disable_barge_in_control.
    
      // Union field _noise_suppression_level can be only one of the following:
      "noiseSuppressionLevel": string
      // End of list of possible types for union field _noise_suppression_level.
    }  
  
Fields  
---  
`profileId` |  `string` Optional. The unique identifier of the channel profile.  
`channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelType)`)` Optional. The type of the channel profile.  
`personaProperty` |  `object (`[PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.PersonaProperty)`)` Optional. The persona property of the channel profile.  
`webWidgetConfig` |  `object (`[WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WebWidgetConfig)`)` Optional. The configuration for the web widget.  
`whatsappConfig` |  `object (`[WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WhatsAppConfig)`)` Optional. Configuration specific to WhatsApp deployments.  
`instagramConfig` |  `object (`[InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.InstagramConfig)`)` Optional. Configuration specific to Instagram deployments.  
Union field `_disable_dtmf`.`_disable_dtmf` can be only one of the following:  
`disableDtmf` |  `boolean` Optional. Whether to disable DTMF (dual-tone multi-frequency).  
Union field `_disable_barge_in_control`.`_disable_barge_in_control` can be only one of the following:  
`disableBargeInControl` |  `boolean` Optional. Whether to disable user barge-in control in the conversation. - **true** : User interruptions are disabled while the agent is speaking. - **false** : The agent retains automatic control over when the user can interrupt.  
Union field `_noise_suppression_level`.`_noise_suppression_level` can be only one of the following:  
`noiseSuppressionLevel` |  `string` Optional. The noise suppression level of the channel profile. Available values are "low", "moderate", "high", "very_high".  
  
### PersonaProperty

JSON representation  
---  
      
    
    {
      "persona": enum ([Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Persona))
    }  
  
Fields  
---  
`persona` |  `enum (`[Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Persona)`)` Optional. The persona of the channel.  
  
### WebWidgetConfig

JSON representation  
---  
      
    
    {
      "modality": enum ([Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Modality)),
      "theme": enum ([Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Theme)),
      "webWidgetTitle": string,
      "securitySettings": {
        object ([SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SecuritySettings))
      }
    }  
  
Fields  
---  
`modality` |  `enum (`[Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Modality)`)` Optional. The modality of the web widget.  
`theme` |  `enum (`[Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Theme)`)` Optional. The theme of the web widget.  
`webWidgetTitle` |  `string` Optional. The title of the web widget.  
`securitySettings` |  `object (`[SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SecuritySettings)`)` Optional. The security settings of the web widget.  
  
### SecuritySettings

JSON representation  
---  
      
    
    {
      "enablePublicAccess": boolean,
      "enableOriginCheck": boolean,
      "allowedOrigins": [
        string
      ],
      "enableRecaptcha": boolean
    }  
  
Fields  
---  
`enablePublicAccess` |  `boolean` Optional. Indicates whether public access to the web widget is enabled. If `true`, the web widget will be publicly accessible. If `false`, the web widget must be integrated with your own authentication and authorization system to return valid credentials for accessing the CES agent.  
`enableOriginCheck` |  `boolean` Optional. Indicates whether origin check for the web widget is enabled. If `true`, the web widget will check the origin of the website that loads the web widget and only allow it to be loaded in the same origin or any of the allowed origins.  
`allowedOrigins[]` |  `string` Optional. The origins that are allowed to host the web widget. An origin is defined by RFC 6454. If empty, all origins are allowed. A maximum of 100 origins is allowed. Example: "https://example.com"  
`enableRecaptcha` |  `boolean` Optional. Indicates whether reCAPTCHA verification for the web widget is enabled.  
  
### WhatsAppConfig

JSON representation  
---  
      
    
    {
      "wabaId": string,
      "phoneNumberId": string,
      "phoneNumber": string,
      "displayName": string,
      "thumbnailUrl": string,
      "description": string
    }  
  
Fields  
---  
`wabaId` |  `string` Required. The WhatsApp Business Account ID.  
`phoneNumberId` |  `string` Required. The Meta phone number ID.  
`phoneNumber` |  `string` Optional. The phone number in E.164 format.  
`displayName` |  `string` Output only. The fetched Meta business page name.  
`thumbnailUrl` |  `string` Output only. The fetched Meta business profile thumbnail URL.  
`description` |  `string` Output only. The description of the Meta business page or profile.  
  
### InstagramConfig

JSON representation  
---  
      
    
    {
      "instagramAccountId": string,
      "displayName": string,
      "thumbnailUrl": string,
      "description": string
    }  
  
Fields  
---  
`instagramAccountId` |  `string` Required. The Instagram Account ID.  
`displayName` |  `string` Output only. The fetched Meta business page name.  
`thumbnailUrl` |  `string` Output only. The fetched Meta business profile thumbnail URL.  
`description` |  `string` Output only. The description of the Meta business page or profile.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### ExperimentConfig

JSON representation  
---  
      
    
    {
      "versionRelease": {
        object ([VersionRelease](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.VersionRelease))
      }
    }  
  
Fields  
---  
`versionRelease` |  `object (`[VersionRelease](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.VersionRelease)`)` Optional. Version release for the experiment.  
  
### VersionRelease

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.State)),
      "trafficAllocations": [
        {
          object ([TrafficAllocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.TrafficAllocation))
        }
      ]
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.State)`)` Optional. State of the version release.  
`trafficAllocations[]` |  `object (`[TrafficAllocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.TrafficAllocation)`)` Optional. Traffic allocations for the version release.  
  
### TrafficAllocation

JSON representation  
---  
      
    
    {
      "id": string,
      "trafficPercentage": integer,
      "appVersion": string
    }  
  
Fields  
---  
`id` |  `string` Optional. Id of the traffic allocation. Free format string, up to 128 characters.  
`trafficPercentage` |  `integer` Optional. Traffic percentage of the traffic allocation. Must be between 0 and 100.  
`appVersion` |  `string` Optional. App version of the traffic allocation. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
  
### WhatsAppCredentials

JSON representation  
---  
      
    
    {
      "authCode": string,
      "pin": string,
      "phoneNumber": string,
      "businessAccountId": string,
      "wabaId": string,
      "conversationProfileId": string
    }  
  
Fields  
---  
`authCode` |  `string` Required. The Meta auth code provided by the embedded signup flow.  
`pin` |  `string` Required. The 6-digit PIN created by the user for two-step verification.  
`phoneNumber` |  `string` Required. The phone number to register with WhatsApp.  
`businessAccountId` |  `string` Required. The Business Account ID to use for the phone number.  
`wabaId` |  `string` Required. The WhatsApp Business Account ID.  
`conversationProfileId` |  `string` Optional. The Conversation Profile ID to use for the deployment.  
  
### InstagramCredentials

JSON representation  
---  
      
    
    {
      "authCode": string,
      "conversationProfileId": string
    }  
  
Fields  
---  
`authCode` |  `string` Required. The Meta auth code provided by the embedded signup flow.  
`conversationProfileId` |  `string` Optional. The Conversation Profile ID to use for the deployment.  
  
### ModelSettings

JSON representation  
---  
      
    
    {
      "model": string,
      "thinkingLevel": enum ([ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ThinkingLevel)),
    
      // Union field _temperature can be only one of the following:
      "temperature": number
      // End of list of possible types for union field _temperature.
    }  
  
Fields  
---  
`model` |  `string` Optional. The LLM model that the agent should use. If not set, the agent will inherit the model from its parent agent.  
`thinkingLevel` |  `enum (`[ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ThinkingLevel)`)` Optional. The thinking level of the model.  
Union field `_temperature`.`_temperature` can be only one of the following:  
`temperature` |  `number` Optional. If set, this temperature will be used for the LLM model. Temperature controls the randomness of the model's responses. Lower temperatures produce responses that are more predictable. Higher temperatures produce responses that are more creative.  
  
### AgentRegistryDeployment

JSON representation  
---  
      
    
    {
      "agentRegistryServiceName": string
    }  
  
Fields  
---  
`agentRegistryServiceName` |  `string` Optional. Output only. The resource name of the deployed Agent Registry service. Format: `projects/{project}/locations/{location}/services/{service}`  
  
### FieldMask

JSON representation  
---  
      
    
    {
      "paths": [
        string
      ]
    }  
  
Fields  
---  
`paths[]` |  `string` The set of field mask paths.  
  
### ChannelType

The type of the channel profile.

Enums  
---  
`UNKNOWN` | Unknown channel type.  
`WEB_UI` | Web UI channel.  
`API` | API channel.  
`TWILIO` | Twilio channel.  
`GOOGLE_TELEPHONY_PLATFORM` | Google Telephony Platform channel.  
`CONTACT_CENTER_AS_A_SERVICE` | Contact Center as a Service (CCaaS) channel.  
`CONTACT_CENTER_AS_A_SERVICE_CHAT` | Contact Center as a Service (CCaaS Chat) channel.  
`FIVE9` | Five9 channel.  
`CONTACT_CENTER_INTEGRATION` | Third party contact center integration channel.  
`WHATSAPP` | WhatsApp channel.  
`INSTAGRAM` | Instagram channel.  
  
### Persona

The persona of the channel.

Enums  
---  
`UNKNOWN` | UNKNOWN persona.  
`CONCISE` | The agent keeps the responses concise and to the point  
`CHATTY` | The agent provides additional context, explanations, and details  
  
### Modality

Modality of the web widget.

Enums  
---  
`MODALITY_UNSPECIFIED` | Unknown modality.  
`CHAT_AND_VOICE` | Widget supports both chat and voice input.  
`VOICE_ONLY` | Widget supports only voice input.  
`CHAT_ONLY` | Widget supports only chat input.  
`CHAT_VOICE_AND_VIDEO` | Widget supports chat, voice, and video input.  
  
### Theme

Theme of the web widget.

Enums  
---  
`THEME_UNSPECIFIED` | Unknown theme.  
`LIGHT` | Light theme.  
`DARK` | Dark theme.  
  
### State

State of the experiment.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`PENDING` | Deprecated: This state is no longer used.  
`RUNNING` | Running state. Experiment is running and valid.  
`DONE` | Deprecated: This state is no longer used.  
`EXPIRED` | Deprecated: This state is no longer used.  
  
### ThinkingLevel

Thinking level configuration for the model.

Enums  
---  
`THINKING_LEVEL_UNSPECIFIED` | Thinking level is unspecified.  
`DEFAULT` | Default thinking level.  
`LOW` | Low thinking level.  
`MEDIUM` | Medium thinking level.  
`HIGH` | High thinking level.  
  
### Modality

The modality of the deployment.

Enums  
---  
`MODALITY_UNSPECIFIED` | Unknown modality.  
`MODALITY_TEXT` | Text modality.  
`MODALITY_VOICE` | Voice modality.  
`MODALITY_VIDEO` | Video modality.  
  
## Output Schema

A deployment represents an immutable, queryable version of the app. It is used to deploy an app version with a specific channel profile.

### Deployment

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "appVersion": string,
      "channelProfile": {
        object ([ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelProfile))
      },
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "experimentConfig": {
        object ([ExperimentConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.ExperimentConfig))
      },
      "whatsappCredentials": {
        object ([WhatsAppCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.WhatsAppCredentials))
      },
      "instagramCredentials": {
        object ([InstagramCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.InstagramCredentials))
      },
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "modality": enum ([Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.Modality_1)),
      "agentRegistryDeployment": {
        object ([AgentRegistryDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.AgentRegistryDeployment))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the deployment. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`displayName` |  `string` Required. Display name of the deployment.  
`appVersion` |  `string` Optional. The resource name of the app version to deploy. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}` Use `projects/{project}/locations/{location}/apps/{app}/versions/-` to use the draft app.  
`channelProfile` |  `object (`[ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelProfile)`)` Required. The channel profile used in the deployment.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this deployment was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when this deployment was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`experimentConfig` |  `object (`[ExperimentConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.ExperimentConfig)`)` Optional. Experiment configuration for the deployment.  
`whatsappCredentials` |  `object (`[WhatsAppCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.WhatsAppCredentials)`)` Optional. Input only. Ephemeral WhatsApp credentials required when configuring a WhatsApp channel profile.  
`instagramCredentials` |  `object (`[InstagramCredentials](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.InstagramCredentials)`)` Optional. Input only. Ephemeral Instagram credentials required when configuring a Instagram channel profile.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. Model settings for the deployment. Overrides model settings configured at the app/agent levels. Note: Deployment-level model settings override is gated behind an allowlist. Contact the CXAS team to enable this field.  
`modality` |  `enum (`[Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.Modality_1)`)` Optional. The modality of the deployment. Note: Deployment-level modality override is gated behind an allowlist. Contact the CXAS team to enable this field.  
`agentRegistryDeployment` |  `object (`[AgentRegistryDeployment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.AgentRegistryDeployment)`)` Optional. Configuration for deploying this deployment to Agent Registry. If present, this deployment will be published to Agent Registry.  
  
### ChannelProfile

JSON representation  
---  
      
    
    {
      "profileId": string,
      "channelType": enum ([ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelType)),
      "personaProperty": {
        object ([PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.PersonaProperty))
      },
      "webWidgetConfig": {
        object ([WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WebWidgetConfig))
      },
      "whatsappConfig": {
        object ([WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WhatsAppConfig))
      },
      "instagramConfig": {
        object ([InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.InstagramConfig))
      },
    
      // Union field _disable_dtmf can be only one of the following:
      "disableDtmf": boolean
      // End of list of possible types for union field _disable_dtmf.
    
      // Union field _disable_barge_in_control can be only one of the following:
      "disableBargeInControl": boolean
      // End of list of possible types for union field _disable_barge_in_control.
    
      // Union field _noise_suppression_level can be only one of the following:
      "noiseSuppressionLevel": string
      // End of list of possible types for union field _noise_suppression_level.
    }  
  
Fields  
---  
`profileId` |  `string` Optional. The unique identifier of the channel profile.  
`channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelType)`)` Optional. The type of the channel profile.  
`personaProperty` |  `object (`[PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.PersonaProperty)`)` Optional. The persona property of the channel profile.  
`webWidgetConfig` |  `object (`[WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WebWidgetConfig)`)` Optional. The configuration for the web widget.  
`whatsappConfig` |  `object (`[WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WhatsAppConfig)`)` Optional. Configuration specific to WhatsApp deployments.  
`instagramConfig` |  `object (`[InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.InstagramConfig)`)` Optional. Configuration specific to Instagram deployments.  
Union field `_disable_dtmf`.`_disable_dtmf` can be only one of the following:  
`disableDtmf` |  `boolean` Optional. Whether to disable DTMF (dual-tone multi-frequency).  
Union field `_disable_barge_in_control`.`_disable_barge_in_control` can be only one of the following:  
`disableBargeInControl` |  `boolean` Optional. Whether to disable user barge-in control in the conversation. - **true** : User interruptions are disabled while the agent is speaking. - **false** : The agent retains automatic control over when the user can interrupt.  
Union field `_noise_suppression_level`.`_noise_suppression_level` can be only one of the following:  
`noiseSuppressionLevel` |  `string` Optional. The noise suppression level of the channel profile. Available values are "low", "moderate", "high", "very_high".  
  
### PersonaProperty

JSON representation  
---  
      
    
    {
      "persona": enum ([Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Persona))
    }  
  
Fields  
---  
`persona` |  `enum (`[Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Persona)`)` Optional. The persona of the channel.  
  
### WebWidgetConfig

JSON representation  
---  
      
    
    {
      "modality": enum ([Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Modality)),
      "theme": enum ([Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Theme)),
      "webWidgetTitle": string,
      "securitySettings": {
        object ([SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SecuritySettings))
      }
    }  
  
Fields  
---  
`modality` |  `enum (`[Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Modality)`)` Optional. The modality of the web widget.  
`theme` |  `enum (`[Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Theme)`)` Optional. The theme of the web widget.  
`webWidgetTitle` |  `string` Optional. The title of the web widget.  
`securitySettings` |  `object (`[SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SecuritySettings)`)` Optional. The security settings of the web widget.  
  
### SecuritySettings

JSON representation  
---  
      
    
    {
      "enablePublicAccess": boolean,
      "enableOriginCheck": boolean,
      "allowedOrigins": [
        string
      ],
      "enableRecaptcha": boolean
    }  
  
Fields  
---  
`enablePublicAccess` |  `boolean` Optional. Indicates whether public access to the web widget is enabled. If `true`, the web widget will be publicly accessible. If `false`, the web widget must be integrated with your own authentication and authorization system to return valid credentials for accessing the CES agent.  
`enableOriginCheck` |  `boolean` Optional. Indicates whether origin check for the web widget is enabled. If `true`, the web widget will check the origin of the website that loads the web widget and only allow it to be loaded in the same origin or any of the allowed origins.  
`allowedOrigins[]` |  `string` Optional. The origins that are allowed to host the web widget. An origin is defined by RFC 6454. If empty, all origins are allowed. A maximum of 100 origins is allowed. Example: "https://example.com"  
`enableRecaptcha` |  `boolean` Optional. Indicates whether reCAPTCHA verification for the web widget is enabled.  
  
### WhatsAppConfig

JSON representation  
---  
      
    
    {
      "wabaId": string,
      "phoneNumberId": string,
      "phoneNumber": string,
      "displayName": string,
      "thumbnailUrl": string,
      "description": string
    }  
  
Fields  
---  
`wabaId` |  `string` Required. The WhatsApp Business Account ID.  
`phoneNumberId` |  `string` Required. The Meta phone number ID.  
`phoneNumber` |  `string` Optional. The phone number in E.164 format.  
`displayName` |  `string` Output only. The fetched Meta business page name.  
`thumbnailUrl` |  `string` Output only. The fetched Meta business profile thumbnail URL.  
`description` |  `string` Output only. The description of the Meta business page or profile.  
  
### InstagramConfig

JSON representation  
---  
      
    
    {
      "instagramAccountId": string,
      "displayName": string,
      "thumbnailUrl": string,
      "description": string
    }  
  
Fields  
---  
`instagramAccountId` |  `string` Required. The Instagram Account ID.  
`displayName` |  `string` Output only. The fetched Meta business page name.  
`thumbnailUrl` |  `string` Output only. The fetched Meta business profile thumbnail URL.  
`description` |  `string` Output only. The description of the Meta business page or profile.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### ExperimentConfig

JSON representation  
---  
      
    
    {
      "versionRelease": {
        object ([VersionRelease](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.VersionRelease))
      }
    }  
  
Fields  
---  
`versionRelease` |  `object (`[VersionRelease](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.VersionRelease)`)` Optional. Version release for the experiment.  
  
### VersionRelease

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.State)),
      "trafficAllocations": [
        {
          object ([TrafficAllocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.TrafficAllocation))
        }
      ]
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.State)`)` Optional. State of the version release.  
`trafficAllocations[]` |  `object (`[TrafficAllocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_deployments#Output.Schema.TrafficAllocation)`)` Optional. Traffic allocations for the version release.  
  
### TrafficAllocation

JSON representation  
---  
      
    
    {
      "id": string,
      "trafficPercentage": integer,
      "appVersion": string
    }  
  
Fields  
---  
`id` |  `string` Optional. Id of the traffic allocation. Free format string, up to 128 characters.  
`trafficPercentage` |  `integer` Optional. Traffic percentage of the traffic allocation. Must be between 0 and 100.  
`appVersion` |  `string` Optional. App version of the traffic allocation. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
  
### WhatsAppCredentials

JSON representation  
---  
      
    
    {
      "authCode": string,
      "pin": string,
      "phoneNumber": string,
      "businessAccountId": string,
      "wabaId": string,
      "conversationProfileId": string
    }  
  
Fields  
---  
`authCode` |  `string` Required. The Meta auth code provided by the embedded signup flow.  
`pin` |  `string` Required. The 6-digit PIN created by the user for two-step verification.  
`phoneNumber` |  `string` Required. The phone number to register with WhatsApp.  
`businessAccountId` |  `string` Required. The Business Account ID to use for the phone number.  
`wabaId` |  `string` Required. The WhatsApp Business Account ID.  
`conversationProfileId` |  `string` Optional. The Conversation Profile ID to use for the deployment.  
  
### InstagramCredentials

JSON representation  
---  
      
    
    {
      "authCode": string,
      "conversationProfileId": string
    }  
  
Fields  
---  
`authCode` |  `string` Required. The Meta auth code provided by the embedded signup flow.  
`conversationProfileId` |  `string` Optional. The Conversation Profile ID to use for the deployment.  
  
### ModelSettings

JSON representation  
---  
      
    
    {
      "model": string,
      "thinkingLevel": enum ([ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ThinkingLevel)),
    
      // Union field _temperature can be only one of the following:
      "temperature": number
      // End of list of possible types for union field _temperature.
    }  
  
Fields  
---  
`model` |  `string` Optional. The LLM model that the agent should use. If not set, the agent will inherit the model from its parent agent.  
`thinkingLevel` |  `enum (`[ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ThinkingLevel)`)` Optional. The thinking level of the model.  
Union field `_temperature`.`_temperature` can be only one of the following:  
`temperature` |  `number` Optional. If set, this temperature will be used for the LLM model. Temperature controls the randomness of the model's responses. Lower temperatures produce responses that are more predictable. Higher temperatures produce responses that are more creative.  
  
### AgentRegistryDeployment

JSON representation  
---  
      
    
    {
      "agentRegistryServiceName": string
    }  
  
Fields  
---  
`agentRegistryServiceName` |  `string` Optional. Output only. The resource name of the deployed Agent Registry service. Format: `projects/{project}/locations/{location}/services/{service}`  
  
### ChannelType

The type of the channel profile.

Enums  
---  
`UNKNOWN` | Unknown channel type.  
`WEB_UI` | Web UI channel.  
`API` | API channel.  
`TWILIO` | Twilio channel.  
`GOOGLE_TELEPHONY_PLATFORM` | Google Telephony Platform channel.  
`CONTACT_CENTER_AS_A_SERVICE` | Contact Center as a Service (CCaaS) channel.  
`CONTACT_CENTER_AS_A_SERVICE_CHAT` | Contact Center as a Service (CCaaS Chat) channel.  
`FIVE9` | Five9 channel.  
`CONTACT_CENTER_INTEGRATION` | Third party contact center integration channel.  
`WHATSAPP` | WhatsApp channel.  
`INSTAGRAM` | Instagram channel.  
  
### Persona

The persona of the channel.

Enums  
---  
`UNKNOWN` | UNKNOWN persona.  
`CONCISE` | The agent keeps the responses concise and to the point  
`CHATTY` | The agent provides additional context, explanations, and details  
  
### Modality

Modality of the web widget.

Enums  
---  
`MODALITY_UNSPECIFIED` | Unknown modality.  
`CHAT_AND_VOICE` | Widget supports both chat and voice input.  
`VOICE_ONLY` | Widget supports only voice input.  
`CHAT_ONLY` | Widget supports only chat input.  
`CHAT_VOICE_AND_VIDEO` | Widget supports chat, voice, and video input.  
  
### Theme

Theme of the web widget.

Enums  
---  
`THEME_UNSPECIFIED` | Unknown theme.  
`LIGHT` | Light theme.  
`DARK` | Dark theme.  
  
### State

State of the experiment.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`PENDING` | Deprecated: This state is no longer used.  
`RUNNING` | Running state. Experiment is running and valid.  
`DONE` | Deprecated: This state is no longer used.  
`EXPIRED` | Deprecated: This state is no longer used.  
  
### ThinkingLevel

Thinking level configuration for the model.

Enums  
---  
`THINKING_LEVEL_UNSPECIFIED` | Thinking level is unspecified.  
`DEFAULT` | Default thinking level.  
`LOW` | Low thinking level.  
`MEDIUM` | Medium thinking level.  
`HIGH` | High thinking level.  
  
### Modality

The modality of the deployment.

Enums  
---  
`MODALITY_UNSPECIFIED` | Unknown modality.  
`MODALITY_TEXT` | Text modality.  
`MODALITY_VOICE` | Voice modality.  
`MODALITY_VIDEO` | Video modality.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ✅ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
