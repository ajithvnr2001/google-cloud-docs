---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-claude-models/
title: Invoke the Anthropic Claude models \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:13:21.459188+00:00
---

# Invoke the Anthropic Claude models  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-claude-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Invoke the Anthropic Claude models Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/invoke-claude-models)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/invoke-claude-models)



This document describes how to invoke the [Anthropic Claude models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude) to generate response for text and multimodal input, by using the Agent Platform SDK for ABAP. Claude models can accept multiple modes of input, including [text](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-chat-prompts-gemini), [image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/image-understanding), and [documents](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/document-understanding). You can use the Claude models for use cases such as the following:

  * Summarizing free-form text
  * Describing or interpreting media assets
  * Translating between languages



To start using the models, describe what you want the model to do. The Agent Platform SDK for ABAP provides ABAP classes and methods to access the Claude models from your SAP environment.

## Before you begin

Before using the Agent Platform SDK for ABAP with the Claude models, make sure that you or your administrators have completed the following prerequisites:

  * [Enabled the Agent Platform API](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * [Enabled a supported Claude model](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#enable-partner-model) from the Model Garden in your Google Cloud project.
  * [Installed](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#installation) the Agent Platform SDK for ABAP in your SAP environment.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#authentication) to access the Agent Platform API.
  * [Configured the model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#claude).



## Send request to Claude

This section explains how to send requests to Claude models through the Agent Platform API by using the Agent Platform SDK for ABAP.

### Instantiate the Claude multimodal invoker class

To invoke the Claude text and multimodal models by using text or multimodal prompts, you can use the `/GOOG/CL_MODEL_CLAUDE` class. You instantiate the class by passing the model key configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#claude):
    
    
    DATA(lo_model) = NEW /goog/cl_model_claude( iv_model_key = 'MODEL_KEY' ).
    

Replace `MODEL_KEY` with the model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#claude).

### Generate content with a prompt

To generate content by providing a text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design) to the model, you can use the `GENERATE_CONTENT` method:
    
    
    lo_model->generate_content( 'PROMPT' ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Provide system instructions to the model

To pass text based [system instructions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions) to the model, you can use the `SET_SYSTEM_INSTRUCTIONS` method:
    
    
    lo_model->set_system_instructions( 'SYSTEM_INSTRUCTIONS' ).
    

Replace `SYSTEM_INSTRUCTIONS` with your [system instructions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions) to the model.

### Set generation configuration for the model

You maintain generation configuration for the models in the table `/GOOG/AI_CONFIG`. To override the generation configuration for a particular call, you can use the `SET_GENERATION_CONFIG` method. If the import parameter for a generation property is set, then the passed parameter value is taken into effect.
    
    
    lo_model->set_generation_config(
                                    iv_temperature        = 'TEMPERATURE'
                                    iv_top_p              = 'TOP_P'
                                    iv_top_k              = 'TOP_K'
                                    iv_max_output_tokens  = 'MAX_OUTPUT_TOKENS' ).
    

Replace the following:

  * `TEMPERATURE`: Randomness temperature.
  * `TOP_P`: Top-P sampling.
  * `TOP_K`: Top-K sampling.
  * `MAX_OUTPUT_TOKENS`: Maximum number of output tokens per message



For more information about these parameters, see [Configure model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#claude).

### Pass multimodal input to the model

You can invoke the Claude models using multimodal input, which can be either [text](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/send-chat-prompts-gemini), [image](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/image-understanding), or [documents](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/document-understanding). You can pass input for images and PDFs as raw data. For PDFs, you can also provide a URI if the PDF is publicly accessible.

The following table lists the supported mime types:

Media type | Supported MIME types  
---|---  
Images | 

  * `image/jpeg`
  * `image/png`
  * `image/gif`
  * `image/webp`

  
Documents | 

  * `application/pdf`

  
  
#### Set raw data

To provide the raw data of a file as input to the model, along with its MIME type, you can use the `SET_INLINE_DATA` method:
    
    
    lo_model->set_inline_data( iv_mime_type = 'MIME_TYPE'
                              iv_data      = 'RAW_DATA'
                              iv_type      = 'base64' ).
    

Replace the following:

  * `MIME_TYPE`: The IANA standard MIME type of the raw data. By default, the MIME type is set to `image/jpeg`.
  * `RAW_DATA`: Base64-encoded raw data of the image or PDF to include inline in the prompt.



To clear the raw data of files from the model's input with the same instance of the `/GOOG/CL_MODEL_CLAUDE` class, you can use the `CLEAR_INLINE_DATA` method:
    
    
    lo_model->clear_inline_data( ).
    

### Count number of tokens in a text prompt

To count the number of tokens in a text prompt before invoking the model with the prompt, you can use the `COUNT_TOKENS` method:
    
    
    DATA(lv_total_tokens) = lo_model->count_tokens( iv_prompt_text         = 'PROMPT'
                                                    iv_system_instructions = 'SYSTEM_INSTRUCTIONS'
                                  )->get_total_tokens( ).
    

Replace the following:

  * `PROMPT`: Your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).
  * `SYSTEM_INSTRUCTIONS`: Your [system instructions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions) to the model.



### Add stop sequences

A `stop_sequence` is a set of strings that instructs Claude to halt generation upon encountering any of these strings in its response. Essentially, it's a command telling Claude, "If you generate this sequence, stop generating immediately!"

The following code sample does not include a `stop_sequence`:
    
    
    lv_prompt = 'Generate a JSON object representing a person with a name, email, and phone number'.
    
    lv_response = lo_model->generate_content( lv_prompt )->get_text( ).
    

This code sample returns the following response:
    
    
    {
      "name": "Dana A",
      "email": "dana@example.com",
      "phoneNumber": "800-555-0199"
    }
    

The following code sample includes a `stop_sequence`:
    
    
    DATA: lt_stop_sequences TYPE TABLE OF STRING.
    
    lv_prompt = 'Generate a JSON object representing a person with a name, email, and phone number'.
    
    APPEND '}' to lt_stop_sequences.
    
    lv_response = lo_model->set_stop_sequence( lt_stop_sequences
                    )->generate_content( lv_prompt
                    )->get_text( ).
    

This code sample returns the following response:

Here's a JSON object representing a person with a name, email, and phone number:
    
    
    {
      "name": "Dana A",
      "email": "dana@example.com",
      "phoneNumber": "800-555-0199"
    

Notice that the output does not include the `}` stop sequence. To parse this as JSON, you need to add the closing `}`.

When a Claude model provides a response, its `stop_reason` property indicates why the model stopped generating text.

To get the stop reason, you can use the following code sample:
    
    
    lv_stop_reason = lo_model->set_stop_sequence( lt_stop_sequences
                    )->generate_content( lv_prompt
                    )->get_stop_reason( ).
    

### Add examples

Few-shot prompting is an effective strategy where you provide a model with a small set of examples to guide its output. You can achieve this by using the conversation history to furnish Claude with these examples.

For example, to analyze tweet sentiment by using Claude, you might begin by asking, "Analyze the sentiment in this tweet: " and then observe the resulting output.
    
    
    lv_prompt = 'The Burger was delicious and my taste buds were on fire, too yummy!'
    lv_system_instruction = 'Please do the sentiment analysis of the review'.
    lv_response = lo_model->set_system_instructions( lv_system_instructions
                         )->generate_text( lv_prompt
                         )->get_text( ).
    

Output:
    
    
    # Sentiment Analysis
    
    This tweet expresses a strongly positive sentiment:
    
    - Words like "delicious" and "yummy" directly convey enjoyment
    - The phrase "taste buds were on fire" is used positively to indicate intense flavor enjoyment
    - The exclamation mark adds enthusiasm
    - "too yummy" emphasizes the exceptional quality
    
    Overall, this is a very positive tweet expressing high satisfaction with the burger.
    

While a comprehensive response is valuable, for automated sentiment analysis of numerous tweets, a more concise output from Claude is preferable. You can standardize Claude's responses to a single word like POSITIVE, NEUTRAL, NEGATIVE or a numeric value like 1, 0, -1.
    
    
    lv_prompt = 'The Burger was delicious and my taste buds were on fire, too yummy!'.
    lv_response = lo_model->add_examples( iv_input = |Unpopular opinion: Pickles are disgusting. Don't hate me|
            iv_output = |NEGATIVE|
            )->add_examples( iv_input = |I think my love for burgers might be getting out of hand. I just bought a burger sticker for my crocs|
            iv_output =  |POSITIVE|
            )->add_examples( iv_input = |Seriously why would anyone ever eat a brugers?  Those things are unhealthy!|
            iv_output =  |NEGATIVE|
            )->generate_content( lv_prompt
            )->get_text( ).
    

Output:
    
    
    POSITIVE
    

## Set assistant text

Another common strategy for getting very specific outputs is to "put words in Claude's mouth". Instead of only providing `user` messages to Claude, you can also supply an `assistant` message that Claude uses when generating output.

If you supply an `assistant` message, then Claude continues the conversation from the last `assistant` token. Just remember that you need to start with a `user` message.
    
    
      lv_prompt = 'The fourth nearest planet to sun is: A) Mercury B) Venus C) Mars D ) Andromeda'.
     lv_assistant_text = 'The answer is:'.
        lv_response = lo_model->set_assistant_text( lv_instruction
                                           )->generate_content( lv_prompt
                                           )->get_text( ).
    

This code snippet shows the following output: `C) Mars`.

### Set Anthropic version

You can set the parameter `anthropic_version`. By default, `vertex-2023-10-16` is the set value for this parameter. You only need to change its value if you want to access any other supported Anthropic version.

If you need to change the Anthropic version, then use the `SET_ANTHROPIC_VERSION` method:
    
    
    lo_model->set_anthropic_version( 'ANTHROPIC_VERSION' ).
    

Replace `ANTHROPIC_VERSION` with the Anthropic version to use. For more information, see the [Anthropic documentation](https://docs.anthropic.com/en/api/claude-on-vertex-ai).

## Receive response from Claude

To receive and process responses from the model, the SDK provides the `/GOOG/CL_RESPONSE_CLAUDE` class.

The SDK chains the response captured by the `/GOOG/CL_RESPONSE_CLAUDE` class to the requests made through the methods of the `/GOOG/CL_MODEL_CLAUDE` class, so that you can directly access the response in a single statement without requiring variables to store the intermediate results.

### Get text response

To receive a text response from the model, you can use the `GET_TEXT` method:
    
    
    DATA(lv_response_text) = lo_model->generate_content( 'PROMPT'
                                    )->get_text( ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Get number of tokens in the request prompt

To receive the number of tokens in the input prompt to the model, you can use the `GET_PROMPT_TOKEN_COUNT` method:
    
    
    DATA(lv_prompt_token_count) = lo_model->generate_content( 'PROMPT'
                                        )->get_prompt_token_count( ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Get number of tokens in the model's response

To receive the number of tokens in the response from the model, you can use the `GET_CANDIDATES_TOKEN_COUNT` method:
    
    
    DATA(lv_candidates_token_count) = lo_model->generate_content( 'PROMPT'
                                            )->get_candidates_token_count( ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Get total token count (request and response)

To get the total token count for both the request and response, use the `GET_TOTAL_TOKEN_COUNT` method:
    
    
    DATA(lv_stop_reason) = lo_model->generate_content( 'PROMPT'
                                  )->get_total_token_count( ).
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

### Get stop reason

To receive the reason for which the model blocked response generation, you can use the `GET_STOP_REASON` method:
    
    
    DATA(lv_stop_reason) = lo_model->generate_content( 'PROMPT'
                                  )->get_stop_reason( ).
    Replace PROMPT with your text prompt.
    

Replace `PROMPT` with your text [prompt](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/introduction-prompt-design).

## Code samples

The following code samples demonstrate how to invoke the Claude models to generate responses for varying types of input.

### Text-based generation

The following code sample shows how to generate a response from a text prompt along with a system instruction. System instruction is optional and you can pass it along with the prompt to instruct the model to behave in a specific manner.

#### Code sample
    
    
    DATA:
      lv_instruction TYPE string,
      lv_prompt      TYPE string.
    
    lv_instruction = 'SYSTEM_INSTRUCTIONS'.
    lv_prompt      = 'PROMPT'.
    
    TRY.
        DATA(lo_model) = NEW /goog/cl_model_claude( iv_model_key = 'MODEL_KEY' ).
    
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

The following code sample shows how to generate a response from a multimodal input, such as text and an image. You provide the input as a base64 encoded string. System instruction is optional and you can pass it along with the prompt to instruct the model to behave in a specific manner.

#### Code sample
    
    
    DATA:
    lv_instruction TYPE string,
    lv_prompt      TYPE string.
    
    lv_instruction = 'SYSTEM_INSTRUCTIONS'.
    lv_prompt      = 'PROMPT'.
    
    TRY.
        DATA(lo_model) = NEW /goog/cl_model_claude( iv_model_key = 'MODEL_KEY' ).
    
        DATA(lv_response) = lo_model->set_system_instructions( lv_instruction
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
  * `SYSTEM_INSTRUCTIONS`: Your [system instructions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/system-instructions) to the model.
  * `MIME_TYPE`: The IANA standard MIME type of the file data. By default, the MIME type is set to `application/pdf`.
  * `INLINE_DATA`: Base64-encoded raw data of the image or PDF to include inline in the prompt.



### Find number of tokens and billable characters in a prompt

Before invoking the model with a prompt, you might want to check the number of tokens in your prompt.

This helps you make informed decisions about your prompts and usage. There is no cost for the count-tokens endpoint. The following code sample shows how to find these numbers before actually invoking the API:

#### Code sample
    
    
    DATA:
      lv_prompt      TYPE string.
    
    lv_prompt      = 'PROMPT'.
    
    TRY.
        DATA(lo_model) = NEW /goog/cl_model_claude( iv_model_key = 'MODEL_KEY' ).
    
        DATA(lv_total_tokens) = lo_model->count_tokens( lv_prompt
                                      )->get_total_tokens( ).
    
    IF lv_total_tokens IS NOT INITIAL.
          cl_demo_output=>display( 'Total Tokens -' && lv_total_tokens ).
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

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
