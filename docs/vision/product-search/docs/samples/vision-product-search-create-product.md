---
url: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-create-product/
title: Create a product \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:06.734290+00:00
---

# Create a product  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-create-product/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)



#  Create a product Stay organized with collections  Save and categorize content based on your preferences. 

Create a product.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and managing your product resources](https://docs.cloud.google.com/vision/product-search/docs/create-product)
  * [Product Search Tutorial](https://docs.cloud.google.com/vision/product-search/docs/tutorial)



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
    
    // createProduct creates a product.
    func createProduct(w io.Writer, projectID string, location string, productID string, productDisplayName string, productCategory string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[CreateProductRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_CreateProductRequest){
    		Parent:    fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		ProductId: productID,
    		Product: &visionpb.[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Product){
    			DisplayName:     productDisplayName,
    			ProductCategory: productCategory,
    		},
    	}
    
    	resp, err := c.CreateProduct(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateProduct: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product name: %s\n", resp.Name)
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Create one product.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @param productDisplayName - Display name of the product.
     * @param productCategory - Category of the product.
     * @throws IOException - on I/O errors.
     */
    public static void createProduct(
        String projectId,
        String computeRegion,
        String productId,
        String productDisplayName,
        String productCategory)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // A resource that represents Google Cloud Platform location.
        String formattedParent = LocationName.format(projectId, computeRegion);
        // Create a product with the product specification in the region.
        // Multiple labels are also supported.
        Product myProduct =
            Product.newBuilder()
                .setName(productId)
                .setDisplayName(productDisplayName)
                .setProductCategory(productCategory)
                .build();
        Product product = client.createProduct(formattedParent, myProduct, productId);
        // Display the product information
        System.out.println(String.format("Product name: %s", product.getName()));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    async function createProduct() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productId = 'Id of the product';
      // const productDisplayName = 'Display name of the product';
      // const productCategory = 'Catoegory of the product';
    
      // Resource path that represents Google Cloud Platform location.
      const locationPath = client.locationPath(projectId, location);
    
      const product = {
        displayName: productDisplayName,
        productCategory: productCategory,
      };
    
      const request = {
        parent: locationPath,
        product: product,
        productId: productId,
      };
    
      const [createdProduct] = await client.createProduct(request);
      console.log(`Product name: ${createdProduct.name}`);
    }
    createProduct();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    from google.protobuf import field_mask_pb2 as field_mask
    
    def create_product(
        project_id, location, product_id, product_display_name, product_category
    ):
        """Create one product.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_id: Id of the product.
            product_display_name: Display name of the product.
            product_category: Category of the product.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # A resource that represents Google Cloud Platform location.
        location_path = f"projects/{project_id}/locations/{location}"
    
        # Create a product with the product specification in the region.
        # Set product display name and product category.
        product = vision.[Product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Product.html)(
            display_name=product_display_name, product_category=product_category
        )
    
        # The response is the product with the `name` field populated.
        response = client.[create_product](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_create_product)(
            parent=location_path, product=product, product_id=product_id
        )
    
        # Display the product information.
        print(f"Product name: {response.name}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvisionproductsearch). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
