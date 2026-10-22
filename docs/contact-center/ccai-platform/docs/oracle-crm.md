---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/oracle-crm/
title: Oracle CRM \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:01.344006+00:00
---

# Oracle CRM  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/oracle-crm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Oracle CRM Stay organized with collections  Save and categorize content based on your preferences. 

The Oracle CRM integration offers the following:

  * Automatic CRM record updates through seamless real-time data exchange.

  * Call records, chat transcripts, consumer uploaded media files, session metadata, and any passthrough custom data are uploaded to Oracle CRM.

  * Agent adapters can be accessed by signing in to the CCAI Platform portal.




## Prerequisites

  * Account with access to Oracle Service Cloud

  * User with an administrator role assigned in the CCAI Platform portal to access developer settings




## Create a profile in Oracle Service Cloud

  1. Sign in to Oracle Service Cloud using an account with administrator permissions.

  2. Click the **navigation** icon and select **Configuration** from the drop-down menu.

  3. Navigate to **select management** > **profiles**.

  4. On the **profiles** tab, select an existing administrator profile.

  5. Right-click and select **copy**.

  6. On the new profile, click the **agent browser UI extensions** tab and make sure that **UJETCall** and **UJETChat** are selected.

  7. Navigate to the **home menu** at the top of the screen and click **save & close**.

  8. On the **profiles** tab, click **home** > **refresh** to see the new profile in the list.




## Add profile settings

  1. In the navigation menu, navigate to **site configuration** > **add-in manager**.

  2. On the **add-in manager** tab, expand the **agent browser UI extensions** menu and select **UJET Call**.

  3. On the **add-in details** screen, navigate to the **extension files** list and select **`call_config.json`**.

  4. Navigate to the **home** menu at the top of the screen and click **profile access**.

  5. On the **add-in access - edit** screen, select the new profile from the **profiles allowed to access** list.

  6. In the **server configuration properties** list, double-click on the value you want to update and enter the new value.

  7. Navigate to the **home** menu at the top of the screen and click **save**.

  8. Select **UJET Chat** from the **agent browser UI extensions** menu and select `chat_config.json`.




## Add users

**Note:** Users cannot be shared. Each user needs to use their own user account.

  1. In the **navigation** menu, navigate to **staff management > staff accounts by profile**.

  2. Navigate to the **home** menu at the top of the screen and click **new**.

  3. Create the new user on the **account details** screen.

  4. Click the **profile** field, and then select the profile you created in the previous section from the **profiles** window.

  5. Click **Ok**.

  6. Click **Change password** to set the password for this user and then click **Ok**. 

**Note:** This password is not automatically compatible for use with the REST API call. You may need to change the password to conform to the REST API password requirements.
  7. Navigate to the **home** menu at the top of the screen and click **save**.




## Configure Oracle CRM in Contact Center AI Platform (CCAI Platform)

Set up an initial connection between CCAI Platform and Oracle by finding the required domain information and adding it into the CCAI Platform portal.

To configure Oracle integration, the administrator must locate the following parameters:

  * Oracle Interface Name
  * Oracle API Username and Password



## Enter interface name into Developer Settings

  1. Sign in to Oracle Service Cloud online.

  2. Copy the **Oracle Interface Name** from the browser URL.

  3. Sign in to the CCAI Platform portal using an account with **admin** permissions assigned.

  4. Navigate to **settings > developer settings**.

  5. Navigate to the CRM section and select **Oracle** as the agent platform.

  6. In the **Oracle Interface Name** field, paste the URL you copied in a previous step.

  7. Enter the email address of the administrator user in the **Oracle API** username field.

  8. Enter the password for the administrator user in the **Oracle API** user password field.

  9. Select the **default user** checkbox to use this administrator account when creating or updating records.

  10. Select the phone number format from the **phone number format** list to specify the format used for phone number lookups and how the phone number is formatted in the Oracle CRM record.

  11. Select the **custom user ID** fields checkbox to use the default user identifier from the Mobile or Web SDK when searching for a user in the CRM.

  12. Select the **attach session metadata files to CRM records** option to include the session metadata file as part of the record in Oracle CRM.

The session metadata file includes detailed information about a session and is sent as a JSON file approximately 15 minutes after the session ends.

  13. Click **save**.




## Embed the agent adapter

The Oracle CRM integration doesn't include an agent adapter package out of the box. However, using the following example code, you can deploy the agent adapters in Oracle by utilizing an iFrame on any web page. You can also customize the size of the adapters in the iFrame.

## Call adapter sample code
    
    
    <html>
    <head>
    <style>
    body {
    margin: 0
    }
    </style>
    </head>
    <body>
    <iframe src="https://instance.domain.co/agent/?type=call&from-crm_type" width="290" height="600" style="border:1px solid gainsboro;" scrolling="no" frameborder="0" allowtransparency="true" allow="microphone; camera; geolocation" noresize>
    </iframe>
    </body>
    </html>
    

## Resize the iFrame

You can increase the size of the iFrames by modifying the width in the browser. To do this, go to **Developer Tools > Console** and locate the width value using the following strings:

  * **Call adapter** : `document.getElementsByClassName("jt-agent-call-widget component")[0].style.width = '350px';`

  * **Chat adapter** : `document.getElementsByClassName("jt-agent-chat-widget component")[0].style.width = '600px';`


**Note:** You can also directly adjust the width in the appropriate `div` tag, for example: `jt-agent-call-widget component`, or `jt-agent-chat-widget-component`.

## Adjust the chat adapter

The chat adapter can scale narrower or wider without any display issues.

**Note:** Any additional height beyond 590 px will just be empty space at the bottom of the adapter.

## Adjust the call adapter

The maximum recommended width of the **call adapter** is 350 pixels. If you assign a width greater than the recommended size, the adapter still works, however, vertical lines appear on the portion of the adapter exceeding 350 pixels. The **dial pad** display and **call** and **cancel** buttons on the outbound call screen appear broken but still function.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
