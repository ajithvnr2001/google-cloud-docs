---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config/
title: Configure the email channel \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:18.511793+00:00
---

# Configure the email channel  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure the email channel Stay organized with collections  Save and categorize content based on your preferences. 

This guide walks you through the steps required to enable the email channel feature.

**Note:** Email channel is only available for Salesforce, Zendesk, Kustomer, and Custom CRMs.

## Enable the email channel globally

A settings page dedicated to email menu types is available in the Contact Center AI Platform (CCAI Platform) **global settings menu**.

  1. Go to **Settings > Email**.
  2. Toggle the **Email channel** switch to **ON** to enable the email channel and all of its features and functionalities. The switch is set to **OFF** by default.



## Append the session ID to email subject lines

You can configure the email channel to add an email's session ID to the subject line when an agent replies. If you turn on this setting, you can't let agents edit the subject lines in emails.

To append the session ID to email subject lines, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Email**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **General** pane, in the **Email Management** section, select the **Automatically append session information to email subject on first replies** checkbox.

  3. Click **Save**.




## Let agents edit the subject lines in emails

You can let agents edit email subject lines when replying to emails. This lets them add important information to subject lines, such as ticket numbers or case IDs, for improved tracking and organization. Editing the email subject line doesn't change the session ID. If you turn on this capability, you can't append the session ID to email subject lines. For more information, see [Edit the subject line in an email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter#edit-subject-line-in-email).

To let agents edit the subject lines in emails, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Email**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **General** pane, in the **Email Management** section, select the **Enable Subject Line Editing** checkbox.

  3. Click **Save**.




## Configure email account data storage

  1. Go to **Settings > Developer Settings > Email Account Management** and click **Manage Email Account**. You are brought to the **Email data storage** tab by default.
  2. Select a storage time period by clicking the drop-down menu in the **Data Management** section.
  3. Data must be stored in either a Cloud Storage or Amazon S3 bucket. Make your selection and enter the following information: 
     1. _Bucket name_ : Name of the destination storage bucket.
     2. _Service Account Key_ : Path to the file containing your JSON service account key.
     3. _Folder path_ : Path to the destination storage bucket.
  4. Click **Test Connection** to verify that the settings are correctly configured.
  5. Click **Add**.
  6. Click **Save** to validate the fields and save the changes.



## Add an email account

To add an email account, do the following:

  1. Go to **Settings > Developer Settings > Email Account Management** and click **Manage Email Account**. The **Email account list** tab at the top of the page displays all onboarded email accounts and includes information and actions for each:

     * Username: Username of the person associated with the account.
     * Email: Email address of the agent associated with the account.
     * Service: Displays the email service type for the account. The only service available is Generic IMAP.
     * Status: Valid or invalid, reflects the operation status of the email.
     * Actions: Lets you edit or delete each line item.
  2. Select **Add Email Account** to display the **Add Email** menu. Enter the required information in the following fields:

     * Email Service: Select Generic IMAP.
     * Email Username: Enter the username associated with the email. The username is a value assigned by your company and might be the same as the email address.
     * Incoming Server: Enter the Incoming IMAP server address associated with the email account.
     * Sender Server: Enter the Sender SMTP server address associated with the email account.
     * Email ID: Enter the email address.
     * Password: Enter the password of the email account.
  3. Optional: Select the **This is an outbound only email account** checkbox to make this an outbound-only email account.

  4. Click **Save**.




## Configure CRM record and session status management

Email communications between end-users and agents are organized into **sessions**. An email session is one single communication stream, defined the same way for **chat** and **voice** sessions. Sessions have multiple interactions, for example:

  1. Email enters queue.
  2. Email is answered by an agent.
  3. Email is transferred to another queue.
  4. Email is responded to and resolved by another Agent



CCAI Platform lets you change how email session **status** is handled as well as how much information is recorded about each session. To change the default settings, navigate to **Settings > Email > General**. The general settings page for email session configuration contains the following options:
    
    
    1. *CRM Record Management*
    1. *Session Status Management*
    

### CRM Record Management

  1. (Optional) Un-check the _Inbound Emails_ checkbox to prevent the creation of CRM tickets for incoming emails. This option is selected by default.

  2. (Optional) Un-check the _Outbound Emails_ checkbox to prevent the creation of CRM tickets for outbound emails. This option is selected by default.

  3. (Optional) _Post email body contents as comments_ : This option is selected by default. If unchecked all other information about the email will be recorded in the CRM (timestamps, agent ID, end-user ID), but the contents of the email(s) will be omitted. Following this option, there are two additional buttons to let you to choose how frequently you want email contents posted to the case associated with the session:

     1. Post comment at the end of session (default option): This option will post a comment to the CRM with email contents for the entire email thread only once, after the email session has ended.

     2. Post comment at the end of each agent reply: This option will post a CRM comment plus all email contents in the thread up to that point every time the agent sends a reply in the thread.

  4. (Optional) _Post email body contents as PDF attachments_ : This option is selected by default. If unchecked, email contents won't be added to the CRM record as PDF attachments. Following this option, there are two additional buttons to let you to choose how frequently you want email contents posted to the case:

     1. Post PDF at the end of session (default option): This option will post the CRM comment with email contents for the entire email thread once, after the email session has ended.

     2. Post PDF at the end of each agent reply: This option will post the comment plus all email contents in the thread up to that point whenever the agent sends a reply in the thread.

  5. (Optional) Check the _Attach email session metadata file_ checkbox to allow CCAI Platform to generate a session metadata file for each email session and attach it to the linked CRM ticket at the end of the session. This box is unchecked by default. If this box remains unchecked, the session metadata file won't be logged to the CRM ticket.




### Session status management

The following settings let you configure timing thresholds related to the status of each **email session**.

#### Paused to Closed

This option is enabled by default. If enabled, CCAI Platform will automatically close an email session that is in Paused status after it reaches the specified timer threshold. You can set the timer threshold in the _Threshold Timer_ field, which can be any value from 1-1000 days. The default value is 60 days.

#### Resolved to Closed

The option is enabled by default. If enabled, CCAI Platform will automatically close an email session that is in Resolved status after it reaches the timer threshold. Case status will automatically convert from Resolved to Closed. You can set the timer threshold in the _Threshold Timer_ field, which can be any value from 1-1000 days. The default setting is 30 days.

#### Active to Paused

This option is enabled by default. If enabled, CCAI Platform will automatically move Active cases to Paused status after the specified timer threshold. You can set the timer threshold in the _Threshold Timer_ field, which can be any value from 1-1000 days. The default setting is 30 days.

#### Closed to Reopened

This option is enabled by default. If enabled, CCAI Platform will automatically move a case status from Closed to Reopened if there is new activity in the case before a specified timer threshold. You can set the timer threshold in the _Threshold Timer_ field, which can be any value from 1-1000 days. The default setting is 30 days.

If this option is **disabled** , CCAI Platform will create a new email session when there is new inbound or outbound activity in the thread of a closed email session regardless of how much time has passed since the last activity.

## Configure queue and channel settings

  1. To make queue level configurations go to **Settings > Queue**.

  2. A tile for the email channel should be visible on the queue menu landing page. If it doesn't appear, make sure that the global email channel settings are [enabled](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#enable_the_email_channel_globally).

  3. Toggle the **Email** switch to **ON** to enable email messaging for end-users and the sending and receiving of email messages through the Agent Adapter.

  4. Click the **Edit/View** button to navigate to the **Queue Menu Configurations** page for email.

  5. The channel drop-down menu lists all enabled support channels. _Email_ will appear here when the email channel has been properly enabled. Select _Email_ to display the **Email Channel Queue Menu Configurations** page.

  6. The language drop-down menu lists all enabled language menus. Select a language to display the queue menu configuration specific to the selected email channel and language. The left-hand menu displays the email queue menus set up under the selected language.

  7. Select an email queue to display the queue settings for that specific menu on the right side of the page. Toggle the _Channel Settings_ switch **ON** to enable the email menu and display the mailbox for that queue in the Agent Adapter.

  8. Click the **Edit** button to open the **Queue Builder** for the email channel. For more information about adding and editing queues, refer to [Web: Add and edit queues](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#web_add_and_edit_queues).




### Channel Settings

The _Email Address_ section displays the support email addresses assigned to this queue. If no support email addresses are assigned, you will see the message "No email assigned".

  1. Click **Update email address** to display the **Email Address Assignment** page and make changes.

  2. Select the **Email Address** drop-down to display all available email addresses for the queue. Select the email address you want to assign to this queue. This selection will apply to inbound and outbound emails. The _Queue Configuration_ page will also update with the selections you make here.

  3. Click **Save** to save the changes, then click **Back to Settings**. The **Human Agents** section will appear if _Channel Setting_ is **ON** , and will display the total number of human agents assigned to the queue. If no human agents are assigned, you will see the message "No agents assigned".

  4. Click **Assign agents** to display the **Human Agent Assignment** page and make changes. Select the individuals or teams you want to assign to a specific queue. This assignment page does not support percentage allocation or cascade groups.

  5. Click **Save** to save the changes before clicking **Back to Settings**. For more information about assigning agents to queues, refer to [Setting up and assigning agents to channels and queues: IVR, Mobile, Web](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#setting_up_and_assigning_agents_to_channels_and_queues_ivr_mobile_web).

  6. Each email queue will be displayed as an email box in the Agent Adapter. All agents assigned to a specific email queue will be able receive and send emails using the Agent Adapter.




## Email auto assignment

You can configure CCAI Platform to automatically assign incoming emails to agents based on email auto-assignment rules.

### Configure email auto-assignment

To configure email auto-assignment, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Email** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, for **Automatic assignment** , click **Configure**. The **Auto assignment** pane appears.

  5. Click the toggle to the on position to turn on email auto assignment for the queue.

  6. Click the **Limit automatic assignment to agents up to [field] emails** checkbox, and then enter a number in the field to set a limit on the number of emails that can be assigned to an agent per day.

  7. Click the **Auto assign incoming emails only during queue operation hours** checkbox to prevent incoming emails from being auto assigned to agents outside of operating hours.

  8. Click the **Auto assign incoming emails only to logged-in agents** checkbox to prevent incoming emails from being auto-assigned to agents that aren't signed in.

  9. Click **Save**.




### Email auto-assignment rules

When auto-assignment is turned off, Contact Center AI Platform puts incoming emails into the queue inbox without assigning them to agents. Agents or supervisors can then manually assign emails to themselves or others.

When auto-assignment is turned on, emails coming into the queue are automatically assigned to agents based on their capacity to handle new sessions.

For information about turning on email auto assign, see Configure email auto-assignment.

#### Email types

When auto-assignment is turned on, the following email types are auto-assigned:

  * New incoming emails

  * Incoming replies to an active email session that doesn't have an assigned agent

  * Incoming replies to a closed email session that doesn't have an assigned agent




#### Agent ranking and email assignment

When auto-assignment is turned on, agents that are assigned to the queue are ranked by the number of active email sessions that are assigned to them (active email sessions are in unopened, reopened, and active statuses). The top ranked agent has the fewest number of active sessions. As each new email arrives, it's assigned to the top-ranked agent in the queue.

If two or more agents have the same number of active email sessions, then the agent with the least-recently assigned session is ranked higher.

#### Email auto-assignment limit

You can set a limit on the maximum number of emails that can be assigned to agents per day. When an agent reaches that limit, emails are no longer auto-assigned to that agent. For more information, see Configure an auto-response email.

## Email signatures

You can configure an email signature that agents can include in outbound emails. You can use variables for agent name, agent company, and agent email address to customize signatures for each agent. You configure signatures at the queue level, and only one signature can be configured per queue. For an agent who's assigned to multiple email queues, the available signature is from the queue that the email is in.

### Configure an email signature for a queue

When you configure an email signature for a queue, the signature becomes available to agents assigned to that queue. For more information, see [Start a new email session](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter#start-a-new-email-session).

To configure an email signature for a queue, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Email** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. For **Email Signatures** , click **Configure**. The **Email Signature** pane appears.

  5. Click the **Email Signature** toggle to the on position.

  6. In the text field, enter your signature. To format your signature, use the formatting bar.

  7. To insert variables that add an agent's information into the signature, do any of the following:

     * To add an agent's name, click **Dynamic Tag > Agent**.

     * To add an agent's company, click **Dynamic Tag > Company**.

     * To add an agent's email address, click **Dynamic Tag > Alias**.

  8. To insert a link, do the following:

     1. Click link **Insert link**. The **Insert/Edit Link** dialog appears.

     2. In the **URL** field, enter the URL for the link.

     3. In the **Text to display** field, enter the link text, and then click **Save**.

  9. To insert an image:

     1. Click image **Insert image**.

     2. Navigate to the image you want. The maximum image size is 200 MB.

     3. Click **Open**.

  10. Click **Save**.




## Configure an outbound-only email account

An outbound-only email account is an email account that doesn't accept responses. If you configure an auto-response email and you don't want recipients to respond to it, you can set the sender email as an outbound-only email account.

Here are some behaviors of outbound-only email accounts:

  * You can use the same outbound-only email account as the sender email for multiple auto-response emails.

  * You can't use an outbound-only email as the default email for a queue.




To configure an outbound-only email account, follow the instructions at Add an email account. Make sure to select the **This is an outbound only email account** checkbox.

## Configure an auto-response email

You can configure an auto-response email for a queue that is sent under certain conditions. For more information about when an auto-response email is sent, see Automated responses.

### Before you begin

If you want to specify the sender email for your auto-response email as an outbound-only email account, you need to Configure an outbound-only email account. Outbound-only emails prevent the recipient from responding.

### Procedure

To configure an auto-response email, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Email** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. For **Auto-response** , click **Configure**. The **Auto-response** pane appears.

  5. Click the **Auto-response** toggle to the on position.

  6. Optional: In the **Sender email** field, select an outbound-only email account if you want your auto-response emails to originate from an email account that doesn't accept responses.

  7. In the **Message** field, enter a message for your auto-response email. Use the formatting buttons as needed.

  8. Optional: Click ![The insert image button.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-insert-image.png)**Insert Image** and navigate to an image that you want to insert into the message. You can insert up to 10 images. The combined size of all inserted images can't exceed 25 MB. Click an image and drag a corner to resize it. For information about the image file types that you can insert, see Allowed file types.

  9. Optional: Click **Browse files** and navigate to a file that you want to attach to the email. You can attach up to 10 files. The combined size of all attached files can't exceed 25 MB. For information about the file types that you can attach, see Allowed file types.

  10. Click **Save**.




### Allowed file types

The following table shows the file types that you can attach to an auto-response email. The **Allowed image files** column shows the image file types that you can insert into auto-response email messages.

Image | Video | Audio | Document  
---|---|---|---  
JPEG, JPG, PNG, GIF, TIFF, RAW, WebP | MP4, MOV, AVI, WMV, WebM | MP3, WAV | PDF, DOC, XLS, PPT, CSV, TXT  
  
## (Optional) Expected automation behaviors

### Automated responses

You can configure email auto-responses for use in the following scenarios:

  * All new inbound emails that are the first emails in a thread.
  * Email replies coming into an email thread in Closed status (reopens the case).
  * Email replies coming into an email thread in Paused status (reactivates the case).
  * Email replies coming into an email thread in Active status, but has had 15 days of inactivity without a status update.



The email auto-response will always include "RE:" and the original email subject in the response. It will be recorded in the CRM ticket in the same manner as Non-automated emails.

You can configure a customized, pre-drafted automated email and pre-fill information into the response template based on the following tags:

  * `@{consumer}`: End-user first name.
  * `@{agent}`: Agent first name.
  * `@{date}`: System date.
  * `@{time}`: System time.
  * `@{queue}`: Email menu name.
  * `@{company}`: Company name.
  * `@{next_working_date}`: Next working date in HOOPS settings.
  * `@{ticket_id}`: CRM ticket ID.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
