---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-productstudio/latest/com.google.shopping.merchant.productstudio.v1alpha.ImageServiceGrpc.ImageServiceBlockingStub
title: Class ImageServiceGrpc.ImageServiceBlockingStub (0.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:43:23.159716+00:00
---

# Class ImageServiceGrpc.ImageServiceBlockingStub (0.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-productstudio/latest/com.google.shopping.merchant.productstudio.v1alpha.ImageServiceGrpc.ImageServiceBlockingStub

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class ImageServiceGrpc.ImageServiceBlockingStub (0.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.39.0 (latest)  0.35.0  0.34.0  0.33.0  0.31.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public static final class ImageServiceGrpc.ImageServiceBlockingStub extends AbstractBlockingStub<ImageServiceGrpc.ImageServiceBlockingStub>

A stub to allow clients to do limited synchronous rpc calls to service ImageService.

Service that exposes Generative AI (GenAI) endpoints for creating and enhancing product image content.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > io.grpc.stub.AbstractStub > io.grpc.stub.AbstractBlockingStub > ImageServiceGrpc.ImageServiceBlockingStub

## Inherited Members

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel)

io.grpc.stub.AbstractBlockingStub.<T>newStub(io.grpc.stub.AbstractStub.StubFactory<T>,io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.<T>withOption(io.grpc.CallOptions.Key<T>,T)

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

io.grpc.stub.AbstractStub.getCallOptions()

io.grpc.stub.AbstractStub.getChannel()

io.grpc.stub.AbstractStub.withCallCredentials(io.grpc.CallCredentials)

io.grpc.stub.AbstractStub.withChannel(io.grpc.Channel)

io.grpc.stub.AbstractStub.withCompression(java.lang.String)

io.grpc.stub.AbstractStub.withDeadline(io.grpc.Deadline)

io.grpc.stub.AbstractStub.withDeadlineAfter(java.time.Duration)

io.grpc.stub.AbstractStub.withDeadlineAfter(long,java.util.concurrent.TimeUnit)

io.grpc.stub.AbstractStub.withExecutor(java.util.concurrent.Executor)

io.grpc.stub.AbstractStub.withInterceptors(io.grpc.ClientInterceptor...)

io.grpc.stub.AbstractStub.withMaxInboundMessageSize(int)

io.grpc.stub.AbstractStub.withMaxOutboundMessageSize(int)

io.grpc.stub.AbstractStub.withOnReadyThreshold(int)

io.grpc.stub.AbstractStub.withWaitForReady()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build(Channel channel, CallOptions callOptions)
    
    
    protected ImageServiceGrpc.ImageServiceBlockingStub build(Channel channel, CallOptions callOptions)

**Parameters**  
---  
**Name** | **Description**  
`channel` | `io.grpc.Channel`  
  
`callOptions` | `io.grpc.CallOptions`  
  
**Returns**  
---  
**Type** | **Description**  
`[ImageServiceGrpc.ImageServiceBlockingStub](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-productstudio/latest/com.google.shopping.merchant.productstudio.v1alpha.ImageServiceGrpc.ImageServiceBlockingStub)` |   
**Overrides**

io.grpc.stub.AbstractStub.build(io.grpc.Channel,io.grpc.CallOptions)

### generateProductImageBackground(GenerateProductImageBackgroundRequest request)
    
    
    public GenerateProductImageBackgroundResponse generateProductImageBackground(GenerateProductImageBackgroundRequest request)

GenerateProductImageBackground generates a new image where the background of the original image is replaced by an AI generated scene based on provided product information and a text prompt.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[GenerateProductImageBackgroundRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-productstudio/latest/com.google.shopping.merchant.productstudio.v1alpha.GenerateProductImageBackgroundRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[GenerateProductImageBackgroundResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-productstudio/latest/com.google.shopping.merchant.productstudio.v1alpha.GenerateProductImageBackgroundResponse)` |   
  
### removeProductImageBackground(RemoveProductImageBackgroundRequest request)
    
    
    public RemoveProductImageBackgroundResponse removeProductImageBackground(RemoveProductImageBackgroundRequest request)

RemoveProductImageBackground generates a new image where the background of the original image is removed.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[RemoveProductImageBackgroundRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-productstudio/latest/com.google.shopping.merchant.productstudio.v1alpha.RemoveProductImageBackgroundRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RemoveProductImageBackgroundResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-productstudio/latest/com.google.shopping.merchant.productstudio.v1alpha.RemoveProductImageBackgroundResponse)` |   
  
### upscaleProductImage(UpscaleProductImageRequest request)
    
    
    public UpscaleProductImageResponse upscaleProductImage(UpscaleProductImageRequest request)

UpscaleProductImage generates a new image where the resolution of the original image is enhanced.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[UpscaleProductImageRequest](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-productstudio/latest/com.google.shopping.merchant.productstudio.v1alpha.UpscaleProductImageRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[UpscaleProductImageResponse](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-productstudio/latest/com.google.shopping.merchant.productstudio.v1alpha.UpscaleProductImageResponse)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
