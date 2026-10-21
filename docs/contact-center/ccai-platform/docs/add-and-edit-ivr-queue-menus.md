---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-and-edit-ivr-queue-menus/
title: IVR: Add and edit queue menus \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:05.160528+00:00
---

# IVR: Add and edit queue menus  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-and-edit-ivr-queue-menus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  IVR: Add and edit queue menus Stay organized with collections  Save and categorize content based on your preferences. 

Setting up the queue menus for the IVR channel shapes your customer's journey, your agent's assignments, and has hundreds of configuration possibilities. The first step of the configuration is to build out the structure of the queues or sub-queues and name each. Queue menus can be set to route to a specific group of agents, deflect to messages, other queues, phone numbers, or voicemail, and many features can be applied at the queue level for specific customization.

Once you complete the following steps, move forward to enable agents.

## Details and tips

  * Due to the number of digits on a keypad, there's a 9 top-level queue menu limit

  * If you need to more than 9 queues, nest more queues within a top-level queue

  * All numbers assigned to your environment will default to the top of the queue unless otherwise assigned as Direct Access points (DAPs)

  * If you are using multiple languages, numbers will default to the language selection message, then when the language is selected, will route to the top of the menu structure for the selected language

  * If you want to hide a queue from a caller who dials into a number that goes to the top of the queue, toggle the **Hide Selection From Menu** option to **Hide** in the menu settings

  * For internal transfers to teams or groups not available to callers, create one queue, hide the option from callers, and create all the necessary sub-queues for agents to pick from for transfers

  * Once your queues are set up, you can see the numbers that the caller needs to select. If there are no numbers next to the option, the queue has been hidden.

In the example, the first option can be selected by pressing 3, and the "Hidden VIP" menu wouldn't be available as an option to press. Hidden queues can be accessed using [Direct Access Points (DAPs)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#direct-access-points).




## Admin configuration

  1. Go to **Settings > Queue.**

  2. Toggle to **On** to enable the IVR channel. **If toggled off** while customers call your support number, callers will hear: "Sorry this number is not available right now" and be disconnected.




### Add and edit queue menus

You can build and edit the structure of your menu just like using a text editor by using your keyboard.

  1. Click **Edit / View** to goto the editing section for queue menus within that channel.

  2. Click **Edit** to add and edit queues on the IVR Menu Structure page.

  3. Click into the **New Item** line to type in the first queue menu name. The queue name will only play to the customer if text-to-speech is used for reading queue options.

  4. Press **return/enter** to create a new queue menu.

  5. Press **return/enter + tab** to create a sub-queue.

  6. Press **shift + tab** to move back if you pressed tab and want to go back a level.

  7. If Mobile or Web queues are set up, you can copy them over by clicking **Copy Queue From** in the top of the edit screen.

  8. Click the **x** next to the queue name to delete a queue option.

  9. Click the grid to move queue options up or down in the list.

  10. Click **Done** to save your new queue menus.




### Allow transfers to queue

This setting lets you enable or disable transfers to go into queue (at the queue level configuration). By default, this is turned ON.

The specific Queue will be hidden from the Queue Transfer menu in the Agent Adapter, if the Allow transfers to Queue is turned OFF. 

  1. Queue menu names are listed in the left panel. **Select a queue** to edit by clicking anywhere next to the name of the queue.

  2. In the setting panel, toggle the **Allow transfers to Queue** to **On**.




Queue transfers permissions will be saved.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
