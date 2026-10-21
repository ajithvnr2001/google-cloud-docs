---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-shortcuts/
title: Chat Shortcuts \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:15.167967+00:00
---

# Chat Shortcuts  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-shortcuts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Chat Shortcuts Stay organized with collections  Save and categorize content based on your preferences. 

When chatting with consumers and prospects, agents need to get to the resolution as quickly as possible, and **chat shortcuts** can be used to add repeatable phrases, steps, and solutions to chat conversations. Once added using the portal, the created shortcuts are accessible in the Agent Adapter. New shortcuts cannot be created by individual Agents and all shortcuts will be visible to all Agents.

Shortcut **Categories** allow groups of shortcuts to be accessed using a category. Categories are optional, can be customized, and there is no limit to the number of categories or shortcuts you can create. Category examples include separating languages, product sets, or types of shortcuts.

## Viewing existing shortcuts

Click **View all shortcuts** to view existing and create new shortcuts.

  1. Go to **Settings > Chat.**

  2. Click **View all shortcuts** in the Chat Shortcuts section.




## Download shortcuts list as csv file

Click the **Download** button 

  1. Optionally, select a category from the existing category list, or type in a new category and click **Create[category name]** to save.

  2. Enter the **Shortcut Keyword**. Agents will enter this keyword to access the associated message in the Agent Adapter.

  3. Enter the **Message** as you would like it to appear in the chat conversation.

To add content with line breaks, use SHIFT+Enter in the Shortcut Message body.

Emoji and other symbols can be used. The example shows how to enter bullet points as a shortcut and also how that shortcut will show in the chat window.

  4. Optionally, click **Add Attributes** to add variable data to the message.

**Important Note** : if the consumer does not need to login to chat with your agents, the first. last, and full name variables won't be available. If a variable is included in an existing shortcut and used, "Customer" will replace the value.

     * **First Name** : Populates the first name of specified party.

     * **Last Name** : Populates the last name of specified party.

     * **Full Name** : Populates the first and last name of specified party.

     * **Queue** : Populates the name of the queue selected by the consumer.

     * **Alias** : Populates the agent alias.

  5. To add hyperlinks to the message body, use the following link structure:

     * Text format structure to open link in the same tab:

`{www.yourcompany.co | Click on this link | same_tab}`

     * Text format structure to open link in a new tab:

`{www.google.com | Click on this link | new_tab}`

  6. Click **Save**.




## Add a chat shortcut

To add a chat shortcut, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Chat**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Chat Shortcuts** pane, and then click **View all shortcuts**. The **Chat Shortcuts** page appears.

  3. Click **Add Shortcut**.

  4. Optional: In the **Category** field, select or create a category for the shortcut.

  5. In the **Shortcut Keyword** field, enter the shortcut keyword.

  6. In the **Message** field, enter the message for your chat shortcut. Use the formatting toolbar to format your message or add links and emoji. To add line breaks, use **SHIFT+Enter** in the shortcut message body.

  7. Optional: To add attributes to your message, do the following:

     1. Click **Add Attributes** , and then click an attribute that you want to include in your message. If the end-user doesn't need to sign in to chat with your agents, the first, last, and full name variables aren't available. If a variable is included in an existing shortcut and is used, "Customer" will replace the value. The following variables are available:

        * **Customer Attributes** :

          * **First Name** : the end-user's first name

          * **Last Name** : the end-user's last name

          * **Full Name** : the end-user's full name

        * **Agent Attributes** :

          * **First Name** : the agent's first name

          * **Last Name** : the agent's last name

          * **Full Name** : the agent's full name

          * **Alias** : the agent's alias

          * **ID** : the agent's ID

        * **Session Attributes** :

          * **Queue** : the assigned queue
     2. Repeat this step to add more attributes.

  8. Click **Save Shortcut**.




## Agent Experience

  1. From the Chat Adapter, press **#** to access a specific category of shortcuts, or **/** to access a specific shortcut.

  2. Enter the **keyword** or some phrases from the shortcut. Search for the shortcut requires entering the same word order - if 2 words in a shortcut are searched out of order, the search won't narrow down.

  3. Select the shortcut with a click of your mouse or press **Enter** on your keyboard.

  4. View all available shortcuts by clicking **Chat Shortcuts**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
