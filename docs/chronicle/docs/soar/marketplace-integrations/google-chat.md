---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-chat/
title: Google Chat \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:45:46.432947+00:00
---

# Google Chat  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/google-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google Chat

This document provides guidance on how to integrate Google Chat with Google SecOps.

## Product Permissions

### Create a service account

  1. In the Google Cloud console, select an existing Google Cloud project or create a new one. Note that the selected Google Cloud project should be a part of the Organization in Google Cloud.
  2. Click the ☰ **Menu** and select the **APIs & Services > Credentials** menu item.
  3. At the top of the page, click **\+ CREATE CREDENTIALS > Service Account**.
  4. Enter a service account name to display in the console.
  5. Optional: Enter a description of the service account.
  6. Click **CREATE** , followed by **CONTINUE** , and **DONE** to finish creating the service account.



### Create service account credentials

  1. After creating the service account, you will be redirected to the list of credentials you can use for the Google Cloud project. Under the **Service Accounts** section, click your newly-created service account. This will be called: _service-account-name@project-name-XXXXXX.iam.gserviceaccount.com_.
  2. Click **ADD KEY > Create new key**.
  3. Keep JSON selected and click **CREATE**.

**Warning:** Do not lose or share this file. If you lose the file, you need to delete and create new credentials for this account.

This initiates downloading the credentials file that you will need to access the API as this service account.

### Set up a new Apps Script project

  1. Go to Google Apps Script.
  2. Create a new Apps Script project.
  3. To execute the integration functionality, add the following code to the newly created project:
         
         var SCOPE = 'https://www.googleapis.com/auth/chat.bot';
         // The values below are copied from the JSON file downloaded upon
         // service account creation.
         // For SERVICE_ACCOUNT_PRIVATE_KEY, remember to include the BEGIN and END lines of the private key
         var SERVICE_ACCOUNT_PRIVATE_KEY = '...';
         var SERVICE_ACCOUNT_EMAIL = 'service-account@project-id.iam.gserviceaccount.com';
         
         // Posts a message into the given space ID via the API, using
         // service account authentication.
         function postMessage(spaceId, message) {
           var service = OAuth2.createService('chat')
               .setTokenUrl('https://accounts.google.com/o/oauth2/token')
               .setPrivateKey(SERVICE_ACCOUNT_PRIVATE_KEY)
               .setClientId(SERVICE_ACCOUNT_EMAIL)
               .setPropertyStore(PropertiesService.getUserProperties())
               .setScope(SCOPE);
           if (!service.hasAccess()) {
             Logger.log('Authentication error: %s', service.getLastError());
             return;
           }
           var url = 'https://chat.googleapis.com/v1/' + spaceId + '/messages';
           UrlFetchApp.fetch(url, {
             method: 'post',
             headers: { 'Authorization': 'Bearer ' + service.getAccessToken() },
             contentType: 'application/json',
             payload: JSON.stringify(message),
           });
         }
         

  4. Open the service account credentials file downloaded from the Google Cloud console.

  5. Copy the private_key value (the one that starts with -----BEGIN PRIVATE KEY-----) and paste it into SERVICE_ACCOUNT_PRIVATE_KEY in the Apps Script project.

  6. Copy the client_email value from the credentials file, and paste it into the SERVICE_ACCOUNT_EMAIL in the Apps Script project.

  7. Link the Apps Script project to the Google Cloud project you created.

  8. Go back to the Google Cloud console, and select the ☰ **> IAM & Admin > Settings** menu item.

  9. Copy the project number defined on this page.

  10. In your Apps Script Project, select the **Project** **Settings > Google Cloud Project** menu item and paste the project number into the Enter Project Number here dialog.

  11. Click **Set Project**.




### Enable the Google Chat API

  1. Go to ☰ **> APIs & Services**, and select **Library**.
  2. Search for **Google Chat API** and click the only result.
  3. Click **ENABLE**.



This enables the API for your project.

### Deploy a bot

  1. In the Apps Script UI, go to **Deploy > New Deployment**.
  2. Select **Add On** for the new deployment type.
  3. Enter a deployment name and description, and click **Save**.
  4. Once saving is finished, click **Get ID** next to the deployment you just created, and copy the deployment ID value.



**Configure the Google Chat bot:**

  1. In the Google Cloud console, go to ☰ **> APIs & Services > Dashboard**.
  2. In the list of enabled APIs, select **Google Chat API**.
  3. Click **Manage** to open the Google Chat API page.
  4. On the opened page, select the **Configuration** tab and set up your bot configuration:

     * In the **App name** field, enter Google Security Operations Chat App.
     * In the **Avatar URL** field, enter https://developers.google.com/chat/images/chat-product-icon.png.
     * In the **Description** field, enter Google SecOps Chat App that can be used to send messages from Google SecOps to a Google Chat Spaces.
     * In the **Functionality** section, select **App works in spaces with multiple users**.
     * In the **Connection settings** section, select **Apps Script project** and paste the deployment ID obtained from the _Deploy a bot_ procedure.
     * In the **Permissions** section, select **Specific people and groups in your domain** and specify who should be able to interact with the bot.
     * Click **Save**. App configuration is completed.

