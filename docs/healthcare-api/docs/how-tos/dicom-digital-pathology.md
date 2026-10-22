---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-digital-pathology/
title: Using the Cloud Healthcare API for digital pathology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:32.656392+00:00
---

# Using the Cloud Healthcare API for digital pathology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-digital-pathology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Using the Cloud Healthcare API for digital pathology Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to store, access, visualize, and use digital pathology whole slide images (WSIs) using the Cloud Healthcare API.

## Overview

[Digital pathology](https://en.wikipedia.org/wiki/Digital_pathology) is transforming medical imaging by enabling conventional glass slides to be archived, visualized, and evaluated across digital workflows. Among its many benefits, digital pathology enables rapid consultation, empowers patients with greater access and understanding, and enhances clinical and research workflows by enabling pathology imaging to be a data source for state of the art AI.

Whole slide digital pathology is represented as a collection of images. The largest of these are typically several gigabytes in size. [DICOM](https://www.dicomstandard.org/) is the interoperable standard for digital pathology and enables whole slide imaging and its associated metadata to be efficiently stored, referenced from electronic health records (e.g., [FHIR](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir)), and accessed through high performance vendor neutral APIs.

The DICOM representation for digital pathology has been designed to support high performance interactive use cases which require the ability to rapidly pan and zoom across gigapixel images. DICOM represents [whole slide digital pathology](https://pubmed.ncbi.nlm.nih.gov/30533276/) as an image pyramid. Levels of the pyramid correspond with magnifications of the whole slide imaging. The imaging represented within a pyramid level is stored as a collection of smaller images, frames. The standard defines APIs that enable image [storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#store-dicom), [search](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#search-dicom) (discovery of available imaging), [metadata retrieval](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#retrieve-metadata), and image retrieval [entire pyramid level](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#retrieve-instance) (magnification) or select [sub-regions (frames)](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances.frames/retrieveFrames) within a pyramid level.

The DICOM APIs supports metadata responses in [JSON and XML](https://docs.cloud.google.com/healthcare-api/docs/dicom#metadata_resources) and the Cloud Healthcare API additionally supports metadata access through [BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-export-bigquery#querying_and_analyzing_dicom_data_in) to enable complex relational queries that join the DICOM metadata with other data sources. Imaging can be returned as stored or [converted](https://docs.cloud.google.com/healthcare-api/docs/dicom#dicom_instances) (transcoded) to alternative formats.

## Generating whole slide DICOM imaging

A growing number of digital pathology slide scanners support generating DICOM imaging directly from the slide scanner. In many cases slide scanner produced DICOM can be ingested directly into the Cloud Healthcare API using either the [DICOMweb](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb) or [DIMSE](https://github.com/GoogleCloudPlatform/healthcare-dicom-dicomweb-adapter) DICOM APIs. If the DICOM producing slide scanners is not connected to a Laboratory Information System (LIS) then it may be necessary to augment the non-pixel metadata in DICOM to add (e.g., patient) or modify (e.g., Study Instance UID) metadata prior to its use within a clinical imaging PACS.

Historically, slide scanners have generated imaging in proprietary formats. The [transformation pipeline](https://github.com/GoogleCloudPlatform/medical-imaging/tree/main/pathology/transformation_pipeline), can be used to transform OpenSlide supported formats to DICOM, merge custom metadata with the generated DICOM, and ingest the generated DICOM directly into the Cloud Healthcare API. This solution has been used to support the transformation of multi-petabyte archives to DICOM.

Tools that can be used to convert digital pathology imaging to DICOM include:

  * [Open Source Google Transformation Pipeline](https://github.com/GoogleCloudPlatform/medical-imaging/tree/main/pathology/transformation_pipeline)
  * [Orthanc "Dicomizer" command-line tool](https://www.orthanc-server.com/static.php?page=wsi)
  * [PixelMed™ Java DICOM Toolkit](http://www.pixelmed.com/dicomtoolkit.html)



DICOM instances can be programmatically imported into the Cloud Healthcare API using: [DICOMweb](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#store-dicom), [DIMSE](https://github.com/GoogleCloudPlatform/healthcare-dicom-dicomweb-adapter), and from [Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export).

## Image storage tiering

The Cloud Healthcare API supports [storage tiering](https://docs.cloud.google.com/healthcare-api/docs/dicom-storage-class) at the granularity of a DICOM instance. For whole slide imaging this means each magnification of a digital pathology image pyramid can be stored at the tier which best matches its expected use. The storage tier of a DICOM instance affects the cost of the data storage, retrieval, and, in some cases, deletion. Storage tiering does not affect data access performance. By default all DICOM instances are stored at the standard storage tier. The Cloud Healthcare API provides an [API](https://docs.cloud.google.com/healthcare-api/docs/dicom-storage-class#change-storage) to view and change the storage class for DICOM instances. In addition, an [image lifecycle management (ILM)](https://github.com/GoogleCloudPlatform/medical-imaging/tree/main/ilm) solution can be used to automate the movement of DICOM instances between storage tiers based on heuristics. The solution can automate the graduation of a DICOM instance through storage tiers based on its size, age, and access patterns.

NOTE: Archival storage increases the cost of pixel data retrieval. Data retrieval charges are paid against the size of the data retrieved and not the size of the data stored. For whole slide imaging this is an important distinction as pixel data can be retrieved using both frame and instance level APIs. Retrieving archival imaging using frame APIs can be particularly advantageous, from a cost perspective, when a subset of an instance's frames are required as data retrieval charges will be made based on the size of the returned data and not the stored instance's size.

## Interactive visualization

The Cloud Healthcare API can be used to support interactive visualization of whole slide imaging for applications which range from zero footprint web viewers (JavaScript) to stand alone client applications. The following open source viewers were tested to be compatible with the Cloud Healthcare API:

  * [Open Source Google Viewer](https://github.com/GoogleCloudPlatform/medical-imaging/tree/main/pathology/viewer): Open source, zero-footprint digital pathology viewer created by Google Research.

  * [Slim (MGH)](https://github.com/MGHComputationalPathology/slim#google-cloud-platform): Open source, zero-footprint digital pathology viewer that supports the [NIH Imaging Data Commons](https://portal.imaging.datacommons.cancer.gov/explore/).

  * [OHIF](https://docs.ohif.org/deployment/google-cloud-healthcare/)

  * [QuPath](https://github.com/GoogleCloudPlatform/qupath-chcapi-extension): Open source desktop application.




### Improving interactive visualization performance

The Digital Pathology DICOM Proxy is a Google Research solution that you can use to improve frame-serving performance for interactive whole slide imaging applications. When deployed, the Digital Pathology DICOM proxy wraps the Cloud Healthcare API and performs just-in-time frame caching to preferentially serve frame images from an in-memory [Memorystore for Redis cache](https://docs.cloud.google.com/memorystore/docs/redis).

### Whole slide imaging color normalization

The DICOM standard requires that WSIs contain an ICC color profile defining the [color space](https://en.wikipedia.org/wiki/Color_space) of the slide scanner that acquired the images. This color space can differ noticeably from the color space used by displays or other slide scanners. If visualized without the embedded ICC profile, the color of images often appears substantially more or less saturated than expected. The Cloud Healthcare API provides APIs to retrieve the ICC profile embedded in a DICOM instance and to transform retrieved images to a reference color space.

  * You can retrieve the ICC profile embedded in a DICOM instance using the bulk data API or the instance retrieval API. You can then transform images retrieved in the slide scanner color space using libraries like [Little-CMS](https://littlecms.com/color-engine/)(written in C++) and [Pillow](https://pillow.readthedocs.io/en/stable/reference/ImageCms.html) (written in Python).

  * The EZ-WSI DICOMweb Python library supports ICC profile transformation as part of its image retrieval and machine learning embedding generation APIs.




## Machine learning

[Path Foundation](https://developers.google.com/health-ai-developer-foundations/path-foundation) is a foundation model developed by Google Research to accelerate machine learning (ML) development in digital pathology.

The model converts a patch (a sub-region) of pathology imaging into an embedding, which is a list of floating-point numbers. This embedding serves as a machine-learned representation of the image. Using image embeddings as input data can help reduce the total amount of data and compute resources required to develop effective ML models.

You can deploy Path Foundation to Google Cloud from [Model Garden](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden/path-foundation). It's also available as open source with open weights on [Hugging Face](https://huggingface.co/google/path-foundation).

To assist with embedding generation, the [EZ-WSI DICOMweb open source Python library](https://github.com/GoogleCloudPlatform/EZ-WSI-DICOMweb) includes interfaces (see the [Getting Started Guide For Generating Pathology Embeddings Colab notebook](https://colab.research.google.com/github/GoogleCloudPlatform/EZ-WSI-DICOMweb/blob/main/ez_wsi_dicomweb/documentation/getting_started_with_embeddings.ipynb)) that simplify the transformation of imaging stored in the Cloud Healthcare API into embeddings. See the [Train a Digital Pathology Linear Classifier From Images Stored on DICOM Colab notebook](https://colab.research.google.com/github/google-health/path-foundation/blob/master/notebooks/train_data_efficient_classifier_dicom.ipynb) for information on how to use EZ-WSI DICOMweb and Pathology Foundations to train a linear classifier from whole slide DICOM imaging.

## Programmatically retrieving metadata and pixel imaging

This section describes methods to retrieve digital pathology metadata and imaging from the Cloud Healthcare API.

### DICOM information model

DICOM uses three Unique Identifiers (UIDs) to uniquely identify imaging:

  * Study Instance UID: Identifies all imaging acquired or generated from a single patient exam.
  * Series Instance UID: Identifies each medical image acquisition within that exam (for example, a unique scan of a pathology slide).
  * SOP Instance UID: Identifies each image acquired or generated as part of that acquisition.



For example, slide scanners often generate multiple images to capture a complete glass slide. These images can include:

  * The imaged tissue area at various magnifications.
  * The slide label.
  * An image of the entire slide.
  * Data describing the slide scanning operation.



### Listing digital pathology DICOM series

To identify slide microscopy images, search for DICOM series where the [Modality](https://dicom.nema.org/medical/Dicom/2024d/output/chtml/part16/sect_CID_29.html) tag (0008,0060) is `SM`. You can use the [`dicomStores.searchForSeries`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/searchForSeries) method for this search.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the DICOM store's parent dataset
  * DICOM_STORE_ID: the DICOM store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/series?Modality=SM"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/series?Modality=SM" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/searchForSeries). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    [
      {
        "00080005": {
          "vr": "CS",
          "Value": [
            "SPECIFIC_CHARACTER_SET"
          ]
        },
        "00080020": {
          "vr": "DA",
          "Value": [
            "STUDY_DATE"
          ]
        },
        "00080030": {
          "vr": "TM"
        },
        "00080050": {
          "vr": "SH",
          "Value": [
            "ACCESSION_NUMBER"
          ]
        },
        "00080060": {
          "vr": "CS",
          "Value": [
              "SM"
          ]
        },
        "00080090": {
          "vr": "PN"
        },
        "00100010": {
          "vr": "PN"
        },
        "00100020": {
          "vr": "LO",
          "Value": [
            "PATIENT_ID"
          ]
        },
        "00100030": {
          "vr": "DA"
        },
        "00100040": {
          "vr": "CS"
        },
        "0020000D": {
          "vr": "UI",
          "Value": [
            "STUDY_INSTANCE_UID"
          ]
        },
        "0020000E": {
          "vr": "UI",
          "Value": [
          "SERIES_INSTANCE_UID"
          ]
        },
        "00200010": {
          "vr": "SH"
        }
      }
    ]
    

### Retrieving digital pathology DICOM metadata

A DICOM series for whole slide imaging usually contains multiple instances. These DICOM instances can represent different levels of the image pyramid or additional regions of the imaged slide.

To view the instance metadata for an instance in the study, call the [`dicomStores.searchForInstances`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/searchForInstances) method:

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the DICOM store's parent dataset
  * DICOM_STORE_ID: the DICOM store ID
  * STUDY_INSTANCE_UID: the study instance unique identifier (UID)



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/instances?StudyInstanceUID=STUDY_INSTANCE_UID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/instances?StudyInstanceUID=STUDY_INSTANCE_UID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/searchForInstances). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    [
      {
        "00080005": {
          "vr": "CS",
          "Value": [
            "SPECIFIC_CHARACTER_SET"
          ]
        },
        "00080016": {
          "vr": "UI",
          "Value": [
            "SOP_CLASS_UID"
          ]
        },
        "00080018": {
          "vr": "UI",
          "Value": [
            "SOP_INSTANCE_UID"
          ]
        },
        "00080020": {
          "vr": "DA",
          "Value": [
            "STUDY_DATE"
          ]
        },
        "00080030": {
          "vr": "TM"
        },
        "00080050": {
          "vr": "SH",
          "Value": [
            "ACCESSION_NUMBER"
          ]
        },
        "00080060": {
          "vr": "CS",
          "Value": [
            "MODALITY"
          ]
        },
        "00080090": {
          "vr": "PN"
        },
        "00100010": {
          "vr": "PN"
        },
        "00100020": {
          "vr": "LO",
          "Value": [
            "PATIENT_ID"
          ]
        },
        "00100030": {
          "vr": "DA"
        },
        "00100040": {
          "vr": "CS"
        },
        "0020000D": {
          "vr": "UI",
          "Value": [
            "STUDY_INSTANCE_UID"
          ]
        },
        "0020000E": {
          "vr": "UI",
          "Value": [
            "SERIES_INSTANCE_UID"
          ]
        },
        "00200010": {
          "vr": "SH"
        },
        "00200013": {
          "vr": "IS",
          "Value": [
            INSTANCE_NUMBER
          ]
        },
        "00280010": {
          "vr": "US",
          "Value": [
            ROWS
          ]
        },
        "00280011": {
          "vr": "US",
          "Value": [
            COLUMNS
          ]
        },
        "00280100": {
          "vr": "US",
          "Value": [
            BITS_ALLOCATED
          ]
        },
        "00400244": {
          "vr": "DA",
          "Value": [
            "PERFORMED_PROCEDURE_STEP_START_DATE"
          ]
        }
      },
    ...
    ]
    

### Retrieving whole slide imaging pixel data

You can programmatically retrieve whole slide imaging pixel data using DICOMweb. The Cloud Healthcare API also supports retrieval through a DICOM adapter using DIMSE protocols.

Most whole slide images are multi-frame images. For these, the Cloud Healthcare API provides direct access to pixel data using the DICOM frame and rendered frame APIs.

Alternatively, you can retrieve pixel data indirectly by fetching an entire DICOM instance and then programmatically decoding the encoded frames from that instance.

Performance considerations for retrieving frames:

  * Retrieving an entire instance is generally faster per frame than batch frame retrieval.
  * Batch frame retrieval is generally faster than retrieving individual frames.



#### EZ-WSI DICOMweb

[EZ-WSI DICOMweb](https://github.com/GoogleCloudPlatform/EZ-WSI-DICOMweb) is an open source Python library. It simplifies retrieving digital pathology pixel data from the Cloud Healthcare API by abstracting the underlying DICOMweb calls. The library can help accelerate frame retrieval in many use cases by converting serial image requests into batch requests. Batch retrieval of frame data often reduces the total time and DICOM store quota required.

A [Colab notebook](https://colab.research.google.com/github/GoogleCloudPlatform/EZ-WSI-DICOMweb/blob/main/ez_wsi_demo.ipynb) demonstrating the library is available.

#### DICOMweb instance retrieval API

The [DICOMweb Instance Retrieval API](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances/retrieveInstance) returns a binary DICOM instance. This instance contains all the metadata and pixel data stored within it.

You can decode the returned binary data using various libraries, such as:

  * [PyDicom](https://pydicom.github.io/) (Python)
  * [Dcm4che](https://web.dcm4che.org/) (Java)
  * [libdicom](https://libdicom.readthedocs.io/en/latest/) (C)
  * [DCMTK](https://dicom.offis.de/dcmtk.php.en) (C/C++)
  * [OpenSlide](https://github.com/openslide/openslide) (Python/C)



### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the DICOM store's parent dataset
  * DICOM_STORE_ID: the DICOM store ID
  * STUDY_INSTANCE_UID: the study instance unique identifier
  * SERIES_INSTANCE_UID: the series instance unique identifier
  * INSTANCE_UID: the instance unique identifier
  * OUTPUT_FILE: file to write the DICOM instance to.



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Accept: application/dicom" \  
         --output OUTPUT_FILE \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "Accept" = "application/dicom" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -OutFile OUTPUT_FILE `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID"

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/searchForSeries). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The `OUTPUT_FILE` file should be populated with content

#### DICOMweb frame API

The [DICOMweb frame API](https://docs.cloud.google.com/healthcare-api/docs/how-tos/\(/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances.frames/retrieveFrames\)) enables retrieval of one or more frames from a DICOM instance. Pixel data retrieved using the API may be requested [transcoded](https://docs.cloud.google.com/healthcare-api/docs/dicom#dicom_frames) to formats other than what is stored natively within the DICOM store.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the DICOM store's parent dataset
  * DICOM_STORE_ID: the DICOM store ID
  * STUDY_INSTANCE_UID: the study instance unique identifier
  * SERIES_INSTANCE_UID: the series instance unique identifier
  * INSTANCE_UID: the instance unique identifier
  * FRAMES: the frame numbers to retrieve pixel data



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Accept: multipart/related; type="image/jpeg"; transfer-syntax=1.2.840.10008.1.2.4.50" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID/frames/FRAMES"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "Accept" = "multipart/related; type="image/jpeg"; transfer-syntax=1.2.840.10008.1.2.4.50" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID/frames/FRAMES" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/searchForSeries). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a multipart response that encodes the requested imaging. 

#### DICOMweb rendered frame API

The [DICOMweb rendered frame](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances.frames/retrieveRendered) API enables server side conversion of frame to a [standard image format](https://docs.cloud.google.com/healthcare-api/docs/dicom#rendered_resources) (e.g., JPEG and PNG).

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the DICOM store's parent dataset
  * DICOM_STORE_ID: the DICOM store ID
  * STUDY_INSTANCE_UID: the study instance unique identifier
  * SERIES_INSTANCE_UID: the series instance unique identifier
  * INSTANCE_UID: the instance unique identifier
  * FRAME: the frame number to retrieve pixel data



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Accept: image/png" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID/frames/FRAME/rendered"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "Accept" = "image/png" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID/frames/FRAME/rendered" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/searchForSeries). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a binary response that encodes the requested imaging. 

### Using retrieve bulk data to retrieve an ICC profile embedded within a DICOM instance

You can use the [DICOMweb retrieve bulkdata](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores.studies.series.instances.bulkdata/retrieveBulkdata) to directly retrieve ICC (International Color Consortium) profile bytes embedded within a DICOM instance. 

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the DICOM store's parent dataset
  * DICOM_STORE_ID: the DICOM store ID
  * STUDY_INSTANCE_UID: the study instance unique identifier
  * SERIES_INSTANCE_UID: the series instance unique identifier
  * INSTANCE_UID: the instance unique identifier
  * OUTPUT_FILE: file to write the icc profile instance to.



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Accept: application/octet-stream; transfer-syntax=*" \  
         --output OUTPUT_FILE \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID/bulkdata/00480105/0/00282000"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "Accept" = "application/octet-stream; transfer-syntax=*" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -OutFile OUTPUT_FILE `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID/bulkdata/00480105/0/00282000"

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores/searchForSeries). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

The `OUTPUT_FILE` file should be populated with content

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
