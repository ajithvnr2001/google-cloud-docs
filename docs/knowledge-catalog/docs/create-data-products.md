---
url: https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products/
title: Create data products \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:29.057573+00:00
---

# Create data products  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Create data products Stay organized with collections  Save and categorize content based on your preferences. 

Data products in Knowledge Catalog (formerly Dataplex Universal Catalog) let you package related data assets into a single, discoverable unit. You can then configure access groups, attach refresh contracts and metadata aspects, and add documentation so consumers can evaluate and request access to those assets.

This document is intended for data product owners. For more information about the architecture and key concepts of data products, see [About data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview).

## Before you begin

Before you create data products, complete the following prerequisites.

### Enable Gemini

Configuring Gemini in your data asset is an optional but highly recommended step before you create your first data product. 

By default, creating a data product requires you to manually enter business descriptions, technical definitions, and onboarding documentation for your assets. When you enable Gemini integration, Knowledge Catalog leverages AI assistance to automatically analyze your schemas and data scan results to generate the following:

  * **Business documentation:** Generates documentation templates and clear descriptions for your data product and its individual data assets.
  * **Insights and sample queries:** Constructs ready-to-use sample queries based on the asset's schema layout, enabling data consumers to immediately start querying the product upon approval.

**Note:** This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

If you choose not to enable Gemini, you can skip this section. However, you must manually provide all asset metadata and query templates during creation.

