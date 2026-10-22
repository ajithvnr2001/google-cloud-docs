---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir/
title: Creating and managing FHIR stores \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:47.500739+00:00
---

# Creating and managing FHIR stores  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Creating and managing FHIR stores Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create, edit, view, list, and delete Fast Healthcare Interoperability Resources (FHIR) stores. FHIR stores hold FHIR resources, such as Claim resources, Patient resources, Medication resources, and more.

**Note:** Changes to a FHIR store might not take effect immediately. To ensure data consistency in the FHIR server, wait for the server to return a response between sending requests.

The Cloud Healthcare API supports the following FHIR versions:

  * [DSTU2](http://hl7.org/fhir/DSTU2)
  * [STU3](http://hl7.org/fhir/stu3)
  * [R4](http://hl7.org/fhir/r4)
  * [R5](http://hl7.org/fhir/r5)



## Creating a FHIR store

Before you can create a FHIR store, you need to [create a dataset](https://docs.cloud.google.com/healthcare-api/docs/how-tos/datasets).

The following samples show how to create a FHIR store using the [`projects.locations.datasets.fhirStores.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/create) method.

**Important:** FHIR stores only support the UTF-8 character set. The Cloud Healthcare API rejects FHIR resources if they contain any characters not in the UTF-8 character set.

### Console

To create a FHIR store, complete the following steps: 

  1. In the Google Cloud console, go to the **Datasets** page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset where you want to create a FHIR store. 
  3. Click **Create Data Store**. 
  4. Select FHIR as the data store type. 
  5. Enter a name that's unique in your dataset. If the name is not unique, the FHIR store creation fails.
  6. Click **Next**. 
  7. To configure your FHIR store, do the following: 
     1. Choose the FHIR version for the FHIR store, one of **DSTU2** , **STU3** , or **R4**.
     2. Select the applicable advanced settings from the following: 
        * **Allow update create** : Select to allow creation of a new resource using an update operation with a user-specified ID.
        * **Referential integrity checks** : Select to enable referential integrity in this store. This can't be changed after creating the store.
        * **Resource versioning** : Select to automatically record historical versions of resources. This can't be changed after creating the store.
     3. Select the applicable profile validation settings from the following fields. For more information, see [ValidationConfig](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#validationconfig): 
        * **Enable profile validation** : Select to enable profile validation. To enforce an implementation guide that's enabled in your FHIR store, you must enable profile validation.
        * **Enable required field validation** : Select to enable resource field validation against the structure definitions in your FHIR profile.
        * **Enable reference type validation** : Select to enable reference type validation.
        * **Enable FHIRPath validation** : Select to enable FHIRPath compatibility check.
     4. Click **Next**.
  8. Optional: To enable implementation guides in your FHIR store, do the following: 
     1. Click **Enable implementation guides**.
     2. Click and expand the **Implementation guides** list.
     3. Select the applicable implementation guides in the list. 

Each implementation guide supports a specific FHIR version. The list shows only those implementation guides that are compatible with the selected FHIR store version.

     4. Click **Import custom IG from Cloud Storage** to import any custom profile validation bundle from a Cloud Storage location.
     5. In the **Select object** panel, select a profile validation bundle resource from a Cloud Storage location. For more information, see [Use Google Cloud console to enable implementation guides](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-profiles#ig-ui).
     6. Click **Select**. 
        * The selected implementation guides are listed in a table with their version, URL, and status.
        * If you have enabled implementation guides but you haven't enabled profile validation, the implementation guide doesn't come into effect.
        * Click **Next**.
  9. Optional: To export resource changes to BigQuery each time the FHIR resources in your store are created, updated, patched, or deleted, do the following: 
     1. Click **Stream resource changes to BigQuery**.
     2. Click **Add a streaming configuration**. For more information on BigQuery streaming, see [Streaming FHIR resource changes to BigQuery](https://cloud.google.com/healthcare-api/docs/how-tos/fhir-bigquery-streaming).
     3. Select the depth level on the **Recursive structure depth** slider to set the depth for all recursive structures in the output schema. By default, the recursive depth value is 2.
     4. Click **Done** to save the streaming configuration.
     5. Click **Next**.
  10. Optional: To configure a Pub/Sub topic for the FHIR store, do the following: 
     1. Click **Receive Cloud Pub/Sub notifications**.
     2. Click **Add a Cloud Pub/Sub topic** and select the topic name. 

When specifying a Pub/Sub topic, enter the qualified URI to the topic, as shown in the following sample: 
            
            projects/PROJECT_ID/topics/PUBSUB_TOPIC

     3. Click **Next**. 
  11. Optional: To add labels to the store, do the following: 
     1. Click **Add Labels to organize your data stores**.
     2. Enter the key and value for the label. For more information on resource labels, see [Using resource labels](https://cloud.google.com/healthcare-api/docs/how-tos/labeling-resources#adding_a_label).
     3. Click **Create**.



The new FHIR store appears in the list.

### gcloud

To create a FHIR store in the dataset, run the [`gcloud healthcare fhir-stores create`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/create) command. 

Before using any of the command data below, make the following replacements: 

  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: an identifier for the FHIR store. The FHIR store ID must have the following: 
    * A unique ID in its dataset
    * A Unicode string of 1-256 characters consisting of the following:
      * Numbers
      * Letters
      * Underscores
      * Dashes
      * Periods
  * FHIR_STORE_VERSION: the FHIR version of the FHIR store. The available options are DSTU2, STU3, or R4.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores create FHIR_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION \
      --version=FHIR_STORE_VERSION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores create FHIR_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION `
      --version=FHIR_STORE_VERSION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores create FHIR_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION ^
      --version=FHIR_STORE_VERSION

You should receive a response similar to the following:

#### Response
    
    
    Created fhirStore [FHIR_STORE_ID].

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: an identifier for the FHIR store. The FHIR store ID must have the following: 
    * A unique ID in its dataset
    * A Unicode string of 1-256 characters consisting of the following:
      * Numbers
      * Letters
      * Underscores
      * Dashes
      * Periods
  * FHIR_STORE_VERSION: the FHIR version of the FHIR store. The available options are DSTU2, STU3, or R4.



Request JSON body: 
    
    
    {
      "version": "FHIR_STORE_VERSION"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "version": "FHIR_STORE_VERSION"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores?fhirStoreId=FHIR_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "version": "FHIR_STORE_VERSION"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores?fhirStoreId=FHIR_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "version": "FHIR_STORE_VERSION"
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // createFHIRStore creates an FHIR store.
    func createFHIRStore(w io.Writer, projectID, location, datasetID, fhirStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.FhirStores
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s", projectID, location, datasetID)
    	version := "R4"
    
    	resp, err := storesService.Create(parent, &healthcare.FhirStore{Version: version}).FhirStoreId(fhirStoreID).Do()
    	if err != nil {
    		return fmt.Errorf("Create: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created FHIR store: %q\n", resp.Name)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.FhirStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.FhirStore;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    import java.util.HashMap;
    import java.util.Map;
    
    public class FhirStoreCreate {
      private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStoreCreate(String datasetName, String fhirStoreId) throws IOException {
        // String datasetName =
        //     String.format(DATASET_NAME, "your-project-id", "your-region-id", "your-dataset-id");
        // String fhirStoreId = "your-fhir-id"
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure the FhirStore to be created.
        Map<String, String> labels = new HashMap<>();
        labels.put("key1", "value1");
        labels.put("key2", "value2");
        String version = "STU3";
        FhirStore content = new FhirStore().setLabels(labels).setVersion(version);
    
        // Create request and configure any parameters.
        FhirStores.Create request =
            client
                .projects()
                .locations()
                .datasets()
                .fhirStores()
                .create(datasetName, content)
                .setFhirStoreId(fhirStoreId);
    
        // Execute the request and process the results.
        FhirStore response = request.execute();
        System.out.println("FHIR store created: " + response.toPrettyString());
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
    
    const createFhirStore = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const version = 'STU3';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
      const request = {
        parent,
        fhirStoreId,
        resource: {
          version,
        },
      };
    
      await healthcare.projects.locations.datasets.fhirStores.create(request);
      console.log(`Created FHIR store: ${fhirStoreId}`);
    };
    
    createFhirStore();

### Python
    
    
    def create_fhir_store(project_id, location, dataset_id, fhir_store_id, version):
        """Creates a new FHIR store within the parent dataset.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
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
        # dataset_id = 'my-dataset'  # replace with the FHIR store's parent dataset ID
        # fhir_store_id = 'my-fhir-store'  # replace with the FHIR store's ID
        # version = 'R4'  # replace with the FHIR store version
        fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
    
        body = {"version": version}
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .create(parent=fhir_store_parent, body=body, fhirStoreId=fhir_store_id)
        )
    
        response = request.execute()
        print(f"Created FHIR store: {fhir_store_id}")
    
        return response
    
    

## Editing a FHIR store

The following samples show how to edit a FHIR store. You can edit a FHIR store to modify properties such as the following:

  * The [Pub/Sub](https://docs.cloud.google.com/healthcare-api/docs/fhir-pubsub) topic to which the Cloud Healthcare API sends notifications of FHIR store changes.
  * The FHIR store's labels. [Labels](https://docs.cloud.google.com/healthcare-api/docs/how-tos/labeling-resources) are key-value pairs that help you organize your Google Cloud resources.

When specifying a Pub/Sub topic, enter the qualified URI to the topic, as shown in the following sample: 
    
    
    projects/PROJECT_ID/topics/PUBSUB_TOPIC

For notifications to work, you must grant additional permissions to the **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts). For more information, see [DICOM, FHIR, and HL7v2 store Pub/Sub permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#dicom_fhir_and_hl7v2_store_cloud_pubsub_permissions). 

### Console

To edit a FHIR store, complete the following steps:

  1. In the Google Cloud console, go to the **Datasets** page.  
[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the FHIR store you want to edit.

  3. In the **Data Stores** list, select the FHIR store you want to edit.

  4. To edit the store's configuration, click edit **FHIR store configuration**.

For more information on the FHIR store's configuration options, see Creating a FHIR store.

  5. To edit the store's implementation guides, click edit **Implementation guides** , and select the applicable implementation guides, or import a custom implementation guide from Cloud Storage. For more information, see [Use Google Cloud console to enable implementation guides](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-profiles#ig-ui).

To edit the implementation guides, or enforce the enabled implementation guides, you must enable profile validation in the **FHIR store configuration** section.

  6. To export resource changes to BigQuery each time the FHIR resources in your store are created, updated, patched, or deleted, click **Add new streaming config** in the **Dataset** field.

  7. Select a BigQuery dataset where resource changes will be streamed. For more information on BigQuery streaming, see [Streaming FHIR resource changes to BigQuery](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bigquery-streaming).

  8. To set the depth for all recursive structures in the output schema, click the relevant depth in the **Recursive Structure Depth** slider. By default, the recursive depth is 2.

  9. To export resource changes only for specific resource types, select the resource types from the **Select FHIR resource types** list.

  10. To configure a Pub/Sub topic for the data store, select a topic name in the **Cloud Pub/Sub Notifications** section. When specifying a Pub/Sub topic, enter the qualified URI to the topic, as shown in the following sample: 
         
         projects/PROJECT_ID/topics/PUBSUB_TOPIC

  11. To add one or more labels to the store, click  edit  **Labels** , click **Add label** and enter the key/value label. For more information on resource labels, see [Using resource labels](https://docs.cloud.google.com/healthcare-api/docs/how-tos/labeling-resources#adding_a_label).

  12. Click **Save**. 




### gcloud

**Note:** You can't edit some FHIR store properties using the Google Cloud CLI. For a list of the properties you can edit, see [`gcloud healthcare fhir-stores update`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/update).

To edit a FHIR store, run the [`gcloud healthcare fhir-stores update`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/update) command.

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the FHIR store's parent dataset
  * `FHIR_STORE_ID`: the FHIR store ID
  * `PUBSUB_TOPIC_ID`: a Pub/Sub topic to which messages are published when an event occurs in a data store



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores update FHIR_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION \
      --pubsub-topic=projects/PROJECT_ID/topics/PUBSUB_TOPIC_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores update FHIR_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION `
      --pubsub-topic=projects/PROJECT_ID/topics/PUBSUB_TOPIC_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores update FHIR_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION ^
      --pubsub-topic=projects/PROJECT_ID/topics/PUBSUB_TOPIC_ID

You should receive a response similar to the following:

#### Response
    
    
    Updated fhirStore [FHIR_STORE_ID].
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID
    notificationConfig:
     pubsubTopic: projects/PROJECT_ID/topics/PUBSUB_TOPIC_ID
    version: FHIR_STORE_VERSION
    

### REST

To edit a FHIR store, use the [`projects.locations.datasets.fhirStores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/patch) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the FHIR store's parent dataset
  * `FHIR_STORE_ID`: the FHIR store ID
  * `PUBSUB_TOPIC_ID`: a Pub/Sub topic to which messages are published when an event occurs in a data store. To determine what data to include in Pub/Sub notifications, see [FHIR Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/fhir-pubsub).
  * `KEY1`: the first label key
  * `VALUE1`: the first label value
  * `KEY2`: the second label key
  * `VALUE2`: the second label value



Request JSON body: 
    
    
    {
      "notificationConfigs": [
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/PUBSUB_TOPIC_ID"
        }
      ],
      "labels": {
        "KEY1": "VALUE1",
        "KEY2": "VALUE2"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "notificationConfigs": [
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/PUBSUB_TOPIC_ID"
        }
      ],
      "labels": {
        "KEY1": "VALUE1",
        "KEY2": "VALUE2"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=notificationConfig,labels"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "notificationConfigs": [
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/PUBSUB_TOPIC_ID"
        }
      ],
      "labels": {
        "KEY1": "VALUE1",
        "KEY2": "VALUE2"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=notificationConfig,labels" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/patch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID%",
      "notificationConfigs": [
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/PUBSUB_TOPIC_ID"
        }
      ],
      "labels": {
        "KEY1": "VALUE1",
        "KEY2": "VALUE2"
      },
      "version": "FHIR_STORE_VERSION"
    }
    

### Go
    
    
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
    
    

## Getting FHIR store details

The following samples show how to get details about a FHIR store.

### Console

To view a FHIR store's details:

  1. In the Google Cloud console, go to the Datasets page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the FHIR store.
  3. Click the name of the FHIR store.



### gcloud

To get details about a FHIR store, run the [`gcloud healthcare fhir-stores describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/describe) command. 

Before using any of the command data below, make the following replacements: 

  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores describe FHIR_STORE_ID \
     --dataset=DATASET_ID \
     --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores describe FHIR_STORE_ID `
     --dataset=DATASET_ID `
     --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores describe FHIR_STORE_ID ^
     --dataset=DATASET_ID ^
     --location=LOCATION

You should receive a response similar to the following.

If you configured any fields in the [`FhirStore`](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#resource-fhirstore) resource, they also appear in the response.

#### Response
    
    
    ...
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID
    ...
    version: FHIR_STORE_VERSION
    

### REST

To get details about a FHIR store, use the [`projects.locations.datasets.fhirStores.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/get) method. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a response similar to the following.

If you configured any fields in the [`FhirStore`](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#resource-fhirstore) resource, they also appear in the response.

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      ...
      "version": "FHIR_STORE_VERSION"
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // getFHIRStore gets an FHIR store.
    func getFHIRStore(w io.Writer, projectID, location, datasetID, fhirStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.FhirStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    
    	store, err := storesService.Get(name).Do()
    	if err != nil {
    		return fmt.Errorf("Get: %w", err)
    	}
    
    	fmt.Fprintf(w, "Got FHIR store: %q\n", store.Name)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.FhirStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.FhirStore;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class FhirStoreGet {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStoreGet(String fhirStoreName) throws IOException {
        // String fhirStoreName =
        //    String.format(
        //        FHIR_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-fhir-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        FhirStores.Get request =
            client.projects().locations().datasets().fhirStores().get(fhirStoreName);
    
        // Execute the request and process the results.
        FhirStore store = request.execute();
        System.out.println("FHIR store retrieved: \n" + store.toPrettyString());
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
    
    const getFhirStore = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}`;
      const request = {name};
    
      const fhirStore =
        await healthcare.projects.locations.datasets.fhirStores.get(request);
      console.log(fhirStore.data);
    };
    
    getFhirStore();

### Python
    
    
    def get_fhir_store(project_id, location, dataset_id, fhir_store_id):
        """Gets the specified FHIR store.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample."""
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        # Imports Python's built-in "json" module
        import json
    
        api_version = "v1"
        service_name = "healthcare"
        # Instantiates an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'  # replace with your GCP project ID
        # location = 'us-central1'  # replace with the parent dataset's location
        # dataset_id = 'my-dataset'  # replace with the FHIR store's parent dataset
        # fhir_store_id = 'my-fhir-store'  # replace with the FHIR store's ID
        fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        fhir_stores = client.projects().locations().datasets().fhirStores()
        fhir_store = fhir_stores.get(name=fhir_store_name).execute()
    
        print(json.dumps(fhir_store, indent=2))
        return fhir_store
    
    

## Listing the FHIR stores in a dataset

The following samples show how to list the FHIR stores in a dataset.

### Console

To view the data stores in a dataset: 

  1. In the Google Cloud console, go to the **Datasets** page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the data store you want to view. 



### gcloud

To view details about a FHIR store, run the [`gcloud healthcare fhir-stores list`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/list) command. 

Before using any of the command data below, make the following replacements: 

  * DATASET_ID: the FHIR store's parent dataset
  * LOCATION: the dataset location



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores list --dataset=DATASET_ID --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores list --dataset=DATASET_ID --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores list --dataset=DATASET_ID --location=LOCATION

You should receive a response similar to the following.

If you configured any fields in the [`FhirStore`](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#resource-fhirstore) resource, they also appear in the response.
    
    
    ID             LOCATION     REF_INT  RES_VER  UPDATE_CREATE  TOPIC
    FHIR_STORE_ID  LOCATION                                       PUBSUB_TOPIC
    ...
    

### REST

To list the FHIR stores in a dataset, use the [`projects.locations.datasets.fhirStores.list`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/list) method. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * DATASET_ID: the FHIR store's parent dataset
  * LOCATION: the dataset location



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a response similar to the following.

If you configured any fields in the [`FhirStore`](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#resource-fhirstore) resource, they also appear in the response.

#### Response
    
    
    {
      "fhirStores": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
          "version": "FHIR_STORE_VERSION"
        },
        {
          ...
        }
      ]
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // listFHIRStores prints a list of FHIR stores to w.
    func listFHIRStores(w io.Writer, projectID, location, datasetID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.FhirStores
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s", projectID, location, datasetID)
    
    	resp, err := storesService.List(parent).Do()
    	if err != nil {
    		return fmt.Errorf("List: %w", err)
    	}
    
    	fmt.Fprintln(w, "FHIR stores:")
    	for _, s := range resp.FhirStores {
    		fmt.Fprintln(w, s.Name)
    	}
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.FhirStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.FhirStore;
    import com.google.api.services.healthcare.v1.model.ListFhirStoresResponse;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.Collections;
    import java.util.List;
    
    public class FhirStoreList {
      private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStoreList(String datasetName) throws IOException {
        // String datasetName =
        //    String.format(DATASET_NAME, "your-project-id", "your-region-id", "your-dataset-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Results are paginated, so multiple queries may be required.
        String pageToken = null;
        List<FhirStore> stores = new ArrayList<>();
        do {
          // Create request and configure any parameters.
          FhirStores.List request =
              client
                  .projects()
                  .locations()
                  .datasets()
                  .fhirStores()
                  .list(datasetName)
                  .setPageSize(100) // Specify pageSize up to 1000
                  .setPageToken(pageToken);
    
          // Execute response and collect results.
          ListFhirStoresResponse response = request.execute();
          stores.addAll(response.getFhirStores());
    
          // Update the page token for the next request.
          pageToken = response.getNextPageToken();
        } while (pageToken != null);
    
        // Print results.
        System.out.printf("Retrieved %s Fhir stores: \n", stores.size());
        for (FhirStore data : stores) {
          System.out.println("\t" + data.toPrettyString());
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
    
    const listFhirStores = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
      const request = {parent};
    
      try {
        const fhirStores =
          await healthcare.projects.locations.datasets.fhirStores.list(request);
        console.log(JSON.stringify(fhirStores.data));
      } catch (error) {
        console.error('Error listing FHIR stores:', error.message || error);
      }
    };
    
    listFhirStores();

### Python
    
    
    def list_fhir_stores(project_id, location, dataset_id):
        """Lists the FHIR stores in the given dataset.
    
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
        # dataset_id = 'my-dataset'  # replace with the parent dataset's ID
        fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
    
        fhir_stores = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .list(parent=fhir_store_parent)
            .execute()
            .get("fhirStores", [])
        )
    
        for fhir_store in fhir_stores:
            print(fhir_store)
    
        return fhir_stores
    
    

## Getting the capabilities or conformance statement for a FHIR store

The following samples show how to get the capabilities ([STU3](https://www.hl7.org/fhir/STU3/capabilitystatement.html) or [R4](https://www.hl7.org/fhir/R4/capabilitystatement.html) or [R5](https://www.hl7.org/fhir/R5/capabilitystatement.html)) or [conformance (DSTU2)](https://hl7.org/fhir/DSTU2/conformance.html) statement for a FHIR store.

The information in the capabilities or conformance statement reflects the settings in the FHIR store. For example, if [`FhirStore.enableUpdateCreate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.enable_update_create) is set to `true`, then this is reflected in the capabilities statement's `CapabilityStatement.rest.resource.updateCreate` field.

The following table shows the Cloud Healthcare API method for getting the capabilities or conformance statement for a FHIR store and its equivalent FHIR specification interaction:

Cloud Healthcare API method | FHIR specification interaction  
---|---  
[`projects.locations.datasets.fhirStores.fhir.capabilities`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/capabilities) | capabilities ([STU3](https://www.hl7.org/fhir/STU3/capabilitystatement.html) or [R4](https://www.hl7.org/fhir/R4/capabilitystatement.html) or [R5](https://www.hl7.org/fhir/R5/capabilitystatement.html)) or [`conformance` (DSTU2)](https://www.hl7.org/fhir/DSTU2/http.html#conformance)  
  
### Console

The Google Cloud console and the gcloud CLI don't support this action. Instead, use `curl`, PowerShell, or your preferred language.

### gcloud

The Google Cloud console and the gcloud CLI don't support this action. Instead, use `curl`, PowerShell, or your preferred language.

### REST

To get the capabilities or conformance statement for a FHIR store, use the [`projects.locations.datasets.fhirStores.fhir.capabilities`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/capabilities) method. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/metadata"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/metadata" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/capabilities). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "acceptUnknown": "both",
      "date": "YYYY-MM-DD",
      "description": "FHIR capability statement for the FHIR store specified by the request.",
      "experimental": true,
      "fhirVersion": "FHIR_STORE_VERSION",
      "format": [
        "json"
      ],
      "id": "FHIR_STORE_ID",
      "kind": "instance",
      "patchFormat": [
        "application/json-patch+json"
      ],
      "publisher": "Google",
      "resourceType": "CapabilityStatement",
      ...
      "status": "draft",
      "url": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "version": "YYYYMMDD"
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // getFHIRMetadata gets FHIR store metadata.
    func getFHIRMetadata(w io.Writer, projectID, location, datasetID, fhirStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    
    	resp, err := fhirService.Capabilities(name).Do()
    	if err != nil {
    		return fmt.Errorf("Capabilities: %w", err)
    	}
    
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("Capabilities: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
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
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.FhirStores.Fhir.Capabilities;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.HttpBody;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class FhirStoreGetMetadata {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStoreGetMetadata(String fhirStoreName) throws IOException {
        // String fhirStoreName =
        //    String.format(
        //        FHIR_NAME, "project-id", "region-id", "dataset-id", "store-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Capabilities request =
            client.projects().locations().datasets().fhirStores().fhir().capabilities(fhirStoreName);
    
        // Execute the request and process the results.
        HttpBody response = request.execute();
        System.out.println("FHIR store metadata retrieved: " + response.toPrettyString());
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
    
    const getFhirStoreCapabilities = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/metadata`;
      const request = {name};
    
      try {
        const fhirStore =
          await healthcare.projects.locations.datasets.fhirStores.get(request);
        console.log(JSON.stringify(fhirStore.data, null, 2));
      } catch (error) {
        console.error(
          'Error getting FHIR store capabilities:',
          error.message || error
        );
      }
    };
    
    getFhirStoreCapabilities();

### Python
    
    
    def get_fhir_store_metadata(project_id, location, dataset_id, fhir_store_id):
        """Gets the FHIR capability statement (STU3, R4), or the conformance statement
        in the DSTU2 case for the store, which contains a description of functionality
        supported by the server.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample."""
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        # Imports Python's built-in "json" module
        import json
    
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
        fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        fhir_stores = client.projects().locations().datasets().fhirStores()
        response = fhir_stores.fhir().capabilities(name=fhir_store_name).execute()
    
        print(json.dumps(response, indent=2))
        return response
    
    

## Setting the base resource validation level

By default, all resources in your FHIR store have base resource validation applied to them. This validation ensures that the following are true when the resource is created:

  * All required fields are defined.
  * All referred resource types are valid.
  * The resource meets all FHIRPath constraints.



You can make your base resource validation less strict by disabling one or more of these types of base resource validation for your FHIR store.

### Console

The Google Cloud console and the gcloud CLI don't support this action. Instead, use `curl`, PowerShell, or your preferred language.

### gcloud

The Google Cloud console and the gcloud CLI don't support this action. Instead, use `curl`, PowerShell, or your preferred language.

### REST

To disable base resource validation in an existing FHIR store, use the [`projects.locations.datasets.fhirStores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/patch) method. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * DATASET_ID: the FHIR store's parent dataset
  * LOCATION: the dataset location
  * BASE_RESOURCE_VALIDATION_TYPE: the base resource validation type you want to disable. To disable validation, set any of the following fields to `true`: 
    * `disableRequiredFieldValidation`
    * `disableReferenceTypeValidation`
    * `disableFhirpathValidation`



Request JSON body: 
    
    
    {
      "validationConfig": {
        "BASE_RESOURCE_VALIDATION_TYPE": true
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "validationConfig": {
        "BASE_RESOURCE_VALIDATION_TYPE": true
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=validationConfig"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "validationConfig": {
        "BASE_RESOURCE_VALIDATION_TYPE": true
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=validationConfig" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/patch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a response similar to the following.

If you configured any fields in the [`FhirStore`](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#resource-fhirstore) resource, they also appear in the response.

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      ...
      "version": "FHIR_STORE_VERSION",
      "validationConfig": {
        "BASE_RESOURCE_VALIDATION_TYPE": true
      }
    }
    

## Deleting a FHIR store

**Caution:** Deleting a FHIR store also deletes the resources in the FHIR store. If deleted, these resources cannot be recovered.

The following samples show how to delete a FHIR store.

### Console

To delete a data store: 

  1. In the Google Cloud console, go to the **Datasets** page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the data store you want to delete.
  3. Choose **Delete** from the **Actions** drop-down list for the data store that you want to delete. 
  4. To confirm, type the data store name and then click **Delete**. 



### gcloud

To delete a FHIR store, run the [`gcloud healthcare fhir-stores delete`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/delete) command. 

Before using any of the command data below, make the following replacements: 

  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores delete FHIR_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores delete FHIR_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare fhir-stores delete FHIR_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION

You should receive a response similar to the following:
    
    
    Deleted fhirStore [FHIR_STORE_ID].
    

### REST

To delete a FHIR store, use the [`projects.locations.datasets.fhirStores.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/delete) method. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {}

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // deleteFHIRStore deletes an FHIR store.
    func deleteFHIRStore(w io.Writer, projectID, location, datasetID, fhirStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.FhirStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    
    	if _, err := storesService.Delete(name).Do(); err != nil {
    		return fmt.Errorf("Delete: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted FHIR store: %q\n", fhirStoreID)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.FhirStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class FhirStoreDelete {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStoreDelete(String fhirStoreName) throws IOException {
        // String fhirStoreName =
        //    String.format(
        //        FHIR_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-fhir-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        FhirStores.Delete request =
            client.projects().locations().datasets().fhirStores().delete(fhirStoreName);
    
        // Execute the request and process the results.
        request.execute();
        System.out.println("FHIR store deleted.");
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
    
    const deleteFhirStore = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}`;
      const request = {name};
    
      try {
        await healthcare.projects.locations.datasets.fhirStores.delete(request);
        console.log(`Deleted FHIR store: ${fhirStoreId}`);
      } catch (error) {
        console.error('Error deleting FHIR store:', error.message || error);
      }
    };
    
    deleteFhirStore();

### Python
    
    
    def delete_fhir_store(project_id, location, dataset_id, fhir_store_id):
        """Deletes the specified FHIR store.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
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
        # dataset_id = 'my-dataset'  # replace with the FHIR store's parent dataset
        # fhir_store_id = 'my-fhir-store'  # replace with the FHIR store's ID
        fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .delete(name=fhir_store_name)
        )
    
        response = request.execute()
        print(f"Deleted FHIR store: {fhir_store_id}")
    
        return response
    
    

## What's next

[Learn how to create and work with FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
