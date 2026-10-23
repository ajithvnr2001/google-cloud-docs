---
url: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-audio-overview/
title: Manage audio overview of your notebook (API) \u00a0|\u00a0 Gemini Notebook Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:42.036754+00:00
---

# Manage audio overview of your notebook (API)  |  Gemini Notebook Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-audio-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Notebook Enterprise ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs)



Send feedback 

#  Manage audio overview of your notebook (API) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After you create your notebook and add data sources to it, you can programmatically generate an audio overview of the notebook. At a time, a given notebook can have only one audio overview. This page describes how to create and delete audio overviews.

## Difference between an audio overview and a podcast

An audio overview is different from a podcast in the following ways:

  * An audio overview must be associated with a notebook with data sources added to it. On the other hand, a podcast can be generated without a Gemini Notebook Enterprise notebook, a Gemini Enterprise license, or a data store. To create a podcast, all you need is an enabled Google Cloud project and the Podcast API User role.
  * To create an audio overview, call the `notebooks.audioOverview` method. To create a podcast, call the `podcasts` method—a standalone API.



## Create an audio overview

To generate an audio overview for the content in your notebook, call the [`notebooks.audioOverviews.create`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.audioOverviews/create) method. Because you can have only one audio overview per notebook, this method is successful only if the notebook has no existing audio overview.

### REST
    
    
    curl -X POST \
      -H "Authorization:Bearer $(gcloud auth print-access-token)" \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/notebooks/NOTEBOOK_ID/audioOverviews" \
      -d '{
      "sourceIds": [
        {
          "id": "SOURCE_ID"
        }
      ],
      "episodeFocus": "EPISODE_FOCUS",
      "languageCode": "LANGUAGE_CODE"
      }
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `LOCATION`: the geographic location of your data store, such as `global`. For more information, see [Locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations). 
  * `NOTEBOOK_ID`: the unique identifier of the notebook.
  * `SOURCE_ID`: the ID of the source based on which you want to generate the audio overview. The `sourceIdsfield` is optional array; if you don't specify any source IDs, all sources in the notebook are used. For information about source ID, see [Add and manage data sources in a notebook (API)](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources).
  * `EPISODE_FOCUS`: a string that describes which topics or content must be highlighted in the audio overview.
  * `LANGUAGE_CODE`: the language code that the audio overview was requested in.



If the request is successful, you should get a JSON response similar to the following. This response shows that the audio overview generation is in progress.
    
    
      {
        "audioOverview": {
          "status": "AUDIO_OVERVIEW_STATUS_IN_PROGRESS",
          "audioOverviewId": "AUDIO_OVERVIEW_ID",
          "generationOptions": {},
          "name": "AUDIO_OVERVIEW_NAME"
        }
      }
    

It takes a few minutes to generate an audio overview.

## Verify a generated audio overview

To verify the generated audio overview, do the following:

  1. Open your notebook. For more information, see [Access the created notebook](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks#access-notebook).
  2. In your notebook's **Studio** , click **Load** to load the conversation. It takes a few moments to load the overview.

In the studio, you can manage your audio overview with tasks such as changing the playback speed and downloading or deleting the audio overview file.




## Delete an audio overview

To delete an existing audio overview, call the [`notebooks.audioOverviews.delete`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks.audioOverviews/delete) method.

### REST
    
    
    curl -X DELETE \
      -H "Authorization:Bearer $(gcloud auth print-access-token)" \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/notebooks/NOTEBOOK_ID/audioOverviews/default" \
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `LOCATION`: the geographic location of your data store, such as `global`. For more information, see [Locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations). 
  * `NOTEBOOK_ID`: the unique identifier of the notebook.



If the request is successful, you should get an empty JSON.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
