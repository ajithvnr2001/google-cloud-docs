---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage/
title: External storage \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:24.502471+00:00
---

# External storage  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  External storage Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) doesn't store [session metadata](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-session-metadata), call recordings, chat transcripts, or any files uploaded by the end-user during a session. To store these types of data, you can use CCAI Platform's external storage capability. With external storage, you can save data to a Cloud Storage bucket or a Secure File Transfer Protocol (SFTP) server.

## Cloud Storage

[Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) provides features such as customer-managed encryption, lifecycle management, and aging and retention policies. These features can help you meet legal and regulatory requirements. For more information about CMEK, see [Customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys).

### Before you begin

To set up external storage with Cloud Storage, you must have the following:

  * A Google Cloud [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) with the `Storage Object Admin` role. For more information, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create). 
  * A JSON service account key. You use this key in [Set up external storage with Cloud Storage](https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage#set-up-cloud-storage). For more information, see [Create a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating). **Important:** Follow Google Cloud's [Best practices for managing service account keys.](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)



### Configure external storage with Cloud Storage

To configure external storage with Cloud Storage, follow these steps:

  1. Sign in to the CCAI Platform portal using administrator credentials.

  2. Click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Developer Settings**.

  3. Go to the **External Storage** pane, and then click the toggle to the on position.

  4. For **Server Setup** , click **Google Cloud** , and then click **Service Account (Bucket Owner)**.

  5. For **Bucket Name** , enter the name of the Cloud Storage bucket where you want to set up external storage.

  6. For **Key (JSON File)** , click **Upload key** , go to the service account key that you want to use, and then open it.

  7. If you want to save your session data to a specific folder in your Cloud Storage bucket, enter the path to the folder in the `https://storage.googleapis.com/storage/v1/b/o/` field.

  8. Select the checkboxes next to the types of data that you want to store.

  9. Optional: For **Email** , clear the checkboxes for the types of email data that you don't want to store in external storage. Checkboxes are selected by default.

  10. Optional: For **Email** , edit the path for a type of email data. This changes the folder in your SFTP server where that type of email data is stored.

  11. Optional: For **CRM Storage** , select the **Also send (selected) session files to the CRM** checkbox if your instance is integrated with a CRM and you want to send session files to it.

  12. For **Multiple Call Recordings** , click one of the following:

     * **Merge** : if you want multiple segment recordings for a call to be merged into a single file.

     * **Separate** : if you want multiple segment recordings for a call to be saved as separate segment files. 

  13. Click **Save**.




## SFTP storage

You can also set up external storage using an SFTP server.

To set up external storage using an SFTP server, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Developer Settings**.

  2. Go to the **External Storage** pane, and then click the toggle to on position.

  3. Select **SFTP Server**.

  4. In the **Host** field, enter the URL or IP address of the SFTP server.

**Important:** If you plan to [set up private egress](https://docs.cloud.google.com/contact-center/ccai-platform/docs/private-egress) from your instance, enter a URL. If you enter an IP address, private egress will be blocked.
  5. In the **Port** field, enter the TCP port number that the SFTP server accepts connections on.

  6. In the **Login User ID** field, enter the login user ID for the SFTP server.

  7. Do one of the following:

     * If the SFTP server requires a password for authentication, enter it in the **Password** field.

     * If the SFTP server requires a private key for authentication, select the **SSH Private Key** checkbox and do the following:

       * In the **Private Key** field, enter the SSH private key.

       * In the **Passphrase** field, the private key passphrase.

  8. To specify a folder to store the data in, enter the folder path in the **sftp://** field. The host and port number immediately follow **sftp://**.

  9. Click **Save**.




## Dynamic folder path and file names

Dynamic external paths for external storage give you greater control over how you name and organize your call recordings, chat transcripts, voicemails, photos, videos, and co-browse files.

You can customize your storage options with unique folder paths and file naming conventions to meet your business needs. Using custom variables such as the date and session ID makes it easier to locate and identify specific recordings.

Custom variables can be specified at the time of recording to generate dynamic folder paths and file names that are unique and meaningful.

### Use variables in path and filename formats

It is possible to use variables in the folder path. Additionally it is possible to configure the filename with the path for each file as well as enable or disable whether a certain artifact (upload type) is pushed into external storage. If you prefer not to customize your file locations, the system will automatically use the default values. You can also specify a file format for each file.

Variables can be CCAI Platform data points, such as `session ID` or `session type`, or custom fields passed into an outbound dialer. Some variables can come from the outbound dialer, such as `domain ID`.

For example, a path and filename could look like this: `Company Domain Identifier\Date of call\Unique Call Identifier\Unique CallIdentifier _ Segment Start Time.wav`. The variables would be Domain ID (`{COMPANY_DOMAIN_ID}`), date when the session started (`{DATE}`), segment start time (`{SEGMENT_START_TIME}`), and session start time (`{SESSION_START_TIME}`).

This feature is backward compatible, meaning that it is possible to construct the path and filename that follows the current naming convention.

#### Variable types

Format | Example | Output  
---|---|---  
Normal | `SEGMENT_START_TIME` | `01_05_17_PM`  
Dash | `-SEGMENT_START_TIME` (note the `-` in the beginning of the variable name) | `-01_05_17_PM`  
Underscore | `_SEGMENT_START_TIME` (note the `_` in the beginning of the variable name) | `_01_05_17_PM`  
Campaign variables | `CAMPAIGN_Location` | `New-York-City` (campaign variable: New York City)  
  
### Variable and path replacement logic

Full file paths are built using the relative custom path and dynamic or static variable settings appropriate for the file type. If a variable doesn't exist or doesn't apply, an `undef` will be replaced.

  * **Example text path:** `data/{BAD_VARIABLE}/{SEGMENT_START_TIME}/custom-test/file-{SESSION_ID}`

  * **Example output:** `data/undef/01_05_17_PM/custom-test/file-123.txt`

In this examples, the extension will be added according to the file. It is not required and will be removed if supplied.




### Path parameters

Path parameters are the variables that can be used in a URL path to retrieve specific data related to a session, call, or chat.

The following path parameters are used to retrieve information related to a session, call or chat recording.

Parameter | Variable | Comment  
---|---|---  
Simple Session Type | `SIMPLE_SESSION_TYPE` | Call or chat or undef  
Session Type | `SESSION_TYPE` | Unified call or chat values  
Session ID | `SESSION_ID` | Call or chat ID  
Upload Date | `UPLOAD_DATE` | Built at upload, this is the date the upload was attempted. Format is `MM_DD_YYYY`, for example `01_31_2022`  
Upload time | `UPLOAD_TIME` | Built at upload, this is the time the upload was attempted. Format is `hh_mm_ss_AM/PM`, for example `02_20_01_AM`  
Upload Year | `UPLOAD_YEAR` | Built at upload, this is the year the upload was attempted. Format is `YYYY`, for example `2022`  
Upload Month | `UPLOAD_MONTH` | Built at upload, the is the month the upload was attempted. Format is `MM`, for example `01`  
Upload Day | `UPLOAD_DAY` | Built at upload, this is the day the upload was attempted. Format is `DD`, for example `31`  
Date | `DATE` | Built at session start time, this is the session created date. Format is `MM_DD_YYYY`, for example `01_31_2022`  
Year | `YEAR` | Built at session start time, this is the session created year. Format is `YYYY`, for example `2022`  
Month | `MONTH` | Built at session start time, this is the session created month. Format is `MM`, for example `01`  
Day | `DAY` | Built at session start time, this is the session created day. Format is `DD`, for example `31`  
Session Start Time | `SESSION_START_TIME` | Session start time. Format is `hh_mm_ss_AM/PM`, for example `02_20_01_AM`  
Segment Start Time | `SEGMENT_START_TIME` | Only available for call recordings, this is the segment start time. Format is `hh_mm_ss_AM/PM`, for example `02_20_01_AM`  
Campaign Variables | `CAMPAIGN_<VAR_NAME>` | These variables come in from the campaign. They are all appended with `CAMPAIGN_` in the CSV file headers. Spaces are changed to '_' in the variables. For example, "My Variable 1" would be converted to `CAMPAIGN_MY_VARIABLE_1`  
  
## Object types

Storage of different object types is available and can be enabled on a per object type basis. To select upload types, in the CCAI Platform portal go to **Developer Settings > External Storage**, and then select the boxes for the upload types that you want.

**Note:** Multiple file and media format options can be selected in the **External Storage** settings. However, some features might not be enabled for your account, which could lead to errors or unexpected results.

### Call recordings

These objects are audio files and can be either mp3 or wav audio files. The default path is `voice-recordings/{simple_session_type}-{session_id}`. For more information, see [Call recording](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recording).

The number of recordings per voice conversation depends on the **Merge** or **Separate** Multiple Call Recordings settings. If you select **Separate** , an audio object is created for each segment of the call—for example, the virtual agent leg and the human agent leg. An audio filename consists of the `{session_id}` value prepended with `call-` and appended with the segment value, separated by `.`. For example—`call-123.2.mp3`.

When the call is completed, the call recording objects are written to external storage

### Call transcripts

The call transcript default path is `call-transcripts/{simple_session_type}-{session_id}`. Call transcript objects are a flat text file that includes a transcription of the voice call. The transcript is only generated if the call is handled by a virtual agent or by a human agent with Agent Assist enabled.

The call transcript object is written at the completion of the call.

The following is an example of a call transcript file:
    
    
    Call ID: 207   |   2024-09-04     PDT   |   46 sec
    --------------------------------------------------
    
    [07:36:23     Virtual Agent: Virtual Agent - Test]     Thanks for calling the YouTube TV and NFL Sunday Ticket support line! Your call may be recorded for monitoring and training purposes. To best support you, which service are you calling about: YouTube TV, or Sunday Ticket? For help with other YouTube or Google products including account recovery, visit support dot google dot com.
    [07:36:44     Virtual Agent: Virtual Agent - Test]     I didn't catch that! If youâ're calling about YouTube TV, say or press 1. For help with NFL Sunday Ticket, just say or press 2.
    
    --------------------------------------------------
    
    [07:36:44     Consumer]     Sunday
    [07:36:57     Consumer]     no problem
    
    --------------------------------------------------
    
    [07:36:57     Virtual Agent: Virtual Agent - Test]     Sure! I can help with NFL Sunday Ticket. Just tell me why youâ€™re calling today.
                                                           You can say things like, help me sign up. I want information about pricing and plans. Or can't watch the game because of an error.
    
    --------------------------------------------------
    
    [07:37:10     Consumer]     agent
    
    --------------------------------------------------
    
    [07:37:10     Virtual Agent: Virtual Agent - Test]     OK, let me connect you to a member of our customer support team!
    

### Chat transcripts

The chat transcript default path is `chat-transcripts/{simple_session_type}-{session_id}`. Chat transcript objects are written to external storage at the end of the chat conversation.

Chat transcripts are provided in two different object types per chat conversation:

#### Flat file chat transcript

The first is a flat text file with `txt` extension. It contains a human-readable transcription of plain text conversation, including the participants and system events.
    
    
    Chat ID: 12   |   2024-07-02     PDT
    --------------------------------------------------
    
    [06:04:02     System]     Hi, Chat. Sorry to hear about the issue you are experiencing. Let's take a few steps together to determine how to fix it as soon as possible.
    
    --------------------------------------------------
    
    [06:05:22     Agent: Derek S.]     hi
    
    --------------------------------------------------
    
    [06:05:30     Chat User]     Hi
    
    --------------------------------------------------
    
    [06:06:03     System]     The chat is ended.
    [06:06:04     System]     End User left the chat.
    

#### JSON file chat transcript

The second is a JSON object with `json` extension. It contains a JSON object that represents the chat transcription.

The JSON object includes the following attributes:

  * **`comm_type`:** The communication type—for example, `chat`.

  * **`comm_id`:** The chat session ID.

  * **`transcript_version`:** The format version of the transcription. The current version is 1.0.

  * **`assigned_at`:** The timestamp for the start of the chat.

  * **`timezone`:** ISO timezone of the chat and associated timestamps.

  * **`entries[]`:** An array of entries in the transcript. Each entry consists of the following:

    * **`timestamp`:** A numeric value representing a Unix timestamp (also known as Unix epoch time or POSIX time).

    * **`type`:** The type of the entry. Can be the following:

    * **`text_template`:** A predefined message as part of the CCAI Platform system or associated SDK configuration.

    * **`text`:** A text message exchanged by the end-user or the agent (human or virtual).

    * **`text_notif`:** A system notification message.

    * **`notif`:** A system event.

    * **`role`:** The role of the originator of the message. This can have any of the following values:

      * **`system`:** The CCAI Platform.

      * **`agent`:** Generated by the human agent.

      * **`virtual_agent`:** Generated by the virtual agent.

      * **`end_user`:** Generated by the end-user.

    * **`user_data`:** The user data related to the agent that originated in the message. Can contain the following:

      * **`name`:** The agent name.

      * **`id`:** The internal ID of the human agent.

      * **`avatar_url`:** The avatar URL of the human agent.

    * **`body`:** The body of the message or event. This can contain the following:

      * **`type`:** Same as type in the entry object.

      * **`content`:** For a text or text_template message, contains the message text content.

      * **`lang`:** For text type entries, this is the ISO country code of the content.

      * **`status`:** The status of the chat. Applies to `notif` type only.

      * **`timeout`:** Whether the chat timed out. Applies to `notif` type only.

      * **`event`:** The event name. Applies to `notif` type only. Event names include the following:

        * **`chatDismissed`:** Chat was dismissed.

        * **`escalationAccepted`:** An escalation was accepted.

        * **`escalationDeflected`:** An escalation was deflected.

        * **`escalationStarted`:** An escalation was started.

        * **`memberLeft`:** The member left the chat.

        * **`taskVaFinished`:** The task virtual agent finished.

        * **`taskVaStarted`:** The task virtual agent started.

        * **`transferAccepted`:** Transfer accepted.

        * **`transferStarted`:** Transfer started.

        * **`transferFailed`:** Transfer failed.



    
    
    {
      "comm_type": "chat",
      "comm_id": 12,
      "transcript_version": "1.0",
      "assigned_at": "2024-07-02T06:04:22.000-07:00",
      "timezone": "America/Los_Angeles",
      "entries": [
        {
          "timestamp": 1719925442,
          "type": "text_template",
          "body": {
            "type": "text_template",
            "content": "Hi, @{END_USER}. Sorry to hear about the issue you are experiencing. Let’s take a few steps together to determine how to fix it as soon as possible."
          },
          "role": "system",
          "user_data": {
    
          }
        },
        {
          "timestamp": 1719925522,
          "type": "text",
          "body": {
            "type": "text",
            "content": "hi",
            "lang": "en"
          },
          "role": "agent",
          "user_data": {
            "name": "Derek S.",
            "id": 3,
            "avatar_url": "https://ujet.s3.amazonaws.com/default-profile.png"
          }
        },
        {
          "timestamp": 1719925530,
          "type": "text",
          "body": {
            "type": "text",
            "content": "Hi"
          },
          "role": "end_user",
          "user_data": {
    
          }
        },
        {
          "timestamp": 1719925563,
          "type": "noti",
          "body": {
            "status": "finished",
            "timeout": false,
            "event": "chatEnded",
            "type": "noti"
          },
          "role": "system",
          "user_data": {
    
          }
        },
        {
          "timestamp": 1719925564,
          "type": "noti",
          "body": {
            "memberIdentity": "end_user-10",
            "memberName": "End User",
            "event": "memberLeft",
            "type": "noti"
          },
          "role": "system",
          "user_data": {
    
          }
        }
      ]
    }
    

### Voicemails

Audio voicemail recordings are stored for calls. The default location for voicemails is `voicemails/{upload_year}/{upload_month}/{upload_day}/{simple_session_type}-{session_id}`. These files are created when the call completes.

### Chat files including photos, videos, audios and documents

The end user or the human agent can share files during a web or mobile chat session. These objects are written to external storage based on the object type:

  * **Photos:** Photo files have a default location of `media/{upload_year}/{upload_month}/{upload_day}/{simple_session_type}-{session_id}-{file_type}-{file_id}`.

  * **Videos:** Video files have a default location of `media/{upload_year}/{upload_month}/{upload_day}/{simple_session_type}-{session_id}-{file_type}-{file_id}`.

  * **Audios:** Audio files have a default location of `media/{upload_year}/{upload_month}/{upload_day}/{simple_session_type}-{session_id}-{file_type}-{file_id}`.

  * **Documents:** Document files have a default location of `documents/{upload_year}/{upload_month}/{upload_day}/{simple_session_type}-{session_id}-{file_type}-{file_id}`.




### Screen Share recordings

With Screen Share, you can record the session and write the video object to external storage. The default location is `co-browse-data/{upload_year}/{upload_month}/{upload_day}/survey-{simple_session_type}-{session_id}`.

For further details on the **Screen share** feature, refer to the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse).

### Session data feed

A session data feed captures the stream of data that is generated when events take place during a session. These events are actions taken by agents, end-users, and CCAI Platform. You can analyze session data feeds to get insights into user experience, customer engagement, agent performance, and more.

For more information, see [session data feed](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-session-data-feed).

The default location is `session-data-feeds/{upload_year}/{upload_month}/{upload_day}/{simple_session_type}-{session_id}-{lang}`. Session data feeds are written at the end of the session.

Files are generated for the languages chosen. The available languages include the following:

  * English

  * Español (MEX)

  * 日本語

  * 中文

  * 한국어

  * Türkçe

  * Deutsch

  * Français (FRA)

  * Hindi

  * Croatian

  * Italiano

  * Português

  * Español (ESP)

  * Français (CAN)

  * Romanian

  * Russian

  * แบบไทย

  * Tagalog

  * Ukrainian

  * Tiếng Việt




The file generated is a flat text file that contains the session metadata for the selected languages. A file is generated for each session in each of the selected languages. The following is an example:
    
    
    Custom data from the customer has arrived
    
    - brand: google.com
    - otherinfo: today is friday
    
    November 18, 2024, 3:48:35 PM UTC
    
    ----------------------------------------
    Chat started
    
    Messaging Inbound (Web Chat)
    - Contact Center AI Chat ID: 112
    - Language: English (US)
    - Menu: Andrew
    - Time: November 18, 2024, 3:48:35 PM UTC
    - Device: BROWSER
    
    November 18, 2024, 3:48:37 PM UTC
    
    ----------------------------------------
    Chat ended
    
    - Contact Center AI Chat ID: 112
    - Disconnected by End User
    - Time of chat: November 18, 2024, 3:49:21 PM UTC
    
    November 18, 2024, 3:49:22 PM UTC
    
    ----------------------------------------
    Dispositions
    
    - List: Dispo List
    - UJET List ID: 1
    - Agent: Amber Sudduth
    
    November 18, 2024, 3:49:24 PM UTC
    
    ----------------------------------------
    Customer rating received
    
    - Customer rating feedback received: 5
    
    November 18, 2024, 3:49:24 PM UTC
    
    ----------------------------------------
    Chat transcript uploaded
    
    Chat message history
    - External storage link: https://ccaas-instance-iwb3d6c.media.uc1.ccaiplatform.com/v1/download/523fe7d5-1d64-4f96-91ef-baef5311c28a
    
    November 18, 2024, 3:49:30 PM UTC
    
    ----------------------------------------
    CCAI Insight chat history uploaded
    
    Cloud Storage URL: gs://bucket/insights/chat_transcript/chat-112.json
    
    November 18, 2024, 3:49:31 PM UTC
    

### Session summaries

The session summary is generated when the [Agent Assist summary service](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#view-session-summaries) enabled. The metadata objects contain a JSON object for the session. The default location is `metadata/{upload_year}/{upload_month}/{upload_day}/{simple_session_type}-{session_id}`.

The file contains a JSON object and has the following attributes:

  * **`id`:** The ID of the call or chat session.

  * **`type`:** The session type. Either `Call` or `Chat`.

  * **`menu_type`:** The type of the menu access. Can be `IvrMenu` for IVR, `MobileMenu` for mobile, or `ChatMenu` for web chat.

  * **`menu_path`:** The menu path that the user navigated.

  * **`ended_at`:** The timestamp for when the session ended.

  * **`session_summary`:** The generated session summary text. This is the same content that is provided to the [agent within the wrapup notes](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#session-summarization-calls).

  * **`session_summary_sections`:** This contains the summary sections provided by Agent Assist summary service.




The following is an example session summary object:
    
    
    {
      "id": 312,
      "type": "Call",
      "menu_type": "IvrMenu",
      "menu_path": "Test",
      "ended_at": "2024-11-13T11:17:28.000-08:00",
      "session_summary": "Resolution: Yes\nInsurance Company: Insurance Company\nSituation: Customer wants to speak to someone from Insurance Company.\nReason For Cancellation: N/A\nAction: Agent transfers the call to Insurance Company.\nCustomer Satisfaction: Satisfied",
      "session_summary_sections": [
        {
          "key": "",
          "value": "Auto-generated Summary"
        },
        {
          "key": "Resolution",
          "value": "Yes"
        },
        {
          "key": "Insurance Company",
          "value": "Insurance Company"
        },
        {
          "key": "Situation",
          "value": "Customer wants to speak to someone from Insurance Company."
        },
        {
          "key": "Reason For Cancellation",
          "value": "N/A"
        },
        {
          "key": "Action",
          "value": "Agent transfers the call to Insurance Company."
        },
        {
          "key": "Customer Satisfaction",
          "value": "Satisfied"
        },
        {
          "key": "Agent",
          "value": "Andrew Harteveldt"
        }
      ]
    }
    

### Metadata JSON files

The metadata file for chat and call sessions is generated at the end of the session. The file is updated 15 minutes after the chat or call is completed. This update includes additional information such as wrap-up notes, feedback, and CSAT score. The updating of the metadata file is done by first deleting the existing object and creating a new one. Object versioning is not performed.

**Note:** In order for the metadata file to be updated post session, the IAM role Storage Object Admin is required.

The metadata objects contain a JSON object for the session. The default location is `metadata/{upload_year}/{upload_month}/{upload_day}/{simple_session_type}-{session_id}`.

For more information about the metadata JSON object, see [Session metadata file](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-session-metadata).

### Email Content

The content body cache for emails. This is only used if the email channel is enabled. The default location is `email-content/{upload_year}/{upload_month}/{upload_day}/{simple_session_type}-{session_id}-{file_type}-{file_id}`.

### Email Attachments

The attachment cache for emails. This is only used if the email channel is enabled. The default location is `email-media/{upload_year}/{upload_month}/{upload_day}/{simple_session_type}-{session_id}-{file_type}-{file_id}`.

### Email Metadata

The metadata cache for emails. This is only used if the email channel is enabled. The default location is `email-metadata/{upload_year}/{upload_month}/{upload_day}/{simple_session_type}-{session_id}`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
