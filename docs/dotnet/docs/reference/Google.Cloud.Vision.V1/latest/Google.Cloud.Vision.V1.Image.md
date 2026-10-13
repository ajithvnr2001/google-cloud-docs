---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image
title: Google Cloud Vision v1 API - Class Image (3.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:32.829403+00:00
---

# Google Cloud Vision v1 API - Class Image (3.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Vision v1 API - Class Image (3.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.7.0/Google.Cloud.Vision.V1.Image)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.6.0/Google.Cloud.Vision.V1.Image)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.5.0/Google.Cloud.Vision.V1.Image)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.4.0/Google.Cloud.Vision.V1.Image)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.3.0/Google.Cloud.Vision.V1.Image)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.2.0/Google.Cloud.Vision.V1.Image)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.1.0/Google.Cloud.Vision.V1.Image)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/3.0.0/Google.Cloud.Vision.V1.Image)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.5.0/Google.Cloud.Vision.V1.Image)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.4.0/Google.Cloud.Vision.V1.Image)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/2.3.0/Google.Cloud.Vision.V1.Image)


    
    
    public sealed class Image : IMessage<Image>, IEquatable<Image>, IDeepCloneable<Image>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Vision v1 API class Image.

Client image to perform Google Cloud Vision API tasks over.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Image

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Vision.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1)

## Assembly

Google.Cloud.Vision.V1.dll

## Constructors 

### Image()
    
    
    public Image()

### Image(Image)
    
    
    public Image(Image other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)`  
  
  
## Properties 

### Content
    
    
    public ByteString Content { get; set; }

Image content, represented as a stream of bytes. Note: As with all `bytes` fields, protobuffers use a pure binary representation, whereas JSON representations use base64.

Currently, this field only works for BatchAnnotateImages requests. It does not work for AsyncBatchAnnotateImages requests.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### Source
    
    
    public ImageSource Source { get; set; }

Google Cloud Storage image location, or publicly-accessible image URL. If both `content` and `source` are provided for an image, `content` takes precedence and is used to perform the image annotation request.

**Property Value**  
---  
**Type** | **Description**  
`[ImageSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.ImageSource)` |   
  
## Methods 

### FetchFromUri(string, HttpClient)
    
    
    public static Image FetchFromUri(string uri, HttpClient httpClient = null)

Constructs an [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image) by downloading data from the given URI.

**Parameters**  
---  
**Name** | **Description**  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The URI to fetch. Must not be null.  
`httpClient` | `[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient)`  
The [HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient) to use to fetch the image, or `null` to use a default client.  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)` | The newly created image.  
**Remarks**

Unlike [FromUri(string)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image#Google_Cloud_Vision_V1_Image_FromUri_System_String_), this method downloads the image locally then uploads it to the Google Cloud Vision server.

### FetchFromUri(Uri, HttpClient)
    
    
    public static Image FetchFromUri(Uri uri, HttpClient httpClient = null)

Constructs an [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image) by downloading data from the given URI.

**Parameters**  
---  
**Name** | **Description**  
`uri` | `[Uri](https://learn.microsoft.com/dotnet/api/system.uri)`  
The URI to fetch. Must not be null.  
`httpClient` | `[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient)`  
The [HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient) to use to fetch the image, or `null` to use a default client.  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)` | The newly created image.  
**Remarks**

Unlike [FromUri(string)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image#Google_Cloud_Vision_V1_Image_FromUri_System_String_), this method downloads the image locally then uploads it to the Google Cloud Vision server.

### FetchFromUriAsync(string, HttpClient)
    
    
    public static Task<Image> FetchFromUriAsync(string uri, HttpClient httpClient = null)

Asynchronously constructs an [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image) by downloading data from the given URI.

**Parameters**  
---  
**Name** | **Description**  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The URI to fetch. Must not be null.  
`httpClient` | `[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient)`  
The [HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient) to use to fetch the image, or `null` to use a default client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)` | A task representing the asynchronous operation. The result will be the newly created image.  
**Remarks**

