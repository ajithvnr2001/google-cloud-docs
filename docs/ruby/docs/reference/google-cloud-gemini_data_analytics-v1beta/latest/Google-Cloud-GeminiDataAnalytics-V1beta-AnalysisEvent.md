---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AnalysisEvent/
title: Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::AnalysisEvent (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:57.731502+00:00
---

# Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::AnalysisEvent (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-AnalysisEvent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::AnalysisEvent (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API class Google::Cloud::GeminiDataAnalytics::V1beta::AnalysisEvent.

An event indicating the progress of an analysis.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #code
    
    
    def code() -> ::String

**Returns**

  * (::String) — Generated code.

Note: The following fields are mutually exclusive: `code`, `planner_reasoning`, `coder_instruction`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #code=
    
    
    def code=(value) -> ::String

**Parameter**

  * **value** (::String) — Generated code.

Note: The following fields are mutually exclusive: `code`, `planner_reasoning`, `coder_instruction`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Generated code.

Note: The following fields are mutually exclusive: `code`, `planner_reasoning`, `coder_instruction`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #coder_instruction
    
    
    def coder_instruction() -> ::String

**Returns**

  * (::String) — Instructions issued for code generation.

Note: The following fields are mutually exclusive: `coder_instruction`, `planner_reasoning`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #coder_instruction=
    
    
    def coder_instruction=(value) -> ::String

**Parameter**

  * **value** (::String) — Instructions issued for code generation.

Note: The following fields are mutually exclusive: `coder_instruction`, `planner_reasoning`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Instructions issued for code generation.

Note: The following fields are mutually exclusive: `coder_instruction`, `planner_reasoning`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #error
    
    
    def error() -> ::String

**Returns**

  * (::String) — A generic error message.

Note: The following fields are mutually exclusive: `error`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #error=
    
    
    def error=(value) -> ::String

**Parameter**

  * **value** (::String) — A generic error message.

Note: The following fields are mutually exclusive: `error`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — A generic error message.

Note: The following fields are mutually exclusive: `error`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #execution_error
    
    
    def execution_error() -> ::String

**Returns**

  * (::String) — An error from code execution.

Note: The following fields are mutually exclusive: `execution_error`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #execution_error=
    
    
    def execution_error=(value) -> ::String

**Parameter**

  * **value** (::String) — An error from code execution.

Note: The following fields are mutually exclusive: `execution_error`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — An error from code execution.

Note: The following fields are mutually exclusive: `execution_error`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #execution_output
    
    
    def execution_output() -> ::String

**Returns**

  * (::String) — Output from code execution.

Note: The following fields are mutually exclusive: `execution_output`, `planner_reasoning`, `coder_instruction`, `code`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #execution_output=
    
    
    def execution_output=(value) -> ::String

**Parameter**

  * **value** (::String) — Output from code execution.

Note: The following fields are mutually exclusive: `execution_output`, `planner_reasoning`, `coder_instruction`, `code`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Output from code execution.

Note: The following fields are mutually exclusive: `execution_output`, `planner_reasoning`, `coder_instruction`, `code`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #planner_reasoning
    
    
    def planner_reasoning() -> ::String

**Returns**

  * (::String) — Python codegen planner's reasoning.

Note: The following fields are mutually exclusive: `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #planner_reasoning=
    
    
    def planner_reasoning=(value) -> ::String

**Parameter**

  * **value** (::String) — Python codegen planner's reasoning.

Note: The following fields are mutually exclusive: `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Python codegen planner's reasoning.

Note: The following fields are mutually exclusive: `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #result_csv_data
    
    
    def result_csv_data() -> ::String

**Returns**

  * (::String) — Result as CSV string.

Note: The following fields are mutually exclusive: `result_csv_data`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #result_csv_data=
    
    
    def result_csv_data=(value) -> ::String

**Parameter**

  * **value** (::String) — Result as CSV string.

Note: The following fields are mutually exclusive: `result_csv_data`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Result as CSV string.

Note: The following fields are mutually exclusive: `result_csv_data`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #result_natural_language
    
    
    def result_natural_language() -> ::String

**Returns**

  * (::String) — Result as NL string.

Note: The following fields are mutually exclusive: `result_natural_language`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #result_natural_language=
    
    
    def result_natural_language=(value) -> ::String

**Parameter**

  * **value** (::String) — Result as NL string.

Note: The following fields are mutually exclusive: `result_natural_language`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Result as NL string.

Note: The following fields are mutually exclusive: `result_natural_language`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #result_reference_data
    
    
    def result_reference_data() -> ::String

**Returns**

  * (::String) — Result as a reference to a data source.

Note: The following fields are mutually exclusive: `result_reference_data`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #result_reference_data=
    
    
    def result_reference_data=(value) -> ::String

**Parameter**

  * **value** (::String) — Result as a reference to a data source.

Note: The following fields are mutually exclusive: `result_reference_data`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Result as a reference to a data source.

Note: The following fields are mutually exclusive: `result_reference_data`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_vega_chart_json`, `result_natural_language`, `result_csv_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #result_vega_chart_json
    
    
    def result_vega_chart_json() -> ::String

**Returns**

  * (::String) — Result as Vega chart JSON string.

Note: The following fields are mutually exclusive: `result_vega_chart_json`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #result_vega_chart_json=
    
    
    def result_vega_chart_json=(value) -> ::String

**Parameter**

  * **value** (::String) — Result as Vega chart JSON string.

Note: The following fields are mutually exclusive: `result_vega_chart_json`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Result as Vega chart JSON string.

Note: The following fields are mutually exclusive: `result_vega_chart_json`, `planner_reasoning`, `coder_instruction`, `code`, `execution_output`, `execution_error`, `result_natural_language`, `result_csv_data`, `result_reference_data`, `error`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