For more information about enabling Gemini in BigQuery, see [Set up Gemini in BigQuery](https://docs.cloud.google.com/gemini/docs/bigquery/set-up-gemini).

**Note** : Gemini in BigQuery is part of Gemini for Google Cloud and doesn't support the same compliance and security offerings as BigQuery. You should only set up Gemini in BigQuery for BigQuery projects that don't require [compliance offerings that aren't supported by Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/discover/certifications). For information about how to turn off or prevent access to Gemini in BigQuery, see [Turn off Gemini in BigQuery](https://docs.cloud.google.com/bigquery/docs/gemini-set-up#turn-off). 

### Enable APIs

Enable the Dataplex, BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com)

### Create data assets

Ensure that your data assets (for example, BigQuery datasets, tables, and views) are created and populated.

For more information about creating data assets, see the following documents:

  * [Create BigQuery datasets](https://docs.cloud.google.com/bigquery/docs/datasets)
  * [Create and use BigQuery tables](https://docs.cloud.google.com/bigquery/docs/tables)
  * [Create logical views in BigQuery](https://docs.cloud.google.com/bigquery/docs/views)
  * [Create materialized views in BigQuery](https://docs.cloud.google.com/bigquery/docs/materialized-views-create)



### Configure identities

Identify or create the [Google Groups](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console) or [service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview) that you want to configure in your data product.

**Note:** To prevent unintended access to underlying data, create unique service accounts and Google Groups for each data product. For enhanced security and governance, we recommend using [Security Google Groups](https://docs.cloud.google.com/identity/docs/how-to/update-group-to-security-group).

### Optional: Configure Looker (Google Cloud core) for data products

If you plan to include Looker (Google Cloud core) assets in your data product, complete the following additional steps:

  1. Ensure that the catalog entry for the Looker (Google Cloud core) resource already exists in Knowledge Catalog in the same region as the data product. For more information, see [Manage Looker (Google Cloud core) resources with Knowledge Catalog](https://docs.cloud.google.com/knowledge-catalog/docs/manage-looker-core-metadata).
  2. Configure [Google OAuth](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication) and [enable mirrored groups](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#steps_to_enable_mirrored_groups) in your Looker (Google Cloud core) instance to create a read-only Looker group for your Google Group.
  3. Assign [folder access levels](https://docs.cloud.google.com/looker/docs/admin-panel-users-content-access#access_levels) and [Looker roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) to the mirrored Looker group.



### Required roles

This section outlines the minimum IAM roles required for the following primary sections:

  * Data product owners: users who create, configure, and manage data products and their associated assets

  * Data product consumers: users who search for, view, and request access to published data products




#### Required roles for data product owners

To get the permissions that you need to create and manage data products, ask your administrator to grant you the following IAM roles on the project: 

  * Full permissions to create, update, delete, manage permissions, and approve or reject access requests for data products: [Dataplex Data Products Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`) 
  * Update and manage permissions, and approve or reject access requests for data products: [Dataplex Data Products Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`) 
  * Add metadata aspects (such as `schema`, `overview`, `contacts`, and `queries`): [Dataplex Entry and EntryLink Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`) 
  * Search for and add assets: [Dataplex Catalog Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) 
  * Edit system aspect types (such as `overview`, `contact`, `contract`, and `queries`): [Dataplex Catalog Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) 
  * Create or retrieve insights data scans for automated documentation and insights generation: [Dataplex DataScan Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataScanAdmin) (`roles/dataplex.dataScanAdmin`) 
  * Access Looker (Google Cloud core) metadata in Knowledge Catalog: Looker Schema Viewer (`roles/looker.schemaViewer`) - on the project that hosts the Looker (Google Cloud core) instance 
  * Grant `roles/looker.instanceUser` to the access group's Google Group: Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) - on the project that hosts the Looker (Google Cloud core) instance 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create and manage data products. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create and manage data products:

  * Create a data product: `dataplex.dataProducts.create`
  * List data products in a project: `dataplex.dataProducts.list`
  * Get or view data product: `dataplex.dataProducts.get`
  * Edit an existing data product: `dataplex.dataProducts.update`
  * Delete data product: `dataplex.dataProducts.delete`
  * Approve data product access request: `dataplex.dataProducts.approve`
  * Search for a data product using Knowledge Catalog: 
    * `dataplex.dataProducts.get`
    * `dataplex.projects.search`
  * Create data product access request: `dataplex.dataProducts.get`
  * Create a data asset: `dataplex.dataAssets.create`
  * List data assets within a data product: `dataplex.dataAssets.list`
  * Get data asset: `dataplex.dataAssets.get`
  * Edit an existing data asset: `dataplex.dataAssets.update`
  * Delete data asset: `dataplex.dataAssets.delete`
  * Create a data scan: `dataplex.datascans.create`
  * List all data scans: `dataplex.datascans.list`
  * Get a data scan: `dataplex.datascans.get`
  * Run a data scan: `dataplex.datascans.run`
  * Edit the `overview` system aspect type: `dataplex.entryGroups.useOverviewAspect`
  * Edit the `refresh cadence` system aspect type: `dataplex.entryGroups.useRefreshCadenceAspect`
  * Edit the `queries` system aspect type: `dataplex.entryGroups.useQueriesAspect`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Required roles for data product consumers

For the data product consumers to search for, view, and request access to data products, as a data product owner, you must ensure the data product is discoverable. To do this, grant the data product consumers the following IAM roles on the data product:

  * Search for data products and request access to them: Dataplex Data Product Consumer (`dataplex.dataProductsConsumer`) and Dataplex Catalog Viewer (`roles/dataplex.catalogViewer`)
  * Read-only access to view data product definitions and metadata: Dataplex Data Product Viewer (`dataplex.dataProductsViewer`)



## Create and configure a data product

Creating a data product involves the following high-level tasks:

  1. **Create a data product**

This mandatory initial step requires defining core details such as a unique data product name, description, region where the data product is created, and contact details.

  2. **Optional: Add assets**

In this phase, you select assets to include in the data product. A key constraint is that assets must reside in the same region as the data product itself. You can add up to 10 assets at a time, with a total maximum of 50 assets allowed per data product.

For the list of supported assets, see [Assets supported](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview#assets-supported).

  3. **Optional: Configure access groups and asset permissions**

In this optional phase, you simplify access control by creating access groups. These access groups act as user-friendly aliases (for example, `Analyst` or `Reader`) for underlying Google Groups and service accounts. You then assign permissions by selecting a specific IAM role and mapping it to an access group for a specific asset.

  4. **Optional: Add contract and aspect details**

In this phase, you enhance governance and data discoverability by attaching metadata frameworks. You can add a [contract](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview#contract) to formally communicate your data refresh cadence, specifying parameters such as refresh frequency, timing, and variance thresholds. You can also attach custom aspects to provide additional business or technical metadata for your data product.

  5. **Optional: Add additional details**

In this final phase, you add rich text documentation, such as user onboarding guides, business definitions, and sample queries, to help consumers interact with the data product immediately upon approval.


**Note:** You can perform the optional steps during data product creation or post creation.

To create and configure a data product, complete the steps in the following sections:

### Create a data product

Define the core details for your data product, such as its ID, location, and contacts. When you define data products and their assets, ensure their IDs adhere to [Knowledge Catalog resource naming guidelines](https://docs.cloud.google.com/knowledge-catalog/docs/guidelines-resources).

**Note:** The REST API methods for creating and configuring data products and assets are long-running operations. When you call these methods, the API returns an [Operation](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.operations) object that you can use to check the status of the task.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Data products** page.

[Go to Data products](https://console.cloud.google.com/dataplex/govern/data-products)

  2. Click **Create**.

  3. In the **Create data products** pane, enter the following details:

     * **Data product name** : Enter a unique name for your data product.
     * **Data product ID** : This is an auto-generated unique identifier. You can edit this field.
     * **Project ID** : This is a unique identifier of the project where the data product is created. Browse and select the project.
     * **Region** : Select the region or multi-region where the data product is created.
     * **Data product icon** : Browse and select an icon to visually identify the data product. This is optional.
     * **Description** : Enter a brief description of the data product.
     * **Contacts** : Provide the point of contact information for governance and approval workflows:

       * **Data product owner(s) email address** : Enter the email address of the data product owners.
       * **Data product approver(s) email address:** Enter the email address of the designated approvers responsible for signing off on access requests or modifications.
     * **Labels** : Add key-value labels to organize your resources. This is optional.

  4. Click **Create data product**.




### Terraform

To create a data product, use the [`google_dataplex_data_product`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_data_product) and [IAM](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_data_product_iam) resources.
    
    
    resource "google_dataplex_data_product" "default" {
      project         = "PROJECT_ID"
      location        = "LOCATION"
      data_product_id = "DATA_PRODUCT_ID"
      display_name    = "DISPLAY_NAME"
      description     = "DESCRIPTION"
      owner_emails    = ["EMAIL_IDs"]
    
      # Optional: Configures designated approvers for access requests
      access_approval_config {
        approver_emails = ["APPROVER_EMAIL_IDs"]
      }
    
      # Optional: Base64-encoded icon (Max 3.0MiB)
      icon = "ICON_BASE64_STRING"
    }
    
    resource "google_dataplex_data_product_iam_member" "consumer_binding" {
      project         = "PROJECT_ID"
      location        = "LOCATION"
      data_product_id = "DATA_PRODUCT_ID"
      role            = "roles/dataplex.dataProductsConsumer"
      member          = "MEMBER"
    }
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project.
  * LOCATION: the region in which you want to create the data product.
  * DATA_PRODUCT_ID: a unique ID for your data product.
  * DISPLAY_NAME: a user-friendly name for your data product.
  * DESCRIPTION: a brief description of the data product.
  * EMAIL_IDs: comma-separated email addresses of the data product owners, for example—`["user1@example.com", "user2@example.com"]`.
  * APPROVER_EMAIL_IDs: comma-separated email addresses of the designated approvers responsible for signing off on access requests or modifications for this data product.
  * ICON_BASE64_STRING: the raw base64-encoded image data representing the data product. The maximum size is 3.0 MiB. Don't include the data URL scheme prefix.
  * MEMBER: the user, service account, or group receiving the consumer role (for example, `group:all-analysts@example.com`).



### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedDataProductServiceClientSnippets
    {
        /// <summary>Snippet for CreateDataProduct</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void CreateDataProductRequestObject()
        {
            // Create client
            [DataProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html) dataProductServiceClient = [DataProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_Create)();
            // Initialize request argument(s)
            [CreateDataProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateDataProductRequest.html) request = new [CreateDataProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateDataProductRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)("[PROJECT]", "[LOCATION]"),
                DataProductId = "",
                DataProduct = new [DataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProduct.html)(),
                ValidateOnly = false,
            };
            // Make the request
            Operation<DataProduct, OperationMetadata> response = dataProductServiceClient.[CreateDataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_CreateDataProduct_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Dataplex_V1_DataProduct_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<DataProduct, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [DataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProduct.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<DataProduct, OperationMetadata> retrievedResponse = dataProductServiceClient.[PollOnceCreateDataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_PollOnceCreateDataProduct_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [DataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProduct.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewDataProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_DataProductClient_NewDataProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.CreateDataProductRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#CreateDataProductRequest.
    	}
    	op, err := c.CreateDataProduct(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CreateDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataProductRequest.html);
    import com.google.cloud.dataplex.v1.[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct.html);
    import com.google.cloud.dataplex.v1.[DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html);
    import com.google.cloud.dataplex.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html);
    
    public class SyncCreateDataProduct {
    
      public static void main(String[] args) throws Exception {
        syncCreateDataProduct();
      }
    
      public static void syncCreateDataProduct() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html) dataProductServiceClient = [DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html).create()) {
          [CreateDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataProductRequest.html) request =
              [CreateDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataProductRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.LocationName.html).of("[PROJECT]", "[LOCATION]").toString())
                  .[setDataProductId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataProductRequest.Builder.html#com_google_cloud_dataplex_v1_CreateDataProductRequest_Builder_setDataProductId_java_lang_String_)("dataProductId1437828576")
                  .setDataProduct([DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct.html).newBuilder().build())
                  .setValidateOnly(true)
                  .build();
          [DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct.html) response = dataProductServiceClient.[createDataProductAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html#com_google_cloud_dataplex_v1_DataProductServiceClient_createDataProductAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_LocationName_com_google_cloud_dataplex_v1_DataProduct_java_lang_String_)(request).get();
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The parent resource where this data product will be created.
     *  Format: projects/{project_id_or_number}/locations/{location_id}
     */
    // const parent = 'abc123'
    /**
     *  Optional. The ID of the data product to create.
     *  The ID must conform to RFC-1034 and contain only lower-case letters (a-z),
     *  numbers (0-9), or hyphens, with the first character a letter, the last a
     *  letter or a number, and a 63 character maximum. Characters outside of
     *  ASCII are not permitted.
     *  Valid format regex: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`
     *  If not provided, a system generated ID will be used.
     */
    // const dataProductId = 'abc123'
    /**
     *  Required. The data product to create.
     */
    // const dataProduct = {}
    /**
     *  Optional. Validates the request without actually creating the data product.
     *  Default: false.
     */
    // const validateOnly = true
    
    // Imports the Dataplex library
    const {DataProductServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [DataProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callCreateDataProduct() {
      // Construct request
      const request = {
        parent,
        dataProduct,
      };
    
      // Run request
      const [operation] = await dataplexClient.createDataProduct(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callCreateDataProduct();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_create_data_product():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataProductServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_product_service.DataProductServiceClient.html)()
    
        # Initialize request argument(s)
        data_product = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataProduct](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DataProduct.html)()
        data_product.display_name = "display_name_value"
        data_product.owner_emails = ["owner_emails_value1", "owner_emails_value2"]
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CreateDataProductRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.CreateDataProductRequest.html)(
            parent="parent_value",
            data_product=data_product,
        )
    
        # Make the request
        operation = client.[create_data_product](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_product_service.DataProductServiceClient.html#google_cloud_dataplex_v1_services_data_product_service_DataProductServiceClient_create_data_product)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### REST

To create a data product, use the [`dataProducts.create`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts/create) method.

For example, send the following `POST` request:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{"display_name": "DISPLAY_NAME", "owner_emails": ["EMAIL_IDs"], "access_approval_config": { "approver_emails": ["APPROVER_EMAIL_IDs"]} }' \
    https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/dataProducts?data_product_id=DATA_PRODUCT_ID
    

Replace the following:

  * DISPLAY_NAME: a user-friendly name for your data product
  * EMAIL_IDs: comma-separated email addresses of the data product owners
  * APPROVER_EMAIL_IDs: comma-separated email addresses of the designated approvers responsible for signing off on access requests or modifications.
  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the region in which you want to create the data product
  * DATA_PRODUCT_ID: a unique ID for your data product



### Optional: Add assets

You can add various data assets, such as BigQuery tables, views, datasets, and models to your data product. For the list of supported assets, see [Assets supported](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview#assets-supported).

### Console

  1. In the **Add assets** pane, click **+Add**.

  2. Search for and select the assets that you want to add to your data product. The assets you select must reside in the same region as the data product.

If you have necessary permissions, you can view the metadata of assets by clicking the asset.

  3. To refine the search results, use **Filters**.

  4. After you select the assets, click **Add**.

**Note:** You can add up to 10 assets at a time, with a total maximum of 50 assets allowed per data product.
  5. Click **Continue**.




### Terraform

To add a data asset to your data product, use the [`google_dataplex_data_product_data_asset`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_data_product_data_asset) resource.
    
    
    resource "google_dataplex_data_product_data_asset" "example_asset" {
    project         = "PROJECT_ID"
    location        = "LOCATION"
    data_product_id = "DATA_PRODUCT_ID"
    data_asset_id   = "DATA_ASSET_ID"
    resource        = "RESOURCE_NAME"
    }
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the region where the data product exists
  * DATA_PRODUCT_ID: the ID of the data product
  * DATA_ASSET_ID: a unique ID for this data asset within the data product
  * RESOURCE_NAME: the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of the data asset (for example, `//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID`)



### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    
    public sealed partial class GeneratedDataProductServiceClientSnippets
    {
        /// <summary>Snippet for CreateDataAsset</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void CreateDataAssetRequestObject()
        {
            // Create client
            [DataProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html) dataProductServiceClient = [DataProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_Create)();
            // Initialize request argument(s)
            [CreateDataAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateDataAssetRequest.html) request = new [CreateDataAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.CreateDataAssetRequest.html)
            {
                ParentAsDataProductName = [DataProductName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductName.html).[FromProjectLocationDataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductName.html#Google_Cloud_Dataplex_V1_DataProductName_FromProjectLocationDataProduct_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]"),
                DataAssetId = "",
                DataAsset = new [DataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataAsset.html)(),
                ValidateOnly = false,
            };
            // Make the request
            Operation<DataAsset, OperationMetadata> response = dataProductServiceClient.[CreateDataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_CreateDataAsset_Google_Cloud_Dataplex_V1_CreateDataAssetRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<DataAsset, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [DataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataAsset.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<DataAsset, OperationMetadata> retrievedResponse = dataProductServiceClient.[PollOnceCreateDataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_PollOnceCreateDataAsset_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [DataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataAsset.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewDataProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_DataProductClient_NewDataProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.CreateDataAssetRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#CreateDataAssetRequest.
    	}
    	op, err := c.CreateDataAsset(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[CreateDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAssetRequest.html);
    import com.google.cloud.dataplex.v1.[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset.html);
    import com.google.cloud.dataplex.v1.[DataProductName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductName.html);
    import com.google.cloud.dataplex.v1.[DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html);
    
    public class SyncCreateDataAsset {
    
      public static void main(String[] args) throws Exception {
        syncCreateDataAsset();
      }
    
      public static void syncCreateDataAsset() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html) dataProductServiceClient = [DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html).create()) {
          [CreateDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAssetRequest.html) request =
              [CreateDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAssetRequest.html).newBuilder()
                  .setParent([DataProductName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductName.html).of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
                  .[setDataAssetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.CreateDataAssetRequest.Builder.html#com_google_cloud_dataplex_v1_CreateDataAssetRequest_Builder_setDataAssetId_java_lang_String_)("dataAssetId2108984609")
                  .setDataAsset([DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset.html).newBuilder().build())
                  .setValidateOnly(true)
                  .build();
          [DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset.html) response = dataProductServiceClient.[createDataAssetAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html#com_google_cloud_dataplex_v1_DataProductServiceClient_createDataAssetAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_DataProductName_com_google_cloud_dataplex_v1_DataAsset_java_lang_String_)(request).get();
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The parent resource where this data asset will be created.
     *  Format:
     *  projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}
     */
    // const parent = 'abc123'
    /**
     *  Optional. The ID of the data asset to create.
     *  The ID must conform to RFC-1034 and contain only lower-case letters (a-z),
     *  numbers (0-9), or hyphens, with the first character a letter, the last a
     *  letter or a number, and a 63 character maximum. Characters outside of
     *  ASCII are not permitted.
     *  Valid format regex: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`
     *  If not provided, a system generated ID will be used.
     */
    // const dataAssetId = 'abc123'
    /**
     *  Required. The data asset to create.
     */
    // const dataAsset = {}
    /**
     *  Optional. Validates the request without actually creating the data asset.
     *  Defaults to false.
     */
    // const validateOnly = true
    
    // Imports the Dataplex library
    const {DataProductServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [DataProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callCreateDataAsset() {
      // Construct request
      const request = {
        parent,
        dataAsset,
      };
    
      // Run request
      const [operation] = await dataplexClient.createDataAsset(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callCreateDataAsset();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_create_data_asset():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataProductServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_product_service.DataProductServiceClient.html)()
    
        # Initialize request argument(s)
        data_asset = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataAsset](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DataAsset.html)()
        data_asset.resource = "resource_value"
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[CreateDataAssetRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.CreateDataAssetRequest.html)(
            parent="parent_value",
            data_asset=data_asset,
        )
    
        # Make the request
        operation = client.[create_data_asset](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_product_service.DataProductServiceClient.html#google_cloud_dataplex_v1_services_data_product_service_DataProductServiceClient_create_data_asset)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### REST

To add a data asset to your data product, use the [`dataAssets.create`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts.dataAssets/create) method.

For example, send the following `POST` request:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{"resource": "RESOURCE_NAME"}' \
    https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/dataProducts/DATA_PRODUCT_ID/dataAssets?data_asset_id=DATA_ASSET_ID
    

Replace the following:

  * RESOURCE_NAME: the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of the data asset (for example, `//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID`)
  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the region where the data product exists
  * DATA_PRODUCT_ID: the ID of the data product
  * DATA_ASSET_ID: a unique ID for this data asset within the data product



### Optional: Configure access groups and asset permissions

In the **Configure access groups and asset permissions** pane, you can create [access groups](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview#access-group) and assign permissions to assets.

#### Configure access groups

### Console

  1. Click **Add access group**.

  2. In the **Access group name** field, enter a name for the access group. For example, `Analyst`.

  3. In the **Access group description** field, enter a description for the access group.

  4. In the **Access group identifier** field, enter the email address of a Google Group that you want to assign to this access group

Data product consumers who request access for themselves are added as members to the mapped Google Group.

For more information about creating Google Groups, see [Create and manage Google Groups in the Google Cloud console](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console).

  5. In the **Access group service account** field, enter the email address of a service account that you want to assign to this access group.

Data product consumers who request access for their service accounts are granted the Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) IAM role to impersonate the data producer service account mapped to the access group.

For more information about creating service accounts, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create).

  6. Optional: In the **Default role** field, select a default IAM role (for example, `BigQuery Data Viewer`) for this access group. This role is automatically granted on all existing and newly added supported assets in the data product unless you override it at the asset level.

  7. Click **Done**.

  8. To add another access group, click **Add access group** and repeat the steps.

You can add a maximum of three access groups per data product.

  9. Click **Save**.




### Terraform

To define access groups for your data product, use the `access_groups` nested block within the [google_dataplex_data_product](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_data_product) resource.

For example, use the following configuration:
    
    
    resource "google_dataplex_data_product" "example_data_product" {
      project         = "PROJECT_ID"
      location        = "LOCATION"
      data_product_id = "DATA_PRODUCT_ID"
      display_name    = "DISPLAY_NAME"
      owner_emails    = ["EMAIL_IDs"]
    
      access_groups {
        id           = "analyst" # Internal identifier for configuration
        group_id     = "analyst" # Unique identifier of the access group, should be same as the 'id'
        display_name = "Business Analyst"
        description  = "Access group for regional analysts"
        principal {
          google_group = "analyst-team@example.com"
        }
      }
    
    # Service account principal
      access_groups {
        id           = "scientist"
        group_id     = "scientist"
        display_name = "Data Scientist"
        principal {
          service_account = "SERVICE_ACCOUNT_EMAIL_ADDRESS"
        }
      }
    }
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the region where the data product exists
  * DATA_PRODUCT_ID: a unique ID for the data product
  * DISPLAY_NAME: a user-friendly name for your data product
  * EMAIL_IDs: comma-separated email addresses of the data product owners, for example—`["user1@example.com", "user2@example.com"]`
  * SERVICE_ACCOUNT_EMAIL_ADDRESS: the email address of the service account



### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedDataProductServiceClientSnippets
    {
        /// <summary>Snippet for UpdateDataProduct</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void UpdateDataProductRequestObject()
        {
            // Create client
            [DataProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html) dataProductServiceClient = [DataProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_Create)();
            // Initialize request argument(s)
            [UpdateDataProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateDataProductRequest.html) request = new [UpdateDataProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateDataProductRequest.html)
            {
                DataProduct = new [DataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProduct.html)(),
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
                ValidateOnly = false,
            };
            // Make the request
            Operation<DataProduct, OperationMetadata> response = dataProductServiceClient.[UpdateDataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_UpdateDataProduct_Google_Cloud_Dataplex_V1_DataProduct_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<DataProduct, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [DataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProduct.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<DataProduct, OperationMetadata> retrievedResponse = dataProductServiceClient.[PollOnceUpdateDataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_PollOnceUpdateDataProduct_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [DataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProduct.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewDataProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_DataProductClient_NewDataProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.UpdateDataProductRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#UpdateDataProductRequest.
    	}
    	op, err := c.UpdateDataProduct(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct.html);
    import com.google.cloud.dataplex.v1.[DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html);
    import com.google.cloud.dataplex.v1.[UpdateDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataProductRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    
    public class SyncUpdateDataProduct {
    
      public static void main(String[] args) throws Exception {
        syncUpdateDataProduct();
      }
    
      public static void syncUpdateDataProduct() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html) dataProductServiceClient = [DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html).create()) {
          [UpdateDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataProductRequest.html) request =
              [UpdateDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataProductRequest.html).newBuilder()
                  .setDataProduct([DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct.html).newBuilder().build())
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().build())
                  .setValidateOnly(true)
                  .build();
          [DataProduct](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProduct.html) response = dataProductServiceClient.[updateDataProductAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html#com_google_cloud_dataplex_v1_DataProductServiceClient_updateDataProductAsync_com_google_cloud_dataplex_v1_DataProduct_com_google_protobuf_FieldMask_)(request).get();
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The data product to update.
     *  The data product's `name` field is used to identify the data product to
     *  update.
     */
    // const dataProduct = {}
    /**
     *  Optional. The list of fields to update.
     *  If this is empty or not set, then all the fields will be updated.
     */
    // const updateMask = {}
    /**
     *  Optional. Validates the request without actually updating the data product.
     *  Default: false.
     */
    // const validateOnly = true
    
    // Imports the Dataplex library
    const {DataProductServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [DataProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callUpdateDataProduct() {
      // Construct request
      const request = {
        dataProduct,
      };
    
      // Run request
      const [operation] = await dataplexClient.updateDataProduct(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callUpdateDataProduct();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_update_data_product():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataProductServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_product_service.DataProductServiceClient.html)()
    
        # Initialize request argument(s)
        data_product = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataProduct](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DataProduct.html)()
        data_product.display_name = "display_name_value"
        data_product.owner_emails = ["owner_emails_value1", "owner_emails_value2"]
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[UpdateDataProductRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.UpdateDataProductRequest.html)(
            data_product=data_product,
        )
    
        # Make the request
        operation = client.[update_data_product](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_product_service.DataProductServiceClient.html#google_cloud_dataplex_v1_services_data_product_service_DataProductServiceClient_update_data_product)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### REST

To configure an access group for the data product, use the [`dataProducts.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts/patch) method.

For example, send the following `PATCH` request:
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{"access_groups": ACCESS_GROUPS_MAP}' \
    https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/dataProducts/DATA_PRODUCT_ID?update_mask="access_groups"
    

Replace the following:

  * ACCESS_GROUPS_MAP: a JSON object representing a map where each key is an access group ID and the value is an [AccessGroup](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts#accessgroup) object. For example:
        
        {
        "analyst": {
          "id": "analyst",
          "display_name": "Analyst access group",
          "description": "Access group for analysts",
          "principal":
            {
              "google_group": "analyst-team@example.com",
              "service_account": "analyst-svc@gserviceaccount.com"
            },
          "default_iam_role_config":
            {
              "role": "roles/bigquery.dataViewer"
            }
        }
        }
        

  * PROJECT_ID: the ID of your Google Cloud project

  * LOCATION: the region where the data product exists

  * DATA_PRODUCT_ID: the ID of your data product




#### Configure asset permissions

After you configure access groups, you can configure permissions for the assets in the data product.

If you configured a default IAM role for an access group, supported assets automatically inherit that role (indicated by a **Default** label in the **Permissions** column). You can override the default role for specific assets by assigning a different role.

### Console

  1. In the **Asset permissions** section, select the asset for which you want to configure permissions. You can select and configure permissions for up to 10 assets at a time.

  2. Click **Configure permissions**.

  3. In the **Select access group** field, select an access group.

  4. In the **Assign IAM role** field, select an IAM role that you want to assign to the access group.

For example, if your asset is a BigQuery table named `Sales`, and if you selected `Analyst` access group, and assigned `BigQuery Metadata Viewer` role to this access group, the data product consumers who are part of the `Analyst` access group have `BigQuery Metadata Viewer` permission on the `Sales` table.

You can add multiple roles to an asset.

  5. Click **Configure**. The **Permissions** column in the assets table displays the assigned permissions and their configuration state for each access group:

     * **Applied** : The IAM role (either inherited from the access group's default role or configured specifically for the asset) is active on the underlying resource.
     * **Failed** : Applying the IAM role to the underlying resource failed. You can find the detailed failure reason in Cloud Logging.
     * **Unsupported** : Applying permissions isn't supported for this asset's resource type.
  6. To configure permissions for other assets, repeat the steps.

  7. Click **Continue**.




### Terraform

Assign IAM roles to your access groups for specific assets using the `access_group_configs` block in the [google_dataplex_data_product_data_asset](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_data_product_data_asset) resource.

For example, use the following configuration:
    
    
    resource "google_dataplex_data_product_data_asset" "example_data_asset" {
    project         = "PROJECT_ID"
    location        = "LOCATION"
    data_product_id = "DATA_PRODUCT_ID"
    data_asset_id   = "DATA_ASSET_ID"
    resource        = "RESOURCE_NAME"
    
    access_group_configs {
      access_group = "analyst" # Must match the 'id' defined in google_dataplex_data_product
      iam_roles    = ["roles/bigquery.dataViewer"]
    }
    }
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the region where the data product exists
  * DATA_PRODUCT_ID: the ID of the data product
  * DATA_ASSET_ID: a unique ID for this data asset within the data product
  * RESOURCE_NAME: the [full resource name](https://docs.cloud.google.com/iam/docs/full-resource-names) of the data asset (for example, `//bigquery.googleapis.com/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID`)



### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedDataProductServiceClientSnippets
    {
        /// <summary>Snippet for UpdateDataAsset</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void UpdateDataAssetRequestObject()
        {
            // Create client
            [DataProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html) dataProductServiceClient = [DataProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_Create)();
            // Initialize request argument(s)
            [UpdateDataAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateDataAssetRequest.html) request = new [UpdateDataAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.UpdateDataAssetRequest.html)
            {
                DataAsset = new [DataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataAsset.html)(),
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)(),
                ValidateOnly = false,
            };
            // Make the request
            Operation<DataAsset, OperationMetadata> response = dataProductServiceClient.[UpdateDataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_UpdateDataAsset_Google_Cloud_Dataplex_V1_DataAsset_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<DataAsset, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [DataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataAsset.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<DataAsset, OperationMetadata> retrievedResponse = dataProductServiceClient.[PollOnceUpdateDataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_PollOnceUpdateDataAsset_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [DataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataAsset.html) retrievedResult = retrievedResponse.Result;
            }
        }
    }

### Go

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    //go:build examples
    
    package main
    
    import (
    	"context"
    
    	dataplex "cloud.google.com/go/dataplex/apiv1"
    	dataplexpb "cloud.google.com/go/dataplex/apiv1/dataplexpb"
    )
    
    func main() {
    	ctx := context.Background()
    	// This snippet has been automatically generated and should be regarded as a code template only.
    	// It will require modifications to work:
    	// - It may require correct/in-range values for request initialization.
    	// - It may require specifying regional endpoints when creating the service client as shown in:
    	//   https://pkg.go.dev/cloud.google.com/go#hdr-Client_Options
    	c, err := dataplex.[NewDataProductClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dataplex/latest/apiv1.html#cloud_google_com_go_dataplex_apiv1_DataProductClient_NewDataProductClient)(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	defer c.Close()
    
    	req := &dataplexpb.UpdateDataAssetRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#UpdateDataAssetRequest.
    	}
    	op, err := c.UpdateDataAsset(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    	// TODO: Use resp.
    	_ = resp
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset.html);
    import com.google.cloud.dataplex.v1.[DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html);
    import com.google.cloud.dataplex.v1.[UpdateDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataAssetRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    
    public class SyncUpdateDataAsset {
    
      public static void main(String[] args) throws Exception {
        syncUpdateDataAsset();
      }
    
      public static void syncUpdateDataAsset() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html) dataProductServiceClient = [DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html).create()) {
          [UpdateDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataAssetRequest.html) request =
              [UpdateDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.UpdateDataAssetRequest.html).newBuilder()
                  .setDataAsset([DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset.html).newBuilder().build())
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().build())
                  .setValidateOnly(true)
                  .build();
          [DataAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAsset.html) response = dataProductServiceClient.[updateDataAssetAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html#com_google_cloud_dataplex_v1_DataProductServiceClient_updateDataAssetAsync_com_google_cloud_dataplex_v1_DataAsset_com_google_protobuf_FieldMask_)(request).get();
        }
      }
    }

### Node.js

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. The data asset to update.
     *  The data asset's `name` field is used to identify the data asset to update.
     */
    // const dataAsset = {}
    /**
     *  Optional. The list of fields to update.
     *  If this is empty or not set, then all the fields will be updated.
     */
    // const updateMask = {}
    /**
     *  Optional. Validates the request without actually updating the data asset.
     *  Defaults to false.
     */
    // const validateOnly = true
    
    // Imports the Dataplex library
    const {DataProductServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [DataProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callUpdateDataAsset() {
      // Construct request
      const request = {
        dataAsset,
      };
    
      // Run request
      const [operation] = await dataplexClient.updateDataAsset(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callUpdateDataAsset();

### Python

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_update_data_asset():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataProductServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_product_service.DataProductServiceClient.html)()
    
        # Initialize request argument(s)
        data_asset = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataAsset](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DataAsset.html)()
        data_asset.resource = "resource_value"
    
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[UpdateDataAssetRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.UpdateDataAssetRequest.html)(
            data_asset=data_asset,
        )
    
        # Make the request
        operation = client.[update_data_asset](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_product_service.DataProductServiceClient.html#google_cloud_dataplex_v1_services_data_product_service_DataProductServiceClient_update_data_asset)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### REST

To configure permissions for the assets in the data product, use the [`dataAssets.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts.dataAssets/patch) method.

For example, send the following `PATCH` request:
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{"access_group_configs": ACCESS_GROUP_CONFIGS_MAP}' \
    https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/dataProducts/DATA_PRODUCT_ID/dataAssets/DATA_ASSET_ID?update_mask="access_group_configs"
    

Replace the following:

  * ACCESS_GROUP_CONFIGS_MAP: a JSON object representing a map where each key is an access group ID and the value is an [AccessGroupConfig](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts.dataAssets#accessgroupconfig) object. For example:
        
        {
        "analyst": {
          iam_roles: ["roles/bigquery.dataViewer"]
          }
        }
        

  * PROJECT_ID: the ID of your Google Cloud project

  * LOCATION: the region where the data product exists

  * DATA_PRODUCT_ID: the ID of your data product

  * DATA_ASSET_ID: the ID of the asset for which you want to configure permissions




### Optional: Add contract and aspect details

You can add contracts and aspects for a data product.

#### Add a contract

To establish a foundation of trust between data producers and consumers, you can attach a [contract](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview#contract) to your data product. By specifying parameters such as refresh time and thresholds, you provide consumers with the necessary context to understand when the data is updated and whether it meets their specific business requirements.

###  Console 

  1. In the **Add contract and aspect details** pane, click **Add contract**.

  2. In the **Select contract** field, select `Refresh cadence`.

  3. In the **Frequency** field, select an agreed-upon schedule for how often data is updated or delivered, ensuring a predictable flow from data producer to data consumer. For example, `Weekly`.

  4. In the **Refresh time** field, enter a maximum acceptable time when data is updated at its source and when it becomes available to the consumer. For example, `23:00 PST`.

  5. In the **Threshold (in minutes)** field, enter a measurable limit in minutes for the acceptable delay in data delivery. For example, enter `30` to set a threshold of 30 minutes.

  6. Optional: In the **Cron schedule** field, enter a cron expression that defines the schedule for data generation and delivery in the format: `MINUTE HOUR DAY_OF_MONTH MONTH DAY_OF_WEEK`

The following are the accepted values:

     * MINUTE: `0`-`59`
     * HOUR: `0`-`23`
     * DAY_OF_MONTH: `1`-`31`
     * MONTH: `1-31` or `JAN-DEC`
     * DAY_OF_WEEK: `0-6` or `SUN-SAT`

For example, `0 8 * * 1-5` runs at 8:00 AM on weekdays (Monday-Friday).

  7. Click **Save**.




###  REST 

Contracts are modeled as [aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspects) on the data product. To add a `Refresh Cadence` contract for a data product, use the [`entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

For example, send the following `PATCH` request:
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d \
    '{
      "aspects": {
        "dataplex-types.global.refresh-cadence": {
          "aspectType": "projects/dataplex-types/locations/global/aspectTypes/refresh-cadence",
          "data": {
            "frequency": "REFRESH_FREQUENCY"
          }
        }
      }
    }' \
    "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entryGroups/@dataplex/entries/projects/DATA_PRODUCT_PROJECT_NUMBER/locations/DATA_PRODUCT_LOCATION/dataProducts/DATA_PRODUCT_ID?updateMask=aspects"
    

Replace the following:

  * REFRESH_FREQUENCY: the agreed-upon schedule for how often data is updated or delivered, ensuring a predictable flow from data producer to data consumer. For example: `Weekly`
  * PROJECT_ID: the ID of your Google Cloud project where the API call is being made
  * LOCATION: the region of the Knowledge Catalog service endpoint you are calling (for example, `us-central1`)
  * DATA_PRODUCT_PROJECT_NUMBER: the project number where the data product resource is located
  * DATA_PRODUCT_LOCATION: the location of the data product resource
  * DATA_PRODUCT_ID: the ID of your data product

**Note:** The project number is a unique, automatically generated numeric identifier that is different from your Project ID. For more information on how to find or retrieve your project number, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

###  Terraform 

Contracts are modeled as [aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspects) on the data product. To manage a contract, you must manage the underlying Knowledge Catalog entry. Because Terraform doesn't automatically discover existing aspects, you must first import the [`google_dataplex_entry`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry).

To import the entry, use the following command:
    
    
    terraform import google_dataplex_entry.data_product_metadata "projects/DATA_PRODUCT_PROJECT_NUMBER/locations/LOCATION/entryGroups/@dataplex/entries/projects/DATA_PRODUCT_PROJECT_NUMBER/locations/LOCATION/dataProducts/DATA_PRODUCT_ID"
    

Terraform configuration:
    
    
    resource "google_dataplex_entry" "data_product_metadata" {
    project        = "DATA_PRODUCT_PROJECT_NUMBER"
    location       = "LOCATION"
    entry_group_id = "@dataplex"
    entry_id       = "projects/DATA_PRODUCT_PROJECT_NUMBER/locations/LOCATION/dataProducts/DATA_PRODUCT_ID"
    entry_type     = "projects/655216118709/locations/global/entryTypes/data-product"
    
    aspects {
      aspect_key = "655216118709.global.refresh-cadence"
      aspect {
        data = jsonencode({
          frequency = "REFRESH_FREQUENCY"
        })
      }
    }
    }
    

Replace the following:

  * DATA_PRODUCT_PROJECT_NUMBER: the project number where the data product resource is located
  * LOCATION: the region of the Knowledge Catalog service endpoint you are calling (for example, `us-central1`)
  * DATA_PRODUCT_ID: the ID of your data product
  * REFRESH_FREQUENCY: the agreed-upon schedule for how often data is updated or delivered, ensuring a predictable flow from data producer to data consumer. For example: `Weekly`



For general information on the import process, refer to the [Terraform import documentation](https://developer.hashicorp.com/terraform/cli/import).

#### Add aspects

Use [aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspects) to enrich your data product with structured, reusable metadata. These templates provide a standardized way for data producers to communicate the quality and fitness of a data product, improving governance and helping consumers determine if the product meets their business needs.

To add aspects for the data product, follow these steps:

###  Console 

  1. In the **Add contract and aspect details** pane, click **\+ Add aspect**.

  2. In the **Select aspect type** field, search for and select an aspect type from the list. For example, `Geo context`.

  3. Click **Save**.




###  REST 

To add aspects for a data product, use the [`entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

For example, send the following `PATCH` request:
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d \
    '{
      "aspects": {
        "ASPECT_PROJECT_ID.ASPECT_LOCATION.ASPECT_NAME": {
          "aspectType": "projects/ASPECT_PROJECT_ID/locations/ASPECT_LOCATION/aspectTypes/ASPECT_NAME",
          "data": {}
        }
      }
    }' \
    "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entryGroups/@dataplex/entries/projects/DATA_PRODUCT_PROJECT_NUMBER/locations/DATA_PRODUCT_LOCATION/dataProducts/DATA_PRODUCT_ID?updateMask=aspects"
    

Replace the following:

  * ASPECT_PROJECT_ID: the ID of your Google Cloud project where the aspect is created
  * ASPECT_LOCATION: the region of the Knowledge Catalog service endpoint where the aspect is created (for example, `us-central1`)
  * ASPECT_NAME: the name of the aspect you want to attach to the data product
  * PROJECT_ID: the ID of your Google Cloud project where the API call is being made
  * LOCATION: the region of the Knowledge Catalog service endpoint you are calling (for example, `us-central1`)
  * DATA_PRODUCT_PROJECT_NUMBER: the project number where the data product resource is located
  * DATA_PRODUCT_LOCATION: the location of the data product resource
  * DATA_PRODUCT_ID: the ID of your data product



###  Terraform 

To manage aspects, you must manage the underlying Knowledge Catalog entry. Because Terraform doesn't automatically discover existing aspects, you must first import the [`google_dataplex_entry`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry).

To import the entry, use the following command:
    
    
    terraform import google_dataplex_entry.data_product_metadata "projects/DATA_PRODUCT_PROJECT_NUMBER/locations/LOCATION/entryGroups/@dataplex/entries/projects/DATA_PRODUCT_PROJECT_NUMBER/locations/LOCATION/dataProducts/DATA_PRODUCT_ID"
    

Terraform configuration:
    
    
    resource "google_dataplex_entry" "data_product_metadata" {
    project        = "DATA_PRODUCT_PROJECT_NUMBER"
    location       = "LOCATION"
    entry_group_id = "@dataplex"
    entry_id       = "projects/DATA_PRODUCT_PROJECT_NUMBER/locations/LOCATION/dataProducts/DATA_PRODUCT_ID"
    entry_type     = "projects/655216118709/locations/global/entryTypes/data-product"
    
    aspects {
      aspect_key = "ASPECT_PROJECT_NUMBER.ASPECT_LOCATION.ASPECT_NAME"
      aspect {
        data = {}
      }
    }
    }
    

Replace the following:

  * DATA_PRODUCT_PROJECT_NUMBER: the project number where the data product resource is located
  * LOCATION: the region of the Knowledge Catalog service endpoint you are calling (for example, `us-central1`)
  * DATA_PRODUCT_ID: the ID of your data product
  * ASPECT_PROJECT_NUMBER: the Google Cloud project number where the aspect is created
  * ASPECT_LOCATION: the region of the Knowledge Catalog service endpoint where the aspect is created (for example, `us-central1`)
  * ASPECT_NAME: the name of the aspect you want to attach to the data product



For general information on the import process, refer to the [Terraform import documentation](https://developer.hashicorp.com/terraform/cli/import).

### Optional: Add additional details

You can add documentation and sample queries for your data product to provide essential context, business logic descriptions, and user guides. In Knowledge Catalog, documentation is managed through the `overview` system aspect.

You can manually create this documentation or use [Knowledge Catalog data insights](https://docs.cloud.google.com/knowledge-catalog/docs/data-insights-structured-data) to automatically generate it.

#### Manually add documentation and sample queries

###  Console 

To add documentation for your data product, follow these steps:

  1. In the **Add additional details** pane, click edit **Edit** next to **Documentation**.

  2. Type in the content in the rich-text editor.

  3. Click **Save**.




To add sample queries for your data product, follow these steps:

  1. In the **Add additional details** pane, click edit **Add queries** in the **Query recommendation** section.

  2. Type the sample queries.

  3. Click **Save**.




The newly created data product appears on the Knowledge Catalog **Data products** page.

###  REST 

Documentation is modeled as [aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspects) on the data product. To add documentation, use the [`entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

For example, send the following `PATCH` request:
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d \
    '{
      "aspects": {
        "dataplex-types.global.overview": {
          "aspectType": "projects/dataplex-types/locations/global/aspectTypes/overview",
          "data": {
            "content": "DOCUMENTATION"
          }
        }
      }
    }' \
    "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/entryGroups/@dataplex/entries/projects/DATA_PRODUCT_PROJECT_NUMBER/locations/DATA_PRODUCT_LOCATION/dataProducts/DATA_PRODUCT_ID?updateMask=aspects"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project where the API call is being made
  * LOCATION: the region of the Knowledge Catalog service endpoint you are calling (for example, `us-central1`)
  * DATA_PRODUCT_PROJECT_NUMBER: the project number where the data product resource is located
  * DATA_PRODUCT_LOCATION: the location of the data product resource
  * DATA_PRODUCT_ID: the ID of your data product
  * DOCUMENTATION: the content that you want to attach to the data product



###  Terraform 

Documentation is modeled as [aspects](https://docs.cloud.google.com/knowledge-catalog/docs/enrich-entries-metadata#aspects) on the data product. To manage documentation, you must manage the underlying Knowledge Catalog entry. Because Terraform doesn't automatically discover existing aspects, you must first import the [`google_dataplex_entry`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry).

To import the entry, use the following command:
    
    
    terraform import google_dataplex_entry.data_product_metadata "projects/DATA_PRODUCT_PROJECT_NUMBER/locations/LOCATION/entryGroups/@dataplex/entries/projects/DATA_PRODUCT_PROJECT_NUMBER/locations/LOCATION/dataProducts/DATA_PRODUCT_ID"
    

Terraform configuration:
    
    
    resource "google_dataplex_entry" "data_product_metadata" {
    project        = "DATA_PRODUCT_PROJECT_NUMBER"
    location       = "LOCATION"
    entry_group_id = "@dataplex"
    entry_id       = "projects/DATA_PRODUCT_PROJECT_NUMBER/locations/LOCATION/dataProducts/DATA_PRODUCT_ID"
    entry_type     = "projects/655216118709/locations/global/entryTypes/data-product"
    
    aspects {
      aspect_key = "655216118709.global.overview"
      aspect {
        data = jsonencode({
          content = "DOCUMENTATION"
        })
      }
    }
    }
    

Replace the following:

  * DATA_PRODUCT_PROJECT_NUMBER: the project number where the data product resource is located
  * LOCATION: the region of the Knowledge Catalog service endpoint you are calling (for example, `us-central1`)
  * DATA_PRODUCT_ID: the ID of your data product
  * DOCUMENTATION: the content that you want to attach to the data product



For general information on the import process, refer to the [Terraform import documentation](https://developer.hashicorp.com/terraform/cli/import).

#### Generate automated documentation and sample queries using data insights

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Before you generate documentation and sample queries using Gemini, complete the following prerequisites:

  1. Enable the Gemini for Google Cloud API in the project where you create the data product.

  2. Grant insight-specific user roles: Ask your administrator to grant your identity the following roles and permissions on the data product project:

     * Generate and manage data insights: Dataplex DataScan Editor (`roles/dataplex.dataScanEditor`) or Dataplex DataScan Administrator (`roles/dataplex.dataScanAdmin`) on the project where data product resides 
     * View generated insights: Dataplex DataScan DataViewer (`roles/dataplex.dataScanDataViewer`) on the project where data product resides
  3. Configure cross-project service agent permissions. If your underlying data assets reside in a Google Cloud project different from your data product project, you must grant the Knowledge Catalog service agent (P4SA) access to those assets:

     1. To generate or retrieve the service agent identifier for your data product project, run the following Google Cloud CLI command:
            
            gcloud beta services identity create --service=dataplex.googleapis.com --project=DATA_PRODUCT_PROJECT_ID
            

Replace DATA_PRODUCT_PROJECT_ID with the Google Cloud project ID where your data product resides.

     2. In each external project where your assets reside, grant the data product project's service agent the following roles:

        * BigQuery Data Editor (`roles/bigquery.dataEditor`) on the underlying tables and datasets

        * BigQuery Studio Admin (`roles/bigquery.studioAdmin`) on the asset project




To generate documentation and sample queries for your data product using data insights, follow these steps:

  1. In the **Add additional details** pane, on the **Generate insights with Gemini** bar, and click **Generate**.

Wait for a few minutes for the insight generation process to complete.

  2. To review the generated content, click **View**.

  3. Evaluate the generated content:

     * If the content is accurate, click **Save**. This populates the rich-text editor with a predefined documentation template and adds sample queries to the **Insights** section.

     * If the content doesn't meet expectations, click **Discard**.

  4. Click **Save** to finalize.




## What's next

  * Learn more about [managing data products](https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-products).
  * Learn how to [search for data products](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products#search).
  * As a data consumer, learn how to [request access to data products](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products#request-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
