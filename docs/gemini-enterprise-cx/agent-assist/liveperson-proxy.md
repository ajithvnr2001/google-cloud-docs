---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson-proxy/
title: Deploy the proxy server \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:44:24.584960+00:00
---

# Deploy the proxy server  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson-proxy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Deploy the proxy server Stay organized with collections  Save and categorize content based on your preferences. 

This guide outlines the steps required to set up a proxy server. You will use the proxy server in conjunction with an [application server](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson-application) to simplify authentication with the Dialogflow API. For instructions on rendering the UI modules in the agent workspace, see the [main LivePerson tutorial page](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson). Both an application server and a proxy server in the same directory are required before you can render the modules in LivePerson.

Although it is possible to set up this integration deployment on any hosting platform, these instructions use Google's [Cloud Run](https://cloud.google.com/run/docs).

## Before you begin

Make sure that you have already [deployed the application server](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson-application) before you start this tutorial.

## Configuration

When you deploy the service, you must define following environment variables. Make sure to leave the `LP_CLIENT_ID` and `LP_CLIENT_SECRET` variables blank when you initially create the application server. LivePerson will provide these variables when you [create a Conversational Cloud application](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson#install_a_conversational_cloud_application), and you will update them at that time. You will also initially skip `APPLICATION_SERVER_URL` and `DF_PROXY_SERVER_URL`, setting both after the application and proxy servers have been deployed and returned the required values.

  * `LP_ACCOUNT_ID`: LivePerson account ID.
  * `LP_CLIENT_ID`: Your LivePerson client ID. This will be provided by LivePerson once the Conversational Cloud application has been installed. (Skip this variable for now, you will update it once the information has been provided).
  * `LP_CLIENT_SECRET`: Your LivePerson client secret. This will be provided by LivePerson once the Conversational Cloud application has been installed. (Skip this variable for now, you will update it once the information has been provided).
  * `LP_SENTINEL_DOMAIN`: Go to https://developers.liveperson.com/domain-api.html. Enter your account number and look up the domain for "sentinel".
  * `LP_ACCOUNT_CONFIG_READONLY_DOMAIN`: Go to https://developers.liveperson.com/domain-api.html. Enter your account number and look up the domain for "`accountConfigReadOnly`".
  * `APPLICATION_SERVER_URL`: URL of the UI application server.
  * `JWT_SECRET`: A "secret" phrase that will be used to sign the authentication tokens. You can use any phrase, although a long, random secret is most secure. Please see best practices at https://fusionauth.io/learn/expert-advice/tokens/building-a-secure-jwt/#keys.



Sample `.env` file:
    
    
        LP_ACCOUNT_ID = 12345678
        LP_CLIENT_ID = abc-123-f0f0
        LP_CLIENT_SECRET = abc123abc123abc123abc123
        LP_SENTINEL_DOMAIN = va.sentinel.liveperson.net
        LP_ACCOUNT_CONFIG_READONLY_DOMAIN = z1.acr.liveperson.net
        APPLICATION_SERVER_URL = https://my-project.wm.r.appspot.com
        JWT_SECRET = an_example_JWT_secret_phrase_please_use_something_better
    

## Deploy

The UI application server must be deployed to a Google Cloud hosting service. We recommend using either Google App Engine or Cloud Run. The steps below use Cloud Run as an example.

### Deploy using CLI

In your local terminal, change the active directory to the repository's root directory.

Run the following command to save the state of your repository into [Google Cloud Platform Container Registry](https://console.cloud.google.com/gcr/images). Replace `PROJECT-ID` with your Google Cloud Platform project ID.
    
    
        gcloud builds submit --tag gcr.io/PROJECT-ID/agent-assist-modules-proxy-server
    

Deploy your integration to live using the following command. Replace `PROJECT-ID` with your agent's Google Cloud Platform project ID, and `SERVICE-ACCOUNT-EMAIL` with your service account client email.
    
    
        gcloud run deploy --image gcr.io/PROJECT-ID/agent-assist-modules-proxy-server --service-account=SERVICE-ACCOUNT-EMAIL --memory 1Gi --platform managed
    

  * When prompted for a region, select a region (for example, `us-central1`).
  * When prompted for a service name hit enter to accept the default.
  * When prompted to allow unauthenticated invocations press `y`.



For more information, see the [Cloud Run documentation](https://docs.cloud.google.com/run/docs/deploying). You can view a list of your active integration deployments under [Cloud Run](https://console.cloud.google.com/run) in the Google Cloud Platform Console.

### Environment variables

Follow the [Cloud Run instructions](https://docs.cloud.google.com/run/docs/configuring/environment-variables) to set the necessary environment variables.

Once the service has been deployed, the CLI will output the URL that the application was deployed to (`target_url`). Go back and set the `DF_PROXY_SERVER_URL` environment variable for the **application server** using this value.

### Shut down the proxy server

To shut down the application server, you need to delete the Cloud Run service.

In your local terminal, run the following command and select the previously chosen target platform to list active deployments:
    
    
        gcloud beta run services list
    

Next, run the following command:
    
    
        gcloud beta run services delete agent-assist-modules-proxy-server
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
