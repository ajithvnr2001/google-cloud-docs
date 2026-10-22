---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-get-metadata/
title: Get FHIR capability statement \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:10.924179+00:00
---

# Get FHIR capability statement  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-get-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Get FHIR capability statement Stay organized with collections  Save and categorize content based on your preferences. 

Get a capability statement of an FHIR store.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and managing FHIR stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir)



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
    
    // getFHIRMetadata gets FHIR store metadata.
    func getFHIRMetadata(w io.Writer, projectID, location, datasetID, fhirStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    
    	resp, err := fhirService.Capabilities(name).Do()
    	if err != nil {
    		return fmt.Errorf("Capabilities: %w", err)
    	}
    
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("Capabilities: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
    	}
    	fmt.Fprintf(w, "%s", respBytes)
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
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.FhirStores.Fhir.Capabilities;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.HttpBody;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class FhirStoreGetMetadata {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStoreGetMetadata(String fhirStoreName) throws IOException {
        // String fhirStoreName =
        //    String.format(
        //        FHIR_NAME, "project-id", "region-id", "dataset-id", "store-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Capabilities request =
            client.projects().locations().datasets().fhirStores().fhir().capabilities(fhirStoreName);
    
        // Execute the request and process the results.
        HttpBody response = request.execute();
        System.out.println("FHIR store metadata retrieved: " + response.toPrettyString());
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
    
    const getFhirStoreCapabilities = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/metadata`;
      const request = {name};
    
      try {
        const fhirStore =
          await healthcare.projects.locations.datasets.fhirStores.get(request);
        console.log(JSON.stringify(fhirStore.data, null, 2));
      } catch (error) {
        console.error(
          'Error getting FHIR store capabilities:',
          error.message || error
        );
      }
    };
    
    getFhirStoreCapabilities();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def get_fhir_store_metadata(project_id, location, dataset_id, fhir_store_id):
        """Gets the FHIR capability statement (STU3, R4), or the conformance statement
        in the DSTU2 case for the store, which contains a description of functionality
        supported by the server.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample."""
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        # Imports Python's built-in "json" module
        import json
    
        api_version = "v1"
        service_name = "healthcare"
        # Instantiates an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'  # replace with your GCP project ID
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the parent dataset's ID
        # fhir_store_id = 'my-fhir-store' # replace with the FHIR store ID
        fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        fhir_stores = client.projects().locations().datasets().fhirStores()
        response = fhir_stores.fhir().capabilities(name=fhir_store_name).execute()
    
        print(json.dumps(response, indent=2))
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
