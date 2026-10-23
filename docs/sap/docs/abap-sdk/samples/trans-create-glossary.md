---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/samples/trans-create-glossary/
title: Create glossary \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:43.754590+00:00
---

# Create glossary  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/samples/trans-create-glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Samples ](https://docs.cloud.google.com/sap/docs/abap-sdk/samples/all-samples)



Send feedback 

#  Create glossary Stay organized with collections  Save and categorize content based on your preferences. 

This code sample can be used to create a glossary by using Google Cloud Cloud Translation API (v3).

A _glossary_ is a custom dictionary that the Cloud Translation API (v3) uses to consistently translate business's domain-specific terminology.

Make sure a glossary file is prepared and uploaded to a Cloud Storage bucket in the same Google Cloud project. For more information about preparing a glossary file, see [Creating and using glossaries (Advanced)](https://docs.cloud.google.com/translate/docs/advanced/glossary).

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
    CLASS zcl_cs_create_glossary DEFINITION
      PUBLIC FINAL
      CREATE PUBLIC.
    
      PUBLIC SECTION.
        INTERFACES if_oo_adt_classrun.
    ENDCLASS.
    
    
    
    CLASS ZCL_CS_CREATE_GLOSSARY IMPLEMENTATION.
    
    
      METHOD if_oo_adt_classrun~main.
        "Data decalarations
        DATA lv_p_projects_id  TYPE string.
        DATA lv_p_locations_id TYPE string.
        DATA ls_input          TYPE /goog/cl_translation_v3=>ty_022.
    
        TRY.
            " Open HTTP Connection
            " Pass the configured client key, TRANSLATE_DEMO is used as example, replace it with actual value
            DATA(lo_translate) = NEW /goog/cl_translation_v3( iv_key_name = 'TRANSLATE_DEMO' ).
    
            " Derive project id from the object
            lv_p_projects_id  = lo_translate->gv_project_id.
    
            " Set a location id, 'us-central1' is used as example, replace it with actual value
            lv_p_locations_id = 'us-central1'.
    
            " Pass a display name. The value passed below is an example, replace it with actual value
            ls_input-display_name = 'Finance Term Glossary EN to ES'.
    
            " Source language in BCP-47 format. The value passed below is an example, replace it with actual value
            ls_input-language_pair-source_language_code = 'en-US'.
    
            " Target language in BCP-47 format. The value passed below is an example, replace it with actual value
            ls_input-language_pair-target_language_code = 'es-ES'.
    
            " Complete name of glossary has following format:
            " projects/<PROJECT_ID>/locations/<LOCATION_ID>/glossaries/<GLOSSARY_ID>
            " The value used for GLOSSARY ID is an example, replace it with actual value.
            CONCATENATE 'projects/'
                         lo_translate->gv_project_id
                         '/locations/us-central1/glossaries/'
                         'FI_GLOSSARY_EN_ES'
                        INTO ls_input-name.
    
           " TODO: Pass the complete path of glossary file which is stored in GCS bucket
           " ls_input-input_config-gcs_source-input_uri =
    
            " Call API method
            lo_translate->create_glossaries( EXPORTING iv_p_projects_id  = lv_p_projects_id
                                                       iv_p_locations_id = lv_p_locations_id
                                                       is_input          = ls_input
                                             IMPORTING es_output         = DATA(ls_output)
                                                       ev_ret_code       = DATA(lv_ret_code)
                                                       ev_err_text       = DATA(lv_err_text)
                                                       es_err_resp       = DATA(ls_err_resp) ).
            IF /goog/cl_http_client=>is_success( lv_ret_code ).
              " This returns a long running operation id as glossary creation is adhoc
              " You can use the LRO ID to poll to check the status of the operation (SUCCESS Or FAILURE)
              out->write( | LRO ID:{ ls_output-name }| ).
            ELSE.
    
              out->write( | Error occurred: { lv_err_text }| ).
    
            ENDIF.
    
            " Close HTTP Connection
            lo_translate->close( ).
    
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
    
    REPORT zr_create_glossaries.
    
    "Data declarations
    DATA: lv_p_projects_id  TYPE string,
          lv_p_locations_id TYPE string,
          ls_input          TYPE /goog/cl_translation_v3=>ty_022.
    
    TRY.
    
        "Open HTTP Connection
        "Pass the configured client key - TRANSLATE_DEMO is used an example, replace it with actual value.
        DATA(lo_translate) = NEW /goog/cl_translation_v3( iv_key_name = 'TRANSLATE_DEMO' ).
    
        "Populate required parameters
        "Derive project id from the object
        lv_p_projects_id  = lo_translate->gv_project_id.
    
        "Set a location id, 'us-central1' is used as example, replace it with actual value.
        lv_p_locations_id = 'us-central1'.
    
        "Pass a display name, the value passed below is an example, replace it with actual value
        ls_input-display_name = 'Finance Term Glossary EN to ES'.
    
        "Source language in BCP-47 format. The value passed below is an example, replace it with actual value
        ls_input-language_pair-source_language_code = 'en-US'.
    
        "Target language in BCP-47 format. The value passed below is an example, replace it with actual value
        ls_input-language_pair-target_language_code = 'es-ES'.
    
        "Complete name of glossary has following format:
        "projects/<PROJECT_ID>/locations/<LOCATION_ID>/glossaries/<GLOSSARY_ID>
        "The value used for GLOSSARY ID is an exmaple, replace it with actual value
        CONCATENATE 'projects/'
                     lo_translate->gv_project_id
                     '/locations/us-central1/glossaries/'
                     'FI_GLOSSARY_EN_ES'
                     INTO ls_input-name.
    
        "TODO: Pass the complete path of glossary file which is stored in GCS bucket
        "ls_input-input_config-gcs_source-input_uri =
    
        "Call API method
        CALL METHOD lo_translate->create_glossaries
          EXPORTING
            iv_p_projects_id  = lv_p_projects_id
            iv_p_locations_id = lv_p_locations_id
            is_input          = ls_input
          IMPORTING
            es_output         = DATA(ls_output)
            ev_ret_code       = DATA(lv_ret_code)
            ev_err_text       = DATA(lv_err_text)
            es_err_resp       = DATA(ls_err_resp).
        IF /goog/cl_http_client=>is_success( lv_ret_code ).
          "This returns a long running operation id for the job that is scheduled for glossary creation
          "You can use the LRO ID to poll and check the status of the operation
          WRITE: 'LRO ID:', ls_output-name.
        ELSE.
          MESSAGE lv_err_text TYPE 'E'.
        ENDIF.
    
        "Close HTTP Connection
        lo_translate->close( ).
    
      CATCH /goog/cx_sdk INTO DATA(lo_exception).
        MESSAGE lo_exception->get_text( ) TYPE 'E'.
    ENDTRY.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
