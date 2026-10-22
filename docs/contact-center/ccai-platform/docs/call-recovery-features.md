---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recovery-features/
title: Call recovery features \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:08.456625+00:00
---

# Call recovery features  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recovery-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Call recovery features Stay organized with collections  Save and categorize content based on your preferences. 

After a call is connected to an agent, if the call fails or is unexpectedly ended from the agent's side, then the call goes into a call recovery flow. Depending on the type and duration of a failed call, the call recovery can either be automatic or manually initiated by an agent.

## Why calls are unexpectedly ended or dropped

A call might drop unexpectedly for the following reasons:

  * The agent closes the active tab or browser during the call.

  * There are network issues on the agent's side—for example, the Wifi drops or the bandwidth is exceeded.

  * There are network issues on the caller's side.




## Mobile SDK: automatic call recovery

If the agent's connection is interrupted or unexpectedly ended from their voice provider, Contact Center AI Platform (CCAI Platform) waits for up to one minute for the agent to be reconnected. If the agent reconnects, the call is automatically recovered and both the agent and caller can resume the call.

If the agent doesn't reconnect within one minute, or if the caller hangs up, the call is ended and the status is set to `Finished`.

## Manual callback

### End the call and call back

When an agent is on a call, they have the option to end the call and call back. This is useful if there is a bad connection or the caller has difficulty hearing.

Click **End and call back** to end the call and place a new outbound call to the caller with a new Call ID. If this call originated as a VoIP call from the Mobile SDK, the VoIP is used to call the end-user back. If this was an IVR call or a Mobile SDK PSTN call, the call is placed back to the end-user through PSTN.

### Short call recovery

If **Automatic Wrap up** is enabled and the call connects but is ended within 10 seconds of connecting, the call adapter appears with the message, "The call was too short". The agent can click either **Call back** , or **Back to Available** , placing them back in `Available` status.

The agent can do the following:

  * Click **Call back** to place a new outbound call to the caller with a new call ID.

  * Click **Back to Available** to set the agent's status to available.




A timer also counts down to automatically set the agent's status back to `Available`. The timer is set for 15 seconds by default.

See [Wrap-up settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#wrap-up-settings) for more information about automatic wrap-up settings.

### Voicemail callback

When an agent listens to a voicemail, they have the option to click **Call back**. This places a new outbound call and sets the status of the original voicemail call to `Voicemail Read`.

### Scheduled call recovery

If an end-user schedules a call through the web SDK or mobile SDKs and doesn't pick up the call at the scheduled time, a callback option is presented to the agent to create a new outbound call. The original call ID has the following fail reason: `End-user No Answer`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
