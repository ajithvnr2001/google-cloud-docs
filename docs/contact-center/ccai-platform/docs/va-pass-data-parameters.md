---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-pass-data-parameters/
title: Pass data parameters \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:48.131961+00:00
---

# Pass data parameters  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-pass-data-parameters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Pass data parameters Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to capture data parameters from inbound session initiation protocol (SIP) headers and pass them to virtual agents, virtual task assistants, and outbound SIP headers.

## Data parameters by channel

The following table is a high-level overview outlining data parameter availability by channel.

**Note:** While we strive to maintain the accuracy of this table, be aware that there might be some inconsistencies as we add new data parameter features on a regular basis. Refer to your CCAI Platform portal for the available parameters.Data parameter type | Customer Support Virtual Agent | Task Virtual Assistant  
---|---|---  
Web | Mobile | IVR | SMS | Web | Mobile | IVR | SMS  
**Fixed** |  | ✔ | ✔ | ✔ |  |  |  | ✔ |   
**Dynamic** | **CContact Center AI Platform (CCAI Platform) metadata** | ✔ | ✔ | ✔ |  |  |  | ✔ |   
**Signed parameters** | ✔ | ✔ |  |  |  |  |  |   
**Unsigned parameters** | ✔ | ✔ |  |  |  |  |  |   
**SIP headers** |  |  | ✔ |  |  |  | ✔ |   
**Form** |  |  |  |  |  |  | ✔ |   
  
## Capture data parameters from inbound SIP headers

