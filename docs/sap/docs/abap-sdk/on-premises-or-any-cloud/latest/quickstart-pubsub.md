---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-pubsub/
title: Publish messages to Google Cloud Pub/Sub \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:43.488557+00:00
---

# Publish messages to Google Cloud Pub/Sub  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-pubsub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Publish messages to Google Cloud Pub/Sub Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/quickstart-pubsub)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/quickstart-pubsub)



This quickstart shows you how to create a program that publishes a "Hello World!" message to a Pub/Sub topic by using the [Pub/Sub API](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview).

## Before you begin

Before you run this quickstart, make sure that you or your administrators have completed the following prerequisites:

  * You have a Google Cloud account and project.

  * Billing is enabled for your project. [See how to confirm that billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  * The on-premises or any cloud edition of ABAP SDK for Google Cloud is installed and configured. [See how to install and configure the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).



  * Authentication to access Google Cloud APIs is set up. [See how to set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

  * Grant the service account the IAM role `roles/pubsub.publisher`.

  * Make sure the Pub/Sub API is enabled in your Google Cloud project.

[Go to API library](https://console.cloud.google.com/project/_/apis/library/pubsub.googleapis.com)

  * Create a Pub/Sub topic `SAMPLE_TOPIC_01` and add a pull subscription `SAMPLE_SUB_TOPIC_01` to the same. For more information, see [Create a topic](https://docs.cloud.google.com/pubsub/docs/create-topic#create_a_topic) and [Create a subscription](https://docs.cloud.google.com/pubsub/docs/create-subscription#create_subscriptions).




## Create a program to publish messages to Google Cloud

  1. In the SAP system, create an executable program in your custom namespace (for example, Z or Y) by using transaction `SE38`.

     1. In the SAP GUI, enter transaction code `SE38`.

     2. In the **Program** field, enter a name of your program for example, `ZDEMO_PUBSUB`.

     3. Click **Create**.

     4. Specify the program attributes:

        1. In the **Title** field, enter a title of your program, for example, `Publish messages to a Pub/Sub topic`.

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
            
            REPORT zr_qs_publish_messages.
            
            * Data Declaration
            DATA:
              lv_p_projects_id TYPE string,
              lv_p_topics_id   TYPE string,
              ls_input         TYPE /goog/cl_pubsub_v1=>ty_023.
            
            TRY.
            * Instantiate the client stub
                DATA(lo_pubsub) = NEW /goog/cl_pubsub_v1( iv_key_name = 'DEMO_PUBSUB' ).
            
            * Pass the relevant input parameters
                lv_p_topics_id = 'SAMPLE_TOPIC_01'.
                lv_p_projects_id = lo_pubsub->gv_project_id.
                APPEND VALUE #( data = cl_http_utility=>encode_base64( 'Hello World!' ) ) to ls_input-messages.
            
            * Call the API
                CALL METHOD lo_pubsub->publish_topics
                  EXPORTING
                    iv_p_projects_id = lv_p_projects_id
                    iv_p_topics_id   = lv_p_topics_id
                    is_input         = ls_input
                  IMPORTING
                    es_output        = DATA(ls_output)
                    ev_ret_code      = DATA(lv_ret_code)
                    ev_err_text      = DATA(lv_err_text)
                    es_err_resp      = DATA(ls_err_resp).
            
            * Handle the output
                IF lo_pubsub->is_success( lv_ret_code ).
                  MESSAGE 'Message was published!' TYPE 'S'.
                ELSE.
                  MESSAGE 'Message was not published!' TYPE 'E'.
                ENDIF.
            
            * Close the HTTP Connection
                lo_pubsub->close( ).
            
              CATCH /goog/cx_sdk INTO DATA(lo_exception).
                MESSAGE lo_exception->get_text( ) TYPE 'E'.
            ENDTRY.
            

Replace `DEMO_PUBSUB` with the client key name.

  2. Run your application in `SE38`.

  3. To validate the results, follow these steps:

     1. In the Google Cloud console, go to **Pub/Sub**.

     2. Select the subscription `SAMPLE_SUB_TOPIC_01` and go to the **Messages** tab.

     3. Use the PULL feature to check whether the "Hello World!" message has been published to the topic.




## What's next

  * Explore other quickstarts available on the GitHub repository, [GoogleCloudPlatform/google-cloud-abap/abap-sdk /ZGOOG_SDK_QUICKSTART/](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_QUICKSTART).
  * Read the guide [Application development with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/developer).
  * View the [code samples](https://docs.cloud.google.com/sap/docs/abap-sdk/samples/all-samples#on-premises-or-any-cloud-edition).
  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
