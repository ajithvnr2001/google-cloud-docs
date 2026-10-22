---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup/
title: Google Cloud project setup \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:41.030804+00:00
---

# Google Cloud project setup  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Google Cloud project setup Stay organized with collections  Save and categorize content based on your preferences. 

This page documents the steps required to configure a Google Cloud project for telephony integration.

## Select or create a Google Cloud project

SIP Trunks are connected to a project for communication reasons only, but their impact is not limited to a specific project.

For example, you may have three different projects (development, testing, production). If the same SIP Trunk is used for all SBC to GTP communication, only the first request to create the SIP Trunk will succeed, and the rest of the requests to create the SIP Trunk in the same region/hostname will fail.

We recommend that a different project be used for the sole purpose of managing SIP Trunks. This allows a different team to be responsible for the trunks, and within the Trunk UI, they can establish different groups of SBCs for development, testing, and production.

To use services provided by Google Cloud, you must create a _project_. A project organizes all your Google Cloud resources. A project consists of a set of collaborators, enabled APIs (and other resources), monitoring tools, billing information, and authentication and access controls. You can create one project, or you can create multiple projects and use them to organize your Google Cloud resources in a [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). When creating a project, take note of the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). You will need this ID to make API calls. For more information on projects, see the [Resource Manager documentation](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 



[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

## Permissions

  1. In the Google Cloud Console, navigate to **IAM & Admin -> IAM**.
  2. Either select an existing service account or create a new one, and make sure that it has the **`Dialogflow API Admin`** role assigned to it. This role is required for telephony integration.



## Phone number API access

Using the phone number API methods requires special access. Contact your Google representative for more information.

## Configure Dialogflow, conversation profile, and phone number

This section walks you through the process of creating a [Conversational AI conversation profile](https://docs.cloud.google.com/agent-assist/docs/conversation-profile) with an associated Google Telephony Platform (GTP) phone number.

  1. Navigate to [Colab Enterprise](https://console.cloud.google.com/vertex-ai/colab/) If prompted, enable the **Compute Engine** , **Dataform** , and **Vertex** APIs.
  2. Click **Import notebooks** , then select **URL** as the data source. Enter this [GitHub repository URL](https://github.com/GoogleCloudPlatform/dialogflow-integrations/blob/master/tools/SIP_SIPREC_integration_Dialogflow_CURL_commands_with_SIP_TRUNK_management.ipynb), then click **IMPORT**.
  3. In the `PROJECT_ID` field, enter the Google Cloud project ID for the project you'd like to associate with the integration. Your existing projects can be found in the drop-down menu at the top of the page in the [Cloud Console](https://console.cloud.google.com/).
  4. Enter your chosen region in the `REGION` field. All [Dialogflow regions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region) are supported.
  5. Either leave the `JWT` field as is, or enter your `JWT` value here. If left blank, SSO is used by default. 
  6. Click the play button in the top **Project** section to run that section of code. When prompted, allow the notebook to access your Google credentials.
  7. Expand the **Configuring Conversational AI for SIP/SIPREC** section. Under **Create a dummy Dialogflow ES agent...** , click **Show code** and run the code without making any changes. This creates a dummy Dialogflow ES agent and sets its tier to Enterprise. A dummy Dialogflow ES agent is required in order to access Dialogflow API endpoints. Each Google Cloud project can have a single Dialogflow ES agent.
  8. Expand to display the code under the **Script to create a`ConversationProfile`...** section. 
     * `CONVERSATION_PROFILE_NAME`: Can be any string. You can use the default value or input your own.
     * `SECURITY_SETTINGS`: Can be any string. You can use the default value or input your own.
     * `PHONE_NUMBER_COUNTRY_CODE`: Enter the country code you want to associate with your GTP phone number.
     * `CX_AGENT_NAME`: Enter the name of the Dialogflow CX agent you want the generated conversation profile to be associated with.
  9. Run the code. The output will include the name of the generated `ConversationProfile`, security settings, and GTP phone number.
  10. Navigate to the [Dialogflow ES console](https://dialogflow.cloud.google.com/) to verify that an agent named `Dummy_ES_agent` has been created. Click **Settings** to verify that the agent is associated with the correct Google Cloud project and that it has been upgraded to the **Essentials** edition.
  11. Navigate to the [Agent Assist console](https://agentassist.cloud.google.com/). Click **Conversation profiles** in the left-hand menu to verify that a conversation profile with your entered `CONVERSATION_PROFILE_NAME` has been created.
  12. Navigate to the [Conversational AI Insights console](https://ccai.cloud.google.com/insights/projects). Verify that all conversation transcripts associated with your Dialogflow CX agent have been imported.



## (Optional) Request a quota increase for Dialogflow CX Phone Gateway call length

Dialogflow ES Essentials and Dialogflow CX subscriptions come with standard available quotas. If you are not using Dialogflow at all, for example only Agent Assist, Transcription, or Call Recording, your default quota is the same as the Dialogflow ES Essentials quota.

You have the option of requesting a quota increase if needed based on your estimated traffic. In most use cases the standard quota is sufficient for setup and testing, but runtime applications require an increase. See the [Dialogflow quotas page](https://docs.cloud.google.com/dialogflow/quotas) for quota details and instructions for requesting an increase.

## (Optional) Enable audit logging for the Dialogflow API

You can optionally enable [audit logging](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) for the Dialogflow API (dialogflow.googleapis.com) for Admin Read, Data Read, and Data Write. Doing so lets you see all the individual Conversational AI API calls made and the credentials used for authorization and consumption. This can be useful for troubleshooting and debugging.

## What's next

Learn how to [setup and configure an SBC](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/sbc-config).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
