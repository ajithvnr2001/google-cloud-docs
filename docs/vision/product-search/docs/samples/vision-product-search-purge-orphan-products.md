---
url: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-purge-orphan-products/
title: Delete orphan products \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:36.912384+00:00
---

# Delete orphan products  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-purge-orphan-products/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)



#  Delete orphan products Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates how to delete a batch of orphaned products.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Deleting resources](https://docs.cloud.google.com/vision/product-search/docs/delete-resources)



## Code sample

### Go

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    )
    
    // purgeOrphanProducts deletes all products not in any product sets.
    func purgeOrphanProducts(w io.Writer, projectID string, location string) error {
    	// projectID := "your-gcp-project-id"
    	// location := "us-west1"
    
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[PurgeProductsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_PurgeProductsRequest){
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		Target: &visionpb.[PurgeProductsRequest_DeleteOrphanProducts](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_PurgeProductsRequest_DeleteOrphanProducts){
    			DeleteOrphanProducts: true,
    		},
    		Force: true,
    	}
    
    	// The purge operation is async.
    	op, err := c.PurgeProducts(ctx, req)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	fmt.Fprintf(w, "Processing operation name: %q\n", op.Name())
    
    	if err := op.Wait(ctx); err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "Orphan products deleted.\n")
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.vision.v1.[BatchOperationMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.BatchOperationMetadata.html);
    import com.google.cloud.vision.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.LocationName.html);
    import com.google.cloud.vision.v1.[ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html);
    import com.google.cloud.vision.v1.[PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.html);
    import com.google.protobuf.[Empty](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Empty.html);
    import java.util.concurrent.TimeUnit;
    
    public class PurgeProducts {
    
      // Delete the product and all its reference images.
      public static void purgeOrphanProducts(String projectId, String computeRegion) throws Exception {
    
        // String projectId = "YOUR_PROJECT_ID";
        // String computeRegion = "us-central1";
        // boolean force = true;
    
        try ([ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html) client = [ProductSearchClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html).create()) {
          String parent = [LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.LocationName.html).format(projectId, computeRegion);
    
          // The purge operation is async.
          [PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.html) request =
              [PurgeProductsRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.html).newBuilder()
                  .[setDeleteOrphanProducts](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.Builder.html#com_google_cloud_vision_v1_PurgeProductsRequest_Builder_setDeleteOrphanProducts_boolean_)(true)
                  // The operation is irreversible and removes multiple products.
                  // The user is required to pass in force=True to actually perform the
                  // purge.
                  // If force is not set to True, the service raises an exception.
                  .[setForce](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.PurgeProductsRequest.Builder.html#com_google_cloud_vision_v1_PurgeProductsRequest_Builder_setForce_boolean_)(true)
                  .setParent(parent)
                  .build();
    
          OperationFuture<Empty, BatchOperationMetadata> response = client.[purgeProductsAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/com.google.cloud.vision.v1.ProductSearchClient.html#com_google_cloud_vision_v1_ProductSearchClient_purgeProductsAsync__org_jspecify_annotations_Nullable_com_google_cloud_vision_v1_LocationName_)(request);
          response.getPollingFuture().get(180, TimeUnit.SECONDS);
    
          System.out.println("Orphan products deleted.");
        }
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function purgeOrphanProducts() {
      // Deletes all products not in any product sets.
    
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
    
      const formattedParent = client.locationPath(projectId, location);
    
      // The operation is irreversible and removes multiple products.
      // The user is required to pass in force=true to actually perform the purge.
      // If force is not set to True, the service raises an error.
      const force = true;
    
      try {
        const [operation] = await client.purgeProducts({
          parent: formattedParent,
          deleteOrphanProducts: true,
          force: force,
        });
        await operation.promise();
        console.log('Orphan products deleted.');
      } catch (err) {
        console.log(err);
      }
    }
    purgeOrphanProducts();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    from google.protobuf import field_mask_pb2 as field_mask
    
    def purge_orphan_products(project_id, location, force):
        """Delete all products not in any product sets.
        Args:
            project_id: Id of the project.
            location: A compute region name.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        parent = f"projects/{project_id}/locations/{location}"
    
        # The purge operation is async.
        operation = client.[purge_products](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_purge_products)(
            request={
                "parent": parent,
                "delete_orphan_products": True,
                # The operation is irreversible and removes multiple products.
                # The user is required to pass in force=True to actually perform the
                # purge.
                # If force is not set to True, the service raises an exception.
                "force": force,
            }
        )
    
        operation.result(timeout=500)
    
        print("Orphan products deleted.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvisionproductsearch). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
