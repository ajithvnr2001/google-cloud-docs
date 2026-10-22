---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaigns-do-not-call/
title: Company Do Not Call list \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:24.710793+00:00
---

# Company Do Not Call list  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaigns-do-not-call/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Company Do Not Call list Stay organized with collections  Save and categorize content based on your preferences. 

You can use Contact Center AI Platform to manage blocked numbers for your campaigns. The **Company Do Not Call list** specifically lets you create and maintain this registry at the company level.

Customers can place themselves on the US National Do Not Call (DNC) registry if they don't want to receive solicitation calls. Businesses can check this registry at the [National Do Not Call Registry](https://www.donotcall.gov/). CCAI Platform does not support the national registry.

## Expected behavior

The DNC list can block direct, manual, and outbound calls, as well as outbound and scheduled calls created by the Apps API, depending on how you configure it. The configuration also allows the list to be updated using the **Do Not Call Again** disposition code for cases.

If an agent attempts to contact an end user on the list, they receive the following message: `This call cannot be placed because the phone number is on the Company DNC list`.

Configured emergency numbers cannot be added to the Company DNC list or blocked from outbound calls.

When making a call, the dialer checks the DNC list before dialing each number and skips blocked numbers.

Additional considerations:

  * Automated callback scenarios aren't blocked.

  * For preview mode for outbound calls, the contact is presented to the agent only if it's not on the DNC list.

  * If the dialer has been configured to block direct, manual outbound calls made by agents, the following error message is displayed: `This call cannot be placed because the phone number is on the Company DNC list`.

  * If you add third-party numbers, they are blocked if the third-party numbers are on the Company DNC list. Using the **Do Not Call Again** disposition code allows the entry of the number into a DNC database.




The DNC list consists of contact entries with the following fields:

  * **Phone number**

  * **Timestamp** : The time when the contact was added to the list.

  * `expires_at`: The date or time when numbers can be removed from the DNC list.

    * Contacts are removed from the DNC list within an hour of the expiration time.

    * If it's not set, the number remains on the list indefinitely.


**Note:** Strings are limited to 200 characters.

## Enable the DNC list

To enable the DNC list, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Campaigns > Company Do Not Call (DNC) List**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Move the switch to **ON**. By default, the switch is **OFF**. Additional menu options appear. Configure the following options as needed:

     * To apply the DNC list check to direct, manual outbound calls made by agents as well as outbound and scheduled calls created by the Apps API, select the checkbox.

     * To allow the use of the **Do Not Call Again** disposition code, enable the disposition code. By default, this option is **OFF**.

**Note:** Since this option also exists independently in the campaigns settings, it is important to ensure that both the disposition code and the feature itself are enabled for the DNC list to work in conjunction with the disposition code.

**Note:** If the Company Do Not Call (DNC) List isn't visible in your instance, contact your account team to enable it.

## API endpoints for the Company Do Not Call list

The Company DNC endpoints let you do the following:

  * Add multiple phone numbers to the DNC list.

  * Remove phone numbers from the DNC list.

  * Check whether a phone number is on the DNC list.




For more information, see [Company Do Not Call List](https://externals.ujet.co/apidocs/apps/publication.html#CompanyDoNotCallList).

## View the DNC list and blocked numbers in reporting

**Important:** You can't see or download the full DNC list because it contains PII.

  * If a call is attempted to a blocked number, this is logged in the real-time metrics field.

  * Attempted calls that are blocked using DNC are logged as `dnc_abandoned` with the following reason: `Company DNC`.

  * Numbers on the DNC list are also included in the **Campaign Summary Report**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
