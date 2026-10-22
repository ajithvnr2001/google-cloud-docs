---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/csat-chat-api/
title: CSAT in the chat API \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:20.718385+00:00
---

# CSAT in the chat API  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/csat-chat-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  CSAT in the chat API Stay organized with collections  Save and categorize content based on your preferences. 

Customer Satisfaction (CSAT) surveys let you collect feedback from end-users at the end of a chat API session. With this feature, administrators can enable and configure CSAT surveys at both the global and queue level, customize and localize survey messages, and ensure that CSAT data flows into reporting dashboards and CRM integrations.

This document explains how to do the following:

  * Enable or disable CSAT for the chat API globally and per queue

  * Customize and localize CSAT survey messages

  * Understand the inheritance logic between global and queue-level settings




## Before you begin

Before you begin, ensure the following requirements are met.

### System and user setup

  * You must have administrator permissions.

  * The **Customer Satisfaction Ratings** toggle in **Settings > Operation Management** must be turned on. If this main toggle is off, all chat API CSAT toggles in Global and Queue settings will be disabled.

  * If you want end-users to leave written feedback, the **Enable Customer Satisfaction Qualitative Feedback** option in **Settings > Operation Management** must be turned on.

  * If you want CSAT results posted to CRM tickets, the **Enable Customer Satisfaction Rating to Post in CRM record** option in **Settings > Operation Management** must be turned on.




## Configure CSAT at the global level

  * Location: **Settings > Chat > Chat API > Chat API CSAT**

  * Configuration:

    1. Navigate to **Settings > Chat**.

    2. Go to the **Chat API** section.

    3. Locate the **Chat API CSAT** toggle.

    4. Toggle it on to enable CSAT surveys for all chat API sessions by default.

    5. Click **Save**.




When enabled, all chat queues that use the chat API will inherit this global CSAT setting. A CSAT survey will be delivered to end-users at the end of their chat sessions unless overridden at the queue level.

**Important:** If the **Customer Satisfaction Ratings** toggle in **Operation Management** is turned off, the **Chat API CSAT** toggle will appear unavailable. You must enable the main toggle first.

## Configure CSAT at the queue level

  * Location: **Settings > Queue > Web/Mobile > [select queue] > Chat API > Chat API CSAT**

  * Configuration:

    1. Navigate to **Settings > Queues** and select the desired chat queue (web or mobile).

    2. Scroll to the **Chat API** section.

    3. Locate the **Chat API CSAT** toggle.

    4. To override the global setting for this queue, toggle it on or off as needed.

    5. Click **Save**.




The queue-level setting takes priority over the global setting. If the global toggle is on but a specific queue's toggle is off, end-users in that queue will not receive a CSAT survey.

### Inheritance logic

CSAT configuration follows a **Queue > Parent > Global** inheritance model:

  * If no queue-level override is set, the queue inherits its CSAT setting from the parent, which in turn inherits from the global setting.

  * If a queue-level override is set, it takes precedence regardless of the global or parent setting.

  * If the **Customer Satisfaction Ratings** toggle in **Operation Management** is off, all CSAT toggles are forced off and read-only at every level.




## Customize and localize CSAT messages

### Edit survey messages

**Location:**

  * **Settings > Chat > Chat API > Chat API CSAT** (global)

  * **Settings > Queues > [Queue Name] > Chat API > Chat API CSAT** (queue)




**Configuration:**

  * In the CSAT settings section (global or queue level), locate the message fields.

  * Customize the following fields as needed. See the following table.

  * Click **Save**.


Field | Default Value | Description  
---|---|---  
Form Title | Rate Your Experience | The heading displayed at the top of the survey form.  
Form Feedback | Let us know how we can improve. | Subtitle text shown below the form title.  
Result Title | Thank you! | Heading shown after the end-user submits a rating.  
Result Subtitle | We appreciate your feedback | Subtitle shown after submission.  
Feedback Label | Additional feedback | Label for the optional text feedback input field.  
  
