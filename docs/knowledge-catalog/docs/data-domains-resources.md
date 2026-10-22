---
url: https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-resources/
title: Include resources in data domains \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:20.494647+00:00
---

# Include resources in data domains  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-resources/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Include resources in data domains Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Data domains in Knowledge Catalog (formerly Dataplex Universal Catalog) let you organize projects, data products, and individual assets, such as BigQuery datasets and tables, into a logical hierarchy. After you authorize a domain and create resource bindings, users can search within that business context to discover included resources and view their metadata.

## How it works

To include a resource in a domain, you must perform the following steps:

  1. Get the domain principal ID for the domain you want to authorize. For more information, see Get the domain principal.
  2. Authorize the domain to grant the access to a specific resource or a project. 
  3. Create a binding between the resource and the domain. For more information, see Bind resources to the domain.



## About data domain authorization

Domain authorization establishes trust between the resource and the domain. A resource owner grants IAM permissions to the data domain IAM principal on the target resource or project. This action lets Knowledge Catalog authorize and execute the creation of the binding that links the resource to the domain.

Domain authorization is verified only when a binding is created. This means that if you revoke the domain principal's IAM role on a resource, that resource isn't automatically unbound or removed from the domain. Domain users with the `roles/dataplex.dataDomainEntryReader` role continue to discover the resource and view its metadata until the resource-domain binding is explicitly deleted.

### Domain authorization and domain user permissions

