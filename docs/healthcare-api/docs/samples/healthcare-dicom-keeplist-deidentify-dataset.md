---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-dicom-keeplist-deidentify-dataset/
title: De-identify DICOM data using keeplist \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:22.324925+00:00
---

# De-identify DICOM data using keeplist  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-dicom-keeplist-deidentify-dataset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  De-identify DICOM data using keeplist Stay organized with collections  Save and categorize content based on your preferences. 

Remove PII from DICOM data by using a keeplist.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [De-identifying DICOM data using DicomConfig](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-deidentify)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // deidentifyDataset creates a new dataset containing de-identified data from the source dataset.
    func deidentifyDataset(w io.Writer, projectID, location, sourceDatasetID, destinationDatasetID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	datasetsService := healthcareService.Projects.Locations.Datasets
    
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, location)
    
    	req := &healthcare.DeidentifyDatasetRequest{
    		DestinationDataset: fmt.Sprintf("%s/datasets/%s", parent, destinationDatasetID),
    		Config: &healthcare.DeidentifyConfig{
    			Dicom: &healthcare.DicomConfig{
    				KeepList: &healthcare.TagFilterList{
    					Tags: []string{
    						"PatientID",
    					},
    				},
    			},
    		},
    	}
    
    	sourceName := fmt.Sprintf("%s/datasets/%s", parent, sourceDatasetID)
    	resp, err := datasetsService.Deidentify(sourceName, req).Do()
    	if err != nil {
    		return fmt.Errorf("Deidentify: %w", err)
    	}
    
    	// Wait for the deidentification operation to finish.
    	operationService := healthcareService.Projects.Locations.Datasets.Operations
    	for {
    		op, err := operationService.Get(resp.Name).Do()
    		if err != nil {
    			return fmt.Errorf("operationService.Get: %w", err)
    		}
    		if !op.Done {
    			time.Sleep(1 * time.Second)
    			continue
    		}
    		if op.Error != nil {
    			return fmt.Errorf("deidentify operation error: %v", *op.Error)
    		}
    		fmt.Fprintf(w, "Created de-identified dataset %s from %s\n", resp.Name, sourceName)
    		return nil
    	}
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Java API reference documentation](https://googleapis.dev/java/google-api-services-healthcare/latest/index.html). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.DeidentifyConfig;
    import com.google.api.services.healthcare.v1.model.DeidentifyDatasetRequest;
    import com.google.api.services.healthcare.v1.model.DicomConfig;
    import com.google.api.services.healthcare.v1.model.Operation;
    import com.google.api.services.healthcare.v1.model.TagFilterList;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.Collections;
    
    public class DatasetDeIdentify {
      private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void datasetDeIdentify(String srcDatasetName, String destDatasetName)
          throws IOException {
        // String srcDatasetName =
        //     String.format(DATASET_NAME, "your-project-id", "your-region-id", "your-src-dataset-id");
        // String destDatasetName =
        //    String.format(DATASET_NAME, "your-project-id", "your-region-id", "your-dest-dataset-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure what information needs to be De-Identified.
        // For more information on de-identifying using tags, please see the following:
        // https://cloud.google.com/healthcare/docs/how-tos/dicom-deidentify#de-identification_using_tags
        TagFilterList tags = new TagFilterList().setTags(Arrays.asList("PatientID"));
        DicomConfig dicomConfig = new DicomConfig().setKeepList(tags);
        DeidentifyConfig config = new DeidentifyConfig().setDicom(dicomConfig);
    
        // Create the de-identify request and configure any parameters.
        DeidentifyDatasetRequest deidentifyRequest =
            new DeidentifyDatasetRequest().setDestinationDataset(destDatasetName).setConfig(config);
        Datasets.Deidentify request =
            client.projects().locations().datasets().deidentify(srcDatasetName, deidentifyRequest);
    
        // Execute the request, wait for the operation to complete, and process the results.
        try {
          Operation operation = request.execute();
          while (operation.getDone() == null || !operation.getDone()) {
            // Update the status of the operation with another request.
            Thread.sleep(500); // Pause for 500ms between requests.
            operation =
                client
                    .projects()
                    .locations()
                    .datasets()
                    .operations()
                    .get(operation.getName())
                    .execute();
          }
          System.out.println(
              "De-identified Dataset created. Response content: " + operation.getResponse());
        } catch (Exception ex) {
          System.out.printf("Error during request execution: %s", ex.toString());
          ex.printStackTrace(System.out);
        }
      }
    
      private static CloudHealthcare createClient() throws IOException {
        // Use Application Default Credentials (ADC) to authenticate the requests
        // For more information see https://cloud.google.com/docs/authentication/production
        GoogleCredentials credential =
            GoogleCredentials.getApplicationDefault()
                .createScoped(Collections.singleton(CloudHealthcareScopes.CLOUD_PLATFORM));
    
        // Create a HttpRequestInitializer, which will provide a baseline configuration to all requests.
        HttpRequestInitializer requestInitializer =
            request -> {
              new HttpCredentialsAdapter(credential).initialize(request);
              request.setConnectTimeout(60000); // 1 minute connect timeout
              request.setReadTimeout(60000); // 1 minute read timeout
            };
    
        // Build the client for interacting with the service.
        return new CloudHealthcare.Builder(HTTP_TRANSPORT, JSON_FACTORY, requestInitializer)
            .setApplicationName("your-application-name")
            .build();
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Node.js API reference documentation](https://github.com/googleapis/google-api-nodejs-client/blob/main/src/apis/healthcare/README.md). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const deidentifyDataset = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const sourceDatasetId = 'my-source-dataset';
      // const destinationDatasetId = 'my-destination-dataset';
      // const keeplistTags = 'PatientID'
      const sourceDataset = `projects/${projectId}/locations/${cloudRegion}/datasets/${sourceDatasetId}`;
      const destinationDataset = `projects/${projectId}/locations/${cloudRegion}/datasets/${destinationDatasetId}`;
      const request = {
        sourceDataset: sourceDataset,
        destinationDataset: destinationDataset,
        resource: {
          config: {
            dicom: {
              keepList: {
                tags: [keeplistTags],
              },
            },
          },
        },
      };
    
      await healthcare.projects.locations.datasets.deidentify(request);
      console.log(
        `De-identified data written from dataset ${sourceDatasetId} to dataset ${destinationDatasetId}`
      );
    };
    
    deidentifyDataset();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Dict type for runtime type hints.
    from typing import Dict
    
    
    def deidentify_dataset(
        project_id: str,
        location: str,
        dataset_id: str,
        destination_dataset_id: str,
    ) -> Dict[str, str]:
        """Uses a DICOM tag keeplist to create a new dataset containing de-identified DICOM data from the source dataset.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/datasets
        before running the sample.
        See https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.html#deidentify
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Google Cloud project you want
              to use.
          location: The name of the dataset's location.
          dataset_id: The ID of the source dataset containing the DICOM store to de-identify.
          destination_dataset_id: The ID of the dataset where de-identified DICOM data
            is written.
    
        Returns:
          A dictionary representing a long-running operation that results from
          calling the 'DeidentifyDataset' method. Use the
          'google.longrunning.Operation'
          API to poll the operation status.
        """
        # Imports the Python built-in time module.
        import time
    
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        # Imports HttpError from the Google Python API client errors module.
        from googleapiclient.errors import HttpError
    
        api_version = "v1"
        service_name = "healthcare"
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'
        # location = 'us-central1'
        # dataset_id = 'my-source-dataset'
        # destination_dataset_id = 'my-destination-dataset'
        source_dataset = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        destination_dataset = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, destination_dataset_id
        )
    
        body = {
            "destinationDataset": destination_dataset,
            "config": {
                "dicom": {
                    "keepList": {
                        "tags": [
                            "Columns",
                            "NumberOfFrames",
                            "PixelRepresentation",
                            "MediaStorageSOPClassUID",
                            "MediaStorageSOPInstanceUID",
                            "Rows",
                            "SamplesPerPixel",
                            "BitsAllocated",
                            "HighBit",
                            "PhotometricInterpretation",
                            "BitsStored",
                            "PatientID",
                            "TransferSyntaxUID",
                            "SOPInstanceUID",
                            "StudyInstanceUID",
                            "SeriesInstanceUID",
                            "PixelData",
                        ]
                    }
                }
            },
        }
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .deidentify(sourceDataset=source_dataset, body=body)
        )
    
        # Set a start time for operation completion.
        start_time = time.time()
        # TODO(developer): Increase the max_time if de-identifying many resources.
        max_time = 600
    
        try:
            operation = request.execute()
            while not operation.get("done", False):
                # Poll until the operation finishes.
                print("Waiting for operation to finish...")
                if time.time() - start_time > max_time:
                    raise RuntimeError("Timed out waiting for operation to finish.")
                operation = (
                    client.projects()
                    .locations()
                    .datasets()
                    .operations()
                    .get(name=operation["name"])
                    .execute()
                )
                # Wait 5 seconds between each poll to the operation.
                time.sleep(5)
    
            if operation.get("error"):
                raise TimeoutError(f"De-identify operation failed: {operation['error']}")
            else:
                print(f"De-identified data to dataset: {destination_dataset_id}")
                print(
                    f"Resources succeeded: {operation.get('metadata').get('counter').get('success')}"
                )
                print(
                    f"Resources failed: {operation.get('metadata').get('counter').get('failure')}"
                )
                return operation
    
        except HttpError as err:
            # A common error is when the destination dataset already exists.
            if err.resp.status == 409:
                raise RuntimeError(
                    f"Destination dataset with ID {destination_dataset_id} already exists."
                )
            else:
                raise err
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
