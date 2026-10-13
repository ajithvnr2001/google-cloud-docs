---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.types.QueryDataResponse
title: Class QueryDataResponse (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:59:32.772014+00:00
---

# Class QueryDataResponse (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.types.QueryDataResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class QueryDataResponse (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    QueryDataResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Response containing the generated query and related information.

## Attributes  
  
---  
**Name** | **Description**  
`generated_query` |  `str`   
Generated query for the given user prompt.   
`intent_explanation` |  `str`   
A natural language explanation of the generated query. Populated if options.generate_explanation was true in the request.   
`query_result` |  `[google.cloud.geminidataanalytics_v1beta.types.ExecutedQueryResult](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.types.ExecutedQueryResult)`   
The result of executing the query. Populated if options.generate_query_result or options.generate_natural_language_answer was true in the request, and execution was successful or attempted.   
`natural_language_answer` |  `str`   
A natural language answer to the query, based on the query_result. Populated if options.generate_natural_language_answer was true in the request and query execution was successful based in the response from executeSql API.   
`disambiguation_question` |  `MutableSequence[str]`   
If ambiguity was detected in the natural language query and options.generate_disambiguation_question was true, this field contains a question to the user for clarification. The returned represents the service's best effort based on the ambiguous input.   
`pipeline_debug_info` |  `google.protobuf.struct_pb2.Struct`   
Detailed step-by-step pipeline execution information. Populated only if generation_options.generate_debug_info was true. Provided for debugging and transparency purposes only. The structure and content of this object is not guaranteed and may change at any time without notice. Do not write production code or business logic depending on the fields in this object.   
`token_usage` |  `[google.cloud.geminidataanalytics_v1beta.types.TokenUsage](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1beta.types.TokenUsage)`   
Overall token usage for the request.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
