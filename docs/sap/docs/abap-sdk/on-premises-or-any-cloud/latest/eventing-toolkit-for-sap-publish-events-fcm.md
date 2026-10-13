---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events-fcm/
title: Publish events to Firebase Cloud Messaging \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:35.361636+00:00
---

# Publish events to Firebase Cloud Messaging  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events-fcm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Publish events to Firebase Cloud Messaging Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/eventing-toolkit-for-sap-publish-events-fcm)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events-fcm)



The document describes how to publish events to Firebase Cloud Messaging (FCM) through the Business Eventing Toolkit for SAP.

## Prerequisites

Make sure that you or your administrators have completed the following prerequisites:

  * Enabled the Firebase Cloud Messaging API. For information about how to enable Firebase Cloud Messaging APIs, see [Enabling APIs](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api).
  * Configured a client key for authentication. For information about how to set up authentication in the on-premises or any cloud edition of ABAP SDK for Google Cloud, see [Authentication overview](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).
  * The service account configured in the client key for authentication must have the following role: [Firebase Cloud Messaging API Admin (`roles/firebasenotifications.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/firebasecloudmessaging#firebasenotifications.admin).
  * Configured target Google Cloud services with the following details:

    * **Event Processor Class** : `/GOOG/CL_PUBLISHER_FCM`
    * **Google Cloud Key Name** : The client key for authentication.
    * **Event Parameter 1** : The name of the FCM topic.
    * **Event Parameter 2** : Optional. The name of the FCM notification title.

For information about how to configure target Google Cloud services, see [Configure target Google Cloud services](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-configuration#configure-target-gc-service).




## Publish events

To publish event data to Firebase Cloud Messaging, call the `publish()` method:
    
    
    DATA: lt_data TYPE /goog/if_ce_publisher=>tt_messages.
    
    " Write logic to populate LT_DATA.
    lt_data = VALUE #( ( data = 'Hello World!' ) ).
    
    /goog/cl_event_publisher=>publish_event(
          EXPORTING
            iv_event_key = 'EVENT_KEY'
            it_data      = lt_data
          IMPORTING
            et_output    = DATA(lt_output)
        ev_ret_code  = DATA(lv_ret_code)
    ev_err_text  = DATA(lv_err_text)
    ).
    

Replace `EVENT_KEY` with the event key configured for publishing events to Firebase Cloud Messaging.

To send an event as a CloudEvent, you can configure the **Cloud Event Default Attribute Key** and attach this key to your **Event key** when configuring the [target Google Cloud services](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-configuration#configure-target-gc-service). The Business Eventing Toolkit for SAP then picks up the default attribute values for the CloudEvent.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
