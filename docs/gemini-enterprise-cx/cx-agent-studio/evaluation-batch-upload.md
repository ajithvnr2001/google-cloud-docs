---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation-batch-upload/
title: Evaluation batch upload \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:04.253923+00:00
---

# Evaluation batch upload  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation-batch-upload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Evaluation batch upload Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the format required to upload **golden evaluations** in a CSV file. For details about golden evaluations, see the [golden evaluations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#golden) documentation.

## Download the template

  * Navigate to the **Evaluate** tab and click **\+ Add test case - > Golden**.
  * In the menu that appears, click **Download template**.
  * After you have used the template to create a CSV file containing your golden evaluations, you can upload it by clicking **Upload file** in the same menu.



## General structure

  * A single CSV file can contain multiple evaluations. Each evaluation can span multiple rows.
  * The first row of an evaluation is the **evaluation row** and defines its overall properties (name and metadata).
  * Each subsequent row is a **conversation row** and defines a single conversation turn in the evaluation (for example, an end-user says something, the agent is expected to reply, or a tool call is expected).
  * You can start a new test case by providing a new name in the `display_name` column. Each new `display_name` value defines the start of a new evaluation.



## Header row

Your CSV file must have a header row as the first line. This header defines the a data variable in each column. All variables other than the required variables are optional, unless required by an [`action_type` value](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation-batch-upload#required_header_variables). Optional variable columns can be in any order after the required variables.

  * **Required variables** : `display_name`, `turn_index`, `action_type`.



## Define a conversation evaluation

Each new evaluation starts at an **evaluation row**. Each **conversation row** below the evaluation row corresponds to one conversation turn, until the next evaluation row.

### Evaluation row

The first line after the header row must be an **evaluation row**. Each evaluation row defines a new evaluation.

  * **Required:** Enter a unique, human-readable name for the evaluation in the `display_name` field.
  * **Optional:** You can optionally add any [metadata variable data](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation-batch-upload#metadata_variables) in this row.



### Conversation row

Each row corresponds to data from one conversation turn.

  * **Required:** Enter values in the `turn_index` and `action_type` fields. `display_name` must be left blank.
  * **Optional:** Enter values for any header columns other than [metadata variables](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation-batch-upload#metadata_variables) or `display_name`.



## Variables

**Note:** For variables requiring `JSON`, you must provide a valid `JSON` object as a string. Example: `{"param_name": "param_value", "number_param": 123}`.

The following tables describe the available data variables. All variables other than the required variables are optional, unless required by an `action_type` value. All variables must be defined in the header row, one per column. Optional variable columns can be in any order after the required columns.

### Required header variables

Column name | Description  
---|---  
`display_name` | The human-readable name of your evaluation. This is only filled in for the first row of a new evaluation. Each new `display_name` value defines a new evaluation.  
`turn_index` | A number (1, 2, 3...) indicating the sequential order of the conversation turn. All rows in one turn share the index value. Values must start at 1 for each evaluation. Each subsequent row must have the same or greater value than the row preceding it.  
`action_type` | Specifies what this row's data represents. Each value has optional variable values that must be also filled (as indicated) in order for the conversation turn to input correctly. Input value must be one of the following:  
  
`INPUT_TEXT`: An end-user text input.  
\- (Required) `text_content`.  
  
`INPUT_IMAGE`: An end-user image input.  
\- (Required) `image_mime_type`, `image_content`.  
  
`INPUT_TOOL_RESPONSE`: A tool response input.  
\- (Required) `tool_name`.  
\- (Optional) `tool_response_json`.  
  
`INPUT_UPDATED_VARIABLES`: Update variables from an input.  
\- (Required) `updated_variables_json`  
  
`EXPECTATION_TEXT`: Expected output from an agent text response.  
\- (Required) `response_agent`, `text_content`.  
\- (Optional) `expectation_note`.  
  
`EXPECTATION_TOOL_CALL`: Expected tool call.  
\- (Required) `tool_name`.  
\- (Optional) `tool_call_args_json`, `expectation_note`.  
  
`EXPECTATION_TOOL_RESPONSE`: Expected tool response.  
\- (Required) `tool_name`.  
\- (Optional) `expectation_note`.  
  
`EXPECTATION_AGENT_TRANSFER`: Expected agent transfer.  
\- (Required) `agent_transfer_target`.  
\- (Optional) `expectation_note`.  
  
### Metadata variables

Column name | Description  
---|---  
`evaluation_id` | A unique ID for the evaluation. Each `evaluation_id` value must be unique to your Customer Experience Agent Studio agent. If no value is entered manually in this column, a unique ID will be generated automatically.  
`description` | Free-text notes or a description of the evaluation's purpose.  
`tags` | Semicolon-separated tags for organizing evaluations (for example, "tag1;tag2").  
`evaluation_groups` | Semicolon-separated names of any evaluation groups that the evaluation belongs to (for example, "group name 1;group name 2"). Any `evaluation_groups` values entered in this column but not defined in the header will be ignored.  
  
### Conversation turn variables

Column name | Description  
---|---  
`response_agent` | Name of the agent that provided the response. Expected only for `EXPECTATION_TEXT`.  
`text_content` | The text for `INPUT_TEXT` or `EXPECTATION_TEXT`.  
`image_mime_type` | The IANA standard MIME type of the source image. Supported values: `image/png`, `image/jpeg`, `image/webp`, `image/heic`, `image/heif`.  
`image_content` | Bytes string of the `INPUT_IMAGE`.  
`tool_name` | The `display_name` for the tool being called or responding. Expected for `INPUT_TOOL_RESPONSE,EXPECTATION_TOOL_CALL` or `EXPECTATION_TOOL_RESPONSE`.  
`tool_call_args_json` | The JSON arguments for an `EXPECTATION_TOOL_CALL`.  
`tool_response_json` | The JSON content of an `INPUT_TOOL_RESPONSE`.  
`updated_variables_json` | The JSON content for `INPUT_UPDATED_VARIABLES`.  
`agent_transfer_target` | Display name of the target agent for an `EXPECTATION_AGENT_TRANSFER`.  
`expectation_note` | Note or description of the expectation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
