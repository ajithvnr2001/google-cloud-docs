---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events/
title: Publish events through the Business Eventing Toolkit for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:29.510158+00:00
---

# Publish events through the Business Eventing Toolkit for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Publish events through the Business Eventing Toolkit for SAP Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/eventing-toolkit-for-sap-publish-events)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events)



This document describes how to publish events through the Business Eventing Toolkit for SAP.

## Publish events programmatically to configured Google Cloud targets

The target service is derived based on the configured target Google Cloud services. For information about how to configure target Google Cloud services, see [Configure target Google Cloud services](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-configuration#configure-target-gc-service).

The following code snippet shows how to publish event data to configured targets:
    
    
    /goog/cl_event_publisher=>publish_event(
         EXPORTING
            iv_event_key = 'EVENT_KEY'
            it_data      = VALUE /goog/cl_publisher_base=>tt_messages( ( data = 'Hello World!' ) )
         IMPORTING
            et_output    = DATA(lt_output)
            et_return    = DATA(lt_return)
    ).
    

Replace `EVENT_KEY` with the event key configured for publishing events to your [target Google Cloud services](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-configuration#configure-target-gc-service).

To send an event as a CloudEvent, you can configure the **Cloud Event Default Attribute Key** and attach this key to your **Event Key** when configuring the [target Google Cloud services](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-configuration#configure-target-gc-service). The Business Eventing Toolkit for SAP then picks up the default attribute values for the CloudEvent.

## Publish API requests programmatically as CloudEvents with default values

The following code snippet shows how to publish an HTTP API request as a CloudEvent with default values:
    
    
    lo_api_client->encode_as_cloud_event(
       EXPORTING
          iv_ce_key         = 'CLOUD_EVENT_ATTRIBUTE_KEY'
    ).
    

Replace `CLOUD_EVENT_ATTRIBUTE_KEY` with the **Cloud Event Default Attribute Key** configured in the [Configure CloudEvent attributes](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-configuration#configure-cloud-event-attributes) section.

## Publish API requests programmatically as CloudEvents

To override the default values defined in the configuration table when you publish a business event as a CloudEvent programmatically, you can pass specific values for CloudEvent attributes using the `ENCODE_AS_CLOUD_EVENT` method.

The following code snippet shows how to override the default values when encoding an HTTP request as a CloudEvent:
    
    
    lo_api_client->encode_as_cloud_event(
       EXPORTING
          "mandatory attributes
          iv_source         = 'SAP'
          iv_type           = 'ce.structured-ce'
          " add optional attributes
          iv_subject        = 'test'
          " extension attributes -> key,value
          it_extension_attr = VALUE #( ( name = 'my_ext_attr1' value = 'my_ext_value1')
                                       ( name = 'my_ext_attr2' value = 'my_ext_value2' ) )
          iv_encoding       = /goog/if_ce_spec_version=>c_ce_encoding-binary
    ).
    

Explore the following to publish your SAP events:

  * [Publish events to Pub/Sub](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events-pubsub)
  * [Publish events to Cloud Run functions](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events-cloud-functions)
  * [Publish events to Firebase Cloud Messaging](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events-fcm)
  * [Publish events to Integration Connectors](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events-integration-connectors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
