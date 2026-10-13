---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.MaskImageConfig
title: Class MaskImageConfig (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:35.747648+00:00
---

# Class MaskImageConfig (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.MaskImageConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MaskImageConfig (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    MaskImageConfig(
        mask_mode: typing.Literal[
            "MASK_MODE_DEFAULT",
            "MASK_MODE_USER_PROVIDED",
            "MASK_MODE_BACKGROUND",
            "MASK_MODE_FOREGROUND",
            "MASK_MODE_SEMANTIC",
        ],
        segmentation_classes: typing.Optional[typing.List[int]] = None,
        dilation: typing.Optional[float] = None,
    )

Mask image config.

## Attributes  
  
---  
**Name** | **Description**  
`mask_mode` |  `Literal['MASK_MODE_DEFAULT', 'MASK_MODE_USER_PROVIDED', 'MASK_MODE_BACKGROUND', 'MASK_MODE_FOREGROUND', 'MASK_MODE_SEMANTIC']`   
Mask mode for the image. Can take the following values: * MASK_MODE_DEFAULT: Default mask mode * MASK_MODE_USER_PROVIDED: User provided mask * MASK_MODE_BACKGROUND: Background mask * MASK_MODE_FOREGROUND: Foreground mask * MASK_MODE_SEMANTIC: Semantic mask   
`dilation` |  `Optional[float]`   
Dilation percentage of the mask provided. Float between 0 and 1. Defaults to 1.0   
`segmentation_classes` |  `Optional[List[int]]`   
List of class IDs for segmentation. Max of 5 IDs   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
