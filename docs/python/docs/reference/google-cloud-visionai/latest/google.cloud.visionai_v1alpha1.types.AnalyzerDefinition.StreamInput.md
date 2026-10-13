---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.AnalyzerDefinition.StreamInput
title: Class StreamInput (0.5.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:01.017156+00:00
---

# Class StreamInput (0.5.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-visionai/latest/google.cloud.visionai_v1alpha1.types.AnalyzerDefinition.StreamInput

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class StreamInput (0.5.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.3 (latest)  0.5.2  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    StreamInput(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The inputs to this analyzer.

We accept input name references of the following form: :

Example:

Suppose you had an operator named "SomeOp" that has 2 output arguments, the first of which is named "foo" and the second of which is named "bar", and an operator named "MyOp" that accepts 2 inputs.

Also suppose that there is an analyzer named "some-analyzer" that is running "SomeOp" and another analyzer named "my-analyzer" running "MyOp".

To indicate that "my-analyzer" is to consume "some-analyzer"'s "foo" output as its first input and "some-analyzer"'s "bar" output as its second input, you can set this field to the following: input = ["some-analyzer:foo", "some-analyzer:bar"]

## Attribute  
  
---  
**Name** | **Description**  
`input` |  `str`   
The name of the stream input (as discussed above).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
