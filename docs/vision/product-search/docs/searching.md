---
url: https://docs.cloud.google.com/vision/product-search/docs/searching/
title: Searching for Products \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:10:11.308606+00:00
---

# Searching for Products  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/searching/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/product-search/docs/create-product-set-search-products)



Send feedback 

#  Searching for Products Stay organized with collections  Save and categorize content based on your preferences. 

Once you have [created your product set](https://docs.cloud.google.com/vision/product-search/docs/create-product) and the product set has been indexed, you can query the product set using the Cloud Vision API.

## Matching product search

You can find similar products to a given image by passing the image's Google Cloud Storage URI, web URL, or [base64 encoded string](https://docs.cloud.google.com/vision/product-search/docs/base64) to Vision API Product Search. Refer to the [Usage Limits](https://docs.cloud.google.com/vision/quotas) for maximum request size and quota information.

See the [Understanding search responses & multi-detection](https://docs.cloud.google.com/vision/product-search/docs/searching-response) topic for an example of single product detection and multi-detection of products in an image.

### Search using a local image

The following samples read a local file and query the API by including inline the raw image bytes (base64 encoded image) in the request.

### REST

Before using any of the request data, make the following replacements: 

  * BASE64_ENCODED_IMAGE: The base64 representation (ASCII string) of your binary image data. This string should look similar to the following string: 
    * `/9j/4QAYRXhpZgAA...9tAVx/zDQDlGxn//2Q==`
Visit the [base64 encode](https://docs.cloud.google.com/vision/product-search/docs/base64) topic for more information.
  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_SET_ID: The ID for the product set you want to run the operation on.



**Field-specific considerations:**

  * `features.maxResults` \- The maximum number of results to be returned. 
  * `imageContext.productCategories` \- The product category to search in. Currently you can only specify one product category (homegoods, apparel, toys, packaged goods, and general ). 
  * `imageContext.filter` \- (Optional) A key-value filtering expression (or multiple expressions) for product label. Format: "`key`=`value`". Filtering key-value pairs can be linked with AND or OR expressions: "`color`=`blue` AND `style`=`mens`", or "`color`=`blue` OR `color`=`black`". If using the OR expression **all keys in the expression must be the same**. 



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/images:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "image": {
            "content": base64-encoded-image
          },
          "features": [
            {
              "type": "PRODUCT_SEARCH",
              "maxResults": 5
            }
          ],
          "imageContext": {
            "productSearchParams": {
              "productSet": "projects/project-id/locations/location-id/productSets/product-set-id",
              "productCategories": [
                   "apparel"
              ],
              "filter": "style = womens"
            }
          }
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/images:annotate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/images:annotate" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

The response JSON includes the two following result types:

  * `productSearchResults` \- Contains a list of matching products for the entire image. In the sample response the matching products are: product_id65, product_id35, product_id34, product_id62, product_id32. 
  * `productGroupedResults` \- Contains bounding box coordinates and matching items for _each_ product identified in the image. In the following response there is only one product identified, followed by matching products in the sample product set: product_id65, product_id35, product_id34, product_id93, product_id62. 



Note that while there is overlap in the two result types, there may also be differences (for example, product_id32 and product_id93 in the response).

**Note: Zero coordinate values omitted.** When the API detects a coordinate ("x" or "y") value of 0, **_that coordinate is omitted in the JSON response_**. Thus, a response with a bounding poly around the entire image would be   
**[{},{"x": 1},{"x": 1,"y": 1},{"y": 1}]**. For more information, see the [API Reference documentation](https://cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.products.referenceImages#boundingpoly). 

#### Response
    
    
    
    
    
    {
      "responses": [
        {**"productSearchResults"** : {
            "indexTime": "2019-09-04T21:03:35.662099907Z",
            "results": [
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id65** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.38946953,
                "image": "projects/project-id/locations/location-id/products/product_id65/referenceImages/**image65** "
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id35** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.3847863,
                "image": "projects/project-id/locations/location-id/products/product_id35/referenceImages/**image35** "
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id34** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.33896044,
                "image": "projects/project-id/locations/location-id/products/product_id34/referenceImages/**image34** "
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id62** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.32509044,
                "image": "projects/project-id/locations/location-id/products/product_id62/referenceImages/**image62** "
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id32** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.3237155,
                "image": "projects/project-id/locations/location-id/products/product_id32/referenceImages/image32"
              }
            ],**"productGroupedResults"** : [
              {
                "boundingPoly": {
                  "normalizedVertices": [
                    {
                      "x": 0.00458825,
                      "y": 0.11000001
                    },
                    {
                      "x": 0.988353,
                      "y": 0.11000001
                    },
                    {
                      "x": 0.988353,
                      "y": 0.9290588
                    },
                    {
                      "x": 0.00458825,
                      "y": 0.9290588
                    }
                  ]
                },
                "results": [
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id65** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.41785678,
                    "image": "projects/project-id/locations/location-id/products/product_id65/referenceImages/**image65** "
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id35** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.3803885,
                    "image": "projects/project-id/locations/location-id/products/product_id35/referenceImages/**image35** "
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id34** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.36055994,
                    "image": "projects/project-id/locations/location-id/products/product_id34/referenceImages/**image34** "
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id93** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "shoe"
                        },
                        {
                          "key": "kids",
                          "value": "true"
                        }
                      ]
                    },
                    "score": 0.33286288,
                    "image": "projects/project-id/locations/location-id/products/product_id93/referenceImages/**image93** "
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id62** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.32263064,
                    "image": "projects/project-id/locations/location-id/products/product_id62/referenceImages/**image62** "
                  }
                ],
                "objectAnnotations": [
                  {
                    "mid": "/m/01d40f",
                    "name": "Dress",
                    "score": 0.95488
                  }
                ]
              }
            ]
          }
        }
      ]
    }

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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

