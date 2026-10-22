---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-transfer/
title: Transfer calls \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:34.475680+00:00
---

# Transfer calls  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-transfer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Transfer calls Stay organized with collections  Save and categorize content based on your preferences. 

In Contact Center AI Platform (CCAI Platform), you can either **warm transfer** or **cold transfer** end-users to another agent or queue. In a warm transfer the end-user stays on the line and talks to the next agent before the transfer is complete. Cold transfers assign the end-user to the new agent or queue without the original agent staying on the line.

## Transfer details

Transferring a call to a **Team** is not supported at this time. Agent assignments are based on queues. Set up a team-specific queue if this option is required for your workflow.

  * _Available_ agents can receive transfer calls. _Unavailable_ Agents can also receive transfers, if enabled at **Operations Management > Agent Status.**

  * For IVR calls, agents will only see the IVR-specific queues. The same applies to Mobile and Web calls.

  * **Automatic Redirection** : When a call is transferred to a queue with an Automatic Redirection active, the call will follow the Automatic Redirection path just as a new call would. **Leave Ongoing Calls with 3rd Parties** must be enabled **Settings > Call**.

  * **After Hour deflection** : If the _Automatic Redirection_ for a queue is set to _message_ or _voicemail_ , transfers to a queue outside of operating hours will follow the After Hour deflection. If Automatic Redirection is set to _queue_ or _phone number_ , Automatic Redirection will take priority over After Hours deflection.

  * **Overcapacity Deflection** : Warm transfers don't trigger the Overcapacity Deflection. Only cold transfers are deflected when Overcapacity Deflection is enabled.

  * **Call Priority** : Transferred calls have higher priority than standard inbound calls by default.

  * **Call Duration** : The call duration starts at the initial call pickup and remains for the duration of the call to properly represent how long the caller has been on the call. It does not reset when transfers take place.

  * **Call Recording** : When enabled, the call recording won't capture the portion of the call after the agent leaves if a call is transferred to a 3rd party.




## Warm transfers

Warm transfers can be done with the end-user on hold or not on hold, or a combination of both. We suggest putting the caller on hold so that you can bring them in as soon as the transfer is about to be completed. This gives you a chance to tell the next agent why they are being transferred and any other details that makes the experience smoother for the end-user. Warm transfers don't trigger Overcapacity Deflection (if configured).

  * Click **Hold** to place caller on hold (they will hear hold music).

  * Click **Transfer** to initiate the transfer action.

  * You can use the search field to search for an agent, manager, or queue. Predicted wait times, after hours, and redirection settings for the queue are included in this view so you have an idea of what the caller can expect. A green phone icon indicates the queue is set to Automatic Redirection. A moon icon indicates the queue is outside of the set hours of operation.

  * After the new agent joins the call, the caller is still on hold and cannot hear the agent's conversation. Click **Hold** again to take the caller off of hold.

  * Click **End call** to complete the transfer.




## Cold transfers

A cold transfer occurs when an agent transfers a call to another agent or queue and then immediately exits the call. The transferring agent doesn't stay on the call to brief the next agent or to confirm that the call is answered. When the receiving agent answers, the call begins immediately. Cold transfers are useful in a busy contact center where the transferring agents don't have time to wait with the caller until the next agent answers.

**Note:** Cold transfers can only be sent to agents or leaf queues. Cold transfers to branch queues, to third parties, or to queues that auto-direct to third parties are not supported.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
