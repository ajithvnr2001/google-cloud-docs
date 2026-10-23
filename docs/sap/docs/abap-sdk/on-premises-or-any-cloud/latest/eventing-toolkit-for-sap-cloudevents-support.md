---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-cloudevents-support/
title: CloudEvents support: Send and receive SAP events \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:10.380435+00:00
---

# CloudEvents support: Send and receive SAP events  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-cloudevents-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  CloudEvents support: Send and receive SAP events Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/eventing-toolkit-for-sap-cloudevents-support)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-cloudevents-support)



This document shows you how to send and receive SAP events as CloudEvents, for integration with third-party systems.

This feature is supported with the on-premises or any cloud edition of ABAP SDK for Google Cloud, independent of the Business Eventing Toolkit for SAP.

## Send events with structured encoding

To send an event with structured encoding, follow these steps:

  1. **Prepare your event data** : Before sending an event, you need to gather and structure the relevant data.

  2. **Create a client object** : Create a client object that facilitates communication with the target Google Cloud API.

  3. **Encode data as a CloudEvent** : Transform your prepared data into a CloudEvent payload. Populate the CloudEvent payload with required context attributes, optional attributes, and any relevant extension attributes.

  4. **Transmit the CloudEvent** : Once your data is encoded as a CloudEvent, you need to send the resulting CloudEvent payload to the API method.




The following code sample illustrates how to send data representing a material creation event from SAP to Google Cloud. For this sample CloudEvent with structured encoding, you specify a custom extension attribute called `MATNR` and set its value to `12345`. You provide the required CloudEvent `source` and `type` attributes. The `id` and `time` attributes are automatically generated for you.
    
    
    " 1. Prepare your event data: Populate the LS_MARA structure with your material data.
    
    " 2. Create a client object: Instantiate the API client you want to use
    DATA(lo_client) = NEW API_CLASS_NAME( iv_key_name = 'CLIENT_KEY' ).
    
    " 3. Encode data as a CloudEvent: Provide cloud event attributes: context, optional and Extension attributes
    lo_client->encode_as_cloud_event(
           EXPORTING iv_source = 'SAP'
                     iv_type   = 'sap.s4hana.material.created'
     iv_subject = 'Material created'
                     it_extension_attr = VALUE #( ( name = 'matnr' value = '12345' ) )
     iv_encoding = /goog/if_ce_spec_version=>c_ce_encoding-structured
             ir_data     = REF #( ls_mara )
           IMPORTING ev_data     = lv_data_payload ).
    
    * 4. Send the Payload: Use the lv_data_payload in your subsequent API method call.
    lo_client->API_METHOD ...
    

Replace the following:

  * `CLIENT_KEY`: The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).
  * `API_CLASS_NAME`: The class of the API you want to call with CloudEvents. For example, for sending your event payload to Pub/Sub API, the class name is `/GOOG/CL_PUBSUB_V1`. For information about the class name of supported APIs, see the [SDK reference documentation](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/overview).
  * `API_METHOD`: The API method that you need to call, for example, `PUBLISH_TOPICS`.



## Sending events with binary encoding

To send an event with binary encoding, follow these steps:

  1. **Prepare your event data** : With binary encoding, the event data itself is sent as the raw payload, without being wrapped in a JSON object within the CloudEvent.

  2. **Create a client object** : Create a client object that facilitates communication with the target Google Cloud API.

  3. **Populate CloudEvent header** : Populate your CloudEvent header with required context attributes, optional attributes, and any relevant extension attributes.

  4. **Transmit the CloudEvent** : Send the raw data payload along with the populated headers in an API method call.




The following code sample illustrates how to send data representing a material creation event from SAP to Google Cloud. For this sample CloudEvent with binary encoding, you specify a custom extension attribute called `MATNR` and set its value to `12345`. You provide the required CloudEvent `source` and `type` attributes. The `id` and `time` attributes are automatically generated for you. These CloudEvent attributes are added to the HTTP header of your API request.
    
    
    " 1. Prepare your event data: Populate the LS_MARA structure with your material data.
    
    " 2. Create a client object: Instantiate the API client you want to use (e.g., lo_client).
    DATA(lo_client) = NEW API_CLASS_NAME( iv_key_name = 'CLIENT_KEY' ).
    
    " 3. Populate the CloudEvent header: Provide cloud event attributes: context, optional and Extension attributes
    lo_client->encode_as_cloud_event(
    EXPORTING iv_source = 'SAP'
                      iv_type   = 'sap.s4hana.material.created'
      iv_subject = 'Material created'
                      it_extension_attr = VALUE #( ( name = 'matnr' value = '12345' ) )
      iv_encoding = /goog/if_ce_spec_version=>c_ce_encoding-binary ).
    
    * 4. Send the Payload: Call API method with payload as LS_MARA
    CALL METHOD lo_client->API_METHOD ...
    

