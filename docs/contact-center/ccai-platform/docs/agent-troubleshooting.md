---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-troubleshooting/
title: Agent adapter troubleshooting \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:26.697649+00:00
---

# Agent adapter troubleshooting  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent adapter troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with the agent adapter.

## Troubleshooting tools

The following tools can help troubleshoot agent network issues.

### Call statistics & Twilio network test

  * The [VoIP Network Assessment Test](https://myconnectionserver.visualware.com/portals/voip-test/voip-assessment-test) monitors network health. You can run it from multiple computers on the network to monitor network health and call traffic capacity. Google recommends running network tests throughout the day.

  * The [Twilio Network test](https://networktest.twilio.com/) runs a range of tests related to connecting to Twilio's TURN servers that handle calls. This tool checks your UDP and TCP connections and gives an estimated number of voice or chat sessions your connection might be able to support. This tool also tests the ability to connect and take calls over the Twilio network. Google recommends that you allow the entire test to finish. We also recommend that you test throughout the day to monitor changing network loads.




### My Traceroute (MTR)

MTR is a tool that combines ping and traceroute into one diagnostic tool. It is available for [Microsoft Windows](https://sourceforge.net/projects/winmtr/files/WinMTR-v092.zip/download) and [Mac OS](https://libraries.io/homebrew/mtr). MTR probes routers on the route path by limiting the number of hops individual packets can traverse and listening to their expiry responses. It regularly repeats this process, usually once per second, and keeps track of the response times of the hops along the path. The target IP addresses are the Twilio call servers.

## Agent adapter messages

The following list shows messages that can appear in the agent adapter.

### Access errors

"notAccessible.rolesTitle": "**You are logged in** ",

"notAccessible.as": "**as** ",

"notAccessible.rolesDescription": " **login as agent account** ",

"notAccessible.noRolesTitle": "**You need to be assigned to a team first.** ",

"notAccessible.noRolesDescription": "**Please ask to your administrator.** ",

"notAccessible.logOut": "**Log out** ",

"notAccessible.webApp": "**Go to the web app** "

### Call disconnected during payment

"inCall.statusDisconnectedDuringPayment": "**The call was disconnected during payment** ",

### Call dropped

"participants.failed": "**Call dropped** ",

"participants.statusFailed": "**call dropped...** "

### Call failed to initiate

"toastr.failedToStartCall": "**Failed to start a call.** ",

"toastr.failedToCallNoPhoneNumber": "**Failed to call: No phone number.** ",

"toastr.switching": "**connecting via`voipProvider​`**"

### Call failed

"inCall.failReason.unknown": "**Oops, something went wrong with the call.** "

### Chat canceled

"inChat.cancled": "**This chat is canceled** "

### Chat failed to load

"inChat.loadingFailed": "**Loading failed** "

### Chat timed out

"inChat.timedOut": "**This chat timed out** "

### Connection errors

"toastr.crmCallFailed": "**Oops! Looks like we are having trouble connecting. Please refresh the browser or contact support if the problem persists** "

### EU rejected, abandoned, or call expired

"inCall.failReason.euRejected": "**The call is rejected <br>by the customer.**",

"inCall.failReason.expired": "**The call is expired.** ",

"inCall.failReason.euAbandoned": "**The call is abandoned <br>by the customer.**",

"inCall.failReason.canceled": "**The call is canceled.** ",

### Failed transfer

"transfer.failedTitle": "**Transfer failed** ",

"transfer.failedCallDescription": "**Transferred call hasn't been picked up.** ",

"transfer.failedChatDescription": "**Transferred chat hasn't been picked up.** ",

### Invalid device

"actions.smartActionProgressTitle.invalidDevice": "**No`deviceType​` app**"

"actions.smartActionProgressInfo.invalidDevice": "**User is using`​deviceType​`**"

For more info check out [Send SMS to Launch Smart Actions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Sending_SMS_to_Launch_SmartActions/index.md#UUID-11c3da84-509c-e4ce-8b95-0f630f3a9ac0)

### Misc. errors

"toastr.error": "**ERROR** "

"toastr.wrongPhoneNumber": "**Wrong phone number`phoneNumber`**"

"toastr.logoutWhileInCall": "**You cannot log out when in call.** "

"toastr.unverifiable": "**The user's mobile device doesn't support automatic verification. Please verify through questions.** "

"toastr.failedToCallDirectly": "**Failed to call directly.** "

"toastr.errorWhileFetchingVoicemail": "**Error occurred when fetching voicemail data :`error`**"

### Missed calls

"waitingCalls.missedCallTitle": "**Missed Call** ",

"waitingCalls.missedCallInfo": "**At`missedCallAt`**"

### Permission errors

"permissionErrors.notificationTitle": "**Browser notifications blocked!** ",

"permissionErrors.notificationDescription": "**You are not able to receive notifications. Please see how to allow notifications** ",

"permissionErrors.autoplayTitle": "**Incoming calls are now muted due to inactivity** ",

"permissionErrors.autoplayDescription": "**Please click on the calling window to restore your audio** ",

"permissionErrors.here": **"here** ",

"permissionErrors.micTitle": "**Microphone turned off!** ",

"permissionErrors.micDescription": "**You will not be able to take calls. Please see how to allow microphone access** ",

"permissionErrors.refreshDescription": "**I changed the settings, let's see:** ",

"permissionErrors.refresh": "**REFRESH** ",

"permissionErrors.goToActivateTabDescription": "**Click to go to active CCAI Platform adapter** ",

"permissionErrors.go": "**GO** "

See [Granting Notification and Microphone Permissions](https://docs.cloud.google.com/contact-center/ccai-platform/Getting_Started/index.md#UUID-cdaaf0b7-c7b5-0593-a9f7-1afde4ee4a2b)

### Recovered calls

"inCall.statusRecovered": "**This call is recovered.** ",

**Redaction Errors:**

"toastr.unableToStartRedaction": "**Unable to start redaction** ",

"toastr.unableToStopRedaction": "**Unable to stop redaction** "

For more info about this feature, see [Call Redaction](https://docs.cloud.google.com/contact-center/ccai-platform/Queue_and_Menu_Setup/index.md#UUID-f3dfea58-a8d5-d301-8834-6f52a1c643e9)

### Restart calls

"inCall.restart": "**RESTART** ",

"inCall.callBack": "**CALL BACK** ",

### Short calls

"inCall.statusTooShort": "**The call was too short.** ",

### Target time exceeded

"waitingCalls.targetTimeExceeded": "**Target pickup time exceeded** "

See [Target metrics](https://docs.cloud.google.com/contact-center/ccai-platform/docs/target-metrics)

### Teammate answered call

"toastr.noCommsTitle": "**On to the next one** ",

"toastr.noCommsDescription": "**A teammate answered the call.** ",

"toastr.noComms": "**No worries! Looks like someone took care of it. Next one!** "

### Unsuccessful call transfer

"transfer.notFound": "**No available agent** ",

"transfer.unavailable": "**Unavailable** ",

"transfer.notFoundMenu": "**No available queue or agent** ",

"transfer.notFoundUser": "**No available agent** "

### Unsuccessful chat transfer

"inChat.transferFailed": "**Transfer failed** ",

"inChat.please": "**please** ",

"inChat.tryAgain": "**try again** ",

## CRM Unavailable: Taking calls and chats in CCAI Platform

Occasionally CRMs like Zendesk and Salesforce will become unavailable. During those periods of unavailability, you can take calls and chats right from the CCAI Platform portal. Once your CRM becomes available again, all tickets or cases will be created for the calls and chats you handled in the CCAI Platform portal. Information added to your CRM ticket (all consumer information, pictures, screenshots, etc.) is stored directly in the CRM.

### Feature details

  * Call and chat sessions will be routed to Agents in the same manner as in your CRM,

  * If smart actions are used, the Agent won't be able to view images and videos received, but they will be uploaded to the CRM record when the CRM is available again.

  * The CCAI Platform portal is always available for taking calls and chats but is not recommended unless necessary since the Agent lacks the context provided in CRM records.

  * CCAI Platform will continue to retry CRM record creation until your CRM is back online. Once your CRM is available again, the records from the calls and chats handled will be created in your CRM.




### Signing in to the CCAI Platform portal

You will be able to sign in using your normal username and password.

  1. Navigate to your company's CCAI Platform page (ask your manager if you're unsure).

  2. Enter your work email address - the same one you use when login into your CRM (Zendesk, Salesforce, Kustomer etc.).

  3. Enter the password you use to login to your Agent Adapter in your CRM.

Example of CRM login screen for reference:

  4. Click **Login**.

  5. If you forgot your password, click **Forgot password** and follow the instructions in the email you receive.




### Taking calls and chats in the CCAI Platform portal

Although you are taking calls or chats in a different "place," the interface will be very familiar, so you don't need to learn anything new.

  1. Click the phone icon to show the phone adapter. You can receive and place calls in the same way from here as you do in your CRM.

  2. Click the chat icon to show the chat adapter and can take multiple chats in the same way you do from your CRM. The main difference is that you won't have the CRM record behind the adapter with more information about the consumer.

  3. Once your CRM becomes available, all records (cases/tickets/opportunities) will be created for the calls and chats you handled in the CCAI Platform Portal. Information added to your CRM ticket (all consumer information, pictures, screenshots, etc.) is stored directly in the CRM. CCAI Platform does not store your consumer data.




## Agent network strength indicator

To help agents, supervisors, and admins work remotely, the Agent Call adapter displays a network strength indicator. Using the call's MOS score, this real-time indicator shows the measure of network strength and when too low, will indicate if the call quality would be impacted. Agents can click the indicator to see more information about the current detected signal strength.

If agents report poor connection indicated, troubleshoot with [Contact Center Network, Software, and Hardware Requirements](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Getting_Started) or contact support.

### Agent experience

  * From the agent adapter, the indicator is displayed in the upper-right corner.

![agent adapter](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162fa7808aa292.png)

  * To see more details about the current detected signal strength, click the icon.

  * The panel opens with details that can help troubleshoot the issues.

![agent adapter troubleshoot](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162fa7808aed7a.png)

Clicking **Send Report** generates a report to support. Once you have done this, the support team will analyze the report and provide feedback. Contact support for your report related feedback.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
