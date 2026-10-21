---
url: https://docs.cloud.google.com/agent-assist/docs/ui-modules-container-documentation/
title: Container V1 \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:57:09.050955+00:00
---

# Container V1  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/ui-modules-container-documentation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Container V1 Stay organized with collections  Save and categorize content based on your preferences. 

This page contains the API documentation for the container method of implementing UI modules. The following are the Agent Assist features that you can implement as components within your container.

  * [Knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-knowledge-assist-documentation), Keys: `'FAQ'` and `'ARTICLE_SUGGESTION'`
  * [Generative knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-knowledge-assist-v2-documentation), Key: `'KNOWLEDGE_ASSIST_V2'`
  * [Smart Reply](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-smart-reply-documentation), Key: `'SMART_REPLY'`
  * [Conversation Summarization](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-summarization-documentation), Key: `'CONVERSATION_SUMMARIZATION'`



## Attributes

Property name | Type | Comment  
---|---|---  
features | string | Comma-separated list of Agent Assist suggestion feature keys to render. Example: "SMART_REPLY, CONVERSATION_SUMMARIZATION"  
api-headers | string | Additional headers to include in Dialogflow API calls. Example: "Content-Type:application/json, Accept:application/json"  
conversation-profile | string | Name of the conversation profile to use.  
agent-desktop | AgentDesktop | Agent desktop software to integrate with.  
auth-token | string | Authentication token to use for API calls.  
api-key | string | Optional API key to use for API calls.  
channel | CommunicationChannel | Communication channel used for this application (chat, voice, or omnichannel).  
custom-api-endpoint | string | Optional custom API endpoint to use (if UI modules are configured with a proxy server).  
theme | 'dark' | 'light' | Color theme to use.  
show-header | BooleanString | Whether to show the Agent Assist suggestions header.  
dark-mode-background | string | Background color to use for dark mode. If none is specified, defaults are provided for the primary supported agent desktops.  
notifier-server-endpoint | string | Notifier server endpoint to use for event-based conversations.  
event-based-transport | EventBasedTransport | Transport protocol to use for event-based conversations.  
event-based-library | EventBasedLibrary | Library to use for event-based conversations.  
oauth-client-id | string | Optional OAuth Client ID for implicit authentication, used in some agent desktop configurations (Genesys Cloud).  
redirect-uri | string | Optional redirect URI to navigate to after authentication, used in some agent desktop configurations (Genesys Cloud).  
genesys-cloud-region | string | Optional region for Genesys Cloud, defaults to mypurecloud.com.  
  
### Usage

Attributes are string-based component properties which can be set in the following ways:

### HTML

`js <element-selector property-name="value">`

### JavaScript

`js var el = document.querySelector('element-selector'); el.setAttribute('property-name', 'value');`

## Inputs

Property name | Type | Comment  
---|---|---  
socketIoConnectOpts | SocketIoConnectOpts | Additional Socket.io connect options.  
config | UiModuleContainerConfig | Configuration object to define module-specific configurations.  
  
### Usage

Inputs are typically JavaScript objects or other complex property types which must be assigned on the element instance directly:
    
    
    const el = document.querySelector('element-selector');
    el.propertyName = value;
    

## Types

See the following section for the custom types used by the component.

### AgentDesktop
    
    
    "LivePerson" | "GenesysCloud" | "SalesForce" | "Custom"
    

### CommunicationChannel
    
    
    "chat" | "voice" | "omnichannel"
    

### BooleanString
    
    
    "true" | "false"
    

### EventBasedTransport
    
    
    "websocket" | "polling"
    

### EventBasedLibrary
    
    
    "SocketIo"
    

### SocketIoConnectOpts
    
    
    interface SocketIoConnectOpts extends SocketIOClient.ConnectOpts {
      auth: {
        token: string;
      };
      withCredentials?: boolean;
    }
    

### UiModuleContainerConfig
    
    
    interface UiModuleContainerConfig {
      knowledgeAssistConfig?: {
        articleLinkConfig: {
          /**
           * Whether to open the article in a new tab or as a dialog. Defaults to new
           * tab.
           */
          target?: "blank" | "popup";
          /**
           * Options to configure the popup's size and location. See
           * https://developer.mozilla.org/en-US/docs/Web/API/Window/open#window_features.
           */
          popupWindowOptions?: string;
          /**
           * The field name on the document metadata if a separate article link source
           * is provided.
           */
          linkMetadataKey?: string;
        };
      };
      knowledgeAssistV2Config?: {
        articleLinkConfig?: {
          /**
           * Whether to open the article in a new tab or as a dialog. Defaults to new
           * tab.
           */
          target?: "blank" | "popup";
          /**
           * Options to configure the popup's size and location. See
           * https://developer.mozilla.org/en-US/docs/Web/API/Window/open#window_features.
           */
          popupWindowOptions?: string;
          /**
           * The field name on the document metadata if a separate article link source
           * is provided.
           */
          linkMetadataKey?: string;
        };
        showCopyAnswer: boolean;
        showPasteAnswer: boolean;
      };
      summarizationConfig?: {
        /**
         * Optional callback that can be used to save the generated summary to an
         * external source.
         */
        onSaveSummary?: (
          summary: {
            summary: string;
            conversationDetails: ConversationDetails;
          },
          saveCallbacks: {
            setLoading: () => void;
            setSuccess: (message: string) => void;
            setError: (message: string) => void;
          }
        ) => void;
    
        /** Whether to show the 'Generate summary' button. */
        showGenerateSummaryButton?: "true" | "false";
      };
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
