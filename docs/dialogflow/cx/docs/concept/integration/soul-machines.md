---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/soul-machines/
title: Soul Machines \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:50.694002+00:00
---

# Soul Machines  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/soul-machines/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Soul Machines Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Dialogflow CX integrates with [Soul Machines](https://www.soulmachines.com/), which lets you create and have conversations with 3D avatars.

**Note:** When using a third party integration, requests and end-user data are sent to both Google and the third party. The terms of service, SLA, pricing, and quotas [for your agent edition](https://docs.cloud.google.com/dialogflow/docs/editions) are applicable for Google's handling of these requests. The third party's terms of service, SLA, pricing, and quotas are applicable for the third party's handling of these requests. 

## Setup

To set up the integration:

  1. Follow these steps to get a Dialogflow CX service account key in [Google Cloud console](https://console.cloud.google.com/): 
     * [Create a Google Cloud Service Account](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#sa) for the project that contains your Dialogflow CX agents. The minimum Identity and Access Management (IAM) roles required to integrate with Soul Machines are `Dialogflow API Client` and `Dialogflow API Reader`.
     * Download the service account key in JSON format.
  2. Follow these steps to link a digital avatar to Dialogflow CX in the [Soul Machines](https://www.soulmachines.com/) dashboard: 
     * Customize an existing project by clicking the **Customize** button, or create a new project.
     * Select **Knowledge** on the navigation menu.
     * In **Conversation** , click **Replace Conversation**.
     * Select **Dialogflow CX**.
     * Upload the Google Cloud service account key that you downloaded in the previous step.
  3. Your Soul Machines avatar is now integrated with your Dialogflow CX agent.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
