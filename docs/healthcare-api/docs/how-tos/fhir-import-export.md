---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export/
title: Import and export FHIR resources using Cloud Storage \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:31.645558+00:00
---

# Import and export FHIR resources using Cloud Storage  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Import and export FHIR resources using Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to export and import FHIR resources to and from Cloud Storage using the [`projects.locations.datasets.fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import) and [`projects.locations.datasets.fhirStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export) methods.

Depending on the format of your FHIR data, to load data into a FHIR store, you could use the [`projects.locations.datasets.fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import) method or the [`projects.locations.datasets.fhirStores.fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle) method. For guidance in choosing a method, see [FHIR import](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-import).

**Note:** To work with [Synthea™ Synthetic Patient Generation](https://synthetichealth.github.io/synthea/), complete the steps in Generating simulated patient data.

## Setting Cloud Storage permissions

Before exporting and importing FHIR resources to and from Cloud Storage, you must grant additional permissions to the **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts). For more information, see [FHIR store Cloud Storage permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#fhir_store_cloud_storage_permissions).

## Generating simulated patient data

Synthea™ is a simulator for generating patient population data. If you aren't using Synthea™ to generate patient population data, skip to Importing FHIR resources or Exporting FHIR resources.

You can only import data in the version your FHIR store is configured to accept.

To download and install Synthea™, complete the following steps:

  1. Clone the Synthea™ tool repository from GitHub:
         
         git clone https://github.com/synthetichealth/synthea.git
         

  2. Complete the [installation steps](https://github.com/synthetichealth/synthea#installation).




Continue to one of the following sections to generate data for a specific FHIR version:

  * R4
  * DSTU2 and STU3



### Generating simulated patient data for R4

By default, generated Synthea™ data uses the FHIR R4 JSON representation for resources. To generate Synthea™ FHIR R4 data and import it into a Cloud Healthcare API FHIR store, complete the following steps:

  1. Follow the instructions to [generate synthetic patient data](https://github.com/synthetichealth/synthea#generate-synthetic-patients). The generated data outputs to the `synthea/output/fhir_r4` for FHIR R4.

  2. Copy the generated data to a Cloud Storage bucket so that you can import it into a Cloud Healthcare API FHIR store. For example, to copy the data to a directory called `synthea-data` in an existing Cloud Storage bucket, run the following [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command from the `synthea` directory:
         
         gcloud storage cp output/fhir_r4/* gs://BUCKET/synthea-data

  3. Follow the instructions for importing FHIR resources.




### Generating simulated patient data for DSTU2 or STU3

To generate Synthea™ FHIR DSTU2 or STU3 data and import it into a Cloud Healthcare API FHIR store, complete the following steps:

  1. From the `synthea` directory, use a text editor to open the `src/main/resources/synthea.properties` file and then make the following changes, depending on whether you are generating DSTU2 or STU3 data.

To generate FHIR STU3 data:

     * Set all `*.fhir.export` and `*.fhir_dstu2.export` values to `false`
     * Set all `*.fhir_stu3.export` values to true

To generate FHIR DSTU2 data:

     * Set all `*.fhir.export` and `*.fhir_stu3.export` values to `false`
     * Set all `*.fhir_dstu2.export` values to true

For example, to generate FHIR STU3 data:
    
    exporter.fhir.export = false
    **exporter.fhir_stu3.export = true**
    exporter.fhir_dstu2.export = false
    
    exporter.hospital.fhir.export = false
    **exporter.hospital.fhir_stu3.export = true**
    exporter.hospital.fhir_dstu2.export = false
    
    exporter.practitioner.fhir.export = false
    **exporter.practitioner.fhir_stu3.export = true**
    exporter.practitioner.fhir_dstu2.export = false

  2. Follow the instructions to [generate synthetic patient data](https://github.com/synthetichealth/synthea#generate-synthetic-patients). The generated data outputs to the `synthea/output/fhir_stu3` for FHIR STU3 or the `synthea/output/fhir_dstu2` directory for FHIR DSTU2.

  3. Copy the generated data to a Cloud Storage bucket so that you can import it into a Cloud Healthcare API FHIR store. For example, to copy the data to a directory called `synthea-data` in an existing Cloud Storage bucket, run the following [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command from the `synthea` directory:
         
         gcloud storage cp output/fhir_stu3/* gs://BUCKET/synthea-data

  4. Follow the instructions for importing FHIR resources.




## Importing FHIR resources

When configuring the body of the import request, set the [`ContentStructure`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import#contentstructure) to one of the following values:

  * `CONTENT_STRUCTURE_UNSPECIFIED`
  * `BUNDLE`: The source file contains one or more lines of newline-delimited JSON (ndjson). Each line is a bundle, which contains one or more resources. If you don't specify `ContentStructure`, it defaults to `BUNDLE`.
  * `RESOURCE`: The source file contains one or more lines of newline-delimited JSON (ndjson). Each line is a single resource.
  * `BUNDLE_PRETTY`: The entire source file is one JSON bundle. The JSON can span multiple lines.
  * `RESOURCE_PRETTY`: The entire source file is one JSON resource. The JSON can span multiple lines.



For example, suppose that you are importing a file named `resources.ndjson` with the following content:
    
    
    {"class":{"code":"IMP","display":"inpatient encounter","system":"http://hl7.org/fhir/v3/ActCode"},"id":"6090e773-3e91-40a7-8fce-1e22f6774c29","reason":[{"text":"The patient had an abnormal heart rate. She was concerned about this."}],"resourceType":"Encounter","status":"finished","subject":{"reference":"Patient/2938bb9e-1f16-429e-8d44-9508ab0e4151"}}
    {"class":{"code":"IMP","display":"inpatient encounter","system":"http://hl7.org/fhir/v3/ActCode"},"id":"7101f884-4f02-51b8-9gdf-2f33g7885d30","reason":[{"text":"The patient was experiencing recurrent fevers."}],"resourceType":"Encounter","status":"finished","subject":{"reference":"Patient/3049cc0f-2g27-530f-9e55-0619bc1f5262"}}
    {"birthDate":"1970-01-01","gender":"female","id":"2938bb9e-1f16-429e-8d44-9508ab0e4151","name":[{"family":"Smith","given":["Darcy"],"use":"official"}],"resourceType":"Patient"}
    

The file contains two Encounter resources and one Patient resource. Each resource is on a separate line, so you set `ContentStructure` to `RESOURCE`.

Your data might import incorrectly or not import at all if `ContentStructure` does not match the format of your data. For example, the sample file above will not import correctly unless `ContentStructure` is set to `RESOURCE` in the import request.

**Important:** FHIR stores only support the UTF-8 character set. Resources will be rejected if they contain any characters not in the UTF-8 character set.

The following samples show how to import FHIR resources from a Cloud Storage bucket.

### Console

To import FHIR resources from a Cloud Storage bucket, complete the following steps:

  1. In the Google Cloud console, go to the **Datasets** page.  
[Go to Datasets](https://console.cloud.google.com/healthcare/browser)
  2. Click the dataset that contains the FHIR store to which you are importing FHIR resources.
  3. In the list of data stores, choose **Import** from the **Actions** list for the FHIR store.  
  
The **Import to FHIR store** page appears.
  4. In the **Project** list, select a Cloud Storage project.
  5. In the **Location** list, select a Cloud Storage bucket.
  6. In **FHIR import settings** , select the relevant content structure.
  7. Click **Import** to import FHIR resources.
  8. To track the status of the operation, click the **Operations** tab. After the operation completes, the following indications appear: 
     * The **Long-running operation status** section has a green check mark under the **OK** heading.
     * The **Overview** section has a green check mark and an **OK** indicator in the same row as the operation ID.
If you encounter any errors, click **Actions** , and then click **View details in Cloud Logging**. 



### gcloud

To import FHIR resources into a FHIR store, use the [`gcloud healthcare fhir-stores import gcs`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/import/gcs) command. Specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The location of the object in a Cloud Storage bucket. The location of the files within the bucket is arbitrary and does not have to adhere exactly to the format specified in the following sample. When specifying the location of the FHIR resources in Cloud Storage, you can use wildcards to import multiple files from one or more directories. The following wildcards are supported: 
    * Use `*` to match 0 or more non-separator characters. For example, `gs://BUCKET/DIRECTORY/Example*.ndjson` matches Example.ndjson and Example22.ndjson in DIRECTORY.
    * Use `**` to match 0 or more characters (including separators). Must be used at the end of a path and with no other wildcards in the path. Can also be used with a filename extension (such as .ndjson), which imports all files with the filename extension in the specified directory and its subdirectories. For example, `gs://BUCKET/DIRECTORY/**.ndjson` imports all files with the .ndjson filename extension in DIRECTORY and its subdirectories. 
    * Use `?` to match 1 character. For example, `gs://BUCKET/DIRECTORY/Example?.ndjson` matches Example1.ndjson but does not match Example.ndjson or Example01.ndjson. 



The following sample shows the `gcloud healthcare fhir-stores import gcs` command.
    
    
    gcloud healthcare fhir-stores import gcs FHIR_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION \
      --gcs-uri=gs://BUCKET/DIRECTORY/FHIR_RESOURCE_NAME.ndjson

To specify the structure of the FHIR source files, use the [`--content-structure`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/import/gcs#--content-structure) flag.

The command line displays the operation ID and, after the operation completes, `done`:
    
    
    Request issued for: [FHIR_STORE_ID]
    Waiting for operation [OPERATION_ID] to complete...done.
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID
    

To view more details of the operation, run the [`gcloud healthcare operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations/describe) command, providing the OPERATION_ID from the response:
    
    
    gcloud healthcare operations describe OPERATION_ID \
      --dataset=DATASET_ID

The response includes `done: true`.
    
    
    done: true
    metadata:
    '@type': type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata
    apiMethodName: google.cloud.healthcare.v1.fhir.FhirService.ImportResources
    createTime: 'CREATE_TIME'
    endTime: 'END_TIME'
    logsUrl: https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL,
    counter:
      success: 'SUCCESS_COUNT' 
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID
    response:
    '@type': type.googleapis.com/google.cloud.healthcare.v1.fhir.rest.ImportResourcesResponse
    fhirStore: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID
    

### API

To import FHIR resources into a FHIR store, use the [`projects.locations.datasets.fhirStores.import`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/import) method.

  * The location of the files within the bucket is arbitrary and does not have to adhere exactly to the format specified in the following samples.
  * When specifying the location of the FHIR resources in Cloud Storage, you can use wildcards to import multiple files from one or more directories. The following wildcards are supported: 
    * Use `*` to match 0 or more non-separator characters. For example, `gs://BUCKET/DIRECTORY/Example*.ndjson` matches Example.ndjson and Example22.ndjson in DIRECTORY.
    * Use `**` to match 0 or more characters (including separators). Must be used at the end of a path and with no other wildcards in the path. Can also be used with a filename extension (such as .ndjson), which imports all files with the filename extension in the specified directory and its subdirectories. For example, `gs://BUCKET/DIRECTORY/**.ndjson` imports all files with the .ndjson filename extension in DIRECTORY and its subdirectories. 
    * Use `?` to match 1 character. For example, `gs://BUCKET/DIRECTORY/Example?.ndjson` matches Example1.ndjson but does not match Example.ndjson or Example01.ndjson. 



### curl

To import FHIR resources into a FHIR store, make a `POST` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The location of the object in a Cloud Storage bucket
  * An access token



The following sample shows how to import a single file using a `POST` request using `curl`.
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'contentStructure': 'CONTENT_STRUCTURE',
          'gcsSource': {
            'uri': 'gs://BUCKET/DIRECTORY/FHIR_RESOURCE_FILE'
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:import"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns a response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.fhir.FhirService.ImportResources",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.fhir.rest.ImportResourcesResponse",
      }
    }
    

### PowerShell

To import FHIR resources into a FHIR store, make a `POST` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The location of the object in a Cloud Storage bucket
  * An access token



The following sample shows a `POST` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'contentStructure': 'CONTENT_STRUCTURE',
        'gcsSource': {
          'uri': 'gs://BUCKET/DIRECTORY/FHIR_RESOURCE_FILE'
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:import" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
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
        "apiMethodName": "google.cloud.healthcare.v1.fhir.FhirService.ImportResources",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.fhir.rest.ImportResourcesResponse",
      }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // importsFHIRResource imports an FHIR resource.
    func importFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, gcsURI string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.FhirStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    	req := &healthcare.ImportResourcesRequest{
    		ContentStructure: "RESOURCE",
    		GcsSource: &healthcare.GoogleCloudHealthcareV1FhirGcsSource{
    			Uri: gcsURI,
    		},
    	}
    
    	op, err := storesService.Import(name, req).Do()
    	if err != nil {
    		return fmt.Errorf("Import: %w", err)
    	}
    
    	operationsService := healthcareService.Projects.Locations.Datasets.Operations
    	ticker := time.NewTicker(1 * time.Second)
    	defer ticker.Stop()
    	for {
    		select {
    		case <-ctx.Done():
    			return ctx.Err()
    		case <-ticker.C:
    			newOp, err := operationsService.Get(op.Name).Do()
    			if err != nil {
    				return fmt.Errorf("operationsService.Get(%q): %v", op.Name, err)
    			}
    			if newOp.Done {
    				if newOp.Error != nil {
    					return fmt.Errorf("import operation %q completed with error: %s", op.Name, newOp.Error.Details)
    				}
    				return nil
    			}
    		}
    	}
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.FhirStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.GoogleCloudHealthcareV1FhirGcsSource;
    import com.google.api.services.healthcare.v1.model.ImportResourcesRequest;
    import com.google.api.services.healthcare.v1.model.Operation;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class FhirStoreImport {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStoreImport(String fhirStoreName, String gcsUri) throws IOException {
        // String fhirStoreName =
        //    String.format(
        //        FHIR_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-fhir-id");
        // String gcsUri = "gs://your-bucket-id/path/to/destination/dir"
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure where the store should be imported from.
        GoogleCloudHealthcareV1FhirGcsSource gcsSource =
            new GoogleCloudHealthcareV1FhirGcsSource().setUri(gcsUri);
        ImportResourcesRequest importRequest = new ImportResourcesRequest().setGcsSource(gcsSource);
    
        // Create request and configure any parameters.
        FhirStores.CloudHealthcareImport request =
            client
                .projects()
                .locations()
                .datasets()
                .fhirStores()
                .healthcareImport(fhirStoreName, importRequest);
    
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
          System.out.println("FHIR store import complete: " + operation.getResponse());
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
      responseType: 'json',
    });
    const sleep = ms => {
      return new Promise(resolve => setTimeout(resolve, ms));
    };
    
    const importFhirResources = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const gcsUri = 'my-bucket/my-directory/*.json'
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}`;
      const request = {
        name,
        resource: {
          contentStructure: 'RESOURCE',
          gcsSource: {
            uri: `gs://${gcsUri}`,
          },
        },
      };
      try {
        const operation =
          await healthcare.projects.locations.datasets.fhirStores.import(request);
        const operationName = operation.data.name;
    
        console.log(`Import operation started: ${operationName}`);
    
        let done = false;
        let operationStatus;
        let attempts = 0;
    
        while (!done && attempts < 100) {
          console.log('Waiting for import operation to complete...');
          attempts++;
          await sleep(5000); // Wait 5 seconds between polls
    
          operationStatus =
            await healthcare.projects.locations.datasets.operations.get({
              name: operationName,
            });
    
          done = operationStatus.data.done;
        }
    
        if (operationStatus.data.error) {
          console.error(
            'Import FHIR resources failed:',
            operationStatus.data.error
          );
        } else if (done) {
          const successCount =
            operationStatus.data.metadata?.counter?.success || 0;
          console.log(
            `Import FHIR resources succeeded. ${successCount} resources imported.`
          );
        } else {
          console.error('Import operation timed out in the sample.');
        }
      } catch (error) {
        console.error(
          'An error occurred during the import process:',
          error.message || error
        );
      }
    };
    
    importFhirResources();

### Python
    
    
    def import_fhir_resources(project_id, location, dataset_id, fhir_store_id, gcs_uri):
        """Import resources into the FHIR store by copying them from the
        specified source.
    
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
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the parent dataset's ID
        # fhir_store_id = 'my-fhir-store'  # replace with the FHIR store ID
        # gcs_uri = 'my-bucket'  # replace with a Cloud Storage bucket
        fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        body = {
            "contentStructure": "CONTENT_STRUCTURE_UNSPECIFIED",
            "gcsSource": {"uri": f"gs://{gcs_uri}"},
        }
    
        # Escape "import()" method keyword because "import"
        # is a reserved keyword in Python
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .import_(name=fhir_store_name, body=body)
        )
    
        response = request.execute()
        print(f"Imported FHIR resources: {gcs_uri}")
    
        return response
    
    

## Exporting FHIR resources

The following samples show how to export FHIR resources to a Cloud Storage bucket. When you export FHIR resources from a FHIR store, all resources in the FHIR store are exported.

If you export FHIR resources on a schedule, consider exporting your data incrementally. For instructions, see Incremental exports.

During export, the Cloud Healthcare API creates one file for each resource type from the FHIR store. The filename consists of the operation ID and the resource type separated by an underscore. Each file consists of newline-delimited JSON where each line is a FHIR resource corresponding to the resource type in the filename. For example, if you export multiple Patient records, the output file will be called something similar to `1264567891234567_Patient` and will contain a line for each Patient resource from the FHIR store.

### Console

To export FHIR resources to Cloud Storage, complete the following steps:

  1. In the Google Cloud console, go to the **Datasets** page.  
[Go to Datasets](https://console.cloud.google.com/healthcare/browser)
  2. Click the dataset that contains the FHIR store from which you are exporting FHIR resources.
  3. In the list of data stores, choose **Export** from the **Actions** list for the FHIR store.  
  
The **Export FHIR resources** page displays.
  4. Select **Google Cloud Storage Bucket**.
  5. In the **Project** list, select a Cloud Storage project.
  6. In the **Location** list, select a Cloud Storage bucket.
  7. Click **Export** to export FHIR resources to the defined location in Cloud Storage.
  8. To track the status of the operation, click the **Operations** tab. After the operation completes, the following indications appear: 
     * The **Long-running operation status** section has a green check mark under the **OK** heading.
     * The **Overview** section has a green check mark and an **OK** indicator in the same row as the operation ID.
If you encounter any errors, click **Actions** , and then click **View details in Cloud Logging**. 



### gcloud

To export FHIR resources to a Cloud Storage bucket, use the [`gcloud healthcare fhir-stores export gcs`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/export/gcs) command. Specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The name of the parent project
  * The destination Cloud Storage bucket or directory. Write to a Cloud Storage bucket or directory, rather than an object, because the Cloud Healthcare API creates one object for each resource type. Each object consists of newline-delimited JSON where each line is a FHIR resource. If you specify a directory that doesn't exist, it's created.
  * An optional flag, `--resource-type`, that only exports specific resource types, defined as a comma-separated list of one or more FHIR resources types
  * An optional flag, `--since`, that only exports resources updated after a specific time, defined as `YYYY-MM-DDThh:mm:ss.sss+zz:zz`



The following sample shows the `gcloud healthcare fhir-stores export gcs` command.
    
    
    gcloud healthcare fhir-stores export gcs FHIR_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION \
      --project=PROJECT_ID
      --gcs-uri=gs://BUCKET/DIRECTORY

The command line displays the operation ID:
    
    
    Waiting for operation [OPERATION_ID] to complete...done.
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID
    

To view the status of the operation, run the [`gcloud healthcare operations describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/operations/describe) command, providing the OPERATION_ID from the response:
    
    
    gcloud healthcare operations describe OPERATION_ID \
      --dataset=DATASET_ID

After the command completes, the response includes `done`.
    
    
    metadata:
    '@type': type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata
    apiMethodName: google.cloud.healthcare.v1.fhir.FhirService.ExportFhirData
    createTime: "CREATE_TIME"
    endTime: "END_TIME"
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID
    response:
    '@type': type.googleapis.com/google.cloud.healthcare.v1.fhir.rest.ExportResourcesResponse
    fhirStore: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID
    resourceCount: 'RESOURCE_COUNT'
    

### API

To export FHIR resources, use the [`projects.locations.datasets.fhirStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export) method.

  * Write to a Cloud Storage bucket or directory, rather than an object, because the Cloud Healthcare API creates one newline-delimited JSON file for each resource type. In each JSON file, each line is a FHIR resource.
  * If the command specifies a directory that does not exist, the directory is created.



### curl

To export FHIR resources, make a `POST` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The destination Cloud Storage bucket
  * An access token
  * An optional field, `_type`, that only exports specific resource types, defined as a comma-separated list of one or more FHIR resources types
  * An optional field, `_since`, that only exports resources updated after a specific time, defined as `YYYY-MM-DDThh:mm:ss.sss+zz:zz`



The following sample shows a `POST` request using `curl`.
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'gcsDestination': {
            'uriPrefix': 'gs://BUCKET/DIRECTORY'
          },
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:export"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns a response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1.fhir.FhirService.ExportResources",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.fhir.rest.ExportResourcesResponse",
      }
    }
    

### PowerShell

To export FHIR resources, make a `POST` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The destination Cloud Storage bucket or directory. Write to a Cloud Storage bucket or directory, rather than an object, because the Cloud Healthcare API creates one object for each resource type. Each object consists of newline-delimited JSON where each line is a FHIR resource.
  * An access token
  * An optional field, `_type`, that only exports specific resource types, defined as a comma-separated list of one or more FHIR resources types
  * An optional field, `_since`, that only exports resources updated after a specific time, defined as `YYYY-MM-DDThh:mm:ss.sss+zz:zz`



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
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:export" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
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
        "apiMethodName": "google.cloud.healthcare.v1.fhir.FhirService.ExportResources",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME",
        "logsUrl": "https://console.cloud.google.com/logs/query/CLOUD_LOGGING_URL",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1.fhir.rest.ExportResourcesResponse",
      }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // exportFHIRResource exports the resources in the FHIR store.
    func exportFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, gcsURIPrefix string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.FhirStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    	req := &healthcare.ExportResourcesRequest{
    		GcsDestination: &healthcare.GoogleCloudHealthcareV1FhirGcsDestination{
    			UriPrefix: gcsURIPrefix,
    		},
    	}
    
    	op, err := storesService.Export(name, req).Do()
    	if err != nil {
    		return fmt.Errorf("Export: %w", err)
    	}
    
    	operationsService := healthcareService.Projects.Locations.Datasets.Operations
    	ticker := time.NewTicker(1 * time.Second)
    	defer ticker.Stop()
    	for {
    		select {
    		case <-ctx.Done():
    			return ctx.Err()
    		case <-ticker.C:
    			newOp, err := operationsService.Get(op.Name).Do()
    			if err != nil {
    				return fmt.Errorf("operationsService.Get(%q): %v", op.Name, err)
    			}
    			if newOp.Done {
    				if newOp.Error != nil {
    					return fmt.Errorf("export operation %q completed with error: %v", op.Name, newOp.Error)
    				}
    				return nil
    			}
    		}
    	}
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.FhirStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.ExportResourcesRequest;
    import com.google.api.services.healthcare.v1.model.GoogleCloudHealthcareV1FhirGcsDestination;
    import com.google.api.services.healthcare.v1.model.Operation;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class FhirStoreExport {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStoreExport(String fhirStoreName, String gcsUri) throws IOException {
        // String fhirStoreName =
        //    String.format(
        //        FHIR_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-fhir-id");
        // String gcsUri = "gs://your-bucket-id/path/to/destination/dir"
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure where the store will be exported too.
        GoogleCloudHealthcareV1FhirGcsDestination gcsDestination =
            new GoogleCloudHealthcareV1FhirGcsDestination().setUriPrefix(gcsUri);
        ExportResourcesRequest exportRequest =
            new ExportResourcesRequest().setGcsDestination(gcsDestination);
    
        // Create request and configure any parameters.
        FhirStores.Export request =
            client.projects().locations().datasets().fhirStores().export(fhirStoreName, exportRequest);
    
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
          System.out.println("Fhir store export complete." + operation.getResponse());
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
      responseType: 'json',
    });
    const sleep = ms => {
      return new Promise(resolve => setTimeout(resolve, ms));
    };
    
    const exportFhirResourcesGcs = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const gcsUri = 'my-bucket/my-directory'
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}`;
      const request = {
        name,
        resource: {
          gcsDestination: {
            // The destination location in Cloud Storage for the FHIR resources
            uriPrefix: `gs://${gcsUri}`,
          },
        },
      };
    
      try {
        const operation =
          await healthcare.projects.locations.datasets.fhirStores.export(request);
        const operationName = operation.data.name;
    
        let done = false;
        let operationStatus;
    
        while (!done) {
          console.log('Waiting for operation to complete...');
          await sleep(5000);
    
          operationStatus =
            await healthcare.projects.locations.datasets.operations.get({
              name: operationName,
            });
    
          done = operationStatus.data.done;
        }
    
        if (operationStatus.data.error) {
          console.log('Export failed with error:', operationStatus.data.error);
        } else {
          console.log('Exported FHIR resources successfully');
        }
      } catch (error) {
        console.error('Error exporting FHIR resources:', error.message || error);
      }
    };
    
    exportFhirResourcesGcs();

### Python
    
    
    def export_fhir_store_gcs(project_id, location, dataset_id, fhir_store_id, gcs_uri):
        """Export resources to a Google Cloud Storage bucket by copying
        them from the FHIR store.
    
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
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the parent dataset's ID
        # fhir_store_id = 'my-fhir-store' # replace with the FHIR store ID
        # gcs_uri = 'my-bucket' # replace with a Cloud Storage bucket
        fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        body = {"gcsDestination": {"uriPrefix": f"gs://{gcs_uri}/fhir_export"}}
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .export(name=fhir_store_name, body=body)
        )
    
        response = request.execute()
        print(f"Exported FHIR resources to bucket: gs://{gcs_uri}")
    
        return response
    
    

### Incremental exports

You can specify a timestamp to only export FHIR resources added to your FHIR store since a previous successful export. This improves performance and avoids the cost of re-exporting the entire FHIR store, while also ensuring your exported data is always up-to-date.

When calling [`fhirStores.export`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export), specify the timestamp in the [`_since`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/export#body.request_body.FIELDS.since) field.

## Troubleshooting FHIR import and export requests

If errors occur during a FHIR import or export request, the errors are logged to [Cloud Logging](https://docs.cloud.google.com/logging/docs). For more information, see [Viewing error logs in Cloud Logging](https://docs.cloud.google.com/healthcare-api/docs/how-tos/logging).

If the entire operation returns an error, see [Troubleshooting long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations#troubleshooting).

## What's next

  * If you've successfully imported FHIR data and want to analyze the data in BigQuery, continue to [Exporting FHIR data to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
