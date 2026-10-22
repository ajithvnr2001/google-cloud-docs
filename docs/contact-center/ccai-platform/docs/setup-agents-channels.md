---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/setup-agents-channels/
title: Setting up and assigning agents to channels and queues: IVR, mobile, web \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:13.598761+00:00
---

# Setting up and assigning agents to channels and queues: IVR, mobile, web  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/setup-agents-channels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Setting up and assigning agents to channels and queues: IVR, mobile, web Stay organized with collections  Save and categorize content based on your preferences. 

Channels are configurable and should be enabled and set up individually.

  * IVR (Interactive Voice Response) is your standard phone line channel or entry point. You can assign multiple languages, numbers, and many other configurations once enabled.

  * Mobile is used once the CCAI Platform SDK is installed in your customer-facing Android or iOS app.

  * Web channel requires the configuration of the Web SDK on one or more of your webpages.




Once channels are enabled, and call or chat channels have been assigned agents, you are ready to handle end-user questions and requests.

## Details

  * At least one agent must be assigned to a call or chat queue for the queue to be enabled

  * Agents can only be assigned to a leaf queue, so if there is a sub-queue associated, agents must be assigned to one of the sub-queues

  * Queue menus are set up and ready to use when the color turns from red to white

  * If enabling multiple languages, see [Enable multiple languages for IVR, mobile, and web channels](https://docs.cloud.google.com/contact-center/ccai-platform/docs/enable-multiple-languages)




## Assign agents to the IVR channel

  1. Go to **Settings** > **Queue.**

  2. Toggle the switch to **On**.

  3. Click **Edit / View**.

  4. Queue menu names are listed in the left panel. Select a queue to edit by clicking anywhere next to the name of the queue.

  5. Check the box next to **Instant Voice Call**.

  6. Click **Assign agents** to go to the agent assignment page.

  7. Enter the agent names or team names, then click **Save**.

![Agent name](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ce5479ef7e.gif)

  8. Follow the steps for either [Cascade Groups](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cascade_groups) or [Percent Allocation Groups](https://docs.cloud.google.com/contact-center/ccai-platform/docs/percent_allocation_groups) to use an advanced routing configuration.




## Assign agents and configuring the mobile channel

  1. Go to **Settings** > **Queuex**.

  2. Click **Edit / View** in the Mobile panel.

  3. Queue menu names are listed in the left panel. Select a queue to edit by clicking anywhere next to the name of the queue.

![View or edit queues](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ce547c5819.png)

  4. Mark the checkbox for **Email** to show an email option to customers. Set the email address and instructions for the message field, then click **Save Email**.

Enter an Email address that will appear as the 'Sender', and check the 'Email' box. This will automatically save the email address that you entered.

(optional) Enter any Instructions for the Message field to appear just above the Message field.

If you enabled either of the optional settings then make sure to click **Save Email** .

  5. Mark the checkbox for **Chat** to show chat as an option for this queue.

  6. Mark the checkbox for **Scheduled Voice Call** to show an option for customers to select from a list of available times to receive a call. See

  7. Mark the checkbox for **Instant Voice Call** to show an option in the SDK for customers to place a call using the app.

  8. Click **Assign agents** next to each of the options enabled for the queue.

![Assign agents](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ce547ef092.gif)

  9. Follow the steps for either [Cascade Groups](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cascade_groups) or [Percent Allocation Groups](https://docs.cloud.google.com/contact-center/ccai-platform/docs/percent_allocation_groups) to use an advanced routing configuration.

  10. If using Mobile calls, set up the fallback to IVR setting for each queue. Step-by-step instructions see [Mobile: PSTN Fallback](https://docs.cloud.google.com/contact-center/ccai-platform/docs/mobile-pstn-fallback).

  11. To hide the menu option so that it is not shown as an option in the SDK, toggle Hide Selection from Menu to Hide.

  12. To direct consumers to a message, phone number, or voicemail, use Automatic Redirection. More information here: [Automatic Redirection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/automatic_redirection).

  13. For **Custom After Hour Message Deflection Options Mobile** and **Display After Hour Deflection Message** details, see [Mobile and SDK Messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/customize-mobile-web-messages#customize-mobile-and-web-messages).




## Enable and add agents to the web channel

  1. Go to **Settings** > **Queue**.

  2. Toggle the switch to **On**.

  3. Click **Edit / View** to access the editing section for queues within that channel.

  4. Queue names are listed in the left panel. **Select a queue** to edit by clicking anywhere next to the name of the queue.

  5. Mark the checkbox for **Email** to show an email option to customers.

Enter an Email address that will appear as the 'Sender', and check the 'Email' box. This will automatically save the email address that you entered.

(optional) Enter any Instructions for the Message field to appear just above the Message field.

(optional) Check the **Enable reCAPTCHA** box to help prevent spam emails.

If you enabled either of the optional settings then make sure to click **Save Email**.

  6. Mark the checkbox for **Chat** to show chat as an option for this queue.

  7. Mark the checkbox for **Scheduled Voice Call** to show an option for customers to select from a list of available times to receive a call.

  8. Mark the checkbox for **Instant Voice Call** to show an option for customers to receive a call-back call to the phone number they enter.

![Instance Voice Call setting](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ce54824ae0.gif)

  9. Click **Assign agents** next to each of the options enabled for the queue.

  10. Enter the agent names or team names, then click **Save**.

![Agent details](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ce5482aff0.gif)

  11. Follow the steps for either [Cascade Groups](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cascade_groups) or [Percent Allocation Groups](https://docs.cloud.google.com/contact-center/ccai-platform/docs/percent_allocation_groups) to use an advanced routing configuration.

  12. To hide the menu option so that it is not shown as an option in the SDK, toggle Hide Selection from Menu to Hide.

  13. To other options than directing consumers straight to an agent, use Automatic Redirection. More information here: [Automatic Redirection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/automatic_redirection).

  14. To direct an end-user directly to this queue, use a Direct Access Point. See [Direct Access Points (DAPs)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#direct-access-points).

  15. For **Display After Hour Deflection Message settings** , see [Mobile and Web SDK messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/customize-mobile-web-messages#customize-mobile-and-web-messages).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
