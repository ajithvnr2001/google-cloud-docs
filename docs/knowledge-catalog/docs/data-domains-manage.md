---
url: https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-manage/
title: Manage data domains \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:00.313929+00:00
---

# Manage data domains  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-manage/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage data domains Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you view, update, and delete data domains and subdomains using the Google Cloud console and the REST API. You can inspect included resources, modify display names and labels, or remove empty domains to keep your hierarchy aligned with your business structure.

## Before you begin

Before managing data domains, ensure that you have the required roles and APIs enabled.

### Enable APIs

Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

### Required roles

To get the permissions that you need to manage data domains, ask your administrator to grant you the following IAM roles on the project: 

  * Update data domains and resource bindings: [Dataplex Data Domain Configuration Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`) 
  * View the configuration of the data domain and bindings: [Dataplex Data Domain Configuration Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainViewer) (`roles/dataplex.dataDomainViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View data domains and subdomains

View data domains and subdomains in a specific project.

###  Console 

### View all data domains

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. The table lists the created domains. Click the chevron_right **Expand** arrow next to the data domain name to view the nested subdomains.




### View data domain and subdomain details

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. Click the name of the domain or subdomain you want to view.

  3. The **Domain Details** page displays the following tabs:

     * **Overview** : Provides an overview of the domain and the list of required and optional aspects.
     * **Resources** : Lists resources included in this domain. The list displays only folders, projects, and resources directly included in the domain.



###  REST 

### View data domains and subdomains

To view data domains, use the `projects.locations.dataDomains.list` method:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region of your project. For example, `us-central1`.



HTTP method and URL: 
    
    
    GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### View data subdomains

To view data subdomains, use the `projects.locations.dataDomains.listSubdomains` method:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region where the parent data domain exists. For example, `us-central1`.
  * `DOMAIN_ID`: the unique identifier of the parent data domain.



HTTP method and URL: 
    
    
    GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/subdomains

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/subdomains"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/subdomains" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

Use the `filter` parameter to list subdomains belonging to a specific parent domain:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region where the parent data domain exists. For example, `us-central1`.
  * `PARENT_DOMAIN_ID`: the unique identifier of the parent data domain.



HTTP method and URL: 
    
    
    GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains?filter=parent_data_domain="projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/PARENT_DOMAIN_ID"

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains?filter=parent_data_domain="projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/PARENT_DOMAIN_ID""

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains?filter=parent_data_domain="projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/PARENT_DOMAIN_ID"" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### View data domain details

To get domain or subdomain details, use the `projects.locations.dataDomains.get` method:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region where the data domain exists. For example, `us-central1`.
  * `DOMAIN_ID`: the unique identifier of the data domain or subdomain.



HTTP method and URL: 
    
    
    GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Update a data domain or subdomain

You can update the display name, description, and labels of a domain. You can't change the domain ID or location after you create the domain.

###  Console 

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. Click the domain or subdomain name to go to the details page.

  3. In the top bar, click **Edit**.

  4. Update the **Display name** or **Description**.

  5. Click **Save**.




###  REST 

To update a data domain, use the `projects.locations.dataDomains.patch` method:

**Note:** You must specify which fields to update using the `updateMask` query parameter to avoid overwriting other properties.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region where the data domain exists. For example, `us-central1`.
  * `DOMAIN_ID`: the unique identifier of the data domain or subdomain.



HTTP method and URL: 
    
    
    PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID?updateMask=description,labels

Request JSON body: 
    
    
    {
      "description": "Updated description for the domain",
      "labels": {
        "status": "active"
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID?updateMask=description,labels"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID?updateMask=description,labels" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Delete a data domain or subdomain

You can only delete an empty data domain. You must delete all subdomains and remove all resource bindings associated with the domain before attempting to delete the domain itself. If the domain is not empty, the deletion request fails with an error.

###  Console 

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. Click the domain or subdomain name to go to the details page.

  3. In the top bar, click **Delete**.

  4. Confirm the deletion by typing the data domain or subdomain name.

  5. Click **Delete**.




###  REST 

To delete a data domain, use the `projects.locations.dataDomains.delete` method:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region where the data domain exists. For example, `us-central1`.
  * `DOMAIN_ID`: the unique identifier of the data domain or subdomain.



HTTP method and URL: 
    
    
    DELETE https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## What's next

  * Learn more about [data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-overview).
  * Learn more about [resource binding and inclusion](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-binding-overview).
  * Learn how to [create data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-create).
  * Learn how to [use data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-use).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
