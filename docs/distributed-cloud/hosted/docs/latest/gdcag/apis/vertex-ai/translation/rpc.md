---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/
title: Vertex AI Translation API \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:49:50.785502+00:00
---

# Vertex AI Translation API  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  Vertex AI Translation API Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes the Vertex AI Translation API.

## Service: {TRANSLATION_GDC_ENDPOINT}

The Service name `{TRANSLATION_GDC_ENDPOINT}` is needed to create RPC client stubs.

## `[google.cloud.translation.v3.TranslationService](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslationService)`

Methods  
---  
``[CreateGlossary](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslationService.CreateGlossary)`` |  Creates a glossary and returns the long-running operation.  
``[DeleteGlossary](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslationService.DeleteGlossary)`` |  Deletes a glossary if the glossary hasn't been created.  
``[DetectLanguage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslationService.DetectLanguage)`` |  Detects the language of text within a request.  
``[GetGlossary](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslationService.GetGlossary)`` |  Gets a glossary.  
``[GetSupportedLanguages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslationService.GetSupportedLanguages)`` |  Returns a list of supported languages for translation.  
``[ListGlossaries](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslationService.ListGlossaries)`` |  Lists glossaries in a project.  
``[TranslateDocument](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslationService.TranslateDocument)`` |  Translates documents in synchronous mode.  
``[BatchTranslateDocument](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3beta1#google.cloud.translation.v3beta1.TranslationService.BatchTranslateDocument)`` |  Translates a large volume of document in asynchronous batch mode.  
``[TranslateText](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.cloud.translation.v3#google.cloud.translation.v3.TranslationService.TranslateText)`` |  Translates input text and returns translated text.  
  
## `[google.longrunning.Operations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operations)`

Methods  
---  
``[DeleteOperation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operations.DeleteOperation)`` |  Deletes a long-running operation.  
``[GetOperation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operations.GetOperation)`` |  Gets the latest state of a long-running operation.  
``[ListOperations](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/vertex-ai/translation/rpc/google.longrunning#google.longrunning.Operations.ListOperations)`` |  Lists operations that match the specified filter in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-10 UTC."],[],[]] 
