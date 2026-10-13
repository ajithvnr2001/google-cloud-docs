---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.PointwiseMetricPromptTemplate
title: Class PointwiseMetricPromptTemplate (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:08.089571+00:00
---

# Class PointwiseMetricPromptTemplate (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.PointwiseMetricPromptTemplate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PointwiseMetricPromptTemplate (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    PointwiseMetricPromptTemplate(
        *,
        criteria: typing.Dict[str, str],
        rating_rubric: typing.Dict[str, str],
        input_variables: typing.Optional[typing.List[str]] = None,
        instruction: typing.Optional[str] = None,
        metric_definition: typing.Optional[str] = None,
        evaluation_steps: typing.Optional[typing.Dict[str, str]] = None,
        few_shot_examples: typing.Optional[typing.List[str]] = None
    )

Pointwise metric prompt template for pointwise model-based metrics.

## Methods 

### PointwiseMetricPromptTemplate
    
    
    PointwiseMetricPromptTemplate(
        *,
        criteria: typing.Dict[str, str],
        rating_rubric: typing.Dict[str, str],
        input_variables: typing.Optional[typing.List[str]] = None,
        instruction: typing.Optional[str] = None,
        metric_definition: typing.Optional[str] = None,
        evaluation_steps: typing.Optional[typing.Dict[str, str]] = None,
        few_shot_examples: typing.Optional[typing.List[str]] = None
    )

Initializes a pointwise metric prompt template.

### __str__
    
    
    __str__()

Serializes the pointwise metric prompt template to a string.

### assemble
    
    
    assemble(**kwargs) -> vertexai.evaluation.prompt_template.PromptTemplate

Replaces only the provided variables in the template with specific values.

### get_default_pointwise_evaluation_steps
    
    
    get_default_pointwise_evaluation_steps() -> typing.Dict[str, str]

Returns the default evaluation steps for the metric prompt template.

### get_default_pointwise_instruction
    
    
    get_default_pointwise_instruction() -> str

Returns the default instruction for the metric prompt template.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
