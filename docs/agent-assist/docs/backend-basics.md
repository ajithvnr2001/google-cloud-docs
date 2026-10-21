---
url: https://docs.cloud.google.com/agent-assist/docs/backend-basics/
title: Agent Assist backend modules basics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:22:17.804946+00:00
---

# Agent Assist backend modules basics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/backend-basics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Agent Assist backend modules basics Stay organized with collections  Save and categorize content based on your preferences. 

Agent Assist now offers **backend modules** , an out-of-the-box option for integrating Agent Assist into your system. Backend modules includes a Cloud Pub/Sub interceptor service and a UI connector service. The interceptor processes feature-related event notifications from Dialogflow using Cloud Pub/Sub topics and then the UI connector pushes them to the agent desktop UI. UI connectors also support feedback signals from the agent desktop and sends them to Dialogflow.

**Note:** You can check the [GitHub repository](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/b00b1c1438d655d0cb37848382f3ac7039433bfb/aa-integration-backend) for the latest instruction.

## Backend modules structure

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/agent-assist/images/backend-module.png)

## Backend module components

Backend modules require the following Google products to integrate Agent Assist into your system:

  * Cloud Pub/Sub
  * Cloud Pub/Sub interceptor
  * Memorystore for Redis
  * UI connector



### Cloud Pub/Sub

Cloud Pub/Sub topics are configured in [conversation profiles](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/conversation-profile). Agent Assist will then publish suggestions, new messages, new recognition-result notifications, and conversation lifecycle-related events to the topic. Suggestions are in the form of [`HumanAgentAssistantEvent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/HumanAgentAssistantEvent), and both new messages and conversation lifecycle events in the form of [`ConversationEvent`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/ConversationEvent). For each conversation profile, these four kinds of event messages are published to different topics. For example, a conversation lifecycle event message might be `{"conversation":"projects/your-project-id/locations/global/conversations/your-conversation-id","type":"CONVERSATION_STARTED"}`, which indicates the start of a conversation.

### Cloud Pub/Sub interceptor

The Cloud Pub/Sub interceptor is deployed on [Cloud Run](https://cloud.google.com/run/docs). The functionality of each container instance (server) of this Cloud Run service is identical to each other instance, including:

  * Processing event messages posted by Cloud Pub/Sub topics using HTTP requests.
  * Publishing messages received to Redis Pub/Sub channels, specific to the conversation name and the UI connector server ID. The channel format is `{connector_id}:{conversation_name}`.



### Redis

Redis uses [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview) to do the following:

  * Record the UI connector server ID information for each conversation in mapping `<conversation_name, connector_id>`.
  * Forward event notifications published by Cloud Pub/Sub interceptor to the corresponding UI connector server using the Redis Pub/Sub mechanism.



### UI connector

UI connector is an application that exposes a RESTful Dialogflow API proxy and a SocketIO WebSocket endpoint to stream Dialogflow messages originating from Agent Assist. UI connector is deployed on [Cloud Run](https://docs.cloud.google.com/run/docs). Because WebSocket connections are stateful, the agent desktop will stay connected to the same container on Cloud Run throughout the lifespan of the connection. Therefore, every UI connector server handles different conversations and subscribes to distinct Redis Pub/Sub channels (`{connector_id}:*`) for the conversations they handle. Tasks for each UI connector server:

  * Supports a customized authentication method for agent desktops.
  * Generates temporary JWT after authenticating agent desktops' customized tokens. When they send requests to the Dialogflow API or WebSocket connection, UI connectors validate the attached JWT instead of checking the original agent token.
  * Establishes a SocketIO WebSocket connection with the authenticated agent desktop based on a given conversation name.
  * Subscribes event messages to Redis Pub/Sub channels for the conversations it handles.
  * Pushes Agent Assist events to the desktop UI as they are received.



### Secret Manager

The UI connector needs a JWT secret key to generate temporary JWTs for authenticated agent desktops. This secret key is stored in the [Secret Manager](https://cloud.google.com/secret-manager).

## Directory

The following is an outline of directory structure in the code repository. Contact your Google representative for permissions if you are not able to access the repository.
    
    
    .
    ├── cloud-pubsub-interceptor
    │   ├── Dockerfile: Docker-image creation for Cloud Pub/Sub Interceptor deployment on Cloud Run
    │   ├── main.py: A starter for flask app
    │   ├── requirements.txt: Python packages for running Cloud Pub/Sub Interceptor service
    │   └── unit_test.py: Unit test code for Cloud Pub/Sub Interceptor
    ├── cloudbuild.yaml: An example configuration file for Cloud Build
    ├── deploy.sh: An automated deployment script
    ├── images
    ├── readme.md
    └── ui-connector
        ├── Dockerfile: Builds Docker image for UI Connector deployment on Cloud Run
        ├── auth.py: JWT validation and registration handling
        ├── auth_options.py: Support for authentication through different identity providers
        ├── config.py: Configuration for variables about authentication, logging, and CORS origins
        ├── dialogflow.py: With Dialogflow utilities for runtime-conversation handling
        ├── main.py: A starter for flask app
        ├── requirements.txt: Python packages for running UI Connector
        ├── templates
        │   └── index.html: A simple interactive demo
        └── unit_test.py: Unit test code for UI Connector
    

## Pricing and quotas

Agent Assist integrations include the following services, which have their own applicable pricing and quota limits.

  * Agent Assist [prices](https://cloud.google.com/agent-assist/pricing) and [quotas](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/quotas)
  * Pub/Sub [prices](https://cloud.google.com/pubsub/pricing) and [quotas](https://docs.cloud.google.com/pubsub/quotas)
  * Memorystore [prices](https://cloud.google.com/memorystore/docs/redis/pricing) and [quotas](https://docs.cloud.google.com/memorystore/docs/redis/quotas)
  * Cloud Run [prices](https://cloud.google.com/run/pricing) and [quotas](https://docs.cloud.google.com/run/quotas)



## What's next

See the [backend modules installation guide](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-module-install) for more information about getting started with this integration method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
