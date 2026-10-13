---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-delete-resource/
title: Delete FHIR resource \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:08.243636+00:00
---

# Delete FHIR resource  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-delete-resource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Delete FHIR resource Stay organized with collections  Save and categorize content based on your preferences. 

Delete an FHIR resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating and managing FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources)



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
    
    // deleteFHIRResource deletes an FHIR resource.
    // Regardless of whether the operation succeeds or
    // fails, the server returns a 200 OK HTTP status code. To check that the
    // resource was successfully deleted, search for or get the resource and
    // see if it exists.
    func deleteFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s", projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID)
    
    	if _, err := fhirService.Delete(name).Do(); err != nil {
    		return fmt.Errorf("Delete: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted %q", name)
    
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
    import org.apache.http.impl.client.HttpClients;
    
    public class FhirResourceDelete {
      private static final String FHIR_NAME =
          "projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirResourceDelete(String resourceName)
          throws IOException, URISyntaxException {
        // String resourceName =
        //    String.format(
        //        FHIR_NAME, "project-id", "region-id", "dataset-id", "store-id", "resource-type",
        // "resource-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%sv1/%s", client.getRootUrl(), resourceName);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
    
        HttpUriRequest request =
            RequestBuilder.delete()
                .setUri(uriBuilder.build())
                .addHeader("Content-Type", "application/fhir+json")
                .addHeader("Accept-Charset", "utf-8")
                .addHeader("Accept", "application/fhir+json; charset=utf-8")
                .build();
    
        // Execute the request and process the results.
        // Regardless of whether the operation succeeds or
        // fails, the server returns a 200 OK HTTP status code. To check that the
        // resource was successfully deleted, search for or get the resource and
        // see if it exists.
        HttpResponse response = httpClient.execute(request);
        HttpEntity responseEntity = response.getEntity();
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
          String errorMessage =
              String.format(
                  "Exception deleting FHIR resource: %s\n", response.getStatusLine().toString());
          System.err.print(errorMessage);
          responseEntity.writeTo(System.err);
          throw new RuntimeException(errorMessage);
        }
        System.out.println("FHIR resource deleted.");
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
      responseType: 'json',
    });
    
    const deleteFhirResource = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const resourceType = 'Patient';
      // const resourceId = '9a664e07-79a4-4c2e-04ed-e996c75484e1';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/${resourceType}/${resourceId}`;
      const request = {name};
    
      // Regardless of whether the operation succeeds or
      // fails, the server returns a 200 OK HTTP status code. To check that the
      // resource was successfully deleted, search for or get the resource and
      // see if it exists.
      try {
        await healthcare.projects.locations.datasets.fhirStores.fhir.delete(
          request
        );
        console.log(`Deleted FHIR resource: ${resourceId}`);
      } catch (error) {
        console.error('Error deleting FHIR resource:', error.message || error);
      }
    };
    
    deleteFhirResource();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_resource(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
        resource_type: str,
        resource_id: str,
    ) -> dict:
        """Deletes a FHIR resource.
    
        Regardless of whether the operation succeeds or
        fails, the server returns a 200 OK HTTP status code. To check that the
        resource was successfully deleted, search for or get the resource and
        see if it exists.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample.
        See
        https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.fhirStores.fhir.html#delete
        for the Python API reference.
        Args:
          project_id: The project ID or project number of the Cloud project you want
            to use.
          location: The name of the parent dataset's location.
          dataset_id: The name of the parent dataset.
          fhir_store_id: The name of the FHIR store.
          resource_type: The type of the FHIR resource.
          resource_id: The "logical id" of the FHIR resource you want to delete. The
            ID is assigned by the server.
    
        Returns:
          An empty dict.
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
        # resource_type = 'Patient'
        # resource_id = 'b682d-0e-4843-a4a9-78c9ac64'
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_resource_path = f"{fhir_store_parent}/fhirStores/{fhir_store_id}/fhir/{resource_type}/{resource_id}"
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .delete(name=fhir_resource_path)
        )
        response = request.execute()
        print(f"Deleted {resource_type} resource with ID {resource_id}.")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
