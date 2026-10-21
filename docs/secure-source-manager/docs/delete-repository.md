---
url: https://docs.cloud.google.com/secure-source-manager/docs/delete-repository/
title: Delete a repository \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:42.206139+00:00
---

# Delete a repository  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/delete-repository/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Delete a repository Stay organized with collections  Save and categorize content based on your preferences. 

## Required roles

To get the permissions that you need to delete a repository, ask your administrator to grant you the following IAM roles: 

  * [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance
  * [Secure Source Manager Repo Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`) on the repository



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Delete a repository

You can delete a repository using the gcloud, web interface, or API.

###  Web interface 

  1. To access the Secure Source Manager instance through its web interface, copy the following URL into your browser address bar.
         
         INSTANCE_ID-PROJECT_NUMBER.LOCATION.sourcemanager.dev

Replace the following: 

     * INSTANCE_ID with the instance name.
     * PROJECT_NUMBER with the instance's Google Cloud project number. For information on identifying projects, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * LOCATION with the instance's region.
  2. In the list of repositories, select the repository that you want to delete.
  3. Click **Settings**.
  4. In **Repository Settings** , click **Delete This Repository**.



###  gcloud 

To delete a repository, run the following command:
    
    
    gcloud source-manager repos delete REPOSITORY_ID --region=REGION --project=PROJECT_ID
    

Replace the following:

  * `REPOSITORY_ID`: The ID of the repository you want to delete.
  * `REGION`: The region where the Secure Source Manager instance is located (for example, `us-central1`).
  * `PROJECT_ID`: The project ID where the Secure Source Manager instance is located.



###  API 

To delete your repository and all associated data, use the following HTTP method and URL.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the [project ID](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the Google Cloud project where Secure Source Manager is running.
  * LOCATION: the region where your instance is located. For information on supported locations, see [Locations](https://cloud.google.com/secure-source-manager/docs/locations).
  * REPOSITORY_ID: the repository ID.



HTTP method and URL: 
    
    
    DELETE https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://securesourcemanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    "name":"operations/cc3ea26c-9b57-11ed-be0a-2e3b5910efef","metadata":{"@type":"type.googleapis.com/google.cloud.securesourcemanager.v1.OperationMetadata","createTime":"2023-01-23T19:54:49.904779921Z","endTime":"2023-01-23T19:54:50.947030402Z","target":"projects/my-project/locations/us-central1/repositories/my-repo","verb":"delete","apiVersion":"v1"},"done":true,"response":{"@type":"type.googleapis.com/google.protobuf.Empty"}
    ```
    

## What's next

  * [Disable the Secure Source Manager API](https://docs.cloud.google.com/secure-source-manager/docs/enable-disable#disable).
  * [Delete a Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/delete-instance).
  * [List and view instances](https://docs.cloud.google.com/secure-source-manager/docs/list-view-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
