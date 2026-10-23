---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-fhir-store/
title: Patch FHIR store \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:33.714794+00:00
---

# Patch FHIR store  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-patch-fhir-store/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Patch FHIR store Stay organized with collections  Save and categorize content based on your preferences. 

Patch an FHIR store.

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
    
    // patchFHIRStore updates (patches) a FHIR store by updating its Pub/sub topic name.
    func patchFHIRStore(w io.Writer, projectID, location, datasetID, fhirStoreID, topicName string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.FhirStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    
    	// topicName format is "projects/*/locations/*/topics/*"
    	notificationConfig := &healthcare.FhirNotificationConfig{
    		PubsubTopic: topicName,
    	}
    
    	fhirStore := &healthcare.FhirStore{
    		NotificationConfigs: []*healthcare.FhirNotificationConfig{notificationConfig},
    	}
    
    	patchRequest := storesService.Patch(name, fhirStore).UpdateMask("notificationConfigs")
    
    	if _, err := patchRequest.Do(); err != nil {
    		return fmt.Errorf("Patch: %w", err)
    	}
    
    	fmt.Fprintf(w, "Patched FHIR store %s with Pub/sub topic %s\n", datasetID, topicName)
    
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
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.FhirStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.FhirNotificationConfig;
    import com.google.api.services.healthcare.v1.model.FhirStore;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class FhirStorePatch {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStorePatch(String fhirStoreName, String pubsubTopic) throws IOException {
        // String fhirStoreName =
        // String.format(
        // FHIR_NAME, "your-project-id", "your-region-id", "your-dataset-id",
        // "your-fhir-id");
        // String pubsubTopic = "projects/your-project-id/topics/your-pubsub-topic";
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Fetch the initial state of the FHIR store.
        FhirStores.Get getRequest = client
            .projects()
            .locations()
            .datasets()
            .fhirStores()
            .get(fhirStoreName);
        FhirStore store = getRequest.execute();
    
        // Update the FhirStore fields as needed as needed. For a full list of FhirStore
        // fields, see:
        // https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore
        FhirNotificationConfig notificationConfig = new FhirNotificationConfig()
            .setPubsubTopic(pubsubTopic);
        store.setNotificationConfigs(Collections.singletonList(notificationConfig));
    
        // Create request and configure any parameters.
        FhirStores.Patch request = client
            .projects()
            .locations()
            .datasets()
            .fhirStores()
            .patch(fhirStoreName, store)
            .setUpdateMask("notificationConfigs");
    
        // Execute the request and process the results.
        store = request.execute();
        System.out.println("FHIR store patched: \n" + store.toPrettyString());
      }
    
      private static CloudHealthcare createClient() throws IOException {
        // Use Application Default Credentials (ADC) to authenticate the requests
        // For more information see
        // https://cloud.google.com/docs/authentication/production
        GoogleCredentials credential = GoogleCredentials.getApplicationDefault()
            .createScoped(Collections.singleton(CloudHealthcareScopes.CLOUD_PLATFORM));
    
        // Create a HttpRequestInitializer, which will provide a baseline configuration
        // to all requests.
        HttpRequestInitializer requestInitializer = request -> {
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
    
    const patchFhirStore = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const pubsubTopic = 'my-topic'
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}`;
      const request = {
        name,
        updateMask: 'notificationConfigs',
        resource: {
          notificationConfigs: [
            {
              pubsubTopic: `projects/${projectId}/topics/${pubsubTopic}`,
            },
          ],
        },
      };
    
      try {
        const response =
          await healthcare.projects.locations.datasets.fhirStores.patch(request);
        console.log(
          `Patched FHIR store ${fhirStoreId} with Cloud Pub/Sub topic ${pubsubTopic}`
        );
        console.log(JSON.stringify(response.data, null, 2));
      } catch (error) {
        console.error('Error patching FHIR store:', error.message || error);
      }
    };
    
    patchFhirStore();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def patch_fhir_store(project_id, location, dataset_id, fhir_store_id, pubsub_topic):
        """Updates the FHIR store.
    
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
        # location = 'us-central1'  # replace with the dataset's location
        # dataset_id = 'my-dataset'  # replace with your dataset ID
        # fhir_store_id = 'my-fhir-store'  # replace with the FHIR store's ID
        # pubsub_topic = 'projects/{project_id}/topics/{topic_id}'  # replace with your Pub/Sub topic
        fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        patch = {
            "notificationConfigs": [{"pubsubTopic": pubsub_topic}] if pubsub_topic else []
        }
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .patch(name=fhir_store_name, updateMask="notificationConfigs", body=patch)
        )
    
        response = request.execute()
        print(
            f"Patched FHIR store {fhir_store_id} with Cloud Pub/Sub topic: {pubsub_topic or 'None'}"
        )
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
