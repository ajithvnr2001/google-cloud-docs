---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-import-dicom-instance/
title: Import DICOM data from Cloud Storage \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:51.894894+00:00
---

# Import DICOM data from Cloud Storage  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-import-dicom-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Import DICOM data from Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Import data into a DICOM store from Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Importing and exporting DICOM data using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // importDICOMInstance imports DICOM objects from GCS.
    func importDICOMInstance(w io.Writer, projectID, location, datasetID, dicomStoreID, contentURI string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	req := &healthcare.ImportDicomDataRequest{
    		GcsSource: &healthcare.GoogleCloudHealthcareV1DicomGcsSource{
    			Uri: contentURI,
    		},
    	}
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	lro, err := storesService.Import(name, req).Do()
    	if err != nil {
    		return fmt.Errorf("Import: %w", err)
    	}
    
    	fmt.Fprintf(w, "Import to DICOM store started. Operation: %q\n", lro.Name)
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Java API reference documentation](https://googleapis.dev/java/google-api-services-healthcare/latest/index.html). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.DicomStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.GoogleCloudHealthcareV1DicomGcsSource;
    import com.google.api.services.healthcare.v1.model.ImportDicomDataRequest;
    import com.google.api.services.healthcare.v1.model.Operation;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class DicomStoreImport {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomStoreImport(String dicomStoreName, String gcsUri) throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
        // String gcsUri = "gs://your-bucket-id/path/to/destination/dir"
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure where the store should be imported from.
        GoogleCloudHealthcareV1DicomGcsSource gcsSource =
            new GoogleCloudHealthcareV1DicomGcsSource().setUri(gcsUri);
        ImportDicomDataRequest importRequest = new ImportDicomDataRequest().setGcsSource(gcsSource);
    
        // Create request and configure any parameters.
        DicomStores.CloudHealthcareImport request =
            client
                .projects()
                .locations()
                .datasets()
                .dicomStores()
                .healthcareImport(dicomStoreName, importRequest);
    
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
          System.out.println("DICOM store import complete." + operation.getResponse());
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
    const sleep = ms => {
      return new Promise(resolve => setTimeout(resolve, ms));
    };
    
    const importDicomInstance = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      // const gcsUri = 'my-bucket/my-directory/*.dcm'
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const request = {
        name,
        resource: {
          // The location of the DICOM instances in Cloud Storage
          gcsSource: {
            uri: `gs://${gcsUri}`,
          },
        },
      };
    
      const operation =
        await healthcare.projects.locations.datasets.dicomStores.import(request);
      const operationName = operation.data.name;
    
      const operationRequest = {name: operationName};
    
      // Wait fifteen seconds for the LRO to finish.
      await sleep(15000);
    
      // Check the LRO's status
      const operationStatus =
        await healthcare.projects.locations.datasets.operations.get(
          operationRequest
        );
    
      const {data} = operationStatus;
    
      if (data.error === undefined) {
        console.log('Successfully imported DICOM instances');
      } else {
        console.log('Encountered errors. Sample error:');
        console.log(
          'Resource on which error occurred:',
          data.error.details[0]['sampleErrors'][0]['resource']
        );
        console.log(
          'Error code:',
          data.error.details[0]['sampleErrors'][0]['error']['code']
        );
        console.log(
          'Error message:',
          data.error.details[0]['sampleErrors'][0]['error']['message']
        );
      }
    };
    
    importDicomInstance();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def import_dicom_instance(
        project_id, location, dataset_id, dicom_store_id, content_uri
    ):
        """Imports data into the DICOM store by copying it from the specified
        source.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/dicom
        before running the sample."""
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        api_version = "v1"
        service_name = "healthcare"
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'  # replace with your GCP project ID
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the DICOM store's parent dataset ID
        # dicom_store_id = 'my-dicom-store'  # replace with the DICOM store's ID
        # content_uri = 'my-bucket/*.dcm'  # replace with a Cloud Storage bucket and DCM files
        dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        dicom_store_name = f"{dicom_store_parent}/dicomStores/{dicom_store_id}"
    
        body = {"gcsSource": {"uri": f"gs://{content_uri}"}}
    
        # Escape "import()" method keyword because "import"
        # is a reserved keyword in Python
        request = (
            client.projects()
            .locations()
            .datasets()
            .dicomStores()
            .import_(name=dicom_store_name, body=body)
        )
    
        response = request.execute()
        print(f"Imported DICOM instance: {content_uri}")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
