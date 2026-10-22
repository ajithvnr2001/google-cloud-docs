---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/create-cloudrun-service/
title: Step 2: Create a Cloud Run service \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:45:19.201277+00:00
---

# Step 2: Create a Cloud Run service  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/create-cloudrun-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Step 2: Create a Cloud Run service Stay organized with collections  Save and categorize content based on your preferences. 

In this step, you create a Cloud Run service to deploy the app from the repository that you forked in the previous step. You also set up an automatic Cloud Build trigger, so that the app is built and deployed to Google Cloud whenever you push a new commit to the repository.

## Create a Cloud Run service with continuous build

  1. In the Google Cloud console, navigate to Cloud Run.

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Click **Create service**.

  3. Select **Continuously deploy from a repository**.

  4. Click **Set up with Cloud Build**.

  5. In the **Repository** list, select the forked GitHub repository that you created for your app.

If your repository isn't listed, click **Manage connected repositories**. While completing this step, do the following, if prompted:

     * Authenticate to GitHub.

     * Install Cloud Build on your GitHub account.

  6. If you're selecting a repository for the first time for use with Cloud Build in your project, select the checkbox to agree to the terms of use policy.

  7. Click **Next**.

  8. In the **Build configuration** section, enter the following details:

     * **Branch** : The default branch is `^main$`. Don't update this.

     * **Build type** : Click **Dockerfile**.

     * **Source location** : Enter the following:
           
           /gemini/sample-apps/gemini-streamlit-cloudrun/Dockerfile
           

  9. Click **Save**.

  10. On the **Create service** page, enter the following details in the **Configure** section:

     * **Service name** : Enter `gemini-streamlit-cloudrun`.

     * **Authentication** : Click **Allow public access**.

     * **Service autoscaling** : Set the **Minimum number of instances** to `1`.

  11. Click **Container(s), volumes, networking, security**.

  12. In the **Revision autoscaling** section, enter the following:

     * **Minimum number of instances** : Enter `1`.

     * **Maximum number of instances** : Enter `3`.

  13. Click **Create**.

  14. Optional: To test the app deployment to Cloud Run, do the following:  


     1. On the **Services** page in Cloud Run, click the service name.

[Go to the Services page](https://console.cloud.google.com/run)

     2. On the **Service details** page, click the **URL** displayed next to the service name.




## Set up an automatic Cloud Build trigger

  1. Navigate to the **Triggers** page in Cloud Build.

[Go to the Triggers page](https://console.cloud.google.com/cloud-build/triggers)

  2. Click the name of your new trigger.

  3. Under **Source** , click to expand **Show included and ignored files filters**.

  4. In the **Included files filter** box, enter `gemini-streamlit-cloudrun/**`.

  5. Click **Save**.

**Tip:** If you want to manually build the Cloud Run service again, go to the **Triggers** page and click **Run**.



[ Previous arrow_back  Set up your project and source repository  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/setup-environment)

[ Next Create a load balancer  arrow_forward  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/create-loadbalancer)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
