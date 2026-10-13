---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.Rouge
title: Class Rouge (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:08.685064+00:00
---

# Class Rouge (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.Rouge

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Rouge (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    Rouge(
        *,
        rouge_type: typing.Literal[
            "rouge1",
            "rouge2",
            "rouge3",
            "rouge4",
            "rouge5",
            "rouge6",
            "rouge7",
            "rouge8",
            "rouge9",
            "rougeL",
            "rougeLsum",
        ],
        use_stemmer: bool = False,
        split_summaries: bool = False
    )

The ROUGE Metric.

Calculates the recall of n-grams in prediction as compared to reference and returns a score ranging between 0 and 1. Supported rouge types are rougen[1-9], rougeL, and rougeLsum.

## Methods 

### Rouge
    
    
    Rouge(
        *,
        rouge_type: typing.Literal[
            "rouge1",
            "rouge2",
            "rouge3",
            "rouge4",
            "rouge5",
            "rouge6",
            "rouge7",
            "rouge8",
            "rouge9",
            "rougeL",
            "rougeLsum",
        ],
        use_stemmer: bool = False,
        split_summaries: bool = False
    )

Initializes the ROUGE metric.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
