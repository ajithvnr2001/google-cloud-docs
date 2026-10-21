---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-engine-versions/
title: Manage engine versions \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:32:46.834949+00:00
---

# Manage engine versions  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/manage-engine-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Manage engine versions Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to manage AML AI engine versions. An engine version is used to control the architecture or setting for training and running a model. It is a read-only resource.

For more information on engine versions, see [Engine versions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/engine-versions).

## Before you begin

  * To get the permissions that you need to manage engine versions, ask your administrator to grant you the Financial Services Admin (`financialservices.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  * [Create an instance](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/create-and-manage-instances#create-instance)



## List the engine versions

To list the engine versions, use the [`projects.locations.instances.engineVersions.list`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineVersions/list) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1engineversions.list`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "engineVersions": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/finserv-aml.live-with-data-validation.v1.1.2022-05",
          "state": "ACTIVE",
          "expectedLimitationStartTime": EXPECTED_LIMITATION_START_TIME,
          "expectedDecommissionTime": "EXPECTED_DECOMMISSION_TIME,
          "lineOfBusiness": "RETAIL"
        },
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/finserv-aml.live.v1.1.2022-05",
          "state": "ACTIVE",
          "expectedLimitationStartTime": EXPECTED_LIMITATION_START_TIME,
          "expectedDecommissionTime": "EXPECTED_DECOMMISSION_TIME,
          "lineOfBusiness": "RETAIL"
        }
      ]
    }
    

## Get an engine version

To get an engine version, use the [`projects.locations.instances.engineVersions.get`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineVersions/get) method.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions:

**Permissions**

  * `financialservices.v1engineversions.get`



Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: your Google Cloud project ID listed in the [IAM Settings](https://console.cloud.google.com/iam-admin/settings/project)
  * `LOCATION`: the location of the instance; use one of the [supported regions](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/locations)

Show locations

    * `us-central1`
    * `us-east1`
    * `europe-west2`
    * `europe-west6`
  * `INSTANCE_ID`: the user-defined identifier for the instance
  * `ENGINE_VERSION_ID`: the identifier for the engine version



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://financialservices.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID/engineVersions/ENGINE_VERSION_ID",
      "state": "ACTIVE",
      "expectedLimitationStartTime": EXPECTED_LIMITATION_START_TIME,
      "expectedDecommissionTime": "EXPECTED_DECOMMISSION_TIME,
      "lineOfBusiness": "RETAIL"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
