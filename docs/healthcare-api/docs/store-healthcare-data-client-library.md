---
url: https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library/
title: Store healthcare data with client libraries \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:13.145486+00:00
---

# Store healthcare data with client libraries  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store healthcare data with client libraries

This page shows you how to use the Cloud Healthcare API and the [Google API Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained#google-api-client-libraries) to complete the following tasks: 

  1. Create a Cloud Healthcare API dataset.
  2. Create one of the following data stores inside the dataset:
     * Digital Imaging and Communications in Medicine (DICOM) store
     * Fast Healthcare Interoperability Resources (FHIR) store
     * Health Level Seven International Version 2 (HL7v2) store
  3. Store and inspect a particular type of medical data in the DICOM, FHIR, or HL7v2 store.



If you're only interested in working with one type of data store, you can skip directly to that section of the quickstart after completing the steps in Before you begin and Create a dataset. 

**Note:** The Cloud Healthcare API uses [Google API Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained#google-api-client-libraries) and doesn't support [Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Cloud Healthcare API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable healthcare.googleapis.com

  8. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  9. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/healthcare.datasetAdmin, roles/healthcare.fhirStoreAdmin, roles/healthcare.dicomStoreAdmin, roles/healthcare.hl7V2StoreAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.

  10. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  11. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  12. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  13. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Cloud Healthcare API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable healthcare.googleapis.com

  16. Create local authentication credentials for your user account: 
         
         gcloud auth application-default login

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  17. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/healthcare.datasetAdmin, roles/healthcare.fhirStoreAdmin, roles/healthcare.dicomStoreAdmin, roles/healthcare.hl7V2StoreAdmin`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.




## Install the client libraries

The following samples show how to install the Google API Client Libraries:

### Go

For information on configuring a Go development environment, see [Setting up a Go development environment](https://docs.cloud.google.com/go/docs/setup).
    
    
    go get google.golang.org/api/healthcare/v1
    

### Java

For information on configuring a Java development environment, see [Setting up a Java development environment](https://docs.cloud.google.com/java/docs/setup).

If you're using [Maven](https://maven.apache.org/), add the following to your `pom.xml` file:
    
    
    <dependencyManagement>
      <dependencies>
        <dependency>
          <groupId>com.google.cloud</groupId>
          <artifactId>libraries-bom</artifactId>
          <version>26.32.0</version>
          <type>pom</type>
          <scope>import</scope>
        </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
        <groupId>com.google.apis</groupId>
        <artifactId>google-api-services-healthcare</artifactId>
        <version>v1-rev20240130-2.0.0</version>
      </dependency>
    </dependencies>

### Node.js

For information on configuring a Node.js development environment, see [Setting up a Node.js development environment](https://docs.cloud.google.com/nodejs/docs/setup).
    
    
    npm install @googleapis/healthcare
    

### Python

For information on configuring a Python development environment, see [Setting up a Python development environment](https://docs.cloud.google.com/python/docs/setup).
    
    
    # Use a virtual environment as shown in the Python development environment guide.
    pip install --upgrade google-api-python-client
    

## Create a dataset

_Datasets_ contain data stores, and data stores contain healthcare data. To use the Cloud Healthcare API, you must create at least one dataset. 

Run the following sample to create a dataset. You use this dataset throughout this quickstart.

Before running the samples, uncomment and provide the following values if necessary:

  * the ID of the Google Cloud project that you created or selected in Before you begin for the project ID
  * `my-dataset` for the dataset ID
  * `us-central1` for the dataset location



### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // createDataset creates a dataset.
    func createDataset(w io.Writer, projectID, location, datasetID string) error {
    	// Set a deadline for the dataset to become initialized.
    	ctx, cancel := context.WithTimeout(context.Background(), 2*time.Minute)
    	defer cancel()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	datasetsService := healthcareService.Projects.Locations.Datasets
    
    	parent := fmt.Sprintf("projects/%s/locations/%s", projectID, location)
    
    	resp, err := datasetsService.Create(parent, &healthcare.Dataset{}).DatasetId(datasetID).Context(ctx).Do()
    	if err != nil {
    		return fmt.Errorf("Create: %w", err)
    	}
    
    	// The dataset is not always ready to use immediately, instead a long-running operation is returned.
    	// This is how you might poll the operation to ensure the dataset is fully initialized before proceeding.
    	// Initialization usually takes less than a minute.
    	for !resp.Done {
    		time.Sleep(15 * time.Second)
    		resp, err = datasetsService.Operations.Get(resp.Name).Context(ctx).Do()
    		if err != nil {
    			return fmt.Errorf("Operations.Get(%s): %w", resp.Name, err)
    		}
    	}
    
    	fmt.Fprintf(w, "Created dataset: %q\n", resp.Name)
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
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.Dataset;
    import com.google.api.services.healthcare.v1.model.Operation;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class DatasetCreate {
      private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void datasetCreate(String projectId, String regionId, String datasetId)
          throws IOException {
        // String projectId = "your-project-id";
        // String regionId = "us-central1";
        // String datasetId = "your-dataset-id";
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure the dataset to be created.
        Dataset dataset = new Dataset();
        dataset.setTimeZone("America/Chicago");
    
        // Create request and configure any parameters.
        String parentName = String.format("projects/%s/locations/%s", projectId, regionId);
        Datasets.Create request = client.projects().locations().datasets().create(parentName, dataset);
        request.setDatasetId(datasetId);
    
        // Execute the request, wait for the operation to complete, and process the results.
        try {
          Operation operation = request.execute();
          System.out.println(operation.toPrettyString());
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
          System.out.println("Dataset created. Response content: " + operation.getResponse());
        } catch (Exception ex) {
          System.out.printf("Error during request execution: %s\n", ex.toString());
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

Before trying this sample, follow the Node.js setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Node.js API reference documentation](https://github.com/googleapis/google-api-nodejs-client/blob/main/src/apis/healthcare/README.md). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const createDataset = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      const parent = `projects/${projectId}/locations/${cloudRegion}`;
      const request = {parent, datasetId};
    
      await healthcare.projects.locations.datasets.create(request);
      console.log(`Created dataset: ${datasetId}`);
    };
    
    createDataset();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Dict type for runtime type hints.
    from typing import Dict
    
    
    def create_dataset(project_id: str, location: str, dataset_id: str) -> Dict[str, str]:
        """Creates a Cloud Healthcare API dataset.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/datasets
        before running the sample.
        See
        https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.html#create
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Google Cloud project you want
              to use.
          location: The name of the dataset's location.
          dataset_id: The ID of the dataset to create.
    
        Returns:
          A dictionary representing a long-running operation that results from
          calling the 'CreateDataset' method. Dataset creation is typically fast.
        """
        # Imports the Python built-in time module.
        import time
    
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
    
        # Imports HttpError from the Google Python API client errors module.
        from googleapiclient.errors import HttpError
    
        api_version = "v1"
        service_name = "healthcare"
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'
        # location = 'us-central1'
        # dataset_id = 'my-dataset'
        dataset_parent = f"projects/{project_id}/locations/{location}"
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .create(parent=dataset_parent, body={}, datasetId=dataset_id)
        )
    
        # Wait for operation to complete.
        start_time = time.time()
        max_time = 600  # 10 minutes, but dataset creation is typically only a few seconds.
    
        try:
            operation = request.execute()
            while not operation.get("done", False):
                # Poll until the operation finishes.
                print("Waiting for operation to finish...")
                if time.time() - start_time > max_time:
                    raise TimeoutError("Timed out waiting for operation to finish.")
                operation = (
                    client.projects()
                    .locations()
                    .datasets()
                    .operations()
                    .get(name=operation["name"])
                    .execute()
                )
                # Wait 5 seconds between each poll to the operation.
                time.sleep(5)
    
            if "error" in operation:
                raise RuntimeError(f"Create dataset operation failed: {operation['error']}")
            else:
                dataset_name = operation["response"]["name"]
                print(f"Created dataset: {dataset_name}")
                return operation
    
        except HttpError as err:
            # A common error is when the dataset already exists.
            if err.resp.status == 409:
                print(f"Dataset with ID {dataset_id} already exists.")
                return
            else:
                raise err
    
    

To complete this quickstart, choose from one of the following sections:

  * Store and view a DICOM instance
  * Store and view FHIR resources
  * Store and view an HL7v2 message



## Store and view a DICOM instance

This section shows how to complete the following tasks:

  1. Create a DICOM store.
  2. Store a DICOM instance in the DICOM store.
  3. View the DICOM instance's metadata.



The Cloud Healthcare API implements the [DICOMweb](https://www.dicomstandard.org/using/dicomweb) standard to store and access medical imaging data.

### Create a DICOM store

Before running the samples, uncomment and provide the following values if necessary:

DICOM stores exist inside datasets and hold DICOM instances. Run the following samples to create a DICOM store.

Before running the samples, uncomment and provide the following values if necessary:

  * the ID of the Google Cloud project that you created or selected in Before you begin for the project ID
  * `my-dataset` for the dataset ID
  * `us-central1` for the dataset location
  * `my-dicom-store` for the DICOM store ID



### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Java setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Java API reference documentation](https://googleapis.dev/java/google-api-services-healthcare/latest/index.html). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Node.js setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Node.js API reference documentation](https://github.com/googleapis/google-api-nodejs-client/blob/main/src/apis/healthcare/README.md). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

### Store a DICOM instance

  1. Download the [sample DICOM instance file](https://docs.cloud.google.com/healthcare-api/docs/resources/dicom_00000001_000.dcm) to your machine. The file contains a de-identified patient X-ray.

### curl
         
         curl -O https://cloud.google.com/healthcare-api/docs/resources/dicom_00000001_000.dcm

### PowerShell
         
         Invoke-WebRequest -Uri "https://cloud.google.com/healthcare-api/docs/resources/dicom_00000001_000.dcm" -OutFile $pwd/dicom_00000001_000.dcm

  2. Run the following samples to store the DICOM instance. The samples assume you're running the code from the same directory where you downloaded the DICOM instance.

Before running the samples, uncomment and provide the following values if necessary:

     * the ID of the Google Cloud project that you created or selected in Before you begin for the project ID
     * `my-dataset` for the dataset ID
     * `us-central1` for the dataset location
     * `my-dicom-store` for the DICOM store ID
     * `dicom_00000001_000.dcm` for the DICOM file name

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
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

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
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
    
    




### View DICOM instance metadata

Run the following samples to view the instance metadata.

Before running the samples, uncomment and provide the following values if necessary:

  * the ID of the Google Cloud project that you created or selected in Before you begin for the project ID
  * `my-dataset` for the dataset ID
  * `us-central1` for the dataset location
  * `my-dicom-store` for the DICOM store ID



### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Node.js setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Node.js API reference documentation](https://github.com/googleapis/google-api-nodejs-client/blob/main/src/apis/healthcare/README.md). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

After storing and viewing a DICOM instance in the Cloud Healthcare API, continue to Clean up to avoid incurring charges to your Google Cloud account for the resources used on this page.

For more information on working with DICOM data, see What's next.

## Store and view FHIR resources

This section shows how to complete the following tasks:

  1. Create a FHIR store.
  2. Store a FHIR resource in the FHIR store.
  3. View the FHIR resource's data.



The Cloud Healthcare API implements the [FHIR specification](https://docs.cloud.google.com/healthcare-api/docs/fhir) standard to store and access FHIR data.

### Create a FHIR store

FHIR stores exist inside datasets and hold FHIR resources. Run the following samples to create a FHIR store.

Before running the samples, uncomment and provide the following values if necessary:

  * the ID of the Google Cloud project that you created or selected in Before you begin for the project ID
  * `my-dataset` for the dataset ID
  * `us-central1` for the dataset location
  * `my-fhir-store` for the FHIR store ID



### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Java setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Java API reference documentation](https://googleapis.dev/java/google-api-services-healthcare/latest/index.html). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Node.js setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Node.js API reference documentation](https://github.com/googleapis/google-api-nodejs-client/blob/main/src/apis/healthcare/README.md). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

### Store a FHIR resource

Run the following samples to store a Patient resource.

Before running the samples, uncomment and provide the following values if necessary:

  * the ID of the Google Cloud project that you created or selected in Before you begin for the project ID
  * `my-dataset` for the dataset ID
  * `us-central1` for the dataset location
  * `my-fhir-store` for the FHIR store ID



### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // createFHIRResource creates an FHIR resource.
    func createFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, resourceType string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	payload := map[string]interface{}{
    		"resourceType": resourceType,
    		"language":     "FR",
    	}
    	jsonPayload, err := json.Marshal(payload)
    	if err != nil {
    		return fmt.Errorf("json.Encode: %w", err)
    	}
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    
    	call := fhirService.Create(parent, resourceType, bytes.NewReader(jsonPayload))
    	call.Header().Set("Content-Type", "application/fhir+json;charset=utf-8")
    	resp, err := call.Do()
    	if err != nil {
    		return fmt.Errorf("Create: %w", err)
    	}
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("Create: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
    	}
    	fmt.Fprintf(w, "%s", respBytes)
    
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
    import org.apache.http.entity.StringEntity;
    import org.apache.http.impl.client.HttpClients;
    
    public class FhirResourceCreate {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirResourceCreate(String fhirStoreName, String resourceType)
          throws IOException, URISyntaxException {
        // String fhirStoreName =
        //    String.format(
        //        FHIR_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-fhir-id");
        // String resourceType = "Patient";
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%sv1/%s/fhir/%s", client.getRootUrl(), fhirStoreName, resourceType);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
        StringEntity requestEntity =
            new StringEntity("{\"resourceType\": \"" + resourceType + "\", \"language\": \"en\"}");
    
        HttpUriRequest request =
            RequestBuilder.post()
                .setUri(uriBuilder.build())
                .setEntity(requestEntity)
                .addHeader("Content-Type", "application/fhir+json")
                .addHeader("Accept-Charset", "utf-8")
                .addHeader("Accept", "application/fhir+json; charset=utf-8")
                .build();
    
        // Execute the request and process the results.
        HttpResponse response = httpClient.execute(request);
        HttpEntity responseEntity = response.getEntity();
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_CREATED) {
          System.err.print(
              String.format(
                  "Exception creating FHIR resource: %s\n", response.getStatusLine().toString()));
          responseEntity.writeTo(System.err);
          throw new RuntimeException();
        }
        System.out.print("FHIR resource created: ");
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
      headers: {'Content-Type': 'application/fhir+json'},
      responseType: 'json',
    });
    
    async function createFhirResource() {
      // Replace the following body with the data for the resource you want to
      // create.
      const body = {
        name: [{use: 'official', family: 'Smith', given: ['Darcy']}],
        gender: 'female',
        birthDate: '1970-01-01',
        resourceType: 'Patient',
      };
    
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const resourceType = 'Patient';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}`;
    
      const request = {parent, type: resourceType, requestBody: body};
      const resource =
        await healthcare.projects.locations.datasets.fhirStores.fhir.create(
          request
        );
      console.log(`Created FHIR resource with ID ${resource.data.id}`);
      console.log(resource.data);
    }
    
    createFhirResource();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the types Dict and Any for runtime type hints.
    from typing import Any, Dict  # noqa: E402
    
    
    def create_patient(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
    ) -> Dict[str, Any]:
        """Creates a new Patient resource in a FHIR store.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample.
        See
        https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.fhirStores.fhir.html#create
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Cloud project you want
            to use.
          location: The name of the parent dataset's location.
          dataset_id: The name of the parent dataset.
          fhir_store_id: The name of the FHIR store that holds the Patient resource.
    
        Returns:
          A dict representing the created Patient resource.
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
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        patient_body = {
            "name": [{"use": "official", "family": "Smith", "given": ["Darcy"]}],
            "gender": "female",
            "birthDate": "1970-01-01",
            "resourceType": "Patient",
        }
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .create(parent=fhir_store_name, type="Patient", body=patient_body)
        )
        # Sets required application/fhir+json header on the googleapiclient.http.HttpRequest.
        request.headers["content-type"] = "application/fhir+json;charset=utf-8"
        response = request.execute()
    
        print(f"Created Patient resource with ID {response['id']}")
        return response
    
    

### View FHIR resource contents

Run the following samples to view information about the Patient resource.

Before running the samples, uncomment and provide the following values if necessary:

  * the ID of the Google Cloud project that you created or selected in Before you begin for the project ID
  * `my-dataset` for the dataset ID
  * `us-central1` for the dataset location
  * `my-fhir-store` for the FHIR store ID
  * `Patient` for the FHIR resource type



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
    import org.apache.http.entity.StringEntity;
    import org.apache.http.impl.client.HttpClients;
    
    public class FhirResourceSearchGet {
      private static final String FHIR_NAME =
          "projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s";
      // The endpoint URL for the Healthcare API. Required for HttpClient.
      private static final String API_ENDPOINT = "https://healthcare.googleapis.com";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirResourceSearchGet(String resourceName)
          throws IOException, URISyntaxException {
        // String resourceName =
        //    String.format(
        //        FHIR_NAME, "project-id", "region-id", "dataset-id", "fhir-store-id");
        // String resourceType = "Patient";
    
        // Instantiate the client, which will be used to interact with the service.
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%s/v1/%s", API_ENDPOINT, resourceName);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
        // To set additional parameters for search filtering, add them to the URIBuilder. For
        // example, to search for a Patient with the family name "Smith", specify the following:
        // uriBuilder.setParameter("family:exact", "Smith");
    
        HttpUriRequest request =
            RequestBuilder.get()
                .setUri(uriBuilder.build())
                .build();
    
        // Execute the request and process the results.
        HttpResponse response = httpClient.execute(request);
        HttpEntity responseEntity = response.getEntity();
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
          System.err.print(
              String.format(
                  "Exception searching GET FHIR resources: %s\n", response.getStatusLine().toString()));
          responseEntity.writeTo(System.err);
          throw new RuntimeException();
        }
        System.out.println("FHIR resource GET search results: ");
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
    
    
    // Import google-auth-library for authentication.
    const {GoogleAuth} = require('[google-auth-library](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)');
    
    const searchFhirResourcesGet = async () => {
      const auth = new GoogleAuth({
        scopes: 'https://www.googleapis.com/auth/cloud-platform',
      });
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const resourceType = 'Patient';
      const url = `https://healthcare.googleapis.com/v1/projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/${resourceType}`;
    
      const params = {};
      // Specify search filters in a params object. For example, to filter on a
      // Patient with the last name "Smith", set resourceType to "Patient" and
      // specify the following params:
      // params = {'family:exact' : 'Smith'};
      const client = await [auth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html).[getClient](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)();
      const response = await client.request({
        url,
        method: 'GET',
        params,
        responseType: 'json',
      });
      const resources = response.data.entry;
      console.log(`Resources found: ${resources.length}`);
      console.log(JSON.stringify(resources, null, 2));
    };
    
    searchFhirResourcesGet();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def search_resources_get(
        project_id,
        location,
        dataset_id,
        fhir_store_id,
        resource_type,
    ):
        """
        Uses the searchResources GET method to search for resources in the given FHIR store.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample."""
        # Imports Python's built-in "os" module
        import os
    
        # Imports the google.auth.transport.requests transport
        from google.auth.transport import requests
    
        # Imports a module to allow authentication using a service account
        from google.oauth2 import service_account
    
        # Gets credentials from the environment.
        credentials = service_account.Credentials.from_service_account_file(
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
        )
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
        # fhir_store_id = 'my-fhir-store' # replace with the FHIR store ID
        # resource_type = 'Patient'  # replace with the FHIR resource type
        url = f"{base_url}/projects/{project_id}/locations/{location}"
    
        resource_path = "{}/datasets/{}/fhirStores/{}/fhir/{}".format(
            url, dataset_id, fhir_store_id, resource_type
        )
    
        response = session.get(resource_path)
        response.raise_for_status()
    
        resources = response.json()
    
        print(
            "Using GET request, found a total of {} {} resources:".format(
                resources["total"], resource_type
            )
        )
        print(json.dumps(resources, indent=2))
    
        return resources
    
    

After storing and viewing a FHIR resource in the Cloud Healthcare API, continue to Clean up to avoid incurring charges to your Google Cloud account for the resources used in this page.

For more information on working with FHIR data, see What's next.

## Store and view an HL7v2 message

This section shows how to complete the following tasks:

  1. Create an HL7v2 store.
  2. Store an HL7v2 message in the HL7v2 store.
  3. View the HL7v2 message's data.



The HL7v2 implementation in the Cloud Healthcare API aligns with the [HL7v2 standard](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=185).

### Create an HL7v2 store

HL7v2 stores exist inside datasets and hold HL7v2 messages. Run the following samples to create an HL7v2 store.

Before running the samples, uncomment and provide the following values if necessary:

  * the ID of the Google Cloud project that you created or selected in Before you begin for the project ID
  * `my-dataset` for the dataset ID
  * `us-central1` for the dataset location
  * `my-hl7v2-store` for the HL7v2 store ID



### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Java setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Java API reference documentation](https://googleapis.dev/java/google-api-services-healthcare/latest/index.html). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Node.js setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Node.js API reference documentation](https://github.com/googleapis/google-api-nodejs-client/blob/main/src/apis/healthcare/README.md). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    
    

### Create an HL7v2 message

  1. Download the [sample HL7v2 message file](https://docs.cloud.google.com/static/healthcare-api/docs/resources/hl7v2-sample.json) to your machine:

### curl
         
         curl -O https://cloud.google.com/healthcare-api/docs/resources/hl7v2-sample.json

### PowerShell
         
         Invoke-WebRequest -Uri "https://cloud.google.com/healthcare-api/docs/resources/hl7v2-sample.json" -OutFile $pwd/hl7v2-sample.json

The HL7v2 message contains the following basic information, where it is base-64 encoded in the `data` field of the sample file:
         
         MSH|^~\&|A|SEND_FACILITY|A|A|20180101000000||TYPE^A|20180101000000|T|0.0|||AA||00|ASCII
         EVN|A00|20180101040000
         PID||14^111^^^^MRN|11111111^^^^MRN~1111111111^^^^ORGNMBR
         

  2. Run the following samples to store the HL7v2 message. The samples assume you're running the code from the same directory where you downloaded the HL7v2 message.

Before running the samples, uncomment and provide the following values if necessary:

     * the ID of the Google Cloud project that you created or selected in Before you begin for the project ID
     * `my-dataset` for the dataset ID
     * `us-central1` for the dataset location
     * `my-hl7v2-store` for the HL7v2 store ID
     * `hl7v2-sample.json` for the HL7v2 message file name

### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    	"os"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // ingestHL7V2Message ingests an HL7V2 message.
    func ingestHL7V2Message(w io.Writer, projectID, location, datasetID, hl7V2StoreID, messageFile string) error {
    	ctx := context.Background()
    
    	hl7v2message, err := os.ReadFile(messageFile)
    	if err != nil {
    		return fmt.Errorf("ReadFile: %w", err)
    	}
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	messagesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores.Messages
    
    	req := &healthcare.IngestMessageRequest{
    		Message: &healthcare.Message{
    			Data: base64.StdEncoding.EncodeToString(hl7v2message),
    		},
    	}
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s", projectID, location, datasetID, hl7V2StoreID)
    
    	resp, err := messagesService.Ingest(parent, req).Do()
    	if err != nil {
    		return fmt.Errorf("Create: %w", err)
    	}
    
    	fmt.Fprintf(w, "Ingested HL7V2 message: %q\n", resp.Message.Name)
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
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores.Messages;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.IngestMessageRequest;
    import com.google.api.services.healthcare.v1.model.IngestMessageResponse;
    import com.google.api.services.healthcare.v1.model.Message;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.nio.charset.Charset;
    import java.nio.file.Files;
    import java.nio.file.Paths;
    import java.util.Collections;
    import java.util.List;
    
    @SuppressWarnings("checkstyle:AbbreviationAsWordInName")
    public class HL7v2MessageIngest {
      private static final String HL7v2_NAME = "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s";
      private static final String MESSAGE_NAME =
          "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s/messages/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2MessageIngest(String hl7v2StoreName, String filePath) throws IOException {
        // String hl7v2StoreName =
        //    String.format(
        //        HL7v2_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-hl7v2-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Load the data from file and format it into an ingest request.
        List<String> lines = Files.readAllLines(Paths.get(filePath), Charset.defaultCharset());
        String data = String.join("\n", lines);
        Message message = new Message().setData(data);
        IngestMessageRequest ingestRequest = new IngestMessageRequest().setMessage(message);
    
        // Create request and configure any parameters.
        Messages.Ingest request =
            client
                .projects()
                .locations()
                .datasets()
                .hl7V2Stores()
                .messages()
                .ingest(hl7v2StoreName, ingestRequest);
    
        // Execute the request and process the results.
        IngestMessageResponse response = request.execute();
        System.out.println("HL7v2 message ingested: " + response.toPrettyString());
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
    const fs = require('fs');
    const util = require('util');
    const readFile = util.promisify(fs.readFile);
    
    const ingestHl7v2Message = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      // const hl7v2MessageFile = 'hl7v2-message.json';
      const hl7v2Message = JSON.parse(await readFile(hl7v2MessageFile));
    
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}`;
      const request = {parent, resource: hl7v2Message};
    
      const response =
        await healthcare.projects.locations.datasets.hl7V2Stores.messages.ingest(
          request
        );
      const data = response.data.hl7Ack;
      const buff = new Buffer.from(data, 'base64');
      const hl7Ack = buff.toString('ascii');
      console.log('Ingested HL7v2 message with ACK:\n', hl7Ack);
    };
    
    ingestHl7v2Message();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    def ingest_hl7v2_message(
        project_id, location, dataset_id, hl7v2_store_id, hl7v2_message_file
    ):
        """Ingests a new HL7v2 message from the hospital and sends a notification
        to the Cloud Pub/Sub topic. Return is an HL7v2 ACK message if the message
        was successfully stored.
    
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/hl7v2
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
        # dataset_id = 'my-dataset'  # replace with the HL7v2 store's parent dataset ID
        # hl7v2_store_id = 'my-hl7v2-store'  # replace with the HL7v2 store's ID
        # hl7v2_message_file = 'hl7v2-message.json'  # replace with the path to the HL7v2 file
        hl7v2_parent = f"projects/{project_id}/locations/{location}"
        hl7v2_store_name = "{}/datasets/{}/hl7V2Stores/{}".format(
            hl7v2_parent, dataset_id, hl7v2_store_id
        )
    
        with open(hl7v2_message_file) as hl7v2_message:
            hl7v2_message_content = json.load(hl7v2_message)
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .messages()
            .ingest(parent=hl7v2_store_name, body=hl7v2_message_content)
        )
    
        response = request.execute()
        print(f"Ingested HL7v2 message from file: {hl7v2_message_file}")
        return response
    
    

