---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals
title: Class DataStoreConnectionSignals (2.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:29:47.732213+00:00
---

# Class DataStoreConnectionSignals (2.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataStoreConnectionSignals (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.0 (latest)  2.7.0  2.6.0  2.1.0  2.0.0  1.43.0  1.42.0  1.41.1  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.1  1.33.0  1.32.1  1.31.1  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.1  1.19.0  1.18.0  1.17.1  1.16.0  1.15.0  1.14.1  1.13.5  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.2  1.2.0  1.1.1  1.0.0  0.8.2  0.7.1  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 
    
    
    DataStoreConnectionSignals(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Data store connection feature output signals. Might be only partially field if processing stop before the final answer. Reasons for this can be, but are not limited to: empty UCS search results, positive RAI check outcome, grounding failure, ...

## Attributes  
  
---  
**Name** | **Description**  
`rewriter_model_call_signals` |  `[google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.RewriterModelCallSignals](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.RewriterModelCallSignals)`   
Optional. Diagnostic info related to the rewriter model call.   
`rewritten_query` |  `str`   
Optional. Rewritten string query used for search.   
`search_snippets` |  `MutableSequence[[google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.SearchSnippet](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.SearchSnippet)]`   
Optional. Search snippets included in the answer generation prompt.   
`answer_generation_model_call_signals` |  `[google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.AnswerGenerationModelCallSignals](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.AnswerGenerationModelCallSignals)`   
Optional. Diagnostic info related to the answer generation model call.   
`answer` |  `str`   
Optional. The final compiled answer.   
`answer_parts` |  `MutableSequence[[google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.AnswerPart](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.AnswerPart)]`   
Optional. Answer parts with relevant citations. Concatenation of texts should add up the `answer` (not counting whitespaces).   
`cited_snippets` |  `MutableSequence[[google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.CitedSnippet](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.CitedSnippet)]`   
Optional. Snippets cited by the answer generation model from the most to least relevant.   
`grounding_signals` |  `[google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.GroundingSignals](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.GroundingSignals)`   
Optional. Grounding signals.   
`safety_signals` |  `[google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.SafetySignals](https://docs.cloud.google.com/python/docs/reference/dialogflow-cx/latest/google.cloud.dialogflowcx_v3.types.DataStoreConnectionSignals.SafetySignals)`   
Optional. Safety check result.   
  
## Classes 

### AnswerGenerationModelCallSignals
    
    
    AnswerGenerationModelCallSignals(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Diagnostic info related to the answer generation model call.

### AnswerPart
    
    
    AnswerPart(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Answer part with citation.

### CitedSnippet
    
    
    CitedSnippet(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Snippet cited by the answer generation model.

### GroundingSignals
    
    
    GroundingSignals(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Grounding signals.

### RewriterModelCallSignals
    
    
    RewriterModelCallSignals(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Diagnostic info related to the rewriter model call.

### SafetySignals
    
    
    SafetySignals(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Safety check results.

### SearchSnippet
    
    
    SearchSnippet(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Search snippet details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
