---
url: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-remove-product-from-product-set/
title: Remove a product from a product set \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:43.349196+00:00
---

# Remove a product from a product set  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-remove-product-from-product-set/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)



#  Remove a product from a product set Stay organized with collections  Save and categorize content based on your preferences. 

Remove a product from a product set.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and managing your product resources](https://docs.cloud.google.com/vision/product-search/docs/create-product)



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
    
    // removeProductFromProductSet removes a product from a product set.
    func removeProductFromProductSet(w io.Writer, projectID string, location string, productID string, productSetID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[RemoveProductFromProductSetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_RemoveProductFromProductSetRequest){
    		Name:    fmt.Sprintf("projects/%s/locations/%s/productSets/%s", projectID, location, productSetID),
    		Product: fmt.Sprintf("projects/%s/locations/%s/products/%s", projectID, location, productID),
    	}
    
    	if err = c.RemoveProductFromProductSet(ctx, req); err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product removed from product set.\n")
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Remove a product from a product set.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @param productSetId - Id of the product set.
     * @throws IOException - on I/O errors.
     */
    public static void removeProductFromProductSet(
        String projectId, String computeRegion, String productId, String productSetId)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product set.
        String formattedParent = ProductSetName.format(projectId, computeRegion, productSetId);
    
        // Get the full path of the product.
        String formattedName = ProductName.format(projectId, computeRegion, productId);
    
        // Remove the product from the product set.
        client.removeProductFromProductSet(formattedParent, formattedName);
    
        System.out.println(String.format("Product removed from product set."));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function removeProductFromProductSet() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      const productSetPath = client.productSetPath(
        projectId,
        location,
        productSetId
      );
    
      const productPath = client.productPath(projectId, location, productId);
    
      const request = {
        name: productSetPath,
        product: productPath,
      };
    
      await client.removeProductFromProductSet(request);
      console.log('Product removed from product set.');
    }
    removeProductFromProductSet();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def remove_product_from_product_set(project_id, location, product_id, product_set_id):
        """Remove a product from a product set.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_id: Id of the product.
            product_set_id: Id of the product set.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # Get the full path of the product set.
        product_set_path = client.[product_set_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_set_path)(
            project=project_id, location=location, product_set=product_set_id
        )
    
        # Get the full path of the product.
        product_path = client.[product_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_path)(
            project=project_id, location=location, product=product_id
        )
    
        # Remove the product from the product set.
        client.[remove_product_from_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_remove_product_from_product_set)(name=product_set_path, product=product_path)
        print("Product removed from product set.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvisionproductsearch). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
