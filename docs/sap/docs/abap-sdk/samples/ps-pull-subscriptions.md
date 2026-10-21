---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/samples/ps-pull-subscriptions/
title: Pull subscriptions \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:52.731967+00:00
---

# Pull subscriptions  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/samples/ps-pull-subscriptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Samples ](https://docs.cloud.google.com/sap/docs/abap-sdk/samples/all-samples)



Send feedback 

#  Pull subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

This code sample can be used to pull messages that were published to a Pub/Sub Topic using a subscription.

For a comprehensive collection of code samples for the SAP BTP edition of ABAP SDK for Google Cloud, see the [code sample repository on GitHub](https://github.com/GoogleCloudPlatform/abapsdk-btp-samples/tree/main/src/zgoog_sdk_btp_code_samples).

For a comprehensive collection of code samples for the on-premises or any cloud edition of ABAP SDK for Google Cloud, see the [code samples repository on GitHub](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_DOCS_SAMPLES).

## Code sample

### SAP BTP edition
    
    
    " --------------------------------------------------------------------
    "  Copyright 2024 Google LLC                                         -
    "                                                                    -
    "  Licensed under the Apache License, Version 2.0 (the "License");   -
    "  you may not use this file except in compliance with the License.  -
    "  You may obtain a copy of the License at                           -
    "      https://www.apache.org/licenses/LICENSE-2.0                   -
    "  Unless required by applicable law or agreed to in writing,        -
    "  software distributed under the License is distributed on an       -
    "  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,      -
    "  either express or implied.                                        -
    "  See the License for the specific language governing permissions   -
    "  and limitations under the License.                                -
    " --------------------------------------------------------------------
    CLASS zcl_cs_pull_subscriptions DEFINITION
      PUBLIC FINAL
      CREATE PUBLIC.
    
      PUBLIC SECTION.
        INTERFACES if_oo_adt_classrun.
    ENDCLASS.
    
    
    CLASS zcl_cs_pull_subscriptions IMPLEMENTATION.
      METHOD if_oo_adt_classrun~main.
        " Data Declarations
        DATA lv_p_projects_id      TYPE string.
        DATA lv_p_subscriptions_id TYPE string.
        DATA ls_input              TYPE /goog/cl_pubsub_v1=>ty_026.
        DATA ls_input_ack          TYPE /goog/cl_pubsub_v1=>ty_001.
    
        TRY.
    
            " Open HTTP Connection
            DATA(lo_pubsub) = NEW /goog/cl_pubsub_v1( iv_key_name = 'PUBSUB_DEMO' ).
    
            " Populate relevant parameters
            " Derive project id from the client object
            lv_p_projects_id = lo_pubsub->gv_project_id.
            " Name of the subscription from where we want to pull data
            lv_p_subscriptions_id = 'SAMPLE_SUBSCRIPTION'.
            " Max number of messages that will be received in 1 API call
            ls_input-max_messages = 1.
    
            " Call API method
            lo_pubsub->pull_subscriptions( EXPORTING iv_p_projects_id      = lv_p_projects_id
                                                     iv_p_subscriptions_id = lv_p_subscriptions_id
                                                     is_input              = ls_input
                                           IMPORTING es_output             = DATA(ls_output)
                                                     ev_ret_code           = DATA(lv_ret_code)
                                                     ev_err_text           = DATA(lv_err_text)
                                                     es_err_resp           = DATA(ls_err_resp) ).
    
            IF /goog/cl_http_client=>is_success( lv_ret_code ).
              IF ls_output-received_messages IS NOT INITIAL.
                " Messages published to Pub/Sub should be base-64 encoded
                " Therefore in order to get the exact message, we need to decode the data field.
                " However, attributes published to Pub/Sub should be accessible without any additional logic.
                DATA(lv_msg) = | MESSAGE Received: { cl_http_utility=>decode_base64(
                                                         encoded = ls_output-received_messages[ 1 ]-message-data ) }|.
                APPEND ls_output-received_messages[ 1 ]-ack_id TO ls_input_ack-ack_ids.
    
                " Call API method: pubsub.projects.subscriptions.acknowledge
                " Acknowledge the messages so it is not pulled again.
                lo_pubsub->acknowledge_subscriptions( EXPORTING iv_p_projects_id      = lv_p_projects_id
                                                                iv_p_subscriptions_id = lv_p_subscriptions_id
                                                                is_input              = ls_input_ack
                                                      IMPORTING es_output             = DATA(ls_output_ack)
                                                                ev_ret_code           = lv_ret_code
                                                                ev_err_text           = lv_err_text
                                                                es_err_resp           = ls_err_resp ).
    
                IF lo_pubsub->is_success( lv_ret_code ).
                  out->write( | Error occurred: { lv_msg }| ).
                ELSE.
                  out->write( | Error occurred: { lv_err_text }| ).
                ENDIF.
              ELSE.
                out->write( | No Messages were received!| ).
              ENDIF.
            ELSE.
              out->write( | Error occurred: { lv_err_text }| ).
            ENDIF.
    
            " Close HTTP Connection
            lo_pubsub->close( ).
    
          CATCH /goog/cx_sdk INTO DATA(lo_exception).
            lv_err_text = lo_exception->get_text( ).
            out->write( |Exception occurred: { lv_err_text } | ).
        ENDTRY.
      ENDMETHOD.
    ENDCLASS.
    

### On-premises or any cloud edition
    
    
    **********************************************************************
    *  Copyright 2023 Google LLC                                         *
    *                                                                    *
    *  Licensed under the Apache License, Version 2.0 (the "License");   *
    *  you may not use this file except in compliance with the License.  *
    *  You may obtain a copy of the License at                           *
    *      https://www.apache.org/licenses/LICENSE-2.0                   *
    *  Unless required by applicable law or agreed to in writing,        *
    *  software distributed under the License is distributed on an       *
    *  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,      *
    *  either express or implied.                                        *
    *  See the License for the specific language governing permissions   *
    *  and limitations under the License.                                *
    **********************************************************************
    
    REPORT zr_pull_subscriptions.
    
    DATA:
      lv_p_projects_id      TYPE string,
      lv_p_subscriptions_id TYPE string,
      ls_input              TYPE /goog/cl_pubsub_v1=>ty_026,
      ls_input_ack          TYPE /goog/cl_pubsub_v1=>ty_001.
    
    TRY.
    
    * Open HTTP Connection
        DATA(lo_client) = NEW /goog/cl_pubsub_v1( iv_key_name = 'CLIENT_KEY' ).
    
    * Populate relevant parameters
        " Derive project id from the client object
        lv_p_projects_id = lo_client->gv_project_id.
        " Name of the subscription from where we want to pull data
        lv_p_subscriptions_id = 'SAMPLE_SUBSCRIPTION'.
        " Max number of messages that will be received in 1 API call
        ls_input-max_messages = 1.
    
    * Call API method
        CALL METHOD lo_client->pull_subscriptions
          EXPORTING
            iv_p_projects_id      = lv_p_projects_id
            iv_p_subscriptions_id = lv_p_subscriptions_id
            is_input              = ls_input
          IMPORTING
            es_output             = DATA(ls_output)
            ev_ret_code           = DATA(lv_ret_code)
            ev_err_text           = DATA(lv_err_text)
            es_err_resp           = DATA(ls_err_resp).
    
        IF /goog/cl_http_client=>is_success( lv_ret_code ).
          IF ls_output-received_messages IS NOT INITIAL.
            "Messages published to Pub/Sub should be base-64 encoded, hence in order to get the exact message, we need to decode the data field.
            "However, attributes published to Pub/Sub should be accessible without any additional logic.
            DATA(lv_msg) = | Message Received: { cl_http_utility=>decode_base64( encoded = ls_output-received_messages[ 1 ]-message-data ) }|.
            APPEND ls_output-received_messages[ 1 ]-ack_id TO ls_input_ack-ack_ids.
    
    * Call API method: pubsub.projects.subscriptions.acknowledge
            "Acknowledge the messages so it is not pulled again.
            CALL METHOD lo_client->acknowledge_subscriptions
              EXPORTING
                iv_p_projects_id      = lv_p_projects_id
                iv_p_subscriptions_id = lv_p_subscriptions_id
                is_input              = ls_input_ack
              IMPORTING
                es_output             = DATA(ls_output_ack)
                ev_ret_code           = lv_ret_code
                ev_err_text           = lv_err_text
                es_err_resp           = ls_err_resp.
    
            IF lo_client->is_success( lv_ret_code ).
              MESSAGE lv_msg TYPE 'S'.
            ELSE.
              MESSAGE lv_err_text TYPE 'E'.
            ENDIF.
          ELSE.
            MESSAGE 'No Messages were received!' TYPE 'S'.
          ENDIF.
        ELSE.
          MESSAGE lv_err_text TYPE 'E'.
        ENDIF.
    
    * Close HTTP Connection
        lo_client->close( ).
    
      CATCH /goog/cx_sdk INTO DATA(lo_exception).
        MESSAGE lo_exception->get_text( ) TYPE 'E'.
    ENDTRY.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
