---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-lookups/
title: HubSpot lookups \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:34.376888+00:00
---

# HubSpot lookups  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-lookups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  HubSpot lookups Stay organized with collections  Save and categorize content based on your preferences. 

You can configure your HubSpot integration with primary and secondary lookups, which can identify a caller based on their contact record or company profile. If the primary lookup returns no results, the system attempts the secondary lookup. In addition, you can configure which CRM account display fields from the matched primary or secondary lookup object appear in the agent adapter. Lastly, you can configure the CRM _record_ display fields that appear in the agent adapter, regardless of whether the primary or secondary object was matched. The record display fields apply to the opened CRM record—for example, a ticket or a deal.

Configure the CRM _account_ display fields when you're configuring the primary lookup object and configuring the secondary lookup object. To configure the CRM _record_ display fields, see Configure CRM record display fields in the agent adapter.

**Note:** HubSpot lookups replace the previous HubSpot mobile phone number lookups. If you configured your HubSpot integration using HubSpot mobile phone number lookups, your configuration is preserved until you edit it.

## Before you begin

Before you begin, integrate HubSpot with your Contact Center AI Platform (CCAI Platform) instance. For more information, see [HubSpot](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot).

## Configure the primary lookup object

You can configure the primary lookup object, which is the first object that the system searches for when a session begins. You can also configure which CRM account display fields appear in the agent adapter. The following procedure shows you how to do both.

To configure the primary lookup object and the CRM account display fields, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **CRM** pane, go to the **Account Lookup** section.

  3. To configure the primary lookup object, do the following:

     1. Expand the **Primary Lookup Object** section.

     2. In the **Object Type** list, select the type of object to look up.

     3. In the **Phone number lookup fields** list, select the fields that the system should use to match the end-user's phone number.

     4. In the **Phone number primary field** list, select the field where a customer's phone number is stored when the system creates a new CRM account.

     5. For **Phone Number Format** , select the request phone number format.

     6. Optional: To look up end-users by custom field for SDK sessions, do the following:

        1. Select the **Mobile / Web SDKs: lookup users by custom field for SDK sessions** checkbox.

        2. In the **Custom lookup field in CRM** list, select the custom lookup field.

  4. To configure CRM account display fields in the agent adapter, do the following:

     1. In the **CRM Account Display Fields** section, in the **Matched account display field** list, select the main identifier for the account.

     2. Optional: To display a second field, do the following:

        1. Select the **Display a second field** checkbox.

        2. In the **Second Display Field** list, select a second field type to display.

        3. For **Second field display position** , select the order to display the fields in the agent adapter.

  5. Click **Save**.




## Configure the secondary lookup object

You can configure the secondary lookup object, which serves as a fallback in case the primary lookup returns no results. You can also configure which CRM account display fields appear in the agent adapter. The following procedure shows you how to do both.

To configure the secondary lookup object and the CRM account display fields, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **CRM** pane, go to the **Account Lookup** section.

  3. To configure the secondary lookup object, do the following:

     1. Select the **Secondary Lookup Object** checkbox.

**Note:** The **Object Type** list displays the option type that you didn't select in Configure the primary lookup object.
     2. In the **Phone number lookup fields** list, select the fields that the system should use to match the end-user's phone number.

     3. In the **Phone number primary field** list, select the field where a customer's phone number is stored when when CCAI Platform creates a new CRM account.

     4. For **Phone Number Format** , select the request phone number format.

     5. Optional: To look up end-users by custom field for SDK sessions, do the following:

        1. Select the **Mobile / Web SDKs: lookup users by custom field for SDK sessions** checkbox.

        2. In the **Custom lookup field in CRM** list, select the custom lookup field.

  4. To configure CRM account display fields in the agent adapter, do the following:

     1. In the **CRM Account Display Fields** section, in the **Matched account display field** list, select the main identifier for the account.

     2. Optional: To display a second field, do the following:

        1. Select the **Display a second field** checkbox.

        2. In the **Second Display Field** list, select a second field type to display.

        3. For **Second field display position** , select the order to display the fields in the agent adapter.

  5. Click **Save**.




## Configure CRM record display fields in the agent adapter

You can configure the CRM record display fields that appear in the agent adapter, regardless of whether the primary or secondary object was matched. To configure which CRM _agent_ display fields that appear in the agent adapter, see Configure the primary lookup object and Configure the secondary lookup object.

To configure CRM record display fields in the agent adapter, do the following:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **CRM** pane, go to the **CRM Record Display Fields** section.

  3. In the **Matched record display field** list, select the main identifier for the record.

  4. Optional: To display a second field, do the following:

     1. Select the **Display a second field** checkbox.

     2. In the **Second Display Field** list, select a second field type to display.

  5. Optional: To display a third field, do the following:

     1. Select the **Display a third field** checkbox.

     2. In the **Third Display Field** list, select a third field type to display.

  6. Click **Save**.




## Lookup cascade logic

The following explains the cascade logic that CCAI Platform uses for object lookups:

  * If `contact_id` is provided, CCAI Platform performs a direct GET call first. Otherwise, CCAI Platform searches phone, email, SDK, and SIP identifiers using OR logic.

  * If multiple matching records are found, CCAI Platform selects the one modified most recently. Modification dates are determined as follows:

    * **Contact** uses `lastmodifieddate`.

    * **Company** uses `hs_lastmodifieddate`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
