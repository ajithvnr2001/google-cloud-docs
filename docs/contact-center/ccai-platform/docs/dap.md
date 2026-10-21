---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dap/
title: Direct access points \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:08.166598+00:00
---

# Direct access points  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Direct access points Stay organized with collections  Save and categorize content based on your preferences. 

Direct access points (DAPs) let you direct voice calls to specific queues in your queue structure. Using DAPs makes the call process faster for end-users by routing them directly to specific queues rather than forcing them to navigate a lengthy queue tree. For example, you can configure a DAP to route new end-users to a dedicated onboarding queue.

There are multiple ways to set up DAPs, either using an API or your CRM (or both). This section outlines the configuration options for DAPs.

**Note:** DAPs are available for Web, Mobile, and IVR channels.

## DAP types

You can configure the system to create a DAP with one of the following **access point types** , depending on which channel you're using. The multiple types use different information to detect a match and route an end-user call.

DAP type | IVR | Mobile | Web  
---|---|---|---  
**User Segment DAP** : Matches and routes end-users according to **end-user account data** key and value pairs from your CRM. | ✔ | ✔ | ✔  
**General DAP** : An **access point** that is placed in your app or SDK setup by your developers. When this access point is reached by an end-user, they are routed to a specific queue. | ✔ | ✔ | ✔  
**Support Phone Number DAP** : Routes end-users to specific queues according to the **support phone number** they call to reach your call center. | ✔ |  |   
**API Response DAP** : Matches and routes end-users to specific queues according **API response** key and value pairs. | ✔ |  |   
**Mobile App DAP** : Routes end-users to specific queues according to **mobile application**. Only available for environments with the [Multiple mobile app](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Developer_Resources#UUID-f8702524-4b0a-dc36-83f8-d48e8892a2da) feature enabled. |  | ✔ |   
  
## DAP matching order and interactions

When you use multiple DAP types, Contact Center AI Platform (CCAI Platform) checks for matches, first based on DAP type, then the order in which the DAPs were created. DAP order is different if you're using one or more mobile apps with your environment. If two DAP criteria are met within a specific DAP type, CCAI Platform routes the call based on the first one created.

### Standard IVR channel DAP types and order

  1. **[Mobile PSTN fallback (if using a mobile SDK)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Developer_Resources#UUID-f8702524-4b0a-dc36-83f8-d48e8892a2da)**

     * Match: Route to that queue.
     * No match: Move to next.
  2. **Phone number DAP**

     * Match: Route to that queue.
     * No match: Move to next.
  3. **General DAP**

     * Match: Route to that queue.
     * No match: Move to next.
  4. **API DAP**

     * Match: Route to that queue.
     * No match: Move to next.
  5. **User segment SAP**

     * Match: Route to that queue.
     * No Match: Route to the very top of the queue.



#### Alternate IVR DAP order

For access, contact support.

  1. **General DAP**

     * Match: Route to that queue.
     * No match: Move to next.
  2. **API DAP**

     * Match: Route to that queue.
     * No match: Move to next.
  3. **[Mobile PSTN fallback (if using a mobile SDK)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Developer_Resources#UUID-f8702524-4b0a-dc36-83f8-d48e8892a2da)**

     * Match: Route to that queue.
     * No match: Move to next.
  4. **Phone number DAP**

     * Match: Route to that queue.
     * No match: Move to next.
  5. **User segment DAP**

     * Match: Route to that queue.
     * No Match: Route to the very top of the queue.



### Mobile channel DAP types and order

  1. **General DAP**

     * Match: Route to that queue.
     * No match: Move to next.
  2. **User segment DAP**

     * Match: Route to that queue.
     * No match: Move to next.
  3. **Mobile App DAP**

     * Match: Route to that queue.
     * No Match: Route to the very top of the queue.



#### Alternate DAP order

For access, contact support.

  1. **User segment DAP**

     * Match: Route to that queue.
     * No match: Move to next.
  2. **General DAP**

     * Match: Route to that queue.
     * No match: Move to next.
  3. **Mobile App DAP**

     * Match: Route to that queue.
     * No Match: Route to the very top of the queue.



### Web channel DAP types and order

  1. **General DAP**

     * Match: Route to that queue.
     * No match: Move to next.
  2. **User segment DAP**

     * Match: Route to that queue.
     * No match: Move to next.



#### Alternate DAP order

For access, contact support.

  1. **User segment DAP**

     * Match: Route to that queue.
     * No match: Move to next.
  2. **General DAP**

     * Match: Route to that queue.
     * No match: Move to next.



## User segment DAPs

All CRM software has contact objects (named Contact, People, Customer, or similar). CCAI Platform automatically looks at contact objects whenever an end-user reaches out using IVR or SDK and compares them to the key and value pairs that you used to configure the DAP. 

If the system detects a match, the end-user is immediately routed to the specified queue. You can configure your CRM to include fields that you want to use for end-user routing, such as including a VIP field.

### Example user segment DAP

So an end-user can be automatically routed to an escalation queue, you want to know if they have multiple open support cases. 

  1. In your CRM, create a calculated field that counts open support cases. 

  2. Create a DAP to look for a specific value in that calculated field that indicates multiple support cases are open. 




If the DAP detects a match, the end-user is routed directly to a specified escalation queue, and the case details are passed to the agent.

### Example user segment DAP prerequisites

  1. You must set up user segments in your CRM. For more information, see [Priority User Segments](https://docs.cloud.google.com/contact-center/ccai-platform/docs/perations_Management#priority_user_segments) for instructions.

  2. Enable CRM access

     1. In the CCAI Platform portal, go to **Settings** > **Operation Management**.

     2. Under **CRM Access** , mark the checkbox to **Allow CRM Access for user segment information**.

     3. Click **Save General** to save.

  3. See the [create a DAP](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#create_a_dap) section to set up a user segment DAP.




## Support phone number DAPs

Support phone number DAPs route end-users into dedicated queues according to the phone number they're calling. Phone numbers can be any number managed by CCAI Platform. There is no limit to the number of phone numbers you can use, and phone number DAPs can be set up for multiple languages and locales.

### Example support phone number DAPs

  * An end-user suspects credit card fraud and calls the number listed on the back of the card. That phone number is associated with a DAP that is configured to route the caller into a dedicated fraud prevention queue.

  * You can give out different phone numbers to specific groups of people, such as VIPs or employees. When an end-user calls in, the DAP recognizes the phone number and automatically routes them to the VIP queue or employee menu.




### Supported formats

  * E164 formatted numbers: +(country_code)(phone_number)
  * SIP phone numbers in the incoming sip address format: `sip:[number]@[domain]`



### Example support phone number DAP prerequisites

  1. Make sure that the phone number you want to use is provisioned for your CCAI Platform environment.

  2. See the [create up a DAP](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#create_a_dap) section to set up a support phone number DAP.




## API DAPs

You can configure API DAPs to capture conditions that exist inside or outside of your CRM. This is the only DAP where multiple conditions can be evaluated in order to route sessions (for example, both a phone number and a key-value pair). When an end-user calls in, the contact data is compared to the API data and routed to a specific point in the queue structure.

The request is processed using JSON. `POST` and `GET` HTTP request methods are supported. Unlike other DAP options, you can also use `AND` logic with multiple key and value pairs. When a key-value pair match is detected, CCAI Platform immediately routes the call according to your configuration.

### Example use of DAP API

You have an API with data that shows the end-user is a `Super-user`, the product type is `International`, and that they meet other specific criteria. A DAP configured to recognize specific key-value pairs routes them to a specific queue.

#### Example DAP API prerequisites

The required elements:

  * _API URL_ : A URL endpoint that is able to receive a phone number request and return a JSON response.

  * _Test phone number_ : After the DAP is set up, you must use a test phone number to ensure that the configuration correctly returns results (typically in JSON format).

  * _API credentials_ : Basic authentication is required for a non-Salesforce endpoint.

OR

  * _Salesforce Configuration_ : See the [Salesforce documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Salesforce#api-dap-salesforce) for initial setup in Salesforce.




#### Configure an API DAP

To configure an API DAP, do the following:

  1. Click menu **Menu** , and then click **Settings > Developer settings**.

  2. Go to the **API request direct access point** pane.

  3. In the **Post request URL** field, enter the API endpoint for the DAP. Only one endpoint can be used per environment.

  4. In the **Authentication method** area, select one of the following authentication methods:

     * **Basic authentication**. If you select this option, enter your username and password.

     * **OAuth**. OAuth is only available when using Salesforce. For more information, see [API Direct Access Point - Salesforce REST API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Salesforce#api-dap-salesforce).

     * **Custom header** : Uses HTTP headers for authentication. If you select this option, do the following:

       1. Click **Add field**. The **Add field** dialog displays.

       2. In the **Field key** field, enter the authentication header name.

       3. In the **Field value** field, enter the authentication header value.

       4. Optional: Add additional headers.

       5. Click **Save**.

  5. In the **API request timeout** area, click  expand_more **Expand more** to select the API request timeout value in seconds. To determine the optimal timeout time, consider the following:

     * The optimal API request timeout time depends in part on your server response time. A tool such as Postman can help you determine your server response time.

     * An API request timeout time should be long enough to accommodate the expected API response time, but short enough to keep the end-user's wait time reasonably short.

     * If the API request times out and there is no match for the first DAP type, the next DAP type is checked for a match. If there is no match for any DAP type, the call is sent to the top of the queue. For more information, see DAP matching order and interactions.

     * If you have multiple languages enabled, a language-selection message is played for the caller.

  6. In the **API request method** area, depending on the type of request you're making, select **Post** or **Get**.

  7. In the **Phone number format** area, click  expand_more **Expand more** to select the phone number format that you use to store phone numbers on your server.

  8. In the **Request parameter** field, enter the name of the phone number request parameter. The value can be any string and is case sensitive. If the request parameter doesn't match the corresponding parameter on your server, routing fails. Here is an example API request URL for a GET method:
         
         https://example.com/api_dap?PARAMETER_NAME=+18005550100
         

Replace `PARAMETER_NAME` with the name of the phone number parameter.

  9. Optional: To pass data from the headers of incoming Session Initiation Protocol (SIP) calls to your Interactive Voice Response (IVR) queues, do the following:

     1. Click the **Pass data parameters** toggle to the on position.

     2. In the **Data parameters** area, add the parameters that are required to pass the data. For more information, see [Pass data parameters to Virtual Agents and Virtual Task Assistants](https://docs.cloud.google.com/contact-center/ccai-platform/docs/pass-data-parameters#data-parameters-to-vas-and-virtual-task-assistants).

     3. In the **Data records** area, make a checkbox selection to include data parameters in metadata files, data parameters in CRM records, or both.

  10. In the **Push API response data to CRM** area, make a checkbox selection to format the API response data as a key-value pair, leave the API response in its original JSON format, or both.

  11. Click **Save**.




### Test your configuration

CCAI Platform lets you quickly verify that your connection has been properly configured. You need a phone number that's linked to a contact that you know will return the value you're looking for from the queried server.

  1. Go to **Setting > Developer Settings > API Request Direct Access Point**.

  2. Enter the test phone number in the **Test Connection** field and click **Test this connection.**

  3. View the JSON response from the API.

  4. If null or no results, check the following:

     * Is the connection pointed to a database with the correct data?

     * Is the phone number associated with a contact?

     * Is the phone number format correct?

     * Does the response header match exactly?

     * If the response is timing out, increase the timeout value in the settings above the test section. If the timeout becomes so long that it will lengthen wait times, investigate how to optimize your server response time.




### API DAP logic details

CCAI Platform uses set logic to route calls (see DAP matching order and interactions). API DAPs also can include **multiple conditions** to be evaluated in order to route calls. Because of this, the specific order in which you create API DAPs is extremely important. If you have existing API DAPs and they have any overlap with new API DAPs you are creating, you might need to recreate your existing DAPs in a new order to achieve your required routing.

Each condition can be either a compound set of key and value pairs or a single key and value pair. After a condition is met, CCAI Platform stops checking for matches and immediately routes the call. For this reason, it's important to create the most complex conditions before the least complex. This ensures that the more complex conditions are checked first.

**Correct example: Complex conditions first**

CCAI Platform will match 1 first, then 2, then 3.

  1. "brand = Generico" AND "Customer type = lead" AND "product = retail"

  2. "brand = Generico" AND "Customer type = lead"

  3. "brand = Generico"




**Incorrect example: Simple conditions first**

CCAI Platform will match 1 first, then 2, then 3. If API DAPs are created in this order, conditions 2 and 3 will never be reached because all requests will meet the first condition.

  1. "brand = Generico"

  2. "brand = Generico" AND "Customer type = lead"

  3. "brand = Generico" AND "Customer type = lead" AND "product = retail"




### DAP API endpoint example deployment

You can download an example implementation from GitHub, including configuration and deployment instructions. This shows you how to deploy a DAP API endpoint and configure your implementation to your own requirements.

The GitHub repository is here: <https://github.com/GoogleCloudPlatform/ccaas-dap-api>.

## Create a DAP

  1. Make sure that you have completed any prerequisites required for your DAP type. See the [API DAP](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#api_daps), [support phone number DAP](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#support_phone_number_daps), or [user segment DAP](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#user_segment_daps) sections for instructions.

  2. Go to **Settings > Queue**.

  3. Choose your channel (IVR, Web, or Mobile) and click **Edit / Add**.

  4. Select the queue you want to add the direct access point to. In the **Settings** panel, scroll to **Access Point** and click **\+ Create direct access point**.

  5. Choose the access point type and enter a name in **Access Point Name**. Depending on your channel and access type, enter the following information:

     1. **Support phone number**

        * _Support Phone Number_ : Enter a phone number that has been provisioned to your account by CCAI Platform, including the country code if international. Format is e164 (`+[country_code][phone_number]`) or SIP (`sip:[number]@[domain]`).
        * _Greeting Message_ : Enter a message for end-users in the field to be read by Text-to-Speech, or upload your own audio file. To skip the greeting message, either enter `.` in the field or upload a blank file.
     2. **User segment**

        * _CRM Custom User Segment Field_ : Name of user segment field in your CRM. Example: "Tier"
        * _CRM Custom User Segment Value_ : User segment value to be directed to this queue. Example. "Gold Tier"
        * _Greeting Message_ : Enter a message for end-users in the field to be read by Text-to-Speech, or upload your own audio file. To skip the greeting message, either enter `.` in the field or upload a blank file.
     3. **API Response**

        * _API Response_ : Click **Add Key & Value**. Enter the key and value pairs as they gave been set up in the API. Repeat for each set of key and value pairs required for the DAP.
        * (Optional) _Support Phone Number_ : A CCAI Platform- provisioned phone number that end-users call to reach your call center. This number will be required for matching in addition to the API response key and value pairs.
        * _Greeting Message_ : Enter a message for end-users in the field to be read by Text-to-Speech, or upload your own audio file. To skip the greeting message, either enter `.` in the field or upload a blank file.
     4. **General**

        * _General Access Point Label_ : A recognizable label for developers to use within your app or SDK.
     5. **Mobile App**

        * _Mobile App_ : Choose your mobile app from the drop-down menu.
  6. Click **Create**.




## Test call routing

  1. Call the channel using a phone number or end-user account with parameters that you know should trigger the DAP.

  2. Confirm the call is routed to the correct queue and any entered greeting is played.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
