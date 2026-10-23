---
url: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-use-actions/
title: Extend the assistant with actions \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:32.999107+00:00
---

# Extend the assistant with actions  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-use-actions/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Extend the assistant with actions Stay organized with collections  Save and categorize content based on your preferences. 

With assistant actions, you can ask the assistant to perform tasks for you in other applications, like scheduling a meeting in Google Calendar or sending an email in Gmail. This lets you handle relatively low-effort tasks efficiently, freeing you up for other work that requires more involvement.

See the following sections for information about available actions.

**Note:** The actions available to you depend on which services your administrator has configured. If you don't see an option you expect, contact your organization's administrator.

## Authorize your connected services

Before you can use actions in the assistant, you must authorize the specific connected service to act using your account.

To authorize actions for a service:

  1. In the chat box, click the table_rows **Manage your data** icon.

  2. Find the service you want to authorize, and click **Enable actions**.

  3. Sign in to the service if necessary, and follow the prompts to authorize it.

![Authorize a connected service](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/assistant-actions-authorize.png)Authorize a connected service 



After you authorize the connected service, you can ask the assistant to perform actions using that service on your behalf.

## Schedule an event in Google Calendar

If your administrator has configured Google Calendar actions, you can ask the assistant to create Google Calendar events for you.

To create an event, do the following:

  1. Ask the assistant to schedule the event, providing some basic information. For example, you can say, "Schedule a meeting with Amal, Charlie, and Kim at 3 PM tomorrow."

  2. Edit the draft event created by the assistant.

![Schedule an event in Google Calendar](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/assistant-google-calendar-event.png)Provide event details to the assistant 

Enter any of the following for your event:

Field | Description  
---|---  
**Attendees** | A list of email addresses for everyone who should be invited. You're automatically included.  
**Title** | The name of the event.  
**Start time** | When the event begins.  
**Duration** | How long the event lasts. The default is 30 minutes.  
**Time zone** | The time zone for the event. If you don't specify one, your own time zone is used.  
**Description** | Any additional information about the event.  
  3. If you have not previously used the assistant to manage Google Calendar, click **Authorize** to grant the necessary permissions.

**Note:** The first time that you use the assistant to manage your Google Calendar, you might be asked to grant permissions for both Google Calendar and Gmail. Gemini Enterprise uses a single connection for both tools, so you only have to grant permission once. Approving this request allows the assistant to help you with both your calendar and email seamlessly.
  4. Click **Send**. The assistant creates the event in Google Calendar and sends an email to your selected attendees.




## Send an email in Gmail

If your administrator has configured Gmail actions, you can ask the assistant to send emails for you.

To create and send an email, do the following:

  1. Ask the assistant to send the email, providing some basic information. For example, you can say, "Send an email to Ariel and ask about the status of the design revisions. CC Izumi and Tristan."

  2. Edit the draft email created by the assistant.

![Send an email in Gmail](https://docs.cloud.google.com/static/gemini/enterprise/docs/images/assistant/assistant-gmail-email.png)Provide email details to the assistant 

Enter any of the following for your email:

Field | Description  
---|---  
**To** | A list of everyone who should receive the email.  
**Subject** | The subject line of the email.  
**Content** | The body of the email, which can be in Markdown format.  
**CC** | A list of anyone who should be CC'd on the email.  
**BCC** | A list of anyone who should be BCC'd on the email.  
  3. If you have not previously used the assistant to manage Gmail, click **Authorize** to grant the necessary permissions.

**Note:** The first time that you use the assistant to manage your Gmail, you might be asked to grant permissions for both Gmail and Google Calendar. Gemini Enterprise uses a single connection for both tools, so you only have to grant permission once. Approving this request allows the assistant to help you with both your email and calendar seamlessly.
  4. Click **Send**. The assistant sends the email to your selected recipients.




## Usage limits

Gemini Enterprise app displays the **Usage limit reached** error message when you chat with the assistant or use Gemini Enterprise features in either of the following scenarios: 

  * Your project reached its monthly spend cap.
  * Your project exceeds its pooled quota limit for a specific feature and your Gemini Enterprise administrator hasn't enabled overages. 



This error affects only the feature that reached its limit. You can continue using other features that have remaining quota. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
