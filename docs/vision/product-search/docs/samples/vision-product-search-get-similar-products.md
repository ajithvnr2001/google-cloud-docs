---
url: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-get-similar-products/
title: Get products similar to a local image file \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:59.810380+00:00
---

# Get products similar to a local image file  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-get-similar-products/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)



#  Get products similar to a local image file Stay organized with collections  Save and categorize content based on your preferences. 

Search for products that are similar to a locally stored image.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Product Search Tutorial](https://docs.cloud.google.com/vision/product-search/docs/tutorial)
  * [Searching for Products](https://docs.cloud.google.com/vision/product-search/docs/searching)
  * [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries)



## Code sample

### Go

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Go API reference documentation](https://godoc.org/cloud.google.com/go/vision/apiv1). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	vision "cloud.google.com/go/vision/apiv1"
    	"cloud.google.com/go/vision/v2/apiv1/visionpb"
    )
    
    // getSimilarProducts searches for products from a product set similar to products in an image file.
    func getSimilarProducts(w io.Writer, projectID string, location string, productSetID string, productCategory string, file string, filter string) error {
    	ctx := context.Background()
    	c, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImageAnnotatorClient: %w", err)
    	}
    	defer c.Close()
    
    	f, err := os.Open(file)
    	if err != nil {
    		return fmt.Errorf("Open: %w", err)
    	}
    	defer f.Close()
    
    	image, err := vision.[NewImageFromReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_NewImageFromReader)(f)
    	if err != nil {
    		return fmt.Errorf("NewImageFromReader: %w", err)
    	}
    
    	ictx := &visionpb.[ImageContext](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ImageContext){
    		ProductSearchParams: &visionpb.[ProductSearchParams](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ProductSearchParams){
    			ProductSet:        fmt.Sprintf("projects/%s/locations/%s/productSets/%s", projectID, location, productSetID),
    			ProductCategories: []string{productCategory},
    			Filter:            filter,
    		},
    	}
    
    	response, err := c.[ProductSearch](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_ImageAnnotatorClient_ProductSearch)(ctx, image, ictx)
    	if err != nil {
    		return fmt.Errorf("ProductSearch: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product set index time:\n")
    	fmt.Fprintf(w, "seconds: %d\n", response.IndexTime.Seconds)
    	fmt.Fprintf(w, "nanos: %d\n", response.IndexTime.Nanos)
    
    	fmt.Fprintf(w, "Search results:\n")
    	for _, result := range response.Results {
    		fmt.Fprintf(w, "Score(Confidence): %f\n", result.Score)
    		fmt.Fprintf(w, "Image name: %s\n", result.[Image](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Image))
    
    		fmt.Fprintf(w, "Prodcut name: %s\n", result.[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Product).Name)
    		fmt.Fprintf(w, "Product display name: %s\n", result.[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Product).DisplayName)
    		fmt.Fprintf(w, "Product labels: %s\n", result.[Product](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_Product).ProductLabels)
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Search similar products to image in local file.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productSetId - Id of the product set.
     * @param productCategory - Category of the product.
     * @param filePath - Local file path of the image to be searched
     * @param filter - Condition to be applied on the labels. Example for filter: (color = red OR
     *     color = blue) AND style = kids It will search on all products with the following labels:
     *     color:red AND style:kids color:blue AND style:kids
     * @throws IOException - on I/O errors.
     */
    public static void getSimilarProductsFile(
        String projectId,
        String computeRegion,
        String productSetId,
        String productCategory,
        String filePath,
        String filter)
        throws IOException {
      try (ImageAnnotatorClient queryImageClient = ImageAnnotatorClient.create()) {
    
        // Get the full path of the product set.
        String productSetPath = ProductSetName.format(projectId, computeRegion, productSetId);
    
        // Read the image as a stream of bytes.
        File imgPath = new File(filePath);
        byte[] content = Files.readAllBytes(imgPath.toPath());
    
        // Create annotate image request along with product search feature.
        Feature featuresElement = Feature.newBuilder().setType(Type.PRODUCT_SEARCH).build();
        // The input image can be a HTTPS link or Raw image bytes.
        // Example:
        // To use HTTP link replace with below code
        //  ImageSource source = ImageSource.newBuilder().setImageUri(imageUri).build();
        //  Image image = Image.newBuilder().setSource(source).build();
        Image image = Image.newBuilder().setContent(ByteString.copyFrom(content)).build();
        ImageContext imageContext =
            ImageContext.newBuilder()
                .setProductSearchParams(
                    ProductSearchParams.newBuilder()
                        .setProductSet(productSetPath)
                        .addProductCategories(productCategory)
                        .setFilter(filter))
                .build();
    
        AnnotateImageRequest annotateImageRequest =
            AnnotateImageRequest.newBuilder()
                .addFeatures(featuresElement)
                .setImage(image)
                .setImageContext(imageContext)
                .build();
        List<AnnotateImageRequest> requests = Arrays.asList(annotateImageRequest);
    
        // Search products similar to the image.
        BatchAnnotateImagesResponse response = queryImageClient.batchAnnotateImages(requests);
    
        List<Result> similarProducts =
            response.getResponses(0).getProductSearchResults().getResultsList();
        System.out.println("Similar Products: ");
        for (Result product : similarProducts) {
          System.out.println(String.format("\nProduct name: %s", product.getProduct().getName()));
          System.out.println(
              String.format("Product display name: %s", product.getProduct().getDisplayName()));
          System.out.println(
              String.format("Product description: %s", product.getProduct().getDescription()));
          System.out.println(String.format("Score(Confidence): %s", product.getScore()));
          System.out.println(String.format("Image name: %s", product.getImage()));
        }
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    const fs = require('fs');
    // Creates a client
    const productSearchClient = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    const imageAnnotatorClient = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function getSimilarProductsFile() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'nodejs-docs-samples';
      // const location = 'us-west1';
      // const productSetId = 'indexed_product_set_id_for_testing';
      // const productCategory = 'apparel';
      // const filePath = './resources/shoes_1.jpg';
      // const filter = '';
      const productSetPath = productSearchClient.productSetPath(
        projectId,
        location,
        productSetId
      );
      const content = fs.readFileSync(filePath, 'base64');
      const request = {
        // The input image can be a GCS link or HTTPS link or Raw image bytes.
        // Example:
        // To use GCS link replace with below code
        // image: {source: {gcsImageUri: filePath}}
        // To use HTTP link replace with below code
        // image: {source: {imageUri: filePath}}
        image: {content: content},
        features: [{type: 'PRODUCT_SEARCH'}],
        imageContext: {
          productSearchParams: {
            productSet: productSetPath,
            productCategories: [productCategory],
            filter: filter,
          },
        },
      };
      const [response] = await imageAnnotatorClient.batchAnnotateImages({
        requests: [request],
      });
      console.log('Search Image:', filePath);
      const results = response['responses'][0]['productSearchResults']['results'];
      console.log('\nSimilar product information:');
      results.forEach(result => {
        console.log('Product id:', result['product'].name.split('/').pop(-1));
        console.log('Product display name:', result['product'].displayName);
        console.log('Product description:', result['product'].description);
        console.log('Product category:', result['product'].productCategory);
      });
    }
    getSimilarProductsFile();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def get_similar_products_file(
        project_id,
        location,
        product_set_id,
        product_category,
        file_path,
        filter,
        max_results,
    ):
        """Search similar products to image.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_set_id: Id of the product set.
            product_category: Category of the product.
            file_path: Local file path of the image to be searched.
            filter: Condition to be applied on the labels.
                    Example for filter: (color = red OR color = blue) AND style = kids
                    It will search on all products with the following labels:
                    color:red AND style:kids
                    color:blue AND style:kids
            max_results: The maximum number of results (matches) to return. If omitted, all results are returned.
        """
        # product_search_client is needed only for its helper methods.
        product_search_client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
        image_annotator_client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        # Read the image as a stream of bytes.
        with open(file_path, "rb") as image_file:
            content = image_file.read()
    
        # Create annotate image request along with product search feature.
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)(content=content)
    
        # product search specific parameters
        product_set_path = product_search_client.[product_set_path](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_product_set_path)(
            project=project_id, location=location, product_set=product_set_id
        )
        product_search_params = vision.[ProductSearchParams](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ProductSearchParams.html)(
            product_set=product_set_path,
            product_categories=[product_category],
            filter=filter,
        )
        image_context = vision.[ImageContext](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ImageContext.html)(product_search_params=product_search_params)
    
        # Search products similar to the image.
        response = image_annotator_client.[product_search](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.html)(
            image, image_context=image_context, max_results=max_results
        )
    
        index_time = response.product_search_results.index_time
        print("Product set index time: ")
        print(index_time)
    
        results = response.product_search_results.results
    
        print("Search results:")
        for result in results:
            product = result.product
    
            print(f"Score(Confidence): {result.score}")
            print(f"Image name: {result.image}")
    
            print(f"Product name: {product.name}")
            print("Product display name: {}".format(product.display_name))
            print(f"Product description: {product.description}\n")
            print(f"Product labels: {product.product_labels}\n")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvisionproductsearch). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
