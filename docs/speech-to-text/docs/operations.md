---
url: https://docs.cloud.google.com/speech-to-text/docs/operations/
title: Operations \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:42.229618+00:00
---

# Operations  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Reference ](https://docs.cloud.google.com/speech-to-text/docs/apis)



Send feedback 

#  Operations Stay organized with collections  Save and categorize content based on your preferences. 

For details on supported `google.longrunning` methods, see the [RPC](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.longrunning) and [REST](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v2/projects.locations.operations) documentation.

## ListOperations

To return V2 operations:

  * The RPC `Operations.ListOperations` [method](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.longrunning#google.longrunning.ListOperationsRequest) must be called with the `name` field set to `projects/<project>/locations/<speech location>`, with bracketed terms indicating variable text.

  * The `filter` field must be set to `is_v2(name)` (literally, including parentheses).




## Operation ID

All Cloud Speech-to-Text V2 operations have a `unique_id` in the `name` [field](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.longrunning#operation) that starts with `v2-`. This makes it possible to discern between Cloud Speech-to-Text V2 and V1 operations.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
