---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb/
title: Using the DICOMweb standard \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:40.349198+00:00
---

# Using the DICOMweb standard  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Using the DICOMweb standard Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use the Cloud Healthcare API's implementation of [DICOMweb](https://www.dicomstandard.org/using/dicomweb) to store and manage DICOM image data.

For more information on how the Cloud Healthcare API implements various DICOMweb REST services, see the [DICOM conformance statement](https://docs.cloud.google.com/healthcare-api/docs/dicom).

The DICOMweb implementation in the Cloud Healthcare API only supports REST, not RPC.

## Install the Cloud Healthcare API DICOMweb CLI

**Note:** If you only intend to use DICOM Studio or the API directly to interact with DICOM Web, you can skip this step.

Several of the samples on this page use the [Cloud Healthcare API DICOMweb CLI](https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli), an open source tool that simplifies how to interact with DICOMweb servers. The tool provides functionality for storing, retrieving, deleting, and searching for DICOM files. The GitHub page for the tool contains further information such as detailed installation requirements and ways to customize the tool.

The tool runs using Python. For information on how to set up Python on Google Cloud, see [Setting up a Python development environment](https://docs.cloud.google.com/python/docs/setup).

After setting up Python, you can install the tool using Pip:
    
    
    pip install https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli/archive/v1.0.zip
    

To use the tool, you must authenticate to the Google Cloud servers. You can do so using either of the following methods:

  * [Setting the `GOOGLE_APPLICATION_CREDENTIALS` environment variable](https://docs.cloud.google.com/healthcare-api/docs/how-tos/authentication#setting_the_environment_variables)
  * [Authenticating through the Google Cloud CLI using `gcloud auth application-default login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login)



After configuring either of these options, the tool automatically detects your credentials.

## Store DICOM data

Before you can store DICOM data, you need to [create a DICOM store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom).

The Cloud Healthcare API implements the [Store transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.5) RESTful web service when storing DICOM data. For more information, see [Store transaction](https://docs.cloud.google.com/healthcare-api/docs/dicom#store_transaction) in the Cloud Healthcare API DICOM conformance statement.

**Note:** For large workflows that have high data volumes, we recommend that you use [DICOM import](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export#importing_dicom_objects) for optimal performance.

Store DICOM data using one of the following methods. Include the `application/dicom` Accept header in your request.

  * **Store a DICOM instance** : Typically a `.dcm` file.
  * **Store multiple items using a multiple part (multipart) message** : Construct a multipart file with multiple parts of data separated by a boundary. In your request, set the `Content-Type` to `multipart/related; type=application/dicom; boundary=BOUNDARY`, where `BOUNDARY` is a user-defined value indicating the different parts of the message. See [RFC 1341](https://www.rfc-editor.org/rfc/rfc1341) for details on creating multipart messages.

Use multipart messages to store the following DICOM data types:

    * DICOM studies or series containing multiple instances. Separate each instance using a boundary. For instructions, see Store a DICOM study or series using a multipart message.
    * DICOM JSON metadata with JPEG files. Separate each set of data using a boundary. For instructions, see Create DICOM instances from JSON metadata and JPEG images.



The `SOP_CLASS_UID`, `SOP_INSTANCE_UID`, `STUDY_INSTANCE_UID`, and `SERIES_INSTANCE_UID` values are populated from the provided metadata. UIDs must meet these requirements:

  * Contain only numeric values separated by periods.
  * Contain no protected health information (PHI).



The following samples show how to store an instance in a DICOM store. For more information, see [`projects.locations.datasets.dicomStores.storeInstances`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/storeInstances).

### Store a DICOM instance

The following samples show how to store a DICOM instance. For more information, see [`projects.locations.datasets.dicomStores.storeInstances`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/storeInstances).

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `DICOM_INSTANCE_FILE`: the path to a DICOM instance file on your local machine ending in the `.dcm` suffix



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/dicom" \  
         --data-binary @DICOM_INSTANCE_FILE \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -InFile DICOM_INSTANCE_FILE `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies" | Select-Object -Expand Content

The output is the following XML response: 

#### Response
    
    
    <NativeDicomModel>
      <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
        <Value number="1">https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID</Value>
      </DicomAttribute>
      <DicomAttribute tag="00081199" vr="SQ" keyword="ReferencedSOPSequence">
        <Item number="1">
          <DicomAttribute tag="00081150" vr="UI" keyword="ReferencedSOPClassUID">
            <Value number="1">SOP_CLASS_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081155" vr="UI" keyword="ReferencedSOPInstanceUID">
            <Value number="1">SOP_INSTANCE_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
            <Value number="1">https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID</Value>
          </DicomAttribute>
        </Item>
      </DicomAttribute>
    </NativeDicomModel>
    

### Go
    
    
    import (
    	"bytes"
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // dicomWebStoreInstance stores the given dicomFile with the dicomWebPath.
    func dicomWebStoreInstance(w io.Writer, projectID, location, datasetID, dicomStoreID, dicomWebPath, dicomFile string) error {
    	ctx := context.Background()
    
    	dicomData, err := os.ReadFile(dicomFile)
    	if err != nil {
    		return fmt.Errorf("os.ReadFile: %w", err)
    	}
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	call := storesService.StoreInstances(parent, dicomWebPath, bytes.NewReader(dicomData))
    	call.Header().Set("Content-Type", "application/dicom")
    	resp, err := call.Do()
    	if err != nil {
    		return fmt.Errorf("StoreInstances: %w", err)
    	}
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("StoreInstances: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
    	}
    	fmt.Fprintf(w, "%s", respBytes)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.File;
    import java.io.IOException;
    import java.net.URISyntaxException;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    import java.util.Collections;
    import org.apache.http.HttpEntity;
    import org.apache.http.[HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html);
    import org.apache.http.HttpStatus;
    import org.apache.http.client.HttpClient;
    import org.apache.http.client.methods.HttpUriRequest;
    import org.apache.http.client.methods.RequestBuilder;
    import org.apache.http.client.utils.URIBuilder;
    import org.apache.http.entity.ByteArrayEntity;
    import org.apache.http.impl.client.HttpClients;
    
    public class DicomWebStoreInstance {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomWebStoreInstance(String dicomStoreName, String filePath)
          throws IOException, URISyntaxException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
        // String filePath = "path/to/file.dcm";
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%sv1/%s/dicomWeb/studies", client.getRootUrl(), dicomStoreName);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
        // Load the data from file representing the study.
        File f = new File(filePath);
        byte[] dicomBytes = Files.readAllBytes(Paths.get(filePath));
        ByteArrayEntity requestEntity = new ByteArrayEntity(dicomBytes);
    
        HttpUriRequest request =
            RequestBuilder.post(uriBuilder.build())
                .setEntity(requestEntity)
                .addHeader("Content-Type", "application/dicom")
                .build();
    
        // Execute the request and process the results.
        HttpResponse response = httpClient.execute(request);
        HttpEntity responseEntity = response.getEntity();
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
          System.err.print(
              String.format(
                  "Exception storing DICOM instance: %s\n", response.getStatusLine().toString()));
          responseEntity.writeTo(System.err);
          throw new RuntimeException();
        }
        System.out.println("DICOM instance stored: ");
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
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    const fs = require('fs');
    
    const dicomWebStoreInstance = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      // const dcmFile = 'file.dcm';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const dicomWebPath = 'studies';
      // Use a stream because other types of reads overwrite the client's HTTP
      // headers and cause storeInstances to fail.
      const binaryData = fs.createReadStream(dcmFile);
      const request = {
        parent,
        dicomWebPath,
        requestBody: binaryData,
      };
    
      const instance =
        await healthcare.projects.locations.datasets.dicomStores.storeInstances(
          request,
          {
            headers: {
              'Content-Type': 'application/dicom',
              Accept: 'application/dicom+json',
            },
          }
        );
      console.log('Stored DICOM instance:\n', JSON.stringify(instance.data));
    };
    
    dicomWebStoreInstance();

### Python
    
    
    def dicomweb_store_instance(project_id, location, dataset_id, dicom_store_id, dcm_file):
        """Handles the POST requests specified in the DICOMweb standard.
    
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
        # dcm_file = 'dicom000_0001.dcm'  # replace with a DICOM file
        url = f"{base_url}/projects/{project_id}/locations/{location}"
    
        dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/studies".format(
            url, dataset_id, dicom_store_id
        )
    
        with open(dcm_file, "rb") as dcm:
            dcm_content = dcm.read()
    
        # Sets required "application/dicom" header on the request
        headers = {"Content-Type": "application/dicom"}
    
        response = session.post(dicomweb_path, data=dcm_content, headers=headers)
        response.raise_for_status()
        print("Stored DICOM instance:")
        print(response.text)
        return response
    
    

### Store a DICOM study or series using a multipart message

The following samples show how to store a DICOM study or series, consisting of multiple instances, using a multipart message.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `MULTIPART_FILE`: the path to a multipart file on your local machine. The file contains multiple DICOM instances, with each separated by a boundary.
  * `BOUNDARY`: the boundary used to separate the DICOM instances in the multipart file



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: multipart/related; type=application/dicom; boundary=BOUNDARY" \  
         --data-binary @MULTIPART_FILE \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -InFile MULTIPART_FILE `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies" | Select-Object -Expand Content

The output is similar to the following, with multiple instances returned: 

#### Response
    
    
    <NativeDicomModel>
      <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
        <Value number="1">https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID</Value>
      </DicomAttribute>
      <DicomAttribute tag="00081199" vr="SQ" keyword="ReferencedSOPSequence">
        <Item number="1">
          <DicomAttribute tag="00081150" vr="UI" keyword="ReferencedSOPClassUID">
            <Value number="1">SOP_CLASS_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081155" vr="UI" keyword="ReferencedSOPInstanceUID">
            <Value number="1">SOP_INSTANCE_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
            <Value number="1">https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID</Value>
          </DicomAttribute>
        </Item>
      </DicomAttribute>
    </NativeDicomModel>
    

### Specify a storage class for DICOM instances

By default, the `projects.locations.datasets.dicomStores.storeInstances` method stores a DICOM instance in a DICOM store with a standard storage class. You can set the storage class when you store DICOM objects from your local machine. For more information, see [Change DICOM storage class](https://docs.cloud.google.com/healthcare-api/docs/dicom-storage-class).

The following samples show how to specify the storage class when you store DICOM objects from your local machine.

### curl

Use the [`projects.locations.datasets.dicomStores.storeInstances`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/storeInstances) method. Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `DICOM_INSTANCE_FILE`: the path to a DICOM instance file on your local machine ending in the `.dcm` suffix
  * `STORAGE_CLASS`: the storage class for the DICOM instance in the DICOM store from `STANDARD`,`NEARLINE`, `COLDLINE`, and `ARCHIVE`


    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/dicom" \
        -H "Storage-Class: STORAGE_CLASS" \
        --data-binary @DICOM_INSTANCE_FILE \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies"

If the request is successful, the server returns the response:
    
    
    <NativeDicomModel>
      <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
        <Value number="1">https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID</Value>
      </DicomAttribute>
      <DicomAttribute tag="00081199" vr="SQ" keyword="ReferencedSOPSequence">
        <Item number="1">
          <DicomAttribute tag="00081150" vr="UI" keyword="ReferencedSOPClassUID">
            <Value number="1">SOP_CLASS_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081155" vr="UI" keyword="ReferencedSOPInstanceUID">
            <Value number="1">SOP_INSTANCE_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
            <Value number="1">https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID</Value>
          </DicomAttribute>
        </Item>
      </DicomAttribute>
    </NativeDicomModel>
    

### PowerShell

Use the [`projects.locations.datasets.dicomStores.storeInstances`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/storeInstances) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `DICOM_INSTANCE_FILE`: the path to a DICOM instance file on your local machine ending in the `.dcm` suffix
  * `STORAGE_CLASS`: the storage class for the DICOM instance in the DICOM store from `STANDARD`,`NEARLINE`, `COLDLINE`, and `ARCHIVE`


    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ "Authorization" = "Bearer $cred"; "Storage-Class" = "STORAGE_CLASS" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/dicom" `
      -InFile DCM_FILE.dcm `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    <NativeDicomModel>
      <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
        <Value number="1">https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID</Value>
      </DicomAttribute>
      <DicomAttribute tag="00081199" vr="SQ" keyword="ReferencedSOPSequence">
        <Item number="1">
          <DicomAttribute tag="00081150" vr="UI" keyword="ReferencedSOPClassUID">
            <Value number="1">SOP_CLASS_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081155" vr="UI" keyword="ReferencedSOPInstanceUID">
            <Value number="1">SOP_INSTANCE_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
            <Value number="1">https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID</Value>
          </DicomAttribute>
        </Item>
      </DicomAttribute>
    </NativeDicomModel>
    

### Create DICOM instances from JSON metadata and JPEG images

The Cloud Healthcare API can create DICOM instances using a JSON metadata file and a JPEG file. Create DICOM instances from JSON metadata and JPEG file if you prefer not to do DICOM parsing and serialization yourself, as the Cloud Healthcare API can do these tasks for you.

The HTTP request that stores this data must include the following in the request's `Content-Type`:

  * The `multipart/related` media type
  * The MIME type `application/dicom+json`
  * A `boundary` separator



The following samples show how to store a JSON metadata file with a JPEG file.

### curl

The following sample assumes that you have an existing JPEG image.

Storing a JSON metadata file with a JPEG image comprises three steps:

  1. Create a file that contains a JSON representation of a DICOM instance containing a JPEG image. A template file is provided below.
  2. Create three boundary files:

     * `opening.file`: Contains the opening boundary for the JSON metadata file
     * `middle.file`: Contains the middle boundary for the JPEG image
     * `closing.file`: Contains the closing boundary for all parts of the message
  3. Create a file called `multipart-request.file` by enclosing the JSON metadata file and the JPEG image within the boundary files.




Note the following values that are provided by default in the JSON metadata template file:

  * The Transfer Syntax UID (`1.2.840.10008.1.2.4.50`) designates the Transfer Syntax as JPEG Baseline. Most JPEG images are in the JPEG Baseline format. The Photometric Interpretation Value [(`YBR_FULL_422`)](https://dicom.nema.org/medical/dicom/current/output/html/part05.html#table_8.2.1-1) signifies that the image is in color, not grayscale.
  * `BulkDataUri` is an arbitrary descriptor for the image, and in the template it is set to `jpeg-image`. This value is used when creating the image boundary.



The values for SOP_CLASS_UID, SOP_INSTANCE_UID, STUDY_INSTANCE_UID, and SERIES_INSTANCE_UID can be any numeric value separated by periods. DICOM uses a hierarchy of identifiers for instances, patients, studies, and series, so choose a logical set of identifiers for these variables.

Replace SOP Class UID with a value from the [table of Standard SOP Classes](https://dicom.nema.org/medical/dicom/current/output/html/part04.html#table_B.5-1) that designates the type of image being stored.

**Note:** Depending on the SOP Class you use, you might need to add more tags to the JSON metadata file. For example, if you are using a Magnetic Resonance Image (MR Image), consult [Table A.4-1. MR Image IOD Modules](https://dicom.nema.org/medical/dicom/current/output/html/part03.html#table_A.4-1) to determine the required tags.

Replace Rows with the vertical height of the JPEG image in pixels. Replace Columns with the horizontal width of the JPEG image in pixels.

Complete the following steps:

  1. Save the following text to a file called `instance.json`, replacing variables where specified.
         
         [{
          "00020010":{"vr":"UI","Value":["1.2.840.10008.1.2.4.50"]},
          "00080005":{"vr":"CS","Value":["ISO_IR 192"]},
          "00080016":{"vr":"UI","Value":["SOP_CLASS_UID"]},
          "00080018":{"vr":"UI","Value":["SOP_INSTANCE_UID"]},
          "0020000D":{"vr":"UI","Value":["STUDY_INSTANCE_UID"]},
          "0020000E":{"vr":"UI","Value":["SERIES_INSTANCE_UID"]},
          "00280002":{"vr":"US","Value":[3]},
          "00280004":{"vr":"CS","Value":["YBR_FULL_422"]},
          "00280006":{"vr":"US","Value":[0]},
          "00280008":{"vr":"IS","Value":[1]},
          "00280010":{"vr":"US","Value":[Rows]},
          "00280011":{"vr":"US","Value":[Columns]},
          "00280100":{"vr":"US","Value":[8]},
          "00280101":{"vr":"US","Value":[8]},
          "00280102":{"vr":"US","Value":[7]},
          "00280103":{"vr":"US","Value":[0]},
          "7FE00010":{"vr":"OB","BulkDataURI":"jpeg-image"}
         }]

  2. To create the opening (for the JSON metadata), middle (for the JPEG image), and closing boundaries, run the following commands:
         
         echo -ne "--DICOMwebBoundary\r\nContent-Type: application/dicom+json\r\n\r\n" > opening.file
         echo -ne "\r\n--DICOMwebBoundary\r\nContent-Location: jpeg-image\r\nContent-Type: image/jpeg; transfer-syntax=1.2.840.10008.1.2.4.50\r\n\r\n" > middle.file
         echo -ne "\r\n--DICOMwebBoundary--" > closing.file

  3. Wrap the JPEG image within middle and closing boundaries. The output file, which you send to the Cloud Healthcare API, is called `multipart-request.file`:
         
         cat opening.file instance.json middle.file image.jpg closing.file > multipart-request.file

  4. Make a `POST` request and specify the following information:

     * The name of the parent dataset
     * The name of the DICOM store
     * The `multipart-request.file` file
     * An access token



The following sample shows a `POST` request using `curl`.
    
    
    curl -X POST \
        -H "Content-Type: multipart/related; type=\"application/dicom+json\"; boundary=DICOMwebBoundary" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies \
        --data-binary @multipart-request.file

If the request is successful, the server returns the response in XML format:
    
    
    <NativeDicomModel>
      <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
        <Value number="1">https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID</Value>
      </DicomAttribute>
      <DicomAttribute tag="00081199" vr="SQ" keyword="ReferencedSOPSequence">
        <Item number="1">
          <DicomAttribute tag="00081150" vr="UI" keyword="ReferencedSOPClassUID">
            <Value number="1">SOP_CLASS_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081155" vr="UI" keyword="ReferencedSOPInstanceUID">
            <Value number="1">SOP_INSTANCE_UID</Value>
          </DicomAttribute>
          <DicomAttribute tag="00081190" vr="UR" keyword="RetrieveURL">
            <Value number="1">https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID</Value>
          </DicomAttribute>
        </Item>
      </DicomAttribute>
    </NativeDicomModel>
    

### Use the DICOMweb CLI

The following samples show how to use the Cloud Healthcare API DICOMweb CLI to store one or more DICOM instances. There are more samples available in the [DICOMweb CLI GitHub repository](https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli).

**Storing a single DICOM instance** :
    
    
    dcmweb \
      https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb \
      store DCM_FILE

If the request is successful, the server returns a response similar to the following sample:
    
    
    TIMESTAMP -- DCM_FILE.dcm uploaded as https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID TIMESTAMP -- INSTANCE_UID
    TIMESTAMP -- Transferred SIZE in COUNT files
    

**Storing multiple files in parallel using wildcards** :

The following sample shows how to recursively store multiple DICOM files in parallel from the current working directory. To store the files in parallel, add the `-m` flag.
    
    
    dcmweb -m \
      https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb \
      store "./**.dcm"

If the request is successful, the server returns a response similar to the following sample:
    
    
    TIMESTAMP -- DCM_FILE_1.dcm uploaded as https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID TIMESTAMP -- INSTANCE_UID
    TIMESTAMP -- DCM_FILE_2.dcm uploaded as https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID TIMESTAMP -- INSTANCE_UID
    TIMESTAMP -- DCM_FILE_3.dcm uploaded as https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID TIMESTAMP -- INSTANCE_UID
    ...
    TIMESTAMP -- Transferred SIZE in COUNT files
    

## Search for DICOM data

You can search for studies, series, instances, and frames. The following samples show an implementation of the [Search transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.6) to search for instances in a DICOM store. For more information, see [Search transaction](https://docs.cloud.google.com/healthcare-api/docs/dicom#search_transaction) in the Cloud Healthcare API DICOM conformance statement.

The following samples show how to search for instances in a DICOM store. For more information, see [`projects.locations.datasets.dicomStores.searchForInstances`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/searchForInstances).

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/instances"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/instances" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/searchForInstances). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    [
       {
          "00080005":{
             "vr":"CS",
             "Value":[
                "CODE_STRING"
             ]
          },
          "00080016":{
             "vr":"UI",
             "Value":[
                "UNIQUE_IDENTIFIER"
             ]
          },
          "00080018":{
             "vr":"UI",
             "Value":[
                "UNIQUE_IDENTIFIER"
             ]
          },
          "00080020":{
             "vr":"DA",
             "Value":[
                "DATE_TIME"
             ]
          },
          "00080030":{
             "vr":"TM",
             "Value":[
                "TIME"
             ]
          },
          "00080060":{
             "vr":"CS",
             "Value":[
                "CODE_STRING"
             ]
          },
          "0008103E":{
             "vr":"LO",
             "Value":[
                "LONG_STRING"
             ]
          },
          "00100010":{
             "vr":"PN",
             "Value":[
                {
                   "Alphabetic":"Anonymized"
                }
             ]
          },
       },
    ...
    ]
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // dicomWebSearchInstances searches instances.
    func dicomWebSearchInstances(w io.Writer, projectID, location, datasetID, dicomStoreID string) error {
    	// projectID := "my-project"
    	// location := "us-central1"
    	// datasetID := "my-dataset"
    	// dicomStoreID := "my-dicom-store"
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	resp, err := storesService.SearchForInstances(parent, "instances").Do()
    	if err != nil {
    		return fmt.Errorf("SearchForInstances: %w", err)
    	}
    
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("ioutil.ReadAll: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("SearchForInstances: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
    	}
    
    	respString := string(respBytes)
    	fmt.Fprintf(w, "Found instances: %s\n", respString)
    	return nil
    }
    

### Java
    
    
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
    
    public class DicomWebSearchForInstances {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomWebSearchForInstances(String dicomStoreName) throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        DicomStores.SearchForInstances request =
            client
                .projects()
                .locations()
                .datasets()
                .dicomStores()
                .searchForInstances(dicomStoreName, "instances");
    
        // Execute the request and process the results.
        HttpResponse response = request.executeUnparsed();
        System.out.println("Dicom store instances found: \n" + response.toString());
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
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const dicomWebSearchForInstances = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const dicomWebPath = 'instances';
      const request = {parent, dicomWebPath};
    
      const instances =
        await healthcare.projects.locations.datasets.dicomStores.searchForInstances(
          request,
          {
            headers: {Accept: 'application/dicom+json,multipart/related'},
          }
        );
      console.log(`Found ${instances.data.length} instances:`);
      console.log(JSON.stringify(instances.data));
    };
    
    dicomWebSearchForInstances();

### Python
    
    
    def dicomweb_search_instance(project_id, location, dataset_id, dicom_store_id):
        """Handles the GET requests specified in DICOMweb standard.
    
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
    
        dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/instances".format(
            url, dataset_id, dicom_store_id
        )
    
        # Sets required application/dicom+json; charset=utf-8 header on the request
        headers = {"Content-Type": "application/dicom+json; charset=utf-8"}
    
        response = session.get(dicomweb_path, headers=headers)
        response.raise_for_status()
    
        instances = response.json()
    
        print("Instances:")
        print(json.dumps(instances, indent=2))
    
        return instances
    
    

### Search using DICOM tags

You can refine your searches by appending DICOM tags to your requests in the form of query parameters. For example, you might want to search for studies containing a patient's name.

Like the preceding samples, the following samples show an implementation of the [Search transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.6) to search for studies in a DICOM store. However, these samples show how to search for studies where the patient's name is "Sally Zhang."

The following sample shows a portion of a DICOM instance's metadata where the patient's name is listed:
    
    
    ...
    {
      "vr": "PN",
      "Value": [
        {
          "Alphabetic": "Sally Zhang"
        }
      ]
    }
    ...
    

To search for studies in a DICOM store that pertain to the patient, add a query parameter to your request where you search by the `PatientName` DICOM tag. For a list of supported search parameters in the Cloud Healthcare API, see the [Search transaction](https://docs.cloud.google.com/healthcare-api/docs/dicom#search_transaction) documentation.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID



To send your request, choose one of these options:

#### curl

**Note:** Ensure you have set the [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/production) environment variable to the path for your service account private key file.

**Note:** You can add fuzzy matching when searching by `PatientName` by setting the query parameter below to `?PatientName=Sally%20Zhang&fuzzymatching=true`. Fuzzy matching performs tokenization and normalization on both the value of `PatientName` in the query and the stored value. It matches if any search token is a prefix of any stored token. For example, if `PatientName` is `Sally%20Zhang`, then `sa`, `Zh`, and `Sally^Zhang` match. However, `ally` does not match.

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies?PatientName=Sally%20Zhang"

#### PowerShell

**Note:** Ensure you have set the [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/production) environment variable to the path for your service account private key file.

**Note:** You can add fuzzy matching when searching by `PatientName` by setting the query parameter below to `?PatientName=Sally%20Zhang&fuzzymatching=true`. Fuzzy matching performs tokenization and normalization on both the value of `PatientName` in the query and the stored value. It matches if any search token is a prefix of any stored token. For example, if `PatientName` is `Sally%20Zhang`, then `sa`, `Zh`, and `Sally^Zhang` match. However, `ally` does not match.

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies?PatientName=Sally%20Zhang" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/searchForStudies). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    [
      {
        "00080005": {
          "vr": "CS",
          "Value": [
            "CODE_STRING"
          ]
        },
        "00080020": {
          "vr": "DA",
          "Value": [
            "DATE_TIME"
          ]
        },
        "00080030": {
          "vr": "TM",
          "Value": [
            "TIME"
          ]
        },
        "00080050": {
          "vr": "SH"
        },
        "00080090": {
          "vr": "PN",
          "Value": [
            {
              "Alphabetic": "VALUE"
            }
          ]
        },
        "00100010": {
          "vr": "PN",
          "Value": [
            {
              "Alphabetic": "Sally Zhang"
            }
          ]
        },
        "00100020": {
          "vr": "LO",
          "Value": [
            "VALUE"
          ]
        },
        "00100030": {
          "vr": "DA"
        },
        "00100040": {
          "vr": "CS",
          "Value": [
            "F"
          ]
        },
        "0020000D": {
          "vr": "UI",
          "Value": [
            "STUDY_INSTANCE_UID"
          ]
        },
        "00200010": {
          "vr": "SH"
        }
      }
    ]
    

### Go
    
    
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
    
    

### Use DICOM Studio

The following steps show how to use DICOM Studio to search for studies, series, and instances.

  1. In the Google Cloud console, go to the **DICOM Studio** application.

[Go to DICOM Studio](https://console.cloud.google.com/healthcare/dicom-studio)

  2. Click **Browse an existing DICOM store**. Select the DICOM store you want to search in.

  3. This will move you to the **Workbench** page. Use the filter bar to search for studies, series, or instances. You can search by DICOM tags supported by the Cloud Healthcare API.

     1. For example, to search for a patient named "Sally Zhang", you would filter by "Patient Name" (`PatientName`) and enter "Sally Zhang".
     2. For more information on supported tags, see the [DICOM conformance statement](https://docs.cloud.google.com/healthcare-api/docs/dicom#search_transaction).
  4. The results are displayed in the table. You can expand studies to see series, and expand series to see instances.

  5. You can click any of the results to view more information about them.




### Use the DICOMweb CLI

The following sample shows how to use the Cloud Healthcare API DICOMweb CLI to search for instances in a DICOM store. There are more samples, including how to filter your search, available in the [DICOMweb CLI GitHub repository](https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli).
    
    
    dcmweb \
      https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb \
      search instances

If the request is successful, the server returns the response in JSON format:
    
    
    [
       {
          "00080005":{
             "vr":"CS",
             "Value":[
                "CODE_STRING"
             ]
          },
          "00080016":{
             "vr":"UI",
             "Value":[
                "UNIQUE_IDENTIFIER"
             ]
          },
          "00080018":{
             "vr":"UI",
             "Value":[
                "UNIQUE_IDENTIFIER"
             ]
          },
          "00080020":{
             "vr":"DA",
             "Value":[
                "DATE_TIME"
             ]
          },
          "00080030":{
             "vr":"TM",
             "Value":[
                "TIME"
             ]
          },
          "00080060":{
             "vr":"CS",
             "Value":[
                "CODE_STRING"
             ]
          },
          "0008103E":{
             "vr":"LO",
             "Value":[
                "LONG_STRING"
             ]
          },
          "00100010":{
             "vr":"PN",
             "Value":[
                {
                   "Alphabetic":"Anonymized"
                }
             ]
          },
       },
    
    ...
    
    ]
    

## Retrieve DICOM data

The Cloud Healthcare API implements the [Retrieve transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.4) for retrieving studies, series, instances, and frames in a DICOM store.

For more information, see [Retrieve transaction](https://docs.cloud.google.com/healthcare-api/docs/dicom#retrieve_transaction) in the Cloud Healthcare API DICOM conformance statement.

### Retrieve a study

The following samples show how to retrieve a study. For more information, see [DICOM study/series/instances](https://docs.cloud.google.com/healthcare-api/docs/dicom#dicom_studyseriesinstances) in the Cloud Healthcare API DICOM conformance statement.

When specifying the output file, use an extension like `.multipart`. Then parse the multipart file to get the individual series and instances in the study.

For more information, see [`projects.locations.datasets.dicomStores.studies.retrieveStudy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies/retrieveStudy).

### curl

To retrieve a study, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * The name of the DICOM store
  * The study unique identifier (UID)
  * An output file
  * An access token



The following sample shows a `GET` request using `curl`.
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Accept: multipart/related; type=application/dicom; transfer-syntax=*" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID" \
         --output FILENAME.multipart

If the request is successful, the DICOM file is written to your machine.

### PowerShell

To retrieve a study, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * The name of the DICOM store
  * The study unique identifier (UID)
  * An output file
  * An access token



The following sample shows a `GET` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred"; Accept = "multipart/related; type=application/dicom; transfer-syntax=*" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID" | Select-Object -Expand Content
      -OutFile FILENAME.multipart `

If the request is successful, the DICOM file is written to your machine.

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // dicomWebRetrieveStudy retrieves all instances in the given dicomWebPath
    // study.
    func dicomWebRetrieveStudy(w io.Writer, projectID, location, datasetID, dicomStoreID, dicomWebPath string, outputFile string) error {
    	// projectID := "my-project"
    	// location := "us-central1"
    	// datasetID := "my-dataset"
    	// dicomStoreID := "my-dicom-store"
    	// dicomWebPath := "studies/1.3.6.1.4.1.11129.5.5.111396399857604"
    	// outputFile := "study.multipart"
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores.Studies
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	resp, err := storesService.RetrieveStudy(parent, dicomWebPath).Do()
    	if err != nil {
    		return fmt.Errorf("RetrieveStudy: %w", err)
    	}
    
    	defer resp.Body.Close()
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("RetrieveStudy: status %d %s: %s", resp.StatusCode, resp.Status, resp.Body)
    	}
    
    	file, err := os.Create(outputFile)
    	if err != nil {
    		return fmt.Errorf("os.Create: %w", err)
    	}
    	defer file.Close()
    	if _, err := io.Copy(file, resp.Body); err != nil {
    		return fmt.Errorf("io.Copy: %w", err)
    	}
    
    	// When specifying the output file, use an extension like ".multipart".
    	// Then, parse the downloaded multipart file to get each individual DICOM
    	// file.
    	fmt.Fprintf(w, "Study retrieved and downloaded to file: %v\n", outputFile)
    
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpHeaders](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpHeaders.html);
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.[HttpResponse](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpResponse.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.DicomStores.Studies;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.File;
    import java.io.FileOutputStream;
    import java.io.IOException;
    import java.io.OutputStream;
    import java.util.Collections;
    
    public class DicomWebRetrieveStudy {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomWebRetrieveStudy(String dicomStoreName, String studyId)
          throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
        // String studyId = "your-study-id";
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Studies.RetrieveStudy request =
            client
                .projects()
                .locations()
                .datasets()
                .dicomStores()
                .studies()
                .retrieveStudy(dicomStoreName, "studies/" + studyId);
    
        // Execute the request and process the results.
        HttpResponse response = request.executeUnparsed();
    
        // When specifying the output file, use an extension like ".multipart".
        // Then, parse the downloaded multipart file to get each individual
        // DICOM file.
        String outputPath = "study.multipart";
        OutputStream outputStream = new FileOutputStream(new File(outputPath));
        try {
          response.download(outputStream);
          System.out.println("DICOM study written to file " + outputPath);
        } finally {
          outputStream.close();
        }
    
        if (!response.isSuccessStatusCode()) {
          System.err.print(
              String.format("Exception retrieving DICOM study: %s\n", response.getStatusMessage()));
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
        // The response's default transfer syntax is Little Endian Explicit.
        // As a result, if the file was uploaded using a compressed transfer syntax,
        // the returned object will be decompressed. This can negatively impact performance and lead
        // to errors for transfer syntaxes that the Cloud Healthcare API doesn't support.
        // To avoid these issues, and if the returned object's transfer syntax doesn't matter to
        // your application, use the
        // multipart/related; type="application/dicom"; transfer-syntax=* Accept Header.
        headers.setAccept("multipart/related; type=application/dicom; transfer-syntax=*");
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
    // When specifying the output file, use an extension like ".multipart."
    // Then, parse the downloaded multipart file to get each individual
    // DICOM file.
    const fileName = 'study_file.multipart';
    
    const dicomWebRetrieveStudy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      // const studyUid = '1.3.6.1.4.1.5062.55.1.2270943358.716200484.1363785608958.61.0';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const dicomWebPath = `studies/${studyUid}`;
      const request = {parent, dicomWebPath};
    
      const study =
        await healthcare.projects.locations.datasets.dicomStores.studies.retrieveStudy(
          request,
          {
            headers: {
              Accept:
                'multipart/related; type=application/dicom; transfer-syntax=*',
            },
            responseType: 'arraybuffer',
          }
        );
    
      const fileBytes = Buffer.from(study.data);
    
      await writeFile(fileName, fileBytes);
      console.log(
        `Retrieved study and saved to ${fileName} in current directory`
      );
    };
    
    dicomWebRetrieveStudy();

### Python
    
    
    def dicomweb_retrieve_study(
        project_id, location, dataset_id, dicom_store_id, study_uid
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
        # study_uid = '1.3.6.1.4.1.5062.55.1.227'  # replace with the study UID
        url = f"{base_url}/projects/{project_id}/locations/{location}"
    
        dicomweb_path = "{}/datasets/{}/dicomStores/{}/dicomWeb/studies/{}".format(
            url, dataset_id, dicom_store_id, study_uid
        )
    
        # When specifying the output file, use an extension like ".multipart."
        # Then, parse the downloaded multipart file to get each individual
        # DICOM file.
        file_name = "study.multipart"
    
        response = session.get(dicomweb_path)
    
        response.raise_for_status()
    
        with open(file_name, "wb") as f:
            f.write(response.content)
            print(f"Retrieved study and saved to {file_name} in current directory")
    
        return response
    
    

### Retrieve an instance

The following samples show how to retrieve an instance. For more information, see [DICOM instances](https://docs.cloud.google.com/healthcare-api/docs/dicom#dicom_instances) in the Cloud Healthcare API DICOM conformance statement.

If you are retrieving an instance, you can avoid having to parse multipart boundaries by using the `Accept: application/dicom` HTTP header. Adding `transfer-syntax=*` avoids transcoding by returning the file in the format it was originally stored in.

For more information, see [`projects.locations.datasets.dicomStores.studies.series.instances.retrieveInstance`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances/retrieveInstance).

### curl

To retrieve an instance, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * The name of the DICOM store
  * The study unique identifier (UID)
  * The series UID, the instance UID
  * An output filename
  * An access token



The following sample shows a `GET` request using `curl`.
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Accept: application/dicom; transfer-syntax=*" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID" \
         --output FILENAME.dcm

If the request is successful, the DICOM file is written to your machine.

### PowerShell

To retrieve an instance, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * The name of the DICOM store
  * The study unique identifier (UID)
  * The series UID
  * The instance UID
  * An output filename
  * An access token



The following sample shows a `GET` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred"; Accept = "application/dicom; transfer-syntax=*" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID"
      -OutFile FILENAME.dcm `

If the request is successful, the DICOM file is written to your machine.

### Go
    
    
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
    
    

### Retrieve consumer image formats

The following samples show how to retrieve a consumer imaging format like JPEG or PNG using the Cloud Healthcare API implementation of [Rendered Resources](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.4.1.1.3). For more information, see [Rendered resources](https://docs.cloud.google.com/healthcare-api/docs/dicom#rendered_resources) in the Cloud Healthcare API DICOM conformance statement.

For more information, see [`projects.locations.datasets.dicomStores.studies.series.instances.retrieveRendered`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances/retrieveRendered).

**Note:** If you are rendering a multi-frame image, use the [`frames.retrieveFrames`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances.frames/retrieveFrames) method instead of the [`frames.retrieveRendered`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances.frames/retrieveRendered) method because `frames.retrieveRendered` doesn't support multi-frame images.

### curl

To retrieve an image, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * The name of the DICOM store
  * The study unique identifier (UID)
  * The series UID
  * The instance UID
  * An output filename
  * An access token



The following sample shows how to retrieve a PNG image with a `GET` request using `curl`.
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Accept: image/png" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID/rendered" \
         --output FILENAME.png

If the request is successful, the PNG file is written to your machine.

### PowerShell

To retrieve an image, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * The name of the DICOM store
  * The study unique identifier (UID)
  * The series UID
  * The instance UID
  * An output filename
  * An access token



The following sample shows how to retrieve a PNG image with a `GET` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred"; Accept = "image/png" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID/rendered"
      -OutFile FILENAME.png `

If the request is successful, the PNG file is written to your machine.

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // dicomWebRetrieveRendered retrieves a consumer imaging format like JPEG or PNG.
    func dicomWebRetrieveRendered(w io.Writer, projectID, location, datasetID, dicomStoreID, dicomWebPath string, outputFile string) error {
    	// projectID := "my-project"
    	// location := "us-central1"
    	// datasetID := "my-dataset"
    	// dicomStoreID := "my-dicom-store"
    	// dicomWebPath := "studies/1.3.6.1.4.1.11129.5.5.1113639985/series/1.3.6.1.4.1.11129.5.5.1953511724/instances/1.3.6.1.4.1.11129.5.5.9562821369/rendered"
    	// outputFile := "rendered_image.png"
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores.Studies.Series.Instances
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	call := storesService.RetrieveRendered(parent, dicomWebPath)
    	call.Header().Set("Accept", "image/png")
    	resp, err := call.Do()
    	if err != nil {
    		return fmt.Errorf("RetrieveRendered: %w", err)
    	}
    
    	defer resp.Body.Close()
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("RetrieveRendered: status %d %s: %s", resp.StatusCode, resp.Status, resp.Body)
    	}
    
    	file, err := os.Create(outputFile)
    	if err != nil {
    		return fmt.Errorf("os.Create: %w", err)
    	}
    	defer file.Close()
    	if _, err := io.Copy(file, resp.Body); err != nil {
    		return fmt.Errorf("io.Copy: %w", err)
    	}
    
    	fmt.Fprintf(w, "Rendered PNG image retrieved and downloaded to file: %v\n", outputFile)
    
    	return nil
    }
    

### Java
    
    
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
    
    public class DicomWebRetrieveRendered {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final String DICOMWEB_PATH = "studies/%s/series/%s/instances/%s/rendered";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomWebRetrieveRendered(String dicomStoreName, String dicomWebPath)
          throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
        // String dicomWebPath = String.format(DICOMWEB_PATH, "your-study-id", "your-series-id",
        // "your-instance-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Instances.RetrieveRendered request =
            client
                .projects()
                .locations()
                .datasets()
                .dicomStores()
                .studies()
                .series()
                .instances()
                .retrieveRendered(dicomStoreName, dicomWebPath);
    
        // Execute the request and process the results.
        HttpResponse response = request.executeUnparsed();
    
        String outputPath = "image.png";
        OutputStream outputStream = new FileOutputStream(new File(outputPath));
        try {
          response.download(outputStream);
          System.out.println("DICOM rendered PNG image written to file " + outputPath);
        } finally {
          outputStream.close();
        }
    
        if (!response.isSuccessStatusCode()) {
          System.err.print(
              String.format(
                  "Exception retrieving DICOM rendered image: %s\n", response.getStatusMessage()));
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
        // Retrieve using the PNG consumer imaging format.
        headers.setAccept("image/png");
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
    const fileName = 'rendered_image.png';
    
    const dicomWebRetrieveRendered = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      // const studyUid = '1.3.6.1.4.1.5062.55.1.2270943358.716200484.1363785608958.61.0';
      // const seriesUid = '2.24.52329571877967561426579904912379710633';
      // const instanceUid = '1.3.6.2.4.2.14619.5.2.1.6280.6001.129311971280445372188125744148';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const dicomWebPath = `studies/${studyUid}/series/${seriesUid}/instances/${instanceUid}/rendered`;
      const request = {parent, dicomWebPath};
    
      const rendered =
        await healthcare.projects.locations.datasets.dicomStores.studies.series.instances.retrieveRendered(
          request,
          {
            headers: {Accept: 'image/png'},
            responseType: 'arraybuffer',
          }
        );
      const fileBytes = Buffer.from(rendered.data);
    
      await writeFile(fileName, fileBytes);
      console.log(
        `Retrieved rendered image and saved to ${fileName} in current directory`
      );
    };
    
    dicomWebRetrieveRendered();

### Python
    
    
    def dicomweb_retrieve_rendered(
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
    
        dicomweb_path = "{}/dicomWeb/studies/{}/series/{}/instances/{}/rendered".format(
            dicom_store_path, study_uid, series_uid, instance_uid
        )
    
        file_name = "rendered_image.png"
    
        # Sets the required Accept header on the request for a PNG image
        headers = {"Accept": "image/png"}
        response = session.get(dicomweb_path, headers=headers)
        response.raise_for_status()
    
        with open(file_name, "wb") as f:
            f.write(response.content)
            print(
                "Retrieved rendered image and saved to {} in current directory".format(
                    file_name
                )
            )
    
        return response
    
    

### Retrieve metadata

You can retrieve the metadata for all instances in a studies or series. The following sample shows how to retrieve the metadata for an instance. For more information, see [Metadata resources](https://docs.cloud.google.com/healthcare-api/docs/dicom#metadata_resources) in the Cloud Healthcare API DICOM conformance statement.

For more information, see [`projects.locations.datasets.dicomStores.studies.series.instances.retrieveMetadata`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances/retrieveMetadata).

When you call `retrieveMetadata`, the method returns the same set of fields that are returned when you search for an instance with the `includefield=all` query parameter.

The trade-off between `retrieveMetadata` and `searchForInstances` is customizability. `retrieveMetadata` returns a consistent response with a narrow search scope. That is ideal for scenarios with high-ingestion of DICOM instances. Meanwhile, `searchForInstances` can be customized with multiple query parameter such as `includefield`. That is appropriate for scenarios that need to minimize response size by only including select fields.

By default, `retrieveMetadata` returns a JSON response. To return an XML response, pass an `Accept: multipart/related; type="application/dicom+xml"` HTTP header in your request.

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `STUDY_INSTANCE_UID`: the study instance unique identifier
  * `SERIES_INSTANCE_UID`: the series instance unique identifier
  * `INSTANCE_UID`: the instance unique identifier



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID/metadata"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID/metadata" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances/retrieveMetadata). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    [
      {
        "00020002": {
          "vr": "UI",
          "Value": [
            "UNIQUE_IDENTIFIER"
          ]
        },
        "00020003": {
          "vr": "UI",
          "Value": [
            "UNIQUE_IDENTIFIER"
          ]
        },
        "00020010": {
          "vr": "UI",
          "Value": [
            "UNIQUE_IDENTIFIER"
          ]
        },
        "00020012": {
          "vr": "UI",
          "Value": [
            "UNIQUE_IDENTIFIER"
          ]
        },
        "00020013": {
          "vr": "SH",
          "Value": [
            "OFFIS_DCMTK_"
          ]
        },
        "00080016": {
          "vr": "UI",
          "Value": [
            "UNIQUE_IDENTIFIER"
          ]
        },
        ...
      }
    ]
    

### Retrieve bulk data

A DICOM instance consists of numerous data elements. While most data elements contain small pieces of metadata (like a patient's name or a study date), some may hold large amounts of data, also called "bulkdata". To understand which data is "bulk data" in the Cloud Healthcare API, see [Bulkdata definition](https://docs.cloud.google.com/healthcare-api/docs/dicom#bulkdata-definition).

The Cloud Healthcare API processes these "bulk data" elements separately. To retrieve the raw value bytes, call [`projects.locations.datasets.dicomStores.studies.series.instances.bulkdata.retrieveBulkdata`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies.series.instances.bulkdata/retrieveBulkdata) using one of the following options:

  * **Direct retrieval** : If you know the identifiers for the study, series, instance, and the specific tag that you want to retrieve, you can construct the request URL and call `retrieveBulkdata` directly. Direct retrieval is the most efficient method because it requires only a single API call.

  * **Retrieval through DICOM instance metadata** : When you retrieve an instance's metadata, the response contains a `BulkDataURI` for each supported bulkdata tag. You can use this URI to perform a `retrieveBulkdata` request. This method is useful for discovering the available bulk data tags for an instance before retrieval.




The following samples show how to retrieve bulk data using direct retrieval:

### REST

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `STUDY_INSTANCE_UID`: the study instance unique identifier
  * `SERIES_INSTANCE_UID`: the series instance unique identifier
  * `INSTANCE_UID`: the instance unique identifier
  * `BULK_DATA_PATH`: the bulk data tag, such as `7FE00010` for `PixelData`. For a tag (AAAA,AAAA) within a sequence (BBBB,BBBB) at item index i, the path would be `BBBBBBBB/i/AAAAAAAA`
  * `OUTPUT_FILE_PATH`: a path on your local machine where the bulk data is stored in a DAT file. You must specify the `.dat` extension.



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         --output OUTPUT_FILE_PATH \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID/bulkdata/BULK_DATA_PATH"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -OutFile OUTPUT_FILE_PATH `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID/bulkdata/BULK_DATA_PATH"

If successful, the DAT file is downloaded to your local machine. 

### Use DICOM Studio

After searching for DICOM data, you can use DICOM Studio to view studies, series, instances, and their metadata.

  1. Search for the DICOM data you want to retrieve.

  2. In the results table, click a study, series, or instance to navigate to its details page.

  3. From the details page, you can do the following:

     * **View metadata** : The metadata is displayed on the details page, under the **Metadata** tab
     * **View rendered pixel data** : For a series, instances are shown inline on the **Overview** tab. For an instance, click the **Viewer** tab to see the rendered image.
     * **Navigate the hierarchy** : From a study details page, you can view a list of series in that study by clicking the **Series** tab. From a series details page, you can view a list of instances in that series by clicking the **Instances** tab.
     * **Download bulk data** : From an instance details page, you can click **Download** to get a [DICOM Part 10 binary file](https://docs.cloud.google.com/healthcare-api/docs/dicom#dicom_part_10_file_format) containing all data



### Use the DICOMweb CLI

The following sample shows how to use the Cloud Healthcare API DICOMweb CLI to retrieve all instances in a DICOM store and save them to your machine in the current working directory. There are more samples available in the [DICOMweb CLI GitHub repository](https://github.com/GoogleCloudPlatform/healthcare-api-dicomweb-cli).
    
    
    dcmweb \
      https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb \
      retrieve

If the request is successful, the server returns a response similar to the following and the DICOM files are written to your machine:
    
    
    TIMESTAMP -- Saving files into ./
    TIMESTAMP -- Transferred SIZE in COUNT files
    

## Delete a study, series, or instance

The Cloud Healthcare API implements a proprietary web service for deleting DICOM studies, series, and instances. This service is not part of the DICOMweb standard services. For more information, see the [Delete section](https://docs.cloud.google.com/healthcare-api/docs/dicom#deletion) in the Cloud Healthcare API DICOM conformance statement.

Deletion requests for studies and series return a long-running operation. After the operation completes, all instances in the study or series are deleted.

Deletion requests for instances do not return a long-running operation, instead they return an empty response body like the following:
    
    
    {}
    

The following samples show how to delete a DICOM study. For more information, see [`projects.locations.datasets.dicomStores.studies.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies/delete).

### REST

  1. Delete the study.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the DICOM store's parent dataset
     * `DICOM_STORE_ID`: the DICOM store ID
     * `STUDY_INSTANCE_UID`: the study instance unique identifier

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb/studies/STUDY_INSTANCE_UID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores.studies/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

  2. Get the status of the long-running operation.

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the DICOM store's parent dataset
     * `OPERATION_ID`: the ID returned from the long-running operation

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dicomweb.DicomWebService.DeleteStudy",
        "createTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "endTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "logsUrl": "CLOUD_LOGGING_URL",
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty",
      }
    }
    




### Go
    
    
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
    
    

### Use DICOM Studio

You can delete a study, series, or instance from its details page in DICOM Studio.

  1. Search for the study, series, or instance you want to delete.

  2. Navigate to the details page for the item you want to delete.

  3. Click the **Delete** button.

  4. Confirm the deletion in the dialog that appears.




### Use the DICOMweb CLI

The following sample shows how to use the Cloud Healthcare API DICOMweb CLI to delete a study:
    
    
    dcmweb \
        https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID/dicomWeb \
       delete studies/STUDY_INSTANCE_UID

If the request is successful, the server returns an operation which the CLI tool polls until the deletion operation completes.

## Update or patch a study, series, or instance

**Preview**  
  
This section describes Preview features that are subject to change and may have limited support. Changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see [Pre-GA Offering Terms for Cloud Healthcare API](https://cloud.google.com/healthcare-api/docs/pre-ga-terms) and the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

The [DICOMweb](https://www.dicomstandard.org/using/dicomweb) standard does not specify methods to update DICOM data, but the Cloud Healthcare API offers several methods for updating this data after ingestion. See [Update and patch DICOM studies, series, and instances](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-update-patch) for available methods and guides.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
