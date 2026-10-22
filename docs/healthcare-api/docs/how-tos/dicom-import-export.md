---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export/
title: Importing and exporting DICOM data using Cloud Storage \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:51.421950+00:00
---

# Importing and exporting DICOM data using Cloud Storage  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Importing and exporting DICOM data using Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to export DICOM instances to and import DICOM objects from Cloud Storage. A _DICOM instance_ is typically an image, but can be another type of persistent data such as a structured report. A [_DICOM object_](https://docs.cloud.google.com/storage/docs/objects) in Cloud Storage is a DICOM instance that resides in Cloud Storage. For more information, see [Cloud Storage](https://docs.cloud.google.com/storage).

## Setting Cloud Storage permissions

Before exporting and importing DICOM data to and from Cloud Storage, you must grant extra permissions to the **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts). For more information, see [DICOM store Cloud Storage permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#dicom_store_cloud_storage_permissions).

## Importing DICOM objects

To import several DICOM instance files to a DICOM store, you can use any of the following methods:

  * Programmatically [store the data directly in a DICOM store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#storing_dicom_data) from your local machine using the [Store Transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.5) RESTful web service as implemented in the Cloud Healthcare API.
  * [Upload the DICOM data in a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/uploading-objects#uploading-an-object) and then import the files into a DICOM store using a single import operation as explained in this section.



The following samples show how to import DICOM objects from a Cloud Storage bucket.

**Note:** To store a DICOM instance directly, such as from your local machine, [store the DICOM data](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#store-dicom) using the [Store Transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.5) RESTful web service as implemented in the Cloud Healthcare API.

### Console

To import DICOM objects from a Cloud Storage bucket, complete the following steps:

  1. In the Google Cloud console, go to the **Datasets** page.  
[Go to Datasets](https://console.cloud.google.com/healthcare/browser)
  2. Click the dataset that contains the DICOM store to which you are importing DICOM objects.
  3. In the list of data stores, choose **Import** from the **Actions** list for the DICOM store.  
  
The **Import to DICOM store** page appears.
  4. In the **Project** list, select a Cloud Storage project.
  5. In the **Location** list, select a Cloud Storage bucket.
  6. To set a specific location for importing files, do the following: 
     1. Expand **Advanced Options**.
     2. Select **Override Cloud Storage Path**.
     3. To set a specific source for importing files, define the path using the following variables in the **Location** text box: 
        * `*` \- matches non-separator characters.
        * `**` \- matches characters, including separators. This can be used with a file name extension to match all files of the same type.
        * `?` \- matches 1 character.
  7. Click **Import** to import DICOM objects from the defined source.
  8. To track the status of the operation, click the **Operations** tab. After the operation completes, the following indications appear: 
     * The **Long-running operation status** section has a green check mark under the **OK** heading.
     * The **Overview** section has a green check mark and an **OK** indicator in the same row as the operation ID.
If you encounter any errors, click **Actions** , and then click **View details in Cloud Logging**. 



### gcloud

To import DICOM objects from a Cloud Storage bucket, use the [`gcloud healthcare dicom-stores import gcs`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/import/gcs) command. Specify the name of the parent dataset, the name of the DICOM store, and the location of the object in a Cloud Storage bucket.

  * The location of the files within the bucket is arbitrary and does not have to adhere exactly to the format specified in the following sample.
  * When specifying the location of the DICOM objects in Cloud Storage, you can use wildcards to import multiple files from one or more directories. The following wildcards are supported: 
    * Use `*` to match 0 or more non-separator characters. For example, `gs://BUCKET/DIRECTORY/Example*.dcm` matches Example.dcm and Example22.dcm in DIRECTORY.
    * Use `**` to match 0 or more characters (including separators). Must be used at the end of a path and with no other wildcards in the path. Can also be used with a filename extension (such as .dcm), which imports all files with the filename extension in the specified directory and its subdirectories. For example, `gs://BUCKET/DIRECTORY/**.dcm` imports all files with the .dcm filename extension in DIRECTORY and its subdirectories. 
    * Use `?` to match 1 character. For example, `gs://BUCKET/DIRECTORY/Example?.dcm` matches Example1.dcm but does not match Example.dcm or Example01.dcm. 



The following sample shows how to import DICOM objects from a Cloud Storage bucket.
    
    
    gcloud healthcare dicom-stores import gcs DICOM_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION \
      --gcs-uri=gs://BUCKET/DIRECTORY/DICOM_INSTANCE.dcm

The command line displays the operation ID:
    
    
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID
    

To view the status of the operation, run the [`gcloud healthcare operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations/describe) command and provide OPERATION_ID from the response:
    
    
    gcloud healthcare operations describe OPERATION_ID \
      --location=LOCATION \
      --dataset=DATASET_ID

After the command completes, the response includes `done: true`.
    
    
    done: true
    metadata:
    '@type': type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata
    apiMethodName: google.cloud.healthcare.v1.dicom.DicomService.ImportDicomData
    counter:
      success: SUCCESSFUL_INSTANCES
      failure: FAILED_INSTANCES
    createTime: "CREATE_TIME"
    endTime: "END_TIME"
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID
    response:
    '@type': "..."
    

### API

To import DICOM objects from a Cloud Storage bucket, use the [`projects.locations.datasets.dicomStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/import) method.

  * The location of the files within the bucket can vary and doesn't have to match the format specified in the following samples.
  * When specifying the location of the DICOM objects in Cloud Storage, use wildcards to import multiple files from one or more directories. The following wildcards are supported: 
    * Use `*` to match 0 or more non-separator characters. For example, `gs://BUCKET/DIRECTORY/Example*.dcm` matches Example.dcm and Example22.dcm in DIRECTORY.
    * Use `**` to match 0 or more characters (including separators). Must be used at the end of a path and with no other wildcards in the path. Can also be used with a filename extension (such as .dcm), which imports all files with the filename extension in the specified directory and its subdirectories. For example, `gs://BUCKET/DIRECTORY/**.dcm` imports all files with the .dcm filename extension in DIRECTORY and its subdirectories. 
    * Use `?` to match 1 character. For example, `gs://BUCKET/DIRECTORY/Example?.dcm` matches Example1.dcm but does not match Example.dcm or Example01.dcm. 



### REST

  1. Import the DICOM object. 

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the DICOM store's parent dataset
     * `DICOM_STORE_ID`: the DICOM store ID
     * `BUCKET/PATH/TO/FILE`: the path to the DICOM object in Cloud Storage

Request JSON body: 
    
    {
      "gcsSource": {
        "uri": "gs://BUCKET/PATH/TO/FILE.dcm"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "gcsSource": {
        "uri": "gs://BUCKET/PATH/TO/FILE.dcm"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "gcsSource": {
        "uri": "gs://BUCKET/PATH/TO/FILE.dcm"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:import" | Select-Object -Expand Content

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations). Long-running operations are returned when method calls might take a substantial amount of time to complete. Note the value of OPERATION_ID. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

  2. Get the status of the long-running operation. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * LOCATION: the dataset location
     * DATASET_ID: the DICOM store's parent dataset
     * OPERATION_ID: the ID returned from the long-running operation

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

If the long-running operation is still running, the server returns a response with the number of DICOM instances pending import. When the LRO finishes successfully, the server returns a response with the status of the operation in JSON format: 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dicom.DicomService.ImportDicomData",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL,
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.dicom.ImportDicomDataResponse"
      }
    }
    




### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // importDICOMInstance imports DICOM objects from GCS.
    func importDICOMInstance(w io.Writer, projectID, location, datasetID, dicomStoreID, contentURI string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	req := &healthcare.ImportDicomDataRequest{
    		GcsSource: &healthcare.GoogleCloudHealthcareV1DicomGcsSource{
    			Uri: contentURI,
    		},
    	}
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	lro, err := storesService.Import(name, req).Do()
    	if err != nil {
    		return fmt.Errorf("Import: %w", err)
    	}
    
    	fmt.Fprintf(w, "Import to DICOM store started. Operation: %q\n", lro.Name)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.DicomStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.GoogleCloudHealthcareV1DicomGcsSource;
    import com.google.api.services.healthcare.v1.model.ImportDicomDataRequest;
    import com.google.api.services.healthcare.v1.model.Operation;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class DicomStoreImport {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomStoreImport(String dicomStoreName, String gcsUri) throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
        // String gcsUri = "gs://your-bucket-id/path/to/destination/dir"
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure where the store should be imported from.
        GoogleCloudHealthcareV1DicomGcsSource gcsSource =
            new GoogleCloudHealthcareV1DicomGcsSource().setUri(gcsUri);
        ImportDicomDataRequest importRequest = new ImportDicomDataRequest().setGcsSource(gcsSource);
    
        // Create request and configure any parameters.
        DicomStores.CloudHealthcareImport request =
            client
                .projects()
                .locations()
                .datasets()
                .dicomStores()
                .healthcareImport(dicomStoreName, importRequest);
    
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
          System.out.println("DICOM store import complete." + operation.getResponse());
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
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    const sleep = ms => {
      return new Promise(resolve => setTimeout(resolve, ms));
    };
    
    const importDicomInstance = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      // const gcsUri = 'my-bucket/my-directory/*.dcm'
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const request = {
        name,
        resource: {
          // The location of the DICOM instances in Cloud Storage
          gcsSource: {
            uri: `gs://${gcsUri}`,
          },
        },
      };
    
      const operation =
        await healthcare.projects.locations.datasets.dicomStores.import(request);
      const operationName = operation.data.name;
    
      const operationRequest = {name: operationName};
    
      // Wait fifteen seconds for the LRO to finish.
      await sleep(15000);
    
      // Check the LRO's status
      const operationStatus =
        await healthcare.projects.locations.datasets.operations.get(
          operationRequest
        );
    
      const {data} = operationStatus;
    
      if (data.error === undefined) {
        console.log('Successfully imported DICOM instances');
      } else {
        console.log('Encountered errors. Sample error:');
        console.log(
          'Resource on which error occurred:',
          data.error.details[0]['sampleErrors'][0]['resource']
        );
        console.log(
          'Error code:',
          data.error.details[0]['sampleErrors'][0]['error']['code']
        );
        console.log(
          'Error message:',
          data.error.details[0]['sampleErrors'][0]['error']['message']
        );
      }
    };
    
    importDicomInstance();

### Python
    
    
    def import_dicom_instance(
        project_id, location, dataset_id, dicom_store_id, content_uri
    ):
        """Imports data into the DICOM store by copying it from the specified
        source.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/dicom
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
        # dataset_id = 'my-dataset'  # replace with the DICOM store's parent dataset ID
        # dicom_store_id = 'my-dicom-store'  # replace with the DICOM store's ID
        # content_uri = 'my-bucket/*.dcm'  # replace with a Cloud Storage bucket and DCM files
        dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        dicom_store_name = f"{dicom_store_parent}/dicomStores/{dicom_store_id}"
    
        body = {"gcsSource": {"uri": f"gs://{content_uri}"}}
    
        # Escape "import()" method keyword because "import"
        # is a reserved keyword in Python
        request = (
            client.projects()
            .locations()
            .datasets()
            .dicomStores()
            .import_(name=dicom_store_name, body=body)
        )
    
        response = request.execute()
        print(f"Imported DICOM instance: {content_uri}")
    
        return response
    
    

To retrieve a single instance or study from a DICOM store, [retrieve DICOM data](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#retrieving_dicom_data) using the [Retrieve Transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.4) RESTful web service as implemented in the Cloud Healthcare API.

### Specify a storage class to import DICOM objects (Preview)

**Preview**  
  
This section describes Preview features that are subject to change and may have limited support. Changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see [Pre-GA Offering Terms for Cloud Healthcare API](https://cloud.google.com/healthcare-api/docs/pre-ga-terms) and the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

By default, the `projects.locations.datasets.dicomStores.import` method imports a DICOM object to a DICOM store with a standard storage class. You can set the storage class when you import DICOM objects from Cloud Storage. For more information, see [Change DICOM storage class](https://docs.cloud.google.com/healthcare-api/docs/dicom-storage-class).

The following samples show how to specify the storage class when you import DICOM objects from Cloud Storage.

### REST

Use the [`projects.locations.datasets.dicomStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.dicomStores/import) method.

  1. Import the DICOM object. 

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: the ID of your Google Cloud project
     * `LOCATION`: the dataset location
     * `DATASET_ID`: the DICOM store's parent dataset
     * `DICOM_STORE_ID`: the DICOM store ID
     * `BUCKET/PATH/TO/FILE`: the path to the DICOM object in Cloud Storage
     * `STORAGE_CLASS`: the storage class for the DICOM object in the DICOM store from `STANDARD`,`NEARLINE`, `COLDLINE`, and `ARCHIVE`

Request JSON body: 
    
    {
      "gcsSource": {
        "uri": "gs://BUCKET/PATH/TO/FILE.dcm"
      },
      "blob_storage_settings": {
        "blob_storage_class": "STORAGE_CLASS"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    cat > request.json << 'EOF'
    {
      "gcsSource": {
        "uri": "gs://BUCKET/PATH/TO/FILE.dcm"
      },
      "blob_storage_settings": {
        "blob_storage_class": "STORAGE_CLASS"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:import"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    @'
    {
      "gcsSource": {
        "uri": "gs://BUCKET/PATH/TO/FILE.dcm"
      },
      "blob_storage_settings": {
        "blob_storage_class": "STORAGE_CLASS"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:import" | Select-Object -Expand Content

The output is the following. The response contains an identifier for a [long-running operation](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.operations). Long-running operations are returned when method calls might take a substantial amount of time to complete. Note the value of OPERATION_ID. You need this value in the next step. 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

  2. Get the status of the long-running operation. 

Before using any of the request data, make the following replacements: 

     * PROJECT_ID: the ID of your Google Cloud project
     * LOCATION: the dataset location
     * DATASET_ID: the DICOM store's parent dataset
     * OPERATION_ID: the ID returned from the long-running operation

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the long-running operation is still running, the server returns a response with the number of DICOM instances pending import. When the LRO finishes, the server returns a response with the status of the operation in JSON format: 

#### Response
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1beta1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1beta1.dicom.DicomService.ImportDicomData",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL,
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1beta1.dicom.ImportDicomDataResponse"
      }
    }
    




### Troubleshooting DICOM import requests

If errors occur during a DICOM import request, the errors are logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

## Exporting DICOM instances

The following samples show how to export DICOM instances to a Cloud Storage bucket. When you export DICOM instances from a DICOM store, all instances in the store are exported.

**Note:** To retrieve a single instance or study from a DICOM store, [retrieve DICOM data](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb#retrieve-dicom) using the [Retrieve Transaction](https://dicom.nema.org/medical/dicom/current/output/html/part18.html#sect_10.4) RESTful web service as implemented in the Cloud Healthcare API.

### Console

To export DICOM instances to Cloud Storage, complete the following steps:

  1. In the Google Cloud console, go to the **Datasets** page.  
[Go to Datasets](https://console.cloud.google.com/healthcare/browser)
  2. Click the dataset that contains the DICOM store from which you are exporting DICOM instances.
  3. In the list of data stores, choose **Export** from the **Actions** list for the DICOM store.
  4. On the **Export DICOM Store** page that appears, select **Google Cloud Storage Bucket**.
  5. In the **Project** list, select a Cloud Storage project.
  6. In the **Location** list, select a Cloud Storage bucket.
  7. In **DICOM Export Settings** , select the file type used to export the DICOM instances. The following types are available: 
     * DICOM file (`.dcm`)
     * octet-stream
     * Image (`.jpg`, `.png`) 
  8. To define additional transfer syntax, choose the syntax from the **Transfer Syntax** list.
  9. Click **Export** to export DICOM instances to the defined location in Cloud Storage.
  10. To track the status of the operation, click the **Operations** tab. After the operation completes, the following indications appear: 
     * The **Long-running operation status** section has a green check mark under the **OK** heading.
     * The **Overview** section has a green check mark and an **OK** indicator in the same row as the operation ID.
If you encounter any errors, click **Actions** , and then click **View details in Cloud Logging**. 



### gcloud

To export DICOM instances to a Cloud Storage bucket, use the [`gcloud healthcare dicom-stores export gcs`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/export/gcs) command.

  * Provide the name of the parent dataset, the name of the DICOM store, and the destination Cloud Storage bucket.
  * Write to a Cloud Storage bucket or directory, rather than an object, because the Cloud Healthcare API creates one `.dcm` file for each object.
  * If the command specifies a directory that does not exist, the directory is created.



The following sample shows the `gcloud healthcare dicom-stores export gcs` command.
    
    
    gcloud healthcare dicom-stores export gcs DICOM_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION \
      --gcs-uri-prefix=gs://BUCKET/DIRECTORY

The command line displays the operation ID:
    
    
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID
    

To view the status of the operation, run the [`gcloud healthcare operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations/describe) command and provide OPERATION_ID from the response:
    
    
    gcloud healthcare operations describe OPERATION_ID \
      --location=LOCATION \
      --dataset=DATASET_ID

After the command completes, the response includes `done: true`.
    
    
    done: true
    metadata:
    '@type': type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata
    apiMethodName: google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData
    counter:
      success: SUCCESSFUL_INSTANCES
      failure: FAILED_INSTANCES
    createTime: "CREATE_TIME"
    endTime: "END_TIME"
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID
    response:
    '@type': "..."
    

### API

To export DICOM instances to a Cloud Storage bucket, use the [`projects.locations.datasets.dicomStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export) method.

  * Write to a Cloud Storage bucket or directory, rather than an object, because the Cloud Healthcare API creates one `.dcm` file for each DICOM object.
  * If the command specifies a directory that does not exist, the directory is created.



### curl

To export DICOM instances, make a `POST` request and provide the following information:

  * The name and location of the parent dataset
  * The name of the DICOM store
  * The destination Cloud Storage bucket



The following sample shows a `POST` request using `curl`.
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'gcsDestination': {
            'uriPrefix': 'gs://BUCKET/DIRECTORY'
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:export"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns a response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter":{
           "success": SUCCESSFUL_INSTANCES
           "failure": FAILED_INSTANCES
        }
      },
      "done": true,
      "response": {
        "@type": "..."
      }
    }
    

### PowerShell

To export DICOM instances, make a `POST` request and provide the following information:

  * The name and location of the parent dataset
  * The name of the DICOM store
  * The destination Cloud Storage bucket



The following sample shows a `POST` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'gcsDestination': {
          'uriPrefix': 'gs://BUCKET/DIRECTORY'
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:export" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns a response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter":{
           "success": SUCCESSFUL_INSTANCES
           "failure": FAILED_INSTANCES
        },
      },
      "done": true,
      "response": {
        "@type": "..."
      }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // exportDICOMInstance exports DICOM objects to GCS.
    func exportDICOMInstance(w io.Writer, projectID, location, datasetID, dicomStoreID, destination string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	req := &healthcare.ExportDicomDataRequest{
    		GcsDestination: &healthcare.GoogleCloudHealthcareV1DicomGcsDestination{
    			UriPrefix: destination, // "gs://my-bucket/path/to/prefix/"
    		},
    	}
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	lro, err := storesService.Export(name, req).Do()
    	if err != nil {
    		return fmt.Errorf("Export: %w", err)
    	}
    
    	fmt.Fprintf(w, "Export to DICOM store started. Operation: %q\n", lro.Name)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.DicomStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.ExportDicomDataRequest;
    import com.google.api.services.healthcare.v1.model.GoogleCloudHealthcareV1DicomGcsDestination;
    import com.google.api.services.healthcare.v1.model.Operation;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class DicomStoreExport {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomStoreExport(String dicomStoreName, String gcsUri) throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
        // String gcsUri = "gs://your-bucket-id/path/to/destination/dir"
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure where the store will be exported too.
        GoogleCloudHealthcareV1DicomGcsDestination gcsDestination =
            new GoogleCloudHealthcareV1DicomGcsDestination().setUriPrefix(gcsUri);
        ExportDicomDataRequest exportRequest =
            new ExportDicomDataRequest().setGcsDestination(gcsDestination);
    
        // Create request and configure any parameters.
        DicomStores.Export request =
            client
                .projects()
                .locations()
                .datasets()
                .dicomStores()
                .export(dicomStoreName, exportRequest);
    
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
          System.out.println("DICOM store export complete." + operation.getResponse());
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
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const exportDicomInstanceGcs = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      // const gcsUri = 'my-bucket/my-directory'
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const request = {
        name,
        resource: {
          gcsDestination: {
            // The destination location of the DICOM instances in Cloud Storage
            uriPrefix: `gs://${gcsUri}`,
            // The format to use for the output files, per the MIME types supported in the DICOM spec
            mimeType: 'application/dicom',
          },
        },
      };
    
      await healthcare.projects.locations.datasets.dicomStores.export(request);
      console.log(`Exported DICOM instances to ${gcsUri}`);
    };
    
    exportDicomInstanceGcs();

### Python
    
    
    def export_dicom_instance(project_id, location, dataset_id, dicom_store_id, uri_prefix):
        """Export data to a Google Cloud Storage bucket by copying
        it from the DICOM store.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/dicom
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
        # dataset_id = 'my-dataset'  # replace with the DICOM store's parent dataset ID
        # dicom_store_id = 'my-dicom-store'  # replace with the DICOM store's ID
        # uri_prefix = 'my-bucket'  # replace with a Cloud Storage bucket
        dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        dicom_store_name = f"{dicom_store_parent}/dicomStores/{dicom_store_id}"
    
        body = {"gcsDestination": {"uriPrefix": f"gs://{uri_prefix}"}}
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .dicomStores()
            .export(name=dicom_store_name, body=body)
        )
    
        response = request.execute()
        print(f"Exported DICOM instances to bucket: gs://{uri_prefix}")
    
        return response
    
    

## Exporting DICOM instances using filters

By default, when you export DICOM files to Cloud Storage all the DICOM files in the DICOM store are exported. Similarly, when you export DICOM metadata to BigQuery, the metadata for all of the DICOM data in the DICOM store is exported.

You can export a subset of DICOM data or metadata using a _filter file_.

### Configure a filter file

  * Each line in the filter file defines the study, series, or instance and uses the format `/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID/instances/INSTANCE_UID`.
  * You can truncate a line to specify the level at which the filter works. For example, you can select an entire study by specifying `/studies/STUDY_INSTANCE_UID`, or you can select an entire series by specifying `/studies/STUDY_INSTANCE_UID/series/SERIES_INSTANCE_UID`.



Consider the following filter file:
    
    
    /studies/1.123.456.789
    /studies/1.666.333.111/series/123.456
    /studies/1.666.333.111/series/567.890
    /studies/1.888.999.222/series/123.456/instances/111
    /studies/1.888.999.222/series/123.456/instances/222
    /studies/1.888.999.222/series/123.456/instances/333
    

This example filter file applies to the following:

  * The entire study with the study instance UID as `1.123.456.789`
  * Two separate series with series instance UIDs as `123.456` and `567.890` in the study `1.666.333.111`
  * Three individual instances with instance IDs as `111`, `222`, and `333` in the study `1.888.999.222` and series `123.456`



### Create a filter file using BigQuery

To create a filter file using BigQuery, you must first [export the metadata of your DICOM store to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-export-bigquery). The exported metadata shows you the study, series, and instance UIDs of the DICOM data in your DICOM store.

After exporting the metadata, complete the following steps:

  1. Run a query to return the UIDs of the study, series, and instances you want to add to the filter file.

For example, the following query shows how to concatenate the study, series, and instance UIDs to match the filter file format requirements:
         
         SELECT CONCAT
             ('/studies/', StudyInstanceUID, '/series/', SeriesInstanceUID, '/instances/', SOPInstanceUID)
         FROM
             [PROJECT_ID:BIGQUERY_DATASET.BIGQUERY_TABLE]

  2. Optional: If the query returns a large result set that exceed the [maximum response size](https://docs.cloud.google.com/bigquery/quotas#query_jobs), [save the query results to a new destination table](https://docs.cloud.google.com/bigquery/docs/writing-results#large-results) in BigQuery.

  3. Save the query results to a file and export it to Cloud Storage. If you saved your query results to a new destination table in Step 2, see [Exporting table data](https://docs.cloud.google.com/bigquery/docs/exporting-data) to export the table's contents to Cloud Storage.

  4. Edit the exported file as necessary, and include it your request to change the storage class of multiple DICOM objects.




### Create a filter file manually

To create a filter file manually, do the following:

  1. Create a filter file containing the DICOM objects you're filtering on.
  2. Upload the filter file to Cloud Storage. For instructions, see [Upload objects from a file system](https://docs.cloud.google.com/storage/docs/uploading-objects).



### Passing in the filter file

After you create a filter file, call the DICOM export operation and pass in the filter file using the REST API. The following samples show how to export DICOM data using a filter.

### gcloud

To export DICOM metadata to Cloud Storage using a filter, use the [`gcloud beta healthcare dicom-stores export gcs`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/healthcare/dicom-stores/export/gcs) command:
    
    
    gcloud beta healthcare dicom-stores export gcs DICOM_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION \
      --gcs-uri-prefix=gs://DESTINATION_BUCKET/DIRECTORY \
      --filter-config-gcs-uri=gs://BUCKET/DIRECTORY/FILTER_FILE

Replace the following:

  * DICOM_STORE_ID: the identifier for the DICOM store
  * DATASET_ID: the name of the DICOM store's parent dataset
  * LOCATION: the location of the DICOM store's parent dataset
  * DESTINATION_BUCKET/DIRECTORY: the destination Cloud Storage bucket
  * BUCKET/DIRECTORY/FILTER_FILE: the location of the filter file in a Cloud Storage bucket



The output is the following:
    
    
    Request issued for: [DICOM_STORE_ID]
    Waiting for operation [projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID] to complete...done.
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID
    

To view the status of the operation, run the [`gcloud healthcare operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations/describe) command and provide OPERATION_ID from the response:
    
    
    gcloud healthcare operations describe OPERATION_ID \
      --location=LOCATION \
      --dataset=DATASET_ID

Replace the following:

  * OPERATION_ID: the ID number returned from the previous response
  * DATASET_ID: the name of the DICOM store's parent dataset
  * LOCATION: the location of the DICOM store's parent dataset



The output is the following:
    
    
    done: true
    metadata:
    '@type': type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata
    apiMethodName: google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData
    counter:
      success: SUCCESSFUL_INSTANCES
      failure: FAILED_INSTANCES
    createTime: 'CREATE_TIME'
    endTime: 'END_TIME'
    logsUrl: 'https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL'
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID
    response:
    '@type': '...'
    

### API

To export DICOM data using a filter, use the [`projects.locations.datasets.dicomStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/export) method.

### curl

To export DICOM data using a filter file, make a `POST` request and provide the following information:

  * The name and location of the parent dataset
  * The name of the DICOM store
  * The destination Cloud Storage bucket
  * The location of the filter file in a Cloud Storage bucket



The following sample shows a `POST` request using `curl`.
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'gcsDestination': {
            'uriPrefix': 'gs://BUCKET/DIRECTORY'
          },
          'filterConfig': {
            'resourcePathsGcsUri': 'gs://BUCKET/DIRECTORY/FILTER_FILE'
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:export"

If the request is successful, the server returns the following response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. Use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation:
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DATASET_ID/operations/OPERATION_NAME"

If the request is successful, the server returns the following response with in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME"
      },
      "done": true,
      "response": {
        "@type": "..."
      }
    }
    

### PowerShell

To export DICOM data using a filter file, make a `POST` request and provide the following information:

  * The name and location of the parent dataset
  * The name of the DICOM store
  * The destination Cloud Storage bucket
  * The location of the filter file in a Cloud Storage bucket



The following sample shows a `POST` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'gcsDestination': {
          'uriPrefix': 'gs://BUCKET/DIRECTORY'
        },
        'filterConfig': {
          'resourcePathsGcsUri': 'gs://BUCKET/DIRECTORY/FILTER_FILE'
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:export" | Select-Object -Expand Content

If the request is successful, the server returns the following response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. Use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get) to track the status of the operation:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/DATASET_ID/operations/OPERATION_NAME" | Select-Object -Expand Content

If the request is successful, the server returns the following response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/REGION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.dicom.DicomService.ExportDicomData",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME"
      },
      "done": true,
      "response": {
        "@type": "..."
      }
    }
    

## Troubleshooting DICOM export requests

If errors occur during a DICOM export request, the errors are logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

If the entire operation returns an error, see [Troubleshooting long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
