---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemini-models/
title: Invoke the Gemini models \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:39.203941+00:00
---

# Invoke the Gemini models  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemini-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Invoke the Gemini models Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/invoke-gemini-models)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-gemini-models)



This document describes how to invoke the Gemini models to generate response for text and multimodal input, by using the Agent Platform SDK for ABAP. Gemini models can accept multiple modes of input, including [text](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-chat-prompts-gemini), [image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/image-understanding), [video](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/video-understanding), [audio](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/audio-understanding), and [documents](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/document-understanding). You can use the Gemini models for use cases such as the following:

  * Summarizing free-form text
  * Describing or interpreting media assets
  * Translating between languages



Using generative models to build AI-centric features doesn't require any machine learning (ML) expertise. You don't need to collect a large dataset or train a model. To start using the models, describe what you want the model to do. The Agent Platform SDK for ABAP provides ABAP classes and methods to access the Gemini models from your SAP environment. To begin, view these code samples.

## Before you begin

Before using the Agent Platform SDK for ABAP with the Gemini models, make sure that you or your administrators have completed the following prerequisites:

  * [Enabled the Agent Platform API](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * [Installed](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#installation) the Agent Platform SDK for ABAP in your SAP environment.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#authentication) to access the Agent Platform API.
  * [Configured the model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).



## Send a request to Gemini

This section explains how to send requests to Gemini models through the Agent Platform API by using the Agent Platform SDK for ABAP.

### Instantiate the Gemini multimodal invoker class

To invoke the Gemini text and multimodal models by using text or multimodal prompts, you can use the `/GOOG/CL_GENERATIVE_MODEL` class. You instantiate the class by passing the model key configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
    
    
    DATA(lo_model) = NEW /goog/cl_generative_model( iv_model_key = 'MODEL_KEY' ).
    

Replace `MODEL_KEY` with the model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).

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
                                    iv_frequency_penalty  = 'FREQUENCY_PENALTY'
                                    iv_include_thoughts   = abap_true
                                    iv_thinking_budget    = 'THINKING_BUDGET'
                                    iv_thinking_level     = 'THINKING_LEVEL').
    

Replace the following:

  * `RESPONSE_MIME_TYPE`: Response MIME type for the model.
  * `TEMPERATURE`: Randomness temperature.
  * `TOP_P`: Top-P sampling.
  * `TOP_K`: Top-K sampling.
  * `CANDIDATE_COUNT`: Number of candidates to generate.
  * `MAX_OUTPUT_TOKENS`: Maximum number of output tokens per message.
  * `PRESENCE_PENALTY`: Positive penalties.
  * `FREQUENCY_PENALTY`: Frequency penalties.
  * `INCLUDE_THOUGHTS`: Set to `abap_true` to include the model's internal reasoning process in the response.
  * `THINKING_BUDGET`: Maximum tokens for internal reasoning.
  * `THINKING_LEVEL`: Intensity of the model's thinking process. For information about thinking level, see [Control model thinking](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking#budget).



For more information about these parameters, see [Configure model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).

### Control randomness of model's output

You can control the randomness of Gemini's output by setting the [seed](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#seed) parameter. While this encourages the model to generate the same response for identical requests, this is a best-effort result and is not guaranteed. Note that changing other parameters, such as temperature, still causes the output to vary.

To set a seed value for a particular call, use the `SET_GENERATION_CONFIG` method.
    
    
    lo_model->set_generation_config( iv_seed = SEED_VALUE).
    

