---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-productstudio/latest/com.google.shopping.merchant.productstudio.v1alpha.GeneratedImageOrBuilder
title: Interface GeneratedImageOrBuilder (0.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:58.062813+00:00
---

# Interface GeneratedImageOrBuilder (0.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-productstudio/latest/com.google.shopping.merchant.productstudio.v1alpha.GeneratedImageOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface GeneratedImageOrBuilder (0.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.39.0 (latest)  0.35.0  0.34.0  0.33.0  0.31.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public interface GeneratedImageOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getGenerationTime()
    
    
    public abstract Timestamp getGenerationTime()

The timestamp when the image was generated.

`.google.protobuf.Timestamp generation_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The generationTime.  
  
### getGenerationTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getGenerationTimeOrBuilder()

The timestamp when the image was generated.

`.google.protobuf.Timestamp generation_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getImageBytes()
    
    
    public abstract ByteString getImageBytes()

Raw bytes for the image.

`bytes image_bytes = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The imageBytes.  
  
### getImageCase()
    
    
    public abstract GeneratedImage.ImageCase getImageCase()

**Returns**  
---  
**Type** | **Description**  
`[GeneratedImage.ImageCase](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-productstudio/latest/com.google.shopping.merchant.productstudio.v1alpha.GeneratedImage.ImageCase)` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. The unique key for the image.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The unique key for the image.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getUri()
    
    
    public abstract String getUri()

Generally web-requestable URI of the generated image. This is a temporary URI and will expire after 6 months. A URI may not be populated immediately after generation. Use get or list api using image_id to get the URI.

`string uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uri.  
  
### getUriBytes()
    
    
    public abstract ByteString getUriBytes()

Generally web-requestable URI of the generated image. This is a temporary URI and will expire after 6 months. A URI may not be populated immediately after generation. Use get or list api using image_id to get the URI.

`string uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uri.  
  
### hasGenerationTime()
    
    
    public abstract boolean hasGenerationTime()

The timestamp when the image was generated.

`.google.protobuf.Timestamp generation_time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the generationTime field is set.  
  
### hasImageBytes()
    
    
    public abstract boolean hasImageBytes()

Raw bytes for the image.

`bytes image_bytes = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the imageBytes field is set.  
  
### hasUri()
    
    
    public abstract boolean hasUri()

Generally web-requestable URI of the generated image. This is a temporary URI and will expire after 6 months. A URI may not be populated immediately after generation. Use get or list api using image_id to get the URI.

`string uri = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the uri field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
