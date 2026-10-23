---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-cloud-functions/
title: Invoke Cloud Run functions \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:08.472482+00:00
---

# Invoke Cloud Run functions  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-cloud-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Invoke Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/quickstart-cloud-functions)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-cloud-functions)



This quickstart shows you how to invoke a function that publishes a message constructed from the arguments that the function receives, using the [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview) API.

## Before you begin

Before you run this quickstart, make sure that you or your administrators have completed the following prerequisites:

  * You have a Google Cloud account and project.

  * Billing is enabled for your project. [See how to confirm that billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  * The on-premises or any cloud edition of ABAP SDK for Google Cloud is installed and configured. [See how to install and configure the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).



  * Make sure that the Cloud Run functions API is enabled in your Google Cloud project.

[Go to API library](https://console.cloud.google.com/project/_/apis/library/cloudfunctions.googleapis.com)

  * Depending on the environment where your SAP system is hosted, set up authentication for invoking Cloud Run functions. For instructions, see [Authentication to invoke Cloud Run functions](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-cloud-functions). Configure the client keys as follows:

    * To access the Cloud Run function endpoint, create a client key named `DEMO-CF`.
    * To invoke the Cloud Run function, create a client key named `DEMO-CF-INVOKER`.
  * In the Google Cloud console, write a 2nd gen HTTP function, `cf-gen2-hello-with-args`, that publishes a message using the provided arguments:
        
        exports.helloWorld = (req, res) => {
            let name = req.body.name || req.query.name;
            let full_name = `${req.body.firstname} ${req.body.lastname}`;
            res.status(200).send(`Hello ${name}! Full Name: ${full_name}`);
          };
        

For information about how to write HTTP functions, see [Write Cloud Run functions](https://docs.cloud.google.com/functions/docs/writing).




## Create a program to invoke Cloud Run functions

  1. In the SAP system, create an executable program in your custom namespace (for example, `Z` or `Y`) by using transaction `SE38`.

     1. In the SAP GUI, enter transaction code `SE38`.

     2. In the **Program** field, enter a name of your program. For example, `ZDEMO_CLOUDFUNC_INVOKER`.

     3. Click **Create**.

     4. Specify the program attributes:

        1. In the **Title** field, enter a title of your program, for example, `Invoke Cloud Function using Cloud Function Invoker`.

        2. In the **Type** field, choose `Executable Program`.

        3. Click **Save**.

     5. Save the program as a **Local Object**.

     6. In the **ABAP Editor** , add the following code:
            
            **********************************************************************
            *  Copyright 2024 Google LLC                                         *
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
            REPORT zr_qs_cfinvoker.
            
            DATA(lv_cf_name)  = CONV string( 'cf-gen2-hello-with-args' ).
            DATA(lv_msg)      = CONV string( '{"firstname": "John", "lastname" : "Doe"}' ).
            
            
            TRY.
                " Create a Client API stub for Cloud Functions
                DATA(lo_cloudfunc_client) = NEW /goog/cl_cloudfunc_v2( iv_key_name   = 'DEMO_CF' ).
                " Create a Client API stub for Cloud Function Invoker.
                " Internally this uses the Cloud Function instance to fetch the cloud function HTTP endpoint
                DATA(lo_cfinvoker_client) = NEW /goog/cl_cloudfunc_invoker( iv_key_name   = 'DEMO_CF_INVOKER' ).
            
                " Send additional query parameters as inputs to the cloud function.
                lo_cfinvoker_client->add_common_qparam( iv_name  = 'name'
                                                        iv_value = 'Johnny' ).
            
                lo_cfinvoker_client->invoke(
                  EXPORTING
                    iv_cf_name      = lv_cf_name            "Cloud Function Name
                    iv_cf_location  = 'us-central1'         "Location where the Cloud Function is hosted
                    io_cf_instance  = lo_cloudfunc_client   "Instance of cloud Function Client API Stub
                    iv_body         = lv_msg                "Input payload to the Cloud Function
                    iv_content_type = 'application/json'
                    iv_method       = 'POST'
                  IMPORTING
                    es_output       = DATA(lv_output)
                    ev_ret_code     = DATA(lv_ret_code)
                    ev_err_text     = DATA(lv_err_text)
                    es_err_resp     = DATA(ls_err_resp)
                ).
            
                IF lo_cfinvoker_client->is_success( iv_code = lv_ret_code ).
                  WRITE: / 'HTTP Return Code:', lv_ret_code.
                  WRITE: / 'Response:', lv_output. "Output of cloud function
                ELSE.
                  WRITE: / 'HTTP Return Code:', lv_ret_code.
                  WRITE: / 'Error:', lv_err_text.
                ENDIF.
            
              CATCH /goog/cx_sdk INTO DATA(lo_exp).
                WRITE: / lo_exp->get_text( ).
            ENDTRY.

Replace the following:

     * `DEMO_CF`: name of the client key that is used to access the Cloud Run function endpoint.
     * `DEMO_CF_INVOKER`: name of the client key that is used to invoke the Cloud Run function.
  2. Run your application in `SE38`. If successful, the following output displays:
         
         HTTP Return Code:        200
          Response: Hello Johnny! Full Name: John Doe
         




## What's next

  * Explore other quickstarts available on the GitHub repository, [GoogleCloudPlatform/google-cloud-abap/abap-sdk /ZGOOG_SDK_QUICKSTART/](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_QUICKSTART).
  * Read the guide [Application development with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/developer).
  * View the [code samples](https://docs.cloud.google.com/sap/docs/abap-sdk/samples/all-samples#on-premises-or-any-cloud-edition).
  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
