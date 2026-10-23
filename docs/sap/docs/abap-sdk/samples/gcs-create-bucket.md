---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/samples/gcs-create-bucket/
title: Create bucket \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:45.522488+00:00
---

# Create bucket  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/samples/gcs-create-bucket/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Samples ](https://docs.cloud.google.com/sap/docs/abap-sdk/samples/all-samples)



Send feedback 

#  Create bucket Stay organized with collections  Save and categorize content based on your preferences. 

This code sample can be used to create a bucket in Cloud Storage.

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
    CLASS zcl_cs_create_buckets DEFINITION
      PUBLIC FINAL
      CREATE PUBLIC.
    
      PUBLIC SECTION.
        INTERFACES if_oo_adt_classrun.
    ENDCLASS.
    
    
    CLASS zcl_cs_create_buckets IMPLEMENTATION.
      METHOD if_oo_adt_classrun~main.
        " Data Declarations
        DATA lv_q_project TYPE string.
        DATA ls_input     TYPE /goog/cl_storage_v1=>ty_001.
    
        TRY.
            " Open HTTP Connection
            " Pass the configured client key
            DATA(lo_client) = NEW /goog/cl_storage_v1( iv_key_name = 'CLIENT_KEY' ).
    
            " Populate the data that needs to be passed to the API
            " Derive project id from the client object
            lv_q_project  = lo_client->gv_project_id.
    
            " Name of the bucket, please note bucket name has to be unique and global
            ls_input-name = 'sample-bucket'.
    
            " Call API method
            lo_client->insert_buckets( EXPORTING iv_q_project = lv_q_project
                                                 is_input     = ls_input
                                       IMPORTING es_output    = DATA(ls_output)
                                                 ev_ret_code  = DATA(lv_ret_code)
                                                 ev_err_text  = DATA(lv_err_text)
                                                 es_err_resp  = DATA(ls_err_resp) ).
    
            IF lo_client->is_success( lv_ret_code ).
              out->write( 'Bucket created successfully!' ).
            ELSE.
              out->write( | Error occurred: { lv_err_text }| ).
            ENDIF.
    
            " Close HTTP connection
            lo_client->close( ).
    
          CATCH /goog/cx_sdk INTO DATA(lo_sdk_excp).
            lv_err_text = lo_sdk_excp->get_text( ).
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
    
    REPORT zr_insert_buckets.
    
    
    * Data Declarations
    DATA:
      lv_q_project TYPE string,
      ls_input     TYPE /goog/cl_storage_v1=>ty_001.
    
    TRY.
    *  Open HTTP Connection
        DATA(lo_client) = NEW /goog/cl_storage_v1( iv_key_name = 'CLIENT_KEY' ).
    
    *   Populate the data that needs to be passed to the api
        "Derive project id from the client object
        lv_q_project  = lo_client->gv_project_id.
        "Name of the bucket
        ls_input-name = 'sample-bucket'.
    
    *   Call API method
        CALL METHOD lo_client->insert_buckets
          EXPORTING
            iv_q_project = lv_q_project
            is_input     = ls_input
          IMPORTING
            es_output    = DATA(ls_output)
            ev_ret_code  = DATA(lv_ret_code)
            ev_err_text  = DATA(lv_err_text)
            es_err_resp  = DATA(ls_err_resp).
    
        IF lo_client->is_success( lv_ret_code ).
          MESSAGE 'Bucket created successfully!' TYPE 'S'.
        ELSE.
          MESSAGE lv_err_text TYPE 'E'.
        ENDIF.
    
    *   Close HTTP connection
        lo_client->close( ).
    
      CATCH /goog/cx_sdk INTO DATA(lo_exception).
        MESSAGE lo_exception->get_text( ) TYPE 'E'.
    ENDTRY.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
