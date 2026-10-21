---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-disposition-timing/
title: Configure disposition timing \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:23.525726+00:00
---

# Configure disposition timing  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-disposition-timing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure disposition timing Stay organized with collections  Save and categorize content based on your preferences. 

Disposition timing lets you control how Contact Center AI Platform (CCAI Platform) behaves when an agent manually changes their status to wrap-up. By default, when an agent enters wrap-up status, the system attributes their wrap-up disposition code and notes to the most recent call or chat session. With disposition timing, you can let agents attribute their disposition code and notes to a previously completed session. You can also let agents modify disposition codes and notes for previously completed sessions.

## Before you begin

Configure wrap-up and disposition codes for your queues. For more information, see [Queue-level wrap-up settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-level-wrap-up-settings) and [Disposition codes and lists](https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-note).

## Configure manual wrap-up attribution

You can configure how CCAI Platform attributes disposition codes and notes during manual wrap-up. That is, when an agent manually changes their status to wrap-up. You can have the system automatically attribute the disposition code and notes to the last session, or you can have the agent adapter present a list of previous sessions that the agent can attribute the disposition codes and notes to.

To configure manual wrap-up attribution, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Wrap-up > Manual Wrap-up** section.

  3. To attribute manual wrap-up to the last session, select the **Automatically attribute manual wrap-up to the last call or chat session** checkbox.

  4. To present a list of previous sessions in the agent adapter for the agent to attribute manual wrap-up to, select the **Select the call or chat session to attribute manual wrap-up to** checkbox.

  5. To configure the list of previous sessions in the agent adapter, select one of the following:

     * **Display the list of the last[INTEGER] calls and chats**. Set the number of call and chat sessions to display in the agent adapter.

     * **Display the list of the calls and chats within the last[INTEGER] hours**. Set a time period, in hours. Sessions that ended within that time period are displayed in the agent adapter.

  6. Click **Save Wrap-Up**.




## Let agents edit disposition codes and notes for previous sessions

Disposition codes and notes for previous sessions appear in the agent adapter for only 15 to 30 minutes after a session ends. After that, they can't be edited. However, agents can still enter new notes, which appear in a new CRM record.

To let agents modify disposition codes and notes for previous sessions, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Wrap-up > Manual Wrap-up** section.

  3. Select the **Allow agents to modify the disposition code and notes of previously completed sessions** checkbox.

  4. Click **Save Wrap-Up**.




Changes are saved in a new CRM record. The original CRM record is unchanged. The system overwrites the existing session metadata file with a new session metadata file.

**Note:** For HubSpot users, the `hs_call_disposition` property on HubSpot call sessions is overwritten to reflect the most recent disposition code. The full history is preserved in the CRM notes.

## Turn on CRM record autoload

CRM record autoload is for agents using an agent adapter embedded in a CRM. With CRM autoload, when an agent selects a previous session to attribute wrap-up to, the associated CRM record automatically displays.

To turn on CRM record autoload, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Wrap-up > Manual Wrap-up** section.

  3. Select the **Automatically load CRM record when switching between calls and chats** checkbox.

  4. Click **Save Wrap-Up**.




## Reporting

  * The system tracks each manual wrap-up disposition submission as a separate wrap-up period with its own start and end time.

  * If agents frequently use manual wrap-up, you might see an increase in the number of wrap-up records per session. Consider the latest disposition as the final outcome.

  * The system attributes each wrap-up period's elapsed time to the session that the agent selected when they submitted the disposition.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
