---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules/
title: Implement UI modules and connectors \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:04.070501+00:00
---

# Implement UI modules and connectors  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Implement UI modules and connectors Stay organized with collections  Save and categorize content based on your preferences. 

Agent Assist provides a set of prebuilt, customizable UI component modules that you can use to integrate Agent Assist features into your UI. You can embed the modules in any web application to display Agent Assist suggestions to your agents. For specific instructions about how to integrate modules into LivePerson, see the [LivePerson tutorial](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson).

## Agent Assist features

The following are the Agent Assist features that you can implement as UI module components.

  * [Companion agent](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-companion-agent)
  * [Knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-knowledge-assist-documentation)
  * [(Proactive) Generative knowledge assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-knowledge-assist-v2-documentation)
  * [Smart reply](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-smart-reply-documentation)
  * [Conversation summarization](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-summarization-documentation)
  * [Transcript](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-transcript-documentation)



## Before you begin

Before you can implement UI modules, configure a [conversation profile](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile).

## Implement UI modules

Choose UI modules based on the Agent Assist features that you use:

Features | Example UI modules  
---|---  
[Companion agent](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-overview), conversation summarization | Companion agent, [Transcript](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-transcript-documentation)  
AI coach, (proactive) generative knowledge assist, smart reply, conversation summarization | Container V2, [Smart reply](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-smart-reply-documentation), [Transcript](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-transcript-documentation)  
  
All UI modules can be used with any agent desktop platform, but Agent Assist only provides Open Source UI module integrations for Genesys Cloud, LivePerson, Twilio, and Salesforce. To integrate UI modules with any other agent desktop platform, you must [create your own integration](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/custom-events).

The UI module connector facilitates communication between the UI components, the agent desktop, and the Agent Assist backend. All client communication takes place through dispatching [custom events](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/custom-events).

### Companion agent

The companion agent is a single component that embeds an interactive [companion agent](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/companion-agent-overview) in your agent desktop. The companion agent feature supersedes most other Agent Assist features, but its UI module includes some complementary features, such as conversation summarization. Because of this, you don't need to use the container alongside the companion agent UI module.

For more details, see the [companion agent API documentation page](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-companion-agent).

### Feature container

The container is a single component that renders your chosen non-companion agent Agent Assist features in one unified, reactive panel. Use the container if you use AI coach, (proactive) generative knowledge assist, smart reply, or conversation summarization.

For more details, see the [Container V2 API documentation page](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-container-v2).

### Individual components

You can integrate some Agent Assist features individually, alongside the companion agent or the container. If your agent desktop handles voice conversations, you'll typically add the Transcript component. We only recommend other individual components if you use a custom application where the modules must be rendered in different sections of the page, or if you require significant customization. For example, you might want to place a Smart reply module directly under the chat display.

In this case, you need to import the selected feature-specific UI module individually. Additionally, you must import and initialize the UI module connector.

## File versions

Retrieve the latest version of a gstatic file by specifying the latest version:
    
    
        <script src="https://www.gstatic.com/agent-assist-ui-modules/v1/companion_agent.js"></script>
    

Retrieve a specific stable version of a gstatic file by specifying the exact version:
    
    
        <script src="https://www.gstatic.com/agent-assist-ui-modules/v1.1/companion_agent.js"></script>
    

**Important:** Specify an exact version for any production use. When upgrading versions, always upgrade all used scripts to the latest.

Latest versions: 
    
    
          Container: v1.16 // Legacy
          Container: v2.7
          Common: v1.17
          Companion agent: v1.1
          Generative knowledge assist: v2.10
          Smart reply: v1.4
          Summarization: v1.3
          Transcript: v1.4
          Genesys Cloud: v1.1
    

## Implement the UI module connector

Unless you're using version 1 of the container, you must implement the UI module connector to use UI modules. Add the following code to your application to expose a global `UiModulesConnector` class that can then be instantiated and initialized:
    
    
        <script src="https://www.gstatic.com/agent-assist-ui-modules/v1/common.js"></script>
    

Methods:
    
    
        constructor(): void;
        init(config: ConnectorConfig): void;
        disconnect(): void;
        setAuthToken(token: string): void;
    

The following outlines the TypeScript interface for the connector configuration object. If you have created a [custom UI module connector](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/custom-events#custom_ui_module_connectors) to use with an unsupported system, set `agentDesktop` to `Custom`. The following example provides a list of supported agent desktop systems.
    
    
    interface ConnectorConfig {
      /** Communication mode for the UI modules application. */
      channel: 'chat' | 'voice';
    
      /** Agent desktop to use. */
      agentDesktop: 'LivePerson' | 'GenesysCloud' | 'SalesForce' | 'GenesysEngageWwe' | 'Custom';
    
      /** Optional desktop source for metric tracking. */
      agentDesktopSource?: string;
    
      /** Conversation profile name to use. */
      conversationProfileName: string;
    
      /** API Connector config. */
      apiConfig: {
        /**
         * Authentication token to attach to outgoing requests. Should be a valid
         * OAuth token for Dialogflow API, or any other token for custom API
         * endpoints.
         */
        authToken: string;
    
        /**
         * Specifies a custom proxy server to call instead of calling the Dialogflow
         * API directly.
         */
        customApiEndpoint?: string;
    
        /** API key to use. */
        apiKey?: string;
    
        /**
         * Additional HTTP headers to include in the Dialogflow/proxy server API
         * request.
         */
        headers?: Array;
      }
    
      /** Event-based connector config. Required for voice/omnichannel conversations and some features of chat conversations. */
      eventBasedConfig?: {
        /** Transport protocol to use for updates. Defaults to 'websocket'. */
        transport?: string;
    
        /** Event-based library to use. */
        library?: 'SocketIo';
    
        /** Endpoint to which the connection will be established. */
        notifierServerEndpoint: string;
    
        /** Additional Socket.io connect options. */
        socketIoConnectOpts?: any;
    
        /** Options to retry initial Socket.io connection in case of failure. */
        backOffOpts?: {
          initialDelay: number;
          maxDelay: number;
          maxAttempts: number;
          connectionTimeout: number;
        };
      }
    
    }
    

Example instantiation:
    
    
    const connector = new UiModulesConnector();
    
    connector.init({
      channel: 'chat',
      agentDesktop: 'Custom',
      conversationProfileName: 'projects/my-project/locations/global/conversationProfiles/123',
      apiConfig: {
        authToken: 'abc123',
        customApiEndpoint: 'https://my-dialogflow-proxy-server.com',
      },
      eventBasedConfig: {
        notifierServerEndpoint: 'https://my-notifier-server-endpoint.com',
        transport: 'websocket',
        library: 'SocketIo',
      }
    });
    

## Price disclaimer

If you use UI modules, there is a cost associated with the underlying services, including the following:

  * [Pub/Sub](https://cloud.google.com/pubsub/pricing)
  * [Memorystore for Redis](https://cloud.google.com/memorystore/docs/redis/pricing)
  * [Cloud Run](https://cloud.google.com/run/pricing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
