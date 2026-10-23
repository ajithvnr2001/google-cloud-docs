---
url: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-import-product-images/
title: Import multiple product images \u00a0|\u00a0 Vision API Product Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:11.703570+00:00
---

# Import multiple product images  |  Vision API Product Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision/product-search/docs/samples/vision-product-search-import-product-images/

The Product Search feature is in maintenance mode. For better scalability and the same functionality as Product Search, use the [Vision Warehouse](https://cloud.google.com/vision-ai/docs/warehouse-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Vision API Product Search ](https://docs.cloud.google.com/vision/product-search/docs)



#  Import multiple product images Stay organized with collections  Save and categorize content based on your preferences. 

Import images of multiple products in a product set.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating a product set](https://docs.cloud.google.com/vision/product-search/docs/create-product-set)
  * [Creating your reference images & indexing](https://docs.cloud.google.com/vision/product-search/docs/create-reference-images)



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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudvisionproductsearch). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
