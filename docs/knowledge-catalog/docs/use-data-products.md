---
url: https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products/
title: Use data products \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:09.467877+00:00
---

# Use data products  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Use data products Stay organized with collections  Save and categorize content based on your preferences. 

This document is intended for Knowledge Catalog (formerly Dataplex Universal Catalog) data product consumers who want to discover and use data products for their use cases.

For more information about the architecture and key concepts of data products, see [About data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview).

## Before you begin

  1. Enable the Dataplex, BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com)




### Required roles

To get the permissions that you need to search for, access, and use data products, ask your administrator to grant you the following IAM roles on the data product or the project: 

  * Search for data products: [Dataplex Catalog Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) 
  * Search for data assets and request access: [Dataplex Data Products Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsConsumer) (`roles/dataplex.dataProductsConsumer`) 
  * Read-only access to view data product definitions and metadata: [Dataplex Data Products Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsViewer) (`roles/dataplex.dataProductsViewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

As a data product consumer, to view the metadata of an asset, you must have the `viewer` permission to access the corresponding asset in the source system. For example, to search for metadata for a dataset or a table in a data product, you need the BigQuery Metadata Viewer role (`roles/bigquery.metadataViewer`). For more information, see [Required roles for accessing search results](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets#required_roles_for_accessing_search_results).

## Search for data products

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Search** page.

[Go to Search](https://console.cloud.google.com/dataplex/dp-search)

  2. Search using keywords or natural language. For more information, see [Search for resources](https://docs.cloud.google.com/knowledge-catalog/docs/search-assets#search-data-assets).

  3. In the search results, click the data product for which you want to view details. You can review the description, assets, contract, aspects, contact details, and other documentation associated with the data product.




###  REST 

To search for a data product, use the [`searchEntries`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations/searchEntries) method.

For example, send the following `POST` request:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d \
      '{
      "query": "ADDITIONAL_KEYWORDS (type=(DATA_PRODUCT))",
      "pageSize": 10
      }' \
    "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/global:searchEntries"
    

Replace the following:

  * ADDITIONAL_KEYWORDS (optional): any additional keywords or search criteria to narrow down the results (for example, `displayName:'My Data Product'` or `description:'sales'`)
  * PROJECT_ID: the ID of your Google Cloud project in which the data product is created



## Request access to data products

As a data product consumer, if you don't have IAM permissions to access a data product, you can request access using the integrated access approval workflows.

### Submit an access request

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Data products** page.

[Go to Data products](https://console.cloud.google.com/dataplex/govern/data-products)

  2. Click the data product that you want to access.

  3. Click **Request access**.

  4. In the **Request details** pane, specify the following parameters:

     * **Access groups** : Select the functional access group you want to join.
     * **Self** or **Service account** : Select the principal type:

       * If you're requesting access for yourself, select **Self**.

       * If you're requesting access for programmatic identity, select **Service account**. This option is only available if the data product supports service accounts.

     * **Justification** : Enter a business justification for your request.

  5. Click **Submit**.




A new change request is generated for the data product owner to review. You will receive an email notification detailing the final status as soon as the request is approved or rejected.

###  REST 

Data product consumers who have the `dataplex.dataProducts.get` permission can request access by creating a `ChangeRequest` resource. Send a `POST` request to the data product resource endpoint using the custom method `:requestAccess`:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{
      "parent": "projects/PROJECT_ID/locations/LOCATION/dataProducts/DATA_PRODUCT_ID",
      "change_request": {
        "justification": "JUSTIFICATION_TEXT",
        "data_product_access_request": {
          "parent": "projects/PROJECT_ID/locations/LOCATION/dataProducts/DATA_PRODUCT_ID",
          "access_group_id": "DATA_PRODUCT_ACCESS_GROUP_ID"
        }
      }
    }' \
    "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/dataProducts/DATA_PRODUCT_ID:requestAccess"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project

  * LOCATION: the region where the data product exists (for example, `us-central1`)

  * DATA_PRODUCT_ID: the unique identifier of the target data product

  * JUSTIFICATION_TEXT: the business reason explaining why access is required

  * DATA_PRODUCT_ACCESS_GROUP_ID: the ID of the specific access group you are requesting to join




### View the status of access requests

As a data product consumer, you can monitor the progress and lifecycle of your submitted access requests. Knowledge Catalog tracks and displays these requests using distinct status states depending on whether you are viewing a unified workflow list or a specific product's access summary.

#### View a unified list of your access requests

To view a comprehensive list of all your submitted access requests across all data products, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance workflows** page.

[Go to Governance workflows](https://console.cloud.google.com/dataplex/governance-workflows)

  2. Click the **My requests** tab.

  3. Review the unified list displaying your past and pending requests, along with their current workflow statuses:

     * **New** : The access request has been created and is pending review by the approver.

     * **Approved** : The request has been approved, but backend systems are still provisioning access.

     * **Rejected** : The request was denied. Review the approver's comments to see the rationale for the rejection.




###  REST 

Send a `GET` request using the custom collection method `:listMine`:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests:listMine"
    

#### View the access summary for a specific data product

In addition to the global workflow list, you can check your access posture for an individual data product. This lets you verify if you already possess inherited access to an asset group without needing to submit a new request.

To view the access summary for a data product, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Data products** page.

[Go to Data products](https://console.cloud.google.com/dataplex/govern/data-products)

  2. Click the specific data product you want to inspect.

  3. Click the **Access summary** tab. Review your status across all access groups for that data product.

The **Access summary** tab uses the following status states:

Status | Description  
---|---  
**No Access** | You don't have access to the access group and haven't yet requested access.  
**Under review** | You have submitted an access request, and the request is pending review by an approver.  
**Approved** | Your access request has been approved, but membership propagation to the underlying Google Group is still processing.  
**Access granted** | Access is fully active. You are a member of the access group and can interact with the data product's assets.  
**Rejected** | Your access request for this access group was rejected.  



###  REST 

Send a `GET` request using the unique ID returned when the request was originally created:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project

  * LOCATION: the region where the data product exists (for example, `us-central1`)

  * CHANGE_REQUEST_ID: the unique ID of your submitted change request




### Delete an access request

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance workflows** page.

[Go to Governance workflows](https://console.cloud.google.com/dataplex/governance-workflows)

  2. Click the **My requests** tab.

  3. Locate the row containing your target data product request. If necessary, apply a filter to isolate the entry.

  4. Click more_vert **Actions** and then click **Delete**.




## Consume data products

To use a data product, ensure that you are granted the necessary permissions. See Request access to data products.

After the data product owner grants you permission, you can access the data product and its assets. For example, if you're granted permissions to access a BigQuery table, you can query it directly in BigQuery to generate insights.

### Access assets using user credentials

If your access request was approved for your user credentials, follow these steps to access the assets:

  1. Search for the data product.
  2. In the search results, click the data product that you want to use.
  3. Click the **Assets** tab.
  4. Click the asset for which you want to view details. This opens the entry details page.

You can access details such as schema, insights, and lineage. If the asset is a BigQuery table or view, you can click **Open in BigQuery** to navigate to the BigQuery studio and query the results.




### Access assets using a service account

If your access request was approved for a service account, you are granted the Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) IAM role on the data producer service account. This lets you create an impersonation chain to access the underlying assets.

To access assets using a service account, follow these steps:

  1. Identify the configured service accounts for the data product by navigating to the **Data Assets** tab of the data product details page.

  2. To impersonate the data producer service account, create an impersonation chain for your service account using the following Google Cloud CLI command:
         
         gcloud config set auth/impersonate_service_account CONSUMER_SERVICE_ACCOUNT,PRODUCER_SERVICE_ACCOUNT
         

Replace the following:

     * CONSUMER_SERVICE_ACCOUNT: the full qualified email address of the service account belonging to the data product consumer

     * PRODUCER_SERVICE_ACCOUNT: the fully qualified email address of the service account mapped to the data product access group

For more information, see [Use service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation).

**Note:** To query BigQuery objects such as tables or routines that require job creation, you must grant the BigQuery Job User (`roles/bigquery.jobUser`) IAM role to both the producer and consumer service accounts within the project where the query is executed.



## Access data products using remote MCP server

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For client applications and development tools that interact with your data products outside of the Google Cloud ecosystem, you can use a remote Model Context Protocol (MCP) server. This architectural pattern allows external developer clients to safely query and discover cataloged data assets while maintaining unified governance boundaries.

To learn how to deploy and connect to an external server, see [Use the Knowledge Catalog remote MCP server](https://docs.cloud.google.com/knowledge-catalog/docs/use-remote-mcp).

## What's next

  * Learn more [about data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview).
  * Learn how to [create a data product](https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products).
  * Learn more about [managing data products](https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-products).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
