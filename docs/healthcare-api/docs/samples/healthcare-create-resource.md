---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-create-resource/
title: Create FHIR resource \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:10.358081+00:00
---

# Create FHIR resource  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-create-resource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Create FHIR resource Stay organized with collections  Save and categorize content based on your preferences. 

Create a FHIR resource in a FHIR store.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and managing FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources)
  * [Store healthcare data with client libraries](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library)



## Code sample

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // createFHIRResource creates an FHIR resource.
    func createFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, resourceType string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	payload := map[string]interface{}{
    		"resourceType": resourceType,
    		"language":     "FR",
    	}
    	jsonPayload, err := json.Marshal(payload)
    	if err != nil {
    		return fmt.Errorf("json.Encode: %w", err)
    	}
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    
    	call := fhirService.Create(parent, resourceType, bytes.NewReader(jsonPayload))
    	call.Header().Set("Content-Type", "application/fhir+json;charset=utf-8")
    	resp, err := call.Do()
    	if err != nil {
    		return fmt.Errorf("Create: %w", err)
    	}
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("Create: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
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
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.net.URISyntaxException;
    import java.util.Collections;
    import org.apache.http.HttpEntity;
    import org.apache.http.[HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html);
    import org.apache.http.HttpStatus;
    import org.apache.http.client.HttpClient;
    import org.apache.http.client.methods.HttpUriRequest;
    import org.apache.http.client.methods.RequestBuilder;
    import org.apache.http.client.utils.URIBuilder;
    import org.apache.http.entity.StringEntity;
    import org.apache.http.impl.client.HttpClients;
    
    public class FhirResourceCreate {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirResourceCreate(String fhirStoreName, String resourceType)
          throws IOException, URISyntaxException {
        // String fhirStoreName =
        //    String.format(
        //        FHIR_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-fhir-id");
        // String resourceType = "Patient";
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%sv1/%s/fhir/%s", client.getRootUrl(), fhirStoreName, resourceType);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
        StringEntity requestEntity =
            new StringEntity("{\"resourceType\": \"" + resourceType + "\", \"language\": \"en\"}");
    
        HttpUriRequest request =
            RequestBuilder.post()
                .setUri(uriBuilder.build())
                .setEntity(requestEntity)
                .addHeader("Content-Type", "application/fhir+json")
                .addHeader("Accept-Charset", "utf-8")
                .addHeader("Accept", "application/fhir+json; charset=utf-8")
                .build();
    
        // Execute the request and process the results.
        HttpResponse response = httpClient.execute(request);
        HttpEntity responseEntity = response.getEntity();
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_CREATED) {
          System.err.print(
              String.format(
                  "Exception creating FHIR resource: %s\n", response.getStatusLine().toString()));
          responseEntity.writeTo(System.err);
          throw new RuntimeException();
        }
        System.out.print("FHIR resource created: ");
        responseEntity.writeTo(System.out);
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
    
      private static String getAccessToken() throws IOException {
        [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credential =
            [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)()
                .createScoped(Collections.singleton(CloudHealthcareScopes.CLOUD_PLATFORM));
    
        return credential.refreshAccessToken().getTokenValue();
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
      headers: {'Content-Type': 'application/fhir+json'},
      responseType: 'json',
    });
    
    async function createFhirResource() {
      // Replace the following body with the data for the resource you want to
      // create.
      const body = {
        name: [{use: 'official', family: 'Smith', given: ['Darcy']}],
        gender: 'female',
        birthDate: '1970-01-01',
        resourceType: 'Patient',
      };
    
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const resourceType = 'Patient';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}`;
    
      const request = {parent, type: resourceType, requestBody: body};
      const resource =
        await healthcare.projects.locations.datasets.fhirStores.fhir.create(
          request
        );
      console.log(`Created FHIR resource with ID ${resource.data.id}`);
      console.log(resource.data);
    }
    
    createFhirResource();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the types Dict and Any for runtime type hints.
    from typing import Any, Dict  # noqa: E402
    
    
    def create_patient(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
    ) -> Dict[str, Any]:
        """Creates a new Patient resource in a FHIR store.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample.
        See
        https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.fhirStores.fhir.html#create
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Cloud project you want
            to use.
          location: The name of the parent dataset's location.
          dataset_id: The name of the parent dataset.
          fhir_store_id: The name of the FHIR store that holds the Patient resource.
    
        Returns:
          A dict representing the created Patient resource.
        """
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        api_version = "v1"
        service_name = "healthcare"
    
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'
        # location = 'us-central1'
        # dataset_id = 'my-dataset'
        # fhir_store_id = 'my-fhir-store'
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        patient_body = {
            "name": [{"use": "official", "family": "Smith", "given": ["Darcy"]}],
            "gender": "female",
            "birthDate": "1970-01-01",
            "resourceType": "Patient",
        }
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .create(parent=fhir_store_name, type="Patient", body=patient_body)
        )
        # Sets required application/fhir+json header on the googleapiclient.http.HttpRequest.
        request.headers["content-type"] = "application/fhir+json;charset=utf-8"
        response = request.execute()
    
        print(f"Created Patient resource with ID {response['id']}")
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
