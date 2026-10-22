---
url: https://docs.cloud.google.com/healthcare-api/docs/dicom/
title: DICOM conformance statement \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:33:02.237626+00:00
---

# DICOM conformance statement  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/dicom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Reference ](https://docs.cloud.google.com/healthcare-api/docs/apis)



Send feedback 

#  DICOM conformance statement Stay organized with collections  Save and categorize content based on your preferences. 

DICOM stores within the Cloud Healthcare API support a subset of the RESTful web services specified in the [DICOM PS3.18 - Web Services](https://dicom.nema.org/medical/dicom/current/output/html/part18.html) standard (commonly referred to as DICOMweb). Specifically, they support the [Studies Service and Resources](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#chapter_10) (previously referred to as the WADO-RS, STOW-RS, and QIDO-RS services).

Additionally, the Cloud Healthcare API supports a proprietary web service for deleting DICOM instances.

The Cloud Healthcare API does not support the [URI Service](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#chapter_9), the [Worklist Service](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#chapter_11), the [Non-Patient Instance Service](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#chapter_12) or any of the [Capabilities Transactions](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_8.9).

**Note:** Interested in [DIMSE](https://dicom.nema.org/medical/dicom/current/output/html/part07.html#sect_7.5) DICOM protocols? We have open sourced several adapters to allow ingestion and retrieval of DICOM data using protocols such as C-Store on [GitHub](https://github.com/GoogleCloudPlatform/healthcare-dicom-dicomweb-adapter).

## Retrieve transaction

The [Retrieve Transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.4) is a RESTful web service for retrieving DICOM imaging data.

The Retrieve Transaction supports the retrieving following resources:

  * DICOM Resources: 
    * Study
    * Series
    * Instance
    * Frames
    * Bulkdata
  * Metadata Resources 
    * Study
    * Series
    * Instance
  * Rendered Resources 
    * Instance
    * Frames



It does not support Thumbnail resources.

See [Quotas and limits](https://docs.cloud.google.com/healthcare-api/quotas) for details on quotas and limits for these methods.

### DICOM study/series/instances

The following Accept Headers are supported:

  * `multipart/related; type="application/dicom"; transfer-syntax=*`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.1` (default)
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.1.99`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.50`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.51`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.57`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.70`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.80`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.81`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.90`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.91`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.110`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.111`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.112`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.201`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.202`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.4.203`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.5`
  * `multipart/related; type="application/dicom"; transfer-syntax=1.2.840.10008.1.2.8.1`

**Warning:** The response's default transfer syntax is Little Endian Explicit. As a result, if the file was uploaded using a compressed transfer syntax, the returned object will be decompressed. This can negatively impact performance and lead to errors for transfer syntaxes that the Cloud Healthcare API doesn't support. To avoid these issues, and if the returned object's transfer syntax doesn't matter to your application, use the `multipart/related; type="application/dicom"; transfer-syntax=*` Accept Header.

### DICOM instances

In addition to the above Accept Headers, RetrieveInstance supports single part content types for convenience:

  * `application/dicom; transfer-syntax=*`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.1`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.1.99`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.50`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.51`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.57`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.70`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.80`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.81`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.90`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.91`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.110`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.111`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.112`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.201`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.202`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.4.203`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.5`
  * `application/dicom; transfer-syntax=1.2.840.10008.1.2.8.1`



This is not part of the official DICOMweb standard.

### DICOM frames

The following Accept Headers are supported:

  * `multipart/related; type="application/octet-stream"; transfer-syntax=*`
  * `multipart/related; type="application/octet-stream"; transfer-syntax=1.2.840.10008.1.2.1` (default)
  * `multipart/related; type="image/jpeg"; transfer-syntax=1.2.840.10008.1.2.4.50`
  * `multipart/related; type="image/jpeg"; transfer-syntax=1.2.840.10008.1.2.4.51`
  * `multipart/related; type="image/jpeg"; transfer-syntax=1.2.840.10008.1.2.4.57`
  * `multipart/related; type="image/jpeg"; transfer-syntax=1.2.840.10008.1.2.4.70`
  * `multipart/related; type="image/png"`
  * `multipart/related; type="image/jls"; transfer-syntax=1.2.840.10008.1.2.4.80`
  * `multipart/related; type="image/jls"; transfer-syntax=1.2.840.10008.1.2.4.81`
  * `multipart/related; type="image/jp2"; transfer-syntax=1.2.840.10008.1.2.4.90`
  * `multipart/related; type="image/jp2"; transfer-syntax=1.2.840.10008.1.2.4.91`
  * `multipart/related; type="image/jphc"; transfer-syntax=1.2.840.10008.1.2.4.201`
  * `multipart/related; type="image/jphc"; transfer-syntax=1.2.840.10008.1.2.4.202`
  * `multipart/related; type="image/jphc"; transfer-syntax=1.2.840.10008.1.2.4.203`
  * `multipart/related; type="image/jxl"; transfer-syntax=1.2.840.10008.1.2.4.110`
  * `multipart/related; type="image/jxl"; transfer-syntax=1.2.840.10008.1.2.4.112`
  * `multipart/related; type="image/dicom-rle"; transfer-syntax=1.2.840.10008.1.2.5`
  * `multipart/related; type="application/x-deflate"; transfer-syntax=1.2.840.10008.1.2.8.1`



A transfer syntax of `*` allows the user to request no transcoding be done, so the transfer syntax of the uploaded file will be used. For `application/octet-stream` the bulk data will be returned in whatever format it appears in the uploaded DICOM file.

### Rendered resources

The following Accept Headers are supported:

  * `image/jpeg` (default)
  * `image/png`



Only retrieving of Instance or Frame resources is supported.

No URL parameters are supported other than [Viewport](https://dicom.nema.org/medical/dicom/current/output/chtml/part18/sect_8.3.5.html#sect_8.3.5.1.3).

### Metadata resources

The following Accept Headers are supported:

  * `application/dicom+json` (default)
  * `multipart/related; type=application/dicom+xml`



Tags that are encoded as InlineBinary elements will be encoded using little-endian byte ordering, as the [transfer syntax parameter](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_8.7.3.5.2) is not supported on endpoints requesting metadata resources.

RetrieveMetadata will include BulkDataURIs for tags matching the [Bulkdata definition](https://docs.cloud.google.com/healthcare-api/docs/dicom#bulkdata-definition).

DICOM sequence tags containing more than approximately 1 MiB of data will not be returned in metadata resources. This limitation applies to metadata resources only. DICOM resources will still contain these tags.

### Bulkdata resources

The following Accept Headers are supported:

  * `multipart/related; type="application/octet-stream"; transfer-syntax=*` (default)
  * `application/octet-stream; transfer-syntax=*`



### Supported transfer syntaxes for transcoding

The above Accept headers describe what media types & transfer syntaxes you can request from the API, but this may not always be possible depending on the transfer syntax of the original file that was uploaded. In particular, transcoding is only possible from the following transfer syntaxes:

  * `1.2.840.10008.1.2` (Little Endian Implicit)
  * `1.2.840.10008.1.2.1` (Little Endian Explicit)
  * `1.2.840.10008.1.2.2` (Explicit VR Big Endian)
  * `1.2.840.10008.1.2.1.99` (Deflated Explicit VR Little Endian)
  * `1.2.840.10008.1.2.4.50` (JPEG Baseline Process 1)
  * `1.2.840.10008.1.2.4.51` (JPEG Extended)
  * `1.2.840.10008.1.2.4.57` (JPEG Lossless)
  * `1.2.840.10008.1.2.4.70` (JPEG Lossless Selection Value 1)
  * `1.2.840.10008.1.2.4.80` (JPEG-LS Lossless)
  * `1.2.840.10008.1.2.4.81` (JPEG-LS Near-Lossless)
  * `1.2.840.10008.1.2.4.90` (JPEG 2000 Lossless Only)
  * `1.2.840.10008.1.2.4.91` (JPEG 2000)
  * `1.2.840.10008.1.2.4.110` (JPEG XL Lossless)
  * `1.2.840.10008.1.2.4.111` (JPEG XL JPEG Recompression)
  * `1.2.840.10008.1.2.4.112` (JPEG XL)
  * `1.2.840.10008.1.2.4.201` (HTJ2K Lossless Only)
  * `1.2.840.10008.1.2.4.202` (HTJ2K Lossless Only with RPCL Options)
  * `1.2.840.10008.1.2.4.203` (HTJ2K)
  * `1.2.840.10008.1.2.5` (RLE Lossless)
  * `1.2.840.10008.1.2.8.1` (Deflated Image Frame Compression)



If the original file has a transfer syntax other than that in the above list and you request transcoding to another format, an error will be returned.

The Cloud Healthcare API cannot transcode non-monochrome images with bit depth greater than 8 to JPEG. Also, images with a Bits Allocated (0028, 0100) value of 1 or that are stored in either Float Pixel Data (7FE0,0008), Double Float Pixel Data (7FE0,0009) tags can only be transcoded between native formats.

In order to disable transcoding and retrieve any file from the API you can set `transfer-syntax=*` in your Accept header.

### Status codes

Code | Meaning  
---|---  
200 (OK) | The response payload contains representations for all of the Target Resource(s).  
400 (Bad Request) | The request was invalid (e.g. bad query parameters or headers) for the specified Target Resource(s) (e.g. missing pixel data).  
401 (Unauthorized) | The request is missing authentication credentials.  
403 (Permission Denied) | The authenticated user doesn't have access to this resource (or the resource doesn't exist).  
406 (Not Acceptable) | The server doesn't support any of the Acceptable Media Types.  
429 (Too Many Requests) | The client is exceeding its [quota](https://docs.cloud.google.com/healthcare-api/quotas).  
503 (Service Unavailable) | The server is currently unavailable or the request exceeded its deadline.  
  
## Store transaction

The [Store Transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.5) is a RESTful web service for storing DICOM imaging data.

The store transaction either accepts Part 10 DICOM binary files directly or it accepts splitting of a DICOM file into metadata (represented in JSON) and bulk data. These 2 versions have different semantics that are described in the following sections.

See [Quotas and limits](https://docs.cloud.google.com/healthcare-api/quotas) for details on quotas and limits for this method.

### DICOM part 10 binary files

The following Content-Types are supported:

  * `multipart/related; type=application/dicom`
  * `application/dicom`



No coercing or replacing of attributes is done by the server.

This version accepts all transfer-syntaxes and SOP classes. Only minimal validation of the DICOM file is done to extract some key metadata attributes.

Note that for convenience, the Store Transaction also accepts a single part HTTP request with a single DICOM instance with content type `application/dicom`. This is not part of the official DICOMweb standard.

See [Store a DICOM instance](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#store-dicom) for the associated how-to guide.

### JSON metadata and bulk data requests

When storing instances using JSON metadata and bulk data, the first multipart part must consist of a [JSON array of DICOM instances](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#chapter_F).

The first part must have a Content-Type of `application/dicom+json; transfer-syntax=TransferSyntaxUID` where `TransferSyntaxUID` is the transfer syntax which was used to encode binary data in [InlineBinary](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_F.2.7) objects. If no InlineBinary objects are present in the metadata, the `transfer-syntax` parameter can be omitted.

The following DICOM elements are required to be present in every instance in the JSON metadata:

  * SpecificCharacterSet
  * TransferSyntaxUID
  * SOPClassUID
  * StudyInstanceUID
  * SeriesInstanceUID
  * SOPInstanceUID



The SpecificCharacterSet element must be set to `ISO_IR 192`, and the JSON metadata must be encoded in unicode UTF-8. The TransferSyntaxUID can be set to any valid transfer syntax, except for the following unsupported transfer syntaxes:

  * `1.2.840.10008.1.2.2` (Explicit VR Big Endian)
  * `1.2.840.10008.1.2.1.99` (Deflated Explicit VR Little Endian)



Within the JSON metadata, the user can specify multiple BulkDataURIs for DICOM tags with VRs of OB, OW, or UN. These BulkDataURIs indicate that the binary data for the tag which contains the URI will be sent in a following part which has the Content-Location header set to the BulkDataURI.

Each instance in the JSON metadata can have at most one BulkDataURI. There must not be any duplicate BulkDataURIs in the JSON metadata. Compressed image bulk data must only be sent for the PixelData tag, and when sent, the transfer syntax specified in the bulk data part must match the value of the instance's TransferSyntaxUID element.

The following Content-Types are supported for bulk data parts:

  * `application/octet-stream`
  * `image/jpeg; transfer-syntax=1.2.840.10008.1.2.4.70`
  * `image/jpeg; transfer-syntax=1.2.840.10008.1.2.4.50`
  * `image/jpeg; transfer-syntax=1.2.840.10008.1.2.​4.​51`
  * `image/jpeg; transfer-syntax=1.2.840.10008.1.2.​4.​57`
  * `image/dicom-rle; transfer-syntax=1.2.840.10008.1.2.5`
  * `image/jls; transfer-syntax=1.2.840.10008.1.2.​4.​80`
  * `image/jls; transfer-syntax=1.2.840.10008.1.2.4.81`
  * `image/jp2; transfer-syntax=1.2.840.10008.1.2.4.90`
  * `image/jp2; transfer-syntax=1.2.840.10008.1.2.4.91`
  * `image/jpx; transfer-syntax=1.2.840.10008.1.2.4.92`
  * `image/jpx; transfer-syntax=1.2.840.10008.1.2.4.93`



An alternative method to specify binary data is to encode it as an InlineBinary base64 encoded string. This is supported for all tags except PixelData, which must be sent as a bulk data part. When InlineBinary objects are used in the JSON metadata, the transfer syntax which was used for encoding must be specified in the Content-Type of the JSON metadata part.

The server doesn't derive [image pixel description macro attributes](https://dicom.nema.org/medical/dicom/current/output/html/part03.html#table_C.7-11c).

See [Create DICOM instances from JSON metadata and JPEG files](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#create-dicom-instance-metadata) for the associated how-to guide.

### Response

On an error, either an additional FailureDetail (0009, 0097) tag (for XML responses) or FailureDetailJSON (0009,1097) tag (for JSON responses) will be returned. The FailureDetail tag provides a human-readable description of the error.

If a DICOM instance has the same `<StudyInstanceUID, SeriesInstanceUID, SOPInstanceUID>` tuple as another instance already in the DICOM store, a [Processing failure](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#table_I.2-2) error is returned with an "already exists" FailureDetail tag.

The response can be in either JSON or XML format which can be controlled via the following Accept header values:

  * `application/dicom+xml` (default)
  * `application/dicom+json`



### Status codes

Code | Meaning  
---|---  
200 (OK) | The resource was successfully stored.  
400 (Bad Request) | The request was invalid (e.g. unsupported media type or transfer syntax).  
401 (Unauthorized) | The request is missing authentication credentials.  
403 (Permission Denied) | The authenticated user doesn't have access to this resource (or the resource doesn't exist).  
406 (Not Acceptable) | The server doesn't support any of the Acceptable Media Types.  
409 (Conflict) | At least one resource wasn't successfully stored (e.g. invalid DICOM file). Check the FailureDetail tag in the response body for more information.  
429 (Too Many Requests) | The client is exceeding its [quota](https://docs.cloud.google.com/healthcare-api/quotas).  
503 (Service Unavailable) | The server is currently unavailable or the request exceeded its deadline.  
  
## Search transaction

The [Search Transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.6) is a RESTful web service for querying DICOM imaging metadata.

The Cloud Healthcare API supports searching for studies, series and instances.

### Search parameters

Searching by the following tags is supported:

  * Studies: 
    * StudyInstanceUID
    * PatientName
    * PatientID
    * AccessionNumber
    * ReferringPhysicianName
    * StudyDate
  * Series: all study level search terms and 
    * SeriesInstanceUID
    * Modality
  * Instances: all study/series level search terms and 
    * SOPInstanceUID



Only single value, exact matching is supported, except for StudyDate which supports range queries and PatientName which supports fuzzy matching.

**Warning:** [Part 6 of the DICOM standard](https://dicom.nema.org/medical/dicom/current/output/chtml/part06/chapter_6.html) specifies that the tags in the preceding list must have a VM of 1 and the specified VR. While the Cloud Healthcare API doesn't block ingestion of non-conformant instances (VM greater than 1 or incorrect VR for the preceding tags), they may not be searchable.

The following additional URL parameters are supported:

  * `fuzzymatching`: If set to `true`, fuzzy matching will be applied to the PatientName tag. Fuzzy matching will perform tokenization and normalization of both the value of PatientName in the query and the stored value. It will match if any search token is a prefix of any stored token. For example, if PatientName is "John^Doe", then "jo", "Do" and "John Doe" will all match. However "ohn" will not match.
  * `includefield`: Can be set to a comma-separated list of attributeIDs, such as DICOM tag IDs or keywords, or set to the value `all` to return all available tags. For a list of available tags, see Returned results.



Paging is supported using the `limit` and `offset` query parameters. There is no Warning response header if no more results are available. You must execute an extra query to determine if there are more results.

  * `limit`: Maximum number of results that should be returned, up to a maximum of 5,000 for studies/series and 50,000 for instances. The default number of results is 100 for studies/series and 1,000 for instances.

  * `offset`: Number of results to skip in the beginning up to a maximum of 1,000,000.




Timezone Offset From UTC is not supported.

### Returned results

The response can be in either JSON or XML format which can be controlled using the following Accept header values:

  * `application/dicom+json` (default)
  * `multipart/related; type=application/dicom+xml`



By default the following attributes will be returned:

  * Studies: 
    * SpecificCharacterSet
    * StudyDate
    * StudyTime
    * AccessionNumber
    * InstanceAvailability
    * ReferringPhysicianName
    * TimezoneOffsetFromUTC
    * PatientName
    * PatientID
    * PatientBirthDate
    * PatientSex
    * StudyInstanceUID
    * StudyID
  * Series: 
    * SpecificCharacterSet
    * Modality
    * TimezoneOffsetFromUTC
    * SeriesDescription
    * SeriesInstanceUID
    * PerformedProcedureStepStartDate
    * PerformedProcedureStepStartTime
    * RequestAttributesSequence
  * Instances: 
    * SpecificCharacterSet
    * SOPClassUID
    * SOPInstanceUID
    * InstanceAvailability
    * TimezoneOffsetFromUTC
    * InstanceNumber
    * Rows
    * Columns
    * BitsAllocated
    * NumberOfFrames



For `includefield=all`, the default attributes will be returned along with the following attributes:

  * Studies: 
    * PersonIdentificationCodeSequence
    * PersonAddress
    * PersonTelephoneNumbers
    * PersonTelecomInformation
    * InstitutionName
    * InstitutionAddress
    * InstitutionCodeSequence
    * ReferringPhysicianIdentificationSequence
    * ConsultingPhysicianName
    * ConsultingPhysicianIdentificationSequence
    * IssuerOfAccessionNumberSequence
    * LocalNamespaceEntityID
    * UniversalEntityID
    * UniversalEntityIDType
    * StudyDescription
    * PhysiciansOfRecord
    * PhysiciansOfRecordIdentificationSequence
    * NameOfPhysiciansReadingStudy
    * PhysiciansReadingStudyIdentificationSequence
    * RequestingServiceCodeSequence
    * ReferencedStudySequence
    * ProcedureCodeSequence
    * ReasonForPerformedProcedureCodeSequence
  * Series: 
    * SeriesNumber
    * Laterality
    * SeriesDate
    * SeriesTime
  * Instances: all attributes present in the DICOM instance, excluding the following exceptions.



DICOM sequence tags containing more than approximately 1 MiB of data will not be returned in the metadata response.

### Inconsistent/invalid metadata

In the case of SearchForStudies/SearchForSeries there is a potential for inconsistent study/series level metadata across multiple instances. For example, two instances could be uploaded with the same StudyInstanceUID but have different StudyDates. In this case, the search behavior is not well defined. Searching by that value may work in some cases, but not others and the returned value may vary across different calls.

### Status codes

Code | Meaning  
---|---  
200 (OK) | The response payload contains representations for all of the Target Resource(s).  
400 (Bad Request) | The request was invalid (e.g. invalid query parameters).  
401 (Unauthorized) | The request is missing authentication credentials.  
403 (Permission Denied) | The authenticated user doesn't have access to this resource (or the resource doesn't exist).  
406 (Not Acceptable) | The server doesn't support any of the Acceptable Media Types.  
429 (Too Many Requests) | The client is exceeding its [quota](https://docs.cloud.google.com/healthcare-api/quotas).  
503 (Service Unavailable) | The server is currently unavailable or the request exceeded its deadline.  
  
## Deletion

The Cloud Healthcare API supports the following proprietary action types:

  * DeleteStudy
  * DeleteSeries
  * DeleteInstance



These use the same request paths as their WADO-RS counterparts (RetrieveStudy, RetrieveSeries, and RetrieveInstance, respectively). Instead of an HTTP `GET` request, a `DELETE` request is used. The effect is that the specified study, series, or instance is deleted along with all the DICOM resources contained in it.

The [`DeleteStudy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies/delete) and [`DeleteSeries`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series/delete) methods return a long running operation which deletes all of the instances in the study or series. Please note that instances cannot be inserted into a study or series that is being deleted by an operation until the operation completes.

See [Managing long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations) for a how-to guide on operations.

A successful [`DeleteInstance`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances/delete) request returns an empty response.

**Warning:** Study and series search results can take a few seconds to be updated after an instance is deleted using DeleteInstance.

### Status codes

Code | Meaning  
---|---  
200 (OK) | The request resource was deleted.  
400 (Bad Request) | The request was invalid.  
401 (Unauthorized) | The request is missing authentication credentials.  
403 (Permission Denied) | The authenticated user doesn't have access to this resource (or the resource doesn't exist).  
429 (Too Many Requests) | The client is exceeding its [quota](https://docs.cloud.google.com/healthcare-api/quotas).  
503 (Service Unavailable) | The server is currently unavailable or the request exceeded its deadline.  
  
## Accept headers

Some of the above methods provide the ability to control the response format using HTTP Accept headers. Wildcard matching is supported at both the top level (e.g. `*/*`) and subtype (e.g. `image/*`). Specifying a `q` value is also supported to indicate relative preference. If a `q` value is not specified for an Accept header, it is set to the default value of 1.0.

In the event that multiple Accept headers are specified and there is a tie between the highest preference Accept headers, the server will choose the Accept header. Clients should not depend on the server's choice of Accept header in this scenario.

## Supported SOP classes

The Cloud Healthcare API can ingest and do basic retrieval of all DICOM SOP classes. For any retrieval that requires transcoding between image formats, see supported transfer syntaxes for transcoding for a list of supported transfer syntaxes.

## DICOM Dictionary Version

The Cloud Healthcare API uses the [DICOM 2026b dictionary](https://dicom.nema.org/medical/dicom/current/output/html/part06.html) for parsing tags of ingested instances and for generating column names when exporting to BigQuery.

## Bulkdata Definition

When retrieving metadata, the Cloud Healthcare API will exclude certain tags that are defined as bulkdata. Instead, these tags will be returned alongside metadata with a BulkDataURI that allows the user to retrieve contents of these tags (see [`RetrieveBulkdata`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances.bulkdata/retrieveBulkdata)). The following is the definition used by the Cloud Healthcare API:

  * Any non-sequence tag exceeding 100 MiB in size.
  * Any Pixel Data tag: (7FE0,0008), (7FE0,0009) (7FE0,0010).
  * Any tag with a VR of OB, OW, or UN.
  * A tag with a VR of OD, OF, OL, or OV that is larger than 2 KiB. 
    * For legacy reasons, tags of instances already ingested into the Cloud Healthcare API might be considered bulkdata if the tag is larger than 256 B (OF and OL) or 512 B (OD).
  * A tag with a VR of AT, FD, FL, UL, US, SV, or UV and has a Value Multiplicity (VM) greater than 512. 
    * For legacy reasons, tags of instances already ingested into the Cloud Healthcare API may be considered bulkdata if the VM is greater than 64.



In addition, the following tags are considered bulkdata, but don't have BulkDataURIs when returned from metadata methods, and contents cannot be retrieved using [`RetrieveBulkdata`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances.bulkdata/retrieveBulkdata):

  * A tag with a VR of SQ and a size greater than approximately 1 MiB.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
