---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-app/
title: Deploy the Genesys Cloud application server \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:56.484962+00:00
---

# Deploy the Genesys Cloud application server  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Deploy the Genesys Cloud application server Stay organized with collections  Save and categorize content based on your preferences. 

You can set up an application server for rendering Agent Assist suggestions on the web in [Genesys Cloud](https://www.genesys.com/genesys-cloud). 

## Objectives

Genesys Cloud integration involves the following processes:

  1. Deploy [the backend server](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-module-install) for the UI module to call the Dialogflow API, register an authentication token, and setup cloud Pub/Sub and Memorystore for Redis.
  2. Deploy the Genesys Cloud application server for rendering the Agent Assist UI module in [Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run).
  3. Create [OAuth client](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-app#create_an_oauth_client).
  4. Complete the [environment variables](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-app#complete_the_environment_variables).
  5. Set up the [interaction widget](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-chat#configure_the_interaction_widget) in Genesys Cloud.
  6. Configure the Agent Assist integration with the interaction widget in Genesys Cloud.
  7. [Configure Messenger](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-chat#configure_the_messenger) in Genesys Cloud.
  8. Use the Genesys Cloud [web chat and messaging tools](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-testing) to test the integration.



## Before you begin

You must complete the following actions before starting the Genesys Cloud integration:

  1. Install the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install), if you haven't already configured it.
  2. Follow the Google Cloud instructions to [create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create) and [assign the Dialogflow API client role](https://docs.cloud.google.com/dialogflow/es/docs/access-control#roles).
  3. Deploy an Agent Assist UI modules [backend](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/backend-module-install). When you deploy the backend server, specify the environment variable `AUTH_OPTION` to be `GenesysCloud`, following the [deployment instructions](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/HEAD/aa-integration-backend#customize-user-authentication-method).



## Deploy Genesys Cloud application server using CLI

  1. Clone the [git repository](https://github.com/GoogleCloudPlatform/agent-assist-integrations) onto your local machine or development environment with the following code: 
         
         git clone https://github.com/GoogleCloudPlatform/agent-assist-integrations
         

  2. In your local terminal, use the following code to change the active directory to the repository root directory where the Docker file resides before running the Google Cloud CLI builds. 
         
         cd genesyscloud/frontend
         

  3. When prompted for a service name, press **Enter** to accept the default.
  4. Deploy the integration using the following command. Replace `PROJECT-ID` with your agent's Google Cloud project ID, `UI_MODULE_SERVICE_ACCOUNT` with your service account client email, and [set the `REGION` for Cloud Run](https://docs.cloud.google.com/run/docs/locations). 
         
         gcloud run deploy $AA_MODULE_APPLICATION_SERVER   
         
         --source ./   
         
         --service-account=$ui_module_service_account   
         
         --memory 1Gi --platform managed   
         
         --region us-central1   
         
         --allow-unauthenticated   
         

  5. Click **Enter** to accept the default service name.



For details, see [Cloud Run documentation](https://docs.cloud.google.com/run/docs/deploying). In the Google Cloud console, you can view a list of your active integration deployments under [Cloud Run](https://console.cloud.google.com/).

### Create an OAuth client

  1. Follow the [instructions](https://developer.genesys.cloud/authorization/platform-auth/use-pkce) in the Genesys Cloud documentation to create a new OAuth client.
  2. Ensure the grant type is **Code Authorization / PKCE**.
  3. Add your application URL to the **Authorized redirect URIs** section.
  4. Update the **OAuth 2.0** client token duration to **3600 seconds**. This matches the [default 1-hour JWT token duration](https://github.com/GoogleCloudPlatform/agent-assist-integrations/blob/HEAD/aa-integration-backend/ui-connector/config.py) for Dialogflow API access. If you require a customized duration, update both the OAuth and JWT token durations accordingly. 
         
         {Application_SERVER_URL}?conversationProfile={CONVERSATION_PROFILE_NAME}&features={FEATURES}
         

Replace {APPLICATION_SERVER_URL} with the URL of your UI application server.
  5. Replace `CONVERSATION_PROFILE_NAME` with the name of the [conversation profile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles), such as `projects/your-project/locations/your-location/conversationProfiles/abc123`.
  6. Replace `{FEATURES}` with a comma-separated list of Agent Assist features you would like the application to include. Important: Only include features configured in your conversation profile. Genesys cloud supports the following [features](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-container-documentation)
  7. To add scopes to the OAuth client, navigate to the **Scopes** section.
  8. Select the following scopes: `alerting`, `authorization`, `conversations`, `notifications`, `messaging`, and `organization`.



Example URL: 
    
    
    https://my-project.wm.run.app?conversationProfile=projects/my-project/conversationProfiles/abc123&features=CONVERSATION_SUMMARIZATION,AGENT_COACHING,PROACTIVE_GENERATIVE_KNOWLEDGE_ASSIST

We recommend [enabling pop-out authentication for embedded iframes](https://help.genesys.cloud/articles/enable-pop-out-authentication-for-embedded-iframes/) to ensure a seamless login experience.

### Complete the environment variables

The Genesys Cloud application uses the following environment variables. To set the environment variables, follow the [Cloud Run instructions](https://docs.cloud.google.com/run/docs/configuring/environment-variables).

  * `OAUTH_CLIENT_ID`: Genesys Cloud OAuth Client ID.
  * `GENESYS_CLOUD_REGION`: [Genesys Cloud region](https://developer.genesys.cloud/platform/api/). For example, `usw2.pure.cloud` for US West(Oregon). The default value is [`mypurecloud.com`](http://mypurecloud.com).
  * `GENESYS_CLOUD_ENVIRONMENT`: Genesys cloud environment. The default value is `prod`.
  * `PROXY_SERVER`: The URL of the Agent Assist backend connector.
  * `APPLICATION_SERVER_URL`: URL of the UI application server.
  * `PROJECT_ID`: Your Google Cloud project ID.
  * `CONVERSATION_PROFILE`: The [conversation profile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles) to use. This should match the profile in the redirect URL of the OAuth client.
  * `FEATURES`: Comma-separated constant for [Agent Assist features](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/ui-modules-container-documentation). This should match the features in the redirect URL of the OAuth client.
  * `CHANNEL`: Choose integration type, the value could be "voice" or "chat".



Sample .env file: 
    
    
    OAUTH_CLIENT_ID={your-oauth-client-id}
    GENESYS_CLOUD_REGION={your-pure-cloud-region}
    GENESYS_CLOUD_ENVIRONMENT={your-pure-cloud-environment}
    PROXY_SERVER={your-proxy-server-endpoint}
    PROJECT_ID={your-gcp-project-id}
    CONVERSATION_PROFILE={your-conversation-profile}
    FEATURES=ARTICLE_SUGGESTION,CONVERSATION_SUMMARIZATION
    CHANNEL={use-voice-or-chat}

When you create an OAuth client, Genesys Cloud also provides a client ID.

Run the deployment command with updated environment variables. 
    
    
        gcloud run deploy $AA_MODULE_APPLICATION_SERVER   
    
        --source ./   
    
        --service-account=$ui_module_service_account   
    
        --memory 1Gi --platform managed   
    
        --region us-central1   
    
        --allow-unauthenticated   
    
        --set-env-vars ^~^OAUTH_CLIENT_ID=$OAUTH_CLIENT_ID~GENESYS_CLOUD_REGION=$GENESYS_CLOUD_REGION~GENESYS_CLOUD_ENVIRONMENT=$GENESYS_CLOUD_ENVIRONMENT~CONVERSATION_PROFILE=$CONVERSATION_PROFILE~FEATURES=$FEATURES~PROJECT_ID=$PROJECT_ID~APPLICATION_SERVER_URL=''~PROXY_SERVER=$PROXY_SERVER~APPLICATION_SERVER_URL=$APPLICATION_SERVER_URL

The Genesys Cloud application server must be deployed to a Google Cloud hosting service. Use App Engine or Cloud Run.

### Shut down the application server

  1. Delete the Cloud Run service.
  2. In your local terminal, run the following command: 
         
         gcloud run services list
         

  3. Select the previously chosen target platform to list active deployments.
  4. Run the following command: 
         
         gcloud run services delete agent-assist-modules-application-server
         




## Price disclaimer

If you use Genesys Cloud integration, there is a cost associated with the underlying [Cloud Run](https://cloud.google.com/run/pricing) service.

## What's next

  * [Configure for chat integration](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-chat)
  * [Test chat integration](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/genesys-cloud-testing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
