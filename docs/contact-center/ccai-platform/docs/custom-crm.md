---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm/
title: Custom CRM \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:24:41.328955+00:00
---

# Custom CRM  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Custom CRM Stay organized with collections  Save and categorize content based on your preferences. 

The Custom CRM solution allows companies to take advantage of the Contact Center AI Platform (CCAI Platform) Portal when using a CRM that is not a current standard integration with CCAI Platform. Custom CRM configuration works when using a homegrown CRM or any non-standard CRM.

Agents handle calls and chats, and supervisors can monitor and pull reports using the CCAI Platform portal. All details about the call or chat session are stored in a session metadata file. This file can contain 20+ data points, including session information, transfers, handle duration, participants, diagnostic information, and much more. The session metadata file can be parsed and used for post-session analysis and tracking.

Session metadata and consumer-uploaded media files are pushed to an external storage service and agents are able to see consumer-uploaded media files directly in the agent adapter during the session.

A custom CRM solution is implemented with a combination of the following components. Some components may or may not apply to your configuration:

  * Generating the session metadata file for each call and chat session

  * Pushing metadata and media files to an external storage service

  * Generic API integration

  * Custom lookup URL

  * CRM record update by email

  * Account or case lookup from the agent adapter




## Prerequisites

In order to use the Custom CRM feature, you must first set up external storage. Refer to External storage for custom CRM solutions for more information.

## Session metadata

