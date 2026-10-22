---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson-application/
title: Deploy the application server \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:53.102064+00:00
---

# Deploy the application server  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Deploy the application server Stay organized with collections  Save and categorize content based on your preferences. 

This guide outlines the steps required to set up an application server that you can use to render Agent Assist suggestions in LivePerson. The application server is used with a [proxy server](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson-proxy) in the same directory. For instructions on rendering the UI modules in the agent workspace, see the [main LivePerson tutorial page](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/liveperson). Both an application server and a proxy server are required before you can render the modules in LivePerson.

Although it is possible to set up this integration deployment on any hosting platform, these instructions use Google's [Cloud Run](https://cloud.google.com/run/docs).

## Configuration

When you deploy the service, you must define following environment variables. Make sure to leave the `LP_CLIENT_ID` and `LP_CLIENT_SECRET` variables blank when you initially create the application server. LivePerson will provide these variables when you [create a Conversational Cloud application](https://docs.cloud.google.com/agent-assist), and you will update them at that time. You will also initially skip `APPLICATION_SERVER_URL` and `DF_PROXY_SERVER_URL`. Each of these two variables will be set after the application and proxy servers have been deployed and returned the required URL values.

  * `LP_ACCOUNT_ID`: LivePerson account ID.
  * `LP_CLIENT_ID`: Your LivePerson client ID. This will be provided by LivePerson once the Conversational Cloud application has been installed. (Skip this variable for now, you will update it once the information has been provided).
  * `LP_CLIENT_SECRET`: Your LivePerson client secret. This will be provided by LivePerson once the Conversational Cloud application has been installed. (Skip this variable for now, you will update it once the information has been provided).
  * `LP_SENTINEL_DOMAIN`: Go to <https://developers.liveperson.com/domain-api.html>. Enter your account number and look up the domain for "sentinel".
  * `LP_ACCOUNT_CONFIG_READONLY_DOMAIN`: Go to <https://developers.liveperson.com/domain-api.html>. Enter your account number and look up the domain for "`accountConfigReadOnly`".
  * `APPLICATION_SERVER_URL`: URL of the UI application server. (Skip for now, and update after the application server has been deployed and you know its URL).
  * `DF_PROXY_SERVER_URL`: The URL of the proxy server. (Skip for now, and update after the proxy server has been deployed and you know its URL.)
  * `PROJECT_ID`: Your Google Cloud project ID. Do not include the `projects/` prefix.



Sample `.env` file:
    
    
        LP_ACCOUNT_ID = 12345678
        LP_CLIENT_ID = abc-123-f0f0
        LP_SENTINEL_DOMAIN = va.sentinel.liveperson.net
        LP_ACCOUNT_CONFIG_READONLY_DOMAIN = z1.acr.liveperson.net
        LP_CLIENT_SECRET = abc123abc123abc123abc123
        APPLICATION_SERVER_URL = https://my-project.wm.r.appspot.com
        DF_PROXY_SERVER_URL = https://proxy-server-dot-my-project.wm.r.appspot.com
        PROJECT_ID = my-project
    

## Deploy

The UI application server must be deployed to a Google Cloud hosting service. We recommend using either [Google App Engine](https://cloud.google.com/appengine/docs) or Cloud Run. The steps below use Cloud Run as an example.

### Set up a gcloud CLI

The deployment processes outlined in this tutorial utilize gcloud CLI commands. Follow the steps below to set up the gcloud CLI locally for this deployment:

  1. On the [gcloud CLI documentation page](https://docs.cloud.google.com/sdk/docs/quickstarts), select your OS and follow the instructions for the installation.
  2. Run `gcloud config get-value project` to check the Google Cloud Platform project configuration.
  3. Go into your Dialogflow agent's settings and check the Project ID associated with the agent. The Google Cloud Platform project configured in the gcloud CLI should match the agent's Project ID.
  4. If the project IDs do not match, run `gcloud config set project PROJECT-ID`, replacing `PROJECT-ID` with the Project ID from step 3.



### Set up a service account

You must create a Service Account in your Google Cloud Platform project in order for the integration to function properly. For more details, see the [Dialogflow documentation](https://docs.cloud.google.com/dialogflow/es/docs/quick/setup#sa-create).

Follow these steps to create a service account and set up the integration:

  1. Select the Google Cloud Platform project associated with your Agent Assist resources.
  2. Click on the navigation menu in the Google Cloud Platform console, hover over **IAM & admin**, and click **Service accounts**.
  3. Click on **\+ CREATE SERVICE ACCOUNT** , fill in the details, and assign it the **Dialogflow Client API** role.



### Enable required APIs

  1. Navigate to your desired Google Cloud Platform project.
  2. Click on the navigation menu in the Google Cloud Platform console and select **Billing**. Make sure that billing is enabled for your project.
  3. [Enable Cloud Build and the Cloud Run API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,run.googleapis.com) for this project.
  4. Clone the following git repository onto your local machine or development environment: `git clone [repository url]`.
  5. Open the root directory of the repository on your local machine or development environment.



### Deploy using CLI

In your local terminal, change the active directory to the repository's root directory.

Run the following command to save the state of your repository into [Google Cloud Platform Container Registry](https://console.cloud.google.com/gcr/images). Replace `PROJECT-ID` with your Google Cloud Platform project ID.
    
    
        gcloud builds submit --tag gcr.io/PROJECT-ID/agent-assist-modules-application-server
    

Deploy your integration to live using the following command. Replace `PROJECT-ID` with your agent's Google Cloud Platform project ID, and `SERVICE-ACCOUNT-EMAIL` with your service account client email.
    
    
        gcloud run deploy --image gcr.io/PROJECT-ID/agent-assist-modules-application-server --service-account=SERVICE-ACCOUNT-EMAIL --memory 1Gi --platform managed
    

  * When prompted for a region, select a region (for example, `us-central1`).
  * When prompted for a service name hit enter to accept the default.
  * When prompted to allow unauthenticated invocations press `y`.



For more information, see the [Cloud Run documentation](https://docs.cloud.google.com/run/docs/deploying). You can view a list of your active integration deployments under [Cloud Run](https://console.cloud.google.com/run) in the Google Cloud Platform Console.

### Environment variables

Follow the [Cloud Run instructions](https://docs.cloud.google.com/run/docs/configuring/environment-variables) to set the necessary environment variables.

Once the service has been deployed, the CLI will output the URL that the application was deployed to (`target_url`). Go back and set the `APPLICATION_SERVER_URL` environment variable using this value.

### Shut down the application server

To shut down the application server, you need to delete the Cloud Run service.

In your local terminal, run the following command and select the previously chosen target platform to list active deployments:
    
    
        gcloud beta run services list
    

Next, run the following command:
    
    
       gcloud beta run services delete agent-assist-modules-application-server
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
