---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-products/
title: Manage data products \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:51.535926+00:00
---

# Manage data products  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-products/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage data products Stay organized with collections  Save and categorize content based on your preferences. 

Knowledge Catalog (formerly Dataplex Universal Catalog) lets you update, grant access to, and delete existing data products. You can keep assets, metadata, and contracts current so data consumers can find and use trusted data.

This document is intended for data product owners. For more information about the architecture and key concepts of data products, see [About data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview).

## Before you begin

  1. Enable the Knowledge Catalog, BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com,bigquery.googleapis.com)


**Note:** This guide assumes you have existing data products to manage. For more information about creating and configuring data products, see [Create data products](https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products).

### Required roles

To get the permissions that you need to manage data products, ask your administrator to grant you the following IAM roles on the project: 

  * Full permissions to create, update, delete, and manage permissions for data products: [**Dataplex Data Products Admin** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`) 
  * Update and manage existing data products: [**Dataplex Data Products Editor** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`) 
  * Add aspects such as `schema`, `overview`, and `contacts`: [**Dataplex Entry and EntryLink Owner** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.entryOwner) (`roles/dataplex.entryOwner`) 
  * Search for and add assets: [**Dataplex Catalog Viewer** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) 
  * Edit system aspect types such as documentation and contract aspect of refresh cadence: [**Dataplex Catalog Editor** ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogEditor) (`roles/dataplex.catalogEditor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage data products. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage data products:

  * Edit the `overview` system aspect type: `dataplex.entryGroups.useOverviewAspect`
  * Edit the `refresh cadence` system aspect type: `dataplex.entryGroups.useRefreshCadenceAspect`
  * Approve access request for a data product: `dataplex.dataProducts.approve`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Access control for BigQuery models

Access to BigQuery models within a data product is managed through [IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) applied to the parent dataset's IAM policy.

If you delete and then recreate a BigQuery model using the same name, Knowledge Catalog restores the permissions previously granted to Google Groups or service accounts through the data product.

## Set permissions to make data product discoverable

To enable potential consumers to search for, view, and request access to a data product, data product owners must ensure the product is discoverable by granting the appropriate IAM roles on the data product resource:

  * Search for, view, and request access to data products: **Dataplex Data Products Consumer** (`roles/dataplex.dataProductsConsumer`)

  * View data product definitions and metadata (read-only access): **Dataplex Data Products Viewer** (`roles/dataplex.dataProductsViewer`)




## Manage data product access requests

When a data product consumer requests access, the data product owner receives an email notification. Owners can review, approve, or reject these requests using either the Google Cloud console or the API.

###  Console 

### Review access requests for a specific data product

  1. In the Google Cloud console, go to the Knowledge Catalog **Data products** page.

[Go to Data products](https://console.cloud.google.com/dataplex/govern/data-products)

  2. Click the data product for which you want to review access requests.

  3. Click the **Access request management** tab.

  4. Select the requester whose request you want to review.

  5. Click more_vert **Actions** and then click **Approve** or **Reject**.

  6. Click **Save**.




### Review access requests across multiple data products

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance workflows** page.

[Go to Governance workflows](https://console.cloud.google.com/dataplex/governance-workflows)

  2. Click the **Pending Approvals** tab.

  3. Optional: Filter the list by the specific data product name to isolate its requests.

  4. Select the target request and click **Approve** or **Reject**.

  5. Click **Save**.




### Post-approval behavior

  * User requests: Consumers who requested access for their user identity are automatically added as members to the Google Group mapped to the access group.

  * Service account requests: Consumers who requested access for a service account are granted permissions to impersonate the data producer service account mapped to the access group.




Once processed, the request status updates automatically and the entry moves to the **Approval log** tab.

###  REST 

### List all pending access requests

To list all access requests that are pending your review within a specific project and location, send a `GET` request using the custom collection method `:listReviewable`:
    
    
    curl -X GET \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests:listReviewable"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project

  * LOCATION: the region where the data product exists (for example, `us-central1`)




### Approve an access request

Data product owners with the `dataplex.dataProducts.approve` permission can approve a pending request by sending a `POST` request to the custom method `:approve`:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID:approve"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project

  * LOCATION: the region where the data product exists (for example, `us-central1`)

  * CHANGE_REQUEST_ID: the unique ID of your access request you want to approve




Unlike console-driven approvals, approving a change request using the REST API doesn't automatically modify Google Group memberships or configure service account token impersonation. You must complete these downstream access management steps manually:

  * For user identity access requests: Add the data product consumer to the mapped Google Group. For more information, see [Add a membership to a Google Group](https://docs.cloud.google.com/identity/docs/how-to/memberships-google-groups#add_a_membership_to_a_google_group).

  * For service account access requests: Grant the **Service Account Token Creator** (`roles/iam.serviceAccountTokenCreator`) IAM role to the data product consumer's service account on the resource by running the following command:
        
        gcloud iam service-accounts add-iam-policy-binding PRODUCER_SERVICE_ACCOUNT \
          --member="serviceAccount:CONSUMER_SERVICE_ACCOUNT" \
          --role="roles/iam.serviceAccountTokenCreator"
        

Replace the following:

    * PRODUCER_SERVICE_ACCOUNT: the fully qualified email address of the service account mapped to the data product's access group

    * CONSUMER_SERVICE_ACCOUNT: the fully qualified email address of the service account belonging to the consumer requesting access




### Reject an access request

Data product owners with the `dataplex.dataProducts.approve` permission can reject a pending request by sending a `POST` request to the custom method `:reject` along with a justification payload:
    
    
    curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{
      "comment": "REJECTION_REASON"
    }' \
    "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID:reject"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project

  * LOCATION: the region where the data product exists (for example, `us-central1`)

  * CHANGE_REQUEST_ID: the unique ID of your access request you want to reject




## Update a data product

You can update the basic details (for example, data product name, description, owner details), assets, access groups, permissions, contract, aspects, and additional documentation for an existing data product.

**Note:** The REST API methods for updating data products and assets are long-running operations. When you call these methods, the API returns an [Operation](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.operations) object that you can use to check the status of the task.

### Update the basic details of a data product

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Data products** page.

[Go to Data products](https://console.cloud.google.com/dataplex/govern/data-products)

  2. Click the data product that you want to update.

  3. Click **Edit**.

  4. Update the **Data product name** , **Data product icon** , **Description** , **Data product owner(s) email address** , **Data product approver(s) email address** , and **Labels** as required.

  5. Click **Save**.




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

To update the basic details of a data product, use the [`dataProducts.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts/patch) method.

