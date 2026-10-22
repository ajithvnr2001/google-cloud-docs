---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/after-hour-deflection/
title: After hour deflection for calls and chats \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:15.936060+00:00
---

# After hour deflection for calls and chats  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/after-hour-deflection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  After hour deflection for calls and chats Stay organized with collections  Save and categorize content based on your preferences. 

Customize your consumer's experience by configuring specific deflection paths for when consumers try to contact you outside of your Hours of Operation are first configured, then deflection is enabled and configured at the global level in the Call Settings and Chat Settings pages. Deflection after hours of operation can be further customized for each leaf-queue in **Settings > Queue**.

The global Languages and Messages settings includes the setup for the voice recordings or Text-to-speech prompts needed once certain settings are enabled.

Add the appropriate messages once announcements or deflections are enabled.

## Details

When After Hour deflection is enabled, calls and chats will be deflected based on the specific operation hours for the queue, language, or channel the consumer has selected or has been routed to. While deflection options and configuration is done on the Call settings and Queue Settings pages, the actual hours are set on the **Support Center Details** settings page. There are multiple options you can offer callers once this setting is enabled.

### Steps to fully enable and configure After Hour deflection

  1. Configure hours of operation for your environment - global and custom hours for each queue, channel, and language as needed.

  2. Enable and configure After Hour deflection for calls.

  3. Enable and configure After Hour deflection for chats.

  4. Configure per-queue deflection options (optional).

  5. Configure and upload appropriate greetings at **Settings > Languages and Messages**.




## CCAI Platform configuration

To configure after hours, follow these steps.

### Enable and configure After Hour deflection for calls

  1. Go to **Settings** > **Call**.

  2. Toggle **Enable After Hour Deflection** to **On** to deflect callers when dialing in after scheduled hours of operation (set at **Settings > Support Center Details**).

  3. Mark the checkbox **Allow transfers to queues outside of operation hours** for the following behavior:

Agents will be able to see the following queues as options to transfer to in the Agent Adapter:

All queues within operating hours

All queues that are outside of operation hours with after hour deflection enabled

All queues that are outside of hours of operation with no deflection enabled and active, logged-in agents

All queues that are after hours with an assigned virtual agent in 24-hour availability mode

Agents won't be able to see the following types of queues:

All queues that are outside of operating hours with an assigned virtual agent limited to queue hours of operation




### Select Mobile and Web SDK call deflection options

When selected, visual options will be displayed when outside of hours of operation. The regular call or chat option won't appear in the UI and the options you select will be the only options available.

  * **After Hours Deflection** : Deflects consumers by presenting alternative options.

    * **Scheduled Call** : Shows a set of available times within the hours of operation for the queue to request a call.

    * **Email** : If after-hour deflection is enabled for email, a message is presented to end-users after hours asking them to contact the email address listed. The email address listed is always the email listed in support center details.

      * Web: gives the customer the email address to contact.

      * Mobile: default email app is launched with an email address in the "To" field, and data like app version and device type can be added to the email body by default.

      * Email address is set in **Settings > Support Center Details:**

    * **Phone Number** : _Only for Mobile SDK._ Deflects consumers to another phone number. Shows as "Call now" and displays the number the phone will be dialing.

    * **Voicemail** : _Only for Mobile SDK._ Allows customers to leave a voicemail. Shows as "Leave a callback message." Voicemails will be delivered to agents assigned to the selected queue for calls.




#### Example deflection UI

Example Mobile SDK that is set to deflect to all options After Hours.

### Select IVR call deflection options

**After Hours Deflection** : During the set hours in the Support Center Details, calls will deflect to the selected option.

**Queue:** If you have a 24-hour queue or just one with longer hours set, all calls will be sent to this queue.

**Phone Number** : Deflects caller to another phone number.

**Voicemail** : Allows caller to leave a voicemail.

