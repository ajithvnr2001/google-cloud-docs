---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/export/
title: Export format reference \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:03.722041+00:00
---

# Export format reference  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Export format reference Stay organized with collections  Save and categorize content based on your preferences. 

This document outlines the directory structure and file organization for an agent application export and import file.

The format is a zip file that when extracted contains a _root directory_ that corresponds to the agent application name.

All paths described in this document are relative to the root directory. All references to other objects (agents, tools, and so on) must use their `displayName` values.

The following tool names are reserved:

  * `end_session`
  * `transfer_to_agent`
  * `customize_response`



When importing and exporting, you can use either JSON or YAML for the individual files. The files described in this document use YAML, but the JSON members are similar.

## Root Directory

The root directory contains the main configuration files for the application:

  * **`app.yaml`** : The central configuration file for the agent application. It defines: 
    * `displayName` (string): The human-readable name of the application.
    * `rootAgent` (string): The **Display Name** of the agent that starts the conversation. Don't use the filename or directory name.
    * `audioProcessingConfig` (object): Settings for text-to-speech and speech-to-text. 
      * `synthesizeSpeechConfigs` (map): Keys are locale codes (for example, `en-US`), values are objects containing `voice` (string).
      * `inactivityTimeout` (string): Duration string (for example, "2s").
      * `ambientSoundConfig` (object): Configures background noise, containing `volumeGainDb` (float) and `prebuiltAmbientSound` (string).
    * `loggingSettings` (object): Configuration for logs and recording. 
      * `redactionConfig` (object): Config for redacting sensitive info.
      * `audioRecordingConfig` (object): Contains `gcsBucket` (string).
      * `bigqueryExportSettings` (object): Contains `enabled` (boolean), `project` (string), `dataset` (string).
      * `cloudLoggingSettings` (object): Contains `enableCloudLogging` (boolean).
    * `guardrails` (list of strings): A list of guardrail names applied globally.
    * `variableDeclarations` (list of objects): Schema definitions for global variables. Each object contains: 
      * `name` (string): Variable name.
      * `description` (string): Explanation of the variable's purpose.
      * `schema` (object): Type definition (for example, `{ type: STRING }` or nested properties).
      * `default` (any): The default value for the variable.
    * `globalInstruction` (string): Path to the global system instruction file.
    * `languageSettings` (object): 
      * `defaultLanguageCode` (string): for example, "en-US".
      * `supportedLanguageCodes` (list of strings): for example, `["fr", "es"]`.
      * `enableMultilingualSupport` (boolean).
  * **`environment.json`** : Key-value pairs for environment-specific variables.
  * **`global_instruction.txt`** : A text file containing the primary prompt/instruction.



## `agents/`

This directory contains the definitions for all agents in the application.

### Agent Structure (`agents/<agent_name>/`)

  * **`<agent_name>.yaml`**: The configuration file for the specific agent. 
    * `displayName` (string): The agent's name.
    * `modelSettings` (object): Contains `model` (string).
    * `instruction` (string): Path to the instruction file relative to the root (for example, `agents/<agent_name>/instruction.txt`).
    * `tools` (list of strings): Display Names of local tools available to this agent.
    * `toolsets` (list of objects): OpenAPI toolsets available to this agent. Each object contains: 
      * `toolset` (string): The name of the toolset.
      * `toolIds` (list of strings): Specific operation IDs to expose from that toolset.
    * `childAgents` (list of strings): Display names of other agents this agent can transition to. This relationship is unidirectional (parent to child); child agents shouldn't list their parents as children unless a circular transition is explicitly intended. Agents cannot have more than one parent (exception: shared utility agents like Escalation or Satisfaction). The Root Agent cannot be listed as a child of any other agent.
    * `*Callbacks` (list of objects): Used for `beforeModelCallbacks`, `afterModelCallbacks`, and so on. Each object contains: 
      * `pythonCode` (string): Path to the callback script.
      * `disabled` (boolean): Whether the callback is active.
      * `description` (string): Description of the callback's logic.
  * **`instruction.txt`** : The specific system prompt for this agent. References to tools must use the syntax `{@TOOL: <tool_display_name>}`, references to other agents must use `{@AGENT: <agent_display_name>}`, and variables must be accessed using `{variable_name}` (for example, `{firstname}`).
  * **`before_model_callbacks/`** , and so on: Directories for callback scripts.



