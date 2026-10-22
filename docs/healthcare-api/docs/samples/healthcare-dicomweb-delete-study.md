---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-dicomweb-delete-study/
title: Delete DICOM study \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:52.122079+00:00
---

# Delete DICOM study  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-dicomweb-delete-study/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Delete DICOM study Stay organized with collections  Save and categorize content based on your preferences. 

Delete all DICOM instances within a given study.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Using the DICOMweb standard](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb)



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
    
    // dicomWebDeleteStudy deletes all instances in the given dicomWebPath study.
    func dicomWebDeleteStudy(w io.Writer, projectID, location, datasetID, dicomStoreID, dicomWebPath string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores.Studies
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	if _, err := storesService.Delete(parent, dicomWebPath).Do(); err != nil {
    		return fmt.Errorf("Delete: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted %q\n", dicomWebPath)
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
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.DicomStores.Studies;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class DicomWebDeleteStudy {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomWebDeleteStudy(String dicomStoreName, String studyId) throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
        // String studyId = "your-study-id";
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Studies.Delete request =
            client
                .projects()
                .locations()
                .datasets()
                .dicomStores()
                .studies()
                .delete(dicomStoreName, "studies/" + studyId);
    
        // Execute the request and process the results.
        request.execute();
        System.out.println("DICOM study deleted.");
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
    
    const dicomWebDeleteStudy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      // const studyUid = '1.3.6.1.4.1.5062.55.1.2270943358.716200484.1363785608958.61.0';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const dicomWebPath = `studies/${studyUid}`;
      const request = {parent, dicomWebPath};
    
      await healthcare.projects.locations.datasets.dicomStores.studies.delete(
        request
      );
      console.log('Deleted DICOM study');
    };
    
    dicomWebDeleteStudy();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def dicomweb_delete_study(project_id, location, dataset_id, dicom_store_id, study_uid):
        """Handles DELETE requests equivalent to the GET requests specified in
        the WADO-RS standard.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/dicom
        before running the sample."""
    
        # Imports the google.auth.transport.requests transport
        from google.auth.transport import requests
    
        # Imports a module to allow authentication using Application Default Credentials (ADC)
        import google.auth
    
        # Gets credentials from the environment. google.auth.default() returns credentials and the
        # associated project ID, but in this sample, the project ID is passed in manually.
        credentials, _ = google.auth.default()
    
        scoped_credentials = credentials.with_scopes(
            ["https://www.googleapis.com/auth/cloud-platform"]
        )
        # Creates a requests Session object with the credentials.
        session = requests.AuthorizedSession(scoped_credentials)
    
        # URL to the Cloud Healthcare API endpoint and version
        base_url = "https://healthcare.googleapis.com/v1"
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'  # replace with your GCP project ID
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the parent dataset's ID
        # dicom_store_id = 'my-dicom-store' # replace with the DICOM store ID
        # study_uid = '1.3.6.1.4.1.5062.55.1.2270943358.716200484.1363785608958.61.0'  # replace with the study UID
        url = f"{base_url}/projects/{project_id}/locations/{location}"
    
        dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/studies/{}".format(
            url, dataset_id, dicom_store_id, study_uid
        )
    
        # Sets the required application/dicom+json; charset=utf-8 header on the request
        headers = {"Content-Type": "application/dicom+json; charset=utf-8"}
    
        response = session.delete(dicomweb_path, headers=headers)
        response.raise_for_status()
    
        print("Deleted study.")
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
