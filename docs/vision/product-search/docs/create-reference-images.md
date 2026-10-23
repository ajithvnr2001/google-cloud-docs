---
url: https://docs.cloud.google.com/vision/product-search/docs/create-reference-images/
title: Creating your reference images & indexing \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:50.978802+00:00
---

# Creating your reference images & indexing  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/create-reference-images/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/product-search/docs/create-product-set-search-products)



Send feedback 

#  Creating your reference images & indexing Stay organized with collections  Save and categorize content based on your preferences. 

Reference images are images containing various views of your products. The following recommendations apply:

  * Make sure the size of the file doesn't exceed the maximum size (20MB).
  * Consider viewpoints that logically highlight the product and contain relevant visual information.
  * Create reference images that supplement any missing viewpoints. For example, if you only have images of the right shoe in a pair, provide mirrored versions of those files as the left shoe.
  * Upload the highest resolution image available.
  * Show the product against a white background.
  * Convert PNGs with transparent backgrounds to a solid background.



Images must be stored in a [Cloud Storage](https://cloud.google.com/storage/) bucket. If you're authenticating your image create call with an API key, the bucket must be public. If you're authenticating with a service account, that service account must have read access on the bucket.

## Creating a single reference image

You can add a reference image to an existing product. This then allows you to search for the product by the image.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * PRODUCT_ID: The ID for the product that is associated with a reference image. This ID is either randomly set or specified by the user at product creation time.
  * CLOUD_STORAGE_IMAGE_URI: the path to a valid image file in a Cloud Storage bucket. You must at least have read privileges to the file. Example: 
    * gs://storage-bucket/filename.jpg

**Note** : The boundingPolys field is optional. If you don't specify a bounding box, Cloud Vision API will try to infer regions of interest in the image that are compatible with the `productCategory` on the parent product. 


HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages

Request JSON body: 
    
    
    {
      "uri": "cloud-storage-image-uri",
      "boundingPolys": [
        {
          "vertices": [
            {
              "x": X_MIN,
              "y": Y_MIN
            },
            {
              "x": X_MAX,
              "y": Y_MIN
            },
            {
              "x": X_MAX,
              "y": Y_MAX
            },
            {
              "x": X_MIN,
              "y": Y_MAX
            }
          ]
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
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages"

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
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/products/product-id/referenceImages" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

You should see output similar to the following. The example request specified a single `boundingPoly` in the image. The vertices for the bounding box are _not_ normalized; the vertex values are the actual pixel values, and _not_ relative to the original image and scaled from 0 to 1. These vertices have the following values: [(33,22),(282,22),(282,278),(33,278)]. 
    
    
    
    {
      "name": "projects/project-id/locations/location-id/products/product-id/referenceImages/image-id",
      "uri": "gs://storage-bucket/filename.jpg",
      "boundingPolys": [
        {
          "vertices": [
            {
              "x": 33,
              "y": 22
            },
            {
              "x": 282,
              "y": 22
            },
            {
              "x": 282,
              "y": 278
            },
            {
              "x": 33,
              "y": 278
            }
          ]
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
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Creating multiple reference images with bulk import

You can also create reference images at the same time you create a product set and multiple products.

Create reference images in bulk by passing the Cloud Storage location of a CSV file to the [`import`](https://docs.cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.productSets/import) method. Thus, the CSV file _and_ the images it points to must both be in a Cloud Storage bucket.

If you're authenticating your bulk import call with an **API key** , this CSV source file must be public.

If you're authenticating with a **service account** , that service account must have read access on the CSV source file.

### CSV format
    
    
    image-uri,[image-id],product-set-id,product-id,product-category,[product-display-name],[label(s)],[bounding-poly]
    

See the [CSV format](https://docs.cloud.google.com/vision/product-search/docs/csv-format) how-to topic for more detailed information about formatting your CSV.

### Bulk creation request

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * STORAGE_PATH: A Cloud Storage bucket/directory where your input CSV file is stored. The requesting user must have at least read permission to the bucket.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets:import

Request JSON body: 
    
    
    {
      "inputConfig": {
        "gcsSource": {
          "csvFileUri": "storage-path"
        }
      }
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
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets:import"

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
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets:import" | Select-Object -Expand Content

You should see output similar to the following. You can use the operation ID (`f10f34e32c40a710`, in this case) to get the status of the task. For an example, see Getting an operation's status:
    
    
    {
      "name": "projects/project-id/locations/location-id/operations/**f10f34e32c40a710** "
    }

After the long-running operation completes you can get the details of the import operation. The response should look similar to the following:
    
    
    {
      "name": "locations/location-id/operations/f10f34e32c40a710",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.BatchOperationMetadata",
        "state": "SUCCESSFUL",
        "submitTime": "2019-12-06T21:16:04.476466873Z",
        "endTime": "2019-12-06T21:16:40.594258084Z"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.ImportProductSetsResponse",
        "referenceImages": [
          {
            "name": "projects/project-id/locations/location-id/products/product_id0/referenceImages/image0",
            "uri": "gs://my-storage-bucket/img_039.jpg"
          },
          {
            "name": "projects/project-id/locations/location-id/products/product_id1/referenceImages/image1",
            "uri": "gs://my-storage-bucket/img_105.jpg"
          },
          {
            "name": "projects/project-id/locations/location-id/products/product_id2/referenceImages/image2",
            "uri": "gs://my-storage-bucket/img_224.jpg"
          },
          {
            "name": "projects/project-id/locations/location-id/products/product_id3/referenceImages/image3",
            "uri": "gs://my-storage-bucket/img_385.jpg"
          }
        ],
        "statuses": [
          {},
          {},
          {},
          {}
        ]
      }
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
    
    
    // importProductSets creates a product set using information in a csv file on GCS.
    func importProductSets(w io.Writer, projectID string, location string, gcsURI string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[ImportProductSetsRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ImportProductSetsRequest){
    		Parent: fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		InputConfig: &visionpb.[ImportProductSetsInputConfig](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ImportProductSetsInputConfig){
    			Source: &visionpb.[ImportProductSetsInputConfig_GcsSource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ImportProductSetsInputConfig_GcsSource){
    				GcsSource: &visionpb.[ImportProductSetsGcsSource](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ImportProductSetsGcsSource){
    					CsvFileUri: gcsURI,
    				},
    			},
    		},
    	}
    
    	op, err := c.ImportProductSets(ctx, req)
    	if err != nil {
    		return fmt.Errorf("ImportProductSets: %w", err)
    	}
    
    	fmt.Fprintf(w, "Processing operation name: %s\n", op.Name())
    
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "processing done.\n")
    
    	for i, status := range resp.Statuses {
    		// `0` is the coee for OK in google.rpc.code
    		fmt.Fprintf(w, "Status of processing line %d of the csv: %d\n", i, status.Code)
    
    		if status.Code == 0 {
    			fmt.Fprintf(w, "Reference image name: %s\n", resp.ReferenceImages[i].Name)
    		} else {
    			fmt.Fprintf(w, "Status code not OK: %s\n", status.Message)
    		}
    	}
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Import images of different products in the product set.
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param gcsUri - Google Cloud Storage URI.Target files must be in Product Search CSV format.
     * @throws Exception - on client errors.
     */
    public static void importProductSets(String projectId, String computeRegion, String gcsUri)
        throws Exception {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // A resource that represents Google Cloud Platform location.
        String formattedParent = LocationName.format(projectId, computeRegion);
        Builder gcsSource = ImportProductSetsGcsSource.newBuilder().setCsvFileUri(gcsUri);
    
        // Set the input configuration along with Google Cloud Storage URI
        ImportProductSetsInputConfig inputConfig =
            ImportProductSetsInputConfig.newBuilder().setGcsSource(gcsSource).build();
    
        // Import the product sets from the input URI.
        OperationFuture<ImportProductSetsResponse, BatchOperationMetadata> response =
            client.importProductSetsAsync(formattedParent, inputConfig);
    
        System.out.println(String.format("Processing operation name: %s", response.getName()));
        ImportProductSetsResponse results = response.get();
        System.out.println("Processing done.");
        System.out.println("Results of the processing:");
    
        for (int i = 0; i < results.getStatusesCount(); i++) {
          System.out.println(
              String.format(
                  "Status of processing line %s of the csv: %s", i, results.getStatuses(i)));
          // Check the status of reference image.
          if (results.getStatuses(i).getCode() == 0) {
            ReferenceImage referenceImage = results.getReferenceImages(i);
            System.out.println(referenceImage);
          } else {
            System.out.println("No reference image.");
          }
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
    
    async function importProductSets() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const gcsUri = 'Google Cloud Storage URI. Target files must be in Product Search CSV format';
    
      // A resource that represents Google Cloud Platform location.
      const projectLocation = client.locationPath(projectId, location);
    
      // Set the input configuration along with Google Cloud Storage URI
      const inputConfig = {
        gcsSource: {
          csvFileUri: gcsUri,
        },
      };
    
      // Import the product sets from the input URI.
      const [response, operation] = await client.importProductSets({
        parent: projectLocation,
        inputConfig: inputConfig,
      });
    
      console.log('Processing operation name: ', operation.name);
    
      // synchronous check of operation status
      const [result] = await response.promise();
      console.log('Processing done.');
      console.log('Results of the processing:');
    
      for (const i in result.statuses) {
        console.log(
          'Status of processing ',
          i,
          'of the csv:',
          result.statuses[i]
        );
    
        // Check the status of reference image
        if (result.statuses[i].code === 0) {
          console.log(result.referenceImages[i]);
        } else {
          console.log('No reference image.');
        }
      }
    }
    importProductSets();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def import_product_sets(project_id, location, gcs_uri):
        """Import images of different products in the product set.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            gcs_uri: Google Cloud Storage URI.
                Target files must be in Product Search CSV format.
        """
        client = vision.ProductSearchClient()
    
        # A resource that represents Google Cloud Platform location.
        location_path = f"projects/{project_id}/locations/{location}"
    
        # Set the input configuration along with Google Cloud Storage URI
        gcs_source = vision.ImportProductSetsGcsSource(csv_file_uri=gcs_uri)
        input_config = vision.ImportProductSetsInputConfig(gcs_source=gcs_source)
    
        # Import the product sets from the input URI.
        response = client.import_product_sets(
            parent=location_path, input_config=input_config
        )
    
        print(f"Processing operation name: {response.operation.name}")
        # synchronous check of operation status
        result = response.result()
        print("Processing done.")
    
        for i, status in enumerate(result.statuses):
            print("Status of processing line {} of the csv: {}".format(i, status))
            # Check the status of reference image
            # `0` is the code for OK in google.rpc.Code.
            if status.code == 0:
                reference_image = result.reference_images[i]
                print(reference_image)
            else:
                print(f"Status code not OK: {status.message}")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

**Common import error messages include:**

  * `The number of columns in the csv line should be 8`: If you're not providing a bounding box, the line must end with a comma. For example: 
        
        "gs://example-reference-images/10002-002/10002-002_B.jpg","sample-set","sample-product-123","apparel",,

  * `Image not found`: Your Cloud Storage URI does not resolve to an image file.
  * `Access denied`: Either your image or your CSV file does not have the correct permissions. Image files must be accessible by the authentication method used for your request. If you are authenticating with an API Key, then your CSV files must be public.



## Indexing

The Product Search index of products is updated approximately every day. When images are added or deleted, the change won't be reflected in your Product Search responses until the index is next updated.

To make sure that indexing has completed successfully, check the [`indexTime`](https://cloud.google.com/vision/product-search/docs/reference/rest/v1/projects.locations.productSets#ProductSet) field of a product set.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
