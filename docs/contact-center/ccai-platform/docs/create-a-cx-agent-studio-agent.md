---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-a-cx-agent-studio-agent/
title: Create and integrate Customer Experience Agent Studio agents \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:09.510368+00:00
---

# Create and integrate Customer Experience Agent Studio agents  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-a-cx-agent-studio-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Create and integrate Customer Experience Agent Studio agents Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to integrate Contact Center AI Platform (CCAI Platform) with CX Agent Studio agents.

## Create CX Agent Studio virtual agents

For information about creating a Customer Experience Agent Studio virtual agent, see [Agents](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/agent).

## Create conversation profile for CX Agent Studio virtual agents

For information about how to create a conversation profile for your CX Agent Studio agent, see [Connect an agent application to a new conversation profile](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/deploy/ccaas#connect_an_agent_application_to_a_new_conversation_profile)

## Create a service account and key

CCAI Platform integrates with CX Agent Studio using the Dialogflow API. To access the API, you need a Google Cloud service account and an associated key. Because these are project-specific, you can reuse them if you are using multiple virtual agents from a single project.

The following steps walk you through creating a service key in Google Cloud. For more information about Google service accounts see [What are service accounts?](https://docs.cloud.google.com/iam/docs/service-account-overview#what-are-service-accounts)

If you have already created a service key with access to CX Agent Studio, you can skip this section. Note that you must enter a service key into the CCAI Platform Portal to link a CX Agent Studio virtual agent.

**Caution:** Follow Google's [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

To create a service account, grant the correct permissions and generate a service account key. Follow these steps:

  1. Navigate to the [Google Cloud console](https://console.cloud.google.com/). A default project appears.

  2. In the toolbar drop-down, select the Google project that you used to set up your CX Agent Studio agent.

  3. Select **IAM & Admin**.

  4. In the side navigation select **Service Accounts**. The service account console will load.

  5. Click **+Create Service Account**.




### Enter the service account details in Google Cloud service

  1. Enter the service account details.

     1. Display name for this service account.

     2. Service account ID is required and must be unique.

     3. Describe what this service account will do.

     4. Grant this service account access to a project.

  2. In the **Select a role** drop-down: Assign the `Dialogflow API Admin` role to the service account.

  3. Click **Continue**.




### Edit actions in the service accounts page

The Google Cloud service accounts page displays any service accounts associated with your project.

![Service accounts page](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca6a70a6ac.png)

**Note:** The Google Cloud service accounts page might display multiple service accounts. Verify the service account `Name` with the service account link from the Agent Settings page before selecting it.

To create a service account key see [Create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating). Follow Google recommended best practices for storing your key.

Based on how your company handles segmentation within Customer Experience Agent Studio, you can create multiple virtual agent platform entries and add specific Customer Experience Agent Studio agents, or create one platform with many Customer Experience Agent Studio agents.

Repeat the previous steps for each Customer Experience Agent Studio agent that you need to onboard to the CCAI Platform Portal.

## Add a virtual agent platform

Select this option to onboard virtual agents built using CX Agent Studio.

  1. Go to **Settings > Developer settings > Virtual agent platform**.

  2. Click **\+ Add Platform**.

The **Add a virtual agent platform** dialog appears.

![Add a virtual agent platform page](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/6bhAryEpi5o7Qxt.png)

  3. Enter a name for the new platform, consider using the project name that the virtual agents were created in.

  4. Select from the following service:

     * **Conversational Agents / CX Agent Studio**
  5. Click **Create**.

  6. Adjacent to the new virtual agent platform in the virtual agent platforms list, toggle the virtual agent platform to **On**.


**Note:** You can use the same service account key file used earlier for the existing virtual agent. You don't need any new credentials in general. However, it's recommended to **generate new service account keys to avoid dealing with expired/deactivated keys**.

Virtual agents onboarded using CX Agent Studio will use the `StreamingAnalyzeContent` API that will best support DTMF inputs and future virtual agent upgrades.

## Virtual agent platform statuses

CCAI Platform validates service account keys based on JSON structure and key validity. A CX Agent Studio virtual agent is fully authenticated only when its key is in the **Valid** state:

  * **Valid** : All workflows in the platform are valid.

  * **Needs Attention** : One or more workflows in the platform are Invalid. Replace with valid service account keys to resolve.

  * **Invalid:** All workflows in the platform are Invalid. When a platform status is invalid, the platform is automatically disabled. Replace invalid service account keys with valid keys to resolve.




If the status is **Invalid** or **Needs Attention,** generate service account keys for any invalid keys, and replace the invalid keys with the new ones. For more information, see [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete).

When the configuration steps are complete, your virtual agents are ready. For more information about how to manage them, see [Assign virtual agents to queues](https://docs.cloud.google.com/contact-center/ccai-platform/docs/assign-virtual-agents-to-queues).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
