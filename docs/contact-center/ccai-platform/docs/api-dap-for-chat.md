---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/api-dap-for-chat/
title: API direct access point for chat \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:22.856475+00:00
---

# API direct access point for chat  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/api-dap-for-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  API direct access point for chat Stay organized with collections  Save and categorize content based on your preferences. 

The API direct access point (DAP) for chat lets you automatically route incoming chat sessions to a queue based on a response from an external API endpoint that you configure. This eliminates the need for end-users to select from a queue menu. The endpoint can be your own or that of a third-party service.

With this capability enabled, when an end-user starts a chat, CCAI Platform sends a request to your API endpoint. The API returns routing data (key-value pairs), which CCAI Platform uses to match the end-user to the correct queue. If no match is found, the standard queue menu appears as a fallback.

The API DAP works for the following:

  * Web and mobile chats

  * New and resumed chats




## Before you begin

By default, this capability is inactive. Contact Google Cloud Support to turn it on for your instance.

## DAP types

There are two DAP types: API response and webhook response. Each DAP type has a different workflow.

### API response

Here's the API response workflow:

  1. An end-user starts a new or resumed chat.

  2. Before the queue menu appears, CCAI Platform sends a request to your API endpoint, including any parameters you have defined, such as session metadata or custom data.

  3. The API returns one or more key-value pairs.

  4. CCAI Platform matches these pairs with the key-value pairs configured on your chat queues. All pairs must match for the chat to be routed to a queue.

  5. If a match is found, the end-user is routed directly to that queue.

  6. The standard queue menu appears if either of the following occurs:

     * No match is found.

     * The API doesn't respond within the configured API request timeout.




### Webhook response

Here's the webhook response workflow:

  1. An end-user starts a new or resumed chat.

  2. Before the queue menu appears, CCAI Platform sends a request to your API endpoint, including a webhook URL.

  3. The API returns an acknowledgment response (HTTP 200) within the API request timeout.

  4. Your system processes the request and sends routing data (key-value pairs) to CCAI Platform using the webhook.

  5. CCAI Platform matches these pairs with the key-value pairs configured on your chat queues. All pairs must match for the chat to be routed to a queue.

  6. If a match is found, the end-user is routed directly to that queue.

  7. The standard queue menu appears if any of the following occurs:

     * No match is found.

     * The acknowledgment isn't received within the API request timeout.

     * The webhook response isn't received within the API callback timeout.




## Configure an API DAP for chat globally

To configure an API DAP for chat globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **API Request Direct Access Point** pane, and then click **Manage API Request Direct Access Point**.

  3. Click the **Chat** tab.

  4. Click the **API Request Direct Access Point for Chat** toggle to the on position.

  5. For **Direct Access Point Type** , select one of the following DAP types:

     * **API Response** : The API returns routing data in its response.

     * **Webhook Response** : The API acknowledges the request, then sends routing data to a webhook.

  6. To specify which chat types trigger the API DAP, for **Chat Types** , select one or both of the following:

     * **New chats**

     * **Resumed chats**

  7. In the **API Request** field, enter the API endpoint URL to use for the DAP.

  8. To configure authentication, do one of the following:

     * To configure basic authentication, do the following:

       1. For **Authentication Method** , select **Basic Authentication**.

       2. For **Authentication Credentials** , enter your username and password.

     * To configure a custom header, do the following:

       1. For **Authentication Method** , select **Custom Header**.

       2. Click **Add field**. The **Add Field** dialog appears.

       3. Enter a field key and field value, and then click **Save**.

  9. To configure the API request timeout, do the following:

     1. For **API Request Timeout** , set the number of seconds that CCAI Platform waits for the API to respond before timing out.

     2. Optional (appears only if you selected the **Webhook Response** DAP type): For **API Callback Timeout** , set the number of seconds that CCAI Platform waits for routing data from the webhook (after the initial acknowledgment) before timing out.

  10. To set the request method, for **API Request Method** , select **POST** or **GET**.

  11. To configure a data parameter, do the following:

     1. Click the **Pass Data Parameters** toggle to the on position.

     2. Click **Add Parameter**. The **Add Parameter** dialog appears.

     3. Do one of the following:

        * To configure a fixed data parameter, do the following:

          1. In the **Type** list, click **Fixed**.

          2. In the **Destination Field** field, enter the destination key.

          3. In the **Destination Value** field, enter the destination value. A preview of your data parameter appears in the **Preview** field.

        * To configure a dynamic data parameter, do the following:

          1. In the **Type** list, click **Dynamic**.

          2. Do one of the following:

             * To configure session metadata, do the following:

               1. In the **Source** list, select **Session Metadata**.

               2. In the **Incoming Field** list, select a metadata type.

             * To configure signed custom data, do the following:

               1. In the **Source** list, select **Signed Custom Data**.

               2. In the **Incoming Field** list, enter the incoming field.

             * To configure unsigned custom data, do the following:

               1. In the **Source** list, select **Unsigned Custom Data**.

               2. In the **Incoming Field** list, enter the incoming field.

          3. In the **Destination Field** field, enter the destination field. A preview of your data parameter appears in the **Preview** field.

     4. Click **Add Parameter**. Your data parameter appears in the **Data Parameters** list.

  12. Optional: To test your configuration, do the following:

     1. Go to the **Test Connection** section. Your data parameters appear in the list.

     2. Optional: To try different parameter values, edit the parameters values in the list.

     3. Click **Test this connection**.

**Note:** If you're testing a Webhook Response DAP type, the test validates the outbound request and acknowledgment only. It doesn't validate webhook data delivery.
  13. Click **Save Chat API**.




## Change the routing logic

Routing logic is the order in which CCAI Platform tries various matching types to match a chat to a queue. CCAI Platform evaluates each matching type in order and routes the chat to the first matching queue. If no match is found, the standard queue menu appears.

Here are the three matching types:

  * **API response** : Matches based on the API response key-value pairs.

  * **General access point label** : Matches based on the queue's general access point label.

  * **User segmentation** : Matches based on user segment data.




To change the routing logic, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **API Request Direct Access Point** pane, and then click **Manage API Request Direct Access Point**.

  3. Click the **Chat** tab.

  4. For **Routing Logic** , hold the pointer over a matching type and drag it to a new position.

  5. Repeat this step if needed.

  6. Click **Save Chat API**.


**Note:** User segmentation matching requires your instance to be connected to a CRM. Otherwise, user segmentation matching is skipped.

## Configure a DAP for chat at the queue level

To configure a DAP for chat at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**. The **Queue Menu Settings** page appears.

  2. Depending on the channel that you want, do one of the following:

     * In the **Mobile** pane, click **Edit / View**.

     * In the **Web** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, go to the **Access Point** section.

  5. Click **Create direct access point**. The **Create Direct Access Point** dialog appears.

  6. In the **Access Point Type** list, click **API Response**.

  7. In the **Access Point Name** field, enter an access point name.

  8. Click **Add Key & Value**. Enter a key-value pair to match with a key-value pair returned in the API response.

  9. Repeat the previous step to add more key-value pairs.

  10. Optional: In the **Greeting Message** field, enter the greeting message that you want to use when an end-user is directed to this menu option.

  11. Click **Create**. Your DAP appears in the **Access Point** list.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
