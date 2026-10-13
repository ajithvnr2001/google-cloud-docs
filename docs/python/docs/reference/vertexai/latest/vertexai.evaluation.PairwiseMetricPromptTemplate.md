---
url: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai.evaluation.PairwiseMetricPromptTemplate
title: Class PairwiseMetricPromptTemplate (1.153.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:24.989676+00:00
---

# Class PairwiseMetricPromptTemplate (1.153.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai.evaluation.PairwiseMetricPromptTemplate

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PairwiseMetricPromptTemplate (1.153.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.153.1 (latest)  1.153.0  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0 
    
    
    PairwiseMetricPromptTemplate(
        *,
        criteria: typing.Dict[str, str],
        rating_rubric: typing.Dict[str, str],
        input_variables: typing.Optional[typing.List[str]] = None,
        instruction: typing.Optional[str] = None,
        metric_definition: typing.Optional[str] = None,
        evaluation_steps: typing.Optional[typing.Dict[str, str]] = None,
        few_shot_examples: typing.Optional[typing.List[str]] = None
    )

Pairwise metric prompt template for pairwise model-based metrics.

## Methods 

### PairwiseMetricPromptTemplate
    
    
    PairwiseMetricPromptTemplate(
        *,
        criteria: typing.Dict[str, str],
        rating_rubric: typing.Dict[str, str],
        input_variables: typing.Optional[typing.List[str]] = None,
        instruction: typing.Optional[str] = None,
        metric_definition: typing.Optional[str] = None,
        evaluation_steps: typing.Optional[typing.Dict[str, str]] = None,
        few_shot_examples: typing.Optional[typing.List[str]] = None
    )

Initializes a pairwise metric prompt template.

### __str__
    
    
    __str__()

Serializes the pairwise metric prompt template to a string.

### assemble
    
    
    assemble(**kwargs) -> vertexai.evaluation.prompt_template.PromptTemplate

Replaces only the provided variables in the template with specific values.

### get_default_pairwise_evaluation_steps
    
    
    get_default_pairwise_evaluation_steps() -> typing.Dict[str, str]

Returns the default evaluation steps for the metric prompt template.

### get_default_pairwise_instruction
    
    
    get_default_pairwise_instruction() -> str

Returns the default instruction for the metric prompt template.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