Replace `SEED_VALUE` with an integer value for [seed](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/adjust-parameter-values#seed).

### Set thinking configuration for the model

The [thinking](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking) configuration only works with [supported Gemini models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking#supported-models).

#### Include model thoughts in response

You use this feature to review the [model's thoughts](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking#thought-summaries) or the model's reasoning process as the model generates the final answer.

To include thoughts for a particular call, use the `SET_GENERATION_CONFIG` method.
    
    
    lo_model->set_generation_config( iv_include_thoughts = abap_true ).
    

#### Control the thinking budget

You can specify the maximum number of tokens that the model can use for its internal "thoughts" or reasoning process before generating the final response. This setting overrides the default limit of 8,192 tokens, letting you customize the limit for your task complexity.

To set the thinking budget for a particular call, you can use the `SET_GENERATION_CONFIG` method.
    
    
    lo_model->set_generation_config( iv_thinking_budget = 'THINKING_BUDGET' ).
    

Replace `THINKING_BUDGET` with an integer value for [thinking budget](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking#budget).

#### Control the thinking level

You can specify the intensity or "thinking level" of the model's reasoning process.

To set the thinking level for a particular call, use the `SET_GENERATION_CONFIG` method.
    
    
    lo_model->set_generation_config( iv_thinking_level = 'THINKING_LEVEL' ).
    

Replace `THINKING_LEVEL` with a valid thinking level value, such as `high`, `medium`, `low`, or `minimal`. For more information about the supported thinking levels, see [Control model thinking](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/thinking#budget).

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

### Set response schema

With [controlled generation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output#googlegenaisdk_ctrlgen_with_enum_schema-python_vertex_ai_sdk), you can ensure that a model's generated output adheres to a specific schema for consistently formatted responses.

To set the response schema for a model, you can use the `SET_GENERATION_CONFIG` method:
    
    
    lo_model->set_generation_config( iv_response_schema = 'RESPONSE_SCHEMA'
       iv_response_mime_type = 'application/json'
    )->generate_content( lv_prompt )->get_text( ).
    

Replace `RESPONSE_SCHEMA` with reference to your ABAP structure following the format as described in [Supported schema fields](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/control-generated-output#fields).

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



### Add content history

To pass the history of a conversation with Gemini, you can use the `ADD_CONTENT_HISTORY` method. Gemini uses the conversation history passed through this method as context for responding to input prompts.
    
    
    DATA:
      ls_content_history TYPE /goog/cl_generative_model=>ty_content_history,
      lt_content_history TYPE /goog/cl_generative_model=>tt_content_history.
    
    ls_content_history-role = 'user'.
    ls_content_history-text = 'HISTORICAL_INPUT_PROMPT'.
    APPEND ls_content_history TO lt_content_history.
    CLEAR ls_content_history.
    
    ls_content_history-role = 'model'.
    ls_content_history-text = 'HISTORICAL_MODEL_RESPONSE'.
    APPEND ls_content_history TO lt_content_history.
    CLEAR ls_content_history.
    
    TRY.
        DATA(lo_model) = NEW /goog/cl_generative_model( iv_model_key = 'gemini-flash' ).
        DATA(lv_response) = lo_model->add_content_history( lt_content_history
                                   )->generate_content('CURRENT_INPUT_PROMPT'
                                   )->get_text( ).
        IF lv_response IS NOT INITIAL.
          cl_demo_output=>display( lv_response ).
    
        ENDIF.
      CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `HISTORICAL_INPUT_PROMPT`: The historical input prompt passed to Gemini.
  * `HISTORICAL_MODEL_RESPONSE`: The historical model response for the historical input prompt.
  * `CURRENT_INPUT_PROMPT`: The input prompt to Gemini for which you want a response in context with the historical input prompts and model responses set.



You can also pass raw files, Cloud Storage file URIs, function calls, and function responses as conversation history by using the `ADD_CONTENT_HISTORY` method. To do so, set the following fields of the variable `LS_CONTENT_HISTORY`:

  * `FILE_INLINE_DATA`: Pass raw file data for one or more files with the following fields: 
    * `MIME_TYPE`: The IANA standard MIME type of the file data.
    * `FILE_DATA`: Base64-encoded raw data of the file.
    * `VIDEO_START_OFFSET`: Video start time (only for video files).
    * `VIDEO_END_OFFSET`: Video end time (only for video files).
  * `FILE_URIS`: Pass the Cloud Storage URI of one or more files with the following fields: 
    * `MIME_TYPE`: The IANA standard MIME type of the file data.
    * `FILE_URI`: The URI of the file stored in a Cloud Storage bucket.
    * `VIDEO_START_OFFSET`: Video start time (only for video files).
    * `VIDEO_END_OFFSET`: Video end time (only for video files).
  * `FUNCTION_CALL`: Pass the function call to the model with the following fields: 
    * `NAME`: The name of the function that you need to call.
    * `ARGS`: Function parameters with values as reference.
  * `FUNCTION_RESPONSE`: Pass the function response from the model with the following fields: 
    * `NAME`: The name of the invoked function that produced the response.
    * `RESPONSE`: Response from the model as reference.



## Receive response from Gemini

To receive processed responses from the model, the SDK provides the `/GOOG/CL_MODEL_RESPONSE` class.

The SDK chains the response captured by the `/GOOG/CL_MODEL_RESPONSE` class to the requests made through the methods of the `/GOOG/CL_GENERATIVE_MODEL` class, so that you can directly access the response in a single statement without requiring variables to store the intermediate results.

### Get text response

To receive a text response from the model, you can use the `GET_TEXT` method.
    
    
    DATA(lv_response_text) = lo_model->generate_content( 'PROMPT'
                                    )->get_text( ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Get model thoughts

To receive the model's internal thoughts or reasoning behind the final response, use the `GET_MODEL_THOUGHTS` method.
    
    
    DATA(lt_model_thoughts) = lo_model->generate_content( 'PROMPT'
                                    )->get_model_thoughts( ).
    

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
                                  )->get_text( ).
        IF lv_response IS NOT INITIAL.
          cl_demo_output=>display( lv_response ).
    
        ENDIF.
      CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `MODEL_KEY`: The model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
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
                                  )->get_text( ).
        IF lv_response IS NOT INITIAL.
          cl_demo_output=>display( lv_response ).
    
        ENDIF.
      CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `MODEL_KEY`: The model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
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
                                  )->get_text( ).
        IF lv_response IS NOT INITIAL.
          cl_demo_output=>display( lv_response ).
    
        ENDIF.
      CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `MODEL_KEY`: The model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
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
                                                    )->get_total_billable_characters( ).
        IF lv_total_tokens IS NOT INITIAL.
          cl_demo_output=>display( 'Total Tokens -' && lv_total_tokens ).
    
        ENDIF.
    
        IF lv_total_billable_characters IS NOT INITIAL.
          cl_demo_output=>display( 'Total Billable Characters -' && lv_total_billable_characters ).
    
        ENDIF.
      CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `PROMPT`: Your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).
  * `MODEL_KEY`: The model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).



## What's next

  * Learn about [application development with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/developer).
  * Ask your questions and discuss the Agent Platform SDK for ABAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
