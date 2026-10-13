---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/invoke-gemini-models/
title: Invoke the Gemini models \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:36.911056+00:00
---

# Invoke the Gemini models  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/invoke-gemini-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Invoke the Gemini models Stay organized with collections  Save and categorize content based on your preferences. 

SAP BTP edition v1.1keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/invoke-gemini-models)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemini-models)



This document describes how to invoke the Gemini models to generate response for text and multimodal input, by using the Agent Platform SDK for ABAP. Gemini models can accept multiple modes of input, including [text](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-chat-prompts-gemini), [image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/image-understanding), [video](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding), [audio](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding), and [documents](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/document-understanding). You can use the Gemini models for use cases such as the following:

  * Summarizing free-form text
  * Describing or interpreting media assets
  * Translating between languages



Using generative models to build AI-centric features doesn't require any machine learning (ML) expertise. You don't need to collect a large dataset or train a model. To start using the models, describe what you want the model to do. The Agent Platform SDK for ABAP provides ABAP classes and methods to access the Gemini models from your SAP environment. To begin, view these code samples.

## Before you begin

Before using the Agent Platform SDK for ABAP with the Gemini models, make sure that you or your administrators have completed the following prerequisites:

  * [Enabled the Agent Platform API](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * [Installed](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#installation) the Agent Platform SDK for ABAP in your SAP environment.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#authentication) to access the Agent Platform API.
  * [Configured the model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).



## Send a request to Gemini

This section explains how to send requests to Gemini models through the Agent Platform API by using the Agent Platform SDK for ABAP.

### Instantiate the Gemini multimodal invoker class

To invoke the Gemini text and multimodal models by using text or multimodal prompts, you can use the `/GOOG/CL_GENERATIVE_MODEL` class. You instantiate the class by passing the model key configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
    
    
    DATA(lo_model) = NEW /goog/cl_generative_model( iv_model_key = 'MODEL_KEY' ).
    

Replace `MODEL_KEY` with the model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).

### Generate content with a prompt

To generate content by providing a text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design) to the model, you can use the `GENERATE_CONTENT` method.
    
    
    lo_model->generate_content( 'PROMPT' ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Provide system instructions to the model

To pass text-based [system instructions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions) to the model, you can use the `SET_SYSTEM_INSTRUCTIONS` method.
    
    
    lo_model->set_system_instructions( 'SYSTEM_INSTRUCTIONS' ).
    

Replace `SYSTEM_INSTRUCTIONS` with your [system instructions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions) to the model.

### Add safety settings

To add safety settings for the model to generate responses, you can use the `ADD_SAFETY_SETTINGS` method. Use this feature to impose safety guidelines on the model to block unsafe content.
    
    
    lo_model->add_safety_settings( iv_harm_category        = 'HARM_CATEGORY'
                            iv_harm_block_threshold = 'HARM_BLOCK_THRESHOLD'
                            iv_harm_block_method    = 'HARM_BLOCK_METHOD' ).
    

Replace the following:

  * `HARM_CATEGORY`: The [Harm category](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/HarmCategory) that you want to apply.
  * `HARM_BLOCK_THRESHOLD`: The probability based [thresholds level](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/HarmBlockThreshold) that you want to apply.
  * `HARM_BLOCK_METHOD`: The [harm block method](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/SafetySetting#HarmBlockMethod) that you want to apply.



With each method call, the `ADD_SAFETY_SETTINGS` method adds the specified safety settings to the model's input.

### Set generation configuration for the model

You maintain the generation configuration for the models in the table `/GOOG/AI_CONFIG`. To override the generation configuration for a particular call, you can use the `SET_GENERATION_CONFIG` method. If you set the import parameter for a generation property, then the passed parameter value takes effect.
    
    
    lo_model->set_generation_config( iv_response_mime_type = 'RESPONSE_MIME_TYPE'
                                    iv_temperature        = 'TEMPERATURE'
                                    iv_top_p              = 'TOP_P'
                                    iv_top_k              = 'TOP_K'
                                    iv_candidate_count    = 'CANDIDATE_COUNT'
                                    iv_max_output_tokens  = 'MAX_OUTPUT_TOKENS'
                                    iv_presence_penalty   = 'PRESENCE_PENALTY'
                                    iv_frequency_penalty  = 'FREQUENCY_PENALTY' ).
    

Replace the following:

  * `RESPONSE_MIME_TYPE`: Response MIME type for the model.
  * `TEMPERATURE`: Randomness temperature.
  * `TOP_P`: Top-P sampling.
  * `TOP_K`: Top-K sampling.
  * `CANDIDATE_COUNT`: Number of candidates to generate.
  * `MAX_OUTPUT_TOKENS`: Maximum number of output tokens per message
  * `PRESENCE_PENALTY`: Positive penalties.
  * `FREQUENCY_PENALTY`: Frequency penalties.



For more information about these parameters, see [Configure model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).

### Pass multimodal input to the model

You can invoke the Gemini models using multimodal input, which can be either [text](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-chat-prompts-gemini), [image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/image-understanding), [video](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding), [documents](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/document-understanding), or a combination of these. You can pass the input either as raw data or by providing the Cloud Storage URI of the file objects.

#### Set raw data

To provide the raw data of a file as input to the model, along with its MIME type, you can use the `SET_INLINE_DATA` method. For video inputs, to consider only a specific part of a video, you can set the start time and end time by using the optional importing parameters `IV_VIDEO_START_OFFSET` and `IV_VIDEO_END_OFFSET`, respectively.
    
    
    lo_model->set_inline_data( iv_mime_type = 'MIME_TYPE'
                              iv_data      = 'RAW_DATA' ).
    

Replace the following:

  * `MIME_TYPE`: The IANA standard MIME type of the raw data. By default, the MIME type is set to `application/pdf`.
  * `RAW_DATA`: Base64-encoded raw data of the image, PDF, or video to include inline in the prompt.



To clear the raw data of files from the model's input with the same instance of the `/GOOG/CL_GENERATIVE_MODEL` class, you can use the `CLEAR_INLINE_DATA` method.
    
    
    lo_model->clear_inline_data( ).
    

#### Set objects from Cloud Storage

To provide the URI of a file object stored in a Cloud Storage bucket as input to the model, along with its MIME type, you can use the `SET_FILE_DATA` method. For video inputs, to consider only a specific part of a video, you can set the start time and end time by using the optional importing parameters `IV_VIDEO_START_OFFSET` and `IV_VIDEO_END_OFFSET`, respectively.
    
    
    lo_model->set_file_data( iv_mime_type = 'MIME_TYPE'
                            iv_file_uri  = 'FILE_URI' ).
    

Replace the following:

  * `MIME_TYPE`: The IANA standard MIME type of the file data. By default, the MIME type is set to `application/pdf`.
  * `FILE_URI`: The URI of the file stored in a Cloud Storage bucket.



If you want to pass all the files present in a Cloud Storage bucket as an input to the model, then use the method `SET_FILES_FROM_GCS` to specify the target Cloud Storage bucket name.
    
    
    lo_model->set_files_from_gcs( iv_storage_bucket_name = 'STORAGE_BUCKET_NAME').
    

Replace `STORAGE_BUCKET_NAME` with the name of the Cloud Storage bucket that contains the files.

If you have a separate client key for invoking the Cloud Storage API through the ABAP SDK for Google Cloud, then pass the client key name in importing parameter `IV_KEY_NAME`.

To clear the objects set through Cloud Storage URIs from the model's input with the same instance of the `/GOOG/CL_GENERATIVE_MODEL` class, you can use the `CLEAR_FILE_DATA` method.
    
    
    lo_model->clear_file_data( ).
    

### Set response MIME type

To set the [MIME type of the response](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/GenerationConfig) that the model responds with, you can use the `SET_RESPONSE_MIME_TYPE` method. If not set, then by default the model takes `text/plain` as the response MIME type.
    
    
    lo_model->set_response_mime_type( iv_mime_type = 'RESPONSE_MIME_TYPE' ).
    

Replace `RESPONSE_MIME_TYPE` with the [response MIME type](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/GenerationConfig) of generated content.

### Count number of tokens in a text prompt

To count the number of tokens in a text prompt before invoking the model with the prompt, you can use the `COUNT_TOKENS` method.
    
    
    DATA(lv_total_tokens) = lo_model->count_tokens( iv_prompt_text         = 'PROMPT'
                                                    iv_system_instructions = 'SYSTEM_INSTRUCTIONS'
                                  )->get_total_tokens( ).
    
    DATA(lv_total_billable_characters) = lo_model->count_tokens(
                                                    iv_prompt_text         = 'PROMPT'
                                                    iv_system_instructions = 'SYSTEM_INSTRUCTIONS'
                                                )->get_total_billable_characters( ).
    

Replace the following:

  * `PROMPT`: Your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).
  * `SYSTEM_INSTRUCTIONS`: Your [system instruction](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions) to the model.



## Receive response from Gemini

To receive processed responses from the model, the SDK provides the `/GOOG/CL_MODEL_RESPONSE` class.

The SDK chains the response captured by the `/GOOG/CL_MODEL_RESPONSE` class to the requests made through the methods of the `/GOOG/CL_GENERATIVE_MODEL` class, so that you can directly access the response in a single statement without requiring variables to store the intermediate results.

### Get text response

To receive a text response from the model, you can use the `GET_TEXT` method.
    
    
    DATA(lv_response_text) = lo_model->generate_content( 'PROMPT'
                                    )->get_text( ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Get safety rating

To receive a list of ratings for the safety of the model's response, you can use the `GET_SAFETY_RATING` method.
    
    
    DATA(lt_safety_ratings) = lo_model->generate_content( 'PROMPT'
                                    )->get_safety_rating( ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Get number of tokens in the request prompt

To receive the number of tokens in the input prompt to the model, you can use the `GET_PROMPT_TOKEN_COUNT` method.
    
    
    DATA(lv_prompt_token_count) = lo_model->generate_content( 'PROMPT'
                                        )->get_prompt_token_count( ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Get number of tokens in the model's response

To receive the number of tokens in the response from the model, you can use the `GET_CANDIDATES_TOKEN_COUNT` method.
    
    
    DATA(lv_candidates_token_count) = lo_model->generate_content( 'PROMPT'
                                            )->get_candidates_token_count( ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Get block reason

To receive the reason for which the model blocked response generation, you can use the `GET_BLOCK_REASON` method.
    
    
    DATA(lv_block_reason) = lo_model->generate_content( 'PROMPT'
                                  )->get_block_reason( ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Get block reason message

To receive a readable reason message for blocking response generation by the model, you can use the `GET_BLOCK_REASON_MESSAGE` method.
    
    
    DATA(lv_block_reason_message) = lo_model->generate_content( 'PROMPT'
                                          )->get_block_reason_message( ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

## Code samples

The following code samples demonstrate how to invoke the Gemini models to generate responses for varying types of input.

### Text-based generation

The following code sample shows how to generate a response from a text prompt along with a system instruction. System instruction is optional and you can pass it along with the prompt to instruct the model to behave in a specific manner.

#### Code sample
    
    
    DATA:
      lv_instruction TYPE string,
      lv_prompt      TYPE string.
    
    lv_instruction = 'SYSTEM_INSTRUCTIONS'.
    lv_prompt      = 'PROMPT'.
    
    TRY.
        DATA(lo_model) = NEW /goog/cl_generative_model( iv_model_key = 'MODEL_KEY' ).
    
        DATA(lv_response) = lo_model->set_system_instructions( lv_instruction
                                  )->generate_content( lv_prompt
                                  )out->write( lv_response ).
        IF lv_response IS NOT INITIAL.
          out->write( lv_response ).
    
      CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        out->write( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `MODEL_KEY`: The model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
  * `PROMPT`: Your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).
  * `SYSTEM_INSTRUCTIONS`: Your [system instructions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions) to the model.



### Multimodal generation

The following code sample shows how to generate a response from a multimodal input, such as text and an image. You can mention Cloud Storage URI or raw file data of an image, video, or document along with a text prompt. System instruction is optional and you can pass it along with the prompt to instruct the model to behave in a specific manner.

#### Code sample
    
    
    DATA:
      lv_instruction TYPE string,
      lv_prompt      TYPE string.
    
    lv_instruction = 'SYSTEM_INSTRUCTIONS'.
    lv_prompt      = 'PROMPT'.
    
    TRY.
        DATA(lo_model) = NEW /goog/cl_generative_model( iv_model_key = 'MODEL_KEY' ).
    
        DATA(lv_response) = lo_model->set_system_instructions( lv_instruction
                                  )->set_file_data( iv_mime_type = 'MIME_TYPE'
                                                    iv_file_uri  = 'FILE_URI'
                                  )->set_inline_data( iv_mime_type = 'MIME_TYPE'
                                                      iv_data      = 'INLINE_DATA'
                                  )->generate_content( lv_prompt
                                  )out->write( lv_response ).
        IF lv_response IS NOT INITIAL.
          out->write( lv_response ).
    
      CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        out->write( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `MODEL_KEY`: The model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
  * `PROMPT`: Your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).
  * `SYSTEM_INSTRUCTIONS`: Your [system instruction](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions) to the model.
  * `MIME_TYPE`: The IANA standard MIME type of the file data. By default, the MIME type is set to `application/pdf`.
  * `FILE_URI`: The URI of the file stored in a Cloud Storage bucket.
  * `INLINE_DATA`: Base64-encoded raw data of the image, PDF, or video to include inline in the prompt.



### Add safety settings for the model

The following code sample shows how to add safety settings for the model to generate response.

#### Code sample
    
    
    DATA:
      lv_instruction TYPE string,
      lv_prompt      TYPE string.
    
    lv_instruction = 'SYSTEM_INSTRUCTIONS'.
    lv_prompt      = 'PROMPT'.
    
    TRY.
        DATA(lo_model) = NEW /goog/cl_generative_model( iv_model_key = 'MODEL_KEY' ).
    
        DATA(lv_response) = lo_model->set_system_instructions( lv_instruction
                                  )->set_file_data( iv_mime_type = 'MIME_TYPE'
                                                    iv_file_uri  = 'FILE_URI'
                                  )->set_inline_data( iv_mime_type = 'MIME_TYPE'
                                                      iv_data      = 'INLINE_DATA'
                                  )->add_safety_settings( iv_harm_category        = 'HARM_CATEGORY'
                                                          iv_harm_block_threshold = 'HARM_BLOCK_THRESHOLD'
                                                          iv_harm_block_method    = 'HARM_BLOCK_METHOD'
                                  )->generate_content( lv_prompt
                                  )out->write( lv_response ).
        IF lv_response IS NOT INITIAL.
          out->write( lv_response ).
    
      CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        out->write( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `MODEL_KEY`: The model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
  * `PROMPT`: Your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).
  * `SYSTEM_INSTRUCTIONS`: Your [system instruction](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions) to the model.
  * `MIME_TYPE`: The IANA standard MIME type of the file data. By default, the MIME type is set to `application/pdf`.
  * `FILE_URI`: The URI of the file stored in a Cloud Storage bucket.
  * `INLINE_DATA`: Base64-encoded raw data of the image, PDF, or video to include inline in the prompt.
  * `HARM_CATEGORY`: The [Harm category](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/HarmCategory) that you want to apply.
  * `HARM_BLOCK_THRESHOLD`: The probability based [thresholds level](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/HarmBlockThreshold) that you want to apply.
  * `HARM_BLOCK_METHOD`: The [harm block method](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/SafetySetting#HarmBlockMethod) that you want to apply.



### Find number of tokens and billable characters in a prompt

Before invoking the model with a prompt, you might want to check the number of tokens in your prompt and how many billable characters are present in your token to plan your Google Cloud project billing. The following code sample shows how to find these numbers and evaluate your billing for similar model call.

#### Code sample
    
    
    DATA:
      lv_prompt      TYPE string.
    
    lv_prompt      = 'PROMPT'.
    
    TRY.
        DATA(lo_model) = NEW /goog/cl_generative_model( iv_model_key = 'MODEL_KEY' ).
    
        DATA(lv_total_tokens) = lo_model->count_tokens( lv_prompt
                                      )->get_total_tokens( ).
    
        DATA(lv_total_billable_characters) = lo_model->count_tokens( lv_prompt
        )out->write( |Total Tokens - { lv_total_tokens }| ).
        IF lv_total_tokens IS NOT INITIAL.
          out->write( |Total Tokens - { lv_total_tokens }| ).
    
        ENDIF.
    
        IF lv_total_billable_characters IS NOT INITIAL.
          out->write( |Total Billable Characters - { lv_total_billable_characters }| ).
    
        out->write( lo_cx_sdk->get_text( ) ).
      CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        out->write( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `PROMPT`: Your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).
  * `MODEL_KEY`: The model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).



## What's next

  * Learn about [application development with the SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/developer).
  * Ask your questions and discuss the Agent Platform SDK for ABAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
