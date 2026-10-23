---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-configuration/
title: Install and configure the Business Eventing Toolkit for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:09.975196+00:00
---

# Install and configure the Business Eventing Toolkit for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Install and configure the Business Eventing Toolkit for SAP Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/eventing-toolkit-for-sap-configuration)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-configuration)



This document describes how to install and configure the Business Eventing Toolkit for SAP.

## Install the Business Eventing Toolkit for SAP

When you install the latest version of the on-premises or any cloud edition of ABAP SDK for Google Cloud, the Business Eventing Toolkit for SAP is installed for you. For information about the installation steps, see [Install and configure the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).

If you're using version 1.9 or earlier of the on-premises or any cloud edition of ABAP SDK for Google Cloud, then update your SDK to the latest version to get the Business Eventing Toolkit for SAP. For more information, see [Update ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#abap-sdk-update).

## Enable the target Google Cloud APIs

Before using target Google Cloud services, ensure the corresponding Google Cloud APIs are enabled in your project. For example, if you plan to publish events to Pub/Sub, enable the Pub/Sub API.

For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api).

## Set up authentication

Once you set up authentication to access Google Cloud APIs in your on-premises or any cloud edition of ABAP SDK for Google Cloud, the Business Eventing Toolkit for SAP uses the same authentication method to publish SAP events to Google Cloud APIs. For information about how to set up authentication in the on-premises or any cloud edition of ABAP SDK for Google Cloud, see [Authentication overview](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

Make sure the service account configured in ABAP SDK for Google Cloud client key configuration has the required IAM roles specific to the target Google Cloud service.

Make a note of the client key that you've created as part of the authentication setup. You use this client key when configuring the Business Eventing Toolkit for SAP in your SAP system.

## Configure CloudEvent attributes

You can maintain default values for CloudEvent attributes. These values are stored in the table `/GOOG/CE_DEFAULT`.

This is an optional configuration. You can either pass CloudEvent attributes or override the default attributes directly in your code.

To configure CloudEvent attributes, do the following:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Business Eventing: Configure Context Attributes for Cloud events**.

  3. Click **New Entries**.

  4. Enter values for the following fields:

Field | Data type | Description  
---|---|---  
**Cloud Event Default Attribute Key** | `String` | Specify a name for the default CloudEvent attribute configuration. For Example: CLOUD_EVENT_ATTRIBUTE_KEY.  
**Source** | `String` | Provide the URI-reference that identifies the context in which an event occurred.  
**ID** | `String` | Unique identifier for the event. Producers must ensure that Source + ID is unique for each distinct event.  
**Specification version** | `String` | The version of the CloudEvents specification which the event uses. If you leave this blank, the system uses 1.0.  
**Type** | `String` | Describes the type of event that occurred. Often used for routing, observability, and policy enforcement.  
**Data content type** | `String` | Content-type of the data value. Enables data to carry any type of content.  
**Data schema** | `String` | URI that identifies the schema that the data adheres to.  
**Subject** | `String` | Describes the subject of the event in the context of the event producer.  
  
For information about these fields, see the CloudEvents [context attributes](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md#required-attributes).

  5. Save the new entry.




## Configure target Google Cloud services

You can use this setting to maintain the target Google Cloud services for your events.

This setting is used when publishing events from SAP to Google Cloud services using the Business Eventing Toolkit for SAP.

To configure target Google Cloud services, do the following:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Business Eventing: Configure Google Cloud Targets for an Event**.

  3. Click **New Entries**.

  4. Enter values for the following fields:

Field | Data type | Description  
---|---|---  
**Event Key** | `String` | Specify a name of the publisher event configuration. For Example, EVENT_KEY.  
**Event Processor Class** | `String` | Specify the processor class for the event. Select one of the following options depending on your target Google Cloud service:
     * `/GOOG/CL_PUBLISHER_PUBSUB`: For publishing events to Pub/Sub. 
     * `/GOOG/CL_PUBLISHER_CLOUDFUNC`: For publishing events to Cloud Run functions. 
     * `/GOOG/CL_PUBLISHER_FCM`: For publishing events to Firebase Cloud Messaging (FCM). 
     * `/GOOG/CL_PUBLISHER_CONNECTORS`: For publishing events to the Integration Connectors API.   
**Google Cloud Key Name** | `String` | The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).  
**Event Parameter 1** | `String` | Specify any additional attribute that is required for the target Google Cloud service that you want to use.  
**Event Parameter 2** | `String` | Specify any additional attribute that is required for the target Google Cloud service that you want to use.  
**Event Parameter 3** | `String` | Specify any additional attribute that is required for the target Google Cloud service that you want to use.  
**Cloud Event Default Attribute Key** | `String` | To send the event as a CloudEvent, provide the value of the corresponding default attribute key that you've configured in the Configure CloudEvent attributes section.  
**Cloud Event: Encoding** | `String` | Select an appropriate mode for encoding your CloudEvents:
     * **Structured** : CloudEvent attributes are passed in the request body.
     * **Binary** : CloudEvent attributes are passed into the request header.
For scenarios when you need to send raw event data directly to Google Cloud services, bypassing the CloudEvents specification, you leave this field blank.  
  5. Save the new entry.




### Extend the publisher module

To integrate with other Google Cloud services or custom targets beyond the prebuilt targets, you can extend the Publisher module by creating your own implementations.

To create a custom implementation, do the following:

  1. In SAP transaction `SE24`, create a new class that inherits from `/GOOG/CL_PUBLISHER_BASE`.
  2. Implement the `PUBLISH_EVENT` and `VALIDATE_PARAMS` methods.

     * `PUBLISH_EVENT`: Contains your custom logic for sending event data to the target. Map the input parameters, transmit the data, and populate the output structure with the target's response.
     * `VALIDATE_PARAMS`: Lets you verify that all necessary parameters are configured in table `/GOOG/CE_ROUTER`. If any required values are missing, then raise an exception of type `/GOOG/CX_SDK`.



When the ABAP code runs, the Publisher class reads the configurations from this table to guide the event publication process.

## Configure a listener for business events

To capture the events triggered due to changes to business objects, you need to configure an event listener for each business object.

### Create a business event linkage

You create a business event linkage to automatically trigger and publish critical SAP business object changes as events to Google Cloud services, by using the Business Eventing Toolkit for SAP.

With this linkage, you define a receiver that serves as the listener for business events.

To create a business event linkage, do the following:

  1. In SAP GUI, execute the transaction code `SWETYPV`.

  2. Click **New Entries**.

  3. Specify an appropriate business object category and business object type.

  4. Specify an event for which you want to listen and forward the event by using the Business Eventing Toolkit for SAP.

  5. In the **Receiver Type** field, enter either `Google_Cloud` or `Google`.

  6. In the **Linkage Setting (Receiver)** section, provide the following:

     * Receiver Call: Select **Method** from drop-down list.
     * Class Name: Enter `/GOOG/CL_BO_EVENT_FORWARD`.
  7. Select the **Linkage Activated** checkbox.

  8. Save the configuration.




### Map the event listener to an event key

To define how the Business Eventing Toolkit for SAP processes specific SAP business events for Google Cloud integration, map the listener for business events to an event key that maintains the settings for publishing events.

To map the event listener to an event key, do the following:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Business Eventing: Configure Event Listeners for Business Objects**.

  3. Click **New Entries**.

  4. Enter values for the following fields:

Field | Data type | Description  
---|---|---  
**Object Type** | `CHAR` | The name of the business object that you've configured in the transaction `SWETYPV`.  
**Event** | `CHAR` | The name of the event linked to the business object.  
**Name of Receiver** | `CHAR` | The name of the receiver configured in transaction `SWETYPV` against the combination of Object Type and Event.  
**Event Key** | `CHAR` | The name of the publisher event configuration maintained in the Configure target Google Cloud services section.  
**Processor Class** | `CHAR` | Optional. The name of the processor class where you've written any additional logic to fill the event body or extend the extension attributes This class must implement the interface `/GOOG/IF_BOR_EVNT_DATA_HANDLER`. For information about how to create a processor class, see Extend the processor class.  
  5. Save the configuration.




#### Default body and cloud event extension attributes

By default, when you publish events to Pub/Sub, the event listener relays the following attributes from the business event container to the target Google Cloud services:
    
    
    {
      "EVENT_OBJECT": "BUS2012",
      "EVENT_OBJECT_KEY": "450000011",
      "EVENT_NAME": "CHANGED",
      "EVENT_CREATOR": "USER-ID",
      "EVENT_CREATION_DATE": "20250321",
      "EVENT_CREATION_TIME": "135050",
      "EVENT_CREATION_TIMESTAMP": "20250321135050",
      "EVENT_CREATION_LANGUAGE": "EN"
    }
    

If the cloud events attributes are configured, then the payload structure is as follows:
    
    
    {
      "eventObjectType": "BUS2012", - Picked from Event Container
      "eventObjectKey": "450000011", - Picked from Event Container
      "eventName": "RELEASED", - Picked from Event Container
      "eventCreator": "USER", - Picked from Event Container
      "eventCreationDate": "20250321", -Picked from Event Container
      "eventCreationTime": "135850", - Picked from Event Container
      "eventCreationTimestamp": "20250321135850", - Picked from Event Container
      "id": "D5D1CB352A321FD081FFF6EEA9566190", - Auto Populated
      "source": "sap-s4hana-doc",  - Picked from CE Defaults
      "type": "pochanged", - Picked from CE Defaults
      "specversion": "1.0", - Picked from CE Defaults
      "time": "2025-04-09T16:16:38Z", - Auto Populated
      "subject": "test-subject-A" - Picked from CE Defaults Table
    }
    

If you create and configure a processor class in your event listener, then the resulting payload reflects your custom payload structure.

### Extend the processor class

The Business Eventing Toolkit for SAP lets you set the data and add additional extension attributes to cloud events. To do so, implement a class that inherits the interface `/GOOG/IF_BOR_EVNT_DATA_HANDLER` and implement the interface method `FILL_EVENT_DATA`. This method has the following importing and changing parameters:

Name | Type | Associated type | Description  
---|---|---|---  
`SENDER` | Importing | `SIBFLPORB` | Local persistent object reference: BOR compatible  
`EVENT` | Importing | `SIBFEVENT` | Event  
`EVENT_CONTAINER` | Importing | Type Ref To IF_SWF_IFS_PARAMETER_CONTAINER | Container for transfer of parameters  
`RECTYPE` | Importing | `SWFERECTYP` | Name of the receiver type  
`HANDLER` | Importing | `SIBFLPORB` | Local persistent object reference: BOR compatible  
`CT_DATA` | Changing | `/GOOG/CL_PUBLISHER_BASE=>TT_MESSAGES` | Table of messages  
`CT_CE_EXTN_ATTRIBUTES` | Changing | `/GOOG/T_CE_ATTR_VALUE` | Cloud Event: attribute name, value pair table  
  
Sample implementation for business object `BUS2012` (Purchase Order) to include PO header information as cloud event body:
    
    
     TYPES: BEGIN OF ty_event_attributes,
                 ekgrp TYPE ekgrp,
                 werks TYPE werks_d,
                 stlnr TYPE stnum,
                 stlal TYPE mast-stlal,
                 stlty TYPE stko-stlty,
               END OF ty_event_attributes.
        DATA: ls_po_header TYPE bapimepoheader.
    
        DATA: ls_event_attributes TYPE ty_event_attributes,
              lv_json             TYPE string.
    
        DATA ls_data TYPE /goog/cl_publisher_base=>ty_message.
    
        CALL FUNCTION 'BAPI_PO_GETDETAIL1'
          EXPORTING
            purchaseorder = '4500000007'
          IMPORTING
            poheader      = ls_po_header.
    
        /ui2/cl_json=>serialize(
          EXPORTING
            data   = ls_po_header
          RECEIVING
            r_json = lv_json
        ).
    
        ls_data-data = lv_json.
        APPEND ls_data TO ct_data.
    

## Configure a listener for RAP events

For each RAP event that you want to send to Google Cloud, you need to create an event handler class. This event handler class acts as an event listener for that RAP event.

To programmatically create an event handler class, you can use the community resource available on [GitHub](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_UTILITIES/zgoog_business_evt_toolkit). You need to provide the RAP entity details and generate the event handler classes. For information about event objects, see the SAP documentation [SAP Business Accelerator Hub](https://api.sap.com/content-type/Events/events/events).

To manually create an event handler class, do the following:

  1. Create an ABAP class for RAP events:

     1. Right-click your ABAP package and select **New > ABAP Class**.
     2. Enter the following details for your ABAP class:

        * Name: A name for your class, for example, `ZCL_PRODUCT_EXT`.
        * Description: A description for your class, for example, `Event handler for RAP events`.
     3. Click **Finish**.

  2. Update the class definition as follows:
         
         class CLASS_NAME definition
           public
           abstract
           final
           for events of RAP_ENTITY_NAME .
         
             public section.
             protected section.
             private section.
             ENDCLASS.
         
         CLASS CLASS_NAME IMPLEMENTATION.
         ENDCLASS.
         

Replace the following:

     * `CLASS_NAME`: Name of the class, for example, `ZCL_PRODUCT_EXT`.
     * `RAP_ENTITY_NAME`: Name of the RAP entity, for example, `R_PRODUCT`.
  3. Open the **Local Types** tab and create a local implementation:
         
         CLASS lcl_event_extension DEFINITION INHERITING FROM cl_abap_behavior_event_handler.
         
         PRIVATE SECTION.
           METHODS on_EVENT_NAME FOR ENTITY EVENT
              created FOR RAP_ENTITY_NAME~EVENT_NAME.
         ENDCLASS.
         
         CLASS lcl_event_extension IMPLEMENTATION.
         
           METHOD on_EVENT_NAME.
             TRY.
                 /goog/cl_event_publisher=>publish_event(
                   EXPORTING
                     iv_event_key = 'EVENT_KEY'
                     it_data      = VALUE #( FOR <ls_created> IN created (
                                             data = /goog/cl_json=>serialize( data = <ls_created> ) ) )
                   IMPORTING
                     et_output    = DATA(lt_output)
                 ).
               CATCH /goog/cx_sdk INTO DATA(lo_exp).
         "Error handling logic here
             ENDTRY.
           ENDMETHOD.
         ENDCLASS.
         




