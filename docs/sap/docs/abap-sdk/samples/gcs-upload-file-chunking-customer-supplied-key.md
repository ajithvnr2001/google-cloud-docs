---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/samples/gcs-upload-file-chunking-customer-supplied-key/
title: Upload file with chunking and customer-supplied encryption key \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:45.080417+00:00
---

# Upload file with chunking and customer-supplied encryption key  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/samples/gcs-upload-file-chunking-customer-supplied-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Samples ](https://docs.cloud.google.com/sap/docs/abap-sdk/samples/all-samples)



Send feedback 

#  Upload file with chunking and customer-supplied encryption key Stay organized with collections  Save and categorize content based on your preferences. 

This code sample can be used to upload a large object to a Cloud Storage bucket using chunking and providing customer-supplied encryption keys to encrypt the object.

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
    CLASS zcl_cs_upload_object_rescskey DEFINITION
      PUBLIC FINAL
      CREATE PUBLIC.
    
      PUBLIC SECTION.
        INTERFACES if_oo_adt_classrun.
    ENDCLASS.
    
    
    CLASS zcl_cs_upload_object_rescskey IMPLEMENTATION.
      METHOD if_oo_adt_classrun~main.
        " Data Declarations
        DATA lv_p_bucket     TYPE string.
        DATA lv_q_name       TYPE string.
        DATA ls_data         TYPE xstring.
        DATA lv_content_type TYPE string.
    
        TRY.
            " Open HTTP Connection
            " Pass the configured client key
            DATA(lo_client) = NEW /goog/cl_storage_v1( iv_key_name = 'CLIENT_KEY' ).
    
            " Populate the data that needs to be passed to the api
            " Name of the bucket
            lv_p_bucket = 'sample-bucket'.
            " Name of the object
            lv_q_name   = 'sample-object'.
            " Read object data into ls_data
            ls_data         = '<Object data in XSTRING form>'.
            " Content type of the object
            lv_content_type = '<Content Type>'.
    
            " Set the common query parameter uploadType as 'resumable'
            " Default chunk size is 8MB
            lo_client->add_common_qparam( iv_name  = 'uploadType'
                                          iv_value = 'resumable' ).
    
            " Set custom headers for Customer Supplied Encryption keys
            lo_client->add_custom_header( iv_name  = 'X-GOOG-ENCRYPTION-ALGORITHM'
                                          iv_value = 'AES256' ). " Supported encryption algorithm
    
            " Base64-encoded string of your AES-256 encryption key
            lo_client->add_custom_header( iv_name  = 'X-Goog-Encryption-Key'
                                          iv_value = '<Encryption Key>' ).
    
            " Base64-encoded string of the SHA256 hash of your encryption key
            lo_client->add_custom_header( iv_name  = 'X-Goog-Encryption-Key-Sha256'
                                          iv_value = '<SHA256 of the Encryption Key>' ).
    
            " Call API method
            lo_client->insert_objects( EXPORTING iv_q_name       = lv_q_name
                                                 iv_p_bucket     = lv_p_bucket
                                                 is_data         = ls_data
                                                 iv_content_type = lv_content_type
                                       IMPORTING es_output       = DATA(ls_output)
                                                 ev_ret_code     = DATA(lv_ret_code)
                                                 ev_err_text     = DATA(lv_err_text)
                                                 es_err_resp     = DATA(ls_err_resp) ).
    
            IF lo_client->is_success( lv_ret_code ).
              out->write( 'File uploaded successfully' ).
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
    
    REPORT zr_upload_object_rescskey.
    
    * Data Declarations
    DATA:
      lv_p_bucket     TYPE string,
      lv_q_name       TYPE string,
      ls_data         TYPE xstring,
      lv_content_type TYPE string.
    
    TRY.
    *  Open HTTP Connection
        DATA(lo_client) = NEW /goog/cl_storage_v1( iv_key_name = 'CLIENT_KEY' ).
    
    *   Populate the data that needs to be passed to the api
        "Name of the bucket
        lv_p_bucket       = 'sample-bucket'.
        "Name of the object
        lv_q_name         = 'sample-object'.
        "Read object data into ls_data
        ls_data          = '<Object data in XSTRING form>'.
        "Content type of the object
        lv_content_type  = '<Content Type>'.
    
        "Set the common query parameter uploadType as 'resumable'
        "Default chunk size is 8MB
        CALL METHOD lo_client->add_common_qparam
          EXPORTING
            iv_name  = 'uploadType'
            iv_value = 'resumable'.
    
    *   Set custom headers for Customer Supplied Encryption keys
        CALL METHOD lo_client->add_custom_header
          EXPORTING
            iv_name  = 'X-GOOG-ENCRYPTION-ALGORITHM'
            iv_value = 'AES256'. "Supported encryption algorithm
    
        "Base64-encoded string of your AES-256 encryption key
        CALL METHOD lo_client->add_custom_header
          EXPORTING
            iv_name  = 'X-Goog-Encryption-Key'
            iv_value = '<Encryption Key>'.
    
        "Base64-encoded string of the SHA256 hash of your encryption key
        CALL METHOD lo_client->add_custom_header
          EXPORTING
            iv_name  = 'X-Goog-Encryption-Key-Sha256'
            iv_value = '<SHA256 of the Encryption Key>'.
    
    * Call API method
        CALL METHOD lo_client->insert_objects
          EXPORTING
            iv_q_name       = lv_q_name
            iv_p_bucket     = lv_p_bucket
            is_data         = ls_data
            iv_content_type = lv_content_type
          IMPORTING
            es_output       = DATA(ls_output)
            ev_ret_code     = DATA(lv_ret_code)
            ev_err_text     = DATA(lv_err_text)
            es_err_resp     = DATA(ls_err_resp).
    
    
    
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
