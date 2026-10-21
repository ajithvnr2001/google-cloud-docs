---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-emergency/
title: Emergency and special services calling \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:02:03.586711+00:00
---

# Emergency and special services calling  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-emergency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Emergency and special services calling Stay organized with collections  Save and categorize content based on your preferences. 

If your administrator [sets up emergency and special services calling](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#set-up-emergency-and-special-services-calling), as an agent in the US or Canada you can make calls to emergency services from the call adapter. Agents in Canada can also make calls to other special services. When you make a call to emergency or special services, you only need to dial the three-digit number for the service. You don't need to dial any dial codes. For more information, see Three-digit emergency and special services numbers.

As an agent, you can do the following:

  * Call emergency and special services.

  * Add an end-user to an ongoing call with an emergency or special services operator.

  * Receive a callback from an emergency or special services operator (for example, in the case of a dropped call).

  * Add a call from an emergency or special services operator to an ongoing call with an end-user.

  * Remove the emergency or special services operator from a call to finish the call with the end-user.

  * Leave a call and let the emergency or special services operator and the end-user finish the call.




## Three-digit emergency and special services numbers

The following table shows the emergency and special services numbers that are available in the US and Canada.

**US emergency numbers** | **Canada emergency numbers** | **Canada special service numbers**  
---|---|---  
911 - Emergency  | 911 - Emergency  | 211 - Public information and referral services   
933 - Emergency test  |  | 311 - Non-emergency municipal government services   
|  | 411 - Local directory assistance   
|  | 511 - Weather and traveler information services   
|  | 611 - Repair service   
|  | 711 - Message relay service (MRS)   
|  | 811 - Non-urgent health care telephone triage service   
|  | 988 - Suicide and crisis lifeline   
  
## Call emergency or special services

To call emergency or special services, follow these steps:

  1. In the CCAI Platform portal, click call **Call**. The call adapter appears.

  2. Click **Start call**. The **Outbound call** screen appears.

  3. Dial the three-digit emergency or special services number that you want, and then click **Next**. The **Calling** screen appears. No intermediary screen, such as the call information screen, appears.

  4. When the call is answered, a **Calling emergency number** banner is displayed.




## Add an emergency or special services call to an ongoing call

To add an emergency or special services call to an ongoing call with an end-user, follow these steps:

  1. [Receive or make a call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-calls).

  2. In the **Call** screen, click **Transfer / Add**. The **Transfer / Add party** screen appears.

  3. Click the **Dialpad** tab.

  4. Dial the three-digit emergency or special services number that you want, and then click **Add number**.

  5. When the call is answered, the ![Icon that indicates three callers.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/three-callers.png)**Callers** icon indicates that there are three callers on the call.

  6. To see the callers on the call, click the ![Icon that indicates three callers.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/three-callers.png)**Callers** icon. The **Participants** screen appears. You should see the end-user and the emergency number in the list of participants.

  7. Do one of the following:

     * Stay on the call until it's completed.

     * Leave the call. To leave the call, do the following:

       * Click **Leave Call**. A confirmation dialog appears.

       * Click **Leave Call**. The end-user and emergency or special services remain on the call.


**Note:** If you receive a call from emergency or special services (for example, due to a callback after a dropped call) you can add an end-user to the call in a similar way.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
