---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/quickstart-address-validation/
title: Validate addresses \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:30.113377+00:00
---

# Validate addresses  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/quickstart-address-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Validate addresses Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/quickstart-address-validation)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-address-validation)



This quickstart shows you how to create a program that validates business addresses stored in SAP database by using the [Address Validation API](https://developers.google.com/maps/documentation/address-validation/overview), through the SAP BTP edition of ABAP SDK for Google Cloud.

## Before you begin

Before you run this quickstart, make sure that you or your administrators have completed the following prerequisites:

  * You have a Google Cloud account and project.

  * Billing is enabled for your project. [See how to confirm that billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  * The SAP BTP edition of ABAP SDK for Google Cloud is installed and configured. [See how to install and configure the SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config).

  * Authentication to access Google Cloud APIs is set up. [See how to set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication).

  * You have access to the [SAP BTP, ABAP environment](https://www.sap.com/india/products/technology-platform/abap.html#overview).

  * You have downloaded and installed the latest [ABAP Development Tools (ADT)](https://tools.hana.ondemand.com/#abap) on the latest Eclipse platform.

  * You have created an [ABAP Cloud Project](https://developers.sap.com/tutorials/abap-environment-create-abap-cloud-project.html).



  * Make sure the Address Validation API is enabled in your Google Cloud project.

[Go to API library](https://console.cloud.google.com/project/_/apis/library/addressvalidation.googleapis.com)




## Create an ABAP class to validate addresses

  1. Create a package:

**Note:** If you already have a package, then you can use your existing package. Skip step 1.
     1. In ADT, go to the Project Explorer.
     2. Right-click the package `ZLOCAL`, and select **New > ABAP Package**.
     3. Enter the following details for your package:

        * **Name** : enter `ZABAPSDK_TEST`.
        * **Description** : enter `ABAP SDK Test Package`.
     4. Click **Next**.

     5. In the **Select a Transport Request** dialog, select the **Create a new request** checkbox.

     6. Enter a description for the transport request.

     7. Click **Finish**.

  2. Create an ABAP class to call the Address Validation API:

     1. Right-click your ABAP package and select **New > ABAP Class**.
     2. Enter the following details for your ABAP class:

        * **Name** : enter `ZGOOG_CL_QS_ADDRESS_VALIDATION`.
        * **Description** : enter `Quick start for Address Validation API`.
     3. Click **Next**.

     4. Select a transport request and click **Finish**.

  3. In the code editor, replace the default code with the following code snippet:
         
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
         CLASS zcl_qs_validate_address DEFINITION
           PUBLIC FINAL
           CREATE PUBLIC.
         
           PUBLIC SECTION.
             INTERFACES if_oo_adt_classrun.
         ENDCLASS.
         
         
         
         CLASS ZCL_QS_VALIDATE_ADDRESS IMPLEMENTATION.
         
         
           METHOD if_oo_adt_classrun~main.
         
             DATA ls_input             TYPE /goog/cl_addrvaldn_v1=>ty_012.
             DATA lo_address_validator TYPE REF TO /goog/cl_addrvaldn_v1.
         
             TRY.
                 " Open HTTP connection
                 " The client key DEMO_ADDR_VAL is an example, replace this with actual value
                 lo_address_validator = NEW #( iv_key_name = 'DEMO_ADDR_VAL' ).
         
                 " Pass the address to be validated
                 ls_input-address-region_code = 'US'.
                 ls_input-address-locality    = 'Mountain View'.
                 APPEND '1600, Amphitheatre, Parkway' TO ls_input-address-address_lines.
         
                 " Call the API Method to validate address
                 lo_address_validator->validate_address( EXPORTING is_input    = ls_input
                                                         IMPORTING es_output   = DATA(ls_output)
                                                                   ev_ret_code = DATA(lv_ret_code)
                                                                   ev_err_text = DATA(lv_err_text)
                                                                   es_err_resp = DATA(ls_err_resp) ).
         
                 IF     lo_address_validator->is_success( lv_ret_code ) = abap_true
                    AND ls_output-result-verdict-address_complete       = abap_true.
                   out->write( 'Address is complete' ).
                 ENDIF.
         
               CATCH /goog/cx_sdk INTO DATA(lo_exception).
                 " Handle exception here
             ENDTRY.
           ENDMETHOD.
         ENDCLASS.
         

Replace `DEMO_ADDR_VAL` with the client key name.

  4. Save and activate the changes.

  5. Run your application:

     1. Select the ABAP class `ZGOOG_CL_QS_ADDRESS_VALIDATION`.
     2. Click **Run > Run As > ABAP Application (Console)**. Alternatively, press `F9`. If successful, the following output displays: 
            
            'Address is complete'
            




## What's next

  * Read the guide [Application development with the SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer).
  * View the [code samples](https://docs.cloud.google.com/sap/docs/abap-sdk/samples/all-samples#sap-btp-edition).
  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
