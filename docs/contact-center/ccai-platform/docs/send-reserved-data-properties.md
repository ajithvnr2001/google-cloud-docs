---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-reserved-data-properties/
title: Send reserved data properties \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:55.072773+00:00
---

# Send reserved data properties  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-reserved-data-properties/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Send reserved data properties Stay organized with collections  Save and categorize content based on your preferences. 

With reserved data properties, you can send information about an end-user to CCAI Platform when a chat or call session begins, or even after a session has begun. CCAI Platform displays this end-user information in the agent adapter in the form of user profile flags. These flags can help an agent or supervisor determine how to handle a session. There are user profile flags for unverified or verified customer, bad actor, and repeat customer.

Here are the reserved data properties that you can send to CCAI Platform:

  * **`reserved_verified_customer`** : indicates that you consider this end-user to be a legitimate customer.

  * **`reserved_bad_actor`** : indicates that you consider this end-user to potentially be a bad actor. This might be due to observing fraudulent behavior or determining that the contact is from a spam campaign.

  * **`reserved_repeat_customer`** : indicates that you have determined that this end-user has contacted your contact center before.




You determine which reserved data parameters apply to an end-user based on your own systems and processes.

You can send reserved data properties to CCAI Platform in the following ways:

  * Send reserved data properties using the SDKs

  * Send reserved data properties using the Apps API

  * Send reserved data properties using SIP headers




## Send reserved data properties using the SDKs

You can send reserved data properties to CCAI Platform using the following SDKs:

  * [Web SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk#reserved-data-properties-web-sdk)

  * [Android SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#reserved-data-properties-android-sdk)

  * [iOS SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide#reserved-data-properties-ios-sdk)




## Send reserved data properties using the Apps API

You can send reserved data properties to CCAI Platform using the Apps API, even after a session has begun. To send reserved data attributes during a chat or call session, see the following:

  * [Update reserved data attributes during a call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-call#update-reserved-data-attributes-during-call)

  * [Update reserved data attributes during a chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-chat#update-reserved-data-attributes-during-chat)




You can also get reserved data properties during a call. See the following:

  * [Get reserved data attributes during a call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-call#get-reserved-data-attributes-during-call)

  * [Get reserved data attributes during a chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-chat#get-reserved-data-attributes-for-chat)




## Send reserved data properties using SIP headers

You can send reserved data properties to CCAI Platform using SIP headers.

Here is an example reserved data properties in a SIP header:
    
    
    setting: {
      redirection: {
        option: "sip",
        sip: {
          uri: "Destination SIP URI",
          data_parameters_enabled: true | false,
          data_parameters: [
            {
              field: "verified_customer",
              type: "dynamic",
              source: "ujet_metadata",
              source_field: "Incoming Field"
            },
            {
              field: "bad_actor",
              type: "dynamic",
              source: "ujet_metadata",
              source_field: "Incoming Field"
            },
            {
              field: "repeat_customer",
              type: "dynamic",
              source: "ujet_metadata",
              source_field: "Incoming Field"
            }
          ],
          data_records: {
            in_metadata: true | false,
            in_crm_record: true | false
          }
        }
      }
    }
    

### Support for virtual agents

If you have a virtual agent (a support agent or a virtual task assistant) that performs end-user verification, the virtual agent can pass the end-user verification information to CCAI Platform. This indicates that the end-user is a legitimate customer. To enable this, you need to configure your virtual agent.

### Configure a support agent to pass the Verified Customer parameter

To configure a support agent to pass the Verified Customer parameter, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Queue**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click a queue that has a virtual agent assigned to it. For more information, see [Assign virtual agents to queues](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent#assign_virtual_agents_to_queues).

  4. In the **Settings for Test** pane, go to **Channel Settings**.

  5. Click **Edit Virtual Agent Assignments**.

  6. Under **Data Parameters** , click **Add Parameter**. The **Add Parameter** dialog appears.

  7. To define the parameter, do the following:

     1. Click the **Type** field, and then select **Dynamic**.

     2. Click the **Source** field, and then select **Session Metadata**.

     3. Click the **Incoming Field** field, and then select **Verified Customer**.

     4. In the **Destination Field** , enter a field name that your CRM will recognize, and that Dialogflow CX will use as a parameter. A preview of the parameter appears in the **Preview** field.

     5. Click **Save** , and then click **Save** again.




### Configure a virtual task assistant to pass the Verified Customer parameter

To configure a virtual task assistant to pass the Verified Customer parameter, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Virtual Agent**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Virtual Agent**.

  2. Go to the **Virtual Agents** pane and find the virtual task assistant that you want to configure. This should be a virtual agent with a **Call** label and an **Assistant** label. For more information, see [Create a virtual task assistant](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-task-assistants#create-virtual-task-assistant).

  3. Click edit **Edit** for the virtual agent that you are configuring. The **Edit a Virtual Task Assistant** dialog appears.

  4. Under **Data Parameters** , click **Add Parameter**. The **Add Parameter** dialog appears.

  5. To define the parameter, do the following:

     1. Click the **Type** field, and then select **Dynamic**.

     2. Click the **Source** field, and then select **Session Metadata**.

     3. Click the **Incoming Field** field, and then select **Verified Customer**.

     4. In the **Destination Field** , enter a field name that your CRM will recognize, and that Dialogflow CX will use as a parameter. A preview of the parameter appears in the **Preview** field.

     5. Click **Save** , and then click **Save** again.




## User profile flags

When reserved data properties are sent to CCAI Platform during a call or chat session, this information is displayed in the agent adapter in the form of user profile flags. There are user profile flags for unverified or verified customer, bad actor, and repeat customer. For information about how these flags are displayed in the agent adapter, see [User profile flags for chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-profile-flags-chat) and [User profile flags for calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-user-profile-flags).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
