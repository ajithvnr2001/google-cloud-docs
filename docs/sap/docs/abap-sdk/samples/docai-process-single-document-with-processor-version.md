---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/samples/docai-process-single-document-with-processor-version/
title: Process a single document with a processor version \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:19.883799+00:00
---

# Process a single document with a processor version  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/samples/docai-process-single-document-with-processor-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Samples ](https://docs.cloud.google.com/sap/docs/abap-sdk/samples/all-samples)



Send feedback 

#  Process a single document with a processor version Stay organized with collections  Save and categorize content based on your preferences. 

This code sample can be used to process a single document using a specified processor version.

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
    CLASS zcl_cs_process_processor_vers DEFINITION
      PUBLIC FINAL
      CREATE PUBLIC.
    
      PUBLIC SECTION.
        INTERFACES if_oo_adt_classrun.
    ENDCLASS.
    
    
    CLASS zcl_cs_process_processor_vers IMPLEMENTATION.
      METHOD if_oo_adt_classrun~main.
        " Data Declarations
        DATA lv_p_projects_id           TYPE string.
        DATA lv_p_locations_id          TYPE string.
        DATA lv_p_processors_id         TYPE string.
        DATA lv_p_processor_versions_id TYPE string.
        DATA ls_input                   TYPE /goog/cl_documentai_v1=>ty_084.
        DATA lv_output                  TYPE /goog/cl_documentai_v1=>ty_085.
        DATA lo_exception               TYPE REF TO /goog/cx_sdk.
    
        TRY.
            " Open HTTP Connection
            DATA(lo_client) = NEW /goog/cl_documentai_v1( iv_key_name = 'DEMO_DOCAI' ).
    
            " Populate relevant parameters
            lv_p_projects_id = lo_client->gv_project_id.
            " Location ID of the Processor
            lv_p_locations_id = 'LOCATION_ID'.
            " Processor ID of the Processor
            lv_p_processors_id = 'PROCESSOR_ID'.
            " Processor Version of the Processor
            lv_p_processor_versions_id = 'PROCESSOR_VERSION_ID'.
            " File contents in base64-encoded format
            ls_input-raw_document-content   = 'CONTENT'.
            " MIME Type of the file
            ls_input-raw_document-mime_type = 'MIME_TYPE'.
    
            " Call API method
            lo_client->process_processor_versions( EXPORTING iv_p_projects_id           = lv_p_projects_id
                                                             iv_p_locations_id          = lv_p_locations_id
                                                             iv_p_processors_id         = lv_p_processors_id
                                                             iv_p_processor_versions_id = lv_p_processor_versions_id
                                                             is_input                   = ls_input
                                                   IMPORTING es_output                  = DATA(ls_output)
                                                             ev_ret_code                = DATA(lv_ret_code)
                                                             ev_err_text                = DATA(lv_err_text)
                                                             es_err_resp                = DATA(ls_err_resp) ).
            IF /goog/cl_http_client=>is_success( lv_ret_code ).
              out->write( | Success | ).
            ELSE.
              out->write( | Error occurred: { lv_err_text }| ).
            ENDIF.
    
            " Close HTTP Connection
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
    
    REPORT zr_process_processor_versions.
    
    DATA:
      lt_bin_data                TYPE STANDARD TABLE OF char1024,
      ls_input                   TYPE /goog/cl_documentai_v1=>ty_084,
      lv_p_projects_id           TYPE string,
      lv_p_locations_id          TYPE string,
      lv_p_processors_id         TYPE string,
      lv_p_processor_versions_id TYPE string,
      lv_file                    TYPE string,
      lv_file_length             TYPE i,
      lv_xfile                   TYPE xstring,
      lv_output                  TYPE string.
    
    lv_file = 'BROWSED_FILE_PATH'.  "File path of document to be processed
    
    * Call function module to upload the file contents
    CALL FUNCTION 'GUI_UPLOAD'
      EXPORTING
        filename   = lv_file
        filetype   = 'BIN'
      IMPORTING
        filelength = lv_file_length
      TABLES
        data_tab   = lt_bin_data.
    
    * Call function module to convert file contents from 'BIN' to 'XSTRIG' format
    CALL FUNCTION 'SCMS_BINARY_TO_XSTRING'
      EXPORTING
        input_length = lv_file_length
      IMPORTING
        buffer       = lv_xfile
      TABLES
        binary_tab   = lt_bin_data.
    
    * Call function module to convert the file contents from 'XSTRING' to 'base-64 encoded' format
    CALL FUNCTION 'SCMS_BASE64_ENCODE_STR'
      EXPORTING
        input  = lv_xfile
      IMPORTING
        output = lv_output.
    
    TRY.
    * Open HTTP Connection
        DATA(lo_client) = NEW /goog/cl_documentai_v1( iv_key_name = 'CLIENT_KEY' ).
    
    * Populate relevant parameters
        lv_p_projects_id = lo_client->gv_project_id.
        lv_p_locations_id = 'LOCATION_ID'.  "Location ID of the Processor
        lv_p_processors_id = 'PROCESSOR_ID'.  "Processor ID of the Processor
        lv_p_processor_versions_id = 'PROCESSOR_VERSION_ID'.  "Processor Version of the Processor
        ls_input-raw_document-content   = lv_output.  "File contents in base64-encoded format
        ls_input-raw_document-mime_type = 'MIME_TYPE'.  "MIME Type of the file
    
    * Call API method
        CALL METHOD lo_client->process_processor_versions
          EXPORTING
            iv_p_projects_id           = lv_p_projects_id
            iv_p_locations_id          = lv_p_locations_id
            iv_p_processors_id         = lv_p_processors_id
            iv_p_processor_versions_id = lv_p_processor_versions_id
            is_input                   = ls_input
          IMPORTING
            es_output                  = DATA(ls_output)
            ev_ret_code                = DATA(lv_ret_code)
            ev_err_text                = DATA(lv_err_text)
            es_err_resp                = DATA(ls_err_resp).
        IF /goog/cl_http_client=>is_success( lv_ret_code ).
          MESSAGE 'Success' TYPE 'S'.
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
