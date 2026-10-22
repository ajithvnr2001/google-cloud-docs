---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization/
title: Configure personalization and memory \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:17.756803+00:00
---

# Configure personalization and memory  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Configure personalization and memory Stay organized with collections  Save and categorize content based on your preferences. 

You can personalize your Gemini Enterprise experience by allowing it to securely learn from your work. Personalization enables Gemini Enterprise to anticipate your needs, help you find information, and take action more efficiently.

This document explains how personalization works, how you remain in control of your data, and how you can provide specific details and enable data sources for personalization.

## Overview

As you use Gemini Enterprise, it builds a personal _Memory_ by understanding your individual needs and work patterns, leading to more relevant and context-aware assistance. When you connect your work applications, such as Microsoft Outlook and Microsoft OneDrive, Gemini Enterprise can extract insights from your email, calendar, and documents to provide deep contextual assistance.

### Key features unlocked by personalization

Personalization transforms Gemini Enterprise into a powerful work assistant that understands you and your projects.

Feature | Description | Examples  
---|---|---  
**Understand your close collaborators** |  Instantly recall recent interactions and shared work with collaborators, as Gemini Enterprise scans recent emails, calendar, and documents to find relevant communications and files. |  Try the following prompts:

  * "What have my `COWORKERS` and I discussed recently?"
  * "Help me prepare for my 1:1 with my manager."

  
**Track your projects and topics** |  Gemini Enterprise can synthesize updates from recent related activity across all of your connected apps. |  Try the following prompts:

  * "What's the latest on Project Nova?"
  * "What are my priorities for today?"

  
**Gain insights from your information and session history** |  Never lose track of a recent decision or action item. Get answers formatted to your reading preferences and relevant to your location. Gemini Enterprise remembers your recent conversations and infers stylistic preferences and location. |  Try the following prompts:

  * "What are some notable upcoming industry events in the next few months?"
  * "What's a challenging weekend project that combines my interests?"

  
  
### Data control

Gemini Enterprise is built with privacy and transparency at its core. You're always in control of your personal information.

  * **User personalization profile** : A dedicated profile section lets you explicitly define your name, role, and industry, giving you more direct control over how Gemini Enterprise communicates with you.

  * **Manage connected sources** : You can view and disconnect any connected application from a central list at any time. If a source is disconnected, Memory no longer gathers insights from it.

**Note:** Changes to connected data sources may take up to 24 hours to take effect.
  * **Manage saved memories** : You can choose whether to allow Gemini Enterprise to reference your specifically saved memories in conversations. You can also review and remove one or all of your specifically saved memories at any time.

  * **Admin controls** : For enterprise users, administrators can manage which data sources can be connected and can disable Memory and personalization profiles for all users. By default, Memory is turned on to provide a helpful experience from the start.




## Add information to memory

In addition to what Gemini Enterprise learns from your interactions, you can build the memory by completing your profile, connecting data sources, and saving specific information as memories.

### Edit your profile

To tailor how Gemini Enterprise responds to your questions, you can provide specific details about your role and preferences. This information helps Gemini Enterprise understand your context and provide more relevant and helpful answers.

To edit your profile, follow these steps:

  1. Navigate to your Gemini Enterprise app.

  2. Navigate to the personalization settings dialog:

     * If you are a new user, click **Authorize Now** to authorize Gemini Enterprise to connect to your apps.

     * If you have already authorized Gemini Enterprise to connect to your apps, click **Settings > Personalization**.

![Edit your profile details.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/personalize-profile.png)Edit your profile details 
  3. In the **Profile** section, enter the following information. This information helps the assistant generate more relevant answers:

     1. For **Preferred name** , enter the name you'd like the assistant to use when responding to your queries.

     2. For **Your role or job title** , enter your job title.

     3. For **Your industry** , select the industry you work in.

Your settings are automatically saved.

  4. Close the **Settings** dialog.




### Add conversation history and data sources

You can allow Gemini Enterprise to learn from your past conversations, enabling more relevant responses. You can also choose to connect specific data sources to enhance the memory.

To enable learning from your conversation history and connect your data sources, do the following:

  1. Navigate to your Gemini Enterprise app.

  2. Click **Settings > Personalization**.

  3. Under **Memory** , enable Gemini Enterprise to learn from your past conversations by clicking the **Conversation history** toggle to the on position.

![Enable learning from conversation history and connected data sources.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/personalize-data-sources.png)Enable learning from your conversation history and connected data sources 
  4. To connect a listed data source, click the toggle for the data source to the on position.

Your settings are automatically saved.

  5. Close the **Settings** dialog.


**Note:** If your administrator has connected your Gemini Enterprise app to Microsoft OneDrive or Microsoft Outlook data sources, then the toggle is in the on position by default.

### Save information as memories

To save specific information for future reference, you can ask Gemini Enterprise to remember the information. Gemini Enterprise stores that information as a saved memory, which you can view, update, or delete.

#### Enable use of saved memories

To allow enhanced responses from the assistant using saved memories, you must configure Gemini Enterprise to reference your memories in conversations.

To enable use of saved memories, do the following:

  1. Navigate to your Gemini Enterprise app.

  2. Click **Settings > Personalization**.

  3. Under **Reference saved memories** , click the toggle to the on position.

![Enable learning from your saved memories.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/personalize-manage-saved-memories.png)Enable learning from your saved memories 



#### Save an item of information as a memory

You can save information as a memory in conversation with the assistant.

  * In the chat box, enter a prompt using the word "remember":
        
        Remember that all new proposals for Project Walby should be reviewed by
        @Roberto Moreno.
        

In response to this prompt, Gemini Enterprise produces output similar to the following:

