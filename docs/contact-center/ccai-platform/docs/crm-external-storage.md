---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage/
title: Set up external storage for CRMs \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:43.530613+00:00
---

# Set up external storage for CRMs  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Set up external storage for CRMs Stay organized with collections  Save and categorize content based on your preferences. 

With Contact Center AI Platform (CCAI Platform), you can use external storage to store and retrieve CCAI Platform session data such as call recordings, chat transcripts, media files uploaded by end-users, email transcripts, and session metadata. These files are stored outside of your CRM, and you can link them to your CRM records. Files are encrypted during transit. Setting up external storage is helpful if you have a CRM that does not have a standard integration with CCAI Platform.

## File types and naming conventions

The following table shows the file types that can be stored in external storage, as well as the naming convention for the various file types:

File type | Naming convention  
---|---  
Call recordings | \- `call-{id}.mp3`  
\- `call-{id}.wav`  
Chat transcripts | \- `chat-{id}.txt`  
Media files | \- `call-{id}-photo-{photo-id}.jpg`  
\- `call-{id}-video-{video-id}.mp4`  
\- `chat-{id}-photo-{photo-id}.jpg`  
\- `chat-{id}-video-{video-id}.mp4`  
Email transcripts | \- `email-{id}.pdf`  
Session metadata | \- `metadata-{id}.json`  
\- `metadata-{id}.txt`  
  
## Storage types

You can use the following storage types for external storage:

  * Cloud Storage

  * SFTP server




## Before you begin

To set up external storage for your CRM, you need the following:

  * A CCAI Platform account with administrator and agent roles

  * Access to your CRM

  * A Cloud Storage bucket or a secure file transfer protocol (SFTP) server, depending on the type of external storage you are setting up




## Set up external storage using Cloud Storage

To set up external storage using Cloud Storage, follow these steps:

  1. Sign in to the CCAI Platform portal using administrator credentials.

  2. Click menu **Menu** , and then click **Settings > Developer Settings**.

  3. Go to the **External Storage** pane, and then click the toggle to the on position.

  4. For **Server Setup** , click **Google Cloud** and then click **Service Account (Bucket Owner)**.

  5. In the **Bucket Name** field, enter the path to your Cloud Storage bucket.

  6. In the **Key (JSON File)** field, click **Upload key**. Select a key file for a service account that has write permissions to the Cloud Storage bucket.

  7. If you want to save your session data to a specific folder in your Cloud Storage bucket, enter the path to the folder in the `https://storage.googleapis.com/storage/v1/b/o/` field.

  8. Select the checkboxes next to the types of data that you want to store.

  9. Optional: For **Email** , clear the checkboxes for the types of email data that you don't want to store in external storage. Checkboxes are selected by default.

  10. Optional: For **Email** , edit the path for a type of email data. This changes the folder in your SFTP server where that type of email data is stored.

  11. Click **Link & Save**.




## Set up external storage using an SFTP server

To set up external storage using an SFTP server, follow these steps:

  1. Sign in to the CCAI Platform portal using administrator credentials.

  2. Click menu **Menu** , and then click **Settings > Developer Settings**.

  3. Go to the **External Storage** pane, and then click the toggle to the on position.

  4. For **Server Setup** , click **SFTP Server**.

  5. In the **Host** field, enter the URL or IP address for your SFTP server.

  6. In the **Port** field, enter the port number for your SFTP server.

  7. In the **Login User ID** field, enter the user ID for signing into your SFTP server.

  8. In the **Password** field, enter the password for signing into your SFTP server, if one is required.

  9. If your SFTP server requires an SSH private key for authentication, select the **SSH Private Key** checkbox.

  10. In the **Private Key** field, enter the private key.

**Important:** You must use one of the key types in Accepted SSH key types.
  11. In the **Passphrase** field, enter the passphrase.

  12. If you want to save your session data to a specific folder in your SFTP server, enter the path to the folder in the `sftp://@:22/` field.

  13. Select the checkboxes next to the types of data that you want to store.

  14. Optional: For **Email** , clear the checkboxes for the types of email data that you don't want to store in external storage. Checkboxes are selected by default.

  15. Optional: For **Email** , edit the path for a type of email data. This changes the folder in your SFTP server where that type of email data is stored.

  16. Click **Save Changes**.




### Accepted SSH key types

The following SSH key types that are accepted as private keys when setting up external storage using an SFTP server:

  * `curve25519-sha256 (node v14.0.0+)`

  * `curve25519-sha256@libssh.org (node v14.0.0+)`

  * `ecdh-sha2-nistp256`

  * `ecdh-sha2-nistp384`

  * `ecdh-sha2-nistp521`

  * `diffie-hellman-group-exchange-sha256`

  * `diffie-hellman-group14-sha256`

  * `diffie-hellman-group15-sha512`

  * `diffie-hellman-group16-sha512`

  * `diffie-hellman-group17-sha512`

  * `diffie-hellman-group18-sha512`

  * `diffie-hellman-group-exchange-sha1`

  * `diffie-hellman-group14-sha1`




## Configure CRM comments

When you integrate with a CRM and save call recordings and chat transcripts to external storage, you can control how the recordings and transcripts are referenced in the CRM record. You can configure CCAI Platform to do one of the following:

  * Add a call recording or chat transcript link as a comment in the CRM record.

  * Add the call recording or chat transcript filename as a comment in the CRM record.

  * Don't add any reference to the call recording or chat transcript in the CRM record.




