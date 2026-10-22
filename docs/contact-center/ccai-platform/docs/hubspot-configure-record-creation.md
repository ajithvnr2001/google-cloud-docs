---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-configure-record-creation/
title: Configure HubSpot record creation \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:59.765534+00:00
---

# Configure HubSpot record creation  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-configure-record-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure HubSpot record creation Stay organized with collections  Save and categorize content based on your preferences. 

There might be circumstances where you don't want a CRM account or a record created when a new interaction is initiated. For example, if you have an account for a company with multiple employees that contact your call center, you wouldn't want to create a new account with each contact. Or you might expect calls that are very short and don't require their own record. This document explains how to configure Contact Center AI Platform (CCAI Platform) to handle these situations with your HubSpot integration.

To configure HubSpot record creation, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Optional: Select the **Skip CRM account creation** checkbox. The **Skip CRM account lookup** checkbox appears. Contact Center AI Platform (CCAI Platform) won't create new HubSpot accounts when an interaction starts.

  3. Optional: Select the **Skip CRM account lookup** checkbox. Contact Center AI Platform won't perform an account lookup in HubSpot when an interaction starts. If the **Skip CRM account lookup** checkbox is cleared and an account is found, it's reused. If no account is found, a new account isn't created.

  4. Optional: Select the **Skip CRM record creation** checkbox. The **Push session data to CRM account** checkbox appears. CCAI Platform doesn't create new HubSpot records (for example, tickets) when an interaction starts. Select **Skip CRM record creation** to avoid creating excessive tickets or records while still retaining a full engagement history.

  5. Optional: Select the **Push session data to CRM account** checkbox. Session data is directly attached to the account.

  6. Optional: Select the **Attach call data also to the Call object** checkbox. When you select this option, call data is attached to the call object regardless of your account and record creation settings.

  7. For **Closed record options when record ID is passed in via SDK** , select one of the following:

     * **Create new record**. If a CCAI Platform SDK passes in a record ID for a closed record, CCAI Platform creates a new HubSpot record for the interaction. The interaction is associated with the new record. If the record ID is for an open record, CCAI Platform associates the record ID with the interaction, as usual.

     * **Reopen record**. If a CCAI Platform SDK passes in a record ID for a closed record, CCAI Platform reopens the record in HubSpot according to HubSpot's reopen rules and status transitions. The interaction is associated with the reopened record. If the record ID is for an open record, CCAI Platform associates the record ID with the interaction, as usual.

  8. Configure the remaining settings.

  9. Click **Save General**.




## Reporting

Even when you configure your instance to skip CRM record creation, call sessions are still written to HubSpot. This means the following:

  * You can continue to report on call volume, duration, and engagement outcomes from HubSpot reporting tools.

  * You can correlate CCAI Platform call activity with existing HubSpot contacts.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
