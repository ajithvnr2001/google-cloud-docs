---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/samples/sm-create-secret/
title: Create secret \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:51.974051+00:00
---

# Create secret  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/samples/sm-create-secret/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Samples ](https://docs.cloud.google.com/sap/docs/abap-sdk/samples/all-samples)



Send feedback 

#  Create secret Stay organized with collections  Save and categorize content based on your preferences. 

To securely store sensitive SAP data, such as API keys and passwords, you can create secrets in Secret Manager by using the ABAP SDK for Google Cloud. Integrating with Secret Manager helps protect sensitive data and maintain compliance across your SAP systems. This code sample shows how to create a secret by using both the SAP BTP and on-premises or any cloud editions of the SDK.

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
    CLASS zcl_cs_create_secret DEFINITION
      PUBLIC FINAL
      CREATE PUBLIC.
    
      PUBLIC SECTION.
        INTERFACES if_oo_adt_classrun.
    ENDCLASS.
    
    
    CLASS zcl_cs_create_secret IMPLEMENTATION.
      METHOD if_oo_adt_classrun~main.
        " Data declarations
        DATA lv_q_secretid    TYPE string.
        DATA lv_p_projects_id TYPE string.
        DATA ls_input         TYPE /goog/cl_secretmgr_v1=>ty_025.
        DATA lt_replicas      TYPE /goog/cl_secretmgr_v1=>ty_t_020.
        DATA ls_replicas      TYPE /goog/cl_secretmgr_v1=>ty_020.
    
        TRY.
    
            " Open HTTP Connection
            " Pass the configured client key
            DATA(lo_secretmgr) = NEW /goog/cl_secretmgr_v1( iv_key_name = 'SECRETMGR_DEMO' ).
    
            " Derive project id from the object
            lv_p_projects_id = lo_secretmgr->gv_project_id.
    
            "   Populate inputs to be passed to the API
            lv_q_secretid = 'Secret_001'.
            " Set a location id, 'us-central1' is used as example
            ls_replicas-location = 'us-central1'.
            INSERT ls_replicas INTO TABLE lt_replicas.
            ls_input-replication-user_managed-replicas = lt_replicas.
    
            " Call API method
            lo_secretmgr->create_secrets( EXPORTING iv_q_secretid    = lv_q_secretid
                                                    iv_p_projects_id = lv_p_projects_id
                                                    is_input         = ls_input
                                          IMPORTING es_output        = DATA(ls_output)
                                                    ev_ret_code      = DATA(lv_ret_code)
                                                    ev_err_text      = DATA(lv_err_text)
                                                    es_err_resp      = DATA(ls_err_resp) ).
            IF /goog/cl_http_client=>is_success( lv_ret_code ).
              out->write( | Secret: { lv_q_secretid } created successfully | ).
            ELSE.
    
              out->write( | Error occurred: { lv_err_text }| ).
    
            ENDIF.
    
            " Close HTTP Connection
            lo_secretmgr->close( ).
    
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
    
    REPORT zr_create_secret.
    
    * Data declarations
    DATA: lv_q_secretid    TYPE string,
          lv_p_projects_id TYPE string,
          ls_input         TYPE /goog/cl_secretmgr_v1=>ty_025,
          lt_replicas      TYPE /goog/cl_secretmgr_v1=>ty_t_020,
          ls_replicas      TYPE /goog/cl_secretmgr_v1=>ty_020.
    
    TRY.
    
    *     Open HTTP Connection
        DATA(lo_sm) = NEW /goog/cl_secretmgr_v1( iv_key_name = 'DEMO_SM' ).
    
    *     Populate inputs to be passed to the API
        lv_q_secretid    = 'Secret_001'.
        lv_p_projects_id = lo_sm->gv_project_id.
    
    *     Location id 'us-central1' is used as an example
        ls_replicas-location = 'us-central1'.
        INSERT ls_replicas INTO TABLE lt_replicas.
        ls_input-replication-user_managed-replicas = lt_replicas.
    
    *     Call API method
        CALL METHOD lo_sm->create_secrets
          EXPORTING
            iv_q_secretid    = lv_q_secretid
            iv_p_projects_id = lv_p_projects_id
            is_input         = ls_input
          IMPORTING
            es_output        = DATA(ls_output)
            ev_ret_code      = DATA(lv_ret_code)
            ev_err_text      = DATA(lv_err_text)
            es_err_resp      = DATA(ls_err_resp).
    
        IF /goog/cl_http_client=>is_success( lv_ret_code ).
          MESSAGE 'Secret created successfully' TYPE 'S'.
        ELSE.
          MESSAGE lv_err_text TYPE 'E'.
        ENDIF.
    
    *     Close HTTP Connection
        lo_sm->close( ).
    
      CATCH /goog/cx_sdk INTO DATA(lo_exception).
        MESSAGE lo_exception->get_text( ) TYPE 'E'.
    ENDTRY.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
