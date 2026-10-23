---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api/get-started-websocket/
title: Get started with Gemini Live API using WebSockets \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:14.440456+00:00
---

# Get started with Gemini Live API using WebSockets  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api/get-started-websocket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Get started with Gemini Live API using WebSockets Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to connect to Gemini Live API by using WebSockets. In this tutorial, you build a real-time multimodal application with a vanilla JavaScript frontend and a Python server handling the authentication and proxying.

## Before you begin

Complete the following steps to set up your environment.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Gemini Enterprise Agent Platform API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. [Install Git](https://git-scm.com/downloads).
  15. [Install Python 3](https://www.python.org/downloads/).



## Clone the demo app

Clone the demo app repository and navigate to that directory:
    
    
    git clone https://github.com/GoogleCloudPlatform/generative-ai.git &&
    cd generative-ai/gemini/multimodal-live-api/native-audio-websocket-demo-apps/plain-js-demo-app
    

### Project structure

The application includes the following files:
    
    
    /
    ├── server.py            # WebSocket proxy + HTTP server
    ├── requirements.txt     # Python dependencies
    └── frontend/
        ├── index.html       # UI
        ├── geminilive.js    # Gemini API client
        ├── mediaUtils.js    # Audio/video streaming
        ├── tools.js         # Custom tool definitions
        └── script.js        # App logic
    

## Run the backend server

The backend (`server.py`) handles the authentication and acts as a WebSocket proxy between the client and Gemini Live API.

To run the backend server, run the following commands:

  1. Install dependencies:
         
         pip3 install -r requirements.txt
         

  2. Authenticate with Google Cloud:
         
         gcloud auth application-default login
         

  3. Start the server:
         
         python3 server.py
         




## Open the frontend UI and connect with Gemini

The frontend manages audio and video capture and playback. The `geminilive.js` file handles the WebSocket connection to the backend.
    
    
    const client = new GeminiLiveAPI(proxyUrl, projectId, model);
    client.addFunction(toolInstance); // Add custom tools
    client.connect(accessToken); // Connect (token optional with proxy)
    

To open the frontend UI and connect with Gemini, do the following:

  1. Open your browser and navigate to <http://localhost:8000>.
  2. In the **Project ID** field, enter the ID of your Google Cloud project.
  3. Click **Connect**.



## Interact with Gemini

Try to do the following:

  * **Text input** : You can write a text message to Gemini by entering your message in the message field and clicking **Send**. Gemini responds to the message using audio.
  * **Voice input** : To speak to Gemini, click **Start mic**. Gemini responds to the prompt using audio.
  * **Video input** : To let Gemini see through your camera, click **Start camera**. You can talk to Gemini about what it sees through your camera.



## What's next

  * Learn how to [configure language and voice](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api/configure-language-voice).
  * Learn how to [configure Gemini capabilities](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api/configure-gemini-capabilities).
  * Learn about [Gemini Live API best practices](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api/best-practices).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