Unlike [FromUri(Uri)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image#Google_Cloud_Vision_V1_Image_FromUri_System_Uri_), this method downloads the image locally then uploads it to the Google Cloud Vision server.

### FetchFromUriAsync(Uri, HttpClient)
    
    
    public static Task<Image> FetchFromUriAsync(Uri uri, HttpClient httpClient = null)

Asynchronously constructs an [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image) by downloading data from the given URI.

**Parameters**  
---  
**Name** | **Description**  
`uri` | `[Uri](https://learn.microsoft.com/dotnet/api/system.uri)`  
The URI to fetch. Must not be null.  
`httpClient` | `[HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient)`  
The [HttpClient](https://learn.microsoft.com/dotnet/api/system.net.http.httpclient) to use to fetch the image, or `null` to use a default client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)` | A task representing the asynchronous operation. The result will be the newly created image.  
**Remarks**

Unlike [FromUri(Uri)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image#Google_Cloud_Vision_V1_Image_FromUri_System_Uri_), this method downloads the image locally then uploads it to the Google Cloud Vision server.

### FromBytes(byte[])
    
    
    public static Image FromBytes(byte[] bytes)

Constructs an [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image) from the given byte array.

**Parameter**  
---  
**Name** | **Description**  
`bytes` | `System.Byte`  
The bytes representing the raw image data.  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)` | The newly created image.  
**Remarks**

This method copies the data from the byte array; modifications to `bytes` after this method returns will not be reflected in the image.

### FromBytes(byte[], int, int)
    
    
    public static Image FromBytes(byte[] bytes, int offset, int count)

Constructs an [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image) from a section of the given byte array.

**Parameters**  
---  
**Name** | **Description**  
`bytes` | `System.Byte`  
The bytes representing the raw image data.  
`offset` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The offset into the byte array of the start of the data to include in the image.  
`count` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The number of bytes to include in the image.  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)` | The newly created image.  
**Remarks**

This method copies the data from the byte array; modifications to `bytes` after this method returns will not be reflected in the image.

### FromFile(string)
    
    
    public static Image FromFile(string path)

Constructs an [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image) by loading data from the given file path.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The file path to load image data from. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)` | The newly created image.  
  
### FromFileAsync(string)
    
    
    public static Task<Image> FromFileAsync(string path)

Asynchronously constructs an [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image) by loading data from the given file path.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The file path to load image data from. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)` | The newly created image.  
  
### FromStream(Stream)
    
    
    public static Image FromStream(Stream stream)

Constructs an [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image) by loading data from the given stream.

**Parameter**  
---  
**Name** | **Description**  
`stream` | `[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)`  
The stream to load image data from. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)` | The newly created image.  
  
### FromStreamAsync(Stream)
    
    
    public static Task<Image> FromStreamAsync(Stream stream)

Asynchronously constructs an [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image) by loading data from the given stream.

**Parameter**  
---  
**Name** | **Description**  
`stream` | `[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)`  
The stream to load image data from. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)` | The newly created image.  
  
### FromUri(string)
    
    
    public static Image FromUri(string uri)

Constructs an [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image) with a [Source](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image#Google_Cloud_Vision_V1_Image_Source) property referring to a URI, which may either be a Google Cloud Storage URI or a publicly accessible HTTP or HTTPS URI. The image is fetched from the URI by the Google Cloud Vision server.

**Parameter**  
---  
**Name** | **Description**  
`uri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The URI of the image, which may either be a Google Cloud Storage URI of the form `gs://bucket-name/file-name` or a publicly accessibly HTTP or HTTPS URI. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)` | The newly created image.  
  
### FromUri(Uri)
    
    
    public static Image FromUri(Uri uri)

Constructs an [Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image) with a [Source](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image#Google_Cloud_Vision_V1_Image_Source) property referring to a URI, which may either be a Google Cloud Storage URI or a publicly accessible HTTP or HTTPS URI. The image is fetched from the URI by the Google Cloud Vision server.

**Parameter**  
---  
**Name** | **Description**  
`uri` | `[Uri](https://learn.microsoft.com/dotnet/api/system.uri)`  
The URI of the image, which may either be a Google Cloud Storage URI of the form `gs://bucket-name/file-name` or a publicly accessibly HTTP or HTTPS URI. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest/Google.Cloud.Vision.V1.Image)` | The newly created image.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
