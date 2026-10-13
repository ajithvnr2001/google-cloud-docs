---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio
title: Google Cloud Speech v1 API - Class RecognitionAudio (3.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:11.527197+00:00
---

# Google Cloud Speech v1 API - Class RecognitionAudio (3.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Speech v1 API - Class RecognitionAudio (3.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.9.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 3.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.8.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.7.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.6.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.5.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.4.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.3.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.2.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.1.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/3.0.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.9.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.8.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.7.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.6.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.5.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.4.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.3.0/Google.Cloud.Speech.V1.RecognitionAudio)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/2.2.0/Google.Cloud.Speech.V1.RecognitionAudio)


    
    
    public sealed class RecognitionAudio : IMessage<RecognitionAudio>, IEquatable<RecognitionAudio>, IDeepCloneable<RecognitionAudio>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Speech v1 API class RecognitionAudio.

Contains audio data in the encoding specified in the `RecognitionConfig`. Either `content` or `uri` must be supplied. Supplying both or neither returns [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]. See [content limits](https://cloud.google.com/speech-to-text/quotas#content).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RecognitionAudio

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Speech.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1)

## Assembly

Google.Cloud.Speech.V1.dll

## Constructors 

### RecognitionAudio()
    
    
    public RecognitionAudio()

### RecognitionAudio(RecognitionAudio)
    
    
    public RecognitionAudio(RecognitionAudio other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)`  
  
  
## Properties 

### AudioSourceCase
    
    
    public RecognitionAudio.AudioSourceOneofCase AudioSourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)[AudioSourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio.AudioSourceOneofCase)` |   
  
### Content
    
    
    public ByteString Content { get; set; }

The audio data bytes encoded as specified in `RecognitionConfig`. Note: as with all bytes fields, proto buffers use a pure binary representation, whereas JSON representations use base64.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### HasContent
    
    
    public bool HasContent { get; }

Gets whether the "content" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasUri
    
    
    public bool HasUri { get; }

Gets whether the "uri" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Uri
    
    
    public string Uri { get; set; }

URI that points to a file that contains audio data bytes as specified in `RecognitionConfig`. The file must not be compressed (for example, gzip). Currently, only Google Cloud Storage URIs are supported, which must be specified in the following format: `gs://bucket_name/object_name` (other URI formats return [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]). For more information, see [Request URIs](https://cloud.google.com/storage/docs/reference-uris).

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
## Methods 

### FetchFromUri(string, HttpClient)
    
    
    public static RecognitionAudio FetchFromUri(string uri, HttpClient httpClient = null)

Constructs a [RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio) by downloading data from the given URI.

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
`[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)` | The newly created RecognitionAudio.  
  
### FetchFromUri(Uri, HttpClient)
    
    
    public static RecognitionAudio FetchFromUri(Uri uri, HttpClient httpClient = null)

Constructs a [RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio) by downloading data from the given URI.

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
`[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)` | The newly created RecognitionAudio.  
  
### FetchFromUriAsync(string, HttpClient)
    
    
    public static Task<RecognitionAudio> FetchFromUriAsync(string uri, HttpClient httpClient = null)

Asynchronously constructs a [RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio) by downloading data from the given URI.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)` | A task representing the asynchronous operation. The result will be the newly created RecognitionAudio.  
  
### FetchFromUriAsync(Uri, HttpClient)
    
    
    public static Task<RecognitionAudio> FetchFromUriAsync(Uri uri, HttpClient httpClient = null)

Asynchronously constructs a [RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio) by downloading data from the given URI.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)` | A task representing the asynchronous operation. The result will be the newly created RecognitionAudio.  
  
### FromBytes(byte[])
    
    
    public static RecognitionAudio FromBytes(byte[] bytes)

Constructs a [RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio) from the given byte array.

**Parameter**  
---  
**Name** | **Description**  
`bytes` | `System.Byte`  
The bytes representing the raw RecognitionAudio data.  
**Returns**  
---  
**Type** | **Description**  
`[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)` | The newly created RecognitionAudio.  
**Remarks**

This method copies the data from the byte array; modifications to `bytes` after this method returns will not be reflected in the RecognitionAudio.

### FromBytes(byte[], int, int)
    
    
    public static RecognitionAudio FromBytes(byte[] bytes, int offset, int count)

Constructs a [RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio) from a section of the given byte array.

**Parameters**  
---  
**Name** | **Description**  
`bytes` | `System.Byte`  
The bytes representing the raw RecognitionAudio data.  
`offset` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The offset into the byte array of the start of the data to include in the RecognitionAudio.  
`count` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The number of bytes to include in the RecognitionAudio.  
**Returns**  
---  
**Type** | **Description**  
`[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)` | The newly created RecognitionAudio.  
**Remarks**

This method copies the data from the byte array; modifications to `bytes` after this method returns will not be reflected in the RecognitionAudio.

### FromFile(string)
    
    
    public static RecognitionAudio FromFile(string path)

Constructs a [RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio) by loading data from the given file path.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The file path to load RecognitionAudio data from. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)` | The newly created RecognitionAudio.  
  
### FromFileAsync(string)
    
    
    public static Task<RecognitionAudio> FromFileAsync(string path)

Asynchronously constructs a [RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio) by loading data from the given file path.

**Parameter**  
---  
**Name** | **Description**  
`path` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The file path to load RecognitionAudio data from. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)` | The newly created RecognitionAudio.  
  
### FromStorageUri(string)
    
    
    public static RecognitionAudio FromStorageUri(string storageUri)

Constructs a [RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio) with a [Uri](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio#Google_Cloud_Speech_V1_RecognitionAudio_Uri) property referring to a Google Cloud Storage URI.

**Parameter**  
---  
**Name** | **Description**  
`storageUri` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
A Google Cloud Storage URI, of the form `gs://bucket-name/object-name`. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)` | The newly created RecognitionAudio.  
  
### FromStream(Stream)
    
    
    public static RecognitionAudio FromStream(Stream stream)

Constructs a [RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio) by loading data from the given stream.

**Parameter**  
---  
**Name** | **Description**  
`stream` | `[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)`  
The stream to load RecognitionAudio data from. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)` | The newly created RecognitionAudio.  
  
### FromStreamAsync(Stream)
    
    
    public static Task<RecognitionAudio> FromStreamAsync(Stream stream)

Asynchronously constructs a [RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio) by loading data from the given stream.

**Parameter**  
---  
**Name** | **Description**  
`stream` | `[Stream](https://learn.microsoft.com/dotnet/api/system.io.stream)`  
The stream to load RecognitionAudio data from. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RecognitionAudio](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Speech.V1/latest/Google.Cloud.Speech.V1.RecognitionAudio)` | The newly created RecognitionAudio.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
