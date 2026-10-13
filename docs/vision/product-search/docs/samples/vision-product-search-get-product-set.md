---
url: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-get-product-set/
title: Get product set information \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:25.662871+00:00
---

# Get product set information  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-get-product-set/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)



#  Get product set information Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve information about a product set.

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
    )
    
    // getProductSet gets a product set.
    func getProductSet(w io.Writer, projectID string, location string, productSetID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[GetProductSetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_GetProductSetRequest){
    		Name: fmt.Sprintf("projects/%s/locations/%s/productSets/%s", projectID, location, productSetID),
    	}
    
    	resp, err := c.GetProductSet(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetProductSet: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product set name: %s\n", resp.Name)
    	fmt.Fprintf(w, "Product set display name: %s\n", resp.DisplayName)
    	fmt.Fprintf(w, "Product set index time:\n")
    	fmt.Fprintf(w, "seconds: %d\n", resp.IndexTime.Seconds)
    	fmt.Fprintf(w, "nanos: %d\n", resp.IndexTime.Nanos)
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Get info about the product set.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productSetId - Id of the product set.
     * @throws IOException - on I/O errors.
     */
    public static void getProductSet(String projectId, String computeRegion, String productSetId)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product set.
        String formattedName = ProductSetName.format(projectId, computeRegion, productSetId);
        // Get complete detail of the product set.
        ProductSet productSet = client.getProductSet(formattedName);
        // Display the product set information
        System.out.println(String.format("Product set name: %s", productSet.getName()));
        System.out.println(
            String.format(
                "Product set id: %s",
                productSet.getName().substring(productSet.getName().lastIndexOf('/') + 1)));
        System.out.println(
            String.format("Product set display name: %s", productSet.getDisplayName()));
        System.out.println("Product set index time:");
        System.out.println(String.format("\tseconds: %s", productSet.getIndexTime().getSeconds()));
        System.out.println(String.format("\tnanos: %s", productSet.getIndexTime().getNanos()));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function getProductSet() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productSetId = 'Id of the product set';
    
      // Resource path that represents Google Cloud Platform location.
      const productSetPath = client.productSetPath(
        projectId,
        location,
        productSetId
      );
    
      const [productSet] = await client.getProductSet({name: productSetPath});
      console.log(`Product Set name: ${productSet.name}`);
      console.log(`Product Set display name: ${productSet.displayName}`);
    }
    getProductSet();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def get_product_set(project_id, location, product_set_id):
        """Get info about the product set.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_set_id: Id of the product set.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # Get the full path of the product set.
        product_set_path = client.[product_set_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_set_path)(
            project=project_id, location=location, product_set=product_set_id
        )
    
        # Get complete detail of the product set.
        product_set = client.[get_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_get_product_set)(name=product_set_path)
    
        # Display the product set information.
        print(f"Product set name: {product_set.name}")
        print("Product set id: {}".format(product_set.name.split("/")[-1]))
        print(f"Product set display name: {product_set.display_name}")
        print("Product set index time: ")
        print(product_set.index_time)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvisionproductsearch). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
