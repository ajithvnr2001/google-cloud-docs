---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-cross-project-adk-agents/
title: Configure cross-project ADK agent access \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:32.197778+00:00
---

# Configure cross-project ADK agent access  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-cross-project-adk-agents/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure cross-project ADK agent access Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how administrators can grant permission for Gemini Enterprise to access an ADK agent that runs within Agent Runtime on Gemini Enterprise Agent Platform in a different Google Cloud project.

## Identify the Gemini Enterprise service agent

To find the service agent email address for your Gemini Enterprise app project:

  1. In the Google Cloud console, go to the project that contains your Gemini Enterprise app.
  2. From the project list, find the project number.
  3. Construct the service agent email address using the following format:
         
         service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com
         

Replace `PROJECT_NUMBER` with the project number from the previous step.




### Grant permissions in the agent project

Grant the Gemini Enterprise service agent permissions in the project where the ADK agent is hosted with Agent Runtime:

  1. In the Google Cloud console, go to the project where the ADK agent is hosted with Agent Runtime.
  2. Go to **IAM & Admin > IAM**.
  3. Click person_add **Grant Access**.
  4. In the **New principals** field, enter the service agent email address that you identified in the previous section.
  5. In the **Select a role** list, search for and select **Discovery Engine Service Agent** (`roles/discoveryengine.serviceAgent`).
  6. Click **Save**.



## What's next

  * After granting these permissions, you can [Register the ADK agent](https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent#register-an-adk-agent) in your Gemini Enterprise app, using the agent's resource path from the agent project.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