You can capture data parameters from inbound SIP headers and pass them to the following:

  * [Outbound SIP headers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-pass-data-parameters#pass-data-parameters-to-outbound-sip-headers).

  * [Virtual agents and virtual task assistants](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-pass-data-parameters#data-parameters-to-vas-and-virtual-task-assistants).




You can also configure CCAI Platform to include inbound SIP header data in CRM records and session metadata files.

**Note:** Data parameters that contain metadata can only be passed to virtual agents. They can't be passed to outbound SIP headers.

To capture data parameters from inbound SIP headers, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Data Parameters** pane.

  3. Under **Voice** , select **Capture data parameters from inbound SIP headers in IVR sessions**.

  4. To use SIP header data for caller ID, do the following:

     1. Select **Use SIP header data for Caller ID**.

     2. In the **Field name** field, enter the SIP header field name.

  5. Select **Include SIP header data in session CRM records** to include SIP header data as a comment in the CRM record.

  6. Select **Include SIP header data in session metadata files** to include SIP header data in the session metadata file.

  7. Click **Save Data Parameters**.




### CRM record

The following code sample shows how the data parameters from an inbound SIP header would look in a CRM record:
    
    
    Call redirected to external SIP.
    SIP destination: <<SIP Destination URI>>
    Data parameters passed:
    {
       "<<destination_field_#1>>" : "<<destination_value_#1>>",
       "<<destination_field_#2>>" : "<<destination_value_#2>>"
     }
    

You can include SIP header data in records for the following CRMs:

  * [Salesforce](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-integration-guide)

  * [Zendesk](https://docs.cloud.google.com/contact-center/ccai-platform/docs/zendesk)

  * [Kustomer](https://docs.cloud.google.com/contact-center/ccai-platform/docs/kustomer)

  * [Custom CRM](https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm)




### Session metadata file

The following code sample shows how the data parameters from an inbound SIP header would look in a [session metadata file](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-session-metadata):
    
    
    "sip_headers": {
      "header 1": "value 1",
      "header 2": "value 2"
    }
    

## Pass data parameters to outbound SIP headers

_For pricing and implementation contact Support._

To send data to an external SIP destination, the Outbound SIP setup for Pass Data Parameters uses the automatic redirection capability. The data parameters defined in the inbound SIP header are gathered and transmitted to the external destination assigned to the selected IVR queue.

With Pass Data Parameters to an Outbound SIP you can:

  * Set up a static **or** dynamic data parameters at the IVR queue level. A fixed parameter helps you to pass a static value. A dynamic parameter lets you retrieve a value and pass it (dynamically).

  * Pass the set up parameters in the outbound SIP headers during automatic redirections.




### Admin config

  1. Go to **Settings > Queue > IVR** and then select the queue.

  2. Go to the **Automatic Redirection** section and make sure the toggle switch is set to **Show**.

  3. Click the **Configure SIP Transfer** link.

  4. On the **Outbound SIP Configuration panel** , enter the **Destination SIP URI** in `+ccNumber@fqdn` format. There is a 256 character limit for this value.

  5. Go to the **Pass Data Parameters** section and make sure the toggle switch is set to **On**. Pass Data Parameters cannot be enabled until the **Destination SIP URI** has been entered.




### Add a fixed parameter for a SIP header

  1. Click the **Add Parameter** button.

  2. Under the **Type** , select **Fixed**.

  3. Enter the following fields

**Destination Field** : the field name under which the data parameter value will be passed to Dialogflow CX.

**Destination Value** : the value being passed.

A sample of the parameter is shown in **Preview**.

  4. Click **Save**.




### Add a dynamic parameter from a SIP Header

  1. Click the **Add Parameter** button.

  2. Under **Type** , select **Dynamic**.

  3. Under **Source** , select **SIP Header**.

  4. Enter the following fields:

**Incoming Field** : the field name in the incoming SIP header the value of which will be passed to Dialogflow CX. This is a free text entry (string)

**Destination Field** : the field name under which the data parameter value will be passed to Dialogflow CX.

A sample of the parameter is shown in **Preview**.

  5. Click **Save**.




### Data records

Use the checkboxes in the **Data Records** section to indicate if you want the data parameters passed to be included in the session metadata files or CRM records.

Click **Save** and then click the **Back to Settings** link.

## Pass data parameters to Virtual Agents and Virtual Task Assistants

Data parameters gather data from incoming calls, hold it during the call, and then pass it back to Dialogflow CX services when the call is routed to a Virtual Agent or Virtual Task Assistant. The data parameters are returned in a set format in the Dialogflow APIs when you invoke the Dialogflow CX Agent.

You can add a data parameter in order to:

  * Collect either static **or** dynamic data settings at the IVR queue level. A fixed parameter helps you to pass a static value. A dynamic parameter lets you retrieve a value and pass it (dynamically).

  * Collect data through a dynamic **form** parameter: Only available for Virtual Task Assistant when the **form** parameters are configured. A data capture form is provided to the agent in the Agent Adapter when they deploy the Virtual Task Assistant. A form parameter defines the field(s) that the agent must fill out. For example, if the form field value is `booking_id`, a corresponding manual input field will appear in the adapter. In order for an agent to dispatch a Task Assistant to collect payment, the `booking_id` must be provided.




The following parameters can be added to an existing or a new Virtual Agent or Virtual Task Assistant:

  * Fixed parameters

  * CCAI Platform metadata parameters

  * SIP header parameters

  * Agent Form parameter (only available for Virtual Task Assistant)




### Add a fixed parameter

Fixed data parameters are fields that the system automatically passes to the VA and Task Assistant.

  1. Click the **Add Parameter** button.
  2. Under **Type** , select **Fixed**.
  3. Enter the following fields: 
     1. Destination Field: The field name under which the data parameter value will be passed to Dialogflow CX.
     2. Destination Value: The value being passed.
  4. A sample of the parameter will be shown in Preview.



### Add a dynamic parameter from CCAI Platform metadata

  1. Click the **Add Parameter** button.

  2. Under **Type** , select **Dynamic**.

  3. Under **Source** , select **CCAIP Metadata**.

  4. In the **Incoming Field** drop-down, select the type of CCAIP Metadata that will be passed to Dialogflow CX. The following CCAIP metadata data parameters can be passed:

     * **ANI (phone number)** : The number the end-user is calling from.

     * **Consumer ID** : The unique ID of the end-user in the platform.

     * **Call ID** : The unique ID of the call in the platform.

     * **Ticket ID (CRM)** : The CRM ticket ID linked to the session.

     * **Queue ID** : The queue ID from the session it's been escalated from.

     * **DNIS/TFN** : The DNIS (Dialed Number Identification Service) or TFN (Toll-Free Number) refers to the unique phone number that an end-user dials to reach your customer support system.

     * **Latest agent ID** : A system-generated ID assigned to each agent operating within the CCAI Platform platform. This ID uniquely identifies the agent responsible for handling the most recent segment of an ongoing call.

     * **Latest agent email** : The email address associated with the agent who handled the latest segment of an active call.

     * **Queue language** : The language short code that identifies the designated queue or department a call is being transferred to based on language requirements.

     * **Current sentiment score** : The average sentiment score for the latest segment of a call.

     * **Overall Sentiment Score** : A cumulative evaluation of the sentiment or satisfaction level throughout the entire call until the point of transfer.

  5. In the **Destination Field** , enter the field name under which the data parameter value will be passed to Dialogflow CX. A sample of the parameter will be shown in Preview.

  6. Click **Save**.




### Add a dynamic parameter from a SIP Header

  1. Click the **Add Parameter** button.

  2. Under **Type** , select **Dynamic**.

  3. Under **Source** , select **SIP Header**. Enter the following fields:

     1. Incoming Field: The field name in the incoming SIP header that will be passed to CCAI Platform. This is a free text entry (string).

     2. Destination Field: The field name under which the data parameter value will be passed to CCAI Platform.

  4. A sample of the parameter will be shown in preview.




### Add a dynamic custom form parameter

**Note:** This feature is only available for Virtual Task Assistant

When the Agent Form parameters are configured, a data capture form is provided to the agent in the Agent Adapter when they deploy the Virtual Task Assistant. A **form parameter** defines the field(s) that the agent must fill out. For example, if the form field value is `booking_id`, a corresponding manual input field will appear in the adapter. In order for an agent to dispatch a Task Assistant to collect payment, they must enter the `booking_id`.

  1. Click **+Add parameter**.

  2. In the **Type** drop-down, select **Dynamic**.

  3. In the **Source** drop-down, select **Form**.

  4. Enter the field name to display on the Agent Adapter.

  5. Select the **Required** checkbox to specify that the parameter has to be filled prior to transferring the session to a Virtual Task Assistant.

  6. Enter the destination parameter. Review the parameter in the preview window before submitting it, as all changes will be accepted without being validated.

  7. Click **Save**.




### Enable passing data parameters at the queue level

**Note:** If the selected queue does not have Virtual Agents assigned, click the **Add Virtual Agent** button to configure a new virtual agent before proceeding.

  1. In the CCAI Platform portal, go to **Settings > Queue > IVR** and then select the queue.

  2. Confirm that the queue has Virtual Agents assigned to it and then click the **Edit Virtual Agent Assignments** link. If the selected queue does not have Virtual Agents assigned, click the **Add Virtual Agent** button to configure a new Virtual Agent before proceeding.

  3. Go to the **Pass Data Parameters** section and make sure the toggle is set to **On**.




### Pass data parameters from the web SDK to a virtual agent

To pass data parameters from the web SDK to a virtual agent through a queue using unsigned custom data, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Web** pane, click **Edit / View**.

  3. Click the queue that you want to add parameters to.

  4. In the SDK, add custom data using the following example formatting:



    
    
    var ujet = new UJET({
    [...]
      customData: {
      "k1": {
        "label": "Version",
        "value": "1.2.3"
      },
      "k2": {
        "label": "Dashboard",
        "value": "<http://example.com>"
      }
      }
    
    })
    

You can then access it in VA using the following command:
    
    
    $session.params.valuek1
    

This command should result in an output of `1.2.3`.

A data parameter command needs to be added for each, so to use `k2` like in the previous example, another one will need to be created.

### Admin Config

  1. Go to **Settings > Queue > IVR** and then select the queue.

  2. Confirm the queue has Virtual Agents assigned to it and then click the **Edit Virtual Agent Assignments** link.

NOTE: If the selected queue does not have Virtual Agents assigned, click the **Add Virtual Agent** button to configure new Virtual Agent before proceeding.

  3. Go to the **Pass Data Parameters** section and check the toggle is set to On.




### Add a Fixed parameter

  1. Click the **Add Parameter** button.

  2. Under **Type** , select **Fixed**.

  3. Enter the following fields

**Destination Field** : the field name under which the data parameter value will be passed to Dialogflow CX.

**Destination Value** : the value being passed.

A sample of the parameter is shown in Preview.




### Add a Dynamic parameter from CCAI Platform Metadata

  1. Click the **Add Parameter** button.

  2. Under **Type** , select **Dynamic**.

  3. Under **Source** , select **CCAI Platform Metadata**.

  4. In the **Incoming Field** drop-down, select the type of CCAI Platform Metadata that needs to be passed to Dialogflow.

The following CCAI Platform metadata data parameters can be passed:

ANI (phone number)

Consumer ID

Call ID

Ticket ID (CRM)

Queue ID

  5. In **Destination Field** , enter the field name under which the data parameter value will be passed to Dialogflow CX.

A sample of the parameter is shown in Preview.

  6. Click **Save**.




### Add a Dynamic parameter from a SIP Header

  1. Click the **Add Parameter** button.

  2. Under **Type** , select **Dynamic**.

  3. Under **Source** , select **SIP Header**.

  4. Enter the following fields:

**Incoming Field** : the field name in the incoming SIP header the value of which will be passed to Dialogflow CX. This is a free text entry (string).

**Destination Field** : the field name under which the data parameter value will be passed to Dialogflow CX.

A sample of the parameter is shown in Preview.




### Data Records

Use the checkboxes in the **Data Records** section to indicate if you want the data parameters passed to be included in the session metadata files or CRM records.

Click **Save** and then click the **Back to Settings** link.

## Pass data parameters to virtual agents mid-session

This feature allows for mid-session data parameter transmission. It encourages dynamic interactions and supports better user experiences by enabling contextual data sharing with virtual agents mid-session. This update introduces a new API endpoint that allows customers to receive data parameters from the SDK during chat sessions and pass them to a virtual agent if a corresponding session is ongoing. This is useful for scenarios such as authentication mid-session.

Secured (signed) or unsecured (unsigned) data can be sent through the Apps API. However, all requests to the API are secured through an API key, helping to ensure that the data is protected during transmission.

The custom data moves through the following process:

  1. Custom data comes in through the SDK or Apps API endpoints.

  2. The custom data is stored or merged with the existing data for the chat.

  3. Custom data is attached to the detect_response call from the end-user's response along with their message.

  4. The custom data is passed to the virtual agent.

  5. All new custom data is posted to the CRM.




### API endpoint

An Apps API endpoint needs to be used in order to accept custom data for a call or chat mid-session.
    
    
    POST
    /apps/api/v1/[chats|calls]/:id/custom_data
    

It receives a payload of 2 possible types: secured (signed) or unsecured (unsigned).

Secured Data (Signed Using JWT):
    
    
    {
    "signed": true,
    "signed_data": "JWT_SIGNED_DATA"
    }
    {
      "custom_data": {
        "reserved_verified_customer": {
          "value": true
        },
        "reserved_bad_actor": {
          "value": false
        },
        "reserved_repeat_customer": {
          "value": true
        },
        "field1": {
          "value": "dummy1"
        },
        "field2": {
          "value": "dummy2"
        }
      },
      "exp": 1734567890,
      "iat": 1734560000
    }
    

Unsecured data:
    
    
    {
      "signed": false,
      "data": {
        "reserved_verified_customer": {
          "value": true
        },
        "reserved_bad_actor": {
          "value": false
        },
        "reserved_repeat_customer": {
          "value": true
        },
        "field1": {
          "value": "dummy1"
        },
        "field2": {
          "value": "dummy2"
        }
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
