---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom/
title: Creating and managing DICOM stores \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:51.034385+00:00
---

# Creating and managing DICOM stores  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Creating and managing DICOM stores Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create, edit, view, list, and delete [Digital Imaging and Communications in Medicine (DICOM)](https://www.dicomstandard.org/) stores.

DICOM stores hold DICOM instances. You can add and manage DICOM instances in a DICOM store using the [DICOMweb](https://www.dicomstandard.org/using/dicomweb) implementation in the Cloud Healthcare API, or you can import and export DICOM instances using Google Cloud services.

For more information on how the Cloud Healthcare API conforms to the DICOM standard, see the [DICOM conformance statement](https://docs.cloud.google.com/healthcare-api/docs/dicom).

**Note:** Changes to a DICOM store might not take effect immediately. To verify data consistency in the DICOM server, wait for the server to return a response between sending requests.

## Creating a DICOM store

Before you can create a DICOM store, you need to [create a dataset](https://docs.cloud.google.com/healthcare-api/docs/how-tos/datasets).

The following samples show how to create a DICOM store:

### Console

To create a DICOM store: 

  1. In the Google Cloud console, go to the Datasets page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset where you want to create a DICOM store. 
  3. Click **Create Data Store**. 
  4. Select DICOM as the data store type. 
  5. Enter a name of your choice that's unique in your dataset. If the name is not unique, the data store creation fails.
  6. Click **Next**. 
  7. If you want to configure a Pub/Sub topic for the data store, click **Receive Cloud Pub/Sub notifications** and select the topic name. When specifying a Pub/Sub topic, enter the qualified URI to the topic, as shown in the following sample: 
         
         projects/PROJECT_ID/topics/PUBSUB_TOPIC

  8. Click **Next**. 
  9. To add one or more labels to the store, click **Add Labels to organize your data stores** and enter the key/value label. For more information on resource labels, see [Using resource labels](https://cloud.google.com/healthcare-api/docs/how-tos/labeling-resources#adding_a_label). 
  10. Click **Create**. 



The new data store appears in the list.

### gcloud

To create a DICOM store, run the [`gcloud healthcare dicom-stores create`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/create) command. 

Before using any of the command data below, make the following replacements: 

  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: an identifier for the DICOM store. The DICOM store ID must have the following: 
    * A unique ID in its dataset
    * A Unicode string of 1-256 characters consisting of the following:
      * Numbers
      * Letters
      * Underscores
      * Dashes
      * Periods



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores create DICOM_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores create DICOM_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores create DICOM_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION

You should receive a response similar to the following:

#### Response
    
    
    Created dicomStore [DICOM_STORE_ID].

### REST

To create a DICOM store, use the [`projects.locations.datasets.dicomStores.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/create) method. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: an identifier for the DICOM store. The DICOM store ID must have the following: 
    * A unique ID in its dataset
    * A Unicode string of 1-256 characters consisting of the following:
      * Numbers
      * Letters
      * Underscores
      * Dashes
      * Periods



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores?dicomStoreId=DICOM_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores?dicomStoreId=DICOM_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID"
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // createDICOMStore creates a DICOM store.
    func createDICOMStore(w io.Writer, projectID, location, datasetID, dicomStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	store := &healthcare.DicomStore{}
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s", projectID, location, datasetID)
    
    	resp, err := storesService.Create(parent, store).DicomStoreId(dicomStoreID).Do()
    	if err != nil {
    		return fmt.Errorf("Create: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created DICOM store: %q\n", resp.Name)
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
    import com.google.api.services.healthcare.v1.model.DicomStore;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    import java.util.HashMap;
    import java.util.Map;
    
    public class DicomStoreCreate {
      private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomStoreCreate(String datasetName, String dicomStoreId) throws IOException {
        // String datasetName =
        //     String.format(DATASET_NAME, "your-project-id", "your-region-id", "your-dataset-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure the dicomStore to be created.
        Map<String, String> labels = new HashMap<>();
        labels.put("key1", "value1");
        labels.put("key2", "value2");
        DicomStore content = new DicomStore().setLabels(labels);
    
        // Create request and configure any parameters.
        DicomStores.Create request =
            client
                .projects()
                .locations()
                .datasets()
                .dicomStores()
                .create(datasetName, content)
                .setDicomStoreId(dicomStoreId);
    
        // Execute the request and process the results.
        DicomStore response = request.execute();
        System.out.println("DICOM store created: " + response.toPrettyString());
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
    
    const createDicomStore = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
      const request = {parent, dicomStoreId};
    
      await healthcare.projects.locations.datasets.dicomStores.create(request);
      console.log(`Created DICOM store: ${dicomStoreId}`);
    };
    
    createDicomStore();

### Python
    
    
    def create_dicom_store(project_id, location, dataset_id, dicom_store_id):
        """Creates a new DICOM store within the parent dataset.
    
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
        dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .dicomStores()
            .create(parent=dicom_store_parent, body={}, dicomStoreId=dicom_store_id)
        )
    
        response = request.execute()
        print(f"Created DICOM store: {dicom_store_id}")
        return response
    
    

## Editing a DICOM store

The following samples show how to make the following changes to a DICOM store:

  * Edit the [Pub/Sub](https://docs.cloud.google.com/healthcare-api/docs/dicom-pubsub) topic to which the Cloud Healthcare API sends notifications of DICOM store changes. The DICOM store supports sending notifications to multiple subscribers. The following example shows how to add one Pub/Sub topic to the DICOM store; additional topics can be added to the [`dicomStore.notificationConfigs`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores#DicomStore) using a similar style.
  * Edit the labels. [Labels](https://docs.cloud.google.com/healthcare-api/docs/how-tos/labeling-resources) are key-value pairs that help you organize your Google Cloud resources.

When specifying a Pub/Sub topic, enter the qualified URI to the topic, as shown in the following sample: 
    
    
    projects/PROJECT_ID/topics/PUBSUB_TOPIC

For notifications to work, you must grant additional permissions to the **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts). For more information, see [DICOM, FHIR, and HL7v2 store Pub/Sub permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#dicom_fhir_and_hl7v2_store_cloud_pubsub_permissions). 

### Console

To edit a DICOM store, complete the following steps: 

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the DICOM store you want to edit.
  3. In the **Data stores** list, click the data store you want to edit.
  4. If you want to configure a Pub/Sub topic for the data store, select the topic name from **Select a Cloud Pub/Sub Topic**.
  5. To add one or more labels to the store, click  edit  **Labels** , click **Add label** , and enter the key/value label. For more information on resource labels, see [Using resource labels](https://cloud.google.com/healthcare-api/docs/how-tos/labeling-resources#adding_a_label).
  6. Click **Save**. 



### gcloud

To edit a DICOM store, run the [`gcloud healthcare dicom-stores update`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/update) command. The gcloud CLI does not support editing labels. 

Before using any of the command data below, make the following replacements: 

  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `PUBSUB_TOPIC`: a Pub/Sub topic to which messages are published when an event occurs in a data store



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores update DICOM_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION \
      --pubsub-topic=projects/PROJECT_ID/topics/PUBSUB_TOPIC

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores update DICOM_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION `
      --pubsub-topic=projects/PROJECT_ID/topics/PUBSUB_TOPIC

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores update DICOM_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION ^
      --pubsub-topic=projects/PROJECT_ID/topics/PUBSUB_TOPIC

You should receive a response similar to the following:

#### Response
    
    
    Updated dicomStore [DICOM_STORE_ID].
    ...
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID
    notificationConfig:
      pubsubTopic: projects/PROJECT_ID/topics/PUBSUB_TOPIC
    

### REST

To edit a DICOM store, use the [`projects.locations.datasets.dicomStores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/patch) method. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID
  * `PUBSUB_TOPIC`: a Pub/Sub topic to which messages are published when an event occurs in a data store
  * `KEY_1`: the first label key
  * `VALUE_1`: the first label value
  * `KEY_2`: the second label key
  * `VALUE_2`: the second label value



Request JSON body: 
    
    
    {
      "notificationConfigs": [
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/PUBSUB_TOPIC"
        }
      ],
      "labels": {
        "KEY_1": "VALUE_1",
        "KEY_2": "VALUE_2"
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
          "pubsubTopic": "projects/PROJECT_ID/topics/PUBSUB_TOPIC"
        }
      ],
      "labels": {
        "KEY_1": "VALUE_1",
        "KEY_2": "VALUE_2"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID?updateMask=notificationConfigs,labels"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "notificationConfigs": [
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/PUBSUB_TOPIC"
        }
      ],
      "labels": {
        "KEY_1": "VALUE_1",
        "KEY_2": "VALUE_2"
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID?updateMask=notificationConfigs,labels" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/patch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a response similar to the following.

If you configured any fields in the [`DicomStore`](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores#resource-dicomstore) resource, they also appear in the response.

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID",
      "notificationConfigs": [
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/PUBSUB_TOPIC"
        }
      ],
      "labels": {
        "KEY_1": "VALUE_1",
        "KEY_2": "VALUE_2"
      }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // patchDICOMStore updates (patches) a DICOM store by updating its Pub/sub topic name.
    func patchDICOMStore(w io.Writer, projectID, location, datasetID, dicomStoreID, topicName string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	if _, err := storesService.Patch(name, &healthcare.DicomStore{
    		NotificationConfig: &healthcare.NotificationConfig{
    			PubsubTopic: topicName, // format is "projects/*/locations/*/topics/*"
    		},
    	}).UpdateMask("notificationConfig").Do(); err != nil {
    		return fmt.Errorf("Patch: %w", err)
    	}
    
    	fmt.Fprintf(w, "Patched DICOM store %s with Pub/sub topic %s\n", datasetID, topicName)
    
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
    import com.google.api.services.healthcare.v1.model.DicomStore;
    import com.google.api.services.healthcare.v1.model.NotificationConfig;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class DicomStorePatch {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void patchDicomStore(String dicomStoreName, String pubsubTopic) throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
        // String pubsubTopic = "projects/your-project-id/topics/your-pubsub-topic";
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Fetch the initial state of the DICOM store.
        DicomStores.Get getRequest =
            client.projects().locations().datasets().dicomStores().get(dicomStoreName);
        DicomStore store = getRequest.execute();
    
        // Update the DicomStore fields as needed as needed. For a full list of DicomStore fields, see:
        // https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.dicomStores#DicomStore
        store.setNotificationConfig(new NotificationConfig().setPubsubTopic(pubsubTopic));
    
        // Create request and configure any parameters.
        DicomStores.Patch request =
            client
                .projects()
                .locations()
                .datasets()
                .dicomStores()
                .patch(dicomStoreName, store)
                .setUpdateMask("notificationConfig");
    
        // Execute the request and process the results.
        store = request.execute();
        System.out.println("DICOM store patched: \n" + store.toPrettyString());
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
    
    const patchDicomStore = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      // const pubsubTopic = 'my-topic'
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const request = {
        name,
        updateMask: 'notificationConfig',
        resource: {
          notificationConfig: {
            pubsubTopic: `projects/${projectId}/topics/${pubsubTopic}`,
          },
        },
      };
    
      await healthcare.projects.locations.datasets.dicomStores.patch(request);
      console.log(
        `Patched DICOM store ${dicomStoreId} with Cloud Pub/Sub topic ${pubsubTopic}`
      );
    };
    
    patchDicomStore();

### Python
    
    
    def patch_dicom_store(project_id, location, dataset_id, dicom_store_id, pubsub_topic):
        """Updates the DICOM store.
    
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
        # pubsub_topic = 'my-topic'  # replace with an existing Pub/Sub topic
        dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        dicom_store_name = f"{dicom_store_parent}/dicomStores/{dicom_store_id}"
    
        patch = {
            "notificationConfig": {
                "pubsubTopic": f"projects/{project_id}/topics/{pubsub_topic}"
            }
        }
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .dicomStores()
            .patch(name=dicom_store_name, updateMask="notificationConfig", body=patch)
        )
    
        response = request.execute()
        print(
            "Patched DICOM store {} with Cloud Pub/Sub topic: {}".format(
                dicom_store_id, pubsub_topic
            )
        )
    
        return response
    
    

## Getting DICOM store details

The following samples show how to get details about a DICOM store.

### Console

To view a DICOM store's details:

  1. In the Google Cloud console, go to the **Datasets** page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the DICOM store you want to view.
  3. Click the name of the DICOM store.

The **Overview** tab shows the details of the selected DICOM store. The **Metrics** tab shows the DICOM store, DICOM study, and DICOM series metrics. For more information, see [View DICOM store, DICOM study, and DICOM series metrics](https://docs.cloud.google.com/healthcare-api/docs/dicom-store-metrics).




### gcloud

To get details about a DICOM store, run the [`gcloud healthcare dicom-stores describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/describe) command. 

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores describe DICOM_STORE_ID \
      --project=PROJECT_ID \
      --dataset=DATASET_ID \
      --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores describe DICOM_STORE_ID `
      --project=PROJECT_ID `
      --dataset=DATASET_ID `
      --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores describe DICOM_STORE_ID ^
      --project=PROJECT_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION

You should receive a response similar to the following.

If you configured any fields in the [`DicomStore`](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores#resource-dicomstore) resource, they also appear in the response.

#### Response
    
    
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID
    

### REST

To get details about a DICOM store, use the [`projects.locations.datasets.dicomStores.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/get) method. 

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
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a response similar to the following.

If you configured any fields in the [`DicomStore`](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores#resource-dicomstore) resource, they also appear in the response.

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID"
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // getDICOMStore gets a DICOM store.
    func getDICOMStore(w io.Writer, projectID, location, datasetID, dicomStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	store, err := storesService.Get(name).Do()
    	if err != nil {
    		return fmt.Errorf("Get: %w", err)
    	}
    
    	fmt.Fprintf(w, "Got DICOM store: %+v\n", store)
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
    import com.google.api.services.healthcare.v1.model.DicomStore;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class DicomStoreGet {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomeStoreGet(String dicomStoreName) throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        DicomStores.Get request =
            client.projects().locations().datasets().dicomStores().get(dicomStoreName);
    
        // Execute the request and process the results.
        DicomStore store = request.execute();
        System.out.println("DICOM store retrieved: \n" + store.toPrettyString());
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
    
    const getDicomStore = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const request = {name};
    
      const dicomStore =
        await healthcare.projects.locations.datasets.dicomStores.get(request);
      console.log(dicomStore.data);
    };
    
    getDicomStore();

### Python
    
    
    def get_dicom_store(project_id, location, dataset_id, dicom_store_id):
        """Gets the specified DICOM store.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/dicom
        before running the sample."""
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        # Imports Python's built-in "json" module
        import json
    
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
        dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        dicom_store_name = f"{dicom_store_parent}/dicomStores/{dicom_store_id}"
    
        dicom_stores = client.projects().locations().datasets().dicomStores()
        dicom_store = dicom_stores.get(name=dicom_store_name).execute()
    
        print(json.dumps(dicom_store, indent=2))
        return dicom_store
    
    

## Listing the DICOM stores in a dataset

The following samples show how to list the DICOM stores in a dataset:

### Console

To view the data stores in a dataset: 

  1. In the Google Cloud console, go to the **Datasets** page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the data store you want to view. 



### gcloud

To list the DICOM stores in a dataset, run the [`gcloud healthcare dicom-stores list`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/list) command. 

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores list \
      --project=PROJECT_ID \
      --dataset=DATASET_ID \
      --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores list `
      --project=PROJECT_ID `
      --dataset=DATASET_ID `
      --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores list ^
      --project=PROJECT_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION

You should receive a response similar to the following.

If you configured any fields in the [`DicomStore`](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores#resource-dicomstore) resource, they also appear in the response.
    
    
    ID             LOCATION     TOPIC
    DICOM_STORE_ID LOCATION     PUBSUB_TOPIC
    ...
    

### REST

To list the DICOM stores in a dataset, use the [`projects.locations.datasets.dicomStores.list`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/list) method. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a response similar to the following.

If you configured any fields in the [`DicomStore`](https://cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores#resource-dicomstore) resource, they also appear in the response.

#### Response
    
    
    {
      "dicomStores": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID"
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
    
    // listDICOMStores prints a list of DICOM stores to w.
    func listDICOMStores(w io.Writer, projectID, location, datasetID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s", projectID, location, datasetID)
    
    	resp, err := storesService.List(parent).Do()
    	if err != nil {
    		return fmt.Errorf("List: %w", err)
    	}
    
    	fmt.Fprintln(w, "DICOM Stores:")
    	for _, s := range resp.DicomStores {
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
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.DicomStores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.DicomStore;
    import com.google.api.services.healthcare.v1.model.ListDicomStoresResponse;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.Collections;
    import java.util.List;
    
    public class DicomStoreList {
      private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomStoreList(String datasetName) throws IOException {
        // String datasetName =
        //     String.format(DATASET_NAME, "your-project-id", "your-region-id", "your-dataset-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Results are paginated, so multiple queries may be required.
        String pageToken = null;
        List<DicomStore> stores = new ArrayList<>();
        do {
          // Create request and configure any parameters.
          DicomStores.List request =
              client
                  .projects()
                  .locations()
                  .datasets()
                  .dicomStores()
                  .list(datasetName)
                  .setPageSize(100) // Specify pageSize up to 1000
                  .setPageToken(pageToken);
    
          // Execute response and collect results.
          ListDicomStoresResponse response = request.execute();
          stores.addAll(response.getDicomStores());
    
          // Update the page token for the next request.
          pageToken = response.getNextPageToken();
        } while (pageToken != null);
    
        // Print results.
        System.out.printf("Retrieved %s DICOM stores: \n", stores.size());
        for (DicomStore data : stores) {
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
    });
    
    const listDicomStores = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
      const request = {parent};
    
      const dicomStores =
        await healthcare.projects.locations.datasets.dicomStores.list(request);
      console.log(JSON.stringify(dicomStores.data));
    };
    
    listDicomStores();

### Python
    
    
    def list_dicom_stores(project_id, location, dataset_id):
        """Lists the DICOM stores in the given dataset.
    
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
        dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
    
        dicom_stores = (
            client.projects()
            .locations()
            .datasets()
            .dicomStores()
            .list(parent=dicom_store_parent)
            .execute()
            .get("dicomStores", [])
        )
    
        for dicom_store in dicom_stores:
            print(dicom_store)
    
        return dicom_stores
    
    

## Deleting a DICOM store

**Caution:** Deleting a DICOM store also deletes the object instances in the DICOM store. If deleted, this data cannot be recovered. DICOM object instances that were exported to Cloud Storage are not affected.

The following samples show how to delete a DICOM store:

### Console

To delete a data store: 

  1. In the Google Cloud console, go to the **Datasets** page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the data store you want to delete.
  3. Choose **Delete** from the **Actions** drop-down list for the data store that you want to delete. 
  4. To confirm, type the data store name and then click **Delete**. 



### gcloud

To delete a DICOM store, run the [`gcloud healthcare dicom-stores delete`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/delete) command. 

Before using any of the command data below, make the following replacements: 

  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores delete DICOM_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores delete DICOM_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare dicom-stores delete DICOM_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION

To confirm, type **Y**. You should receive a response similar to the following. 
    
    
    Deleted dicomStore [DICOM_STORE_ID].
    

### REST

To delete a DICOM store, use the [`projects.locations.datasets.dicomStores.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/delete) method. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the DICOM store's parent dataset
  * `DICOM_STORE_ID`: the DICOM store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

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
    
    // deleteDICOMStore deletes an DICOM store.
    func deleteDICOMStore(w io.Writer, projectID, location, datasetID, dicomStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    	if _, err := storesService.Delete(name).Do(); err != nil {
    		return fmt.Errorf("Delete: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted DICOM store: %q\n", name)
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
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class DicomStoreDelete {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void deleteDicomStore(String dicomStoreName) throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        DicomStores.Delete request =
            client.projects().locations().datasets().dicomStores().delete(dicomStoreName);
    
        // Execute the request and process the results.
        request.execute();
        System.out.println("DICOM store deleted.");
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
    
    const deleteDicomStore = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const request = {name};
    
      await healthcare.projects.locations.datasets.dicomStores.delete(request);
      console.log(`Deleted DICOM store: ${dicomStoreId}`);
    };
    
    deleteDicomStore();

### Python
    
    
    def delete_dicom_store(project_id, location, dataset_id, dicom_store_id):
        """Deletes the specified DICOM store.
    
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
        dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        dicom_store_name = f"{dicom_store_parent}/dicomStores/{dicom_store_id}"
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .dicomStores()
            .delete(name=dicom_store_name)
        )
    
        response = request.execute()
        print(f"Deleted DICOM store: {dicom_store_id}")
        return response
    
    

## What's next

  * [Export and import DICOM object instances to and from Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
