---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-companion/
title: Call companion \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:22.817765+00:00
---

# Call companion  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-companion/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Call companion Stay organized with collections  Save and categorize content based on your preferences. 

[Call companion](https://docs.cloud.google.com/dialogflow/cx/docs/concept/call-companion) is a Dialogflow CX feature that enhances the customer experience by providing a supplementary interactive visual interface on the end-user mobile devices during voice interactions with Dialogflow CX virtual agents. This interface allows for information exchange and end-user interactions.

For Contact Center AI Platform (CCAI Platform), by integrating virtual agents with the existing telephony/IVR infrastructure, the platform enables more personalized customer interactions. In addition, leveraging the existing SMS session-less capabilities, all communication is handled through a single platform. 

## Prerequisites

Prior to being able to use the call companion service with CCAI Platform, the following prerequisites must be met:

  1. A provisioned CCAI Platform.

  2. A Dialogflow CX virtual agent integrated with an IVR queue within the CCAI Platform instance.

  3. SMS capability enabled for a designated phone number associated with the CCAI Platform instance, and not being used for SMS Chat.




## Limitations

  * The SMS capability cannot use the same phone number as the IVR, due to the employment of a session-less SMS API.

  * The SMS API is disabled by default and has to be enabled. It cannot be enabled through the CCAI Platform user interface. A workaround is detailed here: 

    1. Open the Chrome web browser, sign in to the CCAI Platform portal as a user with administrator role.

    2. Open the Chrome .

    3. Click the **Console** tab, and then copy and paste at the prompt.
    
    var xhttp = new XMLHttpRequest();
      xhttp.open("PATCH", "/v1/settings/sms", true);
      xhttp.setRequestHeader("X-UJET-XSRF-TOKEN", localStorage.getItem('xsrf-token'));
      xhttp.setRequestHeader("X-XSRF-TOKEN", localStorage.getItem('xsrf-token'));
      xhttp.setRequestHeader("Accept", "application/json, text/plain, */*");
      xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
      xhttp.send(JSON.stringify({"sessionless": {"enabled": true, "auto_response_message": "This message couldn't be delivered because the sender does not support responses"}}));
    




## Architecture

The workflow will be structured in this manner:

  * End-user calls the telephony/IVR queue.

  * Telephony initiates session request to Dialogflow API.

  * Dialogflow CX starts a conversation.

  * Dialogflow CX creates a call companion URL and triggers a webhook to send SMS to the user using the CCAI Platform session-less SMS API.

  * CCAI Platform SMS server sends the SMS message to the user.

  * End-user opens call companion web UI using the URL present in SMS.

  * End-user can now interact either using the Voice channel or using the screen, leveraging the call companion API.




## Configuration

This section outlines the steps needed to enable the call companion service. 

### Enable data parameters

Data parameters will be leveraged in order to pass necessary information from [CCAI Platform to the Dialogflow CX virtual agent](https://docs.cloud.google.com/contact-center/ccai-platform/docs/pass-data-parameters).

  1. Go to the CCAI Platform portal for the instance.

  2. Go to **Settings > Queue**.

  3. Click **Edit/View IVR Queue**.

  4. Within the IVR Queue, find the queue that has the virtual agent assigned and click **Edit virtual agent assignments**.

  5. Within **Pass data parameters** you can add parameters.

     1. Click **Add parameter**.

     2. Add the following parameters:


Parameter Name | Description | Dynamic or Fixed | Value  
---|---|---|---  
ccTo | Phone number to send SMS to | Dynamic | Session metadata - ANI  
ccFrom | Phone number to send SMS from | Fixed | +13211231212  
ccaipHost | Your CCAI Platform hostname (no https:// or trailing /) | Fixed | myccaip.uc1.ccaiplatform.com  
projectID | The Google Cloud Project ID that your DF Virtual Agent resides in | Fixed | my-gcp-project  
**Note:** Make sure to turn on the toggle button and click save on top of the page.

### Create API credentials

To be able to send the outbound SMS using the CCAI Platform session-less API, the following steps must be taken:

  1. Go to the CCAI Platform portal for the instance.

  2. Go to **Settings > Developer settings**.

  3. Go to the later section **API credentials**.

  4. Click **Add API credentials**.

  5. Provide a name for these API credentials, for example **Sessionless SMS**. An API token will be generated and displayed. 

  6. Copy this API token. 




### Set up webhook in Dialogflow CX virtual agent

The following steps will enable you to setup a webhook in Dialogflow CX. This is necessary to be able to send the outbound SMS using the CCAI Platform session-less SMS API.

  1. Go to the [Dialogflow CX virtual agent](https://dialogflow.cloud.google.com/cx/).

  2. Select the Google Cloud project from the drop-down list at the top.

  3. In your Google Cloud project, select your Dialogflow CX virtual agent.

  4. From the **Manage** tab, you will find the **webhooks** section option.

  5. Click **Create new**.

  6. Provide a display name for the webhook, such as **Send SMS**.

  7. Set the webhook URL to the value:

`https://$session.params.ccaipHost/apps/api/v1/sessionless_sms`

  8. Select **Flexible** as the **Subtype**.

  9. Select **Post** as the **method**.

  10. For the request body, provide the following:
         
         {
           "from_phone": "$session.params.ccFrom",
           "to_phones": [
             "$session.params.ccTo"
           ],
           "messages": [
             "Hello from Google Call Companion! To interact with the call visually click here g.co/cloud/df-callcompanion#$session.params.projectID%2Fglobal%2F$request.session-id&$session.params.call-companion-auth-code  Text STOP to stop all SMS."
           ]
         }
         

**Note:** You can adjust the content of the SMS message by editing the **message** value.
  11. Authentication in **Basic Auth** , provide the first part of CCAI Platform hostname, for example if your CCAI Platform instance host is `myccaip-abc123.uc1.ccaiplatform.com`, provide `myccaip-abc123` as your username.

  12. Pass the API Credential that you created in the earlier API credentials stage as the password.

  13. Click the **save** button at the top of the page.


**Note:** The CCAI Platform hostname is the instance name, region code, and ccaiplatform.com. Take the first part up to the first period as the username for authentication.

### Enable Webhook in virtual agent flow

Now that the webhook has been created in the virtual agent from the previous steps, change the virtual agent to use this webhook at the chosen point in the conversation with the end user. 

Some customers choose to send this SMS message at the start of the session when the user first connects, while others choose to only send the SMS message for certain parts of the conversation or flows.

  1. In the Dialogflow CX virtual agent, go to the conversational flow under **Build**.

  2. Click the **Routes** within the page.

  3. Select a route to view the route configuration.

  4. Go to the **Parameter presets** section.

  5. Add a preset parameter with parameter name `call-companion-auth-code` and value `$sys.func.URL_ENCODE($session.params.call-companion-auth-code)`. Using the Dialogflow CX system function `$sys.func.URL_ENCODE` URL encodes the call companion auth code because it might contain values that need encoding.

  6. Go to the **Webhook** section.

  7. Enable **Webhook** and select the webhook created for sending the SMS.

  8. Specify the fulfillment **tag**.

  9. Click the **save** button on the top.




### Enable call companion in conversation profile

For Dialogflow CX to be enabled for call companion support, it is necessary to activate this service in the conversational profile.

  1. In the Dialogflow CX virtual agent, go to the **Shared resources** and then conversation profile.

  2. Select the virtual agent.

  3. Enable the **call companion** option and click the **save** button.




## Test call companion

To test call companion, place a voice call into the Contact Center AI Platform queue with the virtual agent assigned.

**Note:** Make sure that the number you set to send SMS from (ccFrom data parameter) is not the same phone number.

When the conversation reaches the point where you call the webhook, you should receive the SMS message. From the SMS content, you can open the URL which will open the call companion UI and you can see the conversation as well as interact with the ongoing call. You can interact as regular voice call or with chat.

## Using rich content

The call companion interface uses the Dialogflow CX Messenger. This supports the ability to provide [rich content](https://docs.cloud.google.com/dialogflow/cx/docs/concept/call-companion#rich-content), including buttons.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
