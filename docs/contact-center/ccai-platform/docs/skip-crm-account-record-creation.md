---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/skip-crm-account-record-creation/
title: Skip CRM account and record creation \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:06.002537+00:00
---

# Skip CRM account and record creation  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/skip-crm-account-record-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Skip CRM account and record creation Stay organized with collections  Save and categorize content based on your preferences. 

There might be circumstances where you don't want a CRM account or a record created when a new call or chat session is initiated. For example, if you have an account for a company with multiple employees that contact your call center, you wouldn't want to create a new account with each contact. Or you might expect calls that are very short and don't require their own record. This page explains how to configure Contact Center AI Platform (CCAI Platform) to handle these situations.

When you skip CRM account and record creation, the data mapping options vary significantly depending on whether you map session data to a CRM activity object or to a CCAI Platform session. The following procedures are grouped according to whether you are mapping session data to a CRM activity object or to a CCAI Platform session.

You can skip account and record creation with Salesforce, Zendesk, ServiceNow, and custom CRM integrations.

## Skip account or record creation and map session data to an activity object

This section shows the data mapping options that are available when you map call or chat session data to a CRM activity object. The following procedures show you how to skip CRM account and record creation while mapping to a CRM activity object:

  * Skip account creation and map to an activity object

  * Skip record creation and map to an activity object

  * Skip account and record creation and map to an activity object




### Skip account creation and map to an activity object

To skip CRM account creation and map to a CRM activity object, do the following:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Operation Management**.

  2. In the **General** pane, go to **CRM Record Creation Details**.

  3. For **Session Data** , in the **Map data to** field, select **Activity Object**. The CRM activity object is attached to a CRM record.

  4. For **CRM Record Creation Details** , select the **Skip CRM account creation** checkbox.

  5. Optional: To append the session to the latest open record in the leaf queue, select the **Append call or chat session to latest open record in the same leaf queue** checkbox. If there is no open record in the same leaf queue, a new record is created.

  6. Optional: To skip CRM account lookup, select the **Skip CRM account lookup** checkbox. The **Append call or chat session to latest open record in the same leaf queue** checkbox disappears because you can't find the latest open record if there is no account lookup.

  7. Click **Save General**.




### Skip record creation and map to an activity object

To skip CRM record creation and map to a CRM activity object, do the following:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Operation Management**.

  2. In the **General** pane, go to **CRM Record Creation Details**.

  3. For **Session Data** , in the **Map data to** field, select **Activity Object**.

  4. For **CRM Record Creation Details** , select the **Skip CRM record creation** checkbox. For **Records** , a single data mapping option is available.

  5. Optional: To append the session to the latest open record in the leaf queue, select the **Append call or chat session to latest open record in the same leaf queue** checkbox. If there is no open record in the same leaf queue, no new record is created.

  6. Click **Save General**.




### Skip account and record creation and map to an activity object

To skip CRM account and record creation and map to a CRM activity object, do the following:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Operation Management**.

  2. In the **General** pane, go to **CRM Record Creation Details**.

  3. For **Session Data** , in the **Map data to** field, select **Activity Object**.

  4. For **CRM Record Creation Details** , select the **Skip CRM account creation** and **Skip CRM record creation** checkboxes.

  5. Optional: To append the session to the latest open record in the leaf queue, select the **Append call or chat session to latest open record in the same leaf queue** checkbox. If there is no open record in the same leaf queue, no new record is created.

  6. Optional: To skip CRM account lookup, select the **Skip CRM account lookup** checkbox. The **Append call or chat session to latest open record in the same leaf queue** checkbox disappears because you can't find the latest open record if there is no account lookup.

  7. For **Records** , a single data mapping option is available. Click **Save General**.




## Skip account or record creation and map session data to a CCAI Platform session

This section shows the data mapping options that are available when you map call or chat session data to a CCAI Platform session. The following procedures show you how to skip CRM account and record creation while mapping to a CCAI Platform session:

  * Skip account creation and map to a CCAI Platform session

  * Skip record creation and map to a CCAI Platform session

  * Skip account and record creation and map to a CCAI Platform session




### Skip account creation and map to a CCAI Platform session

To skip CRM account creation and map to a CCAI Platform session, do the following:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Operation Management**.

  2. In the **General** pane, go to **CRM Record Creation Details**.

  3. For **Session Data** , in the **Map data to** field, select **CCaaS Session**. For **Records** , a single data mapping option is available.

  4. For **CRM Record Creation Details** , select the **Skip CRM account creation** checkbox.

  5. Optional: To append the session to the latest open record in the leaf queue, select the **Append call or chat session to latest open record in the same leaf queue** checkbox. If there is no open record in the same leaf queue, a new record is created.

  6. Optional: To skip CRM account lookup, select the **Skip CRM account lookup** checkbox. The **Append call or chat session to latest open record in the same leaf queue** checkbox disappears because you can't find the latest open record if there is no account lookup.

  7. Click **Save General**.




### Skip record creation and map to a CCAI Platform session

To skip CRM record creation and map to a CCAI Platform session, do the following:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Operation Management**.

  2. In the **General** pane, go to **CRM Record Creation Details**.

  3. For **Session Data** , in the **Map data to** field, select **CCAIP Session**.

  4. For **CRM Record Creation Details** , select the **Skip CRM record creation** checkbox. For **Records** , three data mapping options are available. If you don't need the following optional step, select a **Records** option, and then click **Save General**. Otherwise, go to the following step.

  5. Optional: To append the session to the latest open record in the leaf queue, select the **Append call or chat session to latest open record in the same leaf queue** checkbox. If there is no open record in the same leaf queue, no new record is created. For **Records** , a single data mapping option is available.

  6. Click **Save General**.




### Skip account and record creation and map to a CCAI Platform session

To skip CRM account and record creation and map to a CCAI Platform session, do the following:

  1. In the CCAI Platform portal, click menu **Menu** , and then click **Settings > Operation Management**.

  2. In the **General** pane, go to **CRM Record Creation Details**.

  3. For **Session Data** , in the **Map data to** field, select **CCaaS Session**.

  4. For **CRM Record Creation Details** , select the **Skip CRM account creation** and **Skip CRM record creation** checkboxes. For **Records** , three data mapping options are available. If you don't need the following optional steps, select a **Records** option, and then click **Save General**. Otherwise, go to the following step.

  5. Optional: To append the session to the latest open record in the leaf queue, select the **Append call or chat session to latest open record in the same leaf queue** checkbox. If there is no open record in the same leaf queue, no new record is created. For **Records** , a single data mapping option is available. If you don't need the following optional step, click **Save General**. Otherwise, go to the following step.

  6. Optional: To skip CRM account lookup, select the **Skip CRM account lookup** checkbox. The **Append call or chat session to latest open record in the same leaf queue** checkbox disappears because you can't find the latest open record if there is no account lookup. For **Records** , two data mapping option are available. Select an option, and then click **Save General**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