### Search using a remote image

You also have the option of finding similar products to a given image by specifying the Cloud Storage URI to the image.

### REST

Before using any of the request data, make the following replacements: 

  * CLOUD_STORAGE_IMAGE_URI: the path to a valid image file in a Cloud Storage bucket. You must at least have read privileges to the file. Example: 
    * gs://storage-bucket/filename.jpg

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_SET_ID: The ID for the product set you want to run the operation on.



**Field-specific considerations:**

  * `features.maxResults` \- The maximum number of results to be returned. 
  * `imageContext.productCategories` \- The product category to search in. Currently you can only specify one product category (homegoods, apparel, toys, packaged goods, and general ). 
  * `imageContext.filter` \- (Optional) A key-value filtering expression (or multiple expressions) for product label. Format: "`key`=`value`". Filtering key-value pairs can be linked with AND or OR expressions: "`color`=`blue` AND `style`=`mens`", or "`color`=`blue` OR `color`=`black`". If using the OR expression **all keys in the expression must be the same**. 



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/images:annotate

Request JSON body: 
    
    
    {
      "requests": [
        {
          "image": {
            "source": {
              "gcsImageUri": "cloud-storage-image-uri"
            }
          },
          "features": [
            {
              "type": "PRODUCT_SEARCH",
              "maxResults": 5
            }
          ],
          "imageContext": {
            "productSearchParams": {
              "productSet": "projects/project-id/locations/location-id/productSets/product-set-id",
              "productCategories": [
                   "apparel"
              ],
              "filter": "style = womens"
            }
          }
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://vision.googleapis.com/v1/images:annotate"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://vision.googleapis.com/v1/images:annotate" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

The response JSON includes the two following result types:

  * `productSearchResults` \- Contains a list of matching products for the entire image. In the sample response the matching products are: product_id65, product_id35, product_id34, product_id62, product_id32. 
  * `productGroupedResults` \- Contains bounding box coordinates and matching items for _each_ product identified in the image. In the following response there is only one product identified, followed by matching products in the sample product set: product_id65, product_id35, product_id34, product_id93, product_id62. 



Note that while there is overlap in the two result types, there may also be differences (for example, product_id32 and product_id93 in the response).

**Note: Zero coordinate values omitted.** When the API detects a coordinate ("x" or "y") value of 0, **_that coordinate is omitted in the JSON response_**. Thus, a response with a bounding poly around the entire image would be   
**[{},{"x": 1},{"x": 1,"y": 1},{"y": 1}]**. For more information, see the [API Reference documentation](https://cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.products.referenceImages#boundingpoly). 

#### Response
    
    
    
    
    
    {
      "responses": [
        {**"productSearchResults"** : {
            "indexTime": "2019-09-04T21:03:35.662099907Z",
            "results": [
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id65** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.38946953,
                "image": "projects/project-id/locations/location-id/products/product_id65/referenceImages/**image65** "
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id35** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.3847863,
                "image": "projects/project-id/locations/location-id/products/product_id35/referenceImages/**image35** "
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id34** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.33896044,
                "image": "projects/project-id/locations/location-id/products/product_id34/referenceImages/**image34** "
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id62** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.32509044,
                "image": "projects/project-id/locations/location-id/products/product_id62/referenceImages/**image62** "
              },
              {
                "product": {
                  "name": "projects/project-id/locations/location-id/products/**product_id32** ",
                  "displayName": " ",
                  "productCategory": "apparel",
                  "productLabels": [
                    {
                      "key": "style",
                      "value": "women"
                    },
                    {
                      "key": "category",
                      "value": "dress"
                    }
                  ]
                },
                "score": 0.3237155,
                "image": "projects/project-id/locations/location-id/products/product_id32/referenceImages/image32"
              }
            ],**"productGroupedResults"** : [
              {
                "boundingPoly": {
                  "normalizedVertices": [
                    {
                      "x": 0.00458825,
                      "y": 0.11000001
                    },
                    {
                      "x": 0.988353,
                      "y": 0.11000001
                    },
                    {
                      "x": 0.988353,
                      "y": 0.9290588
                    },
                    {
                      "x": 0.00458825,
                      "y": 0.9290588
                    }
                  ]
                },
                "results": [
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id65** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.41785678,
                    "image": "projects/project-id/locations/location-id/products/product_id65/referenceImages/**image65** "
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id35** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.3803885,
                    "image": "projects/project-id/locations/location-id/products/product_id35/referenceImages/**image35** "
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id34** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.36055994,
                    "image": "projects/project-id/locations/location-id/products/product_id34/referenceImages/**image34** "
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id93** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "shoe"
                        },
                        {
                          "key": "kids",
                          "value": "true"
                        }
                      ]
                    },
                    "score": 0.33286288,
                    "image": "projects/project-id/locations/location-id/products/product_id93/referenceImages/**image93** "
                  },
                  {
                    "product": {
                      "name": "projects/project-id/locations/location-id/products/**product_id62** ",
                      "displayName": " ",
                      "productCategory": "apparel",
                      "productLabels": [
                        {
                          "key": "style",
                          "value": "women"
                        },
                        {
                          "key": "category",
                          "value": "dress"
                        }
                      ]
                    },
                    "score": 0.32263064,
                    "image": "projects/project-id/locations/location-id/products/product_id62/referenceImages/**image62** "
                  }
                ],
                "objectAnnotations": [
                  {
                    "mid": "/m/01d40f",
                    "name": "Dress",
                    "score": 0.95488
                  }
                ]
              }
            ]
          }
        }
      ]
    }

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
    
    // getSimilarProductsURI searches for products from a product set similar to products in an image file on GCS.
    func getSimilarProductsURI(w io.Writer, projectID string, location string, productSetID string, productCategory string, imageURI string, filter string) error {
    	ctx := context.Background()
    	c, err := vision.NewImageAnnotatorClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewImageAnnotatorClient: %w", err)
    	}
    	defer c.Close()
    
    	image := vision.[NewImageFromURI](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/latest/apiv1.html#cloud_google_com_go_vision_apiv1_NewImageFromURI)(imageURI)
    
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
     * Search similar products to image in Google Cloud Storage.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productSetId - Id of the product set.
     * @param productCategory - Category of the product.
     * @param gcsUri - GCS file path of the image to be searched
     * @param filter - Condition to be applied on the labels. Example for filter: (color = red OR
     *     color = blue) AND style = kids It will search on all products with the following labels:
     *     color:red AND style:kids color:blue AND style:kids
     * @throws Exception - on errors.
     */
    public static void getSimilarProductsGcs(
        String projectId,
        String computeRegion,
        String productSetId,
        String productCategory,
        String gcsUri,
        String filter)
        throws Exception {
      try (ImageAnnotatorClient queryImageClient = ImageAnnotatorClient.create()) {
    
        // Get the full path of the product set.
        String productSetPath = ProductSetName.of(projectId, computeRegion, productSetId).toString();
    
        // Get the image from Google Cloud Storage
        ImageSource source = ImageSource.newBuilder().setGcsImageUri(gcsUri).build();
    
        // Create annotate image request along with product search feature.
        Feature featuresElement = Feature.newBuilder().setType(Type.PRODUCT_SEARCH).build();
        Image image = Image.newBuilder().setSource(source).build();
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
    // Creates a client
    const productSearchClient = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    const imageAnnotatorClient = new vision.[ImageAnnotatorClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function getSimilarProductsGcs(
      projectId,
      location,
      productSetId,
      productCategory,
      filePath,
      filter
    ) {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productSetId = 'Id of the product set';
      // const productCategory = 'Category of the product';
      // const filePath = 'Local file path of the image to be searched';
      // const filter = 'Condition to be applied on the labels';
      const productSetPath = productSearchClient.productSetPath(
        projectId,
        location,
        productSetId
      );
    
      const request = {
        // The input image can be a GCS link or HTTPS link or Raw image bytes.
        // Example:
        // To use GCS link replace with below code
        // image: {source: {gcsImageUri: filePath}}
        // To use HTTP link replace with below code
        // image: {source: {imageUri: filePath}}
        image: {source: {gcsImageUri: filePath}},
        features: [{type: 'PRODUCT_SEARCH'}],
        imageContext: {
          productSearchParams: {
            productSet: productSetPath,
            productCategories: [productCategory],
            filter: filter,
          },
        },
      };
      console.log(request.image);
    
      const [response] = await imageAnnotatorClient.batchAnnotateImages({
        requests: [request],
      });
      console.log('Search Image:', filePath);
      console.log('\nSimilar product information:');
    
      const results = response['responses'][0]['productSearchResults']['results'];
      results.forEach(result => {
        console.log('Product id:', result['product'].name.split('/').pop(-1));
        console.log('Product display name:', result['product'].displayName);
        console.log('Product description:', result['product'].description);
        console.log('Product category:', result['product'].productCategory);
      });
    }
    getSimilarProductsGcs();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def get_similar_products_uri(
        project_id, location, product_set_id, product_category, image_uri, filter
    ):
        """Search similar products to image.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_set_id: Id of the product set.
            product_category: Category of the product.
            image_uri: Cloud Storage location of image to be searched.
            filter: Condition to be applied on the labels.
            Example for filter: (color = red OR color = blue) AND style = kids
            It will search on all products with the following labels:
            color:red AND style:kids
            color:blue AND style:kids
        """
        # product_search_client is needed only for its helper methods.
        product_search_client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
        image_annotator_client = vision.[ImageAnnotatorClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.image_annotator.ImageAnnotatorClient.html)()
    
        # Create annotate image request along with product search feature.
        image_source = vision.[ImageSource](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ImageSource.html)(image_uri=image_uri)
        image = vision.[Image](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.Image.html)(source=image_source)
    
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
        response = image_annotator_client.[product_search](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.html)(image, image_context=image_context)
    
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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