Replace the following:

  * `CLIENT_KEY`: The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).
  * `API_CLASS_NAME`: The class of the API you want to call with CloudEvents. For example, for sending your event payload to Pub/Sub API, the class name is `/GOOG/CL_PUBSUB_V1`. For information about the class name of supported APIs, see the [SDK reference documentation](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/overview).
  * `API_METHOD`: The API method that you need to call, for example, `PUBLISH_TOPICS`.



## Receive events with structured encoding

To receive an event with structured encoding, follow these steps:

  1. **Define data structure** : Before receiving a CloudEvent, you need to define a data model structure to represent the data payload.
  2. **Receive and parse Input JSON** : Receive the incoming JSON message containing the CloudEvent and parse it into a structured representation.
  3. **Decode CloudEvent** : Once you have the parsed JSON, you need to decode the parsed JSON into CloudEvent attributes and the data payload.



The following parameters provide the data and attributes from the received CloudEvents with structured encoding:

  * **er_data** : Provides the data payload, for example, "first_Name":"John","last_Name":"Doe".
  * **et_extension_attr** : Anything in the payload which is not part of the CloudEvent specification, for example, "riskScore":"80","reason":"Fraud".
  * **es_context_attr** : The CloudEvent context attributes, for example, id":"1234567890","source":"SAP-TEST" "type":"ce.structured-ce","specversion".



The following code snippet illustrates how to decode the structured CloudEvent context and extension attributes from a JSON body:
    
    
    " 1. Define data structure: Create type for holding CloudEvent Data
    TYPES: BEGIN OF ty_cloud_event.
             " Declare cloud event attributes
     INCLUDE TYPE /goog/s_cloudevent_attr.
     " Declare Data
    TYPES:   data       TYPE ty_name,
     " Declare Additional Extension attributes
             risk_score TYPE string,
             reason     TYPE string,
           END OF ty_cloud_event.
    
    DATA: lv_json    TYPE string,
          ls_ce_data TYPE ty_cloud_event.
    
    " 2. Receive and parse Input JSON: Populate Input JSON to be decoded into CloudEvent attributes
    lv_json = '{"id":"1234567890","source":"SAP-TEST","type":"ce.structured-ce","specversion":"1.0","riskScore":"80","reason":"Fraud","data":{"first_Name":"John","last_Name":"Doe"}}'.
    
    " 3. Decode Structured CloudEvent into CloudEvent attributes:
    /goog/cl_ce_utility=>decode_structured_cloud_event(
         EXPORTING
           iv_json           = lv_json
         IMPORTING
           er_data           = ls_ce_data
           et_extension_attr = DATA(lt_ext_attr)
           es_context_attr   = DATA(ls_context_attr)
     ).
    

## Receiving events with binary encoding

With binary encoding, CloudEvent attributes are in headers, and the data is the raw payload.

To receive an event with binary encoding, follow these steps:

  1. **Receive headers and payload** : Receive the incoming message and extract the headers and the raw data payload.

  2. **Process the data payload** : Process the raw data payload according to its content-type.

  3. **Extract CloudEvent attributes from headers** : Parse the received headers and extract the CloudEvent attributes.




The following parameters provide the attributes from the received CloudEvents with binary encoding:

  * **et_extension_attr** : Anything in the payload which is not part of the CloudEvent specification, for example, "riskScore":"80","reason":"Fraud".
  * **es_context_attr** : The CloudEvent context attributes, for example, id":"1234567890","source":"SAP-TEST" "type":"ce.structured-ce","specversion".



The following code snippet illustrates how to extract the binary CloudEvent context and extension attributes from an HTTP request:
    
    
    " 1. Extract CloudEvent attributes from headers: Provide the HTTP request object as input.
    /goog/cl_ce_utility=>decode_binary_cloud_event(
              EXPORTING
                io_request        = server->request
              IMPORTING
                et_extension_attr = DATA(lt_extension_attr)
                es_context_attr   = DATA(ls_context_attr)
    
            ).
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
