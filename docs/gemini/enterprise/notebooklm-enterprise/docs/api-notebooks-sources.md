---
url: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources/
title: Add and manage data sources in a notebook (API) \u00a0|\u00a0 Gemini Notebook Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:00.287045+00:00
---

# Add and manage data sources in a notebook (API)  |  Gemini Notebook Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Notebook Enterprise ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs)



Send feedback 

#  Add and manage data sources in a notebook (API) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After you have created your notebook, you can add various content types to it as data sources. You can do so in batches or as single files. Some of the sources include Google Docs, Google Slides, raw text, web content, and YouTube videos.

This page describes how to perform the following tasks:

  * Add data sources in a batch
  * Upload a file as a source
  * Retrieve a source
  * Delete data sources from a notebook



## Before you begin

If you plan to add Google Docs or Google Slides as your data source, you must authorize access to Google Drive using Google user credentials. To do so, run the following [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login#--enable-gdrive-access) command and follow the instructions in the CLI.
    
    
    gcloud auth login --enable-gdrive-access
    

## Add data sources in a batch

To add sources to a notebook, call the [`notebooks.sources.batchCreate`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchCreate) method.

### REST
    
    
    curl -X POST \
      -H "Authorization:Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
         "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/notebooks/NOTEBOOK_ID/sources:batchCreate" \
      -d '{
      "userContents": [
        {
        USER_CONTENT
        }
       ]
      }'
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `LOCATION`: the geographic location of your data store, such as `global`. For more information, see [Locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations). 
  * `NOTEBOOK_ID`: The unique identifier of the notebook.
  * `USER_CONTENT`: The data source content.



You can add only one of the following data sources as your content:

  * For Google Drive content consisting of Google Docs or Google Slides, add:
        
        "googleDriveContent": {
           "documentId": "DOCUMENT_ID_GOOGLE",
           "mimeType": "MIME_TYPE",
           "sourceName": "DISPLAY_NAME_GOOGLE"
         }
        

Replace the following:

    * `DOCUMENT_ID_GOOGLE`: the ID of the file that's in the Google Drive. This ID appears in the URL of the file. To get the document ID of a file, open the file. Its URL has the pattern: `https://docs.google.com/FILE_TYPE/d/DOCUMENT_ID_GOOGLE/edit?resourcekey=RESOURCE_KEY`.
    * `MIME_TYPE`: the mime type of the selected document. Use `application/vnd.google-apps.document` for Google Docs or `application/vnd.google-apps.presentation` for Google Slides.
    * `DISPLAY_NAME_GOOGLE`: the display name of the data source.
  * For raw text input, add:
        
        "textContent": {
            "sourceName": "DISPLAY_NAME_TEXT",
            "content": "TEXT_CONTENT"
          }
        

Replace the following:

    * `DISPLAY_NAME_TEXT`: the display name of the data source.
    * `TEXT_CONTENT`: the raw text content that you want to upload as a data source.
  * For web content, add:
        
        "webContent": {
           "url": "URL_WEBCONTENT",
           "sourceName": "DISPLAY_NAME_WEB"
         }
        

Replace the following:

    * `URL_WEBCONTENT`: the URL of the content that you want to upload as a data source.
    * `DISPLAY_NAME_WEB`: the display name of the data source.
  * For video content, add:
        
        "videoContent": {
           "youtubeUrl": "URL_YOUTUBE"
         }
        

Replace `URL_YOUTUBE` with the URL of the YouTube video that you want to upload as a data source.




