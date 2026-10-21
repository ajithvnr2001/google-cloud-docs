---
url: https://docs.cloud.google.com/vision/product-search/docs/create-product-set/
title: Creating a product set \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:10:13.615053+00:00
---

# Creating a product set  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/create-product-set/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)
  * [ Guides ](https://docs.cloud.google.com/vision/product-search/docs/create-product-set-search-products)



Send feedback 

#  Creating a product set Stay organized with collections  Save and categorize content based on your preferences. 

A product set is a simple container for a group of products.

## Creating an empty product set

It's best to use a single product set for all of your items, and create additional product sets for testing as you need. The following code samples show you how to create an empty product set.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * DISPLAY_NAME: A string display name of your choosing.



HTTP method and URL: 
    
    
    POST https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets

Request JSON body: 
    
    
    {
      "displayName": "display-name"
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
         "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets"

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
        -Uri "https://vision.googleapis.com/v1/projects/project-id/locations/location-id/productSets" | Select-Object -Expand Content

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format.

You should see output similar to the following. You can use the product set ID (`b6d809615b6dd675`, in this case) to perform other operations on the product set.
    
    
    {
      "name": "projects/project-id/locations/location-id/productSets/**b6d809615b6dd675** ",
      "displayName": "new-product-set"
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
    
    // createProductSet creates a product set.
    func createProductSet(w io.Writer, projectID string, location string, productSetID string, productSetDisplayName string) error {
    	ctx := context.Background()
    	c, err := vision.NewProductSearchClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewProductSearchClient: %w", err)
    	}
    	defer c.Close()
    
    	req := &visionpb.[CreateProductSetRequest](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_CreateProductSetRequest){
    		Parent:       fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		ProductSetId: productSetID,
    		ProductSet: &visionpb.[ProductSet](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/vision/v2/latest/apiv1/visionpb.html#cloud_google_com_go_vision_v2_apiv1_visionpb_ProductSet){
    			DisplayName: productSetDisplayName,
    		},
    	}
    
    	resp, err := c.CreateProductSet(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateProductSet: %w", err)
    	}
    
    	fmt.Fprintf(w, "Product set name: %s\n", resp.Name)
    
    	return nil
    }
    

### Java

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-vision/latest/overview). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Create a product set
     *
     * @param projectId - Id of the project.
     * @param computeRegion - Region name.
     * @param productSetId - Id of the product set.
     * @param productSetDisplayName - Display name of the product set.
     * @throws IOException - on I/O errors.
     */
    public static void createProductSet(
        String projectId, String computeRegion, String productSetId, String productSetDisplayName)
        throws IOException {
      try (ProductSearchClient client = ProductSearchClient.create()) {
    
        // A resource that represents Google Cloud Platform location.
        String formattedParent = LocationName.format(projectId, computeRegion);
    
        // Create a product set with the product set specification in the region.
        ProductSet myProductSet =
            ProductSet.newBuilder().setDisplayName(productSetDisplayName).build();
        CreateProductSetRequest request =
            CreateProductSetRequest.newBuilder()
                .setParent(formattedParent)
                .setProductSet(myProductSet)
                .setProductSetId(productSetId)
                .build();
        ProductSet productSet = client.createProductSet(request);
        // Display the product set information
        System.out.println(String.format("Product set name: %s", productSet.getName()));
      }
    }

### Node.js

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Node.js API reference documentation](https://googleapis.dev/nodejs/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const vision = require('[@google-cloud/vision](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)');
    
    // Creates a client
    const client = new vision.[ProductSearchClient](https://docs.cloud.google.com/nodejs/docs/reference/vision/latest/overview.html)();
    
    async function createProductSet() {
      /**
       * TODO(developer): Uncomment the following line before running the sample.
       */
      // const projectId = 'Your Google Cloud project Id';
      // const location = 'A compute region name';
      // const productSetId = 'Id of the product set';
      // const productSetDisplayName = 'Display name of the product set';
    
      // Resource path that represents Google Cloud Platform location.
      const locationPath = client.locationPath(projectId, location);
    
      const productSet = {
        displayName: productSetDisplayName,
      };
    
      const request = {
        parent: locationPath,
        productSet: productSet,
        productSetId: productSetId,
      };
    
      const [createdProductSet] = await client.createProductSet(request);
      console.log(`Product Set name: ${createdProductSet.name}`);
    }
    createProductSet();

### Python

To learn how to install and use the client library for Vision API Product Search, see [Vision API Product Search client libraries](https://docs.cloud.google.com/vision/product-search/docs/libraries). For more information, see the [Vision API Product Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/vision/latest). 

To authenticate to Vision API Product Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import vision
    
    def create_product_set(project_id, location, product_set_id, product_set_display_name):
        """Create a product set.
        Args:
            project_id: Id of the project.
            location: A compute region name.
            product_set_id: Id of the product set.
            product_set_display_name: Display name of the product set.
        """
        client = vision.[ProductSearchClient](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html)()
    
        # A resource that represents Google Cloud Platform location.
        location_path = f"projects/{project_id}/locations/{location}"
    
        # Create a product set with the product set specification in the region.
        product_set = vision.[ProductSet](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.types.ProductSet.html)(display_name=product_set_display_name)
    
        # The response is the product set with `name` populated.
        response = client.[create_product_set](https://docs.cloud.google.com/python/docs/reference/vision/latest/google.cloud.vision_v1.services.product_search.ProductSearchClient.html#google_cloud_vision_v1_services_product_search_ProductSearchClient_create_product_set)(
            parent=location_path, product_set=product_set, product_set_id=product_set_id
        )
    
        # Display the product set information.
        print(f"Product set name: {response.name}")
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for .NET.](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Vision.V1/latest)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-vision/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/vision/product-search/docs/libraries) on the client libraries page and then visit the [Vision API Product Search reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-vision/latest/Google/Cloud/Vision.html)

## Using bulk import to create a product set with products

You can also use the bulk import function to _simultaneously_ create a product set, create multiple products and their reference images.

Various references for the product set, products, and reference images are all set in the bulk import CSV you use. For more information, see [Formatting a bulk import CSV](https://docs.cloud.google.com/vision/product-search/docs/csv-format).

Perform bulk import by running the following code:

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

## Getting the status of an operation

Several operations you request are long-running, such as product set creation via bulk import, purging a product set, and purging orphaned products. These types of requests will return a JSON with an operation ID that you can use to get the status of the operation.

For example, a batch delete (`purge`) request returns the following JSON:
    
    
    {
    "name": "projects/project-id/locations/location-id/operations/**bc4e1d412863e626** "
    }

In this case, the operation ID is `bc4e1d412863e626`. The following samples show how to get the status of this operation with this ID.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION_ID: A valid location identifier. Valid location identifiers are: `us-west1`, `us-east1`, `europe-west1`, and `asia-east1`. 
  * OPERATION_ID: The ID of your operation. The ID is the last element of the name of your operation. For example: 
    * operation name: `projects/PROJECT_ID/locations/LOCATION_ID/operations/**bc4e1d412863e626**`
    * operation id: `**bc4e1d412863e626**`



HTTP method and URL: 
    
    
    GET https://vision.googleapis.com/v1/locations/location-id/operations/operation-id

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "x-goog-user-project: project-id" \  
         "https://vision.googleapis.com/v1/locations/location-id/operations/operation-id"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred"; "x-goog-user-project" = "project-id" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://vision.googleapis.com/v1/locations/location-id/operations/operation-id" | Select-Object -Expand Content

You should see output similar to the following for a completed **product set purge operation** : 
    
    
    {
      "name": "locations/location-id/operations/operation-id",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.BatchOperationMetadata",
        "state": "SUCCESSFUL",
        "submitTime": "2019-09-04T15:58:39.131591882Z",
        "endTime": "2019-09-04T15:58:43.099020580Z"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.PurgeProductsRequest",
        "parent": "projects/project-id/locations/location-id",**"productSetPurgeConfig": {
          "productSetId": " project-set-id"
        },
        "force": true**
      }
    }

You should see output similar to the following for a completed **purge orphaned products operation** :
    
    
    {
      "name": "locations/location-id/operations/operation-id",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.BatchOperationMetadata",
        "state": "SUCCESSFUL",
        "submitTime": "2019-09-04T16:08:38.278197397Z",
        "endTime": "2019-09-04T16:08:45.075778639Z"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.vision.v1.PurgeProductsRequest",
        "parent": "projects/project-id/locations/location-id",**"deleteOrphanProducts": true,
        "force": true**
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
