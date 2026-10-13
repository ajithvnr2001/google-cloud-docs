---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.Document.ContentOrBuilder
title: Interface Document.ContentOrBuilder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:07.175805+00:00
---

# Interface Document.ContentOrBuilder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.Document.ContentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Document.ContentOrBuilder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface Document.ContentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getContentCase()
    
    
    public abstract Document.Content.ContentCase getContentCase()

**Returns**  
---  
**Type** | **Description**  
`[Document.Content.ContentCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.Document.Content.ContentCase)` |   
  
### getMimeType()
    
    
    public abstract String getMimeType()

The MIME type of the content. Supported types:

  * `application/pdf` (PDF, only native PDFs are supported for now)
  * `text/html` (HTML)
  * `text/plain` (TXT)
  * `application/xml` or `text/xml` (XML)
  * `application/json` (JSON)
  * `application/vnd.openxmlformats-officedocument.wordprocessingml.document` (DOCX)
  * `application/vnd.openxmlformats-officedocument.presentationml.presentation` (PPTX)
  * `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` (XLSX)
  * `application/vnd.ms-excel.sheet.macroenabled.12` (XLSM)

The following types are supported only if layout parser is enabled in the data store:

  * `image/bmp` (BMP)

  * `image/gif` (GIF)
  * `image/jpeg` (JPEG)
  * `image/png` (PNG)
  * `image/tiff` (TIFF)

See <https://www.iana.org/assignments/media-types/media-types.xhtml>.




`string mime_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The mimeType.  
  
### getMimeTypeBytes()
    
    
    public abstract ByteString getMimeTypeBytes()

The MIME type of the content. Supported types:

  * `application/pdf` (PDF, only native PDFs are supported for now)
  * `text/html` (HTML)
  * `text/plain` (TXT)
  * `application/xml` or `text/xml` (XML)
  * `application/json` (JSON)
  * `application/vnd.openxmlformats-officedocument.wordprocessingml.document` (DOCX)
  * `application/vnd.openxmlformats-officedocument.presentationml.presentation` (PPTX)
  * `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet` (XLSX)
  * `application/vnd.ms-excel.sheet.macroenabled.12` (XLSM)

The following types are supported only if layout parser is enabled in the data store:

  * `image/bmp` (BMP)

  * `image/gif` (GIF)
  * `image/jpeg` (JPEG)
  * `image/png` (PNG)
  * `image/tiff` (TIFF)

See <https://www.iana.org/assignments/media-types/media-types.xhtml>.




`string mime_type = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for mimeType.  
  
### getRawBytes()
    
    
    public abstract ByteString getRawBytes()

The content represented as a stream of bytes. The maximum length is 1,000,000 bytes (1 MB / ~0.95 MiB).

Note: As with all `bytes` fields, this field is represented as pure binary in Protocol Buffers and base64-encoded string in JSON. For example, `abc123!?$*&()'-=@~` should be represented as `YWJjMTIzIT8kKiYoKSctPUB+` in JSON. See <https://developers.google.com/protocol-buffers/docs/proto3#json>.

`bytes raw_bytes = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The rawBytes.  
  
### getUri()
    
    
    public abstract String getUri()

The URI of the content. Only Cloud Storage URIs (e.g. `gs://bucket-name/path/to/file`) are supported. The maximum file size is 2.5 MB for text-based formats, 200 MB for other formats.

`string uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The uri.  
  
### getUriBytes()
    
    
    public abstract ByteString getUriBytes()

The URI of the content. Only Cloud Storage URIs (e.g. `gs://bucket-name/path/to/file`) are supported. The maximum file size is 2.5 MB for text-based formats, 200 MB for other formats.

`string uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for uri.  
  
### hasRawBytes()
    
    
    public abstract boolean hasRawBytes()

The content represented as a stream of bytes. The maximum length is 1,000,000 bytes (1 MB / ~0.95 MiB).

Note: As with all `bytes` fields, this field is represented as pure binary in Protocol Buffers and base64-encoded string in JSON. For example, `abc123!?$*&()'-=@~` should be represented as `YWJjMTIzIT8kKiYoKSctPUB+` in JSON. See <https://developers.google.com/protocol-buffers/docs/proto3#json>.

`bytes raw_bytes = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rawBytes field is set.  
  
### hasUri()
    
    
    public abstract boolean hasUri()

The URI of the content. Only Cloud Storage URIs (e.g. `gs://bucket-name/path/to/file`) are supported. The maximum file size is 2.5 MB for text-based formats, 200 MB for other formats.

`string uri = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the uri field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
