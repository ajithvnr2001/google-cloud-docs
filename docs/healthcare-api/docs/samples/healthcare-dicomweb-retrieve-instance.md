---
url: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-dicomweb-retrieve-instance/
title: Retrieve DICOM instance \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:59.088140+00:00
---

# Retrieve DICOM instance  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/samples/healthcare-dicomweb-retrieve-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Samples ](https://docs.cloud.google.com/healthcare-api/docs/samples)



#  Retrieve DICOM instance Stay organized with collections  Save and categorize content based on your preferences. 

Get a DICOM instance within a given study.

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
    	"os"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // dicomWebRetrieveInstance retrieves a specific instance.
    func dicomWebRetrieveInstance(w io.Writer, projectID, location, datasetID, dicomStoreID, dicomWebPath string, outputFile string) error {
    	// projectID := "my-project"
    	// location := "us-central1"
    	// datasetID := "my-dataset"
    	// dicomStoreID := "my-dicom-store"
    	// dicomWebPath := "studies/1.3.6.1.4.1.11129.5.5.1113639985/series/1.3.6.1.4.1.11129.5.5.1953511724/instances/1.3.6.1.4.1.11129.5.5.9562821369"
    	// outputFile := "instance.dcm"
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores.Studies.Series.Instances
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	call := storesService.RetrieveInstance(parent, dicomWebPath)
    	call.Header().Set("Accept", "application/dicom; transfer-syntax=*")
    	resp, err := call.Do()
    	if err != nil {
    		return fmt.Errorf("RetrieveInstance: %w", err)
    	}
    
    	defer resp.Body.Close()
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("RetrieveInstance: status %d %s: %s", resp.StatusCode, resp.Status, resp.Body)
    	}
    
    	file, err := os.Create(outputFile)
    	if err != nil {
    		return fmt.Errorf("os.Create: %w", err)
    	}
    	defer file.Close()
    	if _, err := io.Copy(file, resp.Body); err != nil {
    		return fmt.Errorf("io.Copy: %w", err)
    	}
    
    	fmt.Fprintf(w, "DICOM instance retrieved and downloaded to file: %v\n", outputFile)
    
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Java API reference documentation](https://googleapis.dev/java/google-api-services-healthcare/latest/index.html). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.client.http.[HttpHeaders](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpHeaders.html);
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.[HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.DicomStores.Studies.Series.Instances;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.File;
    import java.io.FileOutputStream;
    import java.io.IOException;
    import java.io.OutputStream;
    import java.util.Collections;
    
    public class DicomWebRetrieveInstance {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final String DICOMWEB_PATH = "studies/%s/series/%s/instances/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomWebRetrieveInstance(String dicomStoreName, String dicomWebPath)
          throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
        // String dicomWebPath = String.format(DICOMWEB_PATH, "your-study-id", "your-series-id",
        // "your-instance-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Instances.RetrieveInstance request =
            client
                .projects()
                .locations()
                .datasets()
                .dicomStores()
                .studies()
                .series()
                .instances()
                .retrieveInstance(dicomStoreName, dicomWebPath);
    
        // Execute the request and process the results.
        HttpResponse response = request.executeUnparsed();
    
        String outputPath = "instance.dcm";
        OutputStream outputStream = new FileOutputStream(new File(outputPath));
        try {
          response.download(outputStream);
          System.out.println("DICOM instance written to file " + outputPath);
        } finally {
          outputStream.close();
        }
    
        if (!response.isSuccessStatusCode()) {
          System.err.print(
              String.format("Exception retrieving DICOM instance: %s\n", response.getStatusMessage()));
          throw new RuntimeException();
        }
      }
    
      private static CloudHealthcare createClient() throws IOException {
        // Use Application Default Credentials (ADC) to authenticate the requests
        // For more information see https://cloud.google.com/docs/authentication/production
        GoogleCredentials credential =
            GoogleCredentials.getApplicationDefault()
                .createScoped(Collections.singleton(CloudHealthcareScopes.CLOUD_PLATFORM));
    
        HttpHeaders headers = new HttpHeaders();
        headers.set("X-GFE-SSL", "yes");
        // Avoid parsing multipart boundaries by setting 'application/dicom' HTTP header.
        // Add 'transfer-syntax=*' to avoid transcoding by returning the file in the format it
        // was originally stored in.
        headers.setAccept("application/dicom; transfer-syntax=*");
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
    const fs = require('fs');
    const util = require('util');
    const writeFile = util.promisify(fs.writeFile);
    const fileName = 'instance_file.dcm';
    
    const dicomWebRetrieveInstance = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      // const studyUid = '1.3.6.1.4.1.5062.55.1.2270943358.716200484.1363785608958.61.0';
      // const seriesUid = '2.24.52329571877967561426579904912379710633';
      // const instanceUid = '1.3.6.2.4.2.14619.5.2.1.6280.6001.129311971280445372188125744148';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const dicomWebPath = `studies/${studyUid}/series/${seriesUid}/instances/${instanceUid}`;
      const request = {parent, dicomWebPath};
    
      const instance =
        await healthcare.projects.locations.datasets.dicomStores.studies.series.instances.retrieveInstance(
          request,
          {
            headers: {Accept: 'application/dicom; transfer-syntax=*'},
            responseType: 'arraybuffer',
          }
        );
      const fileBytes = Buffer.from(instance.data);
    
      await writeFile(fileName, fileBytes);
      console.log(
        `Retrieved DICOM instance and saved to ${fileName} in current directory`
      );
    };
    
    dicomWebRetrieveInstance();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def dicomweb_retrieve_instance(
        project_id,
        location,
        dataset_id,
        dicom_store_id,
        study_uid,
        series_uid,
        instance_uid,
    ):
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
        # study_uid = '1.3.6.1.4.1.5062.55.1.2270943358.716200484.1363785608958.61.0'  # replace with the study UID
        # series_uid = '2.24.52329571877967561426579904912379710633'  # replace with the series UID
        # instance_uid = '1.3.6.2.4.2.14619.5.2.1.6280.6001.129311971280445372188125744148'  # replace with the instance UID
        url = f"{base_url}/projects/{project_id}/locations/{location}"
    
        dicom_store_path = "{}/datasets/{}/dicomStores/{}".format(
            url, dataset_id, dicom_store_id
        )
    
        dicomweb_path = "{}/dicomWeb/studies/{}/series/{}/instances/{}".format(
            dicom_store_path, study_uid, series_uid, instance_uid
        )
    
        file_name = "instance.dcm"
    
        # Set the required Accept header on the request
        headers = {"Accept": "application/dicom; transfer-syntax=*"}
        response = session.get(dicomweb_path, headers=headers)
        response.raise_for_status()
    
        with open(file_name, "wb") as f:
            f.write(response.content)
            print(
                "Retrieved DICOM instance and saved to {} in current directory".format(
                    file_name
                )
            )
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=healthcare). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
