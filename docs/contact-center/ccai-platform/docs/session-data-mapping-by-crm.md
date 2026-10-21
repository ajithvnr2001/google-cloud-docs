---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-data-mapping-by-crm/
title: Session data mapping by CRM \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:48:17.223333+00:00
---

# Session data mapping by CRM  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-data-mapping-by-crm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Session data mapping by CRM Stay organized with collections  Save and categorize content based on your preferences. 

## Configuring session data mapping in Salesforce

A Contact Center AI Platform session object is created and attached to a CRM record by default. However, session data mapping depends on your configuration. You can configure session data mapping in the CCAI Platform portal at **Settings > Operation Management > CRM Record Creation Details**.

### Options for attaching session objects

The **CCAI Platform Session Objects attached to CRM Record if a matching CRM Record is found** checkbox appears when you configure **CRM Record Creation Details** as follows:

  * The **Skip CRM account creation** checkbox is cleared.

  * The **Skip CRM record creation** checkbox is selected.

  * The **Append call or chat session to latest open record in the same leaf queue** is selected.




Otherwise, the **CCAI Platform Session Objects attached to the Accounts/Contacts/Leads** checkbox appears.

## Session data mapping in a custom CRM solution

When the skip record creation option is ON, you will see a warning icon and message if you try to add an endpoint to the Create a record endpoint field because this endpoint is not in use.

## Session data mapping in ServiceNow

If you are configuring skip CRM record creation options for ServiceNow, an additional option, **Push session data to CRM account** , becomes available. This option adds the session data to the CRM account without the creation of a new record. If this option is not selected, the session data won't appear in the account or in a record.

## Session data mapping in Zendesk

If the skip account creation option is ON and the skip record creation option is ON, there are no comments or file attachments in the CRM record because Zendesk does not allow these. If the append call or chat session to the latest open record in the same leaf queue option is enabled, the session data is appended to the latest open record instead.

## Monitoring sessions with account or record creation disabled

Even when the options to create an account or record are disabled, there is an entry in the **Completed Call/Chat** page to show that a call or chat occurred. A call or chat ID is created but the normally embedded link that lets you open the ticket in the CRM won't be available.

## Session data in external storage

Session data is sent to external storage if external storage is configured. For more information, see [Set up external storage for CRMs](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
