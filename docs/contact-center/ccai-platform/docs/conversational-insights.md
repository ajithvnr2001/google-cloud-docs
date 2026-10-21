---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/conversational-insights/
title: Customer Experience Insights and Quality AI \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:22.482860+00:00
---

# Customer Experience Insights and Quality AI  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/conversational-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Customer Experience Insights and Quality AI Stay organized with collections  Save and categorize content based on your preferences. 

[Customer Experience Insights](https://docs.cloud.google.com/contact-center/insights/docs) (CX Insights) helps you detect and visualize patterns in your contact center data. Understanding conversational data drives business value, improves operational efficiency, and provides a voice for customer feedback.

You can analyze conversation data with CX Insights to do the following:

  * Run machine learning analytics to gain additional information such as agent and caller sentiment, entity identification, and call topics. Automatically identify interesting interactions in need of further review.

  * Review a conversation with audio playback, transcript synchronization and analytics annotations.




CX Insights seamlessly integrates with other products, allowing you to import conversations from Dialogflow CX and Agent Assist.

[Quality AI](https://docs.cloud.google.com/contact-center/insights/docs/qai-overview) builds on CX Insights to enable comprehensive contact center quality evaluations, including individual conversations, live agents, and virtual agents.

## Set up CX Insights

This section explains how to set up CX Insights. Google recommends creating a new Cloud Storage bucket specifically for CX Insights, with its own service account key.

### Before you begin

Before you set up CX Insights, do the following:

  * [Enable CX Insights](https://docs.cloud.google.com/contact-center/insights/docs/before-you-begin) on a Google Cloud project. As a part of the process you must enable the following APIs:

    * **Speech-to-Text** : to be able to generate transcripts from the call audio recordings.

    * **Cloud Storage API** : to be able to access the stored call recordings and transcripts from the Cloud Storage bucket. You can either use a pre-existing Cloud Storage bucket or create a new one.

  * [Create a Google Cloud Service Account and key](https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-a-dialogflow-agent#create-a-service-account-and-key) in the project where you will be using CX Insights. In addition, grant the following IAM roles to your service account:

    * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin)

    * [Contact Center AI Insights editor](https://docs.cloud.google.com/iam/docs/roles-permissions/contactcenterinsights#contactcenterinsights.editor)

    * [Cloud Speech-to-Text Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/speech#speech.serviceAgent)

For more information about granting roles to a service account see the [Google IAM Manage Access documentation](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#single-role).

**Important:** Failure to grant the correct IAM Role will prevent CX Insights from functioning correctly. **Caution:** Follow Google's [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).



### Configure CX Insights

To configure CX Insights, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Customer Experience Insights** pane, and then click **Setup Insights**. The **Enable Customer Experience Insights** dialog appears.

  3. Click the **Enable Customer Experience Insights** toggle to the on position.

  4. In the **Customer Experience Insights Project ID** field, enter your CCAI Platform project ID. Use lowercase letters.

  5. In the **Region** field, select the region.

  6. To send call recordings to CX Insights, click the **Send call recordings** toggle to the on position.

  7. To send chat transcripts to CX Insights, click the **Send chat transcripts** toggle to the on position.

  8. For **Server Setup** , select **New Google Cloud Storage**.

  9. In the **GCS Bucket Name** field, enter a name for your Cloud Storage bucket.

  10. In the **Service Account Key** field, enter the service account key that you created in Before you begin.

  11. Optional: In the **Folder Path** field, edit the folder path. Your edits appear in the paths in the **File Destinations** section. For information about using variables in the folder path, see [Dynamic folder path and file names](https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage#dynamic-folder-path-and-file-names).

  12. Click **Save**.




## View CX Insights data

After your conversation data has been uploaded, you can view your CX Insights data in the [CX Insights Console](https://ccai.cloud.google.com/insights/projects). The conversation ID in CX Insights is either the CCAI Platform call or chat ID—for example, `call-123` or `chat-987`.

You can't use the same CX Insights instance to consume conversations from multiple Google Cloud Contact Center as a Service instances. This leads to duplicate conversation IDs, which is not supported. Conversations with duplicate conversation ID fail to be uploaded to CX Insights.

Session metadata is also passed from Google Cloud Contact Center as a Service when the conversation is uploaded to CX Insights. The metadata values are provided as labels in the CX Insights information section when viewing a conversation.

The provided labels are imported:

Metadata key | Calls | Chats | Description  
---|---|---|---  
hold_duration | ✔ |  | Duration that the end-user was put on hold for in seconds.  
customer_phone_number | ✔ |  | The phone number of the end-user.  
outbound_number | ✔ |  | The phone number that the outbound call was placed from (outbound calls only).  
transfers | ✔ | ✔ | The number of times the call was transferred.  
has_feedback | ✔ | ✔ | Whether the conversation had a feedback response.  
fail_reason | ✔ | ✔ | The reason for the failure of the conversation.  
out_ticket_id | ✔ | ✔ | The ticket ID of the conversation.  
agent_assist_conversation_id_X* | ✔ | ✔ | The Agent Assist conversation ID of the conversation.  
dialogflow_conversation_id_X* | ✔ | ✔ | The Dialogflow CX conversation ID of the conversation.  
queue_priority_level | ✔ | ✔ | The priority level of the conversation.  
answer_type | ✔ | ✔ | The type of the answer.  
session_type_v2 | ✔ | ✔ | The type of the session.  
menu | ✔ | ✔ | The menu of the conversation.  
**Note:** * X is a number based on the leg of the conversation where multiple Agent Assist or Dialogflow CX sessions existed.

Other metadata values that are used within CX Insights include the following:

Metadata key | Calls | Chats | Description  
---|---|---|---  
id | ✔ | ✔ | The call or chat ID of the session used for the conversation ID.  
agent_name | ✔ | ✔ | The name of the human agent that handled the conversation.  
agent_id | ✔ | ✔ | The internal CCaaS ID that identified the human agent.  
virtual_agent_id | ✔ | ✔ | The internal CCaaS ID that identified the virtual agent.  
  
Session metadata stored in Cloud Storage is updated 15 minutes after completion of the session.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 
