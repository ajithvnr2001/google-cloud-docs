---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events-cloud-functions/
title: Publish events to Cloud Run functions \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:35.078285+00:00
---

# Publish events to Cloud Run functions  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events-cloud-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Publish events to Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/eventing-toolkit-for-sap-publish-events-cloud-functions)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events-cloud-functions)



The document describes how to publish events to Cloud Run functions through the Business Eventing Toolkit for SAP.

## Prerequisites

Make sure that you or your administrators have completed the following prerequisites:

  * Enabled the Cloud Run functions API. For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api).
  * Configured a client key for authentication. For information about how to set up authentication in the on-premises or any cloud edition of ABAP SDK for Google Cloud, see [Authentication overview](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).
  * The service account configured in the client key for authentication must have the following roles:

    * For gen-1 Cloud Run functions: [Cloud Functions Invoker (`roles/cloudfunctions.invoker`)](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.invoker)
    * For gen-2 Cloud Run functions: [Cloud Run Invoker (`roles/run.invoker`)](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.invoker)
  * Configure target Google Cloud services with the following details:

    * **Event Processor Class** : `/GOOG/CL_PUBLISHER_CLOUDFUNC`
    * **Google Cloud Key Name** : The client key for authentication.
    * **Event Parameter 1** : The name of the Cloud Run functions.
    * **Event Parameter 2** : The location of the Cloud Run functions.
    * **Event Parameter 3** : Optional. The HTTP method used. For example, `GET`, `POST`. If not provided, then the default is `GET`.

For information about how to configure target Google Cloud services, see [Configure target Google Cloud services](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-configuration#configure-target-gc-service).




## Publish events

To publish event data to Cloud Run functions, call the `publish()` method:
    
    
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
    

Replace `EVENT_KEY` with the event key configured for publishing events to Cloud Run functions.

To send an event as a CloudEvent, you can configure the **Cloud Event Default Attribute Key** and attach this key to your **Event key** when configuring the [target Google Cloud services](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-configuration#configure-target-gc-service). The Business Eventing Toolkit for SAP then picks up the default attribute values for the CloudEvent.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
