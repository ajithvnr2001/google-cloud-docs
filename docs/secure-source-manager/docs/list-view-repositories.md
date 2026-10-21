---
url: https://docs.cloud.google.com/secure-source-manager/docs/list-view-repositories/
title: List and view repositories \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:24.065722+00:00
---

# List and view repositories  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/list-view-repositories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  List and view repositories Stay organized with collections  Save and categorize content based on your preferences. 

This document outlines how to search for and view Secure Source Manager repositories by full or partial repository ID.

## Required roles

To get the permissions that you need to search repositories, ask your administrator to grant you the following IAM roles: 

  * [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance
  * [Secure Source Manager Repo Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoReader) (`roles/securesourcemanager.repoReader`) on repositories that you want to search for



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to search repositories. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## List repositories

###  web interface 

To access the Secure Source Manager instance through its web interface, copy the following URL into your browser address bar.
    
    
    INSTANCE_ID-PROJECT_NUMBER.LOCATION.sourcemanager.dev

Replace the following: 

  * INSTANCE_ID with the instance name.
  * PROJECT_NUMBER with the instance's Google Cloud project number. For information on identifying projects, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * LOCATION with the instance's region.



The **My repositories** tab displays all repositories you have access to view.

###  API 

To list details for all repositories in a given region for your instance, use the following HTTP method and URL.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the [project ID](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project where Secure Source Manager is running.
  * INSTANCE_ID: the instance ID.
  * LOCATION: the region where your instance is located. For information on supported locations, see [Locations](https://cloud.google.com/secure-source-manager/docs/locations).



HTTP method and URL: 
    
    
    GET https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories?instance=projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories?instance=projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories?instance=projects/PROJECT_ID/locations/LOCATION/instances/INSTANCE_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
        "repositories" : [
              {
                "createTime" : "2023-08-09T19:32:15Z",
                "instance" : "projects/012345678901/locations/us-central1/instances/my-instance",
                "name" : "projects/my-project/locations/us-central1/repositories/my-repo",
                "uris" : {
                    "api" : "https://my-instance-012345678901-api.us-central1.sourcemanager.dev/v1/projects/my-project/locations/us-central1/repositories/my-repo",
                    "gitHttps" : "https://my-instance-012345678901-git.us-central1.sourcemanager.dev/my-project/my-repo.git",
                    "html" : "https://my-instance-012345678901.us-central1.sourcemanager.dev/my-project/my-repo"
                }
              }
        ]
    }
    

## View details for a specific repository

To list details for a single repository, use the following HTTP method and URL.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the [project ID](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project where Secure Source Manager is running.
  * LOCATION: the region where your instance is located. For information on supported locations, see [Locations](https://cloud.google.com/secure-source-manager/docs/locations).
  * REPOSITORY_ID: the repository ID.



HTTP method and URL: 
    
    
    GET https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
        {
          "createTime" : "2023-08-09T19:32:15Z",
          "instance" : "projects/012345678901/locations/us-central1/instances/my-instance",
          "name" : "projects/my-project/locations/us-central1/repositories/my-repo",
          "uris" : {
              "api" : "https://my-instance-012345678901-api.us-central1.sourcemanager.dev/v1/projects/my-project/locations/us-central1/repositories/my-repo",
              "gitHttps" : "https://my-instance-012345678901-git.us-central1.sourcemanager.dev/my-project/my-repo.git",
              "html" : "https://my-instance-012345678901.us-central1.sourcemanager.dev/my-project/my-repo"
          }
        }
    

## View repositories in the web interface

You can search for repositories within the **My repositories** tab by keyword.

  1. In the Secure Source Manager web interface, enter your search keyword in the **Search repository names** search bar.

The search results include all repositories that include your keyword in their repository ID.

  2. Select the repository you want to view.

The repository page opens.




## What's next

  * [Create a repository](https://docs.cloud.google.com/secure-source-manager/docs/create-repository).
  * [Grant repository-level roles](https://docs.cloud.google.com/secure-source-manager/docs/grant-repository-roles).
  * [Delete a repository](https://docs.cloud.google.com/secure-source-manager/docs/delete-repository).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