> Got it! I'll keep that in mind for any future conversations.
> 
> I created a new memory: All new proposals for Project Walby should be reviewed by rmoreno@cymbalgroup.com.
> 
> I've saved those for you in your saved memories.




#### View your saved memories

You can view a list of your saved memories by asking the assistant, or in the **Settings** dialog.

##### Using the assistant

To view your saved memories using the assistant, do the following:

  * Enter a prompt asking the assistant for your "saved memories" or "saved preferences":
        
        What are my saved memories?
        

In response to this prompt, Gemini Enterprise produces output similar to the following:

> Here are the memories I have saved for you:
> 
>     * **Project Walby:** All new proposals for this project should be sent to rmoreno@cymbalgroup.com for review.
>     * **Professional Development:** You're working on improving your public speaking skills this quarter.
>     * **Writing Style:** You prefer a professional, yet approachable writing style that avoids jargon and uses active voice.
>     * **Personal Preference:** You like coffee.
> 
> Let me know if you would like me to add, change, or remove any of this information.




##### Using Settings

To view your saved memories in the **Settings** dialog, do the following:

  1. Navigate to your Gemini Enterprise app.

  2. Click **Settings > Personalization**.

  3. Under **Managed saved memories** , click **Manage**.

![View your saved memories.](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/personalize-saved-memories.png)View your saved memories 



#### Update a saved memory

You can update a saved memory in conversation with the assistant.

  * In the chat box, enter the updated memory:
        
        Remember that my favorite color is green.
        

In response to this prompt, Gemini Enterprise produces output similar to the following:

> Got it! I'll keep that in mind for any future conversations.
> 
> I updated an existing memory: My favorite color is green.




## Remove information from memory

The core memory feature is enabled by default. You can't disable the memory feature, but you can opt out of providing information from connected data sources, disable use of your saved memories, or delete saved memories.

### Remove conversation history or data sources

You can prevent Gemini Enterprise from learning using your past conversations, or remove specific data sources, using the toggles in the **Settings** dialog.

To turn off learning from your past conversations or remove a specific data source from the Gemini Enterprise memory, do the following:

  1. Navigate to your Gemini Enterprise app.

  2. Click **Settings > Personalization**.

  3. Under **Memory** , disable learning from your past conversations by clicking the **Conversation history** toggle to the off position.

  4. To disconnect a listed data source, click the toggle for the data source to the off position.

**Note:** It takes up to 24 hours for a change to a data source to take effect in Gemini Enterprise.

Your settings are automatically saved.

  5. Close the **Settings** dialog.




### Disable use of saved memories

You can prevent Gemini Enterprise from referencing your saved memories in your conversations.

To disable referencing of your saved memories, do the following:

  1. Navigate to your Gemini Enterprise app.

  2. Click **Settings > Personalization**.

  3. Under **Reference saved memories** , click the toggle to the off position.




### Remove saved memories

You can remove a saved memory using the assistant, or remove one or all of your saved memories in the **Settings** dialog.

**Important:** After you delete a saved memory, the information in that saved memory might still be retained as long as the original conversation is saved. To completely remove the saved memory, delete that conversation as well. For information about managing your conversation history, see [Manage your chat history](https://docs.cloud.google.com/gemini/enterprise/docs/assistant-organize#manage-your-chat-history).

##### Using the assistant

To remove a saved memory using the assistant, ask the assistant to "Forget" or "Remove from memory".

  * In the chat box, enter a prompt such as the following:
        
        Forget my memory about Project Walby proposals.
        

In response to this prompt, Gemini Enterprise produces output similar to the following:

> Got it! I'll keep that in mind for any future conversations.
> 
> I deleted an existing memory.




##### Using Settings

To remove one or all of your saved memories in the **Settings** dialog, do the following:

  1. Navigate to your Gemini Enterprise app.

  2. Click **Settings > Personalization**.

  3. Under **Managed saved memories** , click **Manage**.

  4. In the **Saved memories** dialog, click the delete icon next to a memory to delete it.

  5. To delete all saved memories, click **Delete all**.


**Note:** If you delete saved memories in the **Settings** dialog, you may need to start a new conversation with the assistant for your changes to take effect.

## Turn off personalization and memory

If you are an administrator, you can turn off memory and personalization profiles for all users within your organization.

To disable memory and personalization profiles for all users, do the following:

  1. In Gemini Enterprise, go to the [**Gemini Enterprise** page](https://console.cloud.google.com/gemini-enterprise/).

  2. Choose your Gemini Enterprise app.

  3. Click **Configurations > Feature Management** tab.

  4. To turn off personalization and memory, click **Memory and customization**.

This setting is turned on by default.

  5. Click **Save**.




## Troubleshooting

This section addresses common issues when configuring personalization or connecting data sources for Gemini Enterprise.

### Resolve "Error during authorization"

When attempting to enable personalization or connect data sources, you might encounter an `"Error during authorization"` message. To resolve this error, try the following solutions:

  * **Resolve[Advanced Protection Program](https://support.google.com/accounts/answer/7519408/) blocks**: If you are enrolled in Google's Advanced Protection Program, third-party authentication requests might be restricted. Your Google Workspace Super Administrator must manually mark the Gemini Enterprise OAuth client as trusted in the Google Admin console under **Security > Access and data control > API controls > Manage App Access**.
  * **Disable ad blockers and browser extensions** : Ad blockers or other privacy extensions might block the dialog required for authorization. Try temporarily disabling them or attempting the authorization in an Incognito (private) browser window.
  * **Clear cache and cookies** : Browser cache issues might cause the authentication flow to fail. Clear your browser's cookies and cached files before trying again.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
