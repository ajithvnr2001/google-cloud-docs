---
url: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-list-products-in-product-set/
title: List products in product set \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:45.612190+00:00
---

# List products in product set  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-list-products-in-product-set/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)



#  List products in product set Stay organized with collections  Save and categorize content based on your preferences. 

List all products in a product set.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Getting and listing resources](https://docs.cloud.google.com/vision/product-search/docs/get-list-resources)



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
    	"google.golang.org/api/iterator"
    )
    
    // listProductsInProductSet lists products in a product set.
    func listProductsInProductSet(w io.Writer, projectID string, location string, productSetID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[ListProductsInProductSetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ListProductsInProductSetRequest){
    		Name: fmt.Sprintf("projects/%s/locations/%s/productSets/%s", projectID, location, productSetID),
    	}
    
    	it := c.ListProductsInProductSet(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Next: %w", err)
    		}
    
    		fmt.Fprintf(w, "Product name: %s\n", resp.Name)
    		fmt.Fprintf(w, "Product display name: %s\n", resp.DisplayName)
    		fmt.Fprintf(w, "Product category: %s\n", resp.ProductCategory)
    		fmt.Fprintf(w, "Product labels: %s\n", resp.ProductLabels)
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * List all products in a product set.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productSetId - Id of the product set.
     * @throws IOException - on I/O errors.
     */
    public static void listProductsInProductSet(
        String projectId, String computeRegion, String productSetId) throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product set.
        String formattedName = ProductSetName.format(projectId, computeRegion, productSetId);
        // List all the products available in the product set.
        for (Product product : client.listProductsInProductSet(formattedName).iterateAll()) {
          // Display the product information
          System.out.println(String.format("Product name: %s", product.getName()));
          System.out.println(
              String.format(
                  "Product id: %s",
                  product.getName().substring(product.getName().lastIndexOf('/') + 1)));
          System.out.println(String.format("Product display name: %s", product.getDisplayName()));
          System.out.println(String.format("Product description: %s", product.getDescription()));
          System.out.println(String.format("Product category: %s", product.getProductCategory()));
          System.out.println("Product labels: ");
          for (Product.KeyValue element : product.getProductLabelsList()) {
            System.out.println(String.format("%s: %s", element.getKey(), element.getValue()));
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function listProductsInProductSet() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productSetId = 'Id of the product set';
      const productSetPath = client.productSetPath(
        projectId,
        location,
        productSetId
      );
      const request = {
        name: productSetPath,
      };
    
      const [products] = await client.listProductsInProductSet(request);
      products.forEach(product => {
        console.log(`Product name: ${product.name}`);
        console.log(`Product display name: ${product.displayName}`);
      });
    }
    listProductsInProductSet();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def list_products_in_product_set(project_id, location, product_set_id):
        """List all products in a product set.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_set_id: Id of the product set.
        """
        client = vision.ProductSearchClient()
    
        # Get the full path of the product set.
        product_set_path = client.product_set_path(
            project=project_id, location=location, product_set=product_set_id
        )
    
        # List all the products available in the product set.
        products = client.list_products_in_product_set(name=product_set_path)
    
        # Display the product information.
        for product in products:
            print(f"Product name: {product.name}")
            print("Product id: {}".format(product.name.split("/")[-1]))
            print(f"Product display name: {product.display_name}")
            print(f"Product description: {product.description}")
            print(f"Product category: {product.product_category}")
            print(f"Product labels: {product.product_labels}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvisionproductsearch). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
