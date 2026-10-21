---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-configure-widgets/
title: Configure custom panels \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:30.582939+00:00
---

# Configure custom panels  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-configure-widgets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure custom panels Stay organized with collections  Save and categorize content based on your preferences. 

A custom panel displays one or more URLs for external resources. These can be documentation, tools, or other resources. You can configure a panel for a custom URL or a custom links panel containing multiple links. The configuration options for these panel types vary slightly. For example, you can specify link text in the custom links panel.

**Important:** Custom URLs must support iframes. Otherwise, nothing displays in the panel. Google recommends testing your URL to ensure that it displays in an iframe.

## Configure a panel for a custom URL

You can configure a custom panel containing a URL to an external resource. You can optionally include a navigation bar in the panel. You can also add HTTP headers—for example, for authentication.

To configure a panel for a custom URL, follow these steps:

  1. In the CCAI Platform portal, click **Settings** > **Operations Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Desktop** pane.

  3. For **Custom panel management** , click **Manage custom panels list**. The **Custom Panel** pane appears.

  4. Click **Add custom panel** > **Custom URL**. The **Add Custom URL** pane appears.

  5. To add a name for the custom panel, do the following:

     1. Click the **Select language** field, and then click a language for the custom panel name.

     2. In the **Enter custom panel name** field, enter a name for your panel.

  6. Optional: To add a panel name in a different language, click **Add custom panel name** , and then repeat these steps with a different language.

  7. If you added the panel name in multiple languages, select the default language.

  8. In the **Display URL** field, enter the URL for an external resource. You can use variables, functions, and parameters in the URL.

  9. Optional: To dynamically control the custom-panel language based on the agent's assigned location or language selection, see Dynamically control the custom-panel language.

  10. Select the **Display a navigation bar in custom panel** checkbox if you want a navigation bar to display with this panel.

  11. To add an HTTP header, do the following:

     1. For **HTTP Headers** , click **Add field**.

     2. Enter a key and a value for the HTTP header. You can use variables, functions, and parameters in the value.

  12. To add another HTTP header, click **Add field** , and then enter another key-value pair.

  13. Click **Add Custom URL Panel**. Your custom panel appears in the **Custom Panel** list.




## Configure a custom links panel

You can configure a custom panel that contains a list of links to external resources. This panel can provide agents quick access to resources they need while handling call and chat sessions.

To configure a custom links panel, follow these steps:

  1. In the CCAI Platform portal, click **Settings** > **Operations Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Desktop** pane.

  3. For **Custom panel management** , click **Manage custom panels list**. The **Custom Panel** pane appears.

  4. Click **Add custom panel** > **Custom Links**. The **Add Custom Links Panel** pane appears.

  5. To add a name for the custom panel, do the following:

     1. Click the **Select language** field, and then click a language for the custom panel name.

     2. In the **Enter custom panel name** field, enter a name for your panel.

  6. Optional: To add a panel name in a different language, click **Add custom panel name** , and then fill out the new row using a different language.

  7. If you added the panel name in multiple languages, select the default language.

  8. To add a link, do the following:

     1. Click **Add link**. The **Add Link** pane appears.

     2. In the **URL** field, enter the URL for an external resource. You can use variables, functions, and parameters in the URL.

     3. Optional: To dynamically control the custom-panel language based on the agent's assigned location or language selection, see Dynamically control the custom-panel language.

  9. To add link text for the URL, do the following:

     1. Click the **Select language** field, and then click a language for the link text.

     2. In the **Link text** field, enter the link text for your link.

  10. Optional: To add link text in a different language, click **Add link text** , and then fill out the new row using a different language.

  11. If you added link text in multiple languages, select the default language.

  12. For **Display link in** , specify whether the link opens in a new tab or in the panel.

  13. To add an HTTP header, do the following:

     1. For **HTTP Headers** , click **Add field**.

     2. Enter a key and a value for the HTTP header. You can use variables, functions, and parameters in the value.

  14. To add another HTTP header, click **Add field** , and then enter another key-value pair.

  15. Click **Add**.

  16. To add another link, click **Add link** , and then repeat the steps for adding a link.

  17. Click **Add Custom URL Panel**. Your custom panel appears in the **Custom Panel** list.




## Dynamically control the custom-panel language

You can use the `{AGENT_LOCATION_LANGUAGE}` or the `{AGENT_LANGUAGE}` variable in your custom URL to dynamically control the language for a custom panel:

  * **Agent location language** : Add the `{AGENT_LOCATION_LANGUAGE}` variable to your URL to display the custom panel in the language of the agent's assigned location. Example: `https://YOUR_CCAAS_HOST/lang={AGENT_LOCATION_LANGUAGE}`. For more information, see Variables.

  * **Agent language** : Add the `{AGENT_LANGUAGE}` variable to your URL to display the custom panel in the language selected by the agent in the agent desktop language selector. If an agent changes the language in the language selector, custom panels reload and display the newly selected language. Example: `https://YOUR_CCAAS_HOST/lang={AGENT_LANGUAGE}`. For more information, see Variables.




## Variables

You can include the following variables in URLs and HTTP header field values for custom panels and custom links panels. These variables capture agent, end-user, and session information.

