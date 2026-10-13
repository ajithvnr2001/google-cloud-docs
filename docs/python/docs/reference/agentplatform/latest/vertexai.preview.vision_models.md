---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models
title: Module vision_models (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:32.680562+00:00
---

# Module vision_models (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module vision_models (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 

Classes for working with vision models.

## Classes 

### [ControlImageConfig](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.ControlImageConfig)
    
    
    ControlImageConfig(
        control_type: typing.Literal[
            "CONTROL_TYPE_DEFAULT",
            "CONTROL_TYPE_SCRIBBLE",
            "CONTROL_TYPE_FACE_MESH",
            "CONTROL_TYPE_CANNY",
        ],
        enable_control_image_computation: typing.Optional[bool] = False,
    )

Control image config.

### [ControlReferenceImage](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.ControlReferenceImage)
    
    
    ControlReferenceImage(
        reference_id,
        image: typing.Optional[
            typing.Union[bytes, vertexai.vision_models.Image, str]
        ] = None,
        control_type: typing.Optional[
            typing.Literal["default", "scribble", "face_mesh", "canny"]
        ] = None,
        enable_control_image_computation: typing.Optional[bool] = False,
    )

Control reference image.

This encapsulates the control reference image type.

### [EntityLabel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.EntityLabel)
    
    
    EntityLabel(
        label: typing.Optional[str] = None, score: typing.Optional[float] = None
    )

Entity label holding a text label and any associated confidence score.

### [GeneratedImage](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.GeneratedImage)
    
    
    GeneratedImage(
        image_bytes: typing.Optional[bytes],
        generation_parameters: typing.Dict[str, typing.Any],
        gcs_uri: typing.Optional[str] = None,
    )

Generated image.

### [GeneratedMask](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.GeneratedMask)
    
    
    GeneratedMask(
        image_bytes: typing.Optional[bytes],
        gcs_uri: typing.Optional[str] = None,
        labels: typing.Optional[
            typing.List[vertexai.preview.vision_models.EntityLabel]
        ] = None,
    )

Generated image mask.

### [Image](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.Image)
    
    
    Image(
        image_bytes: typing.Optional[bytes] = None, gcs_uri: typing.Optional[str] = None
    )

Image.

### [ImageCaptioningModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.ImageCaptioningModel)
    
    
    ImageCaptioningModel(model_id: str, endpoint_name: typing.Optional[str] = None)

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
    

### [ImageGenerationModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.ImageGenerationModel)
    
    
    ImageGenerationModel(model_id: str, endpoint_name: typing.Optional[str] = None)

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
    

### [ImageGenerationResponse](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.ImageGenerationResponse)
    
    
    ImageGenerationResponse(images: typing.List[GeneratedImage])

Image generation response.

### [ImageQnAModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.ImageQnAModel)
    
    
    ImageQnAModel(model_id: str, endpoint_name: typing.Optional[str] = None)

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
    

### [ImageSegmentationModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.ImageSegmentationModel)
    
    
    ImageSegmentationModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Segments an image.

### [ImageSegmentationResponse](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.ImageSegmentationResponse)
    
    
    ImageSegmentationResponse(
        _prediction_response: typing.Any,
        masks: typing.List[vertexai.preview.vision_models.GeneratedMask],
    )

Image Segmentation response.

### [ImageTextModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.ImageTextModel)
    
    
    ImageTextModel(model_id: str, endpoint_name: typing.Optional[str] = None)

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
    

### [MaskImageConfig](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.MaskImageConfig)
    
    
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

### [MaskReferenceImage](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.MaskReferenceImage)
    
    
    MaskReferenceImage(
        reference_id,
        image: typing.Optional[
            typing.Union[bytes, vertexai.vision_models.Image, str]
        ] = None,
        mask_mode: typing.Optional[
            typing.Literal[
                "default", "user_provided", "background", "foreground", "semantic"
            ]
        ] = None,
        dilation: typing.Optional[float] = None,
        segmentation_classes: typing.Optional[typing.List[int]] = None,
    )

Mask reference image. This encapsulates the mask reference image type.

### [MultiModalEmbeddingModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.MultiModalEmbeddingModel)
    
    
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
    

### [MultiModalEmbeddingResponse](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.MultiModalEmbeddingResponse)
    
    
    MultiModalEmbeddingResponse(
        _prediction_response: typing.Any,
        image_embedding: typing.Optional[typing.List[float]] = None,
        video_embeddings: typing.Optional[
            typing.List[vertexai.vision_models.VideoEmbedding]
        ] = None,
        text_embedding: typing.Optional[typing.List[float]] = None,
    )

The multimodal embedding response.

### [RawReferenceImage](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.RawReferenceImage)
    
    
    RawReferenceImage(
        reference_id,
        image: typing.Optional[
            typing.Union[bytes, vertexai.vision_models.Image, str]
        ] = None,
    )

Raw reference image.

This encapsulates the raw reference image type.

### [ReferenceImage](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.ReferenceImage)
    
    
    ReferenceImage(
        reference_id,
        image: typing.Optional[
            typing.Union[bytes, vertexai.vision_models.Image, str]
        ] = None,
    )

Reference image.

This is a new base API object for Imagen 3.0 Capabilities.

### [Scribble](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.Scribble)
    
    
    Scribble(image_bytes: typing.Optional[bytes], gcs_uri: typing.Optional[str] = None)

Input scribble for image segmentation.

### [StyleImageConfig](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.StyleImageConfig)
    
    
    StyleImageConfig(style_description: str)

Style image config.

### [StyleReferenceImage](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.StyleReferenceImage)
    
    
    StyleReferenceImage(
        reference_id,
        image: typing.Optional[
            typing.Union[bytes, vertexai.vision_models.Image, str]
        ] = None,
        style_description: typing.Optional[str] = None,
    )

Style reference image. This encapsulates the style reference image type.

### [SubjectImageConfig](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.SubjectImageConfig)
    
    
    SubjectImageConfig(
        subject_description: str,
        subject_type: typing.Literal[
            "SUBJECT_TYPE_DEFAULT",
            "SUBJECT_TYPE_PERSON",
            "SUBJECT_TYPE_ANIMAL",
            "SUBJECT_TYPE_PRODUCT",
        ],
    )

Subject image config.

### [SubjectReferenceImage](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.SubjectReferenceImage)
    
    
    SubjectReferenceImage(
        reference_id,
        image: typing.Optional[
            typing.Union[bytes, vertexai.vision_models.Image, str]
        ] = None,
        subject_description: typing.Optional[str] = None,
        subject_type: typing.Optional[
            typing.Literal["default", "person", "animal", "product"]
        ] = None,
    )

Subject reference image.

This encapsulates the subject reference image type.

### [Video](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.Video)
    
    
    Video(
        video_bytes: typing.Optional[bytes] = None, gcs_uri: typing.Optional[str] = None
    )

Video.

### [VideoEmbedding](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.VideoEmbedding)
    
    
    VideoEmbedding(
        start_offset_sec: int, end_offset_sec: int, embedding: typing.List[float]
    )

Embeddings generated from video with offset times.

### [VideoSegmentConfig](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.VideoSegmentConfig)
    
    
    VideoSegmentConfig(
        start_offset_sec: int = 0, end_offset_sec: int = 120, interval_sec: int = 16
    )

The specific video segments (in seconds) the embeddings are generated for.

### [WatermarkVerificationModel](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.WatermarkVerificationModel)
    
    
    WatermarkVerificationModel(
        model_id: str, endpoint_name: typing.Optional[str] = None
    )

Verifies if an image has a watermark.

### [WatermarkVerificationResponse](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.vision_models.WatermarkVerificationResponse)
    
    
    WatermarkVerificationResponse(
        _prediction_response: Any, watermark_verification_result: Optional[str] = None
    )

WatermarkVerificationResponse(_prediction_response: Any, watermark_verification_result: Optional[str] = None)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