The customized messages will be displayed to end-users in the CSAT survey at the end of their chat API sessions. If no custom values are provided, the default messages are used.

If your integration doesn't provide message overrides using the chat API, the CSAT survey uses the messages configured in the CCAI Platform portal (with Global > Parent > Queue inheritance).

### Add translations for multiple languages

  * Location: Same CSAT settings section (Global or Queue level)

  * Configuration:

    1. At the top of the message field list, select a language from the **Language** dropdown.

    2. Enter or update the translated text for each of the five message fields in the selected language.

    3. Repeat for each language you support.

    4. Click **Save**.




When a chat session is conducted in a specific queue, the CSAT survey will be delivered using the language configured for that queue. If a custom translation isn't provided for a given language, the system falls back to the default translation.

**CSAT survey flow — end-user experience**

The CSAT experience for the end-user is as follows:

  1. When a chat API session ends and CSAT is enabled (globally or at the queue level), the end-user is presented with the CSAT survey form.

  2. The survey displays the localized messages matching the queue's language.

  3. The end-user selects a rating from 1 to 5.

  4. If the **Enable Customer Satisfaction Qualitative Feedback** option is enabled in **Operation Management** , an additional text input field is displayed for the end-user to leave written feedback.

  5. After submission, the end-user sees the configured **Result Title** and **Result Subtitle** confirmation messages.




### Optional: Override CSAT messages using the chat API

The CSAT message strings can be overridden at request time when retrieving CSAT configuration for a chat. Any message fields you don't override fall back to the CCAI Platform portal configuration (Global > Parent > Queue inheritance).

**Endpoint (existing):** `GET /apps/api/v1/chats/:chat_id/csat`

**Overridable fields** (independently optional):

  * `form_title`

  * `form_feedback`

  * `result_title`

  * `result_subtitle`

  * `feedback_label`




**Sample request** (override two fields, leave the rest as defaults):
    
    
    {
      "messages": {
        "form_title": "How was your shopping experience?",
        "feedback_label": "Tell us anything else"
      }
    }
    

**Sample response** (overridden where supplied, defaults everywhere else):
    
    
    {
      "form_title": "How was your shopping experience?",
      "form_feedback": "Let us know how we can improve.",
      "result_title": "Thank you!",
      "result_subtitle": "We appreciate your feedback",
      "feedback_label": "Tell us anything else"
    }
    

**Important:** Message overrides are not persisted for the session. Each call to GET /csat decides its own overrides. If you call the endpoint multiple times for the same chat, include the overrides on each request if you want them applied.

## Reporting and CRM integration

### CSAT in reporting dashboards

  * CSAT scores and text feedback collected from chat API sessions are stored in the chat session metadata.

  * Results are available in the standard NRP CSAT dashboards.




### CSAT in CRM records

  * When the **Enable Customer Satisfaction Rating to Post in CRM record** option is enabled in **Operation Management** , CSAT ratings and text feedback are automatically posted to the CRM ticket associated with the chat session.

  * This integration works with all supported CRMs.




## Troubleshooting

Symptom | Possible Cause | Resolution  
---|---|---  
CSAT toggle is unavailable / read-only | The **Customer Satisfaction Ratings** toggle in **Settings > Operation Management** is turned off. | Navigate to **Settings > Operation Management** and enable the **Customer Satisfaction Ratings** toggle.  
Text feedback field does not appear in the survey | The **Enable Customer Satisfaction Qualitative Feedback** option is disabled. | Enable the option in **Settings > Operation Management**.  
CSAT data does not appear in the CRM ticket | The **Enable Customer Satisfaction Rating to Post in CRM record** option is disabled. | Enable the option in **Settings > Operation Management** and confirm the CRM integration is active.  
Survey messages appear in the wrong language | Translations have not been configured for the queue's language. | In the queue's **CSAT settings** , select the correct language from the dropdown and enter the translations.  
Queue does not show CSAT survey even though global is enabled | The queue has a local override that is set to off. | Navigate to the queue's CSAT settings and either enable it or reset it to inherit from global.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
