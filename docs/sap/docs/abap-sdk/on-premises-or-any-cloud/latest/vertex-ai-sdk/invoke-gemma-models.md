---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemma-models/
title: Invoke the Gemma models \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:28.737115+00:00
---

# Invoke the Gemma models  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemma-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Invoke the Gemma models Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/invoke-gemma-models)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemma-models)



This document describes how to invoke the [Gemma models](https://ai.google.dev/gemma/docs) to generate responses for text and multimodal input, by using the Agent Platform SDK for ABAP. The SDK supports interacting with Gemma models in three ways: deployed on Agent Platform, deployed on Cloud Run, or accessed directly through Gemini API.

Gemma is a family of lightweight, state-of-the-art open models from Google. You can use Gemma models for diverse use cases, including generating creative text, summarizing information, answering questions, interpreting images, and automating tasks through function calling. The ABAP SDK for Google Cloud provides the necessary classes and methods to access Gemma models from your ABAP applications.

## Before you begin

Before using the Agent Platform SDK for ABAP with the Gemma models, make sure that you or your administrators have completed the following prerequisites:

  * [Enabled the Agent Platform API](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * If you want to use Gemma on Agent Platform, then [deployed Gemma models in Agent Platform](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#deploy-gemma-model) in your Google Cloud project.
  * If you want to use Gemma on Cloud Run, then [enabled the Gemini API and Cloud Run API](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * If you want to use Gemma with the Gemini API, then [enabled the Gemini API](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * [Installed](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#installation) the Agent Platform SDK for ABAP in your SAP environment.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#authentication) to access the required APIs.
  * [Configured the model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#gemma).



### Choose how to run Gemma

To use Gemma models with the SDK, you've three options. You can deploy them to an endpoint on Agent Platform or Cloud Run, you can use the hosted Gemma models on the Gemini API.

#### Agent Platform

Deploy your model to [Agent Platform](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-gemma) and note the project number, region, and endpoint ID. You use this information when you instantiate the `/GOOG/CL_GEMMA_ON_VERTEXAI` class in your ABAP code.

To find the required information, do the following:

  1. Deploy your Gemma model through the Agent Platform Model Garden. For more information, see [Use Gemma open models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-gemma).

  2. In the Google Cloud console, go to **Model Garden > Endpoints**.

  3. Select your deployed model's endpoint.

  4. Note the project number, region, and endpoint ID.




#### Cloud Run

Deploy your model to [Cloud Run](https://ai.google.dev/gemma/docs/core/deploy_to_cloud_run_from_ai_studio) and note the URL of the Cloud Run service.

To find required URL, do the following:

  1. Deploy your Gemma model to Cloud Run. For more information, see [Run Gemma 3 on Cloud Run](https://docs.cloud.google.com/run/docs/run-gemma-on-cloud-run).

  2. In the Google Cloud console, navigate to Cloud Run.

  3. Select your deployed model's endpoint.

  4. On the **Service details** page, note the service URL.




#### Gemini API

No deployment is needed. The Gemini API provides hosted access to Gemma models.

### Create RFC destinations

If you run Gemma through the Gemini API, then you don't need an RFC destination. You can skip this section.

If you deploy your Gemma to an endpoint on Agent Platform or Cloud Run, then create an RFC connection.

To create an RFC destination, do the following:

  1. Create an RFC destination for the endpoint depending on where the Gemma is deployed.

     1. In the SAP GUI, enter transaction code `SM59`.
     2. Create an RFC destination of type `G - HTTP connection to External Server`.

        * For Gemma on Agent Platform, enter the following details:
Field | Value  
---|---  
**RFC Destination** | Name of the RFC destination, such as `GOOG_VERTEXAI_GEMMA`  
**Target Host** | Dedicated endpoint in the format: `ENDPOINT_ID.REGION-PROJECT_NUMBER.prediction.vertexai.goog`.  
**Service No.** | The port no., `443`.  
**Path Prefix** | Leave this field blank.  
        * For Gemma on Cloud Run, enter the following details:
Field | Value  
---|---  
**RFC Destination** | Name of the RFC destination, such as `GOOG_GENLANG_GEMMA`.  
**Target Host** | URL of the Cloud Run service.  
**Service No.** | The port no., `443`.  
**Path Prefix** | Leave this field blank.  
     3. Go to the **Logon & Security** tab and activate SSL.

For information about creating RFC destinations, see [RFC destinations](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#create_rfc_destinations).

  2. Configure the service mapping:

     1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`. 

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

     2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Service Map**.
     3. Create new entries in the `/GOOG/SERVIC_MAP` table to link the Google service name to the RFC destination.

        * For Gemma on Agent Platform: Field | Value  
---|---  
**Google Cloud Key Name** | Name of the client key, such as `GEMMA_VERTEXTAI`. You use the name of the client key that you create as part of the [set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#authentication).  
**Google Service Name** | `aiplatform:v1`  
**RFC Destination** | Name of the RFC destination, such as `GOOG_VERTEXAI_GEMMA`.  
        * For Gemma on Cloud Run: Field | Value  
---|---  
**Google Cloud Key Name** | Name of the client key, such as `GEMMA_CLOUDRUN`. You use the name of the client key that you create as part of the [set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#authentication).  
**Google Service Name** | `generativelanguage:v1beta`  
**RFC Destination** | Name of the RFC destination, such as `GOOG_GENLANG_GEMMA`.  
  3. Go to **ABAP SDK for Google Cloud > Utilities > Validate Authentication Configuration** and validate your configuration.




After completing these steps, use the `/GOOG/CL_GEMMA_ON_VERTEXAI` or `/GOOG/CL_GEMMA_ON_CLOUDRUN` classes in your ABAP programs.

## Send requests to Gemma

This section explains how to send requests to Gemma models by using the Agent Platform SDK for ABAP.

### Instantiate the Gemma model class

Depending on the platform where you deploy your Gemma model, you use a different SDK class to call the model:

  * Agent Platform
  * Cloud Run or Gemini API



#### Agent Platform

For Gemma models deployed on Agent Platform, you use the class `/GOOG/CL_GEMMA_ON_VERTEXAI`.
    
    
      TRY.
          DATA(lo_model) = NEW /goog/cl_gemma_on_vertexai(
            iv_model_key   = 'MODEL_KEY'
            iv_project_id  = 'PROJECT_NUMBER'
            iv_location_id = 'REGION'
            iv_endpoint_id = 'VERTEX_ENDPOINT_ID'
          ).
        CATCH /goog/cx_sdk INTO DATA(lo_exception).
          cl_demo_output=>display( lo_exception->get_text( ) ).
          RETURN.
      ENDTRY.
    

#### Cloud Run or Gemini API

For Gemma models accessed through Cloud Run or Gemini API, you use the class `/GOOG/CL_GEMMA_ON_CLOUDRUN`.
    
    
      TRY.
          DATA(lo_model) = NEW /goog/cl_gemma_on_cloudrun(
            iv_model_key = 'MODEL_KEY'
          ).
        CATCH /goog/cx_sdk INTO DATA(lo_exception).
          cl_demo_output=>display( lo_exception->get_text( ) ).
          RETURN.
      ENDTRY.
    

Replace the following:

  * `MODEL_KEY`: The model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
  * `PROJECT_NUMBER`: Your Google Cloud project number where the Gemma model is deployed.
  * `REGION`: The Google Cloud region where your Agent Platform endpoint is deployed.
  * `VERTEX_ENDPOINT_ID`: The ID of the Agent Platform endpoint to which your Gemma model is deployed.



### Generate content with a prompt

To generate content by providing a text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design) to the model, you can use the `GENERATE_CONTENT` method.
    
    
    TRY.
        DATA(lo_response) = lo_model->generate_content( iv_prompt_text = 'PROMPT' ).
        IF lo_response IS BOUND.
          cl_demo_output=>display( lo_response->get_text( ) ).
        ENDIF.
      CATCH /goog/cx_sdk INTO DATA(lo_exception).
        cl_demo_output=>display( lo_exception->get_text( ) ).
    ENDTRY.
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Provide system instructions to the model

To pass text-based [system instructions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions) to the model, you can use the `SET_SYSTEM_INSTRUCTIONS` method.
    
    
    TRY.
        DATA(lo_response) = lo_model->set_system_instructions( 'SYSTEM_INSTRUCTIONS'
                                 )->generate_content( iv_prompt_text = 'PROMPT' ).
        IF lo_response IS BOUND.
          cl_demo_output=>display( lo_response->get_text( ) ).
        ENDIF.
      CATCH /goog/cx_sdk INTO DATA(lo_exception).
        cl_demo_output=>display( lo_exception->get_text( ) ).
    ENDTRY.
    

Replace the following:

  * `SYSTEM_INSTRUCTIONS`: Your [system instructions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions) to the model.
  * `PROMPT`:Your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).



To clear the system instructions, use the `lo_model->clear_system_instructions()` method.

### Set generation configuration for the model

While you can set default generation parameters in `/GOOG/AI_CONFIG`, you can override them for a specific call using the `SET_GENERATION_CONFIG` method.
    
    
    TRY.
        DATA(lo_response) = lo_model->set_generation_config(
                                  iv_temperature       = 'TEMPERATURE'
                                  iv_top_p             = 'TOP_P'
                                  iv_top_k             = 'TOP_K'
                                  iv_max_output_tokens = 'MAX_OUTPUT_TOKENS'
                                )->generate_content( iv_prompt_text = 'PROMPT' ).
        IF lo_response IS BOUND.
          cl_demo_output=>display( lo_response->get_text( ) ).
        ENDIF.
      CATCH /goog/cx_sdk INTO DATA(lo_exception).
        cl_demo_output=>display( lo_exception->get_text( ) ).
    ENDTRY.
    

Replace the following:

  * `TEMPERATURE`: Randomness temperature.
  * `TOP_P`: Top-P sampling.
  * `TOP_K`: Top-K sampling.
  * `MAX_OUTPUT_TOKENS`: Maximum number of output tokens per message
  * `PROMPT`: Your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).



For all available options, see the method parameters in `/GOOG/CL_MODEL_GEMMA_BASE`.

To clear these overrides, use the `lo_model->clear_generation_config()` method.

### Pass multimodal input to the model

Gemma accepts multiple parts in a single prompt, including text and media.

#### Add text parts

To pass the text parts, before calling the `GENERATE_CONTENT` method, use the `ADD_PART_TEXT` method.
    
    
    TRY.
        DATA(lo_response) = lo_model->add_part_text( 'This is the first part of the prompt.'
                                 )->add_part_text( 'This is the second part.'
                                 )->generate_content( ).
        IF lo_response IS BOUND.
          cl_demo_output=>display( lo_response->get_text( ) ).
        ENDIF.
      CATCH /goog/cx_sdk INTO DATA(lo_exception).
        cl_demo_output=>display( lo_exception->get_text( ) ).
    ENDTRY.
    

#### Add inline image data

To pass inline image data, before calling the `GENERATE_CONTENT` method, use the `ADD_PART_INLINE_DATA` method.

Provide Base64-encoded image data.
    
    
    DATA lv_image_base64 TYPE string.
    " ... code to load base64 image data into lv_image_base64 ...
    
    TRY.
        DATA(lo_response) = lo_model->add_part_inline_data(
                                  iv_mime_type = 'image/png'  " or image/jpeg
                                  iv_data      = lv_image_base64
                                )->generate_content( iv_prompt = 'PROMPT').
        IF lo_response IS BOUND.
          cl_demo_output=>display( lo_response->get_text( ) ).
        ENDIF.
      CATCH /goog/cx_sdk INTO DATA(lo_exception).
        cl_demo_output=>display( lo_exception->get_text( ) ).
    ENDTRY.
    

### Count tokens

To estimate the number of tokens a prompt consumes before sending the prompt for generation, use the `count_tokens` method.
    
    
    TRY.
        DATA(lv_token_count) = lo_model->count_tokens(
                                    iv_prompt_text = 'PROMPT'
                                  ).
        cl_demo_output=>display( |Total Tokens: { lv_token_count }| ).
      CATCH /goog/cx_sdk INTO DATA(lo_exception).
        cl_demo_output=>display( lo_exception->get_text( ) ).
    ENDTRY.
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

## Receive response from Gemma

The `GENERATE_CONTENT` method returns an instance of the `/GOOG/CL_GEMMA_RESPONSE` class. This class provides methods to access the model's output.

  * Get text response: `DATA(lv_response_text) = lo_response->get_text()`.
  * Get finish reason: `DATA(lv_finish_reason) = lo_response->get_finish_reason()`.
  * Get token usage: `DATA(ls_usage) = lo_response->get_usage()`. This returns prompt tokens, completion tokens, and total tokens.
  * Get tool calls (for Function Calling): `DATA(lt_tool_calls) = lo_response->get_tool_calls()`. This returns a table of type `/GOOG/CL_MODEL_GEMMA_BASE=>TT_FUNCTION_DETAILS`.
  * Check response type: `lo_response->is_vertex_ai_response()` or `lo_response->is_gemini_api_response()`.



## Demo program

To generate text and multimodal content, use the demo program `/GOOG/R_DEMO_GEMMA` provided by the ABAP SDK for Google Cloud. This demo report provides examples that you can use to interact with Gemma features. It provides examples for both the `/GOOG/CL_GEMMA_ON_VERTEXAI` and `/GOOG/CL_GEMMA_ON_CLOUDRUN` classes.

## Pricing

The cost for Gemma models depends on the deployment method and the specific Google Cloud services you consume.

### Gemma on Agent Platform

You're charged for Vertex AI Inference endpoint usage. This is primarily based on the machine type, such as `g2-standard-12`, the number, and type of accelerators, such as `NVIDIA_L4`.

For detailed information, see [Agent Platform Pricing](https://cloud.google.com/vertex-ai/pricing) and [Generative AI on Agent Platform Pricing](https://docs.cloud.google.com/vertex-ai/generative-ai/pricing).

### Gemma on Cloud Run

You incur costs for the Cloud Run service based on CPU allocation, memory allocation, number of requests, and network egress. For details, see [Cloud Run Pricing](https://cloud.google.com/run/pricing). The container on Cloud Run likely calls the Gemini API (`generativelanguage.googleapis.com`). Usage of the Gemini API is subject to its own pricing model, typically based on the number of input or output characters or tokens. For detailed information, see [Gemini API Pricing](https://ai.google.dev/pricing).

To estimate costs, use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator).

## Quotas and limits

Quotas and limits depend on the services you use.

### Gemma on Agent Platform

Gemma on Agent Platform is subject to [Agent Platform quotas and limits](https://docs.cloud.google.com/vertex-ai/quotas). This includes limits on prediction requests per minute, deployed models, and regional resource quotas.

### Gemma on Cloud Run

Gemma on Cloud Run is subject to [Cloud Run quotas](https://docs.cloud.google.com/run/quotas). This includes limits on the number of services, container instances, and request concurrency. It is also subject to [Gemini API rate limits](https://ai.google.dev/quotas). This typically involves requests per minute.

Check the Google Cloud console for the specific quotas applicable to your project.

## What's next

  * Learn about [application development with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/developer).
  * Ask your questions and discuss the Agent Platform SDK for ABAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