**Note:** **Important - Add the Google Chat App to needed spaces**

As the Google Chat app can't create spaces (initiate conversations), the Google SecOps Chat app needs to be added to the spaces it should send messages to.

After the integration is configured, the "List Spaces" action can be used to fetch the spaces that the Google SecOps app has access to (can send messages to).

If the "List Spaces" action shows no available spaces, it means your app will not be able to send messages in any space. Please go back to the detailed instructions above and make sure you followed each step carefully

## Configure Google Chat integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
API Root URL | String | https://chat.googleapis.com/ | Yes | API Root URL the integration uses to connect to the Google Chat service.  
Service Account | Password | N/A | Yes | Service account JSON file content that the chatbot uses to work with the Google Chat service.  
Verify SSL | Checkbox | Checked | Yes | If enabled, verify that the SSL certificate for the connection to the Google Chat service is valid.  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Ping

#### Description

Test connectivity to Google Chat with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Run On

This action doesn't run on entities, nor has mandatory input parameters.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

**Result type** | **Value/Description** | **Type**  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If successful:_ "Successfully connected to the Google Chat service with the provided connection parameters!"**The action should fail and stop a playbook execution:******_If critical error, like wrong credentials or lost connectivity is reported:_ "Failed to connect to the Google Chat service! Error is {0}".format(exception.stacktrace)" | General  
  
### List Spaces

#### Description

List spaces that the currently configured Google Chat bot was added to.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Filter Key | DDL | Select One Possible Values: 

  * Name
  * Display Name
  * Type

| No | Specify the key that needs to be used to filter Google Chat spaces.  
Filter Logic | DDL | Not SpecifiedPossible Values:

  * Not Specified
  * Equal
  * Contains

| No | Specify what filter logic should be applied. Filtering logic is working based on the value provided in the "Filter Key" parameter.  
Filter Value | String | N/A | No | Specify what value should be used in the filter. If "Equal" is selected, action tries to find the exact match among results.If "Contains" is selected, action tries to find results that contain the specified substring.If nothing is provided in this parameter, the filter is not applied. Filtering logic is working based on the value provided in the "Filter Key" parameter.  
Max Records To Return | Integer | 50 | No | Specify the number of records to return. If nothing is provided, action returns 50 records.  
Include User Memberships | Checkbox | Unchecked | No | If enabled, user memberships information is added to the action Case Wall table and JSON result.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If data is available (is_success=true):_ "Successfully found added spaces for the provided criteria in Google Chat."_If data is not available (is_success=false):_ "No spaces were found for the provided criteria in Google Chat"_If the "Filter Value" parameter has no value (is_success=true):_ "The filter was not applied, because parameter "Filter Value" has an empty value."**The action should fail and stop a playbook execution:******_If the Filter Key parameter is set to "Select One" and the Filter Logic parameter is set to****"Equal" or "Contains":_ "Error executing action "List Spaces". Reason: you need to select a field from the "Filter Key" parameter."_If an invalid value is provided for the Max Records to Return parameter:_ "Error executing action "List Spaces". Reason: "Invalid value was provided for "Max Records to Return". Positive number should be provided."_If a fatal error, like wrong credentials, no connection to server, other is reported:_ "Error executing action "List Spaces". Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table | **Table Name:** Available Spaces Bot was Added to **Table Columns:** {fields}  **Note:** If the "Include User Memberships" checkbox is checked, additional column that have a Display Name for the space members are added. | General  
  
### Send Message

#### Description

Send a message to a Google Chat space that the Google SecOps application was added to.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Space Name | String | N/A | Yes | Specify the space name to send the message to.Example space name: AAAAdaTsel0  
Message Text | String | N/A | Yes | Specify the text of the message to send.  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If a message is sent successfully (is_success=true):_ "Message was sent successfully."**The action should fail and stop a playbook execution:**_If a critical error, like no connection or wrong credentials is reported:_ "Error executing action "Send Message". Reason: {0}''.format(error.Stacktrace) | General  
  
### Send Advanced Message

#### Description

Send an advanced message to a Google Chat space based on the provided message JSON payload.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Space Name | String | N/A | Yes | Specify the space name to send the message to.Example space name: AAAAdaTsel0  
Message JSON Payload | String | {"cards":[{"sections":[{"widgets":[{"image":{"imageUrl":"https://..."}},{"buttons":[{"textButton":{"text":"OPEN IN GOOGLE MAPS","onClick":{"openLink":{"url":"https://..."}}}}]}]}]}]} | Yes | Specify the JSON payload to send with the message. For examples of a messages payload, see this [article](https://developers.google.com/chat/api/guides/message-formats/cards).  
  
#### Run on

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### Case Wall

Result Type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_If a message is sent successfully (is_success=True):_ "Message was sent successfully."**The action should fail and stop a playbook execution:******_If the provided JSON payload is not valid:_ "Error executing action "Send Advanced Message". Reason: the provided message JSON payload is not valid. " _If a critical error, like no connection or wrong credentials is reported:_ "Error executing action "Send Advanced Message". Reason: {0}''.format(error.Stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
