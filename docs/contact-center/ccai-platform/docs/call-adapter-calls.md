---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-calls/
title: Receive and make calls \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:33.611577+00:00
---

# Receive and make calls  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-calls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Receive and make calls Stay organized with collections  Save and categorize content based on your preferences. 

This section describes how to receive inbound calls and make outbound calls.

## Receive an inbound call

The first step of receiving a call is answering it. Answering a call varies slightly depending on whether auto-answer is enabled. For more information, see [Auto-answer](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#auto-answer).

To receive an inbound call:

  1. Answer the call:

     * If auto-answer is disabled, a notification banner appears on your screen notifying you of an inbound call. Click the banner to answer the call.

     * If auto-answer is enabled, an Incoming call screen appears in the call adapter and the target pick-up time appears.

  2. After you answer the call, the following sequence begins in the call adapter:

     1. A new screen appears that displays caller information, queue information, and the support phone number that the caller used.

     2. A final countdown timer appears for the start of the call. If the caller has multiple accounts, you have the option to choose which account to attach to the call.

     3. The call starts.




## Make an outbound call

This procedure is for making outbound calls _without_ flexible outbound dialing. For information about making outbound calls with flexible outbound dialing, see Make an outbound call using flexible outbound dialing. For more information, see [Flexible outbound dialing](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-integration-guide#flexible-outbound-dialing) (for Salesforce) or [Flexible outbound dialing](https://docs.cloud.google.com/contact-center/ccai-platform/docs/zendesk#flexible-outbound-dialing) (for Zendesk).

To make an outbound call, follow these steps:

  1. In the call adapter, click **Start call**. The **Outbound call** screen appears.

  2. To change the country code, do the following:

     1. Click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-country-code-selector-usa.png) (the flag that appears in this selector represents that last country code that you selected). The **Country code** screen appears.

     2. OPTIONAL: To mark a country code as a favorite, click star **Favorite** next to the country code. Favorite country codes are grouped at the top of the list. To remove a country code from your favorites, click the star icon again.

     3. Click the country code that you want for your outbound call. You can use the search field to narrow your search. The flag for the country code appears in the **Outbound call** screen.

  3. Enter the phone number:

     * You can dial the number or paste it into the **Enter phone number** field.

     * If you have a CRM, you can select the number from your CRM.

     * The system automatically includes the selected country code when it places your outbound call. You don't need to enter it with the phone number. If you enter a country code and it doesn't match the country code selector, the country code selector updates to match the code.

  4. To change the outbound number, click **Outbound number** , and then click the outbound number that you want.

  5. To change the language, click **Language** , and then click the language that you want.

  6. To change the queue, click **Queue** , and then click the queue that you want.

  7. Click **Call**. The **Calling** screen appears.

  8. Wait for the end-user to answer the call.




## Make an outbound call using flexible outbound dialing

This procedure is for making outbound calls _with_ flexible outbound dialing. For information about making outbound calls without flexible outbound dialing, see Make an outbound call. For more information, see [Flexible outbound dialing](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-integration-guide#flexible-outbound-dialing) (for Salesforce) or [Flexible outbound dialing](https://docs.cloud.google.com/contact-center/ccai-platform/docs/zendesk#flexible-outbound-dialing) (for Zendesk).

To make an outbound call using flexible outbound dialing, follow these steps:

  1. In the call adapter, click **Start call**. The **Outbound call** screen appears.

  2. To change the country code, do the following:

     1. Click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-country-code-selector-usa.png) (the flag that appears in this selector represents that last country code that you selected). The **Country code** screen appears.

     2. OPTIONAL: To mark a country code as a favorite, click star **Favorite** next to the country code. Favorite country codes are grouped at the top of the list. To remove a country code from your favorites, click the star icon again.

     3. Click the country code that you want for your outbound call. You can use the search field to narrow your search. The flag for the country code appears in the **Outbound call** screen.

  3. Enter the phone number:

     * You can dial the number or paste it into the **Enter phone number** field.

     * If you have a CRM, you can select the number from your CRM.

     * The system automatically includes the selected country code when it places your outbound call. You don't need to enter it with the phone number. If you enter a country code and it doesn't match the country code selector, the country code selector updates to match the code.

  4. To change the outbound number, click **Outbound number** , and then click the outbound number that you want.

  5. Click **Next**. The **Outbound call details** screen appears.

  6. OPTIONAL: If no account ID exists for the phone number you are calling, do the following:

     1. In the **Account ID** section, click  open_in_new . Your CRM app opens.

     2. Select an account or create a new one.

If an account ID exists, you can click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-copy.png)**Copy** to copy the account ID.

  7. OPTIONAL: If no record ID exists for the phone number you are calling, do the following:

     1. In the **Record ID** section, click  open_in_new . Your CRM app opens.

     2. Select a record or create a new one.

If a record ID exists, you can click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-copy.png)**Copy** to copy the record ID.

  8. To call a number that's not saved in the account, click the **Call a separate number** toggle to the on position.

  9. To change the language, click **Language** , and then click the outbound language that you want.

  10. Click **Call**. The **Calling** screen appears.

  11. Wait for the end-user to answer the call.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