If the request is successful, you should get an instance of the [`source`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources#Source) object as a response, similar to the following JSON. Note the SOURCE_ID and SOURCE_RESOURCE_NAME, which are required to perform other tasks, such as retrieving or deleting the data source.
    
    
    {
      "sources": [
        {
          "sourceId": {
            "id": "SOURCE_ID"
          },
          "title": "DISPLAY_NAME",
          "metadata": {
            "xyz": "abc"
          },
          "settings": {
            "status": "SOURCE_STATUS_COMPLETE"
          },
          "name": "SOURCE_RESOURCE_NAME"
        }
      ]
    }
    

## Upload a file as a source

In addition to adding data sources in batches, you can upload single files that can be used as data sources in your notebook. To upload a single file, call the `notebooks.sources.uploadFile` method.

### REST
    
    
    curl -X POST --data-binary "@PATH/TO/FILE" \
      -H "Authorization:Bearer $(gcloud auth print-access-token)" \
      -H "X-Goog-Upload-File-Name: FILE_DISPLAY_NAME" \
      -H "X-Goog-Upload-Protocol: raw" \
      -H "Content-Type: CONTENT_TYPE" \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/upload/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/notebooks/NOTEBOOK_ID/sources:uploadFile" \
    

Replace the following:

  * `PATH/TO/FILE`: the path to the file that you want to upload.
  * `FILE_DISPLAY_NAME`: a string that denotes the display name of the file in the notebook.
  * `CONTENT_TYPE`: the type of content that you want to upload. For a list of supported content types, see Supported content types.
  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `LOCATION`: the geographic location of your data store, such as `global`. For more information, see [Locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations). 
  * `NOTEBOOK_ID`: the unique identifier of the notebook.



If the request is successful, you should get a JSON response similar to the following.
    
    
    {
      "sourceId": {
        "id": "SOURCE_ID"
      }
    }
    

### Supported content types

The file that you upload as a source must be supported.

The following document content types are supported:

File extension | Content type  
---|---  
.pdf | `application/pdf`  
.txt | `text/plain`  
.md | `text/markdown`  
.docx | `application/vnd.openxmlformats-officedocument.wordprocessingml.document`  
.pptx | `application/vnd.openxmlformats-officedocument.presentationml.presentation`  
.xlsx | `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`  
  
The following audio content types are supported:

File extension | Content type  
---|---  
.3g2 | `audio/3gpp2`  
.3gp | `audio/3gpp`  
.aac | `audio/aac`  
.aif | `audio/aiff`  
.aifc | `audio/aiff`  
.aiff | `audio/aiff`  
.amr | `audio/amr`  
.au | `audio/basic`  
.avi | `video/x-msvideo`  
.cda | `application/x-cdf`  
.m4a | `audio/m4a`  
.mid | `audio/midi`  
.midi | `audio/midi`  
.mp3 | `audio/mpeg`  
.mp4 | `video/mp4`  
.mpeg | `audio/mpeg`  
.ogg | `audio/ogg`  
.opus | `audio/ogg`  
.ra | `audio/vnd.rn-realaudio`  
.ram | `audio/vnd.rn-realaudio`  
.snd | `audio/basic`  
.wav | `audio/wav`  
.weba | `audio/webm`  
.wma | `audio/x-ms-wma`  
  
The following image content types are supported:

File extension | Content type  
---|---  
.png | `image/png`  
.jpg | `image/jpg`  
.jpeg | `image/jpeg`  
  
## Retrieve a source

To retrieve a specific source that's added to a notebook, use the [`notebooks.sources.get`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/get) method.

### REST
    
    
    curl -X GET \
      -H "Authorization:Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/notebooks/NOTEBOOK_ID/sources/SOURCE_ID"
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `LOCATION`: the geographic location of your data store, such as `global`. For more information, see [Locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations). 
  * `NOTEBOOK_ID`: the unique identifier that you received when you created the notebook. For more information, see [Create a notebook](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks#create-notebook).
  * `SOURCE_ID`: the source's identifier that you received when you added the source to your notebook.



If the request is successful, you should get a JSON response similar to the following.
    
    
    {
      "sources": [
        {
          "sourceId": {
            "id": "SOURCE_ID"
          },
          "title": "DISPLAY_NAME",
          "metadata": {
            "wordCount": 148,
            "tokenCount": 160
          },
          "settings": {
            "status": "SOURCE_STATUS_COMPLETE"
          },
         "name": "SOURCE_RESOURCE_NAME"
    
        }
      ]
    }
    

## Delete data sources from a notebook

To delete data sources in bulk from a notebook, use the [`notebooks.sources.batchDelete`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.sources/batchDelete) method.

### REST
    
    
      curl -X POST \
        -H "Authorization:Bearer $(gcloud auth print-access-token)" \
        -H "Content-Type: application/json" \
        "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/notebooks/NOTEBOOK_ID/sources:batchDelete" \
        -d '{
          "names": [
            "SOURCE_RESOURCE_NAME_1",
            "SOURCE_RESOURCE_NAME_2"
          ]
        }'
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `LOCATION`: the geographic location of your data store, such as `global`. For more information, see [Locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations). 
  * `NOTEBOOK_ID`: The unique identifier of the notebook.
  * `SOURCE_RESOURCE_NAME`: the complete resource name of the data source to be deleted. This field has the pattern: `projects/PROJECT_NUMBER/locations/LOCATION/notebooks/NOTEBOOK_ID/source/SOURCE_ID`.



If the request is successful, you should receive an empty JSON object.

## What's next

  * [Create an audio overview of your notebook](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-audio-overview) programmatically.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
