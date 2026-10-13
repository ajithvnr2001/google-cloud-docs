---
url: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader
title: Class MediaHttpUploader (2.9.1) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:23:46.219466+00:00
---

# Class MediaHttpUploader (2.9.1)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class MediaHttpUploader (2.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.1 (latest)  2.9.0  2.8.1  2.7.2  2.6.0  2.5.1  2.4.1  2.1.2  2.0.1  1.35.2  1.34.1  1.33.4 
    
    
    public final class MediaHttpUploader

Media HTTP Uploader, with support for both direct and resumable media uploads. Documentation is available [here](https://googleapis.github.io/google-api-java-client/media-upload.html).

For resumable uploads, when the media content length is known, if the provided InputStream has InputStream#markSupported as `false` then it is wrapped in an BufferedInputStream to support the InputStream#mark and InputStream#reset methods required for handling server errors. If the media content length is unknown then each chunk is stored temporarily in memory. This is required to determine when the last chunk is reached.

See [#setDisableGZipContent(boolean)](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader#com_google_api_client_googleapis_media_MediaHttpUploader_setDisableGZipContent_boolean_) for information on when content is gzipped and how to control that behavior.

Back-off is disabled by default. To enable it for an abnormal HTTP response and an I/O exception you should call HttpRequest#setUnsuccessfulResponseHandler with a new HttpBackOffUnsuccessfulResponseHandler instance and HttpRequest#setIOExceptionHandler with HttpBackOffIOExceptionHandler.

Upgrade warning: in prior version 1.14 exponential back-off was enabled by default for an abnormal HTTP response and there was a regular retry (without back-off) when I/O exception was thrown. Starting with version 1.15 back-off is disabled and there is no retry on I/O exception by default.

Upgrade warning: in prior version 1.16 #serverErrorCallback was public but starting with version 1.17 it has been removed from the public API, and changed to be package private.

Implementation is not thread-safe.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > MediaHttpUploader

## Inherited Members

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

## Static Fields 

### CONTENT_LENGTH_HEADER
    
    
    public static final String CONTENT_LENGTH_HEADER

Upload content type header.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### CONTENT_TYPE_HEADER
    
    
    public static final String CONTENT_TYPE_HEADER

Upload content length header.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### DEFAULT_CHUNK_SIZE
    
    
    public static final int DEFAULT_CHUNK_SIZE

Default maximum number of bytes that will be uploaded to the server in any single HTTP request (set to 10 MB).

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MINIMUM_CHUNK_SIZE
    
    
    public static final int MINIMUM_CHUNK_SIZE

Minimum number of bytes that can be uploaded to the server (set to 256KB).

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Constructors 

### MediaHttpUploader(AbstractInputStreamContent mediaContent, HttpTransport transport, HttpRequestInitializer httpRequestInitializer)
    
    
    public MediaHttpUploader(AbstractInputStreamContent mediaContent, HttpTransport transport, HttpRequestInitializer httpRequestInitializer)

Construct the [MediaHttpUploader](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader).

The input stream received by calling AbstractInputStreamContent#getInputStream is closed when the upload process is successfully completed. For resumable uploads, when the media content length is known, if the input stream has InputStream#markSupported as ` false` then it is wrapped in an BufferedInputStream to support the InputStream#mark and InputStream#reset methods required for handling server errors. If the media content length is unknown then each chunk is stored temporarily in memory. This is required to determine when the last chunk is reached.

**Parameters**  
---  
**Name** | **Description**  
`mediaContent` | `com.google.api.client.http.AbstractInputStreamContent`  
The Input stream content of the media to be uploaded  
`transport` | `com.google.api.client.http.HttpTransport`  
The transport to use for requests  
`httpRequestInitializer` | `com.google.api.client.http.HttpRequestInitializer`  
The initializer to use when creating an HttpRequest or `null` for none  
  
## Methods 

### getChunkSize()
    
    
    public int getChunkSize()

Returns the maximum size of individual chunks that will get uploaded by single HTTP requests. The default value is [#DEFAULT_CHUNK_SIZE](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader#com_google_api_client_googleapis_media_MediaHttpUploader_DEFAULT_CHUNK_SIZE).

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDisableGZipContent()
    
    
    public boolean getDisableGZipContent()

Returns whether to disable GZip compression of HTTP content.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getInitiationHeaders()
    
    
    public HttpHeaders getInitiationHeaders()

Returns the HTTP headers used for the initiation request.

**Returns**  
---  
**Type** | **Description**  
`com.google.api.client.http.HttpHeaders` |   
  
### getInitiationRequestMethod()
    
    
    public String getInitiationRequestMethod()

Returns the HTTP method used for the initiation request.

The default value is HttpMethods#POST.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMediaContent()
    
    
    public HttpContent getMediaContent()

Returns the HTTP content of the media to be uploaded.

**Returns**  
---  
**Type** | **Description**  
`com.google.api.client.http.HttpContent` |   
  
### getMetadata()
    
    
    public HttpContent getMetadata()

Returns HTTP content metadata for the media request or `null` for none.

**Returns**  
---  
**Type** | **Description**  
`com.google.api.client.http.HttpContent` |   
  
### getNumBytesUploaded()
    
    
    public long getNumBytesUploaded()

Gets the total number of bytes the server received so far or `0` for direct uploads when the content length is not known.

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the number of bytes the server received so far  
  
### getProgress()
    
    
    public double getProgress()

Gets the upload progress denoting the percentage of bytes that have been uploaded, represented between 0.0 (0%) and 1.0 (100%).

Do not use if the specified AbstractInputStreamContent has no content length specified. Instead, consider using [#getNumBytesUploaded](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader#com_google_api_client_googleapis_media_MediaHttpUploader_getNumBytesUploaded_) to denote progress.

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | the upload progress  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` | if the specified AbstractInputStreamContent has no content length  
  
### getProgressListener()
    
    
    public MediaHttpUploaderProgressListener getProgressListener()

Returns the progress listener to send progress notifications to or `null` for none.

**Returns**  
---  
**Type** | **Description**  
`[MediaHttpUploaderProgressListener](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploaderProgressListener)` |   
  
### getSleeper()
    
    
    public Sleeper getSleeper()

Returns the sleeper.

**Returns**  
---  
**Type** | **Description**  
`com.google.api.client.util.Sleeper` |   
  
### getTransport()
    
    
    public HttpTransport getTransport()

Returns the transport to use for requests.

**Returns**  
---  
**Type** | **Description**  
`com.google.api.client.http.HttpTransport` |   
  
### getUploadState()
    
    
    public MediaHttpUploader.UploadState getUploadState()

Gets the current upload state of the uploader.

**Returns**  
---  
**Type** | **Description**  
`[MediaHttpUploader.UploadState](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader.UploadState)` | the upload state  
  
### isDirectUploadEnabled()
    
    
    public boolean isDirectUploadEnabled()

Returns whether direct media upload is enabled or disabled. If value is set to `true` then a direct upload will be done where the whole media content is uploaded in a single request. If value is set to `false` then the upload uses the resumable media upload protocol to upload in data chunks. Defaults to `false`.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### setChunkSize(int chunkSize)
    
    
    public MediaHttpUploader setChunkSize(int chunkSize)

Sets the maximum size of individual chunks that will get uploaded by single HTTP requests. The default value is [#DEFAULT_CHUNK_SIZE](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader#com_google_api_client_googleapis_media_MediaHttpUploader_DEFAULT_CHUNK_SIZE).

The minimum allowable value is [#MINIMUM_CHUNK_SIZE](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader#com_google_api_client_googleapis_media_MediaHttpUploader_MINIMUM_CHUNK_SIZE) and the specified chunk size must be a multiple of [#MINIMUM_CHUNK_SIZE](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader#com_google_api_client_googleapis_media_MediaHttpUploader_MINIMUM_CHUNK_SIZE).

**Parameter**  
---  
**Name** | **Description**  
`chunkSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MediaHttpUploader](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader)` |   
  
### setDirectUploadEnabled(boolean directUploadEnabled)
    
    
    public MediaHttpUploader setDirectUploadEnabled(boolean directUploadEnabled)

Sets whether direct media upload is enabled or disabled.

If value is set to `true` then a direct upload will be done where the whole media content is uploaded in a single request. If value is set to `false` then the upload uses the resumable media upload protocol to upload in data chunks.

Direct upload is recommended if the content size falls below a certain minimum limit. This is because there's minimum block write size for some Google APIs, so if the resumable request fails in the space of that first block, the client will have to restart from the beginning anyway.

Defaults to `false`.

**Parameter**  
---  
**Name** | **Description**  
`directUploadEnabled` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MediaHttpUploader](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader)` |   
  
### setDisableGZipContent(boolean disableGZipContent)
    
    
    public MediaHttpUploader setDisableGZipContent(boolean disableGZipContent)

Sets whether to disable GZip compression of HTTP content.

By default it is `false`.

If [#setDisableGZipContent(boolean)](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader#com_google_api_client_googleapis_media_MediaHttpUploader_setDisableGZipContent_boolean_) is set to false (the default value) then content is gzipped for direct media upload and resumable media uploads when content length is not known. Due to a current limitation, content is not gzipped for resumable media uploads when content length is known; this limitation will be removed in the future.

**Parameter**  
---  
**Name** | **Description**  
`disableGZipContent` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MediaHttpUploader](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader)` |   
  
### setInitiationHeaders(HttpHeaders initiationHeaders)
    
    
    public MediaHttpUploader setInitiationHeaders(HttpHeaders initiationHeaders)

Sets the HTTP headers used for the initiation request.

**Parameter**  
---  
**Name** | **Description**  
`initiationHeaders` | `com.google.api.client.http.HttpHeaders`  
  
**Returns**  
---  
**Type** | **Description**  
`[MediaHttpUploader](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader)` |   
  
### setInitiationRequestMethod(String initiationRequestMethod)
    
    
    public MediaHttpUploader setInitiationRequestMethod(String initiationRequestMethod)

Sets the HTTP method used for the initiation request.

Can only be HttpMethods#POST (for media upload) or HttpMethods#PUT (for media update). The default value is HttpMethods#POST.

**Parameter**  
---  
**Name** | **Description**  
`initiationRequestMethod` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MediaHttpUploader](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader)` |   
  
### setMetadata(HttpContent metadata)
    
    
    public MediaHttpUploader setMetadata(HttpContent metadata)

Sets HTTP content metadata for the media request or `null` for none.

**Parameter**  
---  
**Name** | **Description**  
`metadata` | `com.google.api.client.http.HttpContent`  
  
**Returns**  
---  
**Type** | **Description**  
`[MediaHttpUploader](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader)` |   
  
### setProgressListener(MediaHttpUploaderProgressListener progressListener)
    
    
    public MediaHttpUploader setProgressListener(MediaHttpUploaderProgressListener progressListener)

Sets the progress listener to send progress notifications to or `null` for none.

**Parameter**  
---  
**Name** | **Description**  
`progressListener` | `[MediaHttpUploaderProgressListener](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploaderProgressListener)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MediaHttpUploader](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader)` |   
  
### setSleeper(Sleeper sleeper)
    
    
    public MediaHttpUploader setSleeper(Sleeper sleeper)

Sets the sleeper. The default value is [Sleeper#DEFAULT](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.util.Sleeper.html#com_google_api_client_util_Sleeper_DEFAULT).

**Parameter**  
---  
**Name** | **Description**  
`sleeper` | `com.google.api.client.util.Sleeper`  
  
**Returns**  
---  
**Type** | **Description**  
`[MediaHttpUploader](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader)` |   
  
### upload(GenericUrl initiationRequestUrl)
    
    
    public HttpResponse upload(GenericUrl initiationRequestUrl)

Executes a direct media upload or resumable media upload conforming to the specifications listed [here.](https://developers.google.com/api-client-library/java/google-api-java-client/media-upload)

This method is not reentrant. A new instance of [MediaHttpUploader](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.media.MediaHttpUploader) must be instantiated before upload called be called again.

If an error is encountered during the request execution the caller is responsible for parsing the response correctly. For example for JSON errors:
    
    
     if (!response.isSuccessStatusCode()) {
       throw GoogleJsonResponseException.from(jsonFactory, response);
     }
     

Callers should call HttpResponse#disconnect when the returned HTTP response object is no longer needed. However, HttpResponse#disconnect does not have to be called if the response stream is properly closed. Example usage:
    
    
     HttpResponse response = batch.upload(initiationRequestUrl);
     try {
       // process the HTTP response object
     } finally {
       response.disconnect();
     }
     

**Parameter**  
---  
**Name** | **Description**  
`initiationRequestUrl` | `com.google.api.client.http.GenericUrl`  
The request URL where the initiation request will be sent  
**Returns**  
---  
**Type** | **Description**  
`com.google.api.client.http.HttpResponse` | HTTP response  
**Exceptions**  
---  
**Type** | **Description**  
`[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