**Agent variables**

  * `{AGENT_ID}`: the agent ID

  * `{AGENT_CUSTOM_ID}`: the agent's custom ID

  * `{AGENT_EMAIL}`: the agent's email

  * `{AGENT_ALIAS}`: the agent's alias

  * `{AGENT_LOCATION_LANGUAGE}`: the language code for the language of the agent's assigned location—for example, `en-US`. To use this variable, the agent needs an assigned location with an assigned language. For more information, see [Configure location and language](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-location#configure-location-and-language).

  * `{AGENT_LANGUAGE}`: the language code for the display language that the agent selects in the agent desktop language selector—for example, `en-US`. If an agent changes the language in the language selector, custom panels reload and display the newly selected language. For more information, see [Change the display language](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-use-agent-desktop#change-display-language).




**End-user variables**

  * `{UJET_ID}`: the end-user ID

  * `{ANI}`: the end-user's phone number

  * `{DEVICE_TYPE}`: the device type of the end-user




**Session variables**

  * `{SESSION_TYPE}`: the session type

  * `{PHONE_NUMBER}`: the end-user's phone number

  * `{SESSION_ID}`: the call ID or chat ID

  * `{MENU_PATH}`: the URL path to the menu

  * `{QUEUE_NAME}`: the name of the queue

  * `{QUEUE_ID}`: the internal queue ID

  * `{LANGUAGE}`: the queue language

  * `{OUTBOUND_PHONE_NUMBER}`: the outbound phone number

  * `{SUPPORT_PHONE_NUMBER}`: the support phone number the end-user is calling




## Functions

You can include functions from the following table in URLs and HTTP header field values for custom panels and custom links panels.

Function | Syntax | Description  
---|---|---  
Default value | `=DEFAULT_VALUE(value_1, value_2)` | Uses `value_1` unless null or empty, then uses `value_2`.  
Concatenation OR | `=CONCAT_OR(value_1, value_2, value_3)` | Concatenation of multiple values with OR. Example: `value_1` OR `value_2` OR `value_3`.  
Concatenation AND | `=CONCAT_AND(value_1, value_2, value_3)` | Concatenation of multiple values with AND. Example: `value_1` AND `value_2` AND `value_3`.   
JSON | `=JSON({"key_1":"value_1", "key_2":"[value_2]"})` | JSON to string. Example: `{"key_1":"value_1","key_2":"value_2"}`.  
JSON array | `=JSON_ARRAY({"key_1":"value_1"},{"key_2":"value_2"})` | JSON array to string. Example: `[{"key_1":"value_1"},{"key_2":"value_2"}]`.  
  
## Parameters

You can include parameters in URLs and HTTP header field values for custom panels and custom links panels.

**Note:** Deleting a parameter can cause problems in a URL or HTTP header that references it. Confirm that a parameter isn't being referenced before deleting it.

You can configure fixed or dynamic parameters:

  * **Fixed parameters** have a constant value that you specify.

  * **Dynamic parameters** have a value that's determined by session metadata or a SIP header.




To configure a fixed or dynamic parameter, follow these steps:

  1. In the CCAI Platform portal, click **Settings** > **Operations Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Agent Desktop** pane.

  3. For **Custom panel management** , click **Manage custom panels list**. The **Custom Panel** pane appears.

  4. Click **Parameter management**. The **Parameter Management** page appears.

  5. Click **Add parameter**. The **Add Parameter** dialog appears.

  6. Do one of the following:

     * To configure a fixed parameter, do the following:

       1. In the **Type** list, select **Fixed**.

       2. In the **Destination Field** field, enter the destination key.

       3. In the **Destination Value** field, enter the destination value. A preview of your parameter appears in the **Preview** field.

     * To configure a dynamic parameter, do the following:

       1. In the **Type** list, select **Dynamic**.

       2. Do one of the following:

          * To configure session metadata, do the following:

            1. In the **Source** list, select **Session Metadata**.

            2. In the **Incoming Field** list, select one of the following metadata types:

               * **ANI (phone number)** : The number that the end-user is calling from.

               * **Consumer ID** : The ID of the end-user.

               * **Call ID/Chat ID** : The ID of the call or chat.

               * **Ticket ID (CRM)** : The CRM ticket ID linked to the session.

               * **Queue ID** : The ID of the queue where the session is escalated from.

               * **DNIS/TFN** : The Dialed Number Identification Service or Toll-Free Number that the end-user dialed.

               * **Latest Agent ID** : The system-generated ID of the agent who handled the most recent segment of an active call.

               * **Latest Agent Email** : The email address of the agent who handled the most recent segment of an active call.

               * **Queue Language** : The language code for the designated queue or department.

               * **Verified Customer** : A [reserved data property](https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-reserved-data-properties) that indicates that your system considers this a legitimate customer.

               * **Bad Actor** : A [reserved data property](https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-reserved-data-properties) that indicates that your system considers this a potentially bad actor.

               * **Repeat Customer** : A [reserved data property](https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-reserved-data-properties) that indicates that your system has determined that this end-user has contacted your contact center before.

          * To configure a SIP header, do the following:

            1. In the **Source** list, select **SIP Header**.

            2. In the **Incoming Field** list, enter the SIP header.

       3. In the **Destination Field** field, enter the destination field. A preview of your parameter appears in the **Preview** field.

  7. Click **Add Parameter**. Your parameter appears in the **Data Parameters** list.


**Note:** Some parameter values overlap with variable values—for example, the `{QUEUE_ID}` variable and the `Queue ID` session metadata parameter. Use one or the other, not both.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
