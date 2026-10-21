---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2/
title: Creating and managing HL7v2 stores \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:01:50.330901+00:00
---

# Creating and managing HL7v2 stores  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Creating and managing HL7v2 stores Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create, edit, view, and delete [Health Level Seven Version 2.x (HL7v2)](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185) stores. HL7v2 stores hold HL7v2 messages, which are used to transmit clinical data between systems.

## Creating an HL7v2 store

Before you can create an HL7v2 store, you need to [create a dataset](https://docs.cloud.google.com/healthcare-api/docs/how-tos/datasets).

When creating an HL7v2 store, specify the [`V3`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#ParserVersion.ENUM_VALUES.V3) parser version. You can't change the parser version after creating the HL7v2 store.

The following samples show how to create an HL7v2 store using the V3 parser.

### Console

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset where you want to create the HL7v2 store. The **Dataset** page is displayed.

  3. Click _add_box_ **Create data store**. The **Create data store** page is displayed.

  4. In the **Type** menu, select **HL7v2**.

  5. In the **ID** field, enter a name for the HL7v2 store. The name must be unique in the dataset. See [Permitted characters and size requirements](https://docs.cloud.google.com/healthcare-api/docs/requirements#permitted_characters_and_size_requirements) for more naming requirements.

  6. Click **Next**. The **Configure your HL7v2 store** section is displayed.

  7. Configure the following settings:

     1. In the **Version** section, leave the default **V3** selection unchanged.
     2. To allow the creation and ingestion of HL7v2 messages with no header, select **Allow null message headers (MSH)**.
     3. To set a custom segment terminator, click **Set a custom segment terminator** and enter the terminator in the **Segment terminator** field. For more information, see [Setting the segment terminator](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages#setting_the_segment_terminator).
     4. To reject incoming HL7v2 messages with the same raw bytes as an HL7v2 message that already exists in the HL7v2 store, select **Reject duplicate messages**.
  8. Click **Next**. The **Receive Cloud Pub/Sub notifications** section is displayed.

  9. If you want to receive Pub/Sub notifications when a clinical event occurs in your HL7v2 store, specify the Pub/Sub topic. The topic must exist before you can configure it on the HL7v2 store.

  10. Click **Next**. The **Add labels to organize your data stores** section is displayed.

  11. To add one or more key/value labels to the HL7v2 store, click _add_ **Add label**. For more information on resource labels, see [Using resource labels](https://docs.cloud.google.com/healthcare-api/docs/how-tos/labeling-resources#adding_a_label).

  12. Click **Create**. The **Dataset** page is displayed, and the HL7v2 store is displayed in the **Data stores** table.




### gcloud

To create an HL7v2 store, run the [`gcloud healthcare hl7v2-stores create`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/create) command.

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the HL7v2 store's parent dataset
  * `HL7V2_STORE_ID`: an identifier for the HL7v2 store subject to the [HL7v2 store character and size requirements](https://docs.cloud.google.com/healthcare-api/docs/requirements#permitted_characters_and_size_requirements)



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores create HL7V2_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION \
      --parser-version=v3

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores create HL7V2_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION `
      --parser-version=v3

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores create HL7V2_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION ^
      --parser-version=v3

You should receive a response similar to the following:

#### Response
    
    
    Created hl7V2Store [HL7V2_STORE_ID].

### REST

To create an HL7v2 store, use the [`projects.locations.datasets.hl7V2Stores.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/create) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the HL7v2 store's parent dataset
  * `HL7V2_STORE_ID`: an identifier for the HL7v2 store subject to the [HL7v2 store character and size requirements](https://docs.cloud.google.com/healthcare-api/docs/requirements#permitted_characters_and_size_requirements)



Request JSON body: 
    
    
    {
      "parserConfig": {
        "version": "V3"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "parserConfig": {
        "version": "V3"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores?hl7V2StoreId=HL7V2_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "parserConfig": {
        "version": "V3"
      }
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores?hl7V2StoreId=HL7V2_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID",
      "parserConfig": {
        "version": "V3"
      }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // createHL7V2Store creates an HL7V2 store.
    func createHL7V2Store(w io.Writer, projectID, location, datasetID, hl7V2StoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores
    
    	// Set the HL7v2 store parser version to V3.
    	store := &healthcare.Hl7V2Store{ParserConfig: &healthcare.ParserConfig{Version: "V3"}}
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s", projectID, location, datasetID)
    
    	resp, err := storesService.Create(parent, store).Hl7V2StoreId(hl7V2StoreID).Do()
    	if err != nil {
    		return fmt.Errorf("Create: %w", err)
    	}
    
    	fmt.Fprintf(w, "Created HL7V2 store: %q\n", resp.Name)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.Hl7V2Store;
    import com.google.api.services.healthcare.v1.model.ParserConfig;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    import java.util.HashMap;
    import java.util.Map;
    
    public class Hl7v2StoreCreate {
      private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2StoreCreate(String datasetName, String hl7v2StoreId) throws IOException {
        // String datasetName =
        // String.format(DATASET_NAME, "your-project-id", "your-region-id",
        // "your-dataset-id");
        // String hl7v2StoreId = "your-hl7v25-id"
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure the store to be created.
        Map<String, String> labels = new HashMap<>();
        labels.put("key1", "value1");
        labels.put("key2", "value2");
        Hl7V2Store content = 
            new Hl7V2Store().setLabels(labels).setParserConfig(new ParserConfig().setVersion("V3"));
    
        // Create request and configure any parameters.
        Hl7V2Stores.Create request = client
            .projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .create(datasetName, content)
            .setHl7V2StoreId(hl7v2StoreId);
    
        // Execute the request and process the results.
        Hl7V2Store response = request.execute();
        System.out.println("Hl7V2Store store created: " + response.toPrettyString());
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
    });
    
    const createHl7v2Store = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
      const request = {
        parent,
        hl7V2StoreId: hl7v2StoreId,
        resource: {
          parserConfig: {
            version: 'V3',
          },
        },
      };
    
      await healthcare.projects.locations.datasets.hl7V2Stores.create(request);
      console.log(`Created HL7v2 store: ${hl7v2StoreId}`);
    };
    
    createHl7v2Store();

### Python
    
    
    def create_hl7v2_store(project_id, location, dataset_id, hl7v2_store_id):
        """Creates a new HL7v2 store within the parent dataset.
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
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
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset ID
        # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
        hl7v2_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
    
        # Use the V3 parser. Immutable after HL7v2 store creation.
        body = {"parserConfig": {"version": "V3"}}
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .create(parent=hl7v2_store_parent, body=body, hl7V2StoreId=hl7v2_store_id)
        )
    
        response = request.execute()
        print(f"Created HL7v2 store: {hl7v2_store_id}")
        return response
    
    

## Use Pub/Sub topics and filters

Using [Pub/Sub](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub) and filters with HL7v2 stores is a common use case, particularly when [transmitting HL7v2 messages over TCP/IP connections](https://docs.cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter).

Some of the examples on this page show how to configure an existing Pub/Sub topic to which the Cloud Healthcare API sends notifications of clinical events in an HL7v2 store. By specifying a list of existing Pub/Sub topics and filters, the Cloud Healthcare API can send notifications to multiple topics, and you can use the filters to restrict which notifications are sent. For more information on how to configure Pub/Sub topics and filters, see [HL7v2 notifications](https://docs.cloud.google.com/healthcare-api/docs/concepts/pubsub#hl7v2_notifications) and [View HL7v2 notifications](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub#view_hl7v2_notifications).

## Editing an HL7v2 store

The following samples show how to edit the list of [Pub/Sub](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub) topics and filters that the Cloud Healthcare API uses to send notifications of HL7v2 store changes.

Several samples also show how to edit the [labels](https://docs.cloud.google.com/healthcare-api/docs/how-tos/labeling-resources) on the HL7v2 store.

When specifying a Pub/Sub topic, enter the qualified URI to the topic, as shown in the following sample: 
    
    
    projects/PROJECT_ID/topics/PUBSUB_TOPIC

For notifications to work, you must grant additional permissions to the **Cloud Healthcare Service Agent** [service account](https://docs.cloud.google.com/iam/docs/service-accounts). For more information, see [DICOM, FHIR, and HL7v2 store Pub/Sub permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#dicom_fhir_and_hl7v2_store_cloud_pubsub_permissions). 

### Console

To edit an HL7v2 store, complete the following steps: 

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the HL7v2 store you want to edit.
  3. In the **Data stores** list, click the data store you want to edit.
  4. To edit the HL7v2 store's configuration, click **HL7v2 Store Configuration**.  
  
For more information on the HL7v2 store's configuration options, see [Creating an HL7v2 store](https://cloud.google.com/healthcare-api/docs/how-tos/hl7v2#creating_an_hl7v2_store).
  5. If you want to configure a Pub/Sub topic for the data store, click **Add Pub/Sub topic** and select the topic name. When specifying a Pub/Sub topic, enter the qualified URI to the topic, as shown in the following sample: 
         
         projects/PROJECT_ID/topics/PUBSUB_TOPIC

  6. If you have added a Pub/Sub topic, click **Done**.
  7. To add one or more labels to the store, click  edit  **Labels** , click **Add label** , and enter the key/value label. For more information on resource labels, see [Using resource labels](https://cloud.google.com/healthcare-api/docs/how-tos/labeling-resources#adding_a_label).
  8. Click **Save**. 



### gcloud

The gcloud CLI doesn't support this action. Instead, use the Google Cloud console, `curl`, PowerShell, or your preferred language.

### REST

To edit an HL7v2 store, use the [`projects.locations.datasets.hl7V2Stores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/patch) method.

Before running the following samples, you must create at least one [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/admin#create_a_topic) in your project.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID
  * PUBSUB_TOPIC1: a Pub/Sub topic to which messages are published when an event occurs in a data store
  * FILTER1: a string used to match messages published to PUBSUB_TOPIC1

See [`filter`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#Hl7V2NotificationConfig.FIELDS.filter) for examples of valid filter values.

  * PUBSUB_TOPIC2: a Pub/Sub topic to which messages are published
  * FILTER2: a string used to match messages published to PUBSUB_TOPIC2
  * KEY1: the first label key
  * VALUE1: the first label value
  * KEY2: the second label key
  * VALUE2: the second label value



Request JSON body: 
    
    
    {
      'notificationConfigs': [
        {
          'pubsubTopic': 'projects/PROJECT_ID/topics/PUBSUB_TOPIC1',
          'filter' : 'FILTER1'
        },
        {
          'pubsubTopic': 'projects/PROJECT_ID/topics/PUBSUB_TOPIC2',
          'filter': 'FILTER2'
        },
      ],
      'labels': {
        'KEY1':'VALUE1',
        'KEY2':'VALUE2'
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      'notificationConfigs': [
        {
          'pubsubTopic': 'projects/PROJECT_ID/topics/PUBSUB_TOPIC1',
          'filter' : 'FILTER1'
        },
        {
          'pubsubTopic': 'projects/PROJECT_ID/topics/PUBSUB_TOPIC2',
          'filter': 'FILTER2'
        },
      ],
      'labels': {
        'KEY1':'VALUE1',
        'KEY2':'VALUE2'
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID?updateMask=notificationConfigs,labels"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      'notificationConfigs': [
        {
          'pubsubTopic': 'projects/PROJECT_ID/topics/PUBSUB_TOPIC1',
          'filter' : 'FILTER1'
        },
        {
          'pubsubTopic': 'projects/PROJECT_ID/topics/PUBSUB_TOPIC2',
          'filter': 'FILTER2'
        },
      ],
      'labels': {
        'KEY1':'VALUE1',
        'KEY2':'VALUE2'
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID?updateMask=notificationConfigs,labels" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/patch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID",
      "labels": {
        "KEY1": "VALUE1",
        "KEY2": "VALUE2"
      },
      "notificationConfigs": [
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/PUBSUB_TOPIC1",
          "filter": "FILTER1"
        },
        {
          "pubsubTopic": "projects/PROJECT_ID/topics/PUBSUB_TOPIC2",
          "filter": "FILTER2"
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
    
    // patchHL7V2Store updates (patches) a HL7V2 store by updating its Pub/sub topic name.
    func patchHL7V2Store(w io.Writer, projectID, location, datasetID, hl7v2StoreID, topicName string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s", projectID, location, datasetID, hl7v2StoreID)
    
    	if _, err := storesService.Patch(name, &healthcare.Hl7V2Store{
    		NotificationConfigs: []*healthcare.Hl7V2NotificationConfig{
    			{
    				PubsubTopic: topicName, // format is "projects/*/locations/*/topics/*"
    			},
    		},
    	}).UpdateMask("notificationConfigs").Do(); err != nil {
    		return fmt.Errorf("Patch: %w", err)
    	}
    
    	fmt.Fprintf(w, "Patched HL7V2 store %s with Pub/sub topic %s\n", datasetID, topicName)
    
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.Hl7V2NotificationConfig;
    import com.google.api.services.healthcare.v1.model.Hl7V2Store;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.Collections;
    import java.util.List;
    
    public class Hl7v2StorePatch {
      private static final String HL7v2_NAME = "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void patchHl7v2Store(String hl7v2StoreName, String pubsubTopic) throws IOException {
        // String hl7v2StoreName =
        //    String.format(
        //        HL7v2_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-hl7v2-id");
        // String pubsubTopic = "projects/your-project-id/topics/your-pubsub-topic";
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Fetch the initial state of the HL7v2 store.
        Hl7V2Stores.Get getRequest =
            client.projects().locations().datasets().hl7V2Stores().get(hl7v2StoreName);
        Hl7V2Store store = getRequest.execute();
    
        Hl7V2NotificationConfig notificationConfig = new Hl7V2NotificationConfig();
        notificationConfig.setPubsubTopic(pubsubTopic);
        List<Hl7V2NotificationConfig> notificationConfigs = new ArrayList<Hl7V2NotificationConfig>();
        notificationConfigs.add(notificationConfig);
        // Update the Hl7v2Store fields as needed as needed. For a full list of Hl7v2Store fields, see:
        // https://cloud.google.com/healthcare/docs/reference/rest/v1/projects.locations.datasets.hl7V2Store#Hl7v2Store
        store.setNotificationConfigs(notificationConfigs);
    
        // Create request and configure any parameters.
        Hl7V2Stores.Patch request =
            client
                .projects()
                .locations()
                .datasets()
                .hl7V2Stores()
                .patch(hl7v2StoreName, store)
                .setUpdateMask("notificationConfigs");
    
        // Execute the request and process the results.
        store = request.execute();
        System.out.println("HL7v2 store patched: \n" + store.toPrettyString());
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
    
    const patchHl7v2Store = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      // const pubsubTopic = 'my-topic'
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}`;
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
    
      await healthcare.projects.locations.datasets.hl7V2Stores.patch(request);
      console.log(
        `Patched HL7v2 store ${hl7v2StoreId} with Cloud Pub/Sub topic ${pubsubTopic}`
      );
    };
    
    patchHl7v2Store();

### Python
    
    
    def patch_hl7v2_store(project_id, location, dataset_id, hl7v2_store_id):
        """Updates the HL7v2 store.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
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
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset
        # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
        hl7v2_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        hl7v2_store_name = f"{hl7v2_store_parent}/hl7V2Stores/{hl7v2_store_id}"
    
        # TODO(developer): Replace with the full URI of an existing Pub/Sub topic
        patch = {"notificationConfigs": None}
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .patch(name=hl7v2_store_name, updateMask="notificationConfigs", body=patch)
        )
    
        response = request.execute()
        print(f"Patched HL7v2 store {hl7v2_store_id} with Cloud Pub/Sub topic: None")
        return response
    
    

## Getting HL7v2 store details

The following samples show how to get details about an HL7v2 store.

### Console

To view an HL7v2 store's details:

  1. In the Google Cloud console, go to the **Datasets** page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the HL7v2 store you want to view.
  3. Click the name of the HL7v2 store.

The **Data store details** page displays the details of the selected an HL7v2 store.




### gcloud

To get details about an HL7v2 store, run the [`gcloud healthcare hl7v2-stores describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/describe) command. 

Before using any of the command data below, make the following replacements: 

  * LOCATION: the dataset location
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores describe HL7V2_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores describe HL7V2_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores describe HL7V2_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION

You should receive a response similar to the following.

If you configured any fields in the [`Hl7V2Store`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#resource:-hl7v2store) resource, they also appear in the response.

#### Response
    
    
    ...
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID
    ...
    

### REST

To get details about an HL7v2 store, use the [`projects.locations.datasets.hl7V2Stores.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/get) method. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a response similar to the following.

If you configured any fields in the [`Hl7V2Store`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#resource:-hl7v2store) resource, they also appear in the response.

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID"
      ...
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // getHL7V2Store gets an HL7V2 store.
    func getHL7V2Store(w io.Writer, projectID, location, datasetID, hl7v2StoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s", projectID, location, datasetID, hl7v2StoreID)
    
    	store, err := storesService.Get(name).Do()
    	if err != nil {
    		return fmt.Errorf("Get: %w", err)
    	}
    
    	fmt.Fprintf(w, "Got HL7V2 store: %q\n", store.Name)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.Hl7V2Store;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class Hl7v2StoreGet {
      private static final String HL7v2_NAME = "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2eStoreGet(String hl7v2StoreName) throws IOException {
        // String hl7v2StoreName =
        //    String.format(
        //        HL7v2_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-hl7v2-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Hl7V2Stores.Get request =
            client.projects().locations().datasets().hl7V2Stores().get(hl7v2StoreName);
    
        // Execute the request and process the results.
        Hl7V2Store store = request.execute();
        System.out.println("HL7v2 store retrieved: \n" + store.toPrettyString());
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
    
    const getHl7v2Store = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}`;
      const request = {name};
    
      const hl7v2Store =
        await healthcare.projects.locations.datasets.hl7V2Stores.get(request);
      console.log(hl7v2Store.data);
    };
    
    getHl7v2Store();

### Python
    
    
    def get_hl7v2_store(project_id, location, dataset_id, hl7v2_store_id):
        """Gets the specified HL7v2 store.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
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
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset
        # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
        hl7v2_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        hl7v2_store_name = f"{hl7v2_store_parent}/hl7V2Stores/{hl7v2_store_id}"
    
        hl7v2_stores = client.projects().locations().datasets().hl7V2Stores()
        hl7v2_store = hl7v2_stores.get(name=hl7v2_store_name).execute()
    
        print("Name: {}".format(hl7v2_store.get("name")))
        if hl7v2_store.get("notificationConfigs") is not None:
            print("Notification configs:")
            for notification_config in hl7v2_store.get("notificationConfigs"):
                print(
                    "\tPub/Sub topic: {}".format(notification_config.get("pubsubTopic")),
                    "\tFilter: {}".format(notification_config.get("filter")),
                )
    
        return hl7v2_store
    
    

## Listing the HL7v2 stores in a dataset

The following samples show how to list the HL7v2 stores in a dataset.

### Console

To view the data stores in a dataset: 

  1. In the Google Cloud console, go to the **Datasets** page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the data store you want to view. 



### gcloud

To list the HL7v2 stores in a dataset, run the [`gcloud healthcare hl7v2-stores list`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/list) command. 

Before using any of the command data below, make the following replacements: 

  * LOCATION: the dataset location
  * DATASET_ID: the HL7v2 store's parent dataset



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores list --dataset=DATASET_ID \
      --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores list --dataset=DATASET_ID `
      --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores list --dataset=DATASET_ID ^
      --location=LOCATION

You should receive a response similar to the following.

If you configured any fields in the [`Hl7V2Store`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#resource:-hl7v2store) resource, they also appear in the response.
    
    
    ID              LOCATION     TOPIC
    HL7V2_STORE_ID  LOCATION     projects/PROJECT_ID/topics/PUBSUB_TOPIC                                   PUBSUB_TOPIC
    ...
    

### REST

To list the HL7v2 stores in a dataset, use the [`projects.locations.datasets.hl7V2Stores.list`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/list) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the HL7v2 store's parent dataset



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a response similar to the following.

If you configured any fields in the [`Hl7V2Store`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores#resource:-hl7v2store) resource, they also appear in the response.

#### Response
    
    
    {
      "hl7V2Stores": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID"
          ...
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
    
    // listHL7V2Stores prints a list of HL7V2 stores to w.
    func listHL7V2Stores(w io.Writer, projectID, location, datasetID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s", projectID, location, datasetID)
    
    	resp, err := storesService.List(parent).Do()
    	if err != nil {
    		return fmt.Errorf("Create: %w", err)
    	}
    
    	fmt.Fprintln(w, "HL7V2 stores:")
    	for _, s := range resp.Hl7V2Stores {
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
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.Hl7V2Store;
    import com.google.api.services.healthcare.v1.model.ListHl7V2StoresResponse;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.Collections;
    import java.util.List;
    
    public class Hl7v2StoreList {
      private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2StoreList(String datasetName) throws IOException {
        // String datasetName =
        //     String.format(DATASET_NAME, "your-project-id", "your-region-id", "your-dataset-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Results are paginated, so multiple queries may be required.
        String pageToken = null;
        List<Hl7V2Store> stores = new ArrayList<>();
        do {
          // Create request and configure any parameters.
          Hl7V2Stores.List request =
              client
                  .projects()
                  .locations()
                  .datasets()
                  .hl7V2Stores()
                  .list(datasetName)
                  .setPageSize(100) // Specify pageSize up to 1000
                  .setPageToken(pageToken);
    
          // Execute response and collect results.
          ListHl7V2StoresResponse response = request.execute();
          stores.addAll(response.getHl7V2Stores());
    
          // Update the page token for the next request.
          pageToken = response.getNextPageToken();
        } while (pageToken != null);
    
        // Print results.
        System.out.printf("Retrieved %s HL7v2 stores: \n", stores.size());
        for (Hl7V2Store data : stores) {
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
    
    const listHl7v2Stores = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
      const request = {parent};
    
      const hl7v2Stores =
        await healthcare.projects.locations.datasets.hl7V2Stores.list(request);
      console.log(hl7v2Stores.data);
    };
    
    listHl7v2Stores();

### Python
    
    
    def list_hl7v2_stores(project_id, location, dataset_id):
        """Lists the HL7v2 stores in the given dataset.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
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
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset
        hl7v2_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
    
        hl7v2_stores = (
            client.projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .list(parent=hl7v2_store_parent)
            .execute()
            .get("hl7V2Stores", [])
        )
    
        for hl7v2_store in hl7v2_stores:
            print("HL7v2 store:\nName: {}".format(hl7v2_store.get("name")))
            if hl7v2_store.get("notificationConfigs") is not None:
                print("Notification configs:")
                for notification_config in hl7v2_store.get("notificationConfigs"):
                    print(
                        "\tPub/Sub topic: {}".format(
                            notification_config.get("pubsubTopic")
                        ),
                        "\tFilter: {}".format(notification_config.get("filter")),
                    )
        return hl7v2_stores
    
    

## Deleting an HL7v2 store

**Caution:** Deleting an HL7v2 store also deletes the data in the HL7v2 store. If deleted, this data cannot be recovered.

The following samples show how to delete an HL7v2 store.

### Console

To delete a data store: 

  1. In the Google Cloud console, go to the **Datasets** page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the data store you want to delete.
  3. Choose **Delete** from the **Actions** drop-down list for the data store that you want to delete. 
  4. To confirm, type the data store name and then click **Delete**. 



### gcloud

To delete an HL7v2 store, run the [`gcloud healthcare hl7v2-stores delete`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/delete) command. 

Before using any of the command data below, make the following replacements: 

  * LOCATION: the dataset location
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores delete HL7V2_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores delete HL7V2_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare hl7v2-stores delete HL7V2_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION

To confirm, type **Y**. You should receive a response similar to the following. 
    
    
    Deleted hl7v2Store [HL7V2_STORE_ID].
    

### REST

To delete an HL7v2 store, use the [`projects.locations.datasets.hl7V2Stores.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/delete) method. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the HL7v2 store's parent dataset
  * HL7V2_STORE_ID: the HL7v2 store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

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
    
    // deleteHL7V2Store deletes an HL7V2 store.
    func deleteHL7V2Store(w io.Writer, projectID, location, datasetID, hl7V2StoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s", projectID, location, datasetID, hl7V2StoreID)
    
    	if _, err := storesService.Delete(name).Do(); err != nil {
    		return fmt.Errorf("Delete: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted HL7V2 store: %q\n", name)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class Hl7v2StoreDelete {
      private static final String HL7v2_NAME = "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2StoreDelete(String hl7v2StoreName) throws IOException {
        // String hl7v2StoreName =
        //    String.format(
        //        HL7v2_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-hl7v2-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Hl7V2Stores.Delete request =
            client.projects().locations().datasets().hl7V2Stores().delete(hl7v2StoreName);
    
        // Execute the request and process the results.
        request.execute();
        System.out.println("HL7v2 store deleted.");
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
    
    const deleteHl7v2Store = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}`;
      const request = {name};
    
      await healthcare.projects.locations.datasets.hl7V2Stores.delete(request);
      console.log(`Deleted HL7v2 store: ${hl7v2StoreId}`);
    };
    
    deleteHl7v2Store();

### Python
    
    
    def delete_hl7v2_store(project_id, location, dataset_id, hl7v2_store_id):
        """Deletes the specified HL7v2 store.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
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
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset
        # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
        hl7v2_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        hl7v2_store_name = f"{hl7v2_store_parent}/hl7V2Stores/{hl7v2_store_id}"
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .delete(name=hl7v2_store_name)
        )
    
        response = request.execute()
        print(f"Deleted HL7v2 store: {hl7v2_store_id}")
        return response
    
    

## What's next

  * [Read the conceptual documentation on how HL7v2 is implemented in the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/concepts/hl7v2).
  * [Learn how to create and manage HL7v2 messages](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
