---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-a-dialogflow-agent/
title: Create and integrate Dialogflow agents \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:19.534223+00:00
---

# Create and integrate Dialogflow agents  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-a-dialogflow-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Create and integrate Dialogflow agents Stay organized with collections  Save and categorize content based on your preferences. 

Before you can create any kind of virtual agent, you must create a Customer Experience Agent Studio agent or a Dialogflow agent and integrate it with Contact Center AI Platform. This document explains how to integrate with a Dialogflow.

## Virtual agent Dialogflow platforms

**Dialogflow ES** : This platform only supports agent setup for Chat channels. Select this option to onboard virtual agents built using Dialogflow ES.

**Dialogflow CX** : This option supports agent setup for both chat and voice channels. Agent interactions include advanced functions such as DTMF support, consumer barge-in, call companion, speech analysis, Customer Experience Insights, and many others. Select this option to onboard virtual agents built using Dialogflow CX.

## Channel-specific responses

(CCAI Platform) automatically sets the channel value when calling the Dialogflow API. Voice calls have the channel set to `voice`, and chat conversations are set to `chat`. This applies to virtual agent support for mobile chat, web chat, and IVR. These capabilities enable you to create channel-specific responses within your virtual agents. For more information, see [Channel-specific response messages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#channel-specific).

## Create Dialogflow ES and Dialogflow CX virtual agents

Specific instructions for the creation of [Dialogflow CX virtual agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) and for [Dialogflow ES virtual agents](https://docs.cloud.google.com/dialogflow/es/docs/quick/build-agent).

## Create conversation profile for Dialogflow CX virtual agents

After you've made a virtual agent, to onboard it into the CCAI Platform portal, you must create a conversation profile in the Agent Assist console.

  1. Navigate to [Agent Assist](https://agentassist.cloud.google.com/).

  2. Select **Conversation Profiles** from the menu.

  3. In the Project drop-down list at the top, select the project that the Dialogflow CX virtual agent was created in.

  4. In the Location drop-down list at the top, select the Google Cloud region that the virtual agent is located in.

  5. Click **Create new**. The **New Conversation Profile** page is displayed.

  6. Enter a name for your conversation profile. Note that this is the name that will appear in the CCAI Platform Portal for the list of available virtual agents.

  7. To link the existing Dialogflow CX virtual agent to the conversation profile:

     1. Navigate to **Choose to use Dialogflow CX** section.

     2. Turn **ON** the **Enable virtual agent** toggle switch.

     3. Enter the `Dialogflow CX Agent ID` in the **Agents** field.

  8. The **Agents** field appears, select the virtual agent that you created in Dialogflow CX.




For additional information, read about [Agent Assist conversation profiles](https://docs.cloud.google.com/agent-assist/docs/conversation-profile).

Conversation profiles provide the ability to use [Dialogflow CX versions and environments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version). Environments are isolated spaces where you can deploy different versions of your Dialogflow CX agent. This lets you manage and test multiple versions of your virtual agent in a controlled way.

## Create a service account and key

CCAI Platform integrates to Dialogflow CX using the Dialogflow API. Access to the API is controlled using Google Cloud service accounts and associated service account key. The service account and associated key are project specific, so if multiple virtual agents are being used from a single project, the same service account and key can be reused.

The following steps walk you through the process of creating the service key in Google Cloud. For more information about Google service accounts see [What are service accounts?](https://docs.cloud.google.com/iam/docs/service-account-overview#what-are-service-accounts)

If you have already created a service key with access to Dialogflow CX, you can skip this section, note that you must enter a service key into the CCAI Platform Portal to link a Dialogflow CX virtual agent.

**Caution:** Follow Google's [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

To create a service account, grant the correct permissions and generate a service account key. Follow these steps:

  1. Navigate to the [Google Cloud console](https://console.cloud.google.com/). A default project appears.

  2. In the toolbar drop-down, select the Google project that you used to set up your Dialogflow CX agent.

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

Based on how your company handles segmentation within Dialogflow CX, you can create multiple virtual agent platform entries and add specific Dialogflow CX agents, or create one platform with many Dialogflow CX agents.

Repeat the previous steps for each Dialogflow CX agent that you need to onboard to the CCAI Platform Portal.

## Add a virtual agent platform

**Dialogflow ES** : This platform only supports agent setup for Chat channels. Select this option to onboard agents built using Dialogflow ES.

**Dialogflow CX** : This option supports agent setup for both Chat and Voice channels. Agent interactions include advanced functions such as DTMF support, consumer barge-in, CCAI Insights tracking, call companion, sentiment analysis, and others. Select this option to onboard agents built using Dialogflow CX.

Select this option to onboard virtual agents built using Dialogflow CX.

  1. Go to **Settings > Developer settings > Virtual agent platform**.

  2. Click **\+ Add Platform**.

The **Add a virtual agent platform** dialog appears.

![Add a virtual agent platform page](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca6a70e241.png)

  3. Enter a name for the new platform, consider using the project name that the virtual agents were created in.

  4. Select from the following services:

     * **Dialogflow ES**

     * **Dialogflow CX**

  5. Click **Create**.

  6. Adjacent to the new virtual agent platform in the virtual agent platforms list, toggle the virtual agent platform to **On**.


**Note:** You can use the same service account key file used earlier for the existing virtual agent. You don't need any new credentials in general. However, it's recommended to **generate new service account keys to avoid dealing with expired/deactivated keys**.

Virtual agents onboarded using Dialogflow CX will use the `StreamingAnalyzeContent` API that will best support DTMF inputs and future virtual agent upgrades.

## Virtual agent platform statuses

CCAI Platform validates service account keys based on JSON structure and key validity. A Dialogflow CX virtual agent is fully authenticated only when its key is in the **Valid** state:

  * **Valid** : All workflows in the platform are valid.

  * **Needs Attention** : One or more workflows in the platform are Invalid. Replace with valid service account keys to resolve.

  * **Invalid:** All workflows in the platform are Invalid. When a platform status is invalid, the platform is automatically disabled. Replace invalid service account keys with valid keys to resolve.




If the status is **Invalid** or **Needs Attention,** generate service account keys for any invalid keys, and replace the invalid keys with the new ones. For more information, see [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete).

When the configuration steps are complete, your virtual agents are ready. For more information about how to manage them, see [Assign virtual agents to queues](https://docs.cloud.google.com/contact-center/ccai-platform/docs/assign-virtual-agents-to-queues).

## Support for partial response in Dialogflow CX

CCAI Platform supports the partial response feature in Dialogflow CX. This is particularly useful when your virtual agent needs to call a webhook that will likely take a while to run and return a response. With partial response enabled, Dialogflow CX can immediately send an initial fulfillment message to the end-user, such as, "One moment while I look that up." This way, while the webhook runs and the final fulfillment message is generated, the end-user expects a short wait instead of assuming that there is a problem. For more information, see [Partial response for streaming API](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response).

Dialogflow CX also lets you specify if the playback of the partial response should be canceled upon returning the final fulfillment to CCAI Platform. If cancellation of partial response is enabled, CCAI Platform terminates the playback of the initial fulfillment if it is still playing and then starts the playback of the final fulfillment. This lets you respond with a partial response fulfillment that could include Speech Synthesis Markup Language (SSML) code to play an audio file, such as a simulated typing sound. The following example is a Dialogflow CX fulfillment that does this:
    
    
    <speak>
      One moment while I look up your order.
      <audio src="typing-sound.mp3">
        <desc>Typing sound</desc>
        PURR (sound didn't load)
      </audio>
    </speak>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
