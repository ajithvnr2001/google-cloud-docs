---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.MultiModalEmbeddingModel
title: Class MultiModalEmbeddingModel (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:44.249540+00:00
---

# Class MultiModalEmbeddingModel (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.MultiModalEmbeddingModel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class MultiModalEmbeddingModel (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    MultiModalEmbeddingModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Generates embedding vectors from images and videos.

Examples::
    
    
    model = MultiModalEmbeddingModel.from_pretrained("multimodalembedding@001")
    image = Image.load_from_file("image.png")
    video = Video.load_from_file("video.mp4")
    
    embeddings = model.get_embeddings(
        image=image,
        video=video,
        contextual_text="Hello world",
    )
    image_embedding = embeddings.image_embedding
    video_embeddings = embeddings.video_embeddings
    text_embedding = embeddings.text_embedding
    

## Methods 

### MultiModalEmbeddingModel
    
    
    MultiModalEmbeddingModel(model_id: str, endpoint_name: typing.Optional[str] = None)

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
  
### get_embeddings
    
    
    get_embeddings(
        image: typing.Optional[vertexai.vision_models.Image] = None,
        video: typing.Optional[vertexai.vision_models.Video] = None,
        contextual_text: typing.Optional[str] = None,
        dimension: typing.Optional[int] = None,
        video_segment_config: typing.Optional[
            vertexai.vision_models.VideoSegmentConfig
        ] = None,
    ) -> vertexai.vision_models.MultiModalEmbeddingResponse

Gets embedding vectors from the provided image.

**Parameters**  
---  
**Name** | **Description**  
`image` |  `Image`   
Optional. The image to generate embeddings for. One of `image`, `video`, or `contextual_text` is required.  
`video` |  `Video`   
Optional. The video to generate embeddings for. One of `image`, `video` or `contextual_text` is required.  
`contextual_text` |  `str`   
Optional. Contextual text for your input image or video. If provided, the model will also generate an embedding vector for the provided contextual text. The returned image and text embedding vectors are in the same semantic space with the same dimensionality, and the vectors can be used interchangeably for use cases like searching image by text or searching text by image. One of `image`, `video` or `contextual_text` is required.  
`dimension` |  `int`   
Optional. The number of embedding dimensions. Lower values offer decreased latency when using these embeddings for subsequent tasks, while higher values offer better accuracy. Available values: `128`, `256`, `512`, and `1408` (default).  
`video_segment_config` |  `VideoSegmentConfig`   
Optional. The specific video segments (in seconds) the embeddings are generated for.  
**Returns**  
---  
**Type** | **Description**  
`MultiModalEmbeddingResponse` | The image and text embedding vectors.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