Replace the following:

  * `EVENT_NAME`: Name of the event, for example, `CREATED`.
  * `RAP_ENTITY_NAME`: Name of the RAP entity, for example, `ZCL_PRODUCT_EXT`.
  * `EVENT_KEY`: Event key that has the target configuration.



## Configure a listener for IDoc events

To capture the events triggered due to changes to [IDoc](https://help.sap.com/docs/SUPPORT_CONTENT/abapconn/3354079801.html#IDocOverview-WhatisanIDoc?), you need to configure an event listener for IDoc events.

### Configure IDoc event listener

To define how the Business Eventing Toolkit for SAP processes IDoc events for Google Cloud integration, configure an event listener for IDoc events. You map the IDoc event listener to an event key that maintains the settings for publishing events.

To configure an IDoc event listener, do the following:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Business Eventing: Configure Event Listeners for IDoc**.

  3. Click **New Entries**.

  4. Enter values for the following fields:

Field | Data type | Description  
---|---|---  
**Basic Type** | `CHAR` | The name of the IDoc basic type for which you want to send events to Google Cloud, for example, `MATMAS05`.  
**IDoc Direction** | `CHAR` | The direction of the IDoc: **Inbound** or **Outbound**.  
**Event Key** | `CHAR` | The name of the publisher event configuration maintained in the Configure target Google Cloud services section.  
**Processor Class** | `CHAR` | Optional. The name of the processor class where you've written any additional logic to fill the event body or extend the extension attributes This class must implement the interface `/GOOG/IF_IDOC_EVT_DATA_HANDLER`. For information about how to create a processor class, see Extend the processor class.  
  5. Save the configuration.




#### Default body and cloud event extension attributes

By default, when you publish events to Pub/Sub, the event listener relays the following attributes:
    
    
    {
      "messages": [
        {
          "attributes": {
            "idocNumber": "0000000000000134",
            "direct": "1",
            "messageType": "MATMAS",
            "basicType": "MATMAS05",
            "createdOn": "20250515",
            "createdAt": "132254",
            "updatedOn": "20250410",
            "updatedAt": "144958"
          },
          "data": [
            {
              "mandt": "100",
              "docnum": "0000000000000132",
              "segnum": "000001",
              "segnam": "E1MARAM",
              "hlevel": "02",
              "dtint2": 1000,
              "sdata": "    TEST-MATNR-IDOC-0111032025KRITIS       11032025KRITIS     KL                  ROH C01                       EA"
            },
            {
              "mandt": "100",
              "docnum": "0000000000000132",
              "segnum": "000002",
              "segnam": "E1MARA1",
              "psgnum": "000001",
              "hlevel": "03",
              "dtint2": 1000
            }
            // ...additional IDOC segments
          ]
        }
      ]
    }
    

If the cloud events attributes are configured, then the payload structure is as follows:
    
    
    {
      "id": "D5D1CB352A321FD081FFF6EEA9566190",   // Auto Populated
      "source": "sap-s4hana-doc",               // Picked from CE Defaults
      "type": "pochanged",                      // Picked from CE Defaults
      "specversion": "1.0",                     // Picked from CE Defaults
      "time": "2025-04-09T16:16:38Z",           // Auto Populated
      "subject": "test-subject-A",              // Picked from CE Defaults Table
      "messages": [
        {
          "attributes": {
            "idocNumber": "0000000000000134",
            "direct": "1",
            "messageType": "MATMAS",
            "basicType": "MATMAS05",
            "createdOn": "20250515",
            "createdAt": "132254",
            "updatedOn": "20250410",
            "updatedAt": "144958"
          },
          "data": [
            {
              "mandt": "100",
              "docnum": "0000000000000132",
              "segnum": "000001",
              "segnam": "E1MARAM",
              "hlevel": "02",
              "dtint2": 1000,
              "sdata": "    TEST-MATNR-IDOC-0111032025KRITIS       11032025KRITIS     KL                  ROH C01                       EA"
            },
            {
              "mandt": "100",
              "docnum": "0000000000000132",
              "segnum": "000002",
              "segnam": "E1MARA1",
              "psgnum": "000001",
              "hlevel": "03",
              "dtint2": 1000
            }
            // ...additional IDOC segments
          ]
        }
      ]
    }
    

If you create and configure a processor class in your event listener, then the resulting payload reflects your custom payload structure.

### Extend the processor class

The Business Eventing Toolkit for SAP lets you customize event data and add extension attributes to cloud events. To do so, implement a class that inherits the interface `/GOOG/IF_IDOC_EVT_DATA_HANDLER` and implement the interface method `FILL_EVENT_DATA`.

The `FILL_EVENT_DATA` method has the following parameters:

Name | Type | Associated type | Description  
---|---|---|---  
`IS_IDOC_CONTRL` | Importing | `EDIDC` | The control records of the IDoc.  
`IT_IDOC_DATA` | Importing | `TAB_EDIDD` | Table of IDoc data records.  
`CT_DATA` | Changing | `/GOOG/CL_PUBLISHER_BASE=>TT_MESSAGES` | Table of messages  
`CT_CE_EXTN_ATTRIBUTES` | Changing | `/GOOG/T_CE_ATTR_VALUE` | Cloud Event: attribute name, value pair table  
  
### Integrate IDoc event publishing with standard SAP IDoc process

To publish IDoc events to Google Cloud services, you need to integrate the Business Eventing Toolkit for SAP's IDoc event forwarding logic into your existing SAP IDoc processing. This ensures that when IDocs are created, changed, or reach a specific status, their data is automatically published as events.

You can integrate IDoc event publishing using one of the following methods:

#### Use the `IDOC_DATA_MAPPER` BAdI

The `IDOC_DATA_MAPPER` [Business Add-In (BAdI)](https://help.sap.com/viewer/46a2cfc13d25463b8b9a3d2a3c3ba0d9/LATEST/en-US/8ff2e540f8648431e10000000a1550b0.html) lets you implement custom logic that triggers during both inbound and outbound IDoc processing. You can use this BAdI to publish IDoc events to Google Cloud.

To implement the `IDOC_DATA_MAPPER` BAdI, do the following:

  1. Open the transaction `SE18`.
  2. In the **BAdI Name** field, enter `IDOC_DATA_MAPPER`.
  3. Navigate to the **Implementation** menu and select **Create**.
  4. In the **Name of Enhancement Implementation** field, enter a name for the enhancement implementation, for example, `ZEI_IDOC_DATA_MAPPER`.
  5. Within the implementation, update the name of the implementing class to `/GOOG/CL_IM_BADI_IDOC_MAPPER`.
  6. Activate your BAdI implementation.



#### Use your existing enhancement exits

If you've existing enhancement exits in your IDoc processing flow, you can insert the IDoc event publishing logic directly into them.

Insert the following ABAP snippet into your enhancement exit:
    
    
    DATA : lt_return TYPE bapiret2_t.
    
    /goog/cl_idoc_event_forward=>publish_event(
          EXPORTING
            is_control = IDOC_CONTROL " Replace with your IDoc control record
            it_data    = IDOC_DATA " Replace with your IDoc data records
          IMPORTING
            et_return  = lt_return
    ).
    
    " Handle errors if LT_RETURN contains erroneous records.
    

Replace the following:

  * `IDOC_CONTROL`: The IDoc [control record](https://help.sap.com/docs/SUPPORT_CONTENT/abapconn/3354079801.html#IDocOverview-ControlRecord).
  * `IDOC_DATA`: The IDoc [data records](https://help.sap.com/docs/SUPPORT_CONTENT/abapconn/3354079801.html#IDocOverview-DataRecords).



#### Use a custom function module (Based on the `OWN_FUNCTION` template)

For publishing outbound IDoc events, you can configure SAP IDoc processing to call a custom function module, which is based on the standard [`OWN_FUNCTION`](https://help.sap.com/doc/saphelp_gbt10/1.0/en-US/4b/4011826f820a93e10000000a421937/frameset.htm) template. This custom function module lets you process IDoc data and trigger event publication before the data is sent to the Google Cloud target service.

For detailed configuration steps on using a custom function module to publish outbound IDoc events, see [Business Eventing Toolkit for SAP Utilities](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_UTILITIES/zgoog_business_evt_toolkit#configure-outbound-idoc-events). While implementing your custom function, you can use the sample Z-implementation available on [GitHub](https://github.com/GoogleCloudPlatform/google-cloud-abap/blob/main/abap-sdk/ZGOOG_SDK_UTILITIES/zgoog_business_evt_toolkit/src/zfg_eventing_utility.fugr.zfm_idoc_own_function.abap).

## Get support

If you need help resolving problems with the on-premises or any cloud edition of ABAP SDK for Google Cloud, then do the following:

  * Refer to the [ on-premises or any cloud edition of ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).

  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

  * Collect all available [diagnostic information](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/getting-support-diag-info) and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
