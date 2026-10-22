---
url: https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-use/
title: Use data domains \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:27.615972+00:00
---

# Use data domains  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-use/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Use data domains Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

As a data domain user, you can use data domains to narrow search results to specific business contexts, search for BigQuery datasets, tables, and data products, and discover metadata within specific domain boundaries.

## Before you begin

Before you perform a search by domain, ensure that you have the required roles and APIs enabled.

### Enable APIs

Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

### Required roles

To get the permissions that you need to search and discover metadata using data domains, ask your administrator to grant you the following IAM roles on the project or data domain: 

  * View metadata of domain entries for discovery: [Dataplex Data Domain Entry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEntryReader) (`roles/dataplex.dataDomainEntryReader`) 
  * View domain configurations and bindings: [Dataplex Data Domain Configuration Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainViewer) (`roles/dataplex.dataDomainViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Browse the domain hierarchy

For more information on how to browse the domain hierarchy, see [View data domains and subdomains in a location](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-manage#view-domains).

## Find resources within a data domain

To search for resources with a domain, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Knowledge Catalog** > **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Click **Try natural search** to activate the natural search feature.

  3. Click **Filters**.

  4. In the **Scope** field, select **Domain** from the list.

  5. In the **Select domain** field, select the domain you want to narrow the results to. Add any additional filters if necessary.




Alternatively, you can use the **Search within domain** menu option to find resources in the domain:

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. Select **Search within domain** from the more_vert menu. This action automatically opens a search window with the **domain** filter applied.

  3. Use the search field to find resources in the domain.




###  REST 

To search entries scoped to a data domain, use the `projects.locations.searchEntries` method and provide the domain path in the `contexts` parameter.

**Note:** The location in the path for `searchEntries` can be `global` (for full fanout) or a specific region depending on your search backend configuration.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region for the search inquiry (or `global`).
  * `QUERY`: the search query string.
  * `DOMAIN_ID`: the unique identifier of the data domain defining the search scope context.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID:searchEntries

Request JSON body: 
    
    
    {
      "query": "QUERY",
      "contexts": [ "projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID" ],
      "semantic_search": true,
      "page_size": 100
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID:searchEntries"

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
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID:searchEntries" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Retrieve context for data domains

You can use the [`lookupContext`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/lookupContext) method to ground AI agents in the business context captured by your data domains. The `lookupContext` method supports data domains in the following ways:

  * **Context for a data domain.** You can pass the entry that represents a data domain in the `resources` list. The response contains the metadata of the data domain, such as its description and the parent data domains in the domain hierarchy.
  * **Data domain membership of data assets.** When you retrieve context for a data asset that is included in one or more data domains, the response contains a `dataDomains` field that lists the data domains the asset belongs to, starting with the most specific domain and ascending to the top-level domain.



To retrieve context for a data domain, send the following request:
    
    
    curl --request POST \
      'https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION:lookupContext' \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H 'Content-Type: application/json' \
      -d '{
        "resources": [
          "projects/PROJECT_ID/locations/LOCATION/entryGroups/@dataplex/entries/projects/PROJECT_NUMBER/locations/LOCATION/dataDomains/DATA_DOMAIN_ID"
        ],
        "options": {
          "format": "yaml"
        }
      }'
    

Replace the following:

  * PROJECT_ID: the ID of the project that contains the data domain.
  * PROJECT_NUMBER: the number of the project that contains the data domain.
  * LOCATION: the location of the data domain.
  * DATA_DOMAIN_ID: the ID of the data domain.



For more information about the `lookupContext` method, see [Retrieve context for data assets](https://docs.cloud.google.com/knowledge-catalog/docs/retrieve-data-context).

## Limitations

When you search for resources outside the domain context, for example when using a global search, the domain's discoverability permissions don't apply. You only see resources that you have access to in the underlying system, such as BigQuery.

Suppose a BigQuery dataset is included in a data domain. You have the `Dataplex Data Domain Entry Reader` role for the domain, but you don't have direct permission to view the dataset in BigQuery:

  * **Searching within the domain:** You see the dataset in your search results because the domain permissions apply.
  * **Searching outside the domain:** You don't see the dataset in your search results. In a general search, domain permissions don't apply, and you don't have direct access in BigQuery.



## What's next

  * Learn more about [data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-overview).
  * Learn how to [create data domains](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-create).
  * Learn how to [manage data domain resources](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
