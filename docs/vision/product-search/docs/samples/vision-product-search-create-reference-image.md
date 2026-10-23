---
url: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-create-reference-image/
title: Create a reference image \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:49.655765+00:00
---

# Create a reference image  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-create-reference-image/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)



#  Create a reference image Stay organized with collections  Save and categorize content based on your preferences. 

Create a reference image.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating your reference images & indexing](https://docs.cloud.google.com/vision/product-search/docs/create-reference-images)
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
    
    // createReferenceImage creates a reference image for a product.
    func createReferenceImage(w io.Writer, projectID string, location string, productID string, referenceImageID string, gcsURI string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[CreateReferenceImageRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_CreateReferenceImageRequest){
    		Parent: fmt.Sprintf("projects/%s/locations/%s/products/%s", projectID, location, productID),
    		ReferenceImage: &visionpb.[ReferenceImage](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ReferenceImage){
    			Uri: gcsURI,
    		},
    		ReferenceImageId: referenceImageID,
    	}
    
    	resp, err := c.CreateReferenceImage(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateReferenceImage: %w", err)
    	}
    
    	fmt.Fprintf(w, "Reference image name: %s\n", resp.Name)
    	fmt.Fprintf(w, "Reference image uri: %s\n", resp.Uri)
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Create a reference image.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productId - Id of the product.
     * @param referenceImageId - Id of the image.
     * @param gcsUri - Google Cloud Storage path of the input image.
     * @throws IOException - on I/O errors.
     */
    public static void createReferenceImage(
        String projectId,
        String computeRegion,
        String productId,
        String referenceImageId,
        String gcsUri)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // Get the full path of the product.
        String formattedParent = ProductName.format(projectId, computeRegion, productId);
        // Create a reference image.
        ReferenceImage referenceImage = ReferenceImage.newBuilder().setUri(gcsUri).build();
    
        ReferenceImage image =
            client.createReferenceImage(formattedParent, referenceImage, referenceImageId);
        // Display the reference image information.
        System.out.println(String.format("Reference image name: %s", image.getName()));
        System.out.println(String.format("Reference image uri: %s", image.getUri()));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function createReferenceImage() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productId = 'Id of the product';
      // const referenceImageId = 'Id of the reference image';
      // const gcsUri = 'Google Cloud Storage path of the input image';
    
      const formattedParent = client.productPath(projectId, location, productId);
    
      const referenceImage = {
        uri: gcsUri,
      };
    
      const request = {
        parent: formattedParent,
        referenceImage: referenceImage,
        referenceImageId: referenceImageId,
      };
    
      const [response] = await client.createReferenceImage(request);
      console.log(`response.name: ${response.name}`);
      console.log(`response.uri: ${response.uri}`);
    }
    createReferenceImage();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def create_reference_image(
        project_id, location, product_id, reference_image_id, gcs_uri
    ):
        """Create a reference image.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_id: Id of the product.
            reference_image_id: Id of the reference image.
            gcs_uri: Google Cloud Storage path of the input image.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # Get the full path of the product.
        product_path = client.[product_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_path)(
            project=project_id, location=location, product=product_id
        )
    
        # Create a reference image.
        reference_image = vision.[ReferenceImage](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ReferenceImage.html)(uri=gcs_uri)
    
        # The response is the reference image with `name` populated.
        image = client.[create_reference_image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_create_reference_image)(
            parent=product_path,
            reference_image=reference_image,
            reference_image_id=reference_image_id,
        )
    
        # Display the reference image information.
        print(f"Reference image name: {image.name}")
        print(f"Reference image uri: {image.uri}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvisionproductsearch). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
