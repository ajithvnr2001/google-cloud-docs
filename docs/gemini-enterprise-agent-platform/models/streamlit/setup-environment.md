---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/setup-environment/
title: Step 1: Set up your project and source repository \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:15.434288+00:00
---

# Step 1: Set up your project and source repository  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/setup-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Step 1: Set up your project and source repository Stay organized with collections  Save and categorize content based on your preferences. 

In this step, you set up your Google Cloud project and Python environment in Cloud Shell, enable the required APIs, and assign the Identity and Access Management (IAM) roles that you need to complete the tutorial. You also set up a GitHub repository containing the app source files by forking and cloning the [`GoogleCloudPlatform/generative-ai`](https://github.com/GoogleCloudPlatform/generative-ai) repository. After completing these steps, you verify the setup by running and testing the app locally in Cloud Shell.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Gemini Enterprise Agent Platform, Compute Engine, Artifact Registry, Identity-Aware Proxy (IAP), Cloud Run Admin, Cloud Build, Identity and Access Management (IAM) API, and Gemini for Google Cloud APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,artifactregistry.googleapis.com,iap.googleapis.com,run.googleapis.com,cloudbuild.googleapis.com,iam.googleapis.com,cloudaicompanion.googleapis.com)

  5. Make sure that you have the following role or roles on the project: Agent Platform User, Cloud Build Editor, Cloud Run Admin, Artifact Registry Admin, Compute Load Balancer Admin, Service Account User, IAP Policy Admin, OAuth Config Editor, and Service Usage Admin. 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Gemini Enterprise Agent Platform, Compute Engine, Artifact Registry, Identity-Aware Proxy (IAP), Cloud Run Admin, Cloud Build, Identity and Access Management (IAM) API, and Gemini for Google Cloud APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,artifactregistry.googleapis.com,iap.googleapis.com,run.googleapis.com,cloudbuild.googleapis.com,iam.googleapis.com,cloudaicompanion.googleapis.com)

  9. Make sure that you have the following role or roles on the project: Agent Platform User, Cloud Build Editor, Cloud Run Admin, Artifact Registry Admin, Compute Load Balancer Admin, Service Account User, IAP Policy Admin, OAuth Config Editor, and Service Usage Admin. 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 




## Set up the source repository

  1. In GitHub, fork the [GoogleCloudPlatform/generative-ai](https://github.com/GoogleCloudPlatform/generative-ai) repository. [Learn more about forking repositories in GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).

[Fork the repository in GitHub](https://github.com/GoogleCloudPlatform/generative-ai/fork)



  2. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  3. In the Cloud Shell terminal, run the following commands to clone the forked repository and set the `gemini-streamlit-cloudrun` directory as the active directory:  

         
         cd  
         git clone https://github.com/GIT_USER_NAME/FORK_NAME/  
         cd FORK_NAME/gemini/sample-apps/gemini-streamlit-cloudrun

Replace the following:

     * GIT_USER_NAME: Your GitHub username.
     * FORK_NAME: The name of the fork repository that you just created in GitHub.



## Set up the environment and dependencies

  1. In the Cloud Shell terminal, run the following commands to set up a virtual environment:
         
         python3 -m venv gemini-streamlit
         source gemini-streamlit/bin/activate
         pip install -r requirements.txt
         

  2. Run the following commands to set the environment variables needed for Agent Platform initialization:
         
         export GCP_PROJECT=$GOOGLE_CLOUD_PROJECT
         export GCP_REGION='us-central1' 
         




## Test the app locally

  1. From the Cloud Shell terminal, run the app by running the following command:
         
         streamlit run app.py \
           --browser.serverAddress=localhost \
           --server.enableCORS=false \
           --server.enableXsrfProtection=false \
           --server.port 8080
         

  2. To preview the app, in the Cloud Shell taskbar, click ![Web Preview Button](https://docs.cloud.google.com/static/shell/docs/images/web_preview.svg), and then click **Preview on port 8080**.

For more information about using the Web Preview feature, see [Preview web apps](https://docs.cloud.google.com/shell/docs/using-web-preview).




[ Previous arrow_back  Overview  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/streamlit-genai-iap)

[ Next Create a Cloud Run service  arrow_forward  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/create-cloudrun-service)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