The session metadata file contains detailed information about the session. This is sent 15 mins after the session has completed. Refer to [Session Metadata File](https://docs.cloud.google.com/contact-center/ccai-platform/docs/rm-session-metadata#UUID-2556172e-903f-4dac-c0e2-02115d533b71) for more information.

## Custom CRM interaction and integration methods

| Generic API | Custom URL  
---|---|---  
Account lookup | Yes | Yes  
Case lookup | Yes |   
Case update | Yes | No  
  
### Generic API

The Generic API integration method provides the ability to use the API of your Custom CRM to establish a two-way connection with CCAI Platform. This seamless method feels the same as the out of the box CRM integration experience. The Agent does not have to take an action to create a CRM record for call or chat sessions and depending on the unique API configuration. It can enable a seamless record lookup and record update.

### Custom URL

The Custom Link option allows your agents to interact with your CRM by utilizing a custom link created for each session. Unlike the standard CRM integration and the Generic API experience, the Agent needs to take action for a CRM record to be created. In some cases this might be just launching a tab with the custom link from the session, and in other cases the Agent may need to manually create the record.

## Custom lookup URL details and configuration

The basic functionality of the URL is to perform a CRM lookup, but depending on your CRM, more complex processes can be triggered based on the custom URL content. The URL for the custom CRM can be configured with variables containing session information and is accessible in the agent adapter during the session. Once the URL is accessed, it will trigger the custom CRM to perform a lookup. This CRM lookup is how agents can make use of a "ticket pop" for the active call or chat session. The custom link process solely relies upon the custom CRM's ability to process this link and modify or rewrite it if necessary.

The externally stored session metadata, call recordings, and other files won't be tied back to the CRM record unless the Email update method listed is also leveraged.

In this configuration, the Agent will log into the CCAI Platform Portal and log into their CRM on separate tabs. Calls and chats will be handled on the CCAI Platform tab, and ticket details will be accessed on a CRM tab.

For this configuration to work:

  * The Agent must be logged in to their CRM in their browser

  * The Agent must be logged into the CCAI Platform Portal in their browser

  * The custom lookup URL must be pre-configured

  * Your CRM needs to handle the custom URL to display relevant CRM record




### Custom lookup URL behavior

  * CCAI Platform will only include parameters in the URL that are not empty.

  * CCAI Platform does not store the generated URL containing ANI/UID/Email in the CCAI Platform database once the session is finished.




### Custom lookup URL configuration

Due to varying unique identifiers and CRM capabilities and behaviors, you will need to create 2 different URLs -- one for IVR/PSTN/SMS sessions and one for web and mobile SDK sessions. IVR/PSTN/SMS sessions will use ANI as the unique identifier whereas web and mobile SDK will likely use CUID and Email.

The following variables can be used to configure a lookup URL:

Variable | Values  
---|---  
`{CUSTOMER_PHONE_NUMBER}` | The end-user's phone number  
`{ANI}` | The end-user's phone number. Retained for backward compatibility.  
`{CUID}` | Custom user ID  
`{EMAIL}` | End-user email  
`{MENU_PATH}` |  The complete queue menu path.  
For example, "Orders/Order confirmation/Order info".   
`{MENU_ID}` | Menu ID  
`{CHANNEL}` |  The session channel. Possible values:

  * chat
  * voice_call

  
`{TYPE}` |  The session type. Possible values for calls:

  * Incoming_Call_(app)
  * Scheduled_Call_(app)
  * Incoming_Call_(web)
  * Scheduled_Call_(web)
  * Outbound_Call
  * Outbound_Call_(api)
  * Incoming_Call_(api)
  * IVR_Call
  * IVR_Call_(app)
  * Voicemail

Possible values for chats:

  * Mobile
  * Web
  * SMS

  
`{SUPPORT_PHONE_NUMBER}` | The support center phone number the end-user calls.  
`{OUTBOUND_NUMBER}` | The phone number that an agent uses for an outbound call.  
`{SESSION_ID}` |  The session ID. Possible values:

  * Call ID
  * Chat ID
  * Email ID

  
`{CUSTOM_AGENT_ID}` | The optional agent ID field in the `user` object. The agent ID can't be obtained until after the session is established and an agent is assigned. For this reason, configure your instance to delay call or chat record creation to allow time for this variable to be defined. You can delay call or chat record creation at **Settings > Operation Management > CRM Record Creation Details**. For more information, see [CRM record creation details](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-record-creation#crm-record-creation-details).  
  
### CCAI Platform portal configuration

  1. Sign in to the CCAI Platform portal using an account with Admin role assigned.

  2. Go to **Settings > Developer Settings**.

  3. In the CRM section, select **Custom CRM**.

  4. Under **CRM lookup** , enter your custom URLs.

  5. Select the **Phone Number Format** to be used in CRM requests.

  6. Click **Save Changes**.

  7. If you have not already done so, configure your external storage service. For more information, see External Storage.




## CRM record update by email

In configurations like the custom lookup URL, once a session has been completed, the session metadata needs to be updated in the CRM. With this feature, CCAI Platform can automatically send session data using email. Approximately 15 minutes after as a session ends, an email is sent to a configured location and the email content is used to update a record in your CRM. This feature can be configured globally and per-queue. Once the email is received, your CRM may be configured to update or create a new CRM record for the session.

### Email details

  * Sent from [no-reply@ccaiplatform.com](mailto:no-reply@ccaiplatform.com)

  * Contains:

    * Subject line

    * Body with the session metadata in JSON syntax

    * Attachment in TXT format with chat transcript when applicable

  * The CCAI Platform will wait for 15 minutes after the session ends, then send the email.

  * Emails are sent for successfully finished sessions only. It is not sent for failed or abandoned sessions.




### Global configuration

  1. Sign in to the CCAI Platform portal using an account with Admin role assigned.

  2. Go to **Settings > Developer Settings**.

  3. In the CRM section ensure **Custom CRM** is selected.

  4. Enable **Send session outcome via Email**.

  5. Enter an email address where you would like the email to be sent.

  6. Click **Save Changes**.




### Per-queue configuration

  1. Sign in to the CCAI Platform portal using an account with Admin role assigned.

  2. Go to **Settings > Queue** and select any sub-queue.

  3. Enable **Send session outcome via Email**.

  4. Enter an email address where you would like the email to be sent.

![Email config display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23d89635.png)

  5. Click **Save Custom CRM setting.**




### Settings inheritance and overriding

Settings | Behavior  
---|---  
Global = NOT enabled  
Queue = NOT enabled | Don't send for all queues.  
Global = NOT enabled  
Queue = Enabled | The queue setting (i.e., on/off state) **overrides** the global setting.  
Email is sent from a given queue to an email address defined in the **queue** setting.  
Global = Enabled  
Queue = NOT enabled | The queue setting (email address, on/off state) **inherits** the global setting.  
Email is sent from a given queue to an email address defined in the **global** setting.  
Global = Enabled  
Queue = Enabled | The queue setting (email address) overrides the global setting.  
Email is sent from a given queue to an email address defined in the queue setting.  
If the email address is empty, then email is not sent.  
  
## Agent experience

**CRM record lookup**

  1. Sign in to the CCAI Platform portal using an account with the Agent role assigned.

  2. Open the call or chat adapter.

  3. Use the **Open in new browser window** button to trigger the lookup.

  4. Use the **Copy link** button to copy the lookup URL to clipboard.




![Agent display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23d8cfe5.png)

## External storage for custom CRM solutions

External Storage for Custom Solutions enables the use of an external storage service to store and retrieve CCAI Platform session metadata, call recordings, chat transcripts, and consumer-uploaded media files. The files are stored outside of a CRM.

In order to configure External Storage, you **must** have:

  * A valid CCAI Platform account with Admin and Agent role assigned for configuration and testing

  * An external storage service


**Note:** CCAI Platform acts as a user of the service but will **not** set up or manage your external storage.

### Folder structure

The following folder structure will be organized in your external storage in **Folder Path** :

  * ujet-chat-transcripts

  * ujet-media

  * ujet-metadata

  * ujet-voice-recordings

  * ujet-voicemails




### File formats and naming conventions

The following file types can be pushed to the external storage service. Files are encrypted during transit using HTTPS:

File | Name  
---|---  
Call recordings | \- call-{id}.mp3  
\- call-{id}.wav  
Media files | \- call-{id}-photo-{photo-id}.jpg  
\- call-{id}-video-{video-id}.mp4  
\- chat-{id}-photo-{photo-id}.jpg  
\- chat-{id}-video-{video-id}.mp4  
Chat transcripts | \- chat-{id}.txt  
Session metadata | \- call-{id}.json  
\- chat-{id}.json  
  
### Agent and supervisor experience

During the call or chat session, photos and videos uploaded by the consumer using smart actions are displayed in the agent adapter.

If you are using the custom URL CRM interaction combined with the session metadata file email update method, agents and supervisors can access session information using your external server.

## Configuring the external storage service

Complete these steps to configure your external storage:

  1. Sign in to the CCAI Platform portal using an account with the Admin role assigned.

  2. Go to **Settings > Developer Settings**.

  3. On the Developer Settings page, navigate to the **External Storage** section.

  4. Enable information storage outside CRM servers by toggling the switch to **On** , then select the types of files to be stored.

  5. In the Server Setup section, select your storage type and complete the setup steps: SFTP server, Google Cloud bucket.




### SFTP server

  1. Enter the SFTP **Host** (URL or IP address.)

  2. Enter the **Port** number.

  3. Enter the SFTP **Login User ID**.

  4. If the SFTP server requires a password for authentication, enter it in the **Password** field.

  5. If the SFTP server requires a private key for authentication, select the **SSH Private Key** checkbox.

  6. Enter (copy & paste) the SSH **Private Key**.

  7. Enter the private key **Passphrase**. If the session information should be stored in a specific folder on the SFTP server, select the **Folder Path** checkbox and enter the **SFTP folder path**.

  8. Click **Save Changes**.




### Cloud Storage

  1. Enter the destination Google Cloud **Bucket Name**.

  2. Enter Google Cloud **Client ID**.

  3. Enter the Google Cloud **Client Secret**.

  4. If the session information should be stored in a specific folder in the Google Cloud bucket, select the **Folder Path** checkbox and enter the **Google Cloud folder path**.

  5. Click **Link & Save**.




## Testing the external storage configuration

For CRMs with existing standard integration:

  1. Sign in to your CRM.

  2. Sign in to CCAI Platform within the CRM using CCAI Platform credentials with an Agent role assigned.

  3. Place a call or chat. The CRM record that is associated with the session is displayed.

  4. When the session is finished, the transcript file should be uploaded within seconds.

  5. Navigate to the external server storage folder directly and verify the file is available.




## Sending session files to the CRM

When External Storage is enabled, the CRM Storage and External Storage URLs developer settings provides the ability to send session files and decide which source to use to display files in the agent adapter.

To view these settings External Storage must be enabled at **Settings > Developer Settings > External Storage**. Toggle the **Enable information storage outside CRM servers** to **On**.

### CRM storage

  1. Go to **Settings > Developer Settings > External Storage > CRM Storage**.

  2. Check the box beside **Also send session files to the CRM** to send session files such as call recordings or chat transcripts to your CRM and to the configured external storage.

  3. Click **Save Changes**.


**Note:** If the checkbox for CRM storage is unchecked, the recordings will be stored only in the external storage and the link to the CRM will be used.

If the checkbox is checked, then the recordings will be stored in both the CRM and the external storage.

### External storage URLs

The External Storage URL is used in two places:

  * The agent adapter.

  * Reporting: displays the media URL in the report as well as in the menus such as Settings, Calls, Completed.



  1. Go to **Settings > Developer Settings > External Storage > External Storage URLs**

  2. Select the source **CRM URLs** or **External Storage URLs** to display files in the agent adapter.

  3. Click **Save Changes**.




### CRM storage

  * If the checkbox for CRM storage is unchecked, the recordings will be stored only in the external storage and a link to the CRM will be used.

  * If the checkbox is checked, then the recordings will be stored in both the CRM and the external storage.




### External storage URLs

The URL is used in two places:

  * One is showing the media in the CCAI Platform adapter. The external storage or CRM.

  * The other one is in the report. We reveal the media URL in the reports as well as in the menus such as Settings, Calls, Completed.




## Display custom CRM in CCAI Platform portal

When using the custom CRM integration with your own custom-built CRM, you can load your CRM on a dedicated page within the CCAI Platform Portal. Once enabled, the CRM tab in the CCAI Platform Portal loads and displays your custom-built CRM page. This can be configured in **Developer Settings > CRM.**

This capability allows agents to handle live support sessions using the CCAI Platform call and chat adapters while also working in your custom CRM. This includes reviewing automatically popped open account and record details and session specific files and data passed in from your mobile app or by consumers, all using the CCAI Platform portal.

**Note:** To display on the CCAI Platform portal, your CRM _must be allowed_ to be displayed inside an iframe hosted on a separate domain.

### Configure a custom CRM page

To configure a custom CRM page, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **CRM** pane, click **Custom CRM**.

  3. Click the **Display CRM in CCAI Platform portal** toggle to the on position.

  4. Under **Display URL** , enter the URL for your custom CRM page, and then click **Save**.




## Open custom URL screen pop

Use **Open Custom URL** to bring up a custom URL screen pop when a contact isn't found in the system. Create a CRM record with a temporary account ID, and trigger a custom link with parameters based on the queue level configuration.

**Note:** If the URL is not set, CCAI Platform will follow the usual lookup process and won't create a CRM record with a temporary account.

### Enable screen pop on a per queue basis

  1. Go to **Settings > Queue > IVR**, click a queue to edit.

  2. Go to **Open Custom URL** in the panel.

  3. Enter a URL to bring up a screen pop.




Include the variable parameters {ACCOUNT_ID} and {PHONE_NUMBER} into the URL.

An example is provided.

  1. Click **Save.**



## Custom CRM generic API integration

The generic API integration method provides the ability to use the API of your CRM to establish a two-way connection with CCAI Platform. This seamless method has the same feel as the out-of-the-box CRM integration experience.

The Agent does not have to take any action to create a CRM record for call or chat sessions. Depending on the unique API configuration, it can enable a seamless record lookup and record update.

### Terminology

**Term** | **Description**  
---|---  
**Account** | It is used to refer to the Account/Contact/Customer/Lead entity in the CRM. Your CRM may have another name for this entity. Accounts contain Records.  
**Record** | It is used to refer to the Case/Ticket/Conversation/Incident entity in the CRM. Your CRM may have another name for this entity. Records belong to Accounts.  
**Comment** | It is used to refer to the Comment/Note entity in the CRM. Your CRM may have another name for this entity. Comments belong to Records.  
  
### API settings

This section outlines the settings specific to the custom CRM API settings.

#### Authentication method

CCAI Platform supports three authentication methods for your CRM:

  * **Basic authentication** : Configure authentication credentials that include **Username** and **password**.

  * **Custom header** : Configure custom header key-value pairs: **Field Key** and **Field Value**. Enter as many pairs as you need.

  * **OAuth** : CCAI Platform supports the industry-standard protocol for authorization OAuth 2.0. Specify OAuth information if you need to enable the **"Include the Redirect URL as part of the Authorization URL and Token URL"** option.

Configure the following values:

    * Authorization URL (required)

    * Token URL (required)

    * Client ID (required)

    * Client Secret (required)

    * Scope

    * State

    * Access Type




#### Phone number format

Select the Phone Number Format to be used in CRM requests:

  * **Automatic** : Create: +1 222 333 4444, Search: *222*333*4444

  * **E.164** : +12223334444

  * **US Local** : 2223334444

  * **US local standard** : (111) 222-3333

  * **International** : +1 222 333 4444




#### API request timeout

Configure the **API Request Timeout** from 1-10 seconds using the drop-down. This timeout will be applied to all endpoints you configure.

#### CRM lookup URLs

Specify **lookup URLs** that will be used to point an Agent to the current account and record.

Enter lookup URLs as they appear in your CRM when you have an account or record page opened in your browser.

You can also use CRM lookup URLs with the [web SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk) and [mobile SDKs](https://docs.cloud.google.com/contact-center/ccai-platform/docs/mobileSDK-overview). You can configure the SDKs to look up CRM account and record information to display in the agent adapter. For a complete list of CRM lookup URLs, see Request URL parameters.

#### Account lookup URL

Use the **{ACCOUNT_ID}** variable to insert the actual account ID.

Example:

`https://www.example.com/contact/{ACCOUNT_ID}`

##### Record lookup URL

Use the **{RECORD_ID}** variable to insert the actual record ID.

_Example:_

`https://www.example.com/record/{RECORD_ID}`

### API endpoints

This is the most important configuration for Generic API.

  1. To make account lookup available to your agents, you have to configure the **Find an account** and **Create an account** endpoints.

  2. Additionally, you can set up **Find a record** and **Create a record** endpoints to enable record lookup or creation to your agents. Account setup from the previous step is required for this.

  3. Finally, if you enter **Update a record** , **Upload a file** , and **Comment** endpoints, it will enable record updates. Record setup from the previous step is required for this.




#### Endpoint configuration

Configure the following settings:

  1. **Request URL** : API endpoint URL.

  2. Choose the **request method** from POST, GET, PUT, or PATCH.

  3. Specify the request **Parameters**. You can use the CCAI Platform defined variables to pass the required information (see the table below). Also, you can enter plain text or numbers as parameters' values. You can add as many parameters as you need.

  4. If the endpoint is POST/PUT/PATCH, CCAI Platform offers more fine-tuned controls on how the request is built. Choose **Request Data Format** from **Property** or **Container**. It specifies the format of the request JSON.

     * **Property**. This indicates that the request object is a basic property map when CCAI Platform builds the request body from parameters.

     * **Container**. This indicates the request object data to be sent needs to be nested within a structure. Choose **Container Type** from **Map** or **Array**. Enter **Container Name**. It is used as the parent object name when building the request body from parameters.

       * Example: Map: { container_name : { ...parameters } }

       * Example: Array: {container_name : [ { ...parameters } ] }

  5. Enter **Response Data Location**. It is used to locate the target response object in the JSON response.




### Request URL Parameters

Parameter | Variable | Comment  
---|---|---  
Agent ID | `{AGENT_ID}` | The internal agent ID.  
Agent Custom ID | `{AGENT_CUSTOM_ID}` | Optional field from the user's profile.  
Agent Email | `{AGENT_EMAIL}` | The answering agent's email if applicable.  
Name of end-user | `{NAME}` |   
End user first name | `{FIRST_NAME}` | Taken from `Name`  
End user last name | `{LAST_NAME}` | Taken from `Name`, defaults to -- if missing.  
External ID | `{UJET_ID}` | CCAI Platform end-user ID  
Email | `{EMAIL}` |   
Call Type/Session Type | `{SESSION_TYPE}` |   
End user phone number | `{PHONE_NUMBER}` | Formatted using setting choice  
Call ID | `{Call_ID}` | CCAI Platform call ID.  
Chat ID | `{Chat_ID}` | CCAI Platform chat ID.  
Language | `{LANG}` |   
Custom UID | `{CUSTOM_USER_ID}` | For Mobile: this is the left-hand side of the email. For example, `test.user3` from `test.user3@test.co`  
Account ID | `{ACCOUNT_ID}` | Found by calling Find/Create contact endpoint.  
Record ID | `{RECORD_ID}` | Found by calling Find/Create record endpoint.  
Session ID | `{SESSION_ID}` | CCAI Platform session ID  
Menu path | `{MENU_PATH}` |   
Outbound phone number | `{OUTBOUND_PHONE_NUMBER}` | Formatted using setting choice  
Queue name | `{QUEUE_NAME}` |   
Queue ID | `{QUEUE_ID}` | The internal queue ID.  
SDK Name | `{SDK_NAME}` | End-user name as indicated in the Web SDK or the Mobile SDK.  
SDK Email | `{SDK_EMAIL}` | End-user email address as indicated in the Web SDK or the Mobile SDK.  
SDK Phone | `{SDK_PHONE}` | End-user phone number as indicated in the Web SDK or the Mobile SDK.  
SDK Identifier | `{SDK_IDENTIFIER}` | Identifies a Web or Mobile SDK end-user or account. Don't include PII in this property. When creating an account, this identifier is required in the request.  
SmartAction session id | `{SMART_ACTION_SESSION_ID}` |   
SmartAction: verification |  | (Coming soon)  
SmartAction: text input |  | (Coming soon)  
Rating | `{RATING}` | Only available if a user left it  
Feedback message | `{FEEDBACK}` | Only available if a user left it  
Call duration | `{CALL_DURATION}` | In mm:ss  
Hold time | `{HOLD_TIME}` | In mm:ss  
Wait time | `{WAIT_TIME}` | In mm:ss  
After call work duration |  | (Coming soon)  
Device Type | `{DEVICE_TYPE}` |   
Disconnected By | `{DISCONNECTED_BY}` |   
Channel | `{CHANNEL}` |   
Record Subject | `{TICKET_SUBJECT}` | Used as record title  
Record Description | `{TICKET_DESCRIPTION}` |   
Record Description HTML | `{TICKET_DESCRIPTION_HTML}` | Same as description just formatted for html  
Comment Body | `{COMMENT_BODY}` | Only available in add comment situation (save rating, end call/chat, call/chat started)  
File Data | `{FILE_DATA}` | Only available in the upload file endpoint, but contains the base64 or data for multipart form.  
  
### Request URL parameter functions

Functions are provided to help with dynamic CCAI Platform variables. These functions are only available for use in the **Request Parameter** section of the endpoint settings.

The resulting value created from a function will be a string. If no values are returned from the function, the parameter is removed from the parameters list in the request before execution.

Function | Function Syntax | Description  
---|---|---  
Default Value | `=DEFAULT_VALUE(val1, val2)` | Value will use `val1` unless null or empty, and default back to `val2`.  
Concatenation `Or` | `=CONCAT_OR(val1, val2, val3)` | Concatenation of multiple values with `or`. Example: 'val1 or val2 or val3'  
Concatenation `And` | `=CONCAT_AND(val1, val2, val3)` | Concatenation of multiple values with `and`. Example: 'val1 and val2 and val3'  
  
#### Examples

The following a some examples of use of the request URL parameter function.

##### Default

The following example uses `DEFAULT_VALUE` in the `Create a Record Endpoint`. The key and value for agent setup use the default function to have a fallback in case of an empty value for an agent email. Agent email may be empty on record creation for a few reasons: a customer may have ended the IVR call before an assigned agent answers the incoming call, or in the case of chats, a record will be created before an agent answers. In this way, required parameters might be defaulted to safe values until later updates or set in cases of abandoned calls.

![Edit Field](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/default-ex-2.png)

##### Concatenation

The following example uses `CONCAT_OR` in the `Find an Account by Query` endpoint. This example is specific to Zoho CRM, but shows how `CONCAT_OR` can be used. `CONCAT_AND` follows the same rules instead connecting values with `and` instead of `or`. Refer to the following cases for values present in the endpoint at the time of execution and the resulting value passed as the request parameter.

**Note:** If CCAI Platform variables are not available at the time of execution, the full string entry at that position is removed. In the first case, if only `ACCOUNT_ID` is present, the strings `Phone:equals` and `Email:equals` are ignored and not returned in the final value.

![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/concat-ex.png)

Keys present | Resulting value  
---|---  
`ACCOUNT_ID` | `(Id:equals:<uuid>)`  
`ACCOUNT_ID`, `EMAIL` | `(Id:equals:<uuid>)` or `(Email:equals:kim@example)`  
`PHONE_NUMBER`, `EMAIL` | `(Phone:equals:+12223334444)` or `(Email:equals:kim@example)`  
  
### API account

The API account endpoints support the integration with accounts in the CRM.

Calls to endpoints that return a 400 error retry. Calls that return other errors don't retry. Retries continue for a week, decreasing with an exponential ramp down. For information about API flows, see [Custom CRM generic API: Flows](https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm#custom-crm-generic-api-flows).

#### Find an account by query endpoint (formerly find an account endpoint)

This endpoint is used to find an account by phone number, email, or internal CRM ID. This is the default endpoint used for finding an account.

Example response:
    
    
    {
      "id": 123,
      "name": "Kim",
      "phone": "11234567890",
      "email": "Kim@agents.co"
    }
    

#### Find an account by ID endpoint

This endpoint is used to find an account by ID. Generally, this ID will be part of the URL. URL validation will also account for if the URL is not formed with the ID, then this endpoint won't be used. This will follow REST standards. If a 404 is returned on failed lookup, find by query will be next.

Example response:
    
    
    {
      "id": 123,
      "name": "Kim",
      "phone": "11234567890",
      "email": "Kim@agents.co"
    }
    

#### Create an account endpoint

This endpoint is used to create an account if we haven't found one. Most CRMs require records to be attached to accounts. To create a unified flow, we enforce this requirement for all CRMs.

### API record

The API record endpoints provide the ability to integrate with records or cases in your CRM.

#### Find a record by query (formerly find a record endpoint)

This endpoint is used to find a record by a criteria. Generally, this is used to find associated records to an account. If the CCAI Platform is configured to re-use existing records, then the found record will be used. This is the default endpoint used for finding a record.

Example response:
    
    
    {
      "id": 456,
      "subject": "Record title",
      "status": "open", // enumerated status open/closed, or 1,2,3
      "contactId": 123, // contact attached to ticket
      "phone": "11234567890", // contact phone
    }
    

#### Create a record endpoint

This endpoint is used to create a record. A new record is created if a record is not found from the **Find a record** request or if CCAI Platform is configured not to re-use existing records.

Example request:
    
    
    {
      "id": 123,
      "subject": "Record title", 
      "description": "A longer description of the record, can be formatted in html",
      "phone": "11234567890", // can be saved in multiple formats
      "contactId": 123,
      "sourceType": "PHONE", // PHONE/CHAT
      "menu": "queue1",
      "direction": "outgoing",
      "rating": 5, // 1-5 scale
      "feedback": "the agent was great!" // description of rating
    }
    

#### Update a record endpoint

This endpoint is used to update a record. It updates the record's title and description. This endpoint also optionally works to update the record according to CCAI Platform events, such as save CSAT rating, call or chat finish events, selected queues, verifying users, and others.

#### Upload a file endpoint

This endpoint is used to upload an attachment.

Choose the **Type** for your upload endpoint

  * **Base64 encoded form**

  * **Multipart form**




Select which files to attach

  * **Call recordings**

  * **Chat transcripts**

  * **Voicemails**

  * **Photos**

  * **Videos**

  * **Session metadata file**




Choose **Attachment Type** from **ID** and **Attachment URL**. It specifies the format of the response JSON.

  * **ID**

  * **Attachment ID.** Enter the location of a parameter in JSON response for attachment's ID. This will be available for attachment builder URL as {ATTACHMENT_ID}.

  * **Attachment Builder URL.** Enter URL to download the file attachment. **RECORD_ID** and **ATTACHMENT_ID** are available variables.

Example: `https://www.example.com/Accounts/{RECORD_ID}/Attachments/{ATTACHMENT_ID}`

  * **Attachment URL**

Enter the location of a parameter in JSON response for the file download URL.




Select the **Add comment to CRM** record checkbox if you want CCAI Platform to leave a comment to a record when a file was uploaded. The Text Format setting from the Comment endpoint will be respected for these comments.

The following example is a multipart form example using `POST/PUT/PATCH`:
    
    
    {
      "file": <file data>
      "id": 123, // optional, this can also just be part of the URL;
                 // for example https://example-customer.com/upload/record/{RECORD_ID}
    }
    

Example response:

**Note:** This depends on your backend capability. If you host a download URL for CCAI Platform use use Example A, otherwise you can also build a URL in Example B.

**Example A: A download URL exists**
    
    
    {
      "id": 123,
      "url": "https://some-hosted-url.com"
    }
    

**Example B**

In this case a download URL does not exist but there is a download attachment endpoint that uses this ID. For example, `https://www.customer-api.com/record/{RECORD_ID}/Attachments/{ATTACHMENT_ID}`.
    
    
    {
      "id": 123
    }
    

##### Comment endpoint

This endpoint is used to add a comment to a record. If the endpoint is configured, the CCAI Platform Platform will add comments to records with the events:

  * call or chat start

  * call or chat end

  * CSAT rating and comment

  * custom data package

  * transfer comments

  * disposition code and notes

  * survey questions and answers




Choose **Text Format** for comments. If the **Convert text to HTML** checkbox is checked, the text will be in HTML format or plain text otherwise.

Example request, `POST/PUT/PATCH`:
    
    
    {
      "comment": "Some text",
     // string can also be formatted on ujet side as html
      "id": 123,
     // optional, this can also just be part of the URL;
     // for example https://example-customer.com/comment/record/{RECORD_ID}
    }
    

## Custom CRM generic API: Flows

This section provides flow charts for the custom CRM generic API flows.

### Basic flow charts

![Basic flow chart](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23db47e2.png)

### Find or create account flow

![Find or create account flow](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23db7b2a.png)

### Find or create record flow

![Find or create record flow](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23dbb006.png)

### Post call or chat actions flow

![Post call or chat actions flow](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23dbe27a.png)

### Update record flow

![Update record flow](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23dc146a.png)

### Comment flow

![Comment flow](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23dc4ea3.png)

### Upload file flow

![Upload file flow](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f23dc81bc.png)

## Agent adapters

A custom CRM offers a generic method to integrate adapters (UI widgets) into CRM systems. The CRM system must be able to handle the way the adapters are activated and triggered within it.

In order to integrate user interface adapters, a CRM software or application is typically necessary. We already provide this capability for several CRM software such as Salesforce, Kustomer, Zendesk and others.

### iFrame

Agent adapters can be seamlessly integrated into a CRM or any other tool through the use of an iFrame tag. To learn more about the HTML iframe Tag see [HTML iframe Tag](https://www.w3schools.com/tags/tag_iframe.ASP).

However, the CRM needs to handle how the adapters are presented to the user. For example it might feature UI buttons to allow for showing and hiding the adapters. Furthermore, the adapters can be designed to be draggable, allowing the Agent to reposition them on the screen at their convenience. The following examples demonstrate URL format.

Call adapter: `https://tenant.loc.ccaiplatform.com/agent/?type=call&from=custom`

Chat adapter: `https://tenant.loc.ccaiplatform.com/agent/?type=chat&from=custom`

### iFrame template

Call adapter: `html <iframe src="https://tenant.loc.ccaiplatform.com/agent/?type=call&from=custom" allow="microphone; camera; geolocation" width="290" height="600"></iframe>`

Chat adapter: `html <iframe src="https://tenant.loc.ccaiplatform.com/agent/?type=chat&from=custom" allow="microphone; camera; geolocation" width="450" height="590"></iframe>`

Note the following when embedding the adapters:

  * The `allow` attribute is required. The call adapter uses WebRTC and needs `microphone`; `camera` and `geolocation` are needed for Screen Share and location-aware features. If the permissions are not delegated to the iframe, the browser silently blocks them and the agent cannot take calls.

  * Embed one adapter per iframe. Each adapter keeps its own realtime connection, so the call and chat adapters are two separate iframes and post events independently.

  * The adapter detects that it is embedded by the fact that its parent window is on a different origin. Serve the host page from your own domain rather than from the CCAI Platform tenant domain.




### URL parameters

URL parameters can be used to provide additional information to the software, such as the type of interaction (call or chat), the source of the interaction (custom), and other relevant details.

If the tenant CRM setting is not available in the lists, the **From** parameter must always be set to **Custom**.

**Type**

  * Call
  * Chat



**From**

  * Custom (This must match with the tenant CRM setting). It must always be **custom** for any CRM other than in the lists. If there is no CRM setup, you can skip this parameter.



### Events in agent adapters

Agent adapters post events that can be hooked into by the CRM system, which then processes updates to the CRM. To do this, the CRM needs to listen to the posts from the parent window and read the post data. Based on the data, it can trigger actions such as opening a ticket tab for a specific session ID.

Both the call Adapter and chat adapter have specific events that can be utilized to enhance the CRM capabilities.

**Call adapter**

  * New Call
  * Consumer joined
  * Call redaction started
  * Call redaction ended
  * End Call



**Chat adapter**

  * New Chat
  * Active Chat
  * Chat Inbound Message
  * Chat Outbound Message
  * Form sent
  * Form completed
  * End Chat
  * Dismissed Chat



**Both adapters**

  * Agent Login
  * Screen Share session started
  * Screen Share session remote control changed
  * Screen Share session full device changed
  * Screen Share session ended
  * Transfer
  * Party added
  * Agent Connects to Session
  * Agent logout
  * Agent Assist added
  * Virtual Task Assistant joined
  * Virtual Task Assistant left
  * Virtual Task Assistant session variables received
  * CRM record pop
  * Open third-party page



### Message format

Every event is sent with the browser's [`window.postMessage()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) API from the adapter iframe to its direct parent window (`window.parent`). The parent window receives it as a [`MessageEvent`](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent).

The message has the following characteristics:

  * **`event.data` is a JSON string, not an object.** Always call `JSON.parse(event.data)` before reading it. Because other scripts on the page may also use `postMessage()` with non-JSON payloads, wrap the parse in a `try`/`catch`.

  * The parsed object has exactly two top-level keys:
        
        {
          "type": "<event type>",
          "data": { ... }
        }
        

`type` is one of the strings listed in Event types. `data` holds the event fields described in Data for events. All event-specific fields are inside `data`, never at the top level.

  * **Empty fields are omitted.** Before posting, the adapter removes any field in `data` whose value is `null`, `undefined`, or an empty string. Treat every field as potentially absent, and don't rely on a key being present with a `null` value.

  * The adapter posts with a target origin of `*`, so the message is delivered to whatever page embeds the iframe. The adapter does **not** restrict who can receive the events. Your listener should check `event.origin` against your tenant's host (for example `https://tenant.loc.ccaiplatform.com`) and ignore messages from any other origin, so that a different iframe on the same page can't spoof adapter events.

  * `type` values are case-sensitive and are not uniformly cased. Most are `Title_Case` (`New_Call`, `End_Chat`); a few are lowercase (`call_redaction_started`, `call_redaction_ended`, `agent_assist_added`) or camelCase (`openThirdPartyPage`). Compare against the exact strings in this document.

  * Events are only posted while the adapter is embedded (its parent window is a different window). If the adapter is opened as a top-level page, nothing is posted.




The following example shows a minimal listener that applies these rules:
    
    
    // Replace with the origin of your tenant.
    const ADAPTER_ORIGIN = 'https://tenant.loc.ccaiplatform.com'
    
    window.addEventListener('message', (event) => {
      if (event.origin !== ADAPTER_ORIGIN) {
        return
      }
    
      let message
      try {
        message = JSON.parse(event.data)
      } catch (e) {
        // Not an agent adapter event; another script on the page posted it.
        return
      }
    
      const { type, data = {} } = message
      switch (type) {
        case 'New_Call':
          // data.call_id, data.agent_id, data.queue_id, ...
          break
        case 'New_Chat':
          // data.chat_id, data.agent_id, data.queue_id, ...
          break
        case 'CRM_Record_Pop':
          // data.recordUrl
          break
        default:
          // Ignore event types you don't handle; new types may be added over time.
          break
      }
    }, false)
    

### Messages to the agent adapter

Communication is mostly one-way (adapter to host), but the host page can send a small set of commands to the call adapter with `postMessage()`. These messages are plain objects (not JSON strings) with the following schema:
    
    
    iframe.contentWindow.postMessage({
      channel: '<channel name>',
      eventType: '<event type>'
    }, ADAPTER_ORIGIN)
    

The following commands are supported on the `api:redaction` channel. They are used to pause and resume recording for call redaction from the host page.

`eventType` | Description  
---|---  
`start_call_redaction` | Pause the recording of the active call to start redaction.  
`stop_call_redaction` | Resume the recording of the active call to stop redaction.  
  
Note the following:

  * The commands are only acted on when call redaction is enabled for the tenant and there is an active call. Otherwise, the adapter logs that the message was ignored and does nothing.

  * When the adapter acts on the command it posts the matching `call_redaction_started` or `call_redaction_ended` event back to the host, so you can confirm that the recording state actually changed.

  * Always pass your tenant origin as the second argument to `postMessage()` instead of `*`, so the command can't be delivered to a different page if the iframe is navigated.

  * The earlier `crm:authority` channel with `redact_call:start` and `redact_call:stop` event types is still accepted by the custom CRM adapter for backward compatibility, but new integrations should use `api:redaction`.




For more information, see [Call redaction](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-redaction).

### Data for events

  * `call_id`: this is an identifier for a voice inbound call with IVR (Interactive Voice Response).

  * `chat_id`: this is an identifier for a messaging inbound call (web or mobile chat).

  * `cobrowse_session_id`: this is an identifier for a Screen Share session. A Screen Share session can be initiated in a call or chat session.

  * `session_type`: this is the type of session, such as voice, chat, or messaging.

  * `va_data_parameters`: all the variables configured in the queue to send to the Virtual Agent. This is only required for events involving the Virtual Agent. Optional.

  * `session_variable`: all the variables from the Virtual Agent that get sent to CCAI Platform in the payload. Optional.

  * `custom_sip_headers`: this enables custom SIP headers from incoming SIP calls to appear in the POST event log. It is only required if custom SIP headers are used. Optional.

  * `custom_data_secured`: contains signed, custom data from your server. Optional.

  * `custom_data_not_secured`: contains unsigned, custom data from your web page. For more information, see [Chat unsigned custom data](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en#chat-unsigned-custom-data). Optional.




**Agent IDs**

  * `agent_id`: this is an identifier for an agent.
  * `from_agent_id`: used when routing calls or chats from one agent to another, to indicate the originating agent.
  * `to_agent_id`: used when routing calls or chats from one agent to another, to indicate the destination agent.
  * `agent_custom_id`: this is an agent ID from the user profile, if it has been entered in the profile. Optional.
  * `from_agent_custom_id`: used when routing calls or chats from one agent to another, to indicate the originating agent.
  * `to_agent_custom_id`: used when routing calls or chats from one agent to another, to indicate the destination agent.
  * `agent_email`: this is the email address of the agent.
  * `from_agent_email`: used when routing calls or chats from one agent to another, to indicate the originating agent.
  * `to_agent_email`: used when routing calls or chats from one agent to another, to indicate the destination agent.



**Virtual Agent IDs**

  * `virtual_agent_id`: this is the ID number assigned to a specific Virtual Agent.



**Queue IDs**

  * `queue_id`: this is the identifier for a CCAI Platform queue, and only exists when the call originates from a queue.
  * `from_queue_id`: used when routing calls or chats from one queue to another, to indicate the originating queue.
  * `to_queue_id`: used when routing calls or chats from one queue to another, to indicate the destination queue.
  * `queue_path`: this is the path for a CCAI Platform queue, and only exists when the call originates from a queue.
  * `from_queue_path`: used when routing calls or chats from one queue to another, to indicate the originating queue.
  * `to_queue_path`: used when routing calls or chats from one queue to another, to indicate the destination queue.



**Campaign ID**

  * `campaign_id`: s CCAI Platform campaign ID. They are only included if the call type is a campaign call.
  * `campaign_name`: a CCAI Platform campaign name. They are only included if the call type is a campaign call.



**Message**

  * `message`: event indicating a new consumer message was received, plus message content.



**Session types**

  * `session_type`: a CCAI Platform session type.
  * `cobrowse_session_remote_control`: indicates the status of a requested remote control Screen Share session. Values: `off`, `requested`, `rejected`, `on`.
  * `cobrowse_session_full_device`: indicates the status of a full device Screen Share session. Values: `off`, `requested`, `rejected`, `on`.



**Participants**

  * `type`: Participant type - `end_user`; `agent`; (from participants.type of /api/v1/calls or /api/v1/chats response).

  * `cobrowse_session_requested_by`: indicates who initiated a Screen Share session. Possible values are `agent` or `end_user`.

  * `cobrowse_session_ended_by`: indicates who ended a Screen Share session. Possible Values are `agent`, `end_user`, or `api`.

  * `end_user_id`: `participants.end_user_id` of `/api/v1/calls` or `/api/v1/chats` response. This field is only present if type: `end_user`.




### Interaction / Session Types

**Call types**

  * Voice Inbound: Standard PSTN calls.
  * Voice Inbound (IVR using Mobile): Fallback PSTN calls made from the Mobile SDK.
  * Voice Inbound (Mobile): Placed by consumers using an installed Mobile SDK.
  * Voice Callback (Web): Initiated from the Web SDK.
  * Voice Inbound (API): Initiated using API.
  * Voice Scheduled (Mobile): Scheduled using an installed Mobile SDK.
  * Voice Scheduled (Web): Scheduled using an installed Web SDK.
  * Voice Outbound: Initiated by an Agent by dialing a number.
  * Voice Outbound (API): Initiated using API.
  * Voice Campaign: Initiated using an Outbound Dialer (Campaign).



**Chat types**

  * Messaging (Whatsapp): Initiated using Whatsapp.
  * Messaging Inbound (SMS)
  * Messaging Outbound (SMS)
  * Messaging Outbound (SMS using API)
  * Messaging (Web): Initiated using an installed Web SDK.
  * Messaging (Mobile): Initiated using an installed Mobile SDK.



**Call or chat type**

  * Screen Share session: Initiated by an agent or end-user during a call or a chat.



### Event types

Here are the event types that are posted by the agent adapter. The **`type`** column is the exact, case-sensitive string that appears in the `type` field of the message.

Event | `type` | Adapter  
---|---|---  
Agent login | `Agent_Login` | Both  
New call | `New_Call` | Call  
Consumer joined | `Consumer_Joined` | Call  
End call | `End_Call` | Call  
Call redaction started | `call_redaction_started` | Call  
Call redaction ended | `call_redaction_ended` | Call  
New chat | `New_Chat` | Chat  
End chat | `End_Chat` | Chat  
Active chat | `Active_Chat` | Chat  
Chat inbound message | `Chat_Inbound_Message` | Chat  
Chat outbound message | `Chat_Outbound_Message` | Chat  
Form sent | `Form_Sent` | Chat  
Form completed | `Form_Completed` | Chat  
Dismissed chat | `Dismissed_Chat` | Chat  
Screen Share session started | `Cobrowse_Session_Started` | Both  
Screen Share session remote control changed | `Cobrowse_Session_Remote_Control_Changed` | Both  
Screen Share session full device changed | `Cobrowse_Session_Full_Device_Changed` | Both  
Screen Share session ended | `Cobrowse_Session_Ended` | Both  
Transfer | `Transfer_Call`, `Transfer_Chat` | Both  
Party added | `Party_Added` | Both  
Agent connects to session | `Agent_Joined_Call`, `Agent_Joined_Chat` | Both  
Agent logout | `Agent_Logout` | Both  
Agent Assist added | `agent_assist_added` | Both  
Virtual Task Assistant joined | `Task_VA_Joined` | Both  
Virtual Task Assistant left | `Task_VA_Left` | Both  
Virtual Task Assistant session variables received | `Task_VA_Variables_Received` | Both  
CRM record pop | `CRM_Record_Pop` | Both  
Open third-party page | `openThirdPartyPage` | Call  
  
Your listener should ignore `type` values it doesn't recognize. New event types can be added over time, and the adapter also posts messages intended for other CCAI Platform surfaces (for example, when it is hosted inside the CCAI Platform agent desktop) that are not part of this contract.

#### Agent login

An agent login event occurs when the agent logs into the adapter.

Here's an example of an `Agent_Login` event:
    
    
    {
      "type": "Agent_Login",
        "data": {
        "agent_id": 1,
        "agent_custom_id": "007",
        "agent_email": "Kim@example.com",
      }
    }
    

Here are descriptions for the event data fields:

  * **`agent_id`** : the agent identifier

  * Optional: **`agent_custom_id`** : the custom identifier of the agent, if it was entered in the agent's profile.

  * **`agent_email`** : the email address associated with the agent's account.




#### New call

A new call event occurs when an agent answers a call. This event contains information such as when the call started, which agent handled the call, and where the call originated.

Here is an example of a `New_Call` event:
    
    
    {
      "type": "New_Call",
      "data": {
        "agent_id": 1,
        "agent_custom_id": "007",
        "agent_email": "Kim@example.com",
        "queue_id": 8469,
        "queue_path": "Developers / Kim",
        "campaign_id": 1432,
        "campaign_name": "Survey Movie",
        "call_id": 103646,
        "session_type": "Voice Campaign (UJET)"
      }
    }
    

Here are descriptions for the event data fields:

  * **`agent_id`** : the agent identifier

  * **`agent_custom_id`** : the custom identifier of the agent, if it was entered in the agent's profile. Optional.

  * **`agent_email`** : the email address associated with the agent's account

  * **`queue_id`** : the identifier of the queue that the call originated from. This field is included when the call originated from a queue. Optional.

  * **`queue_path`** : the path of the queue that the call originated from. This field is included when the call originated from a queue. Optional.

  * **`campaign_id`** : the identifier of the campaign. This field is included for a campaign call. Optional.

  * **`campaign_name`** : the name of the campaign. This field is included for a campaign call. Optional.

  * **`call_id`** : the call identifier

  * **`session_type`** : the session type

  * **`virtual_agent_id`** : the virtual agent identifier. This field is included for events involving the virtual agent. Optional.

  * **`va_data_parameters`** : the variables configured in the queue to send to the virtual agent. This field is included for events involving the virtual agent. Optional.

  * **`session_variable`** : all the variables from the virtual agent that are sent to Contact Center AI Platform. Optional.

  * **`custom_sip_headers`** : enables custom Session Initiation Protocol (SIP) headers from incoming SIP calls to appear in the POST event log. This field is included if custom SIP headers are used. Optional.

  * **`custom_data_secured`** : contains signed, custom data from your server. Optional.

  * **`custom_data_not_secured`** : contains unsigned, custom data from your web page. For more information, see [Chat unsigned custom data](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en#chat-unsigned-custom-data). Optional.




#### Consumer joined

A consumer joined event occurs on a campaign (outbound dialer) call when the consumer's record is resolved and it carries a list campaign manager (LCM) key. It lets the host page look up the dialed contact in its own system before the rest of the call data arrives. This event is only posted for campaign calls whose contact has an LCM key.

Here is an example of a `Consumer_Joined` event:
    
    
    {
      "type": "Consumer_Joined",
      "data": {
        "lcmKey": "acqueon:12345",
        "custom_sip_headers": {
          "X-Account-Id": "A-100"
        },
        "va_data_parameters": {
          "param1": "one"
        },
        "session_variable": {
          "key_one": "value"
        }
      }
    }
    

Here are descriptions for the event data fields:

  * **`lcmKey`** : the list campaign manager key of the dialed contact

  * **`custom_sip_headers`** : custom SIP headers from the call. This field is included if custom SIP headers are used. Optional.

  * **`va_data_parameters`** : the variables configured in the queue to send to the virtual agent. Optional.

  * **`session_variable`** : the variables from the virtual agent that are sent to Contact Center AI Platform. Optional.




#### Call redaction started

A Call redaction started event occurs when a call redaction has started and is not recording. The event data consists of the ID of the agent who handled the call and the call ID.

Note that the `type` of this event is lowercase: `call_redaction_started`.

  * `agent_id`: the ID of the agent who handled the call
  * `call_id`: the ID of the call



Here is an example of a Call redaction started event:
    
    
    {
      "type": "call_redaction_started",
      "data": {
        "agent_id": 2896,
        "call_id": 97939
      }
    }
    

#### Call redaction stopped

The call redaction stopped event occurs when a call redaction has ended and recording has resumed. This event consists of the `ID` of the agent who handled the call and the `call ID`.

Note that the `type` of this event is lowercase: `call_redaction_ended`.

  * `agent_id`: the `ID` of the agent who handled the call
  * `call_id`: the `ID` of the call



Here is an example of a call redaction stopped event data:
    
    
    {
      "type": "call_redaction_ended",
      "data": {
        "agent_id": 2896,
        "call_id": 97939
      }
    }
    

#### End call

An end call event occurs when a call is ended. This event contains information such as when the call ended, which agent handled the call, and where the call originated.

Here's an example of an `End_Call` event:
    
    
    {
      "type": "End_Call",
      "data": {
        "agent_id": 1,
        "agent_custom_id": "007",
        "agent_email": "Kim@example.com",
        "queue_id": 8469,
        "queue_path": "Developers / Kim",
        "campaign_id": 1432,
        "campaign_name": "Survey Movie",
        "call_id": 103646,
        "session_type": "Voice Campaign (UJET)"
      }
    }
    

Here are descriptions for the event data fields:

  * **`agent_id`** : the agent identifier

  * **`agent_custom_id`** : the custom identifier of the agent, if it was entered in the agent's profile. Optional.

  * **`agent_email`** : the email address associated with the agent's account

  * **`queue_id`** : the identifier of the queue that the call originated from. This field is included when the call originated from a queue. Optional.

  * **`queue_path`** : the path of the queue that the call originated from. This field is included when the call originated from a queue. Optional.

  * **`campaign_id`** : the identifier of the campaign. This field is included for a campaign call. Optional.

  * **`campaign_name`** : the name of the campaign. This field is included for a campaign call. Optional.

  * **`call_id`** : the call identifier

  * **`session_type`** : the session type

  * **`virtual_agent_id`** : the virtual agent identifier. This field is included for events involving the virtual agent. Optional.

  * **`va_data_parameters`** : the variables configured in the queue to send to the virtual agent. This field is included for events involving the virtual agent. Optional.

  * **`session_variable`** : all the variables from the virtual agent that are sent to Contact Center AI Platform. Optional.

  * **`custom_sip_headers`** : enables custom Session Initiation Protocol (SIP) headers from incoming SIP calls to appear in the POST event log. This field is included if custom SIP headers are used. Optional.

  * **`custom_data_secured`** : contains signed, custom data from your server. Optional.

  * **`custom_data_not_secured`** : contains unsigned, custom data from your web page. For more information, see [Chat unsigned custom data (Optional)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en#chat-unsigned-custom-data). Optional.




#### New chat

A new chat event occurs when an agent picks up a chat session. This event indicates when the chat started and contains information such as which agent handled the chat where the chat originated.

Here's an example a `New_chat` event:
    
    
    {
      "type": "New_Chat",
      "data": {
        "chat_id": 73522,
        "session_type": "messaging inbound (web chat)",
        "agent_id": 1,
        "agent_email": "ariel@example.com",
        "queue_id": 7678,
        "queue_path": "HB TEAM / Ariel"
      }
    }
    

Here are descriptions for the event data fields:

  * **`chat_id`** : the chat identifier

  * **`session_type`** : the session type

  * **`agent_id`** : the agent identifier

  * **`agent_custom_id`** : the custom identifier of the agent, if it was entered in the agent's profile. Optional.

  * **`agent_email`** : the email address associated with the agent's account.

  * **`queue_id`** : the identifier of the queue that the call originated from. This field is included when the call originated from a queue. Optional.

  * **`queue_path`** : the path of the queue that the call originated from. This field is included when the call originated from a queue. Optional.

  * **`custom_data_secured`** : contains signed, custom data from your server. Optional.

  * **`custom_data_not_secured`** : contains unsigned, custom data from your web page. For more information, see [Chat unsigned custom data (Optional)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en#chat-unsigned-custom-data). Optional.




#### End chat

An end chat event occurs when a chat session ends. This event indicates when the chat ended and contains information such as which agent handled the chat where the chat originated.

Here's an example a `End_Chat` event:
    
    
    {
      "type": "End_Chat",
      "data": {
        "chat_id": 73522,
        "session_type": "Messaging Inbound (Web Chat)",
        "agent_id": 1,
        "agent_email": "ariel@example.com",
        "queue_id": null,
        "queue_path": null,
        "agent_custom_id": null
      }
    }
    

Here are descriptions for the event data fields:

  * **`chat_id`** : the chat identifier.

  * **`session_type`** : the session type.

  * **`agent_id`** : the agent identifier.

  * **`agent_custom_id`** : the custom identifier of the agent, if it was entered in the agent's profile. Optional.

  * **`agent_email`** : the email address associated with the agent's account.

  * **`queue_id`** : the identifier of the queue that the call originated from. This field is included when the call originated from a queue. Optional.

  * **`queue_path`** : the path of the queue that the call originated from. This field is included when the call originated from a queue. Optional.

  * **`custom_data_secured`** : contains signed, custom data from your server. Optional.

  * **`custom_data_not_secured`** : contains unsigned, custom data from your web page. For more information, see [Chat unsigned custom data (Optional)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en#chat-unsigned-custom-data). Optional.




#### Active chat

An active chat event occurs when the agent switches to a chat tab in the chat adapter.

Here's an example of an `Active_Chat` event:
    
    
    {
      "type": "Active_Chat",
      "data": {
        "chat_id": 73521,
        "session_type": "messaging inbound (web chat)",
        "agent_id": 1,
        "agent_email": "ariel@example.com",
        "queue_id": 7678,
        "queue_path": "HB TEAM / Ariel"
      }
    }
    

Here are descriptions for the event data fields:

  * **`chat_id`** : the chat identifier

  * **`session_type`** : the session type

  * **`agent_id`** : the agent identifier

  * **`agent_custom_id`** : the custom identifier of the agent, if it was entered in the agent's profile. Optional.

  * **`agent_email`** : the email address associated with the agent's account.

  * **`queue_id`** : the identifier of the queue that the call originated from. This field is included when the call originated from a queue. Optional.

  * **`queue_path`** : the path of the queue that the call originated from. This field is included when the call originated from a queue. Optional.

  * **`custom_data_secured`** : contains signed, custom data from your server. Optional.

  * **`custom_data_not_secured`** : contains unsigned, custom data from your web page. For more information, see [Chat unsigned custom data (Optional)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en#chat-unsigned-custom-data). Optional.




#### Chat inbound message

A chat inbound message event indicates a new customer message is received. It includes the message content.

Data for the following fields is reported for a chat inbound message event:

  * `chat_id`: identifies the chat session

  * `session_type`: indicates the type of session that is being created, such as messaging inbound through web chat

  * `agent_id`: identifies the agent handling the chat session

  * `agent_custom_id`: this field exists only if the agent's profile includes a custom ID. Optional.

  * `agent_email`: the email address of the agent handling the chat session. This field is included only when the chat originates from a queue. Optional.

  * `queue_id`: the ID of the queue that the chat session originated from. This field is included only when the chat originates from a queue.

  * `queue_path`: the path of the queue that the chat session originated from. This field is included only when the chat originates from a queue.

  * `message`: an event indicating a new consumer message was received, plus the message content

  * `custom_data_secured`: allows the transmission of secured SDK custom data. Optional.

  * `custom_data_not_secured`: allows the transmission of unsecured SDK custom data. Optional.




Here's an example of a `Chat_Inbound_Message` event:
    
    
    {
      "type": "Chat_Inbound_Message",
      "data": {
        "chat_id": 73522,
        "session_type": "messaging inbound (web chat)",
        "agent_id": 1,
        "agent_email": "ariel@example.com",
        "queue_id": 7678,
        "queue_path": "HB TEAM / Ariel",
        "message" : "Can you help me with my order tracking number?"
      }
    }
    

#### Chat outbound message

A chat outbound message event occurs when a new consumer message is received. It includes the message content.

Data for the following fields is reported for a chat outbound message` event:

  * `chat_id`: identifies the chat session

  * `session_type`: indicates the type of session that is being created, such as messaging inbound through web chat

  * `agent_id`: identifies the agent handling the chat session

  * `agent_custom_id`: This field is only included if the agent's profile has a custom ID. Optional.

  * `agent_email`: the email address of the agent handling the chat session. This field is only included when the chat originates from a queue. Optional.

  * `queue_id`: the ID of the queue that the chat session originated from. This field is only included when the chat originates from a queue.

  * `queue_path`: the path of the queue that the chat session originated from. This field is included only when the chat originates from a queue.

  * `message`: event indicates a new consumer message was received, plus message content

  * `custom_data_secured`: allows the transmission of secured SDK custom data. Optional.

  * `custom_data_not_secured`: allows the transmission of unsecured SDK custom data. Optional.




Here's an example of a `Chat_Outbound_Message` event:
    
    
    {
      "type": "Chat_Outbound_Message",
      "data": {
        "chat_id": 73522,
        "session_type": "messaging inbound (web chat)",
        "agent_id": 1,
        "agent_email": "ariel@example.com",
        "queue_id": 7678,
        "queue_path": "HB TEAM / Ariel",
        "message" : "Please give me a moment to look up your account information"
      }
    }
    

#### Form sent

A form sent event occurs when a form is sent to the consumer during a chat session. Both events are posted by the chat adapter when the chat receives the corresponding system message.

Here is an example of a `Form_Sent` event:
    
    
    {
      "type": "Form_Sent",
      "data": {
        "chat_id": 73522,
        "session_type": "Messaging Inbound (Web Chat)",
        "agent_id": 1,
        "agent_custom_id": "007",
        "agent_email": "Kim@example.com",
        "end_user_id": 5512,
        "form_external_id": "payment-details",
        "form_name": "Payment details",
        "form_type": "secure",
        "queue_id": 7678,
        "queue_path": "HB TEAM / Kim",
        "queue_language_id": "en",
        "timestamp": 1727853575000
      }
    }
    

Here are descriptions for the event data fields:

  * **`chat_id`** : the chat identifier

  * **`session_type`** : the session type

  * **`agent_id`** : the agent identifier

  * **`agent_custom_id`** : the custom identifier of the agent, if it was entered in the agent's profile. Optional.

  * **`agent_email`** : the email address associated with the agent's account

  * **`end_user_id`** : the identifier of the consumer in the chat. Optional.

  * **`form_external_id`** : the external identifier of the form that was sent. Optional.

  * **`form_name`** : the name of the form that was sent. Optional.

  * **`form_type`** : the type of the form that was sent. Optional.

  * **`queue_id`** : the identifier of the queue that the chat originated from. This field is included when the chat originated from a queue. Optional.

  * **`queue_path`** : the path of the queue that the chat originated from. This field is included when the chat originated from a queue. Optional.

  * **`queue_language_id`** : the language of the queue. Optional.

  * **`timestamp`** : the time the event was posted, in milliseconds since the Unix epoch

  * **`va_data_parameters`** : the variables configured in the queue to send to the virtual agent. Optional.

  * **`session_variable`** : all the variables from the virtual agent that are sent to Contact Center AI Platform. Optional.

  * **`custom_data_secured`** : contains signed, custom data from your server. Optional.

  * **`custom_data_not_secured`** : contains unsigned, custom data from your web page. For more information, see [Chat unsigned custom data](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en#chat-unsigned-custom-data). Optional.




#### Form completed

A form completed event occurs when the consumer submits a form that was sent during a chat session. The event data has the same fields as the Form sent event.

Here is an example of a `Form_Completed` event:
    
    
    {
      "type": "Form_Completed",
      "data": {
        "chat_id": 73522,
        "session_type": "Messaging Inbound (Web Chat)",
        "agent_id": 1,
        "agent_custom_id": "007",
        "agent_email": "Kim@example.com",
        "end_user_id": 5512,
        "form_external_id": "payment-details",
        "form_name": "Payment details",
        "form_type": "secure",
        "queue_id": 7678,
        "queue_path": "HB TEAM / Kim",
        "queue_language_id": "en",
        "timestamp": 1727853601000
      }
    }
    

#### Dismissed chat

A dismissed chat event occurs when the agent closes the chat tab in the chat adapter.

Here's an example of a `Dismissed_Chat` event:
    
    
    {
      "type":"Dismissed_Chat",
      "data":{"chat_id":73522,
        "session_type":"Messaging Inbound (Web Chat)",
        "agent_id":1,
        "agent_email":"ariel@example.com"
      }
    }
    

Here are descriptions for the event data fields:

  * **`chat_id`** : the chat identifier

  * **`session_type`** : the session type

  * **`agent_id`** : the agent identifier

  * **`agent_custom_id`** : the custom identifier of the agent, if it was entered in the agent's profile. Optional.

  * **`agent_email`** : the email address associated with the agent's account

  * **`queue_id`** : the identifier of the queue that the call originated from. This field is included when the call originated from a queue. Optional.

  * **`queue_path`** : the path of the queue that the call originated from. This field is included when the call originated from a queue. Optional.

  * **`custom_data_secured`** : contains signed, custom data from your server. Optional.

  * **`custom_data_not_secured`** : contains unsigned, custom data from your web page. For more information, see [Chat unsigned custom data (Optional)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en#chat-unsigned-custom-data). Optional.




#### Screen Share session started

A _Screen Share session started_ event occurs when a Screen Share session is started by an agent or an end-user. A Screen Share sessions can be started during a call or a chat. For more information, see [Screen Share](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse).

Here's an example of a JSON object for a Screen Share session started event:
    
    
    {
      "type": "Cobrowse_Session_Started",
      "data": {
        "agent_id": 5,
        "chat_id": 791,
        "cobrowse_session_id": "Y1zYY6XIYX4oapqpEz3qHw",
        "cobrowse_session_requested_by": "agent",
        "cobrowse_session_remote_control": "off",
        "cobrowse_session_full_device": "off"
      }
    }
    

Here are descriptions for the event data fields:

  * **`agent_id`** : The agent identifier.

  * **`call_id`** : The identifier for an inbound call on the IVR (interactive voice response) channel. This field is included if the Screen Share session was started during a call.

  * **`chat_id`** : The identifier for an inbound chat on the web or mobile channel. This field is included if the Screen Share session was started during a chat.

  * **`cobrowse_session_id`** : The identifier for a Screen Share session.

  * **`cobrowse_session_requested_by`** : Indicates who started a Screen Share session. Values are `agent` and `end-user`.

  * **`cobrowse_session_remote_control`** : Indicates the status of a remote control Screen Share session. Values are `on`, `rejected`, `requested`, and `off`.

  * **`cobrowse_session_full_device`** : Indicates the status of a full device Screen Share session. Values are `on`, `rejected`, `requested`, and `off`.

  * **`custom_data_secured`** : contains signed, custom data from your server. Optional.

  * **`custom_data_not_secured`** : contains unsigned, custom data from your web page. For more information, see [Chat unsigned custom data (Optional)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en#chat-unsigned-custom-data). Optional.




#### Screen Share session remote control changed

A Screen Share session remote control changed event occurs when the status of a remote control Screen Share session changes. This event indicates the status of the remote control Screen Share session. For more information, see [ Screen Share](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse).

Here's an example of a JSON object for a `Cobrowse_Session_Remote_Control_Changed` event:
    
    
    {
      "type": "Cobrowse_Session_Remote_Control_Changed",
      "data": {
        "agent_id": 5,
        "chat_id": 791,
        "cobrowse_session_id": "Y1zYY6XIYX4oapqpEz3qHw",
        "cobrowse_session_remote_control": "requested"
      }
    }
    

Here are descriptions for the event data fields:

  * **`agent_id`** : the agent identifier.

  * **`call_id`** : the identifier for an inbound call on the IVR (interactive voice response) channel. This field is included if the Screen Share session was started during a call.

  * **`chat_id`** : the identifier for an inbound chat on the web or mobile channel. This field is included if the Screen Share session was started during a chat.

  * **`cobrowse_session_id`** : the identifier for a Screen Share session.

  * **`cobrowse_session_remote_control`** : indicates the status of a remote control Screen Share session. Values are `on`, `rejected`, `requested`, and `off`.

  * **`custom_data_secured`** : contains signed, custom data from your server. Optional.

  * **`custom_data_not_secured`** : contains unsigned, custom data from your web page. For more information, see [Chat unsigned custom data (Optional)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en#chat-unsigned-custom-data). Optional.




#### Screen Share session full device changed

A Screen Share session full device changed event occurs when the status of a full device Screen Share session changes. This event indicates the status of the full device Screen Share session. For more information, see [Screen Share](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse).

Here's an example of a `Cobrowse_Session_Full_Device_Changed` event:
    
    
    {
      "type": "Cobrowse_Session_Full_Device_Changed",
      "data": {
        "agent_id": 5,
        "cobrowse_session_id": "9-Kshrag-gn6ZSuIxoMtWQ",
        "cobrowse_session_full_device": "rejected"
      }
    }
    

Here are descriptions for the event data fields:

  * **`agent_id`** : the agent identifier.

  * **`call_id`** : the identifier for an inbound call on the IVR (interactive voice response) channel. This field is included if the Screen Share session was started during a call.

  * **`chat_id`** : the identifier for an inbound chat on the web or mobile channel. This field is included if the Screen Share session was started during a chat.

  * **`Cobrowse_session_id`** : the identifier for a Screen Share session.

  * **`Cobrowse_session_full_device`** : indicates the status of a full device Screen Share session. Values are `on`, `rejected`, `requested`, and `off`.

  * **`custom_data_secured`** : contains signed, custom data from your server. Optional.

  * **`custom_data_not_secured`** : contains unsigned, custom data from your web page. For more information, see [Chat unsigned custom data (Optional)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en#chat-unsigned-custom-data). Optional.




#### Screen Share session ended

A Screen Share session started event occurs when a Screen Share session is ended by an agent, an end-user, or the API. For more information, see [Configure Screen Share](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse).

Here's an example of a `Cobrowse_Session_Ended` event:
    
    
    {
      "type": "Cobrowse_Session_Ended",
      "data": {
        "agent_id": 5,
        "cobrowse_session_id": "9-Kshrag-gn6ZSuIxoMtWQ",
        "cobrowse_session_requested_by": "end_user",
        "cobrowse_session_ended_by": "agent",
        "cobrowse_session_remote_control": "on",
        "cobrowse_session_full_device": "rejected"
      }
    }
    

Here are descriptions for the event data fields:

  * **`agent_id`** : the agent identifier.

  * **`call_id`** : the identifier for an inbound call on the IVR (interactive voice response) channel. This field is included if the Screen Share session was started during a call.

  * **`chat_id`** : the identifier for an inbound chat on the web or mobile channel. This field is included if the Screen Share session was started during a chat.

  * **`cobrowse_session_id`** : the identifier for a Screen Share session.

  * **`cobrowse_session_ended_by`** : indicates who ended the Screen Share session. Values are `agent`, `end-user` and `api`.

  * **`cobrowse_session_remote_control`** : indicates the status of a remote control Screen Share session. Values are `on`, `rejected`, `requested`, and `off`.

  * **`cobrowse_session_full_device`** : indicates the status of a full device Screen Share session. Values are `on`, `rejected`, `requested`, and `off`.

  * **`custom_data_secured`** : contains signed, custom data from your server. Optional.

  * **`custom_data_not_secured`** : contains unsigned, custom data from your web page. For more information, see [Chat unsigned custom data (Optional)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en#chat-unsigned-custom-data). Optional.




#### Transfer

A transfer event occurs when call or chat is transferred. It can refer to either a warm or cold transfer.

The following event fields are part of a transfer event.

  * `chat_id` or `call_id`: identifies the call or chat session

  * `session_type`: indicates the type of session that is being created, such as a messaging inbound through web chat

  * `campaign_id`: the ID of the campaign. This field is only present if the call type is a campaign call. Optional.

  * `campaign_name`: the name of the campaign. This field is only present if the call type is a campaign call. Optional.

  * `from_agent_id`: used when routing calls or chats from one agent to another, to indicate the originating agent

  * `from_agent_custom_id`: used when routing calls or chats from one agent to another, to indicate the originating agent. Optional.

  * `from_agent_email`: used when routing calls or chats from one agent to another, to indicate the originating agent

  * `to_agent_id`: used when routing calls or chats from one agent to another, to indicate the destination agent

  * `to_agent_custom_id`: used when routing calls or chats from one agent to another, to indicate the destination agent. Optional.

  * `to_agent_email`: used when routing calls or chats from one agent to another, to indicate the destination agent

  * `from_queue_id`: used when routing calls or chats from one queue to another, to indicate the originating queue

  * `from_queue_path`: used when routing calls or chats from one queue to another, to indicate the originating queue

  * `to_queue_id`: used when routing calls or chats from one queue to another to indicate the destination queue

  * `to_queue_path`: used when routing calls or chats from one queue to another to indicate the destination queue

  * `virtual_agent_id`: the ID assigned to a virtual agent. Optional.

  * `va_data_parameters`: all the variables configured in the queue to send to the virtual agent. This is only required for events involving the virtual agent. Optional.

  * (`session_variable`: all the variables from the virtual agent that get sent to CCAI Platform in the payload. Optional.

  * `custom_sip_headers`: enables custom SIP headers from incoming SIP calls to appear in the POST event log. It is only required if custom SIP headers are used. Optional.

  * `custom_data_secured`: allows the transmission of secured SDK custom data. Optional.

  * `custom_data_not_secured`: allows the transmission of unsecured SDK custom data. Optional.




Here's an example of a transfer event:
    
    
    {
      "type": "Transfer_Chat",
      "data": {
        "chat_id": 103646,
        "session_type": "Messaging Inbound (SMS)",
        "campaign_id": 1432,
        "campaign_name": "Survey Movie",
        "from_agent_id": 1,
        "from_agent_custom_id": "007",
        "from_agent_email": "Ira@example.com",
        "to_agent_id" : 5
        "to_agent_custom_id": "100"
        "to_agent_email" : "ariel@example.com"
        "from_queue_id": 8469,
        "from_queue_path": "Developers / Ariel",
        "to_queue_id" : 1234,
        "to_queue_path" : "Schemes / Auric"
      }
    }
    

#### Party added

A party added event refers to any transfer. It can be either a call or a chat transfer.

A party added event contains the following data:

  * `chat_id` or `call_id`: identifies the call or chat session

  * `session_type`: indicates the type of session that is being created, such as a messaging inbound through web chat

  * `agent_custom_id`: this field exists only if the agent's profile includes a custom ID. Optional.

  * `agent_email`: the email address of the agent handling the call or chat session.

  * `queue_id`: the ID of the queue that the chat session originated from. This field is included only when the chat originates from a queue. Optional.

  * `queue_path`: the path of the queue that the chat session originated from. This field is included only when the chat originates from a queue. Optional.

  * `campaign_id`: the ID of the campaign. This field is only included when the call type is a campaign call. Optional.

  * `campaign_name`: the name of the campaign. This field is only included when the call type is a campaign call. Optional.

  * `type`: the participant type, for example an end_user or agent. This field is returned as part of the participants.type of `/api/v1/calls` or `/api/v1/chats` response

  * `end_user_id`: the end_user_id. This field is returned as part of the from `/api/v1/calls` or `/api/v1/chats` response. This field is only present for end user call or chats that are routed from one agent to another, to indicate the destination agent. Optional.

  * `virtual_agent_id`: the identifier assigned to a virtual agent. Optional.

  * `va_data_parameters`: all the variables configured in the queue to send to the virtual agent. This is only required for events involving the virtual agent. Optional.

  * `session_variable`: all the variables from the virtual agent that get sent to CCAI Platform in the payload. Optional.

  * `custom_sip_headers`: this enables custom SIP headers from incoming SIP calls to appear in the POST event log. It is only required if custom SIP headers are used. Optional.

  * `custom_data_secured`: allows the transmission of secured SDK custom data. Optional.

  * `custom_data_not_secured`: allows the transmission of unsecured SDK custom data. Optional.




Here is an example of a `Party_Added` event.
    
    
    {
      "type": "Party_Added",
      "data": {
        "chat_id": 103646,
        "session_type": "Messaging Inbound (SMS)",
        "campaign_id": 1432,
        "campaign_name": "Survey Movie",
        "agent_id": 1,
        "agent_custom_id": "007",
        "agent_email": "ariel@example.com",
        "queue_id": 8469,
        "queue_path": "Developers / Ariel",
        "type" : "agent"
      }
    }
    

#### Agent connects to session

An agent connects to session event occurs when an agent connects to a session. There two different types of events. The type is determined by whether it is a call or chat.

The following event fields are part of an agent connects to session event.

  * `agent_id`: identifies the agent handling the call or chat session.

  * `agent_email`: the email address of the agent handling the call or chat session.

  * `agent_custom_id`: this field exists only if the agent's profile includes a custom ID. Optional.

  * `chat_id` or `call_id`: identifies the call or chat session.

  * `virtual_agent_id`: the ID assigned to a specific virtual agent. Optional.

  * `campaign_id`: the ID of the campaign. This field is only included when the call type is a campaign call. Optional.

  * `campaign_name`: the name of the campaign. This field is only included when the call type is a campaign call. Optional.

  * `queue_id`: the ID of the queue that the chat session originated from. This field is included only when the chat originates from a queue. Optional.

  * `queue_path`: the path of the queue that the chat session originated from. This field is included only when the chat originates from a queue. Optional.

  * `session_type`: indicates the type of session that is being created, such as a messaging inbound through web chat.

  * `virtual_agent_id`: the ID assigned to a virtual agent. Optional.

  * `va_data_parameters`: all the variables configured in the queue to send to the virtual agent. This is only required for events involving the Virtual Agent. Optional.

  * `session_variable`: all the variables from the virtual agent that get sent to UJET in the payload. Optional.

  * `custom_sip_headers`: this enables custom SIP headers from incoming SIP calls to appear in the POST event log. It is only required if custom SIP headers are used. Optional.

  * `custom_data_secured`: allows the transmission of secured SDK custom data. Optional.

  * `custom_data_not_secured`: allows the transmission of unsecured SDK custom data. Optional.




Here's an example of a `Agent_Joined_Chat` event data:
    
    
    {
      "type": "Agent_Joined_Chat",
      "data": {
        "chat_id": 103646,
        "campaign_id": 1432,
        "campaign_name": "Survey Movie",
        "agent_id": 1,
        "agent_custom_id": "007",
        "agent_email": "ariel@example.com",
        "queue_id": 8469,
        "queue_path": "Developers / Ariel",
        "session_type": "Messaging Inbound (SMS)",
      }
    }
    

#### Agent logout

An agent logout event occurs when an agent logs out of the agent adapter.

The following event fields are a part of an `Agent_Logout` event.

  * `agent_id`: the identifier of the agent who logged in

  * `agent_email`: the email address associated with the agent account

  * `agent_custom_id`: the custom ID of the agent, if it was entered in the agent's profile. Optional.




Here's an example of an `Agent_Logout` event:
    
    
    {
      "type": "Agent_Logout",
      "data": {
        "agent_id": 1,
        "agent_custom_id": "007",
        "agent_email": "ariel@example.com",
      }
    }
    

#### Agent Assist added

An Agent Assist added event occurs when an agent activates Agent Assist during a call or chat session.

Note the following about this event:

  * The `type` of this event is lowercase: `agent_assist_added`.

  * The timestamp field is named **`Timestamp`** (capital T) and is the number of milliseconds since the Unix epoch.




Here's an example of an `agent_assist_added` event:
    
    
    {
      "type": "agent_assist_added",
      "data": {
        "conversation_id": "12345",
        "queue_id": 65,
        "agent_id": 1,
        "session_id": "78534G4RT4284",
        "queue_language_id": "en",
        "Timestamp": 1727853575000
      }
    }
    

Here are the event fields:

  * **`conversation_id`** : the conversation identifier. This field is included when the session uses a conversation profile. Optional.

  * **`queue_id`** : the queue identifier. Optional.

  * **`agent_id`** : the agent identifier

  * **`session_id`** : the session identifier. Optional.

  * **`queue_language_id`** : the language of the queue. Optional.

  * **`Timestamp`** : the time the event was posted, in milliseconds since the Unix epoch




#### Virtual Task Assistant joined

A Virtual Task Assistant joined event occurs when a Virtual Task Assistant (VTA) joins a call or chat session.

Here's an example of a `Task_VA_Joined` event:
    
    
    {
      "type": "Task_VA_Joined",
      "data": {
        "chat_id": 103646,
        "campaign_id": 1432,
        "campaign_name": "Survey Movie",
        "virtual_agent_id": 1,
        "virtual_agent_name": "Order status assistant",
        "participant_id": 1,
        "queue_id": 8469,
        "queue_path": "Developers / Kim",
        "queue_language_id": "en",
        "session_type": "Messaging Inbound (SMS)",
        "conversation_id": "12345",
        "session_id": "78534G4RT4284",
        "timestamp": 1727853575000,
        "data_parameters": {
          "param1": "one",
          "param2": "two"
        }
      }
    }
    

Here are the event fields:

  * **`call_id`** or **`chat_id`** : the call or chat identifier

  * **`campaign_id`** : the identifier of the campaign. This field is included for a campaign call. Optional.

  * **`campaign_name`** : the name of the campaign. This field is included for a campaign call. Optional.

  * **`virtual_agent_id`** : the identifier of the VTA

  * **`virtual_agent_name`** : the name of the VTA as configured in the CCAI Platform portal

  * **`participant_id`** : the participant identifier of the VTA in the session

  * **`queue_id`** : the identifier of the queue that the session originated from. Optional.

  * **`queue_path`** : the path of the queue that the session originated from. Optional.

  * **`queue_language_id`** : the language of the queue. Optional.

  * **`session_type`** : the session type

  * **`conversation_id`** : the conversation identifier. This field is included when the session uses a conversation profile. Optional.

  * **`session_id`** : the session identifier. Optional.

  * **`timestamp`** : the time the event was posted, in milliseconds since the Unix epoch

  * **`data_parameters`** : the variables configured in the CCAI Platform portal and sent to the VTA. Optional.




#### Virtual Task Assistant left

A Virtual Task Assistant left event occurs when the VTA leaves the session. In addition to the fields of the Virtual Task Assistant joined event, it includes the reason the VTA session ended and the session variables the VTA captured.

Here's an example of a `Task_VA_Left` event:
    
    
    {
      "type": "Task_VA_Left",
      "data": {
        "chat_id": 103646,
        "virtual_agent_id": 1,
        "virtual_agent_name": "Order status assistant",
        "participant_id": 1,
        "queue_id": 8469,
        "queue_path": "Developers / Kim",
        "queue_language_id": "en",
        "session_type": "Messaging Inbound (SMS)",
        "conversation_id": "12345",
        "session_id": "78534G4RT4284",
        "timestamp": 1727853600000,
        "finish_reason": "Task VA completed",
        "data_parameters": {
          "param1": "one"
        },
        "captured_variables": [
          {
            "intent_name": null,
            "variables": {
              "order_number": "A-100"
            },
            "captured_at": "2024-11-15 16:46:31 UTC",
            "timestamp": 1727853590000
          }
        ]
      }
    }
    

The additional event fields are:

  * **`finish_reason`** : the reason the VTA session ended

  * **`captured_variables`** : the session variables captured by the VTA, each with the intent that captured them and when they were captured. Optional.




#### Virtual Task Assistant session variables received

A Virtual Task Assistant session variables received event occurs each time the VTA sends a custom session variable payload during the session. The event has the same fields as the Virtual Task Assistant left event except `finish_reason`, and `captured_variables` holds the variables received so far.

Here's an example of a `Task_VA_Variables_Received` event:
    
    
    {
      "type": "Task_VA_Variables_Received",
      "data": {
        "chat_id": 103646,
        "virtual_agent_id": 1,
        "virtual_agent_name": "Order status assistant",
        "participant_id": 1,
        "queue_id": 8469,
        "queue_path": "Developers / Kim",
        "queue_language_id": "en",
        "session_type": "Messaging Inbound (SMS)",
        "conversation_id": "12345",
        "session_id": "78534G4RT4284",
        "timestamp": 1727853590000,
        "data_parameters": {
          "param1": "one"
        },
        "captured_variables": [
          {
            "intent_name": null,
            "variables": {
              "order_number": "A-100"
            },
            "captured_at": "2024-11-15 16:46:31 UTC",
            "timestamp": 1727853590000
          }
        ]
      }
    }
    

Only variables whose `capture_type` includes `event` in the virtual agent's custom session variable payload are included, and keys listed in `invisible_to_adapter_events` are excluded.

### Background screen pop

The screen pop capability enables agents to do a CRM screen pop in the background, which means that customer information is displayed on the agent's screen without any action required by the agent. This provides a more seamless experience for consumers and reduces handling time for agents.

#### CRM record pop

The event, `CRM_Record_Pop`, is a server-side event that triggers when a ticket needs to be popped. This event includes a parameter called `recordUrl` that contains the URL of the CRM record, allowing you to perform a screen pop by subscribing to POST events if you are using embedded adapters.

Here's an example of a `CRM_Record_Pop` event:
    
    
    {
      "type": "CRM_Record_Pop",
      "data": {
        "recordUrl": "https://crm.example.com/tickets/4711"
      }
    }
    

The event has a single field:

  * **`recordUrl`** : the URL of the CRM record to display



To achieve this, the following example demonstrates how to add an event listener that listens to messages sent from another frame or window. This code snippet is designed to enable communication between different frames or windows and allow for dynamic updates to the content displayed in the iframe based on received messages.
    
    
    // Replace with the origin of your tenant.
    const ADAPTER_ORIGIN = 'https://tenant.loc.ccaiplatform.com'
    
    // name is the html property of the iframe that shows the CRM record
    const iframeTarget = document.querySelector('iframe[name="target_iframe_adapter"]')
    
    // example usage of add event listener
    // https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener
    window.addEventListener('message', (e) => {
      // Only accept events posted by the agent adapter.
      if (e.origin !== ADAPTER_ORIGIN) {
        return
      }
    
      let message
      try {
        message = JSON.parse(e.data)
      } catch (err) {
        // Not an agent adapter event.
        return
      }
    
      const { type, data = {} } = message
      console.log('EventListener: ', type)
    
      switch (type) {
        case 'CRM_Record_Pop': {
          const recordUrl = data.recordUrl
          if (!recordUrl) {
            return
          }
          console.log(`Opening recordUrl in iframe ${iframeTarget.getAttribute('name')}`)
    
          // changing an iframe target to the record URL pop
          iframeTarget.src = recordUrl
          break
        }
        case 'New_Chat':
          console.log('Chat started...')
          // handling here for New_Chat events
          break
        case 'End_Chat':
          console.log('Chat ended...')
          // handling here for End_Chat events
          break
        default:
          // code handling for other types
          break
      }
    }, false)
    

#### Open third-party page

The `openThirdPartyPage` event is posted by the call adapter when a call carries a third-party key (for example, a list campaign manager key on a campaign call) and the adapter is about to open the matching third-party page. If you are using embedded adapters you can subscribe to this event to open the page in your own UI instead.

Here's an example of an `openThirdPartyPage` event:
    
    
    {
      "type": "openThirdPartyPage",
      "data": {
        "thirdPartyKey": "acqueon:12345",
        "callId": 103646
      }
    }
    

Here are the event fields:

  * **`thirdPartyKey`** : the third-party key associated with the call

  * **`callId`** : the call identifier




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