For example, to update the description of a data product, send the following `PATCH` request:
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    -d '{"description": "NEW_DESCRIPTION"}' \
    https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/dataProducts/DATA_PRODUCT_ID?update_mask="description"
    

Replace the following:

  * NEW_DESCRIPTION: a new description for the data product
  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the region where the data product exists
  * DATA_PRODUCT_ID: the ID of your data product



### Update assets of a data product

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Data products** page.

[Go to Data products](https://console.cloud.google.com/dataplex/govern/data-products)

  2. Click the data product for which you want to update assets.

  3. Click the **Assets** tab.

  4. To add a new asset, follow these steps:

     1. Click **+Add**.

     2. Search for and select the assets that you want to add to your data product. The assets you select must reside in the same region as the data product.

If you have necessary permissions, you can view the metadata of assets by clicking the asset.

     3. To refine the search results, use **Filters**.

     4. After you select the assets, click **Add**.

  5. To remove an asset from the data product, follow these steps:

     1. For the asset that you want to remove, click more_vert **> Remove**.

     2. To confirm the action, click **Remove**.

**Note:** You can remove up to 10 assets at a time.



### C#

#### Add a new data asset to a data product

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // Generated code. DO NOT EDIT!
    
    namespace GoogleCSharpSnippets
    {
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
    }
    

#### Delete a data asset from a data product

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // Generated code. DO NOT EDIT!
    
    namespace GoogleCSharpSnippets
    {
        using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
        using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
        using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
        public sealed partial class GeneratedDataProductServiceClientSnippets
        {
            /// <summary>Snippet for DeleteDataAsset</summary>
            /// <remarks>
            /// This snippet has been automatically generated and should be regarded as a code template only.
            /// It will require modifications to work:
            /// - It may require correct/in-range values for request initialization.
            /// - It may require specifying regional endpoints when creating the service client as shown in
            ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
            /// </remarks>
            public void DeleteDataAssetRequestObject()
            {
                // Create client
                [DataProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html) dataProductServiceClient = [DataProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_Create)();
                // Initialize request argument(s)
                [DeleteDataAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteDataAssetRequest.html) request = new [DeleteDataAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteDataAssetRequest.html)
                {
                    DataAssetName = [DataAssetName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataAssetName.html).[FromProjectLocationDataProductDataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataAssetName.html#Google_Cloud_Dataplex_V1_DataAssetName_FromProjectLocationDataProductDataAsset_System_String_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]", "[DATA_ASSET]"),
                    Etag = "",
                    ValidateOnly = false,
                };
                // Make the request
                Operation<Empty, OperationMetadata> response = dataProductServiceClient.[DeleteDataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_DeleteDataAsset_Google_Cloud_Dataplex_V1_DataAssetName_Google_Api_Gax_Grpc_CallSettings_)(request);
    
                // Poll until the returned long-running operation is complete
                Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
                // Retrieve the operation result
                [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) result = completedResponse.Result;
    
                // Or get the name of the operation
                string operationName = response.Name;
                // This name can be stored, then the long-running operation retrieved later by name
                Operation<Empty, OperationMetadata> retrievedResponse = dataProductServiceClient.[PollOnceDeleteDataAsset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_PollOnceDeleteDataAsset_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
                // Check if the retrieved long-running operation has completed
                if (retrievedResponse.IsCompleted)
                {
                    // If it has completed, then access the result
                    [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) retrievedResult = retrievedResponse.Result;
                }
            }
        }
    }
    

### Go

#### Add a new data asset to a data product

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // Code generated by protoc-gen-go_gapic. DO NOT EDIT.
    
    
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
    
    

#### Delete a data asset from a data product

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // Code generated by protoc-gen-go_gapic. DO NOT EDIT.
    
    
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
    
    	req := &dataplexpb.DeleteDataAssetRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#DeleteDataAssetRequest.
    	}
    	op, err := c.DeleteDataAsset(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    
    

### Java

#### Add a new data asset to a data product

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /*
     * Copyright 2026 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *      https://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    package com.google.cloud.dataplex.v1.samples;
    
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
    

#### Delete a data asset from a data product

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /*
     * Copyright 2026 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *      https://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    package com.google.cloud.dataplex.v1.samples;
    
    import com.google.cloud.dataplex.v1.[DataAssetName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAssetName.html);
    import com.google.cloud.dataplex.v1.[DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html);
    import com.google.cloud.dataplex.v1.[DeleteDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataAssetRequest.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    
    public class SyncDeleteDataAsset {
    
      public static void main(String[] args) throws Exception {
        syncDeleteDataAsset();
      }
    
      public static void syncDeleteDataAsset() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html) dataProductServiceClient = [DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html).create()) {
          [DeleteDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataAssetRequest.html) request =
              [DeleteDataAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataAssetRequest.html).newBuilder()
                  .setName(
                      [DataAssetName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataAssetName.html).of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]", "[DATA_ASSET]")
                          .toString())
                  .setEtag("etag3123477")
                  .setValidateOnly(true)
                  .build();
          dataProductServiceClient.[deleteDataAssetAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html#com_google_cloud_dataplex_v1_DataProductServiceClient_deleteDataAssetAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_DataAssetName_)(request).get();
        }
      }
    }
    

### Node.js

#### Add a new data asset to a data product

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    //
    // ** This file is automatically generated by gapic-generator-typescript. **
    // ** https://github.com/googleapis/gapic-generator-typescript **
    // ** All changes to this file may be overwritten. **
    
    
    
    'use strict';
    
    function main(parent, dataAsset) {
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
    }
    
    process.on('unhandledRejection', err => {
      console.error(err.message);
      process.exitCode = 1;
    });
    main(...process.argv.slice(2));
    

#### Delete a data asset from a data product

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    //
    // ** This file is automatically generated by gapic-generator-typescript. **
    // ** https://github.com/googleapis/gapic-generator-typescript **
    // ** All changes to this file may be overwritten. **
    
    
    
    'use strict';
    
    function main(name) {
      /**
       * This snippet has been automatically generated and should be regarded as a code template only.
       * It will require modifications to work.
       * It may require correct/in-range values for request initialization.
       * TODO(developer): Uncomment these variables before running the sample.
       */
      /**
       *  Required. The name of the data asset to delete.
       *  Format:
       *  projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}/dataAssets/{data_asset_id}
       */
      // const name = 'abc123'
      /**
       *  Optional. The etag of the data asset.
       *  If this is provided, it must match the server's etag.
       *  If the etag is provided and does not match the server-computed etag,
       *  the request must fail with a ABORTED error code.
       */
      // const etag = 'abc123'
      /**
       *  Optional. Validates the request without actually deleting the data asset.
       *  Defaults to false.
       */
      // const validateOnly = true
    
      // Imports the Dataplex library
      const {DataProductServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
      // Instantiates a client
      const dataplexClient = new [DataProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
      async function callDeleteDataAsset() {
        // Construct request
        const request = {
          name,
        };
    
        // Run request
        const [operation] = await dataplexClient.deleteDataAsset(request);
        const [response] = await operation.promise();
        console.log(response);
      }
    
      callDeleteDataAsset();
    }
    
    process.on('unhandledRejection', err => {
      console.error(err.message);
      process.exitCode = 1;
    });
    main(...process.argv.slice(2));
    

### Python

#### Add a new data asset to a data product

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # -*- coding: utf-8 -*-
    # Copyright 2026 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    #
    # Generated code. DO NOT EDIT!
    #
    # Snippet for CreateDataAsset
    # NOTE: This snippet has been automatically generated for illustrative purposes only.
    # It may require modifications to work in your environment.
    
    # To install the latest published package dependency, execute the following:
    #   python3 -m pip install google-cloud-dataplex
    
    
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
    
    
    

#### Delete a data asset from a data product

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # -*- coding: utf-8 -*-
    # Copyright 2026 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    #
    # Generated code. DO NOT EDIT!
    #
    # Snippet for DeleteDataAsset
    # NOTE: This snippet has been automatically generated for illustrative purposes only.
    # It may require modifications to work in your environment.
    
    # To install the latest published package dependency, execute the following:
    #   python3 -m pip install google-cloud-dataplex
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest)
    
    
    def sample_delete_data_asset():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataProductServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_product_service.DataProductServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DeleteDataAssetRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DeleteDataAssetRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_data_asset](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_product_service.DataProductServiceClient.html#google_cloud_dataplex_v1_services_data_product_service_DataProductServiceClient_delete_data_asset)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    
    

### REST

To add a new data asset to the data product, use the [`dataAssets.create`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts.dataAssets/create) method. For a code example, see [Optional: Add assets](https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products#add-assets).

To delete a data asset from the data product, use the [`dataAssets.delete`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts.dataAssets/delete) method. For example, send the following `DELETE` request:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/dataProducts/DATA_PRODUCT_ID/dataAssets/DATA_ASSET_ID"
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the region in which you want to create the data product
  * DATA_PRODUCT_ID: a unique ID for your data product
  * DATA_ASSET_ID: the ID of the data asset you want to remove from the data product



### Update access groups and asset permissions

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Data products** page.

[Go to Data products](https://console.cloud.google.com/dataplex/govern/data-products)

  2. Click the data product for which you want to update the access groups and permissions.

  3. Click the **Access groups & permissions** tab.

  4. To update an access group, follow these steps:

     1. Click edit **Edit**.

     2. Update the access group name, description, identifier, and **Default role** as required.

**Note:** Adding a **Default role** after IAM roles have already been assigned directly to assets doesn't override those asset-specific permissions. If you remove or clear the **Default role** for an access group, default role permissions are revoked from all assets that rely on it.
     3. To add a new access group, click **Add access group** and follow these steps:

        1. In the **Access group name** field, enter a name for the new access group. For example, `Analyst`.

        2. In the **Access group description** field, enter a description for the access group.

        3. In the **Access group identifier** field, enter the email address of a Google Group or service account or both that you want to assign to this access group:

           * Google Group: Data product consumers who request access for themselves are added as members to the mapped Google Group.

           * Service account: Data product consumers who request access for their service accounts are granted the **Service Account Token Creator** (`roles/iam.serviceAccountTokenCreator`) IAM role to impersonate the data producer service account mapped to the access group.

**Note:** You can add a maximum of three access groups per data product.
        4. Optional: In the **Default role** field, select a default IAM role to automatically grant across all supported assets in the data product. If IAM roles are already assigned directly to specific assets, adding a default role doesn't override those direct permissions.

     4. Click **Add**.

  5. To remove an access group, follow these steps:

     1. For the access group that you want to remove, click more_vert **> Remove**.

     2. To confirm the action, click **Remove**. Removing an access group revokes its default role and any asset-specific permissions from all assets in the data product.

  6. If no access groups are configured for the selected data product, you can add a new access group by clicking **Add access group**.

  7. To update asset permissions, follow these steps:

     1. For the asset you want to update permissions, click more_vert > **Permissions**.

     2. Update the required access groups and IAM roles. You can assign asset-specific roles to override an access group's default role.

     3. Click **Configure**. The **Permissions** column in the assets table displays the updated permissions and their configuration state:

        * **Applied** : The IAM role (default or asset-specific) is active on the underlying resource.
        * **Failed** : Applying the IAM role to the underlying resource failed. You can find the detailed failure reason in Cloud Logging.
        * **Unsupported** : Applying permissions isn't supported for this asset's resource type.



### C#

#### Update access groups

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // Generated code. DO NOT EDIT!
    
    namespace GoogleCSharpSnippets
    {
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
    }
    

#### Update asset permissions

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // Generated code. DO NOT EDIT!
    
    namespace GoogleCSharpSnippets
    {
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
    }
    

### Go

#### Update access groups

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // Code generated by protoc-gen-go_gapic. DO NOT EDIT.
    
    
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
    
    

#### Update asset permissions

### Go

Before trying this sample, follow the Go setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/dataplex). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    
    // Code generated by protoc-gen-go_gapic. DO NOT EDIT.
    
    
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

#### Update access groups

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /*
     * Copyright 2026 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *      https://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    package com.google.cloud.dataplex.v1.samples;
    
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
    

#### Update asset permissions

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /*
     * Copyright 2026 Google LLC
     *
     * Licensed under the Apache License, Version 2.0 (the "License");
     * you may not use this file except in compliance with the License.
     * You may obtain a copy of the License at
     *
     *      https://www.apache.org/licenses/LICENSE-2.0
     *
     * Unless required by applicable law or agreed to in writing, software
     * distributed under the License is distributed on an "AS IS" BASIS,
     * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
     * See the License for the specific language governing permissions and
     * limitations under the License.
     */
    
    package com.google.cloud.dataplex.v1.samples;
    
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

#### Update access groups

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    //
    // ** This file is automatically generated by gapic-generator-typescript. **
    // ** https://github.com/googleapis/gapic-generator-typescript **
    // ** All changes to this file may be overwritten. **
    
    
    
    'use strict';
    
    function main(dataProduct) {
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
    }
    
    process.on('unhandledRejection', err => {
      console.error(err.message);
      process.exitCode = 1;
    });
    main(...process.argv.slice(2));
    

#### Update asset permissions

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Copyright 2026 Google LLC
    //
    // Licensed under the Apache License, Version 2.0 (the "License");
    // you may not use this file except in compliance with the License.
    // You may obtain a copy of the License at
    //
    //     https://www.apache.org/licenses/LICENSE-2.0
    //
    // Unless required by applicable law or agreed to in writing, software
    // distributed under the License is distributed on an "AS IS" BASIS,
    // WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    // See the License for the specific language governing permissions and
    // limitations under the License.
    //
    // ** This file is automatically generated by gapic-generator-typescript. **
    // ** https://github.com/googleapis/gapic-generator-typescript **
    // ** All changes to this file may be overwritten. **
    
    
    
    'use strict';
    
    function main(dataAsset) {
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
    }
    
    process.on('unhandledRejection', err => {
      console.error(err.message);
      process.exitCode = 1;
    });
    main(...process.argv.slice(2));
    

### Python

#### Update access groups

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # -*- coding: utf-8 -*-
    # Copyright 2026 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    #
    # Generated code. DO NOT EDIT!
    #
    # Snippet for UpdateDataProduct
    # NOTE: This snippet has been automatically generated for illustrative purposes only.
    # It may require modifications to work in your environment.
    
    # To install the latest published package dependency, execute the following:
    #   python3 -m pip install google-cloud-dataplex
    
    
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
    
    
    

#### Update asset permissions

### Python

Before trying this sample, follow the Python setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/dataplex/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # -*- coding: utf-8 -*-
    # Copyright 2026 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    #
    # Generated code. DO NOT EDIT!
    #
    # Snippet for UpdateDataAsset
    # NOTE: This snippet has been automatically generated for illustrative purposes only.
    # It may require modifications to work in your environment.
    
    # To install the latest published package dependency, execute the following:
    #   python3 -m pip install google-cloud-dataplex
    
    
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

To update the access groups associated with a data product, use the [`dataProducts.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts/patch) method. For a code example, see [Configure access groups](https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products#configure-access-groups).

To update the asset permissions, use the [`dataAssets.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts.dataAssets/patch) method. For a code example, see [Configure asset permissions](https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products#configure-asset-permissions).

### Update the data product contract

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Data products** page.

[Go to Data products](https://console.cloud.google.com/dataplex/govern/data-products)

  2. Click the data product for which you want to update the contract.

  3. Click the **Contract** tab.

  4. To update the existing contract, follow these steps:

     1. Click edit **Edit**.

     2. Update the necessary fields.

     3. Click **Save**.

  5. If no contract is attached to the selected data product, you can add one by clicking **Add contract**.




###  REST 

To update a contract, use the [`entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method. For a code example, see [Add a contract](https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products#add_a_contract).

### Update aspects of a data product

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Data products** page.

[Go to Data products](https://console.cloud.google.com/dataplex/govern/data-products)

  2. Click the data product for which you want to update the aspects.

  3. Click the **Aspects** tab.

  4. To update an aspect, follow these steps:

     1. Click the aspect you want to update.

     2. Click edit **Edit**.

     3. Update the **Aspect type** , **Country** , and **Region** as required.

     4. Click **Save**.

  5. To add a new aspect for the data product, follow these steps:

     1. Click **\+ Add aspect**.

     2. In the **Select aspect type** field, search for and select an aspect type from the list. For example, `Geo context`.

     3. In the **Country** field, select the country to which the asset belongs.

     4. In the **Region** field, select the business region to which the asset belongs.

     5. Click **Save**.

  6. To delete an aspect, follow these steps:

     1. Click the aspect you want to delete.

     2. Click delete **Delete**.

     3. To confirm the action, click **Confirm**.




###  REST 

To update any aspect on the data product entry, use the [`entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

### Update the data product documentation

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Data products** page.

[Go to Data products](https://console.cloud.google.com/dataplex/govern/data-products)

  2. Click the data product for which you want to update the documentation.

  3. Click the **Overview** tab.

  4. Click edit **Edit** against **Documentation**.

  5. Update user guide, sample queries, and other documentation as required.

  6. Click **Save**.




###  REST 

Documentation is part of the `overview` aspect. To update the data product documentation, use the [`entries.patch`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.entryGroups.entries/patch) method.

## Delete a data product

To delete a data product, you must first remove all the assets from the data product.

### Console

  1. In the Google Cloud console, go to the Knowledge Catalog **Data products** page.

[Go to Data products](https://console.cloud.google.com/dataplex/govern/data-products)

  2. Click the data product that you want to delete.

  3. Click the **Assets** tab.

  4. For every asset listed, click more_vert > **Remove**. Confirm the action by clicking **Remove**.

  5. After you remove all the assets, delete the data product by clicking delete **Delete**.

  6. In the confirmation dialog, enter `delete` and click **Delete**.




### C#

### C#

Before trying this sample, follow the C# setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    
    public sealed partial class GeneratedDataProductServiceClientSnippets
    {
        /// <summary>Snippet for DeleteDataProduct</summary>
        /// <remarks>
        /// This snippet has been automatically generated and should be regarded as a code template only.
        /// It will require modifications to work:
        /// - It may require correct/in-range values for request initialization.
        /// - It may require specifying regional endpoints when creating the service client as shown in
        ///   https://cloud.google.com/dotnet/docs/reference/help/client-configuration#endpoint.
        /// </remarks>
        public void DeleteDataProductRequestObject()
        {
            // Create client
            [DataProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html) dataProductServiceClient = [DataProductServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_Create)();
            // Initialize request argument(s)
            [DeleteDataProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteDataProductRequest.html) request = new [DeleteDataProductRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DeleteDataProductRequest.html)
            {
                DataProductName = [DataProductName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductName.html).[FromProjectLocationDataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductName.html#Google_Cloud_Dataplex_V1_DataProductName_FromProjectLocationDataProduct_System_String_System_String_System_String_)("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]"),
                Etag = "",
                ValidateOnly = false,
            };
            // Make the request
            Operation<Empty, OperationMetadata> response = dataProductServiceClient.[DeleteDataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_DeleteDataProduct_Google_Cloud_Dataplex_V1_DataProductName_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete
            Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
            // Retrieve the operation result
            [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) result = completedResponse.Result;
    
            // Or get the name of the operation
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name
            Operation<Empty, OperationMetadata> retrievedResponse = dataProductServiceClient.[PollOnceDeleteDataProduct](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.DataProductServiceClient.html#Google_Cloud_Dataplex_V1_DataProductServiceClient_PollOnceDeleteDataProduct_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result
                [Empty](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html) retrievedResult = retrievedResponse.Result;
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
    
    	req := &dataplexpb.DeleteDataProductRequest{
    		// TODO: Fill request struct fields.
    		// See https://pkg.go.dev/cloud.google.com/go/dataplex/apiv1/dataplexpb#DeleteDataProductRequest.
    	}
    	op, err := c.DeleteDataProduct(ctx, req)
    	if err != nil {
    		// TODO: Handle error.
    	}
    
    	err = op.Wait(ctx)
    	if err != nil {
    		// TODO: Handle error.
    	}
    }
    

### Java

### Java

Before trying this sample, follow the Java setup instructions in the [Knowledge Catalog quickstart using client libraries](https://docs.cloud.google.com/knowledge-catalog/docs/reference/libraries). For more information, see the [Knowledge Catalog Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/overview). 

To authenticate to Knowledge Catalog, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dataplex.v1.[DataProductName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductName.html);
    import com.google.cloud.dataplex.v1.[DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html);
    import com.google.cloud.dataplex.v1.[DeleteDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataProductRequest.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    
    public class SyncDeleteDataProduct {
    
      public static void main(String[] args) throws Exception {
        syncDeleteDataProduct();
      }
    
      public static void syncDeleteDataProduct() throws Exception {
        // This snippet has been automatically generated and should be regarded as a code template only.
        // It will require modifications to work:
        // - It may require correct/in-range values for request initialization.
        // - It may require specifying regional endpoints when creating the service client as shown in
        // https://cloud.google.com/java/docs/setup#configure_endpoints_for_the_client_library
        try ([DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html) dataProductServiceClient = [DataProductServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html).create()) {
          [DeleteDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataProductRequest.html) request =
              [DeleteDataProductRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DeleteDataProductRequest.html).newBuilder()
                  .setName([DataProductName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductName.html).of("[PROJECT]", "[LOCATION]", "[DATA_PRODUCT]").toString())
                  .setEtag("etag3123477")
                  .setValidateOnly(true)
                  .build();
          dataProductServiceClient.[deleteDataProductAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataplex/latest/com.google.cloud.dataplex.v1.DataProductServiceClient.html#com_google_cloud_dataplex_v1_DataProductServiceClient_deleteDataProductAsync__org_jspecify_annotations_Nullable_com_google_cloud_dataplex_v1_DataProductName_)(request).get();
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
     *  Required. The name of the data product to delete.
     *  Format:
     *  projects/{project_id_or_number}/locations/{location_id}/dataProducts/{data_product_id}
     */
    // const name = 'abc123'
    /**
     *  Optional. The etag of the data product.
     *  If an etag is provided and does not match the current etag of the data
     *  product, then the deletion will be blocked and an ABORTED error will be
     *  returned.
     */
    // const etag = 'abc123'
    /**
     *  Optional. Validates the request without actually deleting the data product.
     *  Default: false.
     */
    // const validateOnly = true
    
    // Imports the Dataplex library
    const {DataProductServiceClient} = require('[@google-cloud/dataplex](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)').v1;
    
    // Instantiates a client
    const dataplexClient = new [DataProductServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dataplex/latest/overview.html)();
    
    async function callDeleteDataProduct() {
      // Construct request
      const request = {
        name,
      };
    
      // Run request
      const [operation] = await dataplexClient.deleteDataProduct(request);
      const [response] = await operation.promise();
      console.log(response);
    }
    
    callDeleteDataProduct();

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
    
    
    def sample_delete_data_product():
        # Create a client
        client = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DataProductServiceClient](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_product_service.DataProductServiceClient.html)()
    
        # Initialize request argument(s)
        request = [dataplex_v1](https://docs.cloud.google.com/python/docs/reference/dataplex/latest).[DeleteDataProductRequest](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.types.DeleteDataProductRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_data_product](https://docs.cloud.google.com/python/docs/reference/dataplex/latest/google.cloud.dataplex_v1.services.data_product_service.DataProductServiceClient.html#google_cloud_dataplex_v1_services_data_product_service_DataProductServiceClient_delete_data_product)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    
    

### REST

To delete a data product, use the [`dataProducts.delete`](https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.dataProducts/delete) method.

For example, send the following `DELETE` request:
    
    
    curl -X DELETE \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" \
    https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/dataProducts/DATA_PRODUCT_ID
    

Replace the following:

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the region where the data product exists
  * DATA_PRODUCT_ID: the ID of your data product that you want to delete



## Data retention and project deletion

When you delete a Google Cloud project that contains data products, the associated resources follow the standard Google Cloud deletion lifecycle, also referred to as a wipeout. For a detailed overview of the technical processes and timelines governing this behavior, see [Data deletion on Google Cloud](https://docs.cloud.google.com/docs/security/deletion).

### Resource lifecycle during project deletion

The lifecycle of your data products and data assets is managed in two primary stages following a project deletion request:

  * Soft deletion (`Hidden` state): Immediately upon initiating project deletion, all data products and data assets within the project are marked as `Hidden`. During this 30-day grace period, the metadata is preserved but is no longer accessible through Dataplex APIs or the Google Cloud console. You can restore the project and its resources at any point during this window.

  * Permanent purge (`Purged` state): After the 30-day grace period expires, the project and all its Knowledge Catalog metadata are permanently deleted. Knowledge Catalog utilizes an internal row deletion policy to verifiably purge these records from storage.




### Behavior of IAM policies on cross-project resources

A critical operational distinction exists between Knowledge Catalog metadata and the IAM policies enforced on your underlying physical data (such as BigQuery datasets or Cloud Storage buckets).

While Knowledge Catalog metadata within the project is automatically purged, any IAM bindings applied to data resources located in a different project (Project B) aren't automatically revoked when the data product owner project (Project A) is deleted.

  * Orphaned bindings: Because the physical resources in the target project remain active, the IAM system doesn't automatically remove the principal identifiers associated with the deleted project.

  * Prevent zombie permissions: To ensure complete decommissioning of data access, manually delete data assets from your data products, or explicitly strip the associated IAM bindings from your cross-project resources, before you initiate a project deletion.




### Project restoration (Undelete)

If you restore a deleted project within the 30-day grace period, Knowledge Catalog attempts to restore your resources and their visibility in the catalog. For cross-project assets, because the underlying IAM bindings weren't automatically revoked during the deletion process, data access typically resumes immediately for the restored project.

## What's next

  * Learn more [about data products](https://docs.cloud.google.com/knowledge-catalog/docs/data-products-overview).
  * Learn how to [search for data products](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-products#search).
  * Learn how to [create a data product](https://docs.cloud.google.com/knowledge-catalog/docs/create-data-products).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
