---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/clean-up/
title: Step 6: Clean up your project \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:23:52.102644+00:00
---

# Step 6: Clean up your project  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/clean-up/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Step 6: Clean up your project Stay organized with collections  Save and categorize content based on your preferences. 

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either [delete the project containing the resources](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects), or keep the project and delete the individual resources.

This section describes how to delete the Google Cloud resources and the Git repository.

## Delete the Cloud Run service

  1. In the Google Cloud console, navigate to Cloud Run.

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select the checkbox next to `gemini-streamlit-cloudrun`.

  3. Click delete**Delete**.

  4. To confirm deletion, click **Delete**. This also deletes all revisions of the service.




## Delete the load balancer

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing)

  2. Select the checkbox next to `gemini-streamlit-app-lb`.

  3. Click delete**Delete**.

  4. Select the checkboxes next to all the additional resources, including backend services and SSL certificates.

  5. Click **Delete load balancer and the selected resources**.




## Delete the Cloud Build trigger

  1. In the Google Cloud console, navigate to the **Triggers** page.

[Go to the Triggers page](https://console.cloud.google.com/cloud-build/triggers)

  2. Click the menu (vertical ellipsis) located at the right end of the trigger, and then click **Delete**.

  3. To confirm deletion, click **Delete**.




## Delete the network endpoint group

  1. In the Google Cloud console, go to the **Network endpoint group** page.

[Go to Network endpoint group](https://console.cloud.google.com/compute/networkendpointgroups/list)

  2. Select the checkbox next to `streamlit-app-neg`.

  3. Click delete**Delete**.

  4. To confirm deletion, click **Delete**.




## Delete the reserved IP address and DNS records

  1. In the Google Cloud console, go to the **External IP addresses** page.

[Go to External IP addresses](https://console.cloud.google.com/networking/addresses)

  2. Select `genai-app-ip`.

  3. Click **Release static address**.

  4. Remove the DNS records created for the reserved IP address. You might have to contact your domain administrator to complete this step.




## Delete Git repository

Go to your Git repository and click **Settings** > **Danger Zone** > **Delete this repository**.

[ Previous arrow_back  Test your IAP-secured app  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/view-app)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