The output contains an HL7v2 message ID. You need this ID in the next section.




### View HL7v2 message contents

Run the following samples to view the HL7v2 message contents.

Before running the samples, uncomment and provide the following values if necessary:

  * the ID of the Google Cloud project that you created or selected in Before you begin for the project ID
  * `my-dataset` for the dataset ID
  * `us-central1` for the dataset location
  * `my-hl7v2-store` for the HL7v2 store ID
  * the ID in the response when you stored the message for the HL7v2 message ID



### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/base64"
    	"encoding/json"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // getHL7V2Message gets an HL7V2 message.
    func getHL7V2Message(w io.Writer, projectID, location, datasetID, hl7V2StoreID, hl7V2MessageID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	messagesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores.Messages
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s/messages/%s", projectID, location, datasetID, hl7V2StoreID, hl7V2MessageID)
    	message, err := messagesService.Get(name).Do()
    	if err != nil {
    		return fmt.Errorf("Get: %w", err)
    	}
    
    	rawData, err := base64.StdEncoding.DecodeString(message.Data)
    	if err != nil {
    		return fmt.Errorf("base64.DecodeString: %w", err)
    	}
    
    	fmt.Fprintf(w, "Got HL7V2 message.\n")
    	fmt.Fprintf(w, "Raw length: %d.\n", len(rawData))
    	fmt.Fprintf(w, "Parsed data:\n")
    	parsedJSON, _ := json.MarshalIndent(message.ParsedData, "", "  ")
    	fmt.Fprintf(w, "%s", parsedJSON)
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
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets.Hl7V2Stores.Messages;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.Message;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    @SuppressWarnings("checkstyle:AbbreviationAsWordInName")
    public class HL7v2MessageGet {
      private static final String MESSAGE_NAME =
          "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s/messages/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2MessageGet(String hl7v2MessageName) throws IOException {
        // String hl7v2MessageName =
        //    String.format(
        //        MESSAGE_NAME, "project-id", "region-id", "dataset-id", "hl7v2-id", "message-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Messages.Get request =
            client.projects().locations().datasets().hl7V2Stores().messages().get(hl7v2MessageName);
    
        // Execute the request and process the results.
        Message store = request.execute();
        System.out.println("HL7v2 message retrieved: \n" + store.toPrettyString());
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
    
    const getHl7v2Message = async () => {
      // TODO(developer): uncomment the lines beginning with 'const' before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      // The value for hl7v2MessageId is the server-generated ID returned when you
      // created or ingested the HL7v2 message in an HL7v2 store.
      // const hl7v2MessageId = 'qCnewKno44gTt3oBn4dQ0u8ZA23ibDdV9GpifD2E=';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}/messages/${hl7v2MessageId}`;
      // Use the 'FULL' enum to include all of the message fields in the response.
      const view = 'FULL';
      const request = {name, view};
    
      const hl7v2Message =
        await healthcare.projects.locations.datasets.hl7V2Stores.messages.get(
          request
        );
      console.log('Got HL7v2 message:\n', hl7v2Message.data);
    };
    
    getHl7v2Message();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def get_hl7v2_message(
        project_id, location, dataset_id, hl7v2_store_id, hl7v2_message_id
    ):
        """Gets an HL7v2 message.
    
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
        # hl7v2_message_id = '2yqbdhYHlk_ucSmWkcKOVm_N0p0OpBXgIlVG18rB-cw='  # replace with the HL7v2 message ID that was returned by the server
        hl7v2_parent = f"projects/{project_id}/locations/{location}"
        hl7v2_message_name = "{}/datasets/{}/hl7V2Stores/{}/messages/{}".format(
            hl7v2_parent, dataset_id, hl7v2_store_id, hl7v2_message_id
        )
    
        msgs = client.projects().locations().datasets().hl7V2Stores().messages()
        message = msgs.get(name=hl7v2_message_name).execute()
    
        print("Name: {}".format(message.get("name")))
        print("Data: {}".format(message.get("data")))
        print("Creation time: {}".format(message.get("createTime")))
        print("Sending facility: {}".format(message.get("sendFacility")))
        print("Time sent: {}".format(message.get("sendTime")))
        print("Message type: {}".format(message.get("messageType")))
        print("Patient IDs:")
        patient_ids = message.get("patientIds")
        for patient_id in patient_ids:
            print("\tPatient value: {}".format(patient_id.get("value")))
            print("\tPatient type: {}".format(patient_id.get("type")))
        print("Labels: {}".format(message.get("labels")))
    
        print(message)
        return message
    
    

After storing and viewing an HL7v2 message in the Cloud Healthcare API, continue to Clean up to avoid incurring charges to your Google Cloud account for the resources used in this page.

For more information on working with HL7v2 data, see What's next.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

If you created a new project for this quickstart, follow the steps in Delete the project. Otherwise, follow the steps in Delete the dataset.

  1. Optional: Revoke the authentication credentials that you created, and delete the local credential file. 
         
         gcloud auth application-default revoke

  2. Optional: Revoke credentials from the gcloud CLI. 
         
         gcloud auth revoke




### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete the dataset

If you no longer need the dataset created in this quickstart, you can delete it. Deleting a dataset permanently deletes the dataset and any FHIR, HL7v2, or DICOM stores it contains.

Before running the samples, uncomment and provide the following values if necessary:

  * the ID of the Google Cloud project that you created or selected in Before you begin for the project ID
  * `my-dataset` for the dataset ID
  * `us-central1` for the dataset location



### Go

Before trying this sample, follow the Go setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Go API reference documentation](https://pkg.go.dev/google.golang.org/api/healthcare/v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // deleteDataset deletes the given dataset.
    func deleteDataset(w io.Writer, projectID, location, datasetID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	datasetsService := healthcareService.Projects.Locations.Datasets
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s", projectID, location, datasetID)
    	if _, err := datasetsService.Delete(name).Do(); err != nil {
    		return fmt.Errorf("Delete: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted dataset: %q\n", name)
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
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class DatasetDelete {
      private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void datasetDelete(String datasetName) throws IOException {
        // String datasetName =
        //     String.format(DATASET_NAME, "your-project-id", "your-region-id", "your-dataset-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Datasets.Delete request = client.projects().locations().datasets().delete(datasetName);
    
        // Execute the request and process the results.
        request.execute();
        System.out.println("Dataset deleted.");
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
    
    const deleteDataset = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
      const request = {name: parent};
    
      await healthcare.projects.locations.datasets.delete(request);
      console.log(`Deleted dataset: ${datasetId}`);
    };
    
    deleteDataset();

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def delete_dataset(project_id: str, location: str, dataset_id: str) -> None:
        """Deletes a dataset.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/datasets
        before running the sample.
        See https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.html#delete
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Google Cloud project you want
              to use.
          location: The name of the dataset's location.
          dataset_id: The name of the dataset to delete.
    
        Returns:
          An empty response body.
        """
        # Imports HttpError from the Google Python API client errors module.
        # Imports the Google API Discovery Service.
        from googleapiclient import discovery
        from googleapiclient.errors import HttpError
    
        api_version = "v1"
        service_name = "healthcare"
        # Returns an authorized API client by discovering the Healthcare API
        # and using GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = discovery.build(service_name, api_version)
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # project_id = 'my-project'
        # location = 'us-central1'
        # dataset_id = 'my-dataset'
        dataset_name = f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
    
        request = client.projects().locations().datasets().delete(name=dataset_name)
    
        try:
            request.execute()
            print(f"Deleted dataset: {dataset_id}")
        except HttpError as err:
            raise err
    
    

## How did it go?

It worked!  **Great!** What did you like about the quickstart? What could we have done better?  Let us know!.  I got stuck.  **We're sorry to hear that.** Let us know what went wrong. We'll want to fix it. 

## What's next

See the following sections for general information on the Cloud Healthcare API and how to perform the tasks in this quickstart using another interface:

  * Read an [overview of Cloud Healthcare API concepts](https://docs.cloud.google.com/healthcare-api/docs/concepts/introduction)
  * [Store healthcare data with `curl` or PowerShell](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-rest)
  * [Store healthcare data with the Google Cloud console](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-console)
  * [Store healthcare data with the gcloud CLI](https://docs.cloud.google.com/healthcare-api/docs/store-healthcare-data-gcloud)



### DICOM

  * [Create and manage DICOM stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom)
  * [Connect a PACS to the Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-connect-pacs)
  * [Use the DICOMweb standard](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicomweb)
  * [Import and export DICOM data using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/dicom-import-export)



See the [DICOM conformance statement](https://docs.cloud.google.com/healthcare-api/docs/dicom) for information on how the Cloud Healthcare API implements the DICOMweb standard.

### FHIR

  * [Create and manage FHIR stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir)
  * [Create and manage FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources)
  * [Import and export FHIR data using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-import-export)



See the [FHIR conformance statement](https://docs.cloud.google.com/healthcare-api/docs/fhir) for information on how the Cloud Healthcare API implements the FHIR standard.

### HL7v2

  * [Create and manage HL7v2 stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2)
  * [Create and manage HL7v2 messages](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages)
  * [Transmit HL7v2 messages over TCP/IP connections](https://docs.cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter)
  * [Import and export HL7v2 messages using Cloud Storage](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-import-export)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
