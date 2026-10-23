---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-import-fhir-resources/
title: Import FHIR resources \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:58.986624+00:00
---

# Import FHIR resources  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-import-fhir-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Import FHIR resources Stay organized with collections  Save and categorize content based on your preferences. 

Import resources to a FHIR store by loading data from the specified sources. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Import and export FHIR resources using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export)



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
    
    // importsFHIRResource imports an FHIR resource.
    func importFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, gcsURI string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.FhirStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    	req := &healthcare.ImportResourcesRequest{
    		ContentStructure: "RESOURCE",
    		GcsSource: &healthcare.GoogleCloudHealthcareV1FhirGcsSource{
    			Uri: gcsURI,
    		},
    	}
    
    	op, err := storesService.Import(name, req).Do()
    	if err != nil {
    		return fmt.Errorf("Import: %w", err)
    	}
    
    	operationsService := healthcareService.Projects.Locations.Datasets.Operations
    	ticker := time.NewTicker(1 * time.Second)
    	defer ticker.Stop()
    	for {
    		select {
    		case <-ctx.Done():
    			return ctx.Err()
    		case <-ticker.C:
    			newOp, err := operationsService.Get(op.Name).Do()
    			if err != nil {
    				return fmt.Errorf("operationsService.Get(%q): %v", op.Name, err)
    			}
    			if newOp.Done {
    				if newOp.Error != nil {
    					return fmt.Errorf("import operation %q completed with error: %s", op.Name, newOp.Error.Details)
    				}
    				return nil
    			}
    		}
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
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.FhirStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.GoogleCloudHealthcareV1FhirGcsSource;
    import com.google.api.services.healthcare.v1.model.ImportResourcesRequest;
    import com.google.api.services.healthcare.v1.model.Operation;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class FhirStoreImport {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStoreImport(String fhirStoreName, String gcsUri) throws IOException {
        // String fhirStoreName =
        //    String.format(
        //        FHIR_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-fhir-id");
        // String gcsUri = "gs://your-bucket-id/path/to/destination/dir"
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure where the store should be imported from.
        GoogleCloudHealthcareV1FhirGcsSource gcsSource =
            new GoogleCloudHealthcareV1FhirGcsSource().setUri(gcsUri);
        ImportResourcesRequest importRequest = new ImportResourcesRequest().setGcsSource(gcsSource);
    
        // Create request and configure any parameters.
        FhirStores.CloudHealthcareImport request =
            client
                .projects()
                .locations()
                .datasets()
                .fhirStores()
                .healthcareImport(fhirStoreName, importRequest);
    
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
          System.out.println("FHIR store import complete: " + operation.getResponse());
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
      responseType: 'json',
    });
    const sleep = ms => {
      return new Promise(resolve => setTimeout(resolve, ms));
    };
    
    const importFhirResources = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const gcsUri = 'my-bucket/my-directory/*.json'
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}`;
      const request = {
        name,
        resource: {
          contentStructure: 'RESOURCE',
          gcsSource: {
            uri: `gs://${gcsUri}`,
          },
        },
      };
      try {
        const operation =
          await healthcare.projects.locations.datasets.fhirStores.import(request);
        const operationName = operation.data.name;
    
        console.log(`Import operation started: ${operationName}`);
    
        let done = false;
        let operationStatus;
        let attempts = 0;
    
        while (!done && attempts < 100) {
          console.log('Waiting for import operation to complete...');
          attempts++;
          await sleep(5000); // Wait 5 seconds between polls
    
          operationStatus =
            await healthcare.projects.locations.datasets.operations.get({
              name: operationName,
            });
    
          done = operationStatus.data.done;
        }
    
        if (operationStatus.data.error) {
          console.error(
            'Import FHIR resources failed:',
            operationStatus.data.error
          );
        } else if (done) {
          const successCount =
            operationStatus.data.metadata?.counter?.success || 0;
          console.log(
            `Import FHIR resources succeeded. ${successCount} resources imported.`
          );
        } else {
          console.error('Import operation timed out in the sample.');
        }
      } catch (error) {
        console.error(
          'An error occurred during the import process:',
          error.message || error
        );
      }
    };
    
    importFhirResources();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def import_fhir_resources(project_id, location, dataset_id, fhir_store_id, gcs_uri):
        """Import resources into the FHIR store by copying them from the
        specified source.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample."""
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        api_version = "v1"
        service_name = "healthcare"
        # Instantiates an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'  # replace with your GCP project ID
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the parent dataset's ID
        # fhir_store_id = 'my-fhir-store'  # replace with the FHIR store ID
        # gcs_uri = 'my-bucket'  # replace with a Cloud Storage bucket
        fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        body = {
            "contentStructure": "CONTENT_STRUCTURE_UNSPECIFIED",
            "gcsSource": {"uri": f"gs://{gcs_uri}"},
        }
    
        # Escape "import()" method keyword because "import"
        # is a reserved keyword in Python
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .import_(name=fhir_store_name, body=body)
        )
    
        response = request.execute()
        print(f"Imported FHIR resources: {gcs_uri}")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
