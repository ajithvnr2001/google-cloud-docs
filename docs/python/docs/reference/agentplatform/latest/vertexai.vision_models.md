---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models
title: Package vision_models (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:42.469429+00:00
---

# Package vision_models (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package vision_models (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 

API documentation for `vision_models` package.

## Classes 

### [GeneratedImage](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.GeneratedImage)

Generated image.

### [Image](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.Image)

Image.

### [ImageCaptioningModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.ImageCaptioningModel)

Generates captions from image.

Examples::
    
    
    model = ImageCaptioningModel.from_pretrained("imagetext@001")
    image = Image.load_from_file("image.png")
    captions = model.get_captions(
        image=image,
        # Optional:
        number_of_results=1,
        language="en",
    )
    

### [ImageGenerationModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.ImageGenerationModel)

Generates images from text prompt.

Examples::
    
    
    model = ImageGenerationModel.from_pretrained("imagegeneration@002")
    response = model.generate_images(
        prompt="Astronaut riding a horse",
        # Optional:
        number_of_images=1,
        seed=0,
    )
    response[0].show()
    response[0].save("image1.png")
    

### [ImageGenerationResponse](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.ImageGenerationResponse)

Image generation response.

### [ImageQnAModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.ImageQnAModel)

Answers questions about an image.

Examples::
    
    
    model = ImageQnAModel.from_pretrained("imagetext@001")
    image = Image.load_from_file("image.png")
    answers = model.ask_question(
        image=image,
        question="What color is the car in this image?",
        # Optional:
        number_of_results=1,
    )
    

### [ImageTextModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.ImageTextModel)

Generates text from images.

Examples::
    
    
    model = ImageTextModel.from_pretrained("imagetext@001")
    image = Image.load_from_file("image.png")
    
    captions = model.get_captions(
        image=image,
        # Optional:
        number_of_results=1,
        language="en",
    )
    
    answers = model.ask_question(
        image=image,
        question="What color is the car in this image?",
        # Optional:
        number_of_results=1,
    )
    

### [MultiModalEmbeddingModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.MultiModalEmbeddingModel)

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
    

### [MultiModalEmbeddingResponse](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.MultiModalEmbeddingResponse)

The multimodal embedding response.

### [Video](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.Video)

Video.

### [VideoEmbedding](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.VideoEmbedding)

Embeddings generated from video with offset times.

### [VideoSegmentConfig](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.VideoSegmentConfig)

The specific video segments (in seconds) the embeddings are generated for.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