## `tools/`

This directory contains "local" tools, which can be either Python functions or Data Store retrievers.

### Tool Structure (`tools/<tool_name>/`)

  * **`<tool_name>.yaml`**: Configuration for the tool. Use **EITHER** `pythonFunction` OR `dataStoreTool`, not both. 
    * `displayName` (string): The name of the tool.
    * **Option A: Python Function Tool**
      * `pythonFunction` (object): 
        * `name` (string): The function name.
        * `pythonCode` (string): Path to the Python implementation relative to the root (for example, `tools/<tool_name>/python_function/python_code.py`).
        * `description` (string): Semantic description for the LLM.
    * **Option B: Data Store Tool**
      * `dataStoreTool` (object): 
        * `name` (string): The tool name (usually matches the directory name).
        * `description` (string): Description of the tool's purpose for the agent.
        * `engineSource` (object): 
          * `dataStoreSources` (list of objects): 
            * `dataStore` (object): 
              * `name` (string): The full resource name of the data store (for example, `projects/...`) or an environment variable (for example, `$env_var`).
        * `modalityConfigs` (list of objects): Optional. Configures behavior for TEXT or AUDIO. 
          * `modalityType` (enum): `TEXT` or `AUDIO`.
          * `groundingConfig` (object): 
            * `groundingLevel` (float): for example, 4.0.
    * `executionType` (enum): for example, `SYNCHRONOUS`.
  * **`python_function/python_code.py`** : The Python code file (only for Python Function Tools).



## `toolsets/`

This directory contains OpenAPI-based toolsets.

### Toolset Structure (`toolsets/<toolset_name>/`)

  * **`<toolset_name>.yaml`**: Configuration for the toolset. 
    * `displayName` (string): Name of the toolset.
    * `openApiToolset` (object): 
      * `openApiSchema` (string): Path to the OpenAPI schema file relative to the root (for example, `toolsets/<toolset_name>/open_api_toolset/open_api_schema.yaml`).
      * `apiAuthentication` (object): Authentication config (for example, `serviceAgentIdTokenAuthConfig`).
  * **`open_api_toolset/open_api_schema.yaml`** : The OpenAPI specification file.



## `guardrails/`

This directory defines content safety filters.

### Guardrail Structure (`guardrails/<guardrail_name>/`)

  * **`<guardrail_name>.yaml`**: 
    * `displayName` (string): Name of the guardrail.
    * `description` (string): Purpose.
    * `enabled` (boolean): Whether it is active.
    * `contentFilter` (object): 
      * `bannedContentsInUserInput` (list of strings): Words and phrases to block.
      * `matchType` (string): for example, "WORD_BOUNDARY_STRING_MATCH".
    * `action` (object): 
      * `respondImmediately` (object): 
        * `responses` (list of objects): Each object contains `text` (string).



## `examples/`

This directory contains the definitions for few-shot examples used in the agent application.

### Example Structure (`examples/<example_name>/`)

  * **`<example_name>.yaml`**: Configuration for the example.



## `evaluations/`

This directory contains test definitions.

### Evaluation Structure (`evaluations/<evaluation_name>/`)

  * **`<evaluation_name>.yaml`**: Defines test scenarios with expected inputs/outputs.



## `evaluationDatasets/`

This directory contains evaluation datasets.

### Evaluation Dataset Structure (`evaluationDatasets/<evaluation_dataset_name>/`)

  * **`<evaluation_dataset_name>.yaml`**: Configuration for the evaluation dataset.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