Agents assigned to the queue that was called when operating hours were reached will be alerted of voicemails left as a result of this deflection setting. If this is applied to a top-level queue with no assignments, voicemails will be available in your CRM.

The message can be customized in **Settings** > **Languages & Messages** > **Voicemail** message.

Additional Voicemail message options are available under **Custom Callbacks**.

Voicemail - Phone Number Blocked

Voicemail - Request Phone Number

Voicemail - Phone Number Input Success

**Message Only:** "After Hour Deflection" message plays and the call ends. The message can be customized in **Settings** > **Languages & Messages** > **After Hour Deflection** message.

Click **Set Deflection** to **Save** the settings.

### Enable and configure After Hour deflection for chats

  1. Go to **Settings** > **Chat.**

  2. **Enable After Hour deflection** : Enable to deflect chat requests outside of operating hours.

  3. If After Hour Deflection is disabled, mark the checkbox **Allow transfers to queues outside of operation when After Hours Deflection is disabled** for the following behavior:

Agents will be able to see the following queues as options to transfer to in the Agent Adapter:

     1. All queues within operating hours

     2. All queues that are outside of hours of operation with no deflection enabled and active, logged-in agents

     3. All queues that are after hours with after hour deflection enabled

     4. All queues that are after hours with an assigned virtual agent in 24-hour availability mode

Agents won't be able to see the following types of queues:

All queues that are outside of operating hours with an assigned virtual agent limited to queue hours of operation

  4. **After hour deflection options** : Select **Email** to deflect an end-user to email if chatting in after hours. If after-hour deflection is enabled for email, a message will be presented to consumers after hours asking them to contact the email address listed. The email address listed will always be the email listed in support center details. Otherwise, the customer will be presented with the email address set in **Settings** > **Support Center Details** from within the body of the chat interaction.

  5. Click **Set Deflection** to save.




## Configure queue-specific settings

Available for IVR, Mobile, and SMS channels. Not available for Web.

### IVR

  1. Go to **Settings** > **Queue** > **IVR**.

  2. Click the queue you want to edit.

  3. Scroll to Custom After Hours Deflection and toggle switch to ON.

**Message** : A message will play, then end the call. Default message set in **Settings** > **Call** or a Custom Greeting can be used.

**Queue** : Deflects the caller to another queue.

**Phone number** : Redirect callers after hours to a phone number. Additional charges for call time apply.

**Voicemail** : directs the caller to voicemail with an option to customize the voicemail greeting.

  4. Click **Set After Hour Deflection** to save.




### Mobile

Mobile configuration allows for either deflecting to a queue, or a combination of other deflection options. If you are deflecting to a queue, the consumer cannot also have another option like leaving a voicemail.

  1. Go to **Settings** > **Queue** > **Mobile**.

  2. Click the queue you want to edit.

  3. Go **Custom After Hours Deflection** and toggle switch to ON.

Deflect to Queue: deflects the consumer to another queue

**OR**

Deflection Options (select one or more):

**Scheduled Call** : When scheduled calls are enabled in the Channel Settings for this queue, you can select this option to present consumers with timeslots for a scheduled call during operating hours.

**Email** : If after-hour deflection is enabled for email, a message will be presented to end-users after hours asking them to contact the email address listed. The email address listed will always be the email listed in support center details. Default email app is launched with an email address in the "To" field, and data like app version and device type call be added to the email body by default. Email address is set in **Settings** > **Support Center Details**.

**Phone Number** : Deflects consumers to another phone number. Shows "Call now" and displays the number the phone will be dialing.

**Voicemail** : Allows consumers to leave a voicemail. Shows as "Leave a callback message." Voicemails will be delivered to agents assigned to the selected queue for calls.

  4. Click **Set After Hour Deflection** to save.




### SMS

  1. Go to **Settings** > **Queue** >SMS.

  2. Click the queue you want to edit.

  3. Scroll to SMS Chat System Messages section and mark the checkbox next to **Enable after hour message**.

  4. Enter the text message to send to consumers.

  5. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
