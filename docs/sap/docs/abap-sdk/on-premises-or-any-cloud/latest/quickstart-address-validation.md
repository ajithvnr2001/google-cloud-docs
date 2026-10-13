---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-address-validation/
title: Validate address \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:33.418337+00:00
---

# Validate address  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-address-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Validate address Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/quickstart-address-validation)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-address-validation)



This quickstart shows you how to create a program that validates an address by using the [Address Validation API](https://developers.google.com/maps/documentation/address-validation/overview).

## Before you begin

Before you run this quickstart, make sure that you or your administrators have completed the following prerequisites:

  * You have a Google Cloud account and project.

  * Billing is enabled for your project. [See how to confirm that billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  * The on-premises or any cloud edition of ABAP SDK for Google Cloud is installed and configured. [See how to install and configure the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).



  * Authentication to access Google Cloud APIs is set up. [See how to set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

  * Make sure the Address Validation API is enabled in your Google Cloud project.

[Go to API library](https://console.cloud.google.com/project/_/apis/library/addressvalidation.googleapis.com)




## Create a program to validate addresses

  1. In the SAP system, create an executable program in your custom namespace (for example, Z or Y) by using transaction `SE38`.

     1. In the SAP GUI, enter transaction code `SE38`.

     2. In the **Program** field, enter a name of your program, for example, `ZDEMO_ADDRESS_VALIDATION`.

     3. Click **Create**.

     4. Specify the program attributes:

        1. In the **Title** field, enter a title of your program, for example, `Validate an address`.

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
            
            REPORT zr_qs_validate_address.
            
            * data declarations
            DATA: lv_ret_code          TYPE i,
                  lv_err_text          TYPE string,
                  ls_input             TYPE /goog/cl_addrvaldn_v1=>ty_012,
                  ls_output            TYPE /goog/cl_addrvaldn_v1=>ty_013,
                  ls_err_resp          TYPE /goog/err_resp,
                  lo_exception         TYPE REF TO /goog/cx_sdk,
                  lo_address_validator TYPE REF TO /goog/cl_addrvaldn_v1.
            
            * instantiate api client stub
            TRY.
                CREATE OBJECT lo_address_validator
                  EXPORTING
                    iv_key_name = 'DEMO_ADDR_VAL'.
            
            * pass the address to be validated
                ls_input-address-region_code = 'US'.
                ls_input-address-locality = 'Mountain View'.
                APPEND '1600, Amphitheatre, Parkway' TO ls_input-address-address_lines.
            
            * call the api method to validate address
                CALL METHOD lo_address_validator->validate_address
                  EXPORTING
                    is_input    = ls_input
                  IMPORTING
                    es_output   = ls_output
                    ev_ret_code = lv_ret_code
                    ev_err_text = lv_err_text
                    es_err_resp = ls_err_resp.
                IF lo_address_validator->is_success( lv_ret_code ) = abap_true AND
                  ls_output-result-verdict-address_complete = abap_true.
                  WRITE: / 'Address is complete'.
                ENDIF.
            
              CATCH /goog/cx_sdk INTO lo_exception.
            * write code here to handle exceptions
            ENDTRY.
            

Replace `DEMO_ADDR_VAL` with the client key name.

  2. Run your application in `SE38`. If successful, the following output displays: 
         
         'Address is complete'
         




## What's next

  * Explore other quickstarts available on the GitHub repository, [GoogleCloudPlatform/google-cloud-abap/abap-sdk /ZGOOG_SDK_QUICKSTART/](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_QUICKSTART).
  * Read the guide [Application development with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/developer).
  * View the [code samples](https://docs.cloud.google.com/sap/docs/abap-sdk/samples/all-samples#on-premises-or-any-cloud-edition).
  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
