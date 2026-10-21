---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-dicomweb-search-studies/
title: DICOM search for studies using query params/DICOM tags \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:42:04.611816+00:00
---

# DICOM search for studies using query params/DICOM tags  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-dicomweb-search-studies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  DICOM search for studies using query params/DICOM tags Stay organized with collections  Save and categorize content based on your preferences. 

Use query parameters to search by DICOM tag, such as PatientName.

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
    
    // queryParamOpt is a googleapi.Option (https://godoc.org/google.golang.org/api/googleapi#CallOption)
    // that adds query parameters to an API call.
    type queryParamOpt struct {
    	key, value string
    }
    
    func (qp queryParamOpt) Get() (string, string) { return qp.key, qp.value }
    
    // dicomWebSearchStudies refines a DICOMweb studies search by appending DICOM tags to the request.
    func dicomWebSearchStudies(w io.Writer, projectID, location, datasetID, dicomStoreID, dicomWebPath string) error {
    	// projectID := "my-project"
    	// location := "us-central1"
    	// datasetID := "my-dataset"
    	// dicomStoreID := "my-dicom-store"
    	// dicomWebPath := "studies"
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	call := storesService.SearchForStudies(name, dicomWebPath)
    	// Refine your search by appending DICOM tags to the
    	// request in the form of query parameters. This sample
    	// searches for studies containing a patient's name.
    	patientName := queryParamOpt{key: "PatientName", value: "Sally Zhang"}
    	resp, err := call.Do(patientName)
    	if err != nil {
    		return fmt.Errorf("Get: %w", err)
    	}
    
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("ioutil.ReadAll: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("SearchForStudies: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
    	}
    	respString := string(respBytes)
    	if len(respString) > 0 {
    		fmt.Fprintf(w, "Found studies: %s\n", respString)
    	} else {
    		fmt.Println("No studies found.")
    	}
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Java API reference documentation](https://googleapis.dev/java/google-api-services-healthcare/latest/index.html). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.[HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.DicomStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class DicomWebSearchStudies {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomWebSearchStudies(String dicomStoreName) throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        DicomStores.SearchForStudies request =
            client
                .projects()
                .locations()
                .datasets()
                .dicomStores()
                .searchForStudies(dicomStoreName, "studies")
                // Refine your search by appending DICOM tags to the
                // request in the form of query parameters. This sample
                // searches for studies containing a patient's name.
                .set("PatientName", "Sally Zhang");
    
        // Execute the request and process the results.
        HttpResponse response = request.executeUnparsed();
        System.out.println("Studies found: \n" + response.toString());
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
    
    const dicomWebSearchStudies = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const dicomWebPath = 'studies';
      const request = {parent, dicomWebPath};
    
      const studies =
        await healthcare.projects.locations.datasets.dicomStores.searchForStudies(
          request,
          {
            // Refine your search by appending DICOM tags to the
            // request in the form of query parameters. This sample
            // searches for studies containing a patient's name.
            params: {PatientName: 'Sally Zhang'},
            headers: {Accept: 'application/dicom+json'},
          }
        );
      console.log(studies);
    
      console.log(`Found ${studies.data.length} studies:`);
      console.log(JSON.stringify(studies.data));
    };
    
    dicomWebSearchStudies();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def dicomweb_search_studies(project_id, location, dataset_id, dicom_store_id):
        """Handles the GET requests specified in the DICOMweb standard.
    
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
        url = f"{base_url}/projects/{project_id}/locations/{location}"
    
        dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/studies".format(
            url, dataset_id, dicom_store_id
        )
    
        # Refine your search by appending DICOM tags to the
        # request in the form of query parameters. This sample
        # searches for studies containing a patient's name.
        params = {"PatientName": "Sally Zhang"}
    
        response = session.get(dicomweb_path, params=params)
    
        response.raise_for_status()
    
        print(f"Studies found: response is {response}")
    
        # Uncomment the following lines to process the response as JSON.
        # patients = response.json()
        # print('Patients found matching query:')
        # print(json.dumps(patients, indent=2))
    
        # return patients
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
