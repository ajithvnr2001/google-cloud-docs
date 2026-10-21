---
url: https://docs.cloud.google.com/agent-assist/docs/genesys-cloud-voice/
title: Genesys Cloud AudioHook integration \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:43:02.049600+00:00
---

# Genesys Cloud AudioHook integration  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-assist/docs/genesys-cloud-voice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Genesys Cloud AudioHook integration Stay organized with collections  Save and categorize content based on your preferences. 

This Genesys Cloud audio connector efficiently captures, processes, and analyzes real-time audio streams from your contact center interactions. It seamlessly integrates with the [Genesys Cloud Audiohook API](https://developer.genesys.cloud/devapps/audiohook/) using a persistent WebSocket connection to the Audiohook service. This connection enables real time audio streaming with gRPC to the Agent Assist integration backend. The connector provides a framework for handling incoming audio chunks, allowing for custom audio processing, transcription, or other AI-driven features like [Summarization](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections), [Proactive Generative Knowledge Assist](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/generative-knowledge-assist).

## Prerequisites

Follow these steps before you begin your Genesys Cloud voice integration:

  1. [Install the Genesys Cloud Application Server](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-app#deploy_cli).
  2. Configure both the [Genesys Cloud OAuth client](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-app#create_an_oauth_client) and the [interaction widget](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-chat#configure_the_interaction_widget).



The documentation for how to create and use the [Oauth client for Geneysys Cloud](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-app#create_an_oauth_client) provides instructions for specifying grant type, redirect, token duration, and which AI-powered features the agent uses. 

  1. Install the [Agent Assist integration backend](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-module-install).
  2. Note the following variables: 
     * VPC_CONNECTOR_NAME
     * SERVICE_REGION
     * REDIS_INSTANCE_ID
  3. [Install the AudioHook monitor at Genesys Cloud](https://help.mypurecloud.com/articles/install-audiohook-monitor-from-genesys-appfoundry/).



## Deploy the Genesys Cloud audio connector server using the Google Cloud CLI

Follow these steps to use the Google Cloud CLI to deploy the audio connector server.

  1. Clone the [GitHub repository](https://github.com/GoogleCloudPlatform/agent-assist-integrations) onto your local machine or development environment with the following code: 
         
         git clone https://github.com/GoogleCloudPlatform/agent-assist-integrations
         cd  genesyscloud/genesyscloud-audiohook 

  2. Navigate to the audio connector root directory.
  3. Create a ENV file in the root directory and update it with the following variables.

Uses the same value from the environment variable of the Agent Assist integration backend:

     * `REDIS_INSTANCE_ID`
     * `VPC_CONNECTOR_NAME`
     * `SERVICE_REGION`

Uses a value from a different source:

     * `UI_CONNECTOR`: The domain name of the deployed [Agent Assist integration backend service](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-module-install#deploy_the_ui_connector_service).
     * `GCP_PROJECT_ID`: Your project's globally unique identifier. Find it by following these [steps](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * `SERVICE_ACCOUNT`: The service account for the AudioHook connector service. If it doesn't exist, the deploy.sh script will create a new one.
     * `API_KEY`: Generate an API key in the AudioHook monitor integration. Refer to the [Add AudioHook Monitor credentials section](https://help.mypurecloud.com/articles/configure-and-activate-audiohook-monitor-in-genesys-cloud/). Leave blank for now, and update the value after configuring AudioHook.
     * `VOICE_INTERCEPTOR_SERVICE`: Choose a name for your voice connector Cloud Run service.

Example ENV file:
    
    CONVERSATION_PROFILE_NAME=projects/{your-project-id}/locations/{your-service-region}/conversationProfiles/{your-conversation-profile-id}
    SERVICE_REGION={your-service-region}
    GCP_PROJECT_ID={your-project-id}
    API_KEY={api-key-from-genesys}
    VPC_CONNECTOR_NAME={vpc-connector-name-from-aa-integration-backend}
    SERVICE_ACCOUNT={your-service-account-name}
    UI_CONNECTOR={your-agent-assist-backend-domain-name}
    REDIS_INSTANCE_ID={redis-instance-id-from-aa-integration-backend}
    VOICE_INTERCEPTOR_SERVICE={your-voice-interceptor-service-name}

  4. Run the deploy.sh script located in the `./genesyscloud/genesyscloud-audiohook` directory:
         
         sh deploy.sh




## Configure the Genesys Cloud AudioHook monitor integration

Follow these steps to configure your integration.

  1. After deploying the voice connector to Cloud Run, configure and activate the AudioHook monitor in [Genesys Cloud](https://help.mypurecloud.com/articles/configure-and-activate-audiohook-monitor-in-genesys-cloud/).
  2. In the Audiohook **Monitor Configuration** tab, update the following variables: 
     * Select **both** for the channel.
     * For the Audiohook Connection URI, use: 
           
           wss://your-cloud-run-domain.run.app/connect

  3. After setting the API key in the **Credentials** tab, update the `API_KEY` environment variable in the ENV file.
  4. Redeploy the voice connector service.
  5. Enable the AudioHook monitor inside the queue. Refer to the "Set behavior and thresholds for all interaction types" section of the Genesys Cloud [article on creating and configuring queues](https://help.mypurecloud.com/articles/create-queues/) for more details.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
