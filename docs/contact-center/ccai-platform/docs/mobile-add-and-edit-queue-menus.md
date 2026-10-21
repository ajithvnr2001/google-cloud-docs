---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/mobile-add-and-edit-queue-menus/
title: Mobile: Add and Edit queue menus \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:05.630124+00:00
---

# Mobile: Add and Edit queue menus  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/mobile-add-and-edit-queue-menus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Mobile: Add and Edit queue menus Stay organized with collections  Save and categorize content based on your preferences. 

Setting up the queues for your Mobile SDK shapes your customer's experience, dictates agent assignments, and has hundreds of configuration possibilities. The first step to the configuration is to build out the structure of the queues or sub-queues and naming each. The queue names will be displayed to customers within the Mobile SDK.

Queues can be configured to enable specific channels (email, call, chat), the assignment of Agents and Teams to each channel, and many features can be applied at the queue level for specific customization.

If you are using the multiple mobile app configuration, you will need to have a specific setup so that each mobile app has a top-level queue and is assigned a DAP. Refer to [Multiple Mobile Apps Technical Guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Developer_Resources#UUID-f8702524-4b0a-dc36-83f8-d48e8892a2da) for details.

Once you complete the steps, move forward to [Enabling and Assigning Agents to Channels: IVR, Mobile, Web](https://docs.cloud.google.com/contact-center/ccai-platform/docs/setup-agents-channels).

## Enable the mobile channel

![Channels page](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ce5485453e.png)

  1. Go to **Settings > Queue**.

  2. Toggle **On** to enable the Mobile Channel.

**Note:** If turned off while customers contact support through your app, end-users will see the following message:

"Sorry, customer support is not available now."




## Add and edit queues

You can build and edit the structure of your queues just like using a text editor by using your keyboard.

  1. Go to **Settings > Queue**.

  2. Click **Edit / View** to go to the editing section for queue menus within this channel.

  3. Click **Edit** to view the Mobile Menu Structure page.

![Mobile menu structure page](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ce5487c7b8.png)

  4. Click into the **New Item** line to type in the first queue menu name. These queue names will be displayed to customers in the Mobile SDK.

  5. Press **return/enter** to create a new queue menu.

  6. Press **return/enter + tab** to create a sub-queue.

  7. Press **shift + tab** to move back if you pressed tab and want to go back a level.

  8. If IVR or Web queues are set up, you can copy them over by clicking **Copy Queue From** in the top of the edit screen.

  9. Click the **X** to delete a queue option.

  10. Drag the icon to move queue options up or down on the list.

  11. Click **Done** to save.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
