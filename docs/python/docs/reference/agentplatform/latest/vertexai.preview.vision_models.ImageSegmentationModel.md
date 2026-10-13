---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.ImageSegmentationModel
title: Class ImageSegmentationModel (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:34.974987+00:00
---

# Class ImageSegmentationModel (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.ImageSegmentationModel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ImageSegmentationModel (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    ImageSegmentationModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Segments an image.

## Methods 

### ImageSegmentationModel
    
    
    ImageSegmentationModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

This constructor should not be called directly. Use `{model_class}.from_pretrained(model_name=...)` instead.

### from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If model_name is unknown.  
`ValueError` | If model does not support this class.  
  
### segment_image
    
    
    segment_image(
        base_image: vertexai.vision_models.Image,
        prompt: typing.Optional[str] = None,
        scribble: typing.Optional[vertexai.preview.vision_models.Scribble] = None,
        mode: typing.Literal[
            "foreground", "background", "semantic", "prompt", "interactive"
        ] = "foreground",
        max_predictions: typing.Optional[int] = None,
        confidence_threshold: typing.Optional[float] = 0.1,
        mask_dilation: typing.Optional[float] = None,
        binary_color_threshold: typing.Optional[float] = None,
    ) -> vertexai.preview.vision_models.ImageSegmentationResponse

Segments an image.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
