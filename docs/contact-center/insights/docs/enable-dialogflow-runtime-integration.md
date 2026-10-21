---
url: https://docs.cloud.google.com/contact-center/insights/docs/enable-dialogflow-runtime-integration/
title: Enable Dialogflow runtime integration \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:23:21.536787+00:00
---

# Enable Dialogflow runtime integration  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/enable-dialogflow-runtime-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Enable Dialogflow runtime integration Stay organized with collections  Save and categorize content based on your preferences. 

Dialogflow runtime integration lets you integrate data from other Dialogflow-powered Contact Center AI services into Customer Experience Insights. These services also include [Agent Assist](https://docs.cloud.google.com/agent-assist/docs) and [virtual agents](https://docs.cloud.google.com/dialogflow/es/docs/agents-overview). After you enable the integration, you can view conversations created in Agent Assist and virtual agent in CX Insights. To learn more about this feature, see the [Concepts documentation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/dialogflow-runtime-integration). CX Insights supports the use of audio conversation data in addition to chat conversation data facilitated through a SIPREC endpoint. The SIPREC integration is established through [Agent Assist](https://docs.cloud.google.com/agent-assist/docs/siprec).

## Prerequisites

To learn how to enable CX Insights for your Google Cloud project, see [Enable Customer Experience Insights](https://docs.cloud.google.com/gemini-enterprise-cx/insights/before-you-begin).

## Enable runtime integration (global endpoint)

  1. Go to the [Agent Assist console](https://agentassist.cloud.google.com/).

  2. Click the settings **Settings** option.

  3. Verify that **Send data to Insights** is enabled. ![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/send-data-to-insights.png)

  4. Go to the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).

  5. Click settings **Agent settings**.

  6. Under the **General** tab, go to the **Logging settings** header and ensure that **Enable Conversation History** is checked. ![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/enable-conv-history.png)




## Enable runtime integration (regional endpoint)

  1. Go to the security settings page at the following link. Substitute your project ID where it says _PROJECT_ID_.
         
         https://ccai.cloud.google.com/projects/PROJECT_ID/securitySettings

  2. Create or update existing security settings in the correct region.

![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/create-security-settings.png)

  3. Verify that **Send data to Insights** is enabled in the **Export** tab. ![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/v3-send-data-to-insights.png)

  4. Go to the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).

  5. Click settings **Agent settings**.

  6. Go to the **General** tab.

  7. Go to the **Logging settings** header.

  8. Ensure **Enable Conversation History** is checked. ![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/enable-conv-history.png)

  9. Attach security settings from the previous step in the **Security** tab. Repeat this step for each virtual agent. ![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/dfcx-security-settings.png)

  10. Go to the [Agent Assist console](https://agentassist.cloud.google.com/).

  11. Attach your security settings to all your conversation profiles in the **Conversation profile** page. ![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/aa-conversation-profile-security-settings.png)




## Enable audio export

  1. (Optional) Enable CX Insights audio export settings for voice conversations. This step is necessary to make your audio files available for listening within CX Insights. Your audio files are stored in a Cloud Storage bucket and nowhere else. So if you don't enable `audio_export_settings`, CX Insights will only have access to the transcript and cannot play back the conversation audio.

     1. Go to the security settings page at the following link. Enter your project ID where indicated.
    
    https://ccai.cloud.google.com/projects/PROJECT_ID/securitySettings

     1. Filter to the correct region.

     2. Click **V2 Security Settings** or security settings created in the previous step.

     3. Click the **Export** tab. ![](https://docs.cloud.google.com/static/gemini-enterprise-cx/insights/images/v3-send-data-to-insights.png)

     4. Enter your Cloud Storage bucket's name.

     5. Click **Save**.

  2. To save the audio recordings for an entire telephony conversation, specify the format of your audio files, for example, `MP3`, `MULAW`, `M4A`, or `OGG`. This setting is available only when using the API.
         
         curl -H "Content-Type: application/json"\
             -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
             -H "x-goog-user-project: PROJECT" \
             -X PATCH https://LOCATION-dialogflow.googleapis.com/v3/projects/PROJECT/locations/LOCATION/securitySettings/SECURITY_SETTINGS?update_mask=audio_export_settings\
             --data '{"audio_export_settings":{"gcs_bucket": "BUCKET","audio_format": "FORMAT"}}'




## Verify Customer Experience Insights service agent permissions

  * Make sure that the Customer Experience Insights service agent has the [permissions to fetch conversations from Dialogflow](https://docs.cloud.google.com/gemini-enterprise-cx/insights/known-issues). This is enabled by default, you can come back to this step if the conversations don't show up.



## Import conversation metadata

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

[Contact your Google representative](https://docs.cloud.google.com/gemini-enterprise-cx/insights/getting-support) to enable this feature in your project.

You can add conversation metadata such as `labels` or [`qualityMetadata`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.conversations#QualityMetadata) to CX Insights either before or after the conversation is imported by using the `UpdateConversation` API with `allow_missing` set to `true`. Provide metadata of valid input fields along with the ID of the Dialogflow conversation in the [`UpdateConversationRequest`](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.conversations/patch#request-body), and CX Insights merges the conversation and metadata.

## Create a conversation in Agent Assist and view it in CX Insights

  1. Create a conversation profile using the Agent Assist console by following [the tutorial instructions](https://docs.cloud.google.com/agent-assist/docs/conversation-profile). Don't enable the virtual agent option.
  2. (Optional) Test the performance of your conversation profile using the [Agent Assist simulator](https://docs.cloud.google.com/agent-assist/docs/simulator).
  3. Follow the instructions to [create a Smart Reply conversation](https://docs.cloud.google.com/agent-assist/docs/smart-reply). Handling conversations at runtime requires direct API calls. These actions cannot be carried out using the Agent Assist console. Make sure that you [complete the conversation](https://docs.cloud.google.com/agent-assist/docs/smart-reply#complete_the_conversation) before moving on. Only completed conversations are visible in CX Insights.
  4. Navigate to the [CX Insights console](https://ccai.cloud.google.com/insights/projects).
  5. Enter the project ID that you used to create the Agent Assist conversation and view this conversation in CX Insights. The CX Insights conversation name matches the conversation name in Agent Assist.



## Create a conversation in virtual agents and view it in CX Insights

  1. [Create a virtual agent](https://docs.cloud.google.com/agent-assist/docs/agent-virtual) and optionally [import sample data to your agent](https://docs.cloud.google.com/agent-assist/docs/agent-virtual#import-the-example-file-to-your-agent).
  2. The remaining steps are the same as [creating a conversation in Agent Assist](https://docs.cloud.google.com/gemini-enterprise-cx/insights/enable-dialogflow-runtime-integration#create_a_conversation_in_agent_assist_and_view_it_in_insights), with the exception that you must enable the **virtual agent** option when you create a conversation profile in order for the profile to use your newly created agent.



## Create a conversation in Dialogflow CX console and view it in CX Insights

  1. [Create a virtual agent](https://docs.cloud.google.com/agent-assist/docs/agent-virtual).
  2. Test the agent to create a conversation.
  3. Navigate to the [CX Insights console](https://ccai.cloud.google.com/insights/projects). After a few moments, you should see your conversation with the test agent on your conversation history.



## Troubleshooting

For help with issues related to Dialogflow runtime integration, see the [Troubleshooting page](https://docs.cloud.google.com/gemini-enterprise-cx/insights/troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
