---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-hl7v2-store-get-iam-policy/
title: Get HL7v2 store IAM policy \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:49.651063+00:00
---

# Get HL7v2 store IAM policy  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-hl7v2-store-get-iam-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Get HL7v2 store IAM policy Stay organized with collections  Save and categorize content based on your preferences. 

Get the access control policy for an HL7v2 store.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Controlling access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/controlling-access)



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
    
    // hl7V2IAMPolicy gets the IAM policy.
    func hl7V2IAMPolicy(w io.Writer, projectID, location, datasetID, hl7V2StoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s", projectID, location, datasetID, hl7V2StoreID)
    
    	policy, err := storesService.GetIamPolicy(name).Do()
    	if err != nil {
    		return fmt.Errorf("GetIamPolicy: %w", err)
    	}
    
    	fmt.Fprintf(w, "IAM policy etag: %q\n", policy.Etag)
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
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.Policy;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class Hl7v2StoreGetIamPolicy {
      private static final String HL7v2_NAME = "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2StoreGetIamPolicy(String hl7v2StoreName) throws IOException {
        // String hl7v2StoreName =
        //    String.format(
        //        HL7v2_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-hl7v2-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Hl7V2Stores.GetIamPolicy request =
            client.projects().locations().datasets().hl7V2Stores().getIamPolicy(hl7v2StoreName);
    
        // Execute the request and process the results.
        Policy policy = request.execute();
        System.out.println("HL7v2 store IAMPolicy retrieved: \n" + policy.toPrettyString());
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
    
    const getHl7v2StoreIamPolicy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      const resource_ = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}`;
      const request = {resource_};
    
      const hl7v2Store =
        await healthcare.projects.locations.datasets.hl7V2Stores.getIamPolicy(
          request
        );
      console.log(
        'Got HL7v2 store IAM policy:',
        JSON.stringify(hl7v2Store.data, null, 2)
      );
    };
    
    getHl7v2StoreIamPolicy();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def get_hl7v2_store_iam_policy(project_id, location, dataset_id, hl7v2_store_id):
        """Gets the IAM policy for the specified HL7v2 store.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
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
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset
        # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
        hl7v2_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        hl7v2_store_name = f"{hl7v2_store_parent}/hl7V2Stores/{hl7v2_store_id}"
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .getIamPolicy(resource=hl7v2_store_name)
        )
        response = request.execute()
    
        print("etag: {}".format(response.get("name")))
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
