---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile/
title: ChannelProfile \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:42.531684+00:00
---

# ChannelProfile  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  ChannelProfile Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ChannelProfile.ChannelType
  * ChannelProfile.PersonaProperty
    * JSON representation
  * ChannelProfile.PersonaProperty.Persona
  * ChannelProfile.WebWidgetConfig
    * JSON representation
  * ChannelProfile.WebWidgetConfig.Modality
  * ChannelProfile.WebWidgetConfig.Theme
  * ChannelProfile.WebWidgetConfig.SecuritySettings
    * JSON representation
  * ChannelProfile.WhatsAppConfig
    * JSON representation
  * ChannelProfile.InstagramConfig
    * JSON representation



A ChannelProfile configures the agent's behavior for a specific communication channel, such as web UI or telephony.

JSON representation  
---  
      
    
    {
      "profileId": string,
      "channelType": enum ([ChannelProfile.ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.ChannelType)),
      "personaProperty": {
        object ([ChannelProfile.PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.PersonaProperty))
      },
      "webWidgetConfig": {
        object ([ChannelProfile.WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.WebWidgetConfig))
      },
      "whatsappConfig": {
        object ([ChannelProfile.WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.WhatsAppConfig))
      },
      "instagramConfig": {
        object ([ChannelProfile.InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.InstagramConfig))
      },
      "disableDtmf": boolean,
      "disableBargeInControl": boolean,
      "noiseSuppressionLevel": string
    }  
  
Fields  
---  
`profileId` |  `string` Optional. The unique identifier of the channel profile.  
`channelType` |  `enum (`[ChannelProfile.ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.ChannelType)`)` Optional. The type of the channel profile.  
`personaProperty` |  `object (`[ChannelProfile.PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.PersonaProperty)`)` Optional. The persona property of the channel profile.  
`webWidgetConfig` |  `object (`[ChannelProfile.WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.WebWidgetConfig)`)` Optional. The configuration for the web widget.  
`whatsappConfig` |  `object (`[ChannelProfile.WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.WhatsAppConfig)`)` Optional. Configuration specific to WhatsApp deployments.  
`instagramConfig` |  `object (`[ChannelProfile.InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.InstagramConfig)`)` Optional. Configuration specific to Instagram deployments.  
`disableDtmf` |  `boolean` Optional. Whether to disable DTMF (dual-tone multi-frequency).  
`disableBargeInControl` |  `boolean` Optional. Whether to disable user barge-in control in the conversation. - **true** : User interruptions are disabled while the agent is speaking. - **false** : The agent retains automatic control over when the user can interrupt.  
`noiseSuppressionLevel` |  `string` Optional. The noise suppression level of the channel profile. Available values are "low", "moderate", "high", "very_high".  
  
## ChannelProfile.ChannelType

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
  
## ChannelProfile.PersonaProperty

Represents the persona property of a channel.

JSON representation  
---  
      
    
    {
      "persona": enum ([ChannelProfile.PersonaProperty.Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.PersonaProperty.Persona))
    }  
  
Fields  
---  
`persona` |  `enum (`[ChannelProfile.PersonaProperty.Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.PersonaProperty.Persona)`)` Optional. The persona of the channel.  
  
## ChannelProfile.PersonaProperty.Persona

The persona of the channel.

Enums  
---  
`UNKNOWN` | UNKNOWN persona.  
`CONCISE` | The agent keeps the responses concise and to the point  
`CHATTY` | The agent provides additional context, explanations, and details  
  
## ChannelProfile.WebWidgetConfig

Message for configuration for the web widget.

JSON representation  
---  
      
    
    {
      "modality": enum ([ChannelProfile.WebWidgetConfig.Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.WebWidgetConfig.Modality)),
      "theme": enum ([ChannelProfile.WebWidgetConfig.Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.WebWidgetConfig.Theme)),
      "webWidgetTitle": string,
      "securitySettings": {
        object ([ChannelProfile.WebWidgetConfig.SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.WebWidgetConfig.SecuritySettings))
      }
    }  
  
Fields  
---  
`modality` |  `enum (`[ChannelProfile.WebWidgetConfig.Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.WebWidgetConfig.Modality)`)` Optional. The modality of the web widget.  
`theme` |  `enum (`[ChannelProfile.WebWidgetConfig.Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.WebWidgetConfig.Theme)`)` Optional. The theme of the web widget.  
`webWidgetTitle` |  `string` Optional. The title of the web widget.  
`securitySettings` |  `object (`[ChannelProfile.WebWidgetConfig.SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#ChannelProfile.WebWidgetConfig.SecuritySettings)`)` Optional. The security settings of the web widget.  
  
## ChannelProfile.WebWidgetConfig.Modality

Modality of the web widget.

Enums  
---  
`MODALITY_UNSPECIFIED` | Unknown modality.  
`CHAT_AND_VOICE` | Widget supports both chat and voice input.  
`VOICE_ONLY` | Widget supports only voice input.  
`CHAT_ONLY` | Widget supports only chat input.  
`CHAT_VOICE_AND_VIDEO` | Widget supports chat, voice, and video input.  
  
## ChannelProfile.WebWidgetConfig.Theme

Theme of the web widget.

Enums  
---  
`THEME_UNSPECIFIED` | Unknown theme.  
`LIGHT` | Light theme.  
`DARK` | Dark theme.  
  
## ChannelProfile.WebWidgetConfig.SecuritySettings

Security settings for the web widget.

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
  
## ChannelProfile.WhatsAppConfig

Configuration specific to WhatsApp deployments.

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
  
## ChannelProfile.InstagramConfig

Configuration specific to Instagram deployments.

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
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