This is available with the following CRMs:

  * Custom CRMs

  * Freshdesk

  * Kustomer

  * Microsoft Dynamics

  * ServiceNow

  * Salesforce

  * Zendesk




### Configure how a call recording is referenced in the CRM record

To configure how a call recording is referenced in the CRM record, do the following:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **CRM Comments Creation Details**.

  3. For **Post call recording link to CRM record** , select one of the following:

     * **Add the call recording link as a comment**

     * **Add only the filename for the call recording as a comment**

     * **Do not add any reference to the call recording**

  4. Click **Save General**.




### Configure how a chat transcript is referenced in the CRM record

To configure how a chat transcript is referenced in the CRM record, do the following:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **CRM Comments Creation Details**.

  3. For **Post chat transcript link to CRM record** , select one of the following:

     * **Add the chat transcript link as a comment**

     * **Add only the filename for the chat transcript as a comment**

     * **Do not add any reference to the chat transcript**

  4. Click **Save General**.




### Configure how a Screen Share recording is referenced in the CRM record

To configure how a Screen Share transcript is referenced in the CRM record, do the following:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **CRM Comments Creation Details**.

  3. For **Post Screen Share link to CRM record** , select one of the following:

     * **Add the chat transcript link as a comment**

     * **Add only the filename for the chat transcript as a comment**

     * **Do not add any reference to the chat transcript**

  4. Click **Save General**.




## Agent experience

During a call or chat session, photos and videos uploaded by the end-user using [Smart Actions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/smart-actions-in-session) are displayed in the agent adapter. When the session is over, agents see a link in the CRM pointing to the session recording or transcript stored on the external server.

## Configure chat transcripts

You can configure CCAI Platform to add a chat transcript to a CRM record after a web SDK or mobile SDK chat session ends. After you do this, end-users using the web SDK can [download chat transcripts](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts#websdk-chat-transcripts) during or after a chat session. Uploading chat transcripts also lets you enable the display of previous chat interactions for agents and end-users. Chat sessions aren't generated for SMS chat sessions, so end-users using SMS chat can't download chat transcripts.

A chat transcript shows a participant, a message, and a timestamp for each interaction in a chat session. For more information, see Chat transcript structure.

### Configure how chat transcripts are added to CRM records

You can configure CCAI Platform to post chat transcripts to CRM records as comments or attachments. This is a requirement for the following capabilities:

  * End-users [downloading chat transcripts](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts#websdk-chat-transcripts).

  * Agents and end-users [viewing previous chat interactions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts#previous-chats) during a chat session.




To configure how chat transcripts are added to your CRM, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Chat**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Chat Transcript** pane.

  3. Select or clear the following checkboxes. You must select at least one of these checkboxes to enable downloading chat transcripts and viewing previous chat interactions.

     * **Post the chat transcript as a comment in the record**

     * **Add the chat transcript as an attachment to the record**

  4. Click **Save Chat Transcript**.




### Enable the display of previous chat interactions

You can enable the [display of previous chat interactions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts#previous-chats) for agents, end-users, or both.

To enable the display of previous chat interactions, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Chat**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Chat Transcript** pane.

  3. Be sure that at least one of the following checkboxes is selected. For more information, see Configure how chat transcripts are added to CRM records.

     * **Post the chat transcript as a comment in the record**

     * **Add the chat transcript as an attachment to the record**

  4. For **Display previous chat interactions** , click the toggle to the on position.

  5. To specify which users to display previous chat interactions to, select one of the following:

     * **To agent and consumer**

     * **To agent only**

     * **To consumer only**

  6. Click **Save Chat Transcript**.




### Location in CRM or server

Transcripts are uploaded to the CRM or server once the chat has been completed. Transcripts can be found where the chat ID and other chat information are stored:

  * **Zendesk:** added in plain text and attached as a file to a private comment in the ticket

  * **Salesforce:** added as a file attachment as a comment or to the CCAI Platform Session Object

  * **Kustomer:** added as both a file attachment and as a comment

  * **MS Dynamics:** added as an attachment under timeline for the ticket




### Chat transcript details

The following sections outline the handling of session transcripts with CRM.

#### Timestamp formatting

The timestamps in the chat transcripts default to the timezone as set in **Settings > Support Center Details**.

The timestamps are formatted in HH:MM:SS format.

#### Participant identification

  * The participants' first name and last name initial show, if available in the system.

  * The chat support agent name includes _Agent_ before the agent's first name.

  * The full name of the agent won't be displayed anywhere in the system generated sections.

  * The full name of the end-user won't be displayed anywhere in the system generated sections.




#### Transcript styling

**Header:**

  * The transcript header contains the following:

    * The chat ID of the specific chat with a prefix "ID:".

    * The start date of the chat in the format of YYYY-MM-DD and timezone.

  * The dotted line made of 50 hyphens (-) is placed in the line right below the header.




**Body:**

  * The individual messages sent by the participants and the system.

  * Messages are chronologically ordered following the order of message exchange and include the following:

    * The exact timestamp of the message in HH:MM:SS format.

    * The name of the participant who sent the message.

    * The message sent by the participant.

    * No text case, styling, or format changes are made to the actual chat message sent by the participant.

    * All back-to-back messages from a single participant or system are stacked together to represent a message block.




#### Chat transcript structure

The following example shows the structure of a chat transcript:

![Transcript structure](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc854b55c.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
