---
url: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks/
title: Create and manage notebooks (API) \u00a0|\u00a0 Gemini Notebook Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:55.751174+00:00
---

# Create and manage notebooks (API)  |  Gemini Notebook Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Notebook Enterprise ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs)



Send feedback 

#  Create and manage notebooks (API) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Gemini Notebook Enterprise is a powerful tool for generating insights and summaries from your documents. This page describes the APIs that let you perform the following notebook management tasks programmatically:

  * Create a notebook
  * Retrieve a notebook
  * List recently viewed notebooks
  * Delete a notebook
  * Share a notebook



## Before you begin

Before you start working with your notebooks, do the following:

  * [Set up Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm)
  * [Get licenses for Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-licensing)



## Create a notebook

To create a new notebook, use the [`notebooks.create`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks/create) method.

### REST
    
    
    curl -X POST \
      -H "Authorization:Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/notebooks" \
      -d '{
      "title": "NOTEBOOK_TITLE",
      }'
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `LOCATION`: the geographic location of your data store, such as `global`. For more information, see [Locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations). 
  * `NOTEBOOK_TITLE`: a UTF-8 encoded string used as a title for the notebook that you want to create.



If the request is successful, you should receive a JSON similar to the following.
    
    
    {
    "title": "NOTEBOOK_TITLE",
    "notebookId": "NOTEBOOK_ID",
    "emoji": "",
    "metadata": {
      "userRole": "PROJECT_ROLE_OWNER",
      "isShared": false,
      "isShareable": true
    },
    "name": "NOTEBOOK_NAME"
    }
    

Note the following:

  * `NOTEBOOK_ID`: a unique ID to identify the created notebook. You need the notebook ID for other notebook management tasks, such as sharing or retrieving.
  * `NOTEBOOK_NAME`: the complete resource name of the notebook. This field has the following pattern: `projects/PROJECT_NUMBER/locations/LOCATION/notebooks/NOTEBOOK_ID `



### Access the created notebook and get its ID in a browser

To access the created notebook and get its ID using a browser, do the following.

  1. Go to the Gemini Notebook Enterprise homepage that's available at one of the following URLs:

     1. If you're using a Google identity, go to:
            
            https://notebook.cloud.google.com/LOCATION/?project=PROJECT_NUMBER
            

     2. If you're using a third-party identity, go to:
            
            https://notebook.cloud.google/LOCATION/?project=PROJECT_NUMBER
            

  2. Select the created notebook. The URL of the selected notebook has the following pattern:

     1. If you're using a Google identity:
            
            https://notebook.cloud.google.com/LOCATION/notebook/NOTEBOOK_ID?project=PROJECT_NUMBER
            

     2. If you're using a third-party identity:
            
            https://notebook.cloud.google/LOCATION/notebook/NOTEBOOK_ID?project=PROJECT_NUMBER
            

  3. Note the URL and the notebook ID, which are useful for other notebook management tasks, such as sharing.




## Retrieve a notebook

To retrieve a specific notebook using its notebook ID, use the [`notebooks.get`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks/get) method.

### REST
    
    
    curl -X GET \
      -H "Authorization:Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/notebooks/NOTEBOOK_ID"
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `LOCATION`: the geographic location of your data store, such as `global`. For more information, see [Locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations). 
  * `NOTEBOOK_ID`: the notebook's unique identifier that you received when you created the notebook.



