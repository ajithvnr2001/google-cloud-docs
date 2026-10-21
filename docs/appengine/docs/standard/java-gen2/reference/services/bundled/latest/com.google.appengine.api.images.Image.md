---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image
title: Interface Image (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:23:23.309124+00:00
---

# Interface Image (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.Image

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface Image (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface Image extends Serializable

`Image` represents an image that can be manipulated by the [ImagesService](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.images.ImagesService).

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

## Methods 

### getBlobKey()
    
    
    public abstract @Nullable BlobKey getBlobKey()

If this image is backed by a blob, return the associated [BlobKey](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.blobstore.BlobKey). If this method returns non-`null`, none of the other methods will currently be available.

**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.blobstore.@org.jspecify.annotations.Nullable BlobKey` |   
  
### getFormat()
    
    
    public abstract Image.@Nullable Format getFormat()

Gets the encoding format of the image.

**Returns**  
---  
**Type** | **Description**  
`com.google.appengine.api.images.Image.@org.jspecify.annotations.Nullable Format` | image format  
  
### getHeight()
    
    
    public abstract int getHeight()

Gets the height of the image.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | image height  
  
### getImageData()
    
    
    public abstract byte @Nullable [] getImageData()

Gets the raw imageData of the image.

**Returns**  
---  
**Type** | **Description**  
`byte @org.jspecify.annotations.Nullable []` | the image data of the image  
  
### getWidth()
    
    
    public abstract int getWidth()

Gets the width of the image.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | image width  
  
### setImageData(byte[] imageData)
    
    
    public abstract void setImageData(byte[] imageData)

Sets the image to contain the image data contained in `imageData`.

**Parameter**  
---  
**Name** | **Description**  
`imageData` | `byte[]`  
new image data for the image to store  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
