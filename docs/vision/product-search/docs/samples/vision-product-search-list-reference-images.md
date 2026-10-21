---
url: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-list-reference-images/
title: List reference images for product \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:50.433007+00:00
---

# List reference images for product  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-list-reference-images/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)



#  List reference images for product Stay organized with collections  Save and categorize content based on your preferences. 

Retrieves a list of reference images for a product.

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
    
    // listReferenceImages lists reference images of a product.
    func listReferenceImages(w io.Writer, projectID string, location string, productID string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[ListReferenceImagesRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ListReferenceImagesRequest){
    		Parent: fmt.Sprintf("projects/%s/locations/%s/products/%s", projectID, location, productID),
    	}
    
    	it := c.ListReferenceImages(ctx, req)
    	for {
    		resp, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Next: %w", err)
    		}
    
    		fmt.Fprintf(w, "Reference image name: %s\n", resp.Name)
    		fmt.Fprintf(w, "Reference image uri: %s\n", resp.Uri)
    		fmt.Fprintf(w, "Reference image bounding polygons: %s\n", resp.BoundingPolys)
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * List all images in a product.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @throws IOException - on I/O errors.
     */
    public static void listReferenceImagesOfProduct(
        String projectId, String computeRegion, String productId) throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product.
        String formattedParent = ProductName.format(projectId, computeRegion, productId);
        for (ReferenceImage image : client.listReferenceImages(formattedParent).iterateAll()) {
          // Display the reference image information.
          System.out.println(String.format("Reference image name: %s", image.getName()));
          System.out.println(
              String.format(
                  "Reference image id: %s",
                  image.getName().substring(image.getName().lastIndexOf('/') + 1)));
          System.out.println(String.format("Reference image uri: %s", image.getUri()));
          System.out.println(
              String.format(
                  "Reference image bounding polygons: %s \n",
                  image.getBoundingPolysList().toString()));
        }
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function listReferenceImage() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
    
      // const formattedParent = client.productPath(projectId, location, productId);
      // const location = 'A compute region name';
      // const productId = 'Id of the product';
      const formattedParent = client.productPath(projectId, location, productId);
      const request = {
        parent: formattedParent,
      };
    
      const [response] = await client.listReferenceImages(request);
      response.forEach(image => {
        console.log(`image.name: ${image.name}`);
        console.log(`image.uri: ${image.uri}`);
      });
    }
    listReferenceImage();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def list_reference_images(project_id, location, product_id):
        """List all images in a product.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_id: Id of the product.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # Get the full path of the product.
        product_path = client.[product_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_path)(
            project=project_id, location=location, product=product_id
        )
    
        # List all the reference images available in the product.
        reference_images = client.[list_reference_images](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_list_reference_images)(parent=product_path)
    
        # Display the reference image information.
        for image in reference_images:
            print(f"Reference image name: {image.name}")
            print("Reference image id: {}".format(image.name.split("/")[-1]))
            print(f"Reference image uri: {image.uri}")
            print("Reference image bounding polygons: {}".format(image.bounding_polys))
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvisionproductsearch). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