If the request is successful, you should get a JSON response similar to the following for an empty notebook. If you call this method after you [add sources](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources#add-source-notebook) to your notebook, you receive details about all the sources added to the retrieved notebook. If you have [configured CMEK details](https://docs.cloud.google.com/gemini/enterprise/docs//notebooklm-enterprise/docs/cmek), you also receive CMEK-related information for the notebook.
    
    
    {
    "title": "NOTEBOOK_TITLE",
    "notebookId": "NOTEBOOK_ID",
    "emoji": "",
    "metadata": {
      "userRole": "PROJECT_ROLE_OWNER",
      "isShared": false,
      "isShareable": true,
      "lastViewed": "LAST_VIEWED_TIME",
      "createTime": "LAST_CREATED_TIME"
    },
    "name": "NOTEBOOK_NAME"
    }
    

## List recently viewed notebooks

To get a list of all notebooks in a project that were recently viewed, use the [`notebooks.listRecentlyViewed`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks/listRecentlyViewed) method. By default, the response lists the last 500 notebooks. You can choose to paginate the responses with the `pageSize` query parameter.

### REST
    
    
    curl -X GET \
      -H "Authorization:Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/notebooks:listRecentlyViewed"
    

Replace the following:

  * `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following values: 
    * `us` for the US multi-region
    * `eu` for the EU multi-region
    * `global` for the Global location
For more information, see [Specify a multi-region for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 
  * `PROJECT_NUMBER`: the number of your Google Cloud project.
  * `LOCATION`: the geographic location of your data store, such as `global`. For more information, see [Locations](https://docs.cloud.google.com/gemini/enterprise/docs/locations). 



If the request is successful, you should get a JSON response similar to the following. The response contains up to last 500 notebooks that a user accessed recently.
    
    
    {
      "notebooks": [
        {
          "title": "NOTEBOOK_TITLE_1",
          "notebookId": "NOTEBOOK_ID_1",
          "emoji": "",
          "metadata": {
            "userRole": "PROJECT_ROLE_OWNER",
            "isShared": false,
            "isShareable": true,
            "lastViewed": "LAST_VIEWED_TIME",
            "createTime": "LAST_CREATED_TIME"
          },
          "name": "NOTEBOOK_NAME_1"
        },
        {
          "title": "NOTEBOOK_TITLE_2",
          "notebookId": "NOTEBOOK_ID_2",
          "emoji": "",
          "metadata": {
            "userRole": "PROJECT_ROLE_OWNER",
            "isShared": false,
            "isShareable": true,
            "lastViewed": "LAST_VIEWED_TIME",
            "createTime": "LAST_CREATED_TIME"
          },
          "name": "NOTEBOOK_NAME_2"
        }
      ]
    }
    

## Delete a notebook

To delete a notebook, use the [`notebooks.batchDelete`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks/batchDelete) method.

### REST
    
    
    curl -X POST \
      -H "Authorization:Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/notebooks:batchDelete" \
      -d '{
        "names": [
          "NOTEBOOK_NAME"
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
  * `NOTEBOOK_NAME`: the complete resource name of the notebook to be deleted. This field has the pattern: `projects/PROJECT_NUMBER/locations/LOCATION/notebooks/NOTEBOOK_ID`.

If the request is successful, you receive an empty JSON object. If the notebook doesn't exist, you also receive an empty JSON object, so make sure to specify the notebook name correctly.




## Share a notebook

To share a new notebook, use the [`notebooks.share`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.notebooks/share) method.

The user with whom you want to share the notebook must be granted the [Cloud NotebookLM User](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#user_roles) role.

### REST

  1. In your Google Cloud project, assign the `Cloud NotebookLM User` Identity and Access Management (IAM) role to the users with whom you want to share the notebook.

  2. Call the following method.
         
         curl -X POST \
           -H "Authorization:Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/notebooks/NOTEBOOK_ID:share" \
           -d '{
             "accountAndRoles": [
              {
                 "email":"USER_EMAIL_1",
                 "role":"USER_ROLE_1",
              },
              {
                 "email":"USER_EMAIL_2",
                 "role":"USER_ROLE_2",
              },
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
     * `NOTEBOOK_ID`: a unique ID to identify the notebook that you want to share. You need the notebook ID for other notebook management tasks, such as sharing or retrieving.
     * `USER_EMAIL`: the email address of the user with whom you want to share the notebook.
     * `USER_ROLE`: a role that you want to assign to the user. It can be one of the following:

       * `PROJECT_ROLE_OWNER`: The user owns the project.
       * `PROJECT_ROLE_WRITER`: The user has write permissions on the project.
       * `PROJECT_ROLE_READER`: The user has read permissions on the project.
       * `PROJECT_ROLE_NOT_SHARED`:The user has no access to the project.

If the request is successful, you receive an empty JSON object.




### Verify users using a browser

To verify whether you've shared the notebook with the correct users and assigned them correct roles, do the following:

  1. Open the notebook in your browser. A notebook has the following URL pattern:

     1. If you're using a Google identity:
            
            https://notebook.cloud.google.com/LOCATION/notebook/NOTEBOOK_ID?project=PROJECT_NUMBER
            

     2. If you're using a third-party identity:
            
            https://notebook.cloud.google/LOCATION/notebook/NOTEBOOK_ID?project=PROJECT_NUMBER
            

  2. Click **Share**.

  3. Verify the users listed as **People with access** and their assigned roles.




## What's next

  * [Add data sources of different types to your notebooks](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks-sources) programmatically.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
