---
url: https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-create/
title: Create data domains \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:51.756175+00:00
---

# Create data domains  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-create/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Create data domains Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to create data domains and subdomains using the Google Cloud console and the REST API, and how to grant Identity and Access Management the roles and permissions to users who interact with the domains and their resources.

## Before you begin

Before creating data domains and assigning domain owners, ensure that you have the required roles and APIs enabled.

  * The maximum nesting depth for domains and subdomains is five levels.
  * You can create up to 50 direct subdomains under a single data domain.
  * Within a project, you can have up to 1,000 domains per region.



### Enable APIs

Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

### Required roles

To get the permissions that you need to create data domains and assign domain owners, ask your administrator to grant you the following IAM roles on the project: 

  * Allows full management of the data domain, its bindings and IAM policies: [Dataplex Data Domain Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainAdmin) (`roles/dataplex.dataDomainAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a data domain

Create a data domain to serve as a logical grouping for data assets and products within a project and location.

###  Console 

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. Click **Create Data Domain** and provide the following information:

     * In the **Display name** field, provide a user-friendly name for the domain. For example, `Finance`.
     * In the **Data Domain ID** field, provide a unique ID for the domain. You can't change this value after the system creates the domain.
     * In the **Location** field, select the region in which you want to create the data domain.
     * In the **Project ID** field, select the project in which you want to create the data domain.
     * Optional: In the **Description** field, provide a short description of the domain.
     * In the **Owners** field, add an owner or owners of the domain. You can enter several email addresses simultaneously.
  3. Optional: In the **Labels** field, enter labels to group related objects together or with other Google Cloud resources.

  4. Click **Create**. It might take a few minutes before you can access or search for the data domain.




###  REST 

To create a data domain, use the `projects.locations.dataDomains.create` method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region in which you want to create the data domain. For example, `us-central1`.
  * `DATA_DOMAIN_ID`: a unique identifier for your data domain.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains?data_domain_id=DATA_DOMAIN_ID

Request JSON body: 
    
    
    {
      "display_name": "Finance Domain",
      "description": "Domain for finance datasets and reports.",
      "contacts": {
        "identities": [
          {
            "contact_name": "Alice Wonderland",
            "contact_role": "owner",
            "contact_id": "alice@example.com"
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains?data_domain_id=DATA_DOMAIN_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains?data_domain_id=DATA_DOMAIN_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Create a data subdomain

Create a subdomain to extend the data domain hierarchy.

###  Console 

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. Select the domain you want to create a subdomain for.

  3. Click **Create Data Subdomain** and provide the following information:

     * In the **Display name** field, provide a user-friendly name for the domain. For example, `Finance`.
     * In the **Data Domain ID** field, provide a unique ID for the domain. You can't change this value after the system creates the domain.
     * Optional: In the **Description** field, provide a short description of the domain.
     * In the **Owners** field, add the email address of the owner of the domain. You can enter several email addresses simultaneously.
  4. Optional: In the **Labels** field, enter labels to group related objects together or with other Google Cloud resources.

  5. Click **Create**. It might take a few minutes before you can access or search for the data subdomain.




###  REST 

To create a data subdomain, use the `projects.locations.dataDomains.create` method and specify the `parent_data_domain` in the request body.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region where the parent data domain exists. For example, `us-central1`.
  * `SUBDOMAIN_ID`: a unique identifier for your data subdomain.
  * `PARENT_DATA_DOMAIN_ID`: the unique ID of the parent data domain under which this subdomain is created.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains?data_domain_id=SUBDOMAIN_ID

Request JSON body: 
    
    
    {
      "display_name": "Finance Subdomain",
      "description": "A subdomain within the Finance domain.",
      "contacts": {
        "identities": [
          {
            "contact_name": "Alice Wonderland",
            "contact_role": "owner",
            "contact_id": "alice@example.com"
          }
        ]
      },
      "parent_data_domain": "projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/PARENT_DATA_DOMAIN_ID"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains?data_domain_id=SUBDOMAIN_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains?data_domain_id=SUBDOMAIN_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Data domain roles and permissions

The following table lists the predefined IAM roles that you can grant to data domain owners and users.

Role name | IAM role | Description  
---|---|---  
Dataplex Data Domain Admin | `roles/dataplex.dataDomainAdmin` | Lets you create and manage data domains and subdomains along with their bindings. The Admin role also lets you manage all IAM roles and permissions for domains.  
Dataplex Data Domain Configuration Viewer | `roles/dataplex.dataDomainViewer` | Lets you view the configuration of the data domain and the resource-domain bindings.  
Dataplex Data Domain Configuration Editor | `roles/dataplex.dataDomainEditor` | Lets you edit existing domains as well as create and manage the resource-domain bindings. The Editor role also lets you manage metadata authorizations that allow the discovery of domain resources by the users.  
Dataplex Data Domain Entry Reader | `roles/dataplex.dataDomainEntryReader` | Lets you discover and view the data domain, its subdomains, and the metadata of all its included resources.  
  
When you grant the roles to domain owners or users, consider the following:

  * Identity and Access Management data domain roles propagate from parent domains to subdomains, but not directly to included resources. This means, if you grant `roles/dataplex.dataDomainEntryReader` to the user of the domain that includes a BigQuery dataset, the user won't see the role among the dataset Identity and Access Management roles. 
  * The `roles/dataplex.dataDomainEntryReader` role granted on a domain lets you perform the following actions:

    * You can discover resources, their details and metadata, but when you view the resource within the domain. For more information, see [Data domain limitations](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-overview#limitations).
    * You can use API methods like `lookupEntry` on the resource located in the domain.



## Grant access to a data domain

###  Console 

To grant access to a data domain, follow these steps:

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. Click the domain name to go to the domain details page.

  3. In the top bar, click **Permissions**.

  4. Click **Add principal**.

  5. In the **New principals** field, enter the email address of the principal.

  6. In the **Select a role** field, choose the data domain role. For example, use `Dataplex Data Domain Entry Reader` to allow the user to discover and view the data domain, its subdomains, and the metadata of the included resources. If you want to grant more roles, click **Add another role**.

  7. Click **Save**.




###  REST 

To set the IAM policy on a data domain, use the `projects.locations.dataDomains.setIamPolicy` method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region where the data domain exists. For example, `us-central1`.
  * `DOMAIN_ID`: the unique identifier of the data domain.
  * `ROLE`: the role you want to grant to the domain user.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "ROLE",
            "members": [
              "user:example-user@google.com",
              "group:finance-consumers@google.com"
            ]
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID:setIamPolicy"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID:setIamPolicy" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Revoke access to a data domain

To remove a role or permission from a principal, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. Click the domain name to go to the domain details page.

  3. In the top bar, click **Permissions**.

  4. In the **Permissions** pane, locate the principal you want to revoke the role for.

  5. Click the **Delete** icon next to the role you want to remove.

  6. Click **Save**.




###  REST 

To revoke access to a data domain using the REST API, retrieve the existing policy using the `projects.locations.dataDomains.getIamPolicy` method, remove the role or principal from the `bindings` list, and set the updated policy using the `projects.locations.dataDomains.setIamPolicy` method:

  1. Get the current IAM policy:

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION_ID`: the region where the data domain exists. For example, `us-central1`.
     * `DOMAIN_ID`: the unique identifier of the data domain.

HTTP method and URL: 
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID:getIamPolicy

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID:getIamPolicy"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID:getIamPolicy" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

  2. Set the updated policy:

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `LOCATION_ID`: the region where the data domain exists. For example, `us-central1`.
     * `DOMAIN_ID`: the unique identifier of the data domain.
     * `ROLE`: the role you want to grant to the domain user.

HTTP method and URL: 
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID:setIamPolicy

Request JSON body: 
    
    {
      "policy": {
        "bindings": [
          {
            "role": "ROLE",
            "members": [
              "user:example-user@google.com",
              "group:finance-consumers@google.com"
            ]
          }
        ]
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID:setIamPolicy"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID:setIamPolicy" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.




**Note:** If the principal's access is inherited from a higher-level IAM policy, you can't delete or edit it at the domain level.

## What's next

  * Learn more about [data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-overview).
  * Learn more about [resource binding and inclusion](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-binding-overview).
  * Learn how to [manage data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-manage).
  * Learn how to [use data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-use).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
