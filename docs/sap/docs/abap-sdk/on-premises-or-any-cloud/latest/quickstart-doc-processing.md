---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-doc-processing/
title: Process documents \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:33.030292+00:00
---

# Process documents  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-doc-processing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Process documents Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/quickstart-doc-processing)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-doc-processing)



This quickstart shows you how to process documents (invoices) from a source bucket and store the processed document (JSON file) in a target bucket by using the batch processing capability of [Document AI API](https://docs.cloud.google.com/document-ai/docs/reference/rest).

## Before you begin

Before you run this quickstart, make sure that you or your administrators have completed the following prerequisites:

  * You have a Google Cloud account and project.

  * Billing is enabled for your project. [See how to confirm that billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  * The on-premises or any cloud edition of ABAP SDK for Google Cloud is installed and configured. [See how to install and configure the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).



  * Authentication to access Google Cloud APIs is set up. [See how to set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

  * Make sure the Document AI API is enabled in your Google Cloud project.

[Go to API library](https://console.cloud.google.com/project/_/apis/library/documentai.googleapis.com)

  * In the Document AI Workbench, create a processor with type `INVOICE_PROCESSOR`. For more information, see [Creating and managing processors](https://docs.cloud.google.com/document-ai/docs/create-processor).

  * In Cloud Storage, create a source bucket to store the invoices for processing and place the invoices in this bucket. For more information, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

  * In Cloud Storage, create a target bucket to store the processed files.




## Create a program to process documents

  1. In the SAP system, create an executable program in your custom namespace (for example, Z or Y) by using transaction `SE38`.

     1. In the SAP GUI, enter transaction code `SE38`.

     2. In the **Program** field, enter a name of your program, for example, `ZDEMO_DOCUMENT_AI`.

     3. Click **Create**.

     4. Specify the program attributes:

        1. In the **Title** field, enter a title of your program, for example, `Process invoices`.

        2. In the **Type** field, choose `Executable Program`.

        3. Click **Save**.

     5. Save the program as a **Local Object**.

     6. In the **ABAP Editor** , add the following code:
            
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
            
            REPORT zr_qs_process_documents.
            
            * data declarations
            DATA:
              lv_p_projects_id   TYPE string,
              lv_p_locations_id  TYPE string,
              lv_p_processors_id TYPE string,
              ls_input           TYPE /goog/cl_documentai_v1=>ty_017.
            
            TRY.
            
            * open http connection
                DATA(lo_client) = NEW /goog/cl_documentai_v1( iv_key_name = 'DEMO_DOC_PROCESSING' ).
            
            * populate relevant parameters
                lv_p_projects_id  = 'PROJECT_ID'.
                lv_p_locations_id = 'LOCATION_ID'.
                lv_p_processors_id = 'PROCESSOR_ID'.
                ls_input-input_documents-gcs_prefix-gcs_uri_prefix = 'SOURCE_BUCKET_URI'.
                ls_input-document_output_config-gcs_output_config-gcs_uri = 'TARGET_BUCKET_URI'.
            
            * call api method
                CALL METHOD lo_client->batch_process_processors
                  EXPORTING
                    iv_p_projects_id   = lv_p_projects_id
                    iv_p_locations_id  = lv_p_locations_id
                    iv_p_processors_id = lv_p_processors_id
                    is_input           = ls_input
                  IMPORTING
                    es_output          = DATA(ls_output)
                    ev_ret_code        = DATA(lv_ret_code)
                    ev_err_text        = DATA(lv_err_text)
                    es_err_resp        = DATA(ls_err_resp).
            
                IF lo_client->is_success( lv_ret_code ).
                  MESSAGE 'Success' TYPE 'S'.
                ELSE.
                  MESSAGE lv_err_text TYPE 'E'.
                ENDIF.
            
            * close http connection
                lo_client->close( ).
            
              CATCH /goog/cx_sdk INTO DATA(lo_exception).
                MESSAGE lo_exception->get_text( ) TYPE 'E'.
            ENDTRY.
            

Replace the following:

        * `DEMO_DOC_PROCESSING`: the client key name.
        * `PROJECT_ID`: the ID of the Google Cloud project.
        * `LOCATION_ID`: the processor's location.
        * `PROCESSOR_ID`: the ID of the processor.
        * `SOURCE_BUCKET_URI`: the URI of the Cloud Storage bucket folder where source documents are kept for processing.
        * `TARGET_BUCKET_URI`: the URI of the Cloud Storage bucket where the processed document (JSON file) would be stored.
  2. Run your application in `SE38`.

  3. To validate the results, follow these steps:

     1. In the Google Cloud console, go to Cloud Storage **Buckets** page.

     2. Open the target bucket. The processed document is stored in the form of a JSON file.




## What's next

  * Explore other quickstarts available on the GitHub repository, [GoogleCloudPlatform/google-cloud-abap/abap-sdk /ZGOOG_SDK_QUICKSTART/](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_QUICKSTART).
  * Read the guide [Application development with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/developer).
  * View the [code samples](https://docs.cloud.google.com/sap/docs/abap-sdk/samples/all-samples#on-premises-or-any-cloud-edition).
  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
