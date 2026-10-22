---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sensitive-data-redaction/
title: Sensitive data redaction \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:46.044593+00:00
---

# Sensitive data redaction  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sensitive-data-redaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Sensitive data redaction Stay organized with collections  Save and categorize content based on your preferences. 

You can configure Contact Center AI Platform (CCAI Platform) to redact sensitive data from chat sessions in real time in the agent adapter, in the web SDK widget, and in chat transcripts. This helps prevent unauthorized people from accessing sensitive data. This capability is available for the web channel.

## Before you begin

Before you begin, do the following:

  * Integrate your CCAI Platform instance with [Sensitive Data Protection (DLP API)](https://cloud.google.com/sensitive-data-protection/docs/dlp-api-overview).
  * Prepare a service account key file (JSON format) from your Google Cloud account to upload to the CCAI Platform portal.
  * Create Sensitive Data Protection [inspection](https://cloud.google.com/sensitive-data-protection/docs/creating-templates-inspect) and [de-identification](https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid) templates.

**Caution:** Follow Google's [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

## Add a redaction platform

To add a redaction platform, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.
  2. In the **Redaction Platform** pane, click **Add platform**. The **Add Redaction Platform** dialog appears.
  3. In the **Name** field, enter a name for your platform.
  4. In the **Service** list, click **Google Cloud DLP API**.
  5. Click **Add**.
  6. Click **Upload key** , and navigate to your service account key file. A valid key is required to activate the redaction platform.
  7. When the key is verified, click **Save**. Your new platform is added to the **Redaction Platform** pane with a **Valid** status and the toggle in the on position.



The system fetches and syncs all available inspection and de-identification templates from your Google Cloud account. For more information, see Before you begin.

## Redaction platform statuses

Here are the redaction platform statuses:

  * **Valid** : The platform is active and all of its templates are valid and accessible.
  * **Invalid** : All of the templates in the platform are invalid or missing. Redactions linked to this platform aren't functional.
  * **Needs attention** : One or more templates in the platform are invalid. Redactions linked to this platform might not be functional until the platform is fixed.



When a platform's status changes to **Needs attention** or **Invalid** , the system sends an email notification to the administrator.

## Configure automatic redaction settings at the global level

To configure automatic redaction settings at the global level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Chat**. If you don't see the **Settings** menu, click menu **Menu**.
  2. Go to the **Automatic Redaction** pane and click the toggle to the on position.
  3. To configure the default template, do the following: 
     1. In the **Platform** list, select a platform.
     2. In the **Inspect** list, select the type of information that you want to redact. Examples are SSN, CC, Phone number, Drivers license number, Passport ID number, Street address, Custom numbers (for example, bank account information).
     3. In the **De-identify** list, select a de-identifier for the system to use to redact sensitive information. For example, `###`, or `***`.
  4. To configure the redaction settings, do the following: 
     1. To redact sensitive data from all incoming messages, select the **Automatically redact all incoming messages to agents** checkbox. Configure whether you want sensitive data redaction to virtual agents, human agents, or both.
     2. To redact sensitive data from all outgoing messages to end-users, select the **Automatically redact all outgoing messages to agents** checkbox. Configure whether you want sensitive data redaction from virtual agents, human agents, or both.
     3. To redact all sensitive data from agents' session notes, select the **Automatically redact all session notes from agents** checkbox.
     4. To let human agents view and hide redacted sensitive data in messages, select the **Allow human agents to view unredacted messages during session** checkbox.
  5. To configure the operation settings, do the following:

     1. To upload unredacted transcripts, select the **Store unredacted transcripts in records** checkbox. Configure whether you want to upload to linked CRM tickets, to external storage, or both.

**Note:** When you select this option, both redacted and unredacted transcripts are stored. Unredacted transcripts are stored in a folder called `chat-transcripts-unredacted`.
     2. To upload unredacted wrap-up notes, select the **Upload unredacted notes in the linked CRM tickets and session metadata** checkbox.

**Note:** When you select this option, both redacted and unredacted wrap-up notes are stored.
     3. To send unredacted transcripts to end-users, select the **Send unredacted transcripts to consumers** checkbox.

  6. Click **Save**.




## Configure automatic redaction settings at the queue level

To configure automatic redaction settings at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**. The **Queue Menu Settings** page appears.
  2. In the **Web** pane, click **Edit / View**.
  3. Click the queue that you want to edit.
  4. For **Automatic Redaction** , click **Configure**.
  5. Click the **Chat Redaction** toggle to the on position.
  6. To configure the default template, do the following: 
     1. In the **Platform** list, select a platform.
     2. In the **Inspect** list, select the type of information that you want to redact. Examples are SSN, CC, Phone number, Drivers license number, Passport ID number, Street address, Custom numbers (for example, bank account information).
     3. In the **De-identify** list, select a de-identifier for the system to use to redact sensitive information. For example, `###`, or `***`.
  7. To configure the redaction settings, do the following: 
     1. To redact sensitive data from all incoming messages, select the **Automatically redact all incoming messages to agents** checkbox. Configure whether you want sensitive data redaction to virtual agents, human agents, or both.
     2. To redact sensitive data from all outgoing messages to end-users, select the **Automatically redact all outgoing messages to agents** checkbox. Configure whether you want sensitive data redaction from virtual agents, human agents, or both.
     3. To redact all sensitive data from agents' session notes, select the **Automatically redact all session notes from agents** checkbox.
     4. To let human agents view and hide redacted sensitive data in messages, select the **Allow human agents to view unredacted messages during session** checkbox.
  8. To configure the operation settings, do the following:

     1. To upload unredacted transcripts, select the **Store unredacted transcripts in records** checkbox. Configure whether you want to upload to linked CRM tickets, to external storage, or both.

**Note:** When you select this option, both redacted and unredacted transcripts are stored. Unredacted transcripts are stored in a folder called `chat-transcripts-unredacted`.
     2. To upload unredacted wrap-up notes, select the **Upload unredacted notes in the linked CRM tickets and session metadata** checkbox.

**Note:** When you select this option, both redacted and unredacted wrap-up notes are stored.
     3. To send unredacted transcripts to end-users, select the **Send unredacted transcripts to consumers** checkbox.

  9. Click **Save**.




## Agent experience

When you configure sensitive data to be redacted for human agents, you can select the **Allow human agents to view unredacted messages during session** checkbox. This displays a **Show redacted** button in the chat adapter. When an agent clicks **Show redacted** , the button changes to **Hide redacted** and the redacted data displays. When an agent clicks **Hide redacted** , the button changes to **Show redacted** and the redacted data is hidden. For more information, see Configure automatic redaction settings at the global level and Configure automatic redaction settings at the queue level.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