When working with data domains, it's important to distinguish between data domain authorization and granting data domain permissions to a user:

  * **Data domain authorization:** This refers to authorizing the data domain on a target resource. You grant the data domain IAM principal permissions on an underlying resource, such as a project or a BigQuery dataset, to create the binding between the resource and the domain.
  * **Granting data domain permissions to a user:** This refers to giving a user or service account permissions to interact with the data domain itself. You grant IAM roles to users directly on the data domain so they can view, edit, or manage the domain within Knowledge Catalog. For more information, see [Data domain roles and permissions](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-create#manage-iam).



### Role types

When you authorize a data domain on a target resource, you can select an IAM role that falls into one of the following role types: **Reader** , **Writer** , or **Admin**. 

In general understanding, the Writer and Admin role types are reserved to enable domains to perform extended range of actions over the resources they are authorised over as follows:

  * Writer role types let the domain manage metadata edit permissions on the resource.
  * Admin role types let the domain manage any permissions on the resource.



Within the scope of data domains, all three role types allow the data domain to create a binding to the target resource. When the binding is created, the users can search for the resource within the domain and view its metadata. For more information, see [Search for data resources](https://docs.cloud.google.com/knowledge-catalog/docs/data-domains-search).

When choosing the role type, take into account the long-term level access you want to grant the domain over the resource.

### Roles recommended for domain authorization

The following tables list the recommended roles you can use to authorize the domain to inspect the resources. For each resource, you can choose a role different than recommended, but such a role must contain the permissions required to perform resource bindings.

Select the resource type you want to view the roles for from the list.

All resourcesProjectBigQuery datasetBigQuery tableData productDataform repositoryDataproc Metastore databaseDataproc Metastore tableCloud Spanner databaseBigLake tableAlloyDB for PostgreSQL instanceGemini Enterprise Agent Platform dataset

Resource type | Role type | Recommended roles | Description | Required permissions  
---|---|---|---|---  
Project | Reader | `roles/browser` | Gives the domain permissions to get information about a project. |  `resourcemanager.projects.get`  
Writer | `roles/editor` | Gives the domain permissions to get information about a project and manage its metadata. |  `resourcemanager.projects.get`  
`resourcemanager.projects.update`  
Admin | `roles/owner` | Gives the domain administrative management over a project, including discovery, metadata governance and access policy administration. |  `resourcemanager.projects.get`  
`resourcemanager.projects.update`  
`resourcemanager.projects.setIamPolicy`  
BigQuery dataset | Reader | `roles/bigquery.metadataViewer` | Gives the domain permissions to get information about a BigQuery dataset. |  `bigquery.datasets.get`  
Writer | `roles/bigquery.dataEditor` | Gives the domain permissions to get information about a BigQuery dataset and manage its metadata. |  `bigquery.datasets.get`  
`bigquery.datasets.updateTag`  
Admin | `roles/bigquery.dataOwner` | Gives the domain administrative management over a BigQuery dataset, including discovery, metadata governance and access policy administration. |  `bigquery.datasets.get`  
`bigquery.datasets.updateTag`  
`bigquery.datasets.setIamPolicy`  
BigQuery table | Reader | `roles/bigquery.metadataViewer` | Gives the domain permissions to get information about a BigQuery table. |  `bigquery.tables.get`  
Writer | `roles/bigquery.dataEditor` | Gives the domain permissions to get information about a BigQuery table and manage its metadata. |  `bigquery.tables.get`  
`bigquery.tables.update`  
Admin | `roles/bigquery.dataOwner` | Gives the domain administrative management over a BigQuery table, including discovery, metadata governance and access policy administration. |  `bigquery.tables.get`  
`bigquery.tables.update`  
`bigquery.tables.setIamPolicy`  
Data product | Reader | `roles/dataplex.dataProductsViewer` | Gives the domain permissions to get information about a data product. |  `dataplex.dataProducts.get`  
Writer | `roles/dataplex.dataProductsEditor` | Gives the domain permissions to get information about a data product and manage its metadata. |  `dataplex.dataProducts.get`  
`dataplex.dataProducts.update`  
Admin | `roles/dataplex.dataProductsAdmin` | Gives the domain administrative management over a data product, including data product discovery, metadata governance and access policy administration. |  `dataplex.dataProducts.get`  
`dataplex.dataProducts.update`  
`dataplex.dataProducts.setIamPolicy`  
Dataform repository | Reader | `roles/dataform.codeViewer` | Gives the domain the read-only access to Dataform code resources. |  `dataform.repositories.get`  
Writer | `roles/dataform.codeOwner` | Gives the domain the full access to Dataform repository and code resources. |  `dataform.repositories.get  
dataform.repositories.update`  
Admin | `roles/dataform.codeOwner` | Gives the domain the full access to Dataform repository and code resources. |  `dataform.repositories.get  
dataform.repositories.setIamPolicy`  
Dataproc Metastore database | Reader | `roles/metastore.metadataUser` | Gives the domain permissions to get the list of Dataproc Metastore databases. |  `metastore.databases.get`  
Writer | `roles/metastore.metadataEditor` | Gives the domain access to read and modify the metadata of Dataproc Metastore databases and tables under those databases. |  `metastore.databases.get  
metastore.databases.update`  
Admin | `roles/metastore.metadataOwner` | Gives the domain full access to the metadata of Dataproc Metastore databases and tables under those databases. |  `metastore.databases.get  
metastore.databases.setIamPolicy`  
Dataproc Metastore table | Reader | `roles/metastore.metadataViewer` | Gives the domain access to read the metadata of Dataproc Metastore databases and tables under those databases. |  `metastore.tables.get`  
Writer | `roles/metastore.metadataEditor` | Gives the domain access to read and modify the metadata of Dataproc Metastore databases and tables under those databases. |  `metastore.tables.get`  
Admin | `roles/metastore.metadataOwner` | Gives the domain full access to the metadata of Dataproc Metastore databases and tables under those databases. |  `metastore.tables.get  
metastore.tables.setIamPolicy`  
Cloud Spanner database | Reader | `roles/spanner.databaseReader` | Gives the domain permissions to read from the Spanner database, execute SQL queries, and view the schema for the database. |  `spanner.databases.get`  
Writer | `roles/spanner.editor` | Gives the domain administrative and operational permissions across Spanner resources, including instance and database management, query execution, backup and restore management, and resource management. |  `spanner.databases.get  
spanner.databases.update`  
Admin | `roles/spanner.databaseAdmin` | Gives the domain full access to manage Spanner instances in the project and databases in these instances. |  `spanner.databases.get  
spanner.databases.setIamPolicy`  
BigLake table | Reader | `roles/biglake.metadataViewer` | Gives the domain read-only metadata access to all BigLake resources. |  `biglake.tables.get`  
Writer | `roles/biglake.editor` | Gives the domain read and write access to all BigLake resources. |  `biglake.tables.get  
biglake.tables.update`  
Admin | `roles/biglake.admin` | Gives the domain full access to all BigLake resources. |  `biglake.tables.get  
biglake.tables.setIamPolicy`  
AlloyDB for PostgreSQL instance | Reader | `roles/alloydb.viewer` | Gives the domain read-only access to AlloyDB for PostgreSQL resources. |  `alloydb.instances.get`  
Writer | `roles/alloydb.editor` | Gives the domain read and write access to AlloyDB for PostgreSQL resources. |  `alloydb.instances.get  
alloydb.instances.update`  
Gemini Enterprise Agent Platform dataset | Reader | `roles/aiplatform.viewer` | Gives the domain permissions to view all resources in Gemini Enterprise Agent Platform. |  `aiplatform.datasets.get`  
Writer | `roles/aiplatform.user` | Gives the domain permissions to use all resources in Gemini Enterprise Agent Platform. |  `aiplatform.datasets.get  
aiplatform.datasets.update`  
  
## Before you begin

Before you include resources in a data domain, ensure that you have the required roles and APIs enabled. Additionally, consider the following limits:

  * A resource can belong to only one domain.
  * A domain can contain up to 500 resources.



### Enable APIs

Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

**Note:** To authorize and bind resources to your data domain, ensure that you have enabled the API corresponding to the target resource's service in the project that hosts the resource. For example, to authorize and bind Spanner database or Vertex AI dataset, you must enable `spanner.googleapis.com` and `aiplatform.googleapis.com` APIs.

### Required roles

To get the permissions that you need to bind resources to data domains, ask your administrator to grant you the following IAM roles on the project: 

  * Manage domains and resource bindings: [Dataplex Data Domain Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataDomainEditor) (`roles/dataplex.dataDomainEditor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Get the domain IAM principal

**Tip:** You can copy the domain IAM principal ID directly from the tooltip located in the **Add resource binding** page in Google Cloud console.

To authorize a data domain to perform actions on a resource, you need the domain IAM principal ID. Keep the domain principal ID at hand, because you must provide it when you authorize the domain on the resource.

###  Console 

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. Click the domain name to go to the domain details page.

  3. In the **Overview** tab, go to **Information** and then **Identifiers**.

  4. Copy the value of **IAM principal**. The format is similar to the following:



    
    
    principal://dataplex.googleapis.com/projects/DOMAIN_PROJECT_NUMBER/name/locations/LOCATION_ID/dataDomains/DOMAIN_ID
    

###  REST 

To get the domain principal using the REST API, use the `projects.locations.dataDomains.get` method to get the data domain. The response includes the `policyMember` field, which contains the IAM principal (`iamPolicyNamePrincipal` or `iamPolicyUidPrincipal`) for the domain:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region where the data domain exists. For example, `us-central1`.
  * `DOMAIN_ID`: the unique identifier of the data domain or subdomain.



HTTP method and URL: 
    
    
    GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Authorize the domain on a resource

Before you can bind a resource, you must grant the domain's principal the required IAM roles on the target resource.

**Note:** You can't directly authorize Gemini Enterprise Agent Platform datasets, Dataproc Metastore databases and tables, Dataform repositories, AlloyDB for PostgreSQL instances, BigLake tables using Google Cloud console. Instead, authorize the resources at the project level allowing the resources to inherit the permissions.

###  Console 

  1. In the Google Cloud console, navigate to the target resource and open the permissions panel for that resource:

     * For projects, Gemini Enterprise Agent Platform datasets, Dataproc Metastore databases and tables, Dataform repositories, AlloyDB for PostgreSQL instances, BigLake tables, go to [**IAM**](https://console.cloud.google.com/iam-admin/iam) page and click **Grant access**.
     * For data products, go to [**Data Products**](https://console.cloud.google.com/dataplex/govern/data-products) page, select the data product, click **Share** > **Set permissions**.
     * For BigQuery datasets and tables, go to [**BigQuery**](https://console.cloud.google.com/bigquery) page, select a dataset or table, and click **Share > Manage permissions**.
     * For Spanner databases, go to [**Spanner**](https://console.cloud.google.com/spanner) page, select the database and click the **Permissions** tab.
  2. Click **Add Principal** or equivalent.

  3. In the **New principals** field, paste the domain's **IAM principal**. For the instructions to get the domain principal, see the Get the domain IAM principal section.

  4. In the **Select a role** menu, select the role that fits your purpose. For the full list of roles, see the Roles recommended for domain authorization section. Wait two to three minutes for the changes to propagate.

  5. Click **Save**.




###  gcloud 

Use the Google Cloud CLI command for your product to grant the required role to the domain principal:
    
    
    principal://dataplex.googleapis.com/projects/DOMAIN_PROJECT_NUMBER/name/locations/LOCATION_ID/dataDomains/DOMAIN_ID
    

For example, using `gcloud` to bind a project:
    
    
    gcloud projects add-iam-policy-binding RESOURCE_PROJECT_ID \
    --member "principal://dataplex.googleapis.com/projects/DOMAIN_PROJECT_NUMBER/name/locations/LOCATION_ID/dataDomains/DOMAIN_ID" \
    --role ROLE
    

Replace the following:

  * RESOURCE_PROJECT_ID: the ID of the target project to authorize.
  * DOMAIN_PROJECT_NUMBER: the project number of the project hosting the data domain.
  * LOCATION_ID: the region where the data domain exists. For example, `us-central1`.
  * DOMAIN_ID: the ID of the data domain.
  * ROLE: the IAM role that fits your required binding purpose.



For specific product commands, such as `bq add-iam-policy-binding` for BigQuery, refer to the product's API documentation.

###  REST 

To grant the domain principal permissions over a resource, you typically get the existing IAM policy using `getIamPolicy`, append the domain principal binding with your chosen role, and set the updated policy using `setIamPolicy`.

The following example shows how to set the IAM policy for a project.

### Get the current IAM policy

Before using any of the request data, make the following replacements: 

  * `RESOURCE_PROJECT_ID`: the ID of the target project to authorize.



HTTP method and URL: 
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/RESOURCE_PROJECT_ID:getIamPolicy

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://cloudresourcemanager.googleapis.com/v1/projects/RESOURCE_PROJECT_ID:getIamPolicy"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://cloudresourcemanager.googleapis.com/v1/projects/RESOURCE_PROJECT_ID:getIamPolicy" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Set the updated policy including the domain principal

Before using any of the request data, make the following replacements: 

  * `RESOURCE_PROJECT_ID`: the ID of the target project to authorize.
  * `DOMAIN_PROJECT_NUMBER`: the project number of the project hosting the data domain.
  * `LOCATION_ID`: the region where the data domain exists. For example, `us-central1`.
  * `DOMAIN_ID`: the ID of the data domain.
  * `ROLE`: the IAM role that fits your required binding purpose.



HTTP method and URL: 
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/RESOURCE_PROJECT_ID:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": {
        "bindings": [
          {
            "role": "ROLE",
            "members": [
              "principal://dataplex.googleapis.com/projects/DOMAIN_PROJECT_NUMBER/name/locations/LOCATION_ID/dataDomains/DOMAIN_ID"
            ]
          }
        ]
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudresourcemanager.googleapis.com/v1/projects/RESOURCE_PROJECT_ID:setIamPolicy"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudresourcemanager.googleapis.com/v1/projects/RESOURCE_PROJECT_ID:setIamPolicy" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

For instructions on setting policies for other resources, see the following API documentation:

  * [Data products](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts/setIamPolicy)
  * [BigQuery datasets](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets/patch)
  * [BigQuery tables](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/setIamPolicy)
  * [Dataform repositories](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/setIamPolicy)
  * [Dataproc Metastore databases](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services.databases/setIamPolicy)
  * [Dataproc Metastoretables](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services.databases.tables/setIamPolicy)
  * [Cloud Spanner databases](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/setIamPolicy)
  * [BigLake tables](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tables/setIamPolicy)
  * [AlloyDB for PostgreSQL instances](https://docs.cloud.google.com/alloydb/docs/reference/rest/v1/projects.locations.clusters.instances/setIamPolicy)
  * [Gemini Enterprise Agent Platform datasets](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1alpha1/projects.locations.datasets/setIamPolicy)



## Bind resources to the domain

After authorizing the domain on the target resources, you can bind the resources to the domain. If you include a project, all resources within the project are automatically added to the domain unless you explicitly override their inclusion.

###  Console 

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. Select the domain you want to add resources to.

  3. Click the **Resources** tab.

  4. Click **Add resources** or **Add projects** , depending on the item that you want to include.

  5. Search for and select the resources that you want to include in the domain.

  6. Click **Select**.




###  REST 

To include a resource in a domain, use the `projects.locations.dataDomains.bindings.create` method. 

To view the payload for the resource that you want to include in the domain, expand one of the following sections: 

### Project

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project hosting the data domain.
  * `LOCATION_ID`: the region where the data domain exists. For example, `us-central1`.
  * `DOMAIN_ID`: the unique identifier of the data domain.
  * `RESOURCE_PROJECT_ID`: the ID of the target project to include in the domain.
  * `BINDING_ID`: an optional unique identifier for this resource binding.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID

Request JSON body: 
    
    
    {
      "resource": "//cloudresourcemanager.googleapis.com/projects/RESOURCE_PROJECT_ID"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### BigQuery dataset and table

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project hosting the data domain.
  * `LOCATION_ID`: the region where the data domain exists. For example, `us-central1`.
  * `DOMAIN_ID`: the unique identifier of the data domain.
  * `RESOURCE_PROJECT_ID`: the ID of the Google Cloud project hosting the resource.
  * `DATASET_ID`: the ID of the target resource (such as a BigQuery dataset).
  * `BINDING_ID`: an optional unique identifier for this resource binding.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID

Request JSON body: 
    
    
    {
      "resource": "//bigquery.googleapis.com/projects/RESOURCE_PROJECT_ID/datasets/DATASET_ID"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Data product

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project hosting the data domain.
  * `LOCATION_ID`: the region where the data domain and resource exist. For example, `us-central1`.
  * `DOMAIN_ID`: the unique identifier of the data domain.
  * `RESOURCE_PROJECT_ID`: the ID of the Google Cloud project hosting the data product.
  * `DATA_PRODUCT_ID`: the unique ID of the target data product.
  * `BINDING_ID`: an optional unique identifier for this resource binding.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID

Request JSON body: 
    
    
    {
      "resource": "//dataplex.googleapis.com/projects/RESOURCE_PROJECT_ID/locations/LOCATION_ID/dataProducts/DATA_PRODUCT_ID"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Dataform repository

Before using any of the request data, make the following replacements: 

  * `DOMAIN_PROJECT_ID`: the ID of the project that hosts the data domain.
  * `DOMAIN_LOCATION_ID`: the region where the data domain is hosted. For example, `us-central1`.
  * `DOMAIN_ID`: the ID of the data domain.
  * `BINDING_ID`: the ID to assign to the new data domain binding.
  * `PROJECT_ID`: the ID of the project hosting the repository.
  * `LOCATION_ID`: the region hosting the repository.
  * `REPOSITORY_ID`: the ID of the Dataform repository.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID

Request JSON body: 
    
    
    {
      "resource": "//dataform.googleapis.com/projects/PROJECT_ID/locations/LOCATION_ID/repositories/REPOSITORY_ID"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Dataproc Metastore database

Before using any of the request data, make the following replacements: 

  * `DOMAIN_PROJECT_ID`: the ID of the project that hosts the data domain.
  * `DOMAIN_LOCATION_ID`: the region where the data domain is hosted. For example, `us-central1`.
  * `DOMAIN_ID`: the ID of the data domain.
  * `BINDING_ID`: the ID to assign to the new data domain binding.
  * `PROJECT_ID`: the ID of the project hosting the database.
  * `LOCATION_ID`: the region hosting the service.
  * `SERVICE_ID`: the ID of the Dataproc Metastore service.
  * `DATABASE_ID`: the ID of the database.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID

Request JSON body: 
    
    
    {
      "resource": "//metastore.googleapis.com/projects/PROJECT_ID/locations/LOCATION_ID/services/SERVICE_ID/databases/DATABASE_ID"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Dataproc Metastore table

Before using any of the request data, make the following replacements: 

  * `DOMAIN_PROJECT_ID`: the ID of the project that hosts the data domain.
  * `DOMAIN_LOCATION_ID`: the region where the data domain is hosted. For example, `us-central1`.
  * `DOMAIN_ID`: the ID of the data domain.
  * `BINDING_ID`: the ID to assign to the new data domain binding.
  * `PROJECT_ID`: the ID of the project hosting the table.
  * `LOCATION_ID`: the region hosting the service.
  * `SERVICE_ID`: the ID of the Dataproc Metastore service.
  * `DATABASE_ID`: the ID of the database.
  * `TABLE_ID`: the ID of the table.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID

Request JSON body: 
    
    
    {
      "resource": "//metastore.googleapis.com/projects/PROJECT_ID/locations/LOCATION_ID/services/SERVICE_ID/databases/DATABASE_ID/tables/TABLE_ID"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Spanner database

Before using any of the request data, make the following replacements: 

  * `DOMAIN_PROJECT_ID`: the ID of the project that hosts the data domain.
  * `DOMAIN_LOCATION_ID`: the region where the data domain is hosted. For example, `us-central1`.
  * `DOMAIN_ID`: the ID of the data domain.
  * `BINDING_ID`: the ID to assign to the new data domain binding.
  * `PROJECT_ID`: the ID of the project hosting the database.
  * `INSTANCE_ID`: the ID of the Spanner instance.
  * `DATABASE_ID`: the ID of the database.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID

Request JSON body: 
    
    
    {
      "resource": "//spanner.googleapis.com/projects/PROJECT_ID/instances/INSTANCE_ID/databases/DATABASE_ID"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### BigLake

Before using any of the request data, make the following replacements: 

  * `DOMAIN_PROJECT_ID`: the ID of the project that hosts the data domain.
  * `DOMAIN_LOCATION_ID`: the region where the data domain is hosted. For example, `us-central1`.
  * `DOMAIN_ID`: the ID of the data domain.
  * `BINDING_ID`: the ID to assign to the new data domain binding.
  * `PROJECT_ID`: the ID of the project hosting the catalog.
  * `LOCATION_ID`: the region hosting the catalog.
  * `CATALOG_ID`: the ID of the catalog.
  * `DATABASE_ID`: the ID of the database.
  * `TABLE_ID`: the ID of the table.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID

Request JSON body: 
    
    
    {
      "resource": "//biglake.googleapis.com/projects/PROJECT_ID/catalogs/CATALOG_ID/databases/DATABASE_ID/tables/TABLE_ID"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### AlloyDB for PostgreSQL

Before using any of the request data, make the following replacements: 

  * `DOMAIN_PROJECT_ID`: the ID of the project that hosts the data domain.
  * `DOMAIN_LOCATION_ID`: the region where the data domain is hosted. For example, `us-central1`.
  * `DOMAIN_ID`: the ID of the data domain.
  * `BINDING_ID`: the ID to assign to the new data domain binding.
  * `PROJECT_ID`: the ID of the project hosting the cluster.
  * `LOCATION_ID`: the region hosting the cluster.
  * `CLUSTER_ID`: the ID of the cluster.
  * `INSTANCE_ID`: the ID of the instance.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID

Request JSON body: 
    
    
    {
      "resource": "//alloydb.googleapis.com/projects/PROJECT_ID/locations/LOCATION_ID/clusters/CLUSTER_ID/instances/INSTANCE_ID"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Gemini Enterprise Agent Platform

Before using any of the request data, make the following replacements: 

  * `DOMAIN_PROJECT_ID`: the ID of the project that hosts the data domain.
  * `DOMAIN_LOCATION_ID`: the region where the data domain is hosted. For example, `us-central1`.
  * `DOMAIN_ID`: the ID of the data domain.
  * `BINDING_ID`: the ID to assign to the new data domain binding.
  * `PROJECT_ID`: the ID of the project hosting the dataset.
  * `LOCATION_ID`: the region hosting the dataset.
  * `DATASET_ID`: the ID of the dataset.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID

Request JSON body: 
    
    
    {
      "resource": "//aiplatform.googleapis.com/projects/PROJECT_ID/locations/LOCATION_ID/datasets/DATASET_ID"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/DOMAIN_PROJECT_ID/locations/DOMAIN_LOCATION_ID/dataDomains/DOMAIN_ID/bindings?data_domain_binding_id=BINDING_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## View included resources

View the folders, projects, and resources directly bound to a data domain.

###  Console 

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. Click the domain name.

  3. Click the **Resources** tab. The list displays resources directly included in the domain.




###  REST 

To list included resource bindings, use the `projects.locations.dataDomains.bindings.list` method:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region where the data domain exists. For example, `us-central1`.
  * `DOMAIN_ID`: the unique identifier of the data domain.



HTTP method and URL: 
    
    
    GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Remove a resource from the domain

Removing a resource unbinds it from the data domain hierarchy.

###  Console 

  1. In the Google Cloud console, go to the **Data domains** page.

[Go to Data domains](https://console.cloud.google.com/dataplex/domains)

  2. Click the domain name.

  3. Click the **Resources** tab.

  4. Select the resource you want to remove.

  5. Click **Delete** and confirm deletion.




###  REST 

To delete a resource binding, use the `projects.locations.dataDomains.bindings.delete` method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION_ID`: the region where the data domain exists. For example, `us-central1`.
  * `DOMAIN_ID`: the unique identifier of the data domain.
  * `BINDING_ID`: the unique identifier of the resource binding.



HTTP method and URL: 
    
    
    DELETE https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings/BINDING_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings/BINDING_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION_ID/dataDomains/DOMAIN_ID/bindings/BINDING_ID" | Select-Object -Expand Content

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
