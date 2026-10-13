---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.ImageGenerationModel
title: Class ImageGenerationModel (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:42.913547+00:00
---

# Class ImageGenerationModel (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models.ImageGenerationModel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ImageGenerationModel (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
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
    

## Methods 

### ImageGenerationModel
    
    
    ImageGenerationModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

This constructor should not be called directly. Use `{model_class}.from_pretrained(model_name=...)` instead.

### edit_image
    
    
    edit_image(
        *,
        prompt: str,
        base_image: typing.Optional[vertexai.vision_models.Image] = None,
        mask: typing.Optional[vertexai.vision_models.Image] = None,
        reference_images: typing.Optional[
            typing.List[vertexai.vision_models.ReferenceImage]
        ] = None,
        negative_prompt: typing.Optional[str] = None,
        number_of_images: int = 1,
        guidance_scale: typing.Optional[float] = None,
        edit_mode: typing.Optional[
            typing.Literal[
                "inpainting-insert", "inpainting-remove", "outpainting", "product-image"
            ]
        ] = None,
        mask_mode: typing.Optional[
            typing.Literal["background", "foreground", "semantic"]
        ] = None,
        segmentation_classes: typing.Optional[typing.List[str]] = None,
        mask_dilation: typing.Optional[float] = None,
        product_position: typing.Optional[typing.Literal["fixed", "reposition"]] = None,
        output_mime_type: typing.Optional[typing.Literal["image/png", "image/jpeg"]] = None,
        compression_quality: typing.Optional[float] = None,
        language: typing.Optional[str] = None,
        seed: typing.Optional[int] = None,
        output_gcs_uri: typing.Optional[str] = None,
        safety_filter_level: typing.Optional[
            typing.Literal["block_most", "block_some", "block_few", "block_fewest"]
        ] = None,
        person_generation: typing.Optional[
            typing.Literal["dont_allow", "allow_adult", "allow_all"]
        ] = None
    ) -> vertexai.preview.vision_models.ImageGenerationResponse

Edits an existing image based on text prompt.

### from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If model_name is unknown.  
`ValueError` | If model does not support this class.  
  
### generate_images
    
    
    generate_images(
        prompt: str,
        *,
        negative_prompt: typing.Optional[str] = None,
        number_of_images: int = 1,
        aspect_ratio: typing.Optional[
            typing.Literal["1:1", "9:16", "16:9", "4:3", "3:4"]
        ] = None,
        guidance_scale: typing.Optional[float] = None,
        language: typing.Optional[str] = None,
        seed: typing.Optional[int] = None,
        output_gcs_uri: typing.Optional[str] = None,
        add_watermark: typing.Optional[bool] = True,
        safety_filter_level: typing.Optional[
            typing.Literal["block_most", "block_some", "block_few", "block_fewest"]
        ] = None,
        person_generation: typing.Optional[
            typing.Literal["dont_allow", "allow_adult", "allow_all"]
        ] = None
    ) -> vertexai.preview.vision_models.ImageGenerationResponse

Generates images from text prompt.

### upscale_image
    
    
    upscale_image(
        image: typing.Union[
            vertexai.vision_models.Image, vertexai.preview.vision_models.GeneratedImage
        ],
        new_size: typing.Optional[int] = 2048,
        upscale_factor: typing.Optional[typing.Literal["x2", "x4"]] = None,
        output_mime_type: typing.Optional[
            typing.Literal["image/png", "image/jpeg"]
        ] = "image/png",
        output_compression_quality: typing.Optional[int] = None,
        output_gcs_uri: typing.Optional[str] = None,
    ) -> vertexai.vision_models.Image

Upscales an image.

This supports upscaling images generated through the `generate_images()` method, or upscaling a new image.

Examples::
    
    
    # Upscale a generated image
    model = ImageGenerationModel.from_pretrained("imagegeneration@002")
    response = model.generate_images(
        prompt="Astronaut riding a horse",
    )
    model.upscale_image(image=response[0])
    
    # Upscale a new 1024x1024 image
    my_image = Image.load_from_file("my-image.png")
    model.upscale_image(image=my_image)
    
    # Upscale a new arbitrary sized image using a x2 or x4 upscaling factor
    my_image = Image.load_from_file("my-image.png")
    model.upscale_image(image=my_image, upscale_factor="x2")
    
    # Upscale an image and get the result in JPEG format
    my_image = Image.load_from_file("my-image.png")
    model.upscale_image(image=my_image, output_mime_type="image/jpeg",
    output_compression_quality=90)
    

**Parameters**  
---  
**Name** | **Description**  
`image` |  `Union[GeneratedImage, Image]`   
Required. The generated image to upscale.  
`new_size` |  `int`   
The size of the biggest dimension of the upscaled image. Only 2048 and 4096 are currently supported. Results in a 2048x2048 or 4096x4096 image. Defaults to 2048 if not provided.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
