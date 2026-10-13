---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/quick-prototyping-with-gemini/
title: Quick prototyping with Gemini \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:36.143290+00:00
---

# Quick prototyping with Gemini  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/quick-prototyping-with-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Quick prototyping with Gemini Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/quick-prototyping-with-gemini)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/quick-prototyping-with-gemini)



Google's [Generative Language API](https://ai.google.dev/api/all-methods#generative-language-api) enables seamless prototyping using the Gemini models. It lets you test and explore the capabilities of Gemini models without needing to set up complex infrastructure or manage model deployment. Google's browser based prototyping tool [Google AI Studio](https://ai.google.dev/aistudio) uses the Generative Language API to enable browser-based prototyping with generative models.

With Agent Platform SDK for ABAP, you can use the Generative Language API—Gemini API to start your prototyping journey, directly from within your ABAP environment. You need an API key generated from Google AI Studio to access the Gemini models. You need to generate this API key only once.

## Generate an API key

The API key that you generate from Google AI Studio provides a convenient way to authenticate to the Gemini API.

To generate an API key, perform the following steps:

  1. In Google AI Studio, open the **API keys** page.

[Get an API key](https://aistudio.google.com/app/apikey)

  2. Click **Create API key**.

  3. If populated, then read and acknowledge the legal notice, and then click **Continue**.

  4. If populated, then read and acknowledge the safety setting reminder.

  5. In the **Create API key** dialog, select one of the following options, as appropriate:

     * **Create API key in new project**
     * **Create API key in existing project**
  6. Copy your key string and keep it secure. You need this API key to configure authentication to the Gemini API.

  7. Copy the project number of the Google Cloud project where the API key is generated. You need this in a later step.




## Set up authentication

To authenticate to Gemini API by using an API key, use one of the following methods:

  * Authenticate by using an API key through a custom authentication class
  * [Authenticate by using an API key stored in Secret Manager](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication#auth_scm_use_apikey)



### Authenticate by using an API key through a custom authentication class

You can create a custom authentication class to keep your API key and configure a client key with the custom authentication class.

  1. In your SAP BTP, ABAP environment, create a new class by inheriting the `/GOOG/CL_AUTH_BASE` class that is shipped with the ABAP SDK for Google Cloud:

     1. In the Eclipse platform, right-click the package where you want to create a class, and then click **New > ABAP Class**.
     2. In the **Name** field, enter `ZCL_TEST_GEMINI_API`.
     3. In the **Description** field, enter `Authentication Class for testing Gemini API`.
     4. In the **Superclass** field, enter `/GOOG/CL_AUTH_BASE`.
     5. Click **Next**.
     6. Select a **Transport Request** or create a new one.
     7. Click **Finish**.
     8. In the editor, replace the existing code with the following code:
            
            CLASS zcl_test_gemini_api DEFINITION
                PUBLIC
                INHERITING FROM /goog/cl_auth_base FINAL
                CREATE PUBLIC.
                PUBLIC SECTION.
                    CONSTANTS: BEGIN OF c_com_scn_sdk,
                                            wif     TYPE /goog/comm_scenario VALUE '/GOOG/COM_SDK_WIF',
                                            apik_sm TYPE /goog/comm_scenario VALUE '/GOOG/COM_SDK_APIKSM',
                                            END OF c_com_scn_sdk.
                    METHODS get_access_token REDEFINITION.
            PROTECTED SECTION.
            PRIVATE SECTION.
            ENDCLASS.
            CLASS zcl_test_gemini_api IMPLEMENTATION.
                METHOD get_access_token.
                    ev_auth_type = CONV #( apikey_sm ).
                    ev_token = API_KEY.
                ENDMETHOD.
            ENDCLASS.
            

Replace `API_KEY` with the API key that you generated in Google AI Studio.

**Note:** Remember to use your API keys securely. Don't share them or embed them in code the public can view. To learn about the best practices for securing your API key, see [Keep your API key secure](https://ai.google.dev/gemini-api/docs/api-key#security).
     9. Activate your `Z` class.

     10. Go to the properties of this class, go to the **API State** tab, and then release the API with the contract state `C1`.

For more information about API state, see [Releasing Development Objects](https://help.sap.com/docs/abap-cloud/abap-development-tools-user-guide/setting-api-release-state).

  2. Access the SAP Fiori launchpad of the BTP ABAP system where the ABAP SDK for Google Cloud is installed.

  3. Access the **Google SDK: Main Configuration** app, and then perform the following steps:

     1. Click **Create**.
     2. In the **Create new entry** dialog, enter values for the following fields:

Field | Description  
---|---  
**Google Cloud Key Name** | Specify a name of the client key configuration, such as `GEMINI_QUICK_TEST`.  
**Google Cloud Service Account Name** | Leave this field blank.  
**Google Cloud Scope** | Leave this field blank.  
**Google Cloud Project Identifier** | Specify the project ID of the Google Cloud project where you created the API key.  
**Google Cloud Project Number** | Specify the project number of the Google Cloud project where you created the API key.  
**Authentication Type** | Select `Z`.  
**Authentication Class** | Select the `ZCL_TEST_GEMINI_API` class that you created in a previous step.  
     3. Save the new entry.

  4. Make a note of the client key. You use this client key for authentication.




## Run sample code

You can explore the Gemini API capabilities by running the following sample code:

  1. In the Eclipse platform, right-click the package where you want to create a class, and then click **New > ABAP Class**.

  2. In the **Name** field, enter `ZCL_INVOKE_LLM`.

  3. In the **Description** field, enter `Sample class for testing Gemini API`.

  4. Click **Next**.

  5. Select a transport request or create a new one.

  6. Click **Finish**.

  7. In the editor, replace the existing code with the following code:
         
         CLASS zcl_invoke_llm DEFINITION
         PUBLIC FINAL
         CREATE PUBLIC.
         PUBLIC SECTION.
             INTERFACES if_oo_adt_classrun.
         ENDCLASS.
         CLASS zcl_invoke_llm IMPLEMENTATION.
         METHOD if_oo_adt_classrun~main.
             DATA lv_sys_instruction TYPE string.
             DATA lv_client_key      TYPE /goog/keyname.
             DATA lv_model_id        TYPE string.
             DATA lv_max_tokens      TYPE int4.
             DATA lv_resp_mime_type  TYPE string.
             DATA lv_prompt          TYPE string.
             DATA lv_temperature     TYPE /goog/num_float.
             DATA lv_top_k           TYPE int4.
             DATA lv_top_p           TYPE /goog/num_float.
             DATA ls_input           TYPE /goog/cl_generativelang_v1beta=>ty_045.
             DATA ls_output          TYPE /goog/cl_generativelang_v1beta=>ty_046.
             DATA ls_part            TYPE /goog/cl_generativelang_v1beta=>ty_068.
             DATA lt_parts           TYPE /goog/cl_generativelang_v1beta=>ty_t_068.
             DATA ls_content         TYPE /goog/cl_generativelang_v1beta=>ty_018.
             DATA lv_msg             TYPE string.
             DATA ls_raw             TYPE string.
             DATA lv_err_msg         TYPE string.
             DATA lo_cx_sdk          TYPE REF TO /goog/cx_sdk.
         
             " TODO Developer: Set values for Mandatory Fields
             lv_model_id = 'gemini-2.5-flash'.  " You can also change the Model ID of your choosing
             lv_client_key = 'GEMINI_QUICK_TEST'.    " Client key configured
         
             " TODO Developer: Set values for Optional Fields, if required
             " lv_temperature =
             " lv_top_k =
             " lv_top_p =
             " lv_max_tokens =
         
             " TODO Developer: (Optional) Set the System Instruction
                 lv_sys_instruction  = 'You are an Italian Chef in a 5 Star Restaurant'.
         
             " TODO Developer: (Mandatory) Set the Prompt
                 lv_prompt = 'Give me a recipe to make Margarita Pizza'.
             IF lv_temperature IS NOT INITIAL.
                 ls_input-generation_config-temperature = lv_temperature.
             ENDIF.
             IF lv_top_k IS NOT INITIAL.
                 ls_input-generation_config-top_k = lv_top_k.
             ENDIF.
             IF lv_top_p IS NOT INITIAL.
                 ls_input-generation_config-top_p = lv_top_p.
             ENDIF.
             IF lv_max_tokens IS NOT INITIAL.
                 ls_input-generation_config-max_output_tokens = lv_max_tokens.
             ENDIF.
             IF lv_sys_instruction IS NOT INITIAL.
                 ls_input-system_instruction-role = 'system'.
                 ls_part-text = lv_sys_instruction.
                 APPEND ls_part TO ls_input-system_instruction-parts.
                 CLEAR ls_part.
             ENDIF.
             ls_content-role = 'user'.
             IF lv_prompt IS NOT INITIAL.
                 ls_part-text = lv_prompt.
                 APPEND ls_part TO ls_content-parts.
                 CLEAR ls_part.
             ENDIF.
             APPEND ls_content TO ls_input-contents.
             CLEAR ls_content.
             TRY.
                     DATA(lo_llm_invoker) = NEW /goog/cl_generativelang_v1beta( iv_key_name = lv_client_key ).
                 CATCH /goog/cx_sdk INTO lo_cx_sdk.
                     lv_err_msg = lo_cx_sdk->get_text( ).
         out->write( |Exception occurred, reason: { lv_err_msg }| ).
             ENDTRY.
             TRY.
                     lo_llm_invoker->generate_content_models( EXPORTING iv_p_models_id = lv_model_id
                                                                                                                             is_input       = ls_input
                                                                                                         IMPORTING es_raw         = ls_raw
                                                                                                                             es_output      = ls_output
                                                                                                                             ev_ret_code    = DATA(lv_ret_code)
                                                                                                                             ev_err_text    = DATA(lv_err_text)
                                                                                                                             es_err_resp    = DATA(ls_err_resp) ).
                 CATCH /goog/cx_sdk INTO lo_cx_sdk.
                     lv_err_msg = lo_cx_sdk->get_text( ).
                     out->write( |Exception occurred, reason: { lv_err_msg }| ).
                     RETURN.
             ENDTRY.
             IF lo_llm_invoker->is_success( lv_ret_code ) = abap_true.
                 ASSIGN ls_output-candidates[ 1 ] TO FIELD-SYMBOL(<ls_candidate>).
                 IF sy-subrc = 0.
                     lt_parts = <ls_candidate>-content-parts.
                     ASSIGN lt_parts[ 1 ] TO FIELD-SYMBOL(<ls_part>).
                     IF sy-subrc = 0.
                         DATA(lv_response) = <ls_part>-text.
                         out->write( lv_response ).
                     ELSE.
                         out->write( |Model stopped generating response due to finish reason: { <ls_candidate>-finish_reason }| ).
                         out->write( |Read more about finish reason in the below link:| ).
                         out->write( |https://cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/GenerateContentResponse#FinishReason| ).
                     ENDIF.
                 ENDIF.
             ELSE.
                 out->write( |Error occurred, reason: { lv_ret_code }:{ lv_err_text }| ).
             ENDIF.
         ENDMETHOD.
         ENDCLASS.
         

  8. Activate your class.

  9. Run the ABAP code.




## Prototype AI use cases using ABAP

You can build prototype SAP applications using the `/GOOG/CL_GENERATIVELANGUAGE_V1` and `/GOOG/CL_GENERATIVELANG_V1BETA` classes shipped with the SDK. You can invoke these classes from your ABAP environment using the client Key that you've created in the Set up authentication section.

## What's next

  * Learn how to [install and configure the Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap).
  * Learn about [Generative AI on Agent Platform for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/vertex-ai-for-sap-overview).
  * Ask your questions and discuss the Agent Platform SDK for ABAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
