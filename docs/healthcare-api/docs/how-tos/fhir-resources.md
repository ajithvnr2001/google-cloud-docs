---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources/
title: Creating and managing FHIR resources \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:58.430612+00:00
---

# Creating and managing FHIR resources  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Creating and managing FHIR resources Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to create, update, patch, view, list, retrieve, and delete FHIR resources.

A FHIR resource can contain data about a patient, a device, an observation, and more. For a full list of FHIR resources, see the FHIR Resource Index ([DSTU2](https://www.hl7.org/fhir/dstu2/resourcelist.html), [STU3](https://www.hl7.org/fhir/stu3/resourcelist.html), [R4](https://www.hl7.org/fhir/r4/resourcelist.html), or [R5](https://www.hl7.org/fhir/r5/resourcelist.html)).

The REST samples on this page work with an R4 FHIR store, and are not guaranteed to work if you're using a DSTU2 or STU3 FHIR store. If you're using a DSTU2 or STU3 FHIR store, see the [official FHIR documentation](https://www.hl7.org/fhir/) for information on how to convert the samples to the FHIR version you're using.

The Go, Java, Node.js, and Python samples work with an STU3 FHIR store.

## Creating a FHIR resource

Before you can create FHIR resources, you need to [create a FHIR store](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir).

**Important:** FHIR stores only support the UTF-8 character set. Resources will be rejected if they contain any characters not in the UTF-8 character set.

The REST and Python samples show how to create the following FHIR resources:

  1. A Patient ([DSTU2](https://www.hl7.org/fhir/DSTU2/patient.html), [STU3](https://www.hl7.org/fhir/STU3/patient.html), [R4](https://www.hl7.org/fhir/R4/patient.html), and [R5](https://www.hl7.org/fhir/R5/patient.html)) resource
  2. An Encounter ([DSTU2](https://www.hl7.org/fhir/DSTU2/encounter.html), [STU3](https://www.hl7.org/fhir/STU3/encounter.html), [R4](https://www.hl7.org/fhir/R4/encounter.html), and [R5](https://www.hl7.org/fhir/R5/encounter.html)) resource for the Patient
  3. An Observation ([DSTU2](https://www.hl7.org/fhir/DSTU2/observation.html), [STU3](https://www.hl7.org/fhir/STU3/observation.html), [R4](https://www.hl7.org/fhir/R4/observation.html), and [R5](https://www.hl7.org/fhir/R5/observation.html)) resource for the Encounter



The samples for all other languages show how to create a generic FHIR resource.

For more information, see [`projects.locations.datasets.fhirStores.fhir.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/create).

The following REST samples work with R4 FHIR stores. The Go, Java, Node.js, and Python samples work with STU3 FHIR stores.

### Console

To upload FHIR resource(s) using JSON to a FHIR store, complete the following steps:

  1. In the Google Cloud console, go to the **FHIR Viewer**. 

[Go to FHIR Viewer](https://console.cloud.google.com/healthcare/fhirviewer)

  2. In the **FHIR Store** drop-down list, select a dataset, and then select a FHIR store in the dataset. 
  3. Click the **Upload** tab. 
  4. In the text area, enter a valid FHIR resource in JSON format. The following is an example: 
         
         {
           "name": [
             {
               "use": "official",
               "family": "Smith",
               "given": [
                 "Darcy"
               ]
             }
           ],
           "gender": "female",
           "birthDate": "1970-01-01",
           "resourceType": "Patient"
         }
         

_Note:_ You can also input a JSON array of multiple FHIR resource objects. 
  5. Click **Save**. After upload completes, you can view the resources in FHIR Viewer. See [Getting a FHIR resource](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources#getting_a_fhir_resource). 



### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID



Request JSON body: 
    
    
    {
      "name": [
        {
          "use": "official",
          "family": "Smith",
          "given": [
            "Darcy"
          ]
        }
      ],
      "gender": "female",
      "birthDate": "1970-01-01",
      "resourceType": "Patient"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "name": [
        {
          "use": "official",
          "family": "Smith",
          "given": [
            "Darcy"
          ]
        }
      ],
      "gender": "female",
      "birthDate": "1970-01-01",
      "resourceType": "Patient"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "name": [
        {
          "use": "official",
          "family": "Smith",
          "given": [
            "Darcy"
          ]
        }
      ],
      "gender": "female",
      "birthDate": "1970-01-01",
      "resourceType": "Patient"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "birthDate": "1970-01-01",
      "gender": "female",
      "id": "PATIENT_ID",
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "name": [
        {
          "family": "Smith",
          "given": [
            "Darcy"
          ],
          "use": "official"
        }
      ],
      "resourceType": "Patient"
    }
    

### Go
    
    
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
    
    

After creating the Patient resource, create an Encounter resource to describe an interaction between the patient and a practitioner.

In the PATIENT_ID field, substitute the ID from the response returned by the server when you created the Patient resource.

The following REST samples work with R4 FHIR stores. The Python sample works with STU3 FHIR stores.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID
  * PATIENT_ID: the response returned by the server when you created the Patient resource



Request JSON body: 
    
    
    {
      "status": "finished",
      "class": {
        "system": "http://hl7.org/fhir/v3/ActCode",
        "code": "IMP",
        "display": "inpatient encounter"
      },
      "reasonCode": [
        {
          "text": "The patient had an abnormal heart rate. She was concerned about this."
        }
      ],
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "resourceType": "Encounter"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "status": "finished",
      "class": {
        "system": "http://hl7.org/fhir/v3/ActCode",
        "code": "IMP",
        "display": "inpatient encounter"
      },
      "reasonCode": [
        {
          "text": "The patient had an abnormal heart rate. She was concerned about this."
        }
      ],
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "resourceType": "Encounter"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Encounter"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "status": "finished",
      "class": {
        "system": "http://hl7.org/fhir/v3/ActCode",
        "code": "IMP",
        "display": "inpatient encounter"
      },
      "reasonCode": [
        {
          "text": "The patient had an abnormal heart rate. She was concerned about this."
        }
      ],
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "resourceType": "Encounter"
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Encounter" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "class": {
        "code": "IMP",
        "display": "inpatient encounter",
        "system": "http://hl7.org/fhir/v3/ActCode"
      },
      "id": "ENCOUNTER_ID",
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "reasonCode": [
        {
          "text": "The patient had an abnormal heart rate. She was concerned about this."
        }
      ],
      "resourceType": "Encounter",
      "status": "finished",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the types Dict and Any for runtime type hints.
    from typing import Any, Dict  # noqa: E402
    
    def create_encounter(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
        patient_id: str,
    ) -> Dict[str, Any]:
        """Creates a new Encounter resource in a FHIR store that references a Patient resource.
    
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
          fhir_store_id: The name of the FHIR store.
          patient_id: The "logical id" of the referenced Patient resource. The ID is
            assigned by the server.
    
        Returns:
          A dict representing the created Encounter resource.
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
        # patient_id = 'b682d-0e-4843-a4a9-78c9ac64'  # replace with the associated Patient resource's ID
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        encounter_body = {
            "status": "finished",
            "class": {
                "system": "http://hl7.org/fhir/v3/ActCode",
                "code": "IMP",
                "display": "inpatient encounter",
            },
            "reason": [
                {
                    "text": (
                        "The patient had an abnormal heart rate. She was"
                        " concerned about this."
                    )
                }
            ],
            "subject": {"reference": f"Patient/{patient_id}"},
            "resourceType": "Encounter",
        }
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .create(parent=fhir_store_name, type="Encounter", body=encounter_body)
        )
        # Sets required application/fhir+json header on the googleapiclient.http.HttpRequest.
        request.headers["content-type"] = "application/fhir+json;charset=utf-8"
        response = request.execute()
        print(f"Created Encounter resource with ID {response['id']}")
    
        return response
    
    

After creating the Encounter resource, create an Observation resource associated with the Encounter resource. The Observation resource provides a measurement of the patient's heart rate in beats per minute (BPM) (`80` in `bpm`).

The following REST samples work with R4 FHIR stores. The Python sample works with STU3 FHIR stores.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID
  * PATIENT_ID: the ID in the response returned by the server when you created the Patient resource
  * ENCOUNTER_ID: the ID in the response returned by the server when you created the Encounter resource



Request JSON body: 
    
    
    {
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "code": {
        "coding": [
          {
            "system": "http://loinc.org",
            "code": "8867-4",
            "display": "Heart rate"
          }
        ]
      },
      "valueQuantity": {
        "value": 80,
        "unit": "bpm"
      },
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "code": {
        "coding": [
          {
            "system": "http://loinc.org",
            "code": "8867-4",
            "display": "Heart rate"
          }
        ]
      },
      "valueQuantity": {
        "value": 80,
        "unit": "bpm"
      },
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "code": {
        "coding": [
          {
            "system": "http://loinc.org",
            "code": "8867-4",
            "display": "Heart rate"
          }
        ]
      },
      "valueQuantity": {
        "value": 80,
        "unit": "bpm"
      },
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "code": {
        "coding": [
          {
            "code": "8867-4",
            "display": "Heart rate",
            "system": "http://loinc.org"
          }
        ]
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      },
      "id": "OBSERVATION_ID",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "valueQuantity": {
        "unit": "bpm",
        "value": 80
      }
    }
    

### Python

Before trying this sample, follow the Python setup instructions in the [Cloud Healthcare API quickstart using client libraries](https://cloud.google.com/healthcare-api/docs/store-healthcare-data-client-library). For more information, see the [Cloud Healthcare API Python API reference documentation](https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1). 

To authenticate to Cloud Healthcare API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the types Dict and Any for runtime type hints.
    from typing import Any, Dict  # noqa: E402
    
    def create_observation(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
        patient_id: str,
        encounter_id: str,
    ) -> Dict[str, Any]:
        """Creates a new Observation resource in a FHIR store that references an Encounter and Patient resource.
    
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
          fhir_store_id: The name of the FHIR store.
          patient_id: The "logical id" of the referenced Patient resource. The ID is
            assigned by the server.
          encounter_id: The "logical id" of the referenced Encounter resource. The ID
            is assigned by the server.
    
        Returns:
          A dict representing the created Observation resource.
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
        # patient_id = 'b682d-0e-4843-a4a9-78c9ac64'  # replace with the associated Patient resource's ID
        # encounter_id = 'a7602f-ffba-470a-a5c1-103f993c6  # replace with the associated Encounter resource's ID
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_observation_path = (
            f"{fhir_store_parent}/fhirStores/{fhir_store_id}/fhir/Observation"
        )
    
        observation_body = {
            "resourceType": "Observation",
            "code": {
                "coding": [
                    {
                        "system": "http://loinc.org",
                        "code": "8867-4",
                        "display": "Heart rate",
                    }
                ]
            },
            "status": "final",
            "subject": {"reference": f"Patient/{patient_id}"},
            "effectiveDateTime": "2019-01-01T00:00:00+00:00",
            "valueQuantity": {"value": 80, "unit": "bpm"},
            "context": {"reference": f"Encounter/{encounter_id}"},
        }
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .create(
                parent=fhir_observation_path,
                type="Observation",
                body=observation_body,
            )
        )
        # Sets required application/fhir+json header on the googleapiclient.http.HttpRequest.
        request.headers["content-type"] = "application/fhir+json;charset=utf-8"
        response = request.execute()
        print(f"Created Observation resource with ID {response['id']}")
    
        return response
    
    

### Conditionally create a FHIR resource

The following `curl` sample shows how to use the [`projects.locations.datasets.fhirStores.fhir.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/create) method to conditionally create a FHIR resource. The method implements the FHIR conditional `create` interaction ([DSTU2](https://hl7.org/fhir/dstu2/http.html#ccreate), [STU3](https://hl7.org/fhir/stu3/http.html#ccreate), [R4](https://hl7.org/fhir/R4/http.html#ccreate), [R5](https://hl7.org/fhir/R5/http.html#ccreate)).

You can use conditional create to avoid creating duplicate FHIR resources. For example, each Patient resource in a FHIR server typically has a unique identifier, such as a medical record number (MRN). To create a new Patient resource and ensure no Patient resource with the same MRN exists, conditionally create the new resource using a search query. The Cloud Healthcare API creates the new resource only if there are no matches for the search query.

The server's response depends on how many resources matched the search query:

Matches | HTTP response code | Behavior  
---|---|---  
Zero | `201 CREATED` | Creates the new resource.  
One | `200 OK` | Doesn't create a new resource.  
More than one | `412 Precondition Failed` | Doesn't create a new resource and returns a `"search criteria are not selective enough"` error.  
  
To use the conditional `create` interaction instead of the `create` interaction, specify an `If-None-Exist` HTTP header containing a [FHIR search query](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search#constructing_a_search_query) in your request:
    
    
    If-None-Exist: FHIR_SEARCH_QUERY

In the Cloud Healthcare API v1, conditional operations exclusively use the `identifier` search parameter, if it exists for the FHIR resource type, to determine which FHIR resources match a conditional search query. 

### REST

The following sample shows how to create an Observation resource using an `If-None-Exist: identifier=my-code-system|ABC-12345` HTTP header. The Cloud Healthcare API creates the resource if and only if no existing Observation resource matches the query `identifier=my-code-system|ABC-12345`.
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/fhir+json" \
      -H "If-None-Exist: identifier=my-code-system|ABC-12345" \
      -d @request.json \
      "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation"

The following sample output intentionally shows a **failed** request. To view the response from a successful request, see Creating a FHIR resource.

If multiple Observation resources match the query, the Cloud Healthcare API returns the following response, and the conditional create request fails:
    
    
    {
      "issue": [
        {
          "code": "conflict",
          "details": {
            "text": "ambiguous_query"
          },
          "diagnostics": "search criteria are not selective enough",
          "severity": "error"
        }
      ],
      "resourceType": "OperationOutcome"
    }
    

## Updating a FHIR resource

The following samples show how to use the [`projects.locations.datasets.fhirStores.fhir.update`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/update) method to update a FHIR resource. The method implements the FHIR standard update interaction ([DSTU2](https://hl7.org/fhir/dstu2/http.html#update), [STU3](https://hl7.org/fhir/STU3/http.html#update), [R4](https://hl7.org/fhir/r4/http.html#update), and [R5](https://hl7.org/fhir/r5/http.html#update)).

When you update a resource, you update the entire contents of the resource. This is in contrast to patching a resource, which updates only part of a resource.

If the FHIR store has [`enableUpdateCreate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.enable_update_create) set, the request is treated as an upsert (update or insert) that updates the resource if it exists or inserts it using the ID specified the request if it does not exist.

The request body must contain a JSON-encoded FHIR resource and the request headers must contain `Content-Type: application/fhir+json`. The resource must contain an `id` element having an identical value to the ID in the REST path of the request.

The following REST samples work with R4 FHIR stores. The Go, Java, Node.js, and Python samples work with STU3 FHIR stores.

### REST

The following samples show how to update the beats per minute (BPM) in an Observation resource.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID
  * OBSERVATION_ID: the Observation resource ID
  * PATIENT_ID: the Patient resource ID
  * ENCOUNTER_ID: the Encounter resource ID
  * BPM_VALUE: the beats per minute (BPM) value in the updated Observation resource



Request JSON body: 
    
    
    {
      "resourceType": "Observation",
      "id": "OBSERVATION_ID",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "code": {
        "coding": [
          {
            "system": "http://loinc.org",
            "code": "8867-4",
            "display": "Heart rate"
          }
        ]
      },
      "valueQuantity": {
        "value": BPM_VALUE,
        "unit": "bpm"
      },
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "resourceType": "Observation",
      "id": "OBSERVATION_ID",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "code": {
        "coding": [
          {
            "system": "http://loinc.org",
            "code": "8867-4",
            "display": "Heart rate"
          }
        ]
      },
      "valueQuantity": {
        "value": BPM_VALUE,
        "unit": "bpm"
      },
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/OBSERVATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "resourceType": "Observation",
      "id": "OBSERVATION_ID",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "code": {
        "coding": [
          {
            "system": "http://loinc.org",
            "code": "8867-4",
            "display": "Heart rate"
          }
        ]
      },
      "valueQuantity": {
        "value": BPM_VALUE,
        "unit": "bpm"
      },
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/OBSERVATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/update). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "code": {
        "coding": [
          {
            "code": "8867-4",
            "display": "Heart rate",
            "system": "http://loinc.org"
          }
        ]
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      },
      "id": "OBSERVATION_ID",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "valueQuantity": {
        "unit": "bpm",
        "value": BPM_VALUE
      }
    }
    

### Go
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // updateFHIRResource updates an FHIR resource to be active or not.
    func updateFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID string, active bool) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	// The following payload works with a Patient resource and is not
    	// intended to work with other types of FHIR resources. If necessary,
    	// supply a new payload with data that corresponds to the FHIR resource
    	// you are updating.
    	payload := map[string]interface{}{
    		"resourceType": resourceType,
    		"id":           fhirResourceID,
    		"active":       active,
    	}
    	jsonPayload, err := json.Marshal(payload)
    	if err != nil {
    		return fmt.Errorf("json.Encode: %w", err)
    	}
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s", projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID)
    
    	call := fhirService.Update(name, bytes.NewReader(jsonPayload))
    	call.Header().Set("Content-Type", "application/fhir+json;charset=utf-8")
    	resp, err := call.Do()
    	if err != nil {
    		return fmt.Errorf("Update: %w", err)
    	}
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("Update: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
    	}
    	fmt.Fprintf(w, "%s", respBytes)
    
    	return nil
    }
    

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
      headers: {'Content-Type': 'application/fhir+json'},
      responseType: 'json',
    });
    
    const updateFhirResource = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const resourceType = 'Patient';
      // const resourceId = '16e8a860-33b3-49be-9b03-de979feed14a';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/${resourceType}/${resourceId}`;
      // The following body works with a Patient resource and is not intended
      // to work with other types of FHIR resources. If necessary, supply a new
      // body with data that corresponds to the FHIR resource you are updating.
      const body = {resourceType: resourceType, id: resourceId, active: true};
      const request = {name, requestBody: body};
    
      try {
        const resource =
          await healthcare.projects.locations.datasets.fhirStores.fhir.update(
            request
          );
        console.log(`Updated ${resourceType} resource:\n`, resource.data);
      } catch (error) {
        console.error(
          `Error updating ${resourceType} resource:`,
          error.message || error
        );
      }
    };
    
    updateFhirResource();

### Python
    
    
    # Imports the types Dict and Any for runtime type hints.
    from typing import Any, Dict  # noqa: E402
    
    
    def update_resource(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
        resource_type: str,
        resource_id: str,
    ) -> Dict[str, Any]:
        """Updates the entire contents of a FHIR resource.
    
        Creates a new current version if the resource already exists, or creates
        a new resource with an initial version if no resource already exists with
        the provided ID.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample.
        See
        https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.fhirStores.fhir.html#update
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Cloud project you want
            to use.
          location: The name of the parent dataset's location.
          dataset_id: The name of the parent dataset.
          fhir_store_id: The name of the FHIR store.
          resource_type: The type of the FHIR resource.
          resource_id: The "logical id" of the resource. The ID is assigned by the
            server.
    
        Returns:
          A dict representing the updated FHIR resource.
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
        # resource_type = 'Patient'
        # resource_id = 'b682d-0e-4843-a4a9-78c9ac64'
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_resource_path = f"{fhir_store_parent}/fhirStores/{fhir_store_id}/fhir/{resource_type}/{resource_id}"
    
        # The following sample body works with a Patient resource and isn't guaranteed
        # to work with other types of FHIR resources. If necessary,
        # supply a new body with data that corresponds to the resource you
        # are updating.
        patient_body = {
            "resourceType": resource_type,
            "active": True,
            "id": resource_id,
        }
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .update(name=fhir_resource_path, body=patient_body)
        )
        # Sets required application/fhir+json header on the googleapiclient.http.HttpRequest.
        request.headers["content-type"] = "application/fhir+json;charset=utf-8"
        response = request.execute()
    
        print(
            f"Updated {resource_type} resource with ID {resource_id}:\n"
            f" {json.dumps(response, indent=2)}"
        )
    
        return response
    
    

### Conditionally updating a FHIR resource

The following samples show how to call the [`projects.locations.datasets.fhirStores.fhir.conditionalUpdate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/conditionalUpdate) method to update a FHIR resource that matches a search query, rather than identifying the resource by its ID. The method implements the FHIR standard conditional update interaction ([DSTU2](https://hl7.org/fhir/dstu2/http.html#cond-update), [STU3](https://hl7.org/fhir/STU3/http.html#cond-update), [R4](https://hl7.org/fhir/r4/http.html#cond-update), and [R5](https://hl7.org/fhir/r5/http.html#cond-update)).

A conditional update can only be applied to one FHIR resource at a time.

The response returned from the server depends on how many matches occur based on the search criteria:

  * **One match** : The resource is successfully updated or an error is returned.
  * **More than one match** : The request returns a `412 Precondition Failed` error.
  * **Zero matches with an`id`**: If the search criteria identify zero matches, the supplied request body contains an `id`, and the FHIR store has [`enableUpdateCreate`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.enable_update_create) set to `true`, the FHIR resource is created with the `id` in the request body.
  * **Zero matches without an`id`**: If the search criteria identify zero matches and the supplied request body doesn't contain an `id`, the FHIR resource is created with a server-assigned ID as if the resource was created using [`projects.locations.datasets.fhirStores.fhir.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/create).



The request body must contain a JSON-encoded FHIR resource and the request headers must contain `Content-Type: application/fhir+json`.

In the Cloud Healthcare API v1, conditional operations exclusively use the `identifier` search parameter, if it exists for the FHIR resource type, to determine which FHIR resources match a conditional search query. 

### REST

The following sample shows how to send a `PUT` request using `curl` and PowerShell to edit an Observation resource using the Observation's identifier (`ABC-12345` in `my-code-system`). The Observation provides a measurement of a patient's heartbeats per minute (BPM).

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID
  * PATIENT_ID: the Patient resource ID
  * ENCOUNTER_ID: the Encounter resource ID
  * BPM_VALUE: the beats per minute (BPM) value in the Observation resource



Request JSON body: 
    
    
    {
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "code": {
        "coding": [
          {
            "system": "http://loinc.org",
            "code": "8867-4",
            "display": "Heart rate"
          }
        ]
      },
      "valueQuantity": {
        "value": BPM_VALUE,
        "unit": "bpm"
      },
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "code": {
        "coding": [
          {
            "system": "http://loinc.org",
            "code": "8867-4",
            "display": "Heart rate"
          }
        ]
      },
      "valueQuantity": {
        "value": BPM_VALUE,
        "unit": "bpm"
      },
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PUT \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?identifier=my-code-system|ABC-12345"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "code": {
        "coding": [
          {
            "system": "http://loinc.org",
            "code": "8867-4",
            "display": "Heart rate"
          }
        ]
      },
      "valueQuantity": {
        "value": BPM_VALUE,
        "unit": "bpm"
      },
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      }
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PUT `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?identifier=my-code-system|ABC-12345" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/conditionalUpdate). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "code": {
        "coding": [
          {
            "code": "8867-4",
            "display": "Heart rate",
            "system": "http://loinc.org"
          }
        ]
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      },
      "id": "OBSERVATION_ID",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "valueQuantity": {
        "unit": "bpm",
        "value": BPM_VALUE
      }
    }
    

## Patching a FHIR resource

The following samples show how to call the [`projects.locations.datasets.fhirStores.fhir.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/patch) method to patch a FHIR resource. The method implements the FHIR standard patch interaction ([DSTU2](https://hl7.org/fhir/DSTU2/http.html#patch), [STU3](https://hl7.org/fhir/STU3/http.html#patch), [R4](https://hl7.org/fhir/R4/http.html#patch), and [R5](https://hl7.org/fhir/R5/http.html#patch)).

When you patch a resource, you update part of the resource by applying the operations specified in a [JSON Patch](http://jsonpatch.com/) document.

The request must contain a JSON patch document, and the request headers must contain `Content-Type: application/json-patch+json`.

The following samples show how to patch an Observation resource. The Observation of a patient's heartbeats per minute (BPM) is updated using the `replace` patch operation.

The following REST samples work with R4 FHIR stores. The Go, Java, Node.js, and Python samples work with STU3 FHIR stores.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID
  * OBSERVATION_ID: the Observation resource ID
  * BPM_VALUE: the beats per minute (BPM) value in the patched Observation resource



Request JSON body: 
    
    
    [
      {
        "op": "replace",
        "path": "/valueQuantity/value",
        "value": BPM_VALUE
      }
    ]
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    [
      {
        "op": "replace",
        "path": "/valueQuantity/value",
        "value": BPM_VALUE
      }
    ]
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json-patch+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/OBSERVATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    [
      {
        "op": "replace",
        "path": "/valueQuantity/value",
        "value": BPM_VALUE
      }
    ]
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json-patch+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/OBSERVATION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "code": {
        "coding": [
          {
            "code": "8867-4",
            "display": "Heart rate",
            "system": "http://loinc.org"
          }
        ]
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      },
      "id": "OBSERVATION_ID",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "valueQuantity": {
        "unit": "bpm",
        "value": BPM_VALUE
      }
    }
    

### Go
    
    
    import (
    	"bytes"
    	"context"
    	"encoding/json"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // patchFHIRResource patches an FHIR resource to be active or not.
    func patchFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID string, active bool) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	// The following payload works with a Patient resource and is not intended to work with
    	// other types of FHIR resources. If necessary, supply a new payload with data that
    	// corresponds to the FHIR resource you are patching.
    	payload := []map[string]interface{}{
    		{
    			"op":    "replace",
    			"path":  "/active",
    			"value": active,
    		},
    	}
    	jsonPayload, err := json.Marshal(payload)
    	if err != nil {
    		return fmt.Errorf("json.Encode: %w", err)
    	}
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s", projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID)
    
    	call := fhirService.Patch(name, bytes.NewReader(jsonPayload))
    	call.Header().Set("Content-Type", "application/json-patch+json")
    	resp, err := call.Do()
    	if err != nil {
    		return fmt.Errorf("Patch: %w", err)
    	}
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("Patch: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
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
    
    public class FhirResourcePatch {
      private static final String FHIR_NAME =
          "projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirResourcePatch(String resourceName, String data)
          throws IOException, URISyntaxException {
        // String resourceName =
        //    String.format(
        //        FHIR_NAME, "project-id", "region-id", "dataset-id", "store-id", "resource-type",
        // "resource-id");
        // The following data works with a Patient resource and is not intended to work with
        // other types of FHIR resources. If necessary, supply new values for data that
        // correspond to the FHIR resource you are patching.
        // String data = "[{\"op\": \"replace\", \"path\": \"/active\", \"value\": false}]";
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%sv1/%s", client.getRootUrl(), resourceName);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
        StringEntity requestEntity = new StringEntity(data);
    
        HttpUriRequest request =
            RequestBuilder.patch(uriBuilder.build())
                .setEntity(requestEntity)
                .addHeader("Content-Type", "application/json-patch+json")
                .addHeader("Accept-Charset", "utf-8")
                .addHeader("Accept", "application/fhir+json; charset=utf-8")
                .build();
    
        // Execute the request and process the results.
        HttpResponse response = httpClient.execute(request);
        HttpEntity responseEntity = response.getEntity();
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
          System.err.print(
              String.format(
                  "Exception patching FHIR resource: %s\n", response.getStatusLine().toString()));
          responseEntity.writeTo(System.err);
          throw new RuntimeException();
        }
        System.out.println("FHIR resource patched: ");
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
      headers: {'Content-Type': 'application/json-patch+json'},
    });
    
    async function patchFhirResource() {
      // TODO(developer): replace patchOptions with your desired JSON patch body
      const patchOptions = [{op: 'replace', path: '/active', value: false}];
    
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const resourceType = 'Patient';
      // const resourceId = '16e8a860-33b3-49be-9b03-de979feed14a';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/${resourceType}/${resourceId}`;
      const request = {
        name,
        requestBody: patchOptions,
      };
    
      await healthcare.projects.locations.datasets.fhirStores.fhir.patch(request);
      console.log(`Patched ${resourceType} resource`);
    }
    
    patchFhirResource();

### Python
    
    
    # Imports the types Dict and Any for runtime type hints.
    from typing import Any, Dict  # noqa: E402
    
    
    def patch_resource(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
        resource_type: str,
        resource_id: str,
    ) -> Dict[str, Any]:
        """Updates part of an existing FHIR resource by applying the operations specified in a [JSON Patch](http://jsonpatch.com/) document.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample.
        See
        https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.fhirStores.fhir.html#patch
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Cloud project you want
            to use.
          location: The name of the parent dataset's location.
          dataset_id: The name of the parent dataset.
          fhir_store_id: The name of the FHIR store.
          resource_type: The type of the FHIR resource.
          resource_id: The "logical id" of the resource. The ID is assigned by the
            server.
    
        Returns:
          A dict representing the patched FHIR resource.
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
        # resource_type = 'Patient'
        # resource_id = 'b682d-0e-4843-a4a9-78c9ac64'
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_resource_path = f"{fhir_store_parent}/fhirStores/{fhir_store_id}/fhir/{resource_type}/{resource_id}"
    
        # The following sample body works with a Patient resource and isn't guaranteed
        # to work with other types of FHIR resources. If necessary,
        # supply a new body with data that corresponds to the resource you
        # are updating.
        patient_body = [{"op": "replace", "path": "/active", "value": False}]
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .patch(name=fhir_resource_path, body=patient_body)
        )
    
        # Sets required application/json-patch+json header.
        # See https://tools.ietf.org/html/rfc6902 for more information.
        request.headers["content-type"] = "application/json-patch+json"
    
        response = request.execute()
    
        print(
            f"Patched {resource_type} resource with ID {resource_id}:\n"
            f" {json.dumps(response, indent=2)}"
        )
    
        return response
    
    

### Executing a `PATCH` request in a FHIR bundle

**Preview**  
  
This section describes Preview features that are subject to change and may have limited support. Changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see [Pre-GA Offering Terms for Cloud Healthcare API](https://cloud.google.com/healthcare-api/docs/pre-ga-terms#pre-ga_offering_terms_for) and the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages).

You can a specify a `PATCH` request in a FHIR bundle (FHIR R4 only). Executing `PATCH` request in a FHIR bundle lets you patch many FHIR resources at once, rather than having to make individual patch requests for each FHIR resource.

To make a `PATCH` request in a bundle, specify the following information in a `resource` object in the request:

  * A `resourceType` field set to `Binary`
  * A `contentType` field set to `application/json-patch+json`
  * The patch body encoded in base64



Ensure that the `resource` object looks like the following:
    
    
    "resource": {
      "resourceType": "Binary",
      "contentType": "application/json-patch+json",
      "data": "WyB7ICJvcCI6ICJyZXBsYWNlIiwgInBhdGgiOiAiL2JpcnRoRGF0ZSIsICJ2YWx1ZSI6ICIxOTkwLTAxLTAxIiB9IF0K"
    }
    

The following shows the patch body that was encoded to base64 in the `data` field:
    
    
    [
      {
        "op": "replace",
        "path": "/birthdate",
        "value": "1990-01-01"
      }
    ]
    

The following samples show how to use a `PATCH` request in a bundle to patch the Patient resource you created in Creating a FHIR resource to have a `birthDate` value of `1990-01-01`:

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: your Google Cloud project ID
  * LOCATION: the location of the parent dataset
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID
  * PATIENT_ID: the ID of an existing Patient resource



Request JSON body: 
    
    
    {
      "type": "transaction",
      "resourceType": "Bundle",
      "entry": [
        {
          "request": {
            "method": "PATCH",
            "url": "Patient/PATIENT_ID"
          },
          "resource": {
            "resourceType": "Binary",
            "contentType": "application/json-patch+json",
            "data": "WyB7ICJvcCI6ICJyZXBsYWNlIiwgInBhdGgiOiAiL2JpcnRoRGF0ZSIsICJ2YWx1ZSI6ICIxOTkwLTAxLTAxIiB9IF0K"
          }
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "type": "transaction",
      "resourceType": "Bundle",
      "entry": [
        {
          "request": {
            "method": "PATCH",
            "url": "Patient/PATIENT_ID"
          },
          "resource": {
            "resourceType": "Binary",
            "contentType": "application/json-patch+json",
            "data": "WyB7ICJvcCI6ICJyZXBsYWNlIiwgInBhdGgiOiAiL2JpcnRoRGF0ZSIsICJ2YWx1ZSI6ICIxOTkwLTAxLTAxIiB9IF0K"
          }
        }
      ]
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/fhir+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "type": "transaction",
      "resourceType": "Bundle",
      "entry": [
        {
          "request": {
            "method": "PATCH",
            "url": "Patient/PATIENT_ID"
          },
          "resource": {
            "resourceType": "Binary",
            "contentType": "application/json-patch+json",
            "data": "WyB7ICJvcCI6ICJyZXBsYWNlIiwgInBhdGgiOiAiL2JpcnRoRGF0ZSIsICJ2YWx1ZSI6ICIxOTkwLTAxLTAxIiB9IF0K"
          }
        }
      ]
    }
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/fhir+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir" | Select-Object -Expand Content

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "entry": [
        {
          "response": {
            "etag": "W/\"MTY0ODgzNjY5MjQyODAxMzAwMA\"",
            "lastModified": "LAST_MODIFIED",
            "location": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID",
            "status": "200 OK"
          }
        }
      ],
      "resourceType": "Bundle",
      "type": "transaction-response"
    }
    

### Conditionally patching a FHIR resource

The following samples show how to call the [`projects.locations.datasets.fhirStores.fhir.conditionalPatch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/conditionalPatch) method to patch a FHIR resource that matches a search query, rather than identifying the resource by its ID. The method implements the FHIR standard conditional patch interaction ([DSTU2](https://hl7.org/fhir/DSTU2/http.html#patch), [STU3](https://hl7.org/fhir/STU3/http.html#patch), [R4](https://hl7.org/fhir/R4/http.html#patch), and [R4](https://hl7.org/fhir/R5/http.html#patch)).

A conditional patch can be applied to only one resource at a time. If the search criteria identify more than one match, the request returns a `412 Precondition Failed` error. If the search criteria doesn't identify any matches, the request returns a `404 Not Found` error.

In the Cloud Healthcare API v1, conditional operations exclusively use the `identifier` search parameter, if it exists for the FHIR resource type, to determine which FHIR resources match a conditional search query. 

### REST

The following samples show how to send a `PATCH` request to edit an Observation resource if the Observation's identifier is `ABC-12345` in `my-code-system`. The Observation of a patient's heartbeats per minute (BPM) is updated using the `replace` patch operation. 

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID
  * BPM_VALUE: the beats per minute (BPM) value in the Observation resource



Request JSON body: 
    
    
    [
      {
        "op": "replace",
        "path": "/valueQuantity/value",
        "value": BPM_VALUE
      }
    ]
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    [
      {
        "op": "replace",
        "path": "/valueQuantity/value",
        "value": BPM_VALUE
      }
    ]
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json-patch+json" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?identifier=my-code-system|ABC-12345"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    [
      {
        "op": "replace",
        "path": "/valueQuantity/value",
        "value": BPM_VALUE
      }
    ]
    '@  | Out-File -FilePath request.json -Encoding utf8

Then execute the following command to send your REST request: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json-patch+json" `  
        -InFile request.json `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?identifier=my-code-system|ABC-12345" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/conditionalPatch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "code": {
        "coding": [
          {
            "code": "8867-4",
            "display": "Heart rate",
            "system": "http://loinc.org"
          }
        ]
      },
      "effectiveDateTime": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      },
      "id": "OBSERVATION_ID",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "valueQuantity": {
        "unit": "bpm",
        "value": BPM_VALUE
      }
    }
    

## Getting a FHIR resource

The following samples show how to get the contents of a FHIR resource.

The following REST samples work with R4 FHIR stores. The Go, Java, Node.js, and Python samples work with STU3 FHIR stores.

### Console

  1. In the Google Cloud console, go to the **FHIR viewer** page.

[Go to the FHIR viewer](https://console.cloud.google.com/healthcare/fhirviewer)

  2. In the **FHIR Store** drop-down list, select a dataset, and then select a FHIR store in the dataset.

  3. To filter the list of resource types, search for the resource types that you want to display.

  4. Click the **Resource Type** field.

  5. In the **Properties** drop-down list that appears, select **Resource Type**.

  6. Enter a resource type.

  7. To search for another resource type, select **OR** from the **Operators** drop-down list that appears, and then enter another resource type.

  8. In the list of resource types, select the resource type for the resource that you want to get the contents of.

  9. In the table of resources that appears, select or [search for](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search#using_the_fhir_viewer) a resource.




### REST

The following samples show how to use the [`projects.locations.datasets.fhirStores.fhir.read`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/read) method to get the details of the Observation resource created in a previous section.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID
  * OBSERVATION_ID: the Observation resource ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/OBSERVATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/OBSERVATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/read). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "code": {
        "coding": [
          {
            "code": "8867-4",
            "display": "Heart rate",
            "system": "http://loinc.org"
          }
        ]
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      },
      "id": "OBSERVATION_ID",
      "identifier": [
        {
          "system": "my-code-system",
          "value": "ABC-12345"
        }
      ],
      "meta": {
        "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
        "versionId": "VERSION_ID"
      },
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "valueQuantity": {
        "unit": "bpm",
        "value": 80
      }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // getFHIRResource gets an FHIR resource.
    func getFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s", projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID)
    
    	call := fhirService.Read(name)
    	call.Header().Set("Content-Type", "application/fhir+json;charset=utf-8")
    	resp, err := call.Do()
    	if err != nil {
    		return fmt.Errorf("Read: %w", err)
    	}
    
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("Read: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
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
    import org.apache.http.impl.client.HttpClients;
    
    public class FhirResourceGet {
      private static final String FHIR_NAME =
          "projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirResourceGet(String resourceName) throws IOException, URISyntaxException {
        // String resourceName =
        //    String.format(
        //        FHIR_NAME, "project-id", "region-id", "dataset-id", "store-id", "resource-type",
        //  "resource-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%sv1/%s", client.getRootUrl(), resourceName);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
    
        HttpUriRequest request = RequestBuilder.get().setUri(uriBuilder.build()).build();
    
        // Execute the request and process the results.
        HttpResponse response = httpClient.execute(request);
        HttpEntity responseEntity = response.getEntity();
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
          String errorMessage =
              String.format(
                  "Exception retrieving FHIR resource: %s\n", response.getStatusLine().toString());
          System.err.print(errorMessage);
          responseEntity.writeTo(System.err);
          throw new RuntimeException(errorMessage);
        }
        System.out.println("FHIR resource retrieved: ");
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
      responseType: 'json',
    });
    
    const getFhirResource = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const resourceType = 'Patient';
      // const resourceId = '16e8a860-33b3-49be-9b03-de979feed14a';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/${resourceType}/${resourceId}`;
      const request = {name};
    
      try {
        const resource =
          await healthcare.projects.locations.datasets.fhirStores.fhir.read(
            request
          );
        console.log(`Got ${resourceType} resource:\n`, resource.data);
      } catch (error) {
        console.error(
          `Error getting ${resourceType} resource:`,
          error.message || error
        );
      }
    };
    
    getFhirResource();

### Python
    
    
    # Imports the types Dict and Any for runtime type hints.
    from typing import Any, Dict  # noqa: E402
    
    
    def get_resource(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
        resource_type: str,
        resource_id: str,
    ) -> Dict[str, Any]:
        """Gets the contents of a FHIR resource.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample.
        See
        https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.fhirStores.fhir.html#read
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Cloud project you want
            to use.
          location: The name of the parent dataset's location.
          dataset_id: The name of the parent dataset.
          fhir_store_id: The name of the FHIR store.
          resource_type: The type of FHIR resource.
          resource_id: The "logical id" of the resource you want to get the contents
            of. The ID is assigned by the server.
    
        Returns:
          A dict representing the FHIR resource.
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
        # resource_type = 'Patient'
        # resource_id = 'b682d-0e-4843-a4a9-78c9ac64'
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_resource_path = f"{fhir_store_parent}/fhirStores/{fhir_store_id}/fhir/{resource_type}/{resource_id}"
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .read(name=fhir_resource_path)
        )
        response = request.execute()
        print(
            f"Got contents of {resource_type} resource with ID {resource_id}:\n",
            json.dumps(response, indent=2),
        )
    
        return response
    
    

## Get all Encounter resource details

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The following samples show how to to view details about an Encounter resource and all resources related to the Encounter.

The method implements the FHIR extended operation `Encounter-everything` defined in the following FHIR versions:

  * [DSTU2](https://hl7.org/fhir/DSTU2/encounter-operations.html#everything)
  * [STU3](https://hl7.org/fhir/stu3/encounter-operations.html#everything)
  * [R4](https://www.hl7.org/fhir/R4/encounter-operation-everything.html)
  * [R5](https://www.hl7.org/fhir/R5/encounter-operation-everything.html)



### REST

Use the [`projects.locations.datasets.fhirStores.fhir.Encounter-everything`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores.fhir/Encounter-everything) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the dataset ID
  * `FHIR_STORE_ID`: the FHIR store ID
  * `ENCOUNTER_ID`: the Encounter resource ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Encounter/ENCOUNTER_ID/\$everything"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Encounter/ENCOUNTER_ID/\$everything" | Select-Object -Expand Content

The following sample response is returned when calling the method on an Encounter resource with the ID `c427ce3e-7677-400e-bc06-33a8cecfdd77`, which is a synthetic resource in the [`gs://gcp-public-data--synthea-fhir-data-10-patients/fhir_r4_ndjson/`](https://console.cloud.google.com/storage/browser/gcp-public-data--synthea-fhir-data-10-patients/fhir_r4_ndjson) public Cloud Storage bucket. 

#### Response
    
    
    {
      "resourceType": "Bundle",
      "type": "searchset",
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Encounter/c427ce3e-7677-400e-bc06-33a8cecfdd77",
          "resource": {
            "class": {
              "code": "AMB",
              "system": "http://terminology.hl7.org/CodeSystem/v3-ActCode"
            },
            "extension": [
              {
                "extension": [
                  {
                    "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-action-Status-extension",
                    "valueCode": "finished"
                  }
                ],
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-action-PerformedContext-extension"
              }
            ],
            "id": "c427ce3e-7677-400e-bc06-33a8cecfdd77",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-encounter-EncounterPerformed"
              ],
              "versionId": "MTcxOTUyMzQ1MzA0MjMwMDAwMA"
            },
            "participant": [
              {
                "individual": {
                  "reference": "Practitioner/d22d7490-0710-4190-bd23-43bc6bca2649"
                }
              }
            ],
            "period": {
              "end": "2015-03-02T17:06:14-08:00",
              "start": "2015-03-02T16:51:14-08:00"
            },
            "resourceType": "Encounter",
            "serviceProvider": {
              "reference": "Organization/69176529-fd1f-3b3f-abce-a0a3626769eb"
            },
            "status": "finished",
            "subject": {
              "reference": "Patient/b0027145-32af-4030-bcb1-1f5b63d3f2e2"
            },
            "type": [
              {
                "coding": [
                  {
                    "code": "185349003",
                    "display": "Encounter for check up (procedure)",
                    "system": "http://snomed.info/sct"
                  }
                ],
                "text": "Encounter for check up (procedure)"
              }
            ]
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Organization/69176529-fd1f-3b3f-abce-a0a3626769eb",
          "resource": {
            "active": true,
            "address": [
              {
                "city": "CAMBRIDGE",
                "country": "US",
                "line": [
                  "330 MOUNT AUBURN STREET"
                ],
                "postalCode": "02138",
                "state": "MA"
              }
            ],
            "contact": [
              {
                "name": {
                  "text": "Synthetic Provider"
                }
              }
            ],
            "id": "69176529-fd1f-3b3f-abce-a0a3626769eb",
            "identifier": [
              {
                "system": "urn:ietf:rfc:3986",
                "value": "69176529-fd1f-3b3f-abce-a0a3626769eb"
              },
              {
                "system": "https://github.com/synthetichealth/synthea",
                "value": "69176529-fd1f-3b3f-abce-a0a3626769eb"
              }
            ],
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-entity-Organization"
              ],
              "versionId": "MTcxOTUyMzQ2Mjg2MzQ3NDAwMA"
            },
            "name": "MOUNT AUBURN HOSPITAL",
            "resourceType": "Organization",
            "telecom": [
              {
                "system": "phone",
                "value": "6174923500"
              }
            ],
            "type": [
              {
                "coding": [
                  {
                    "code": "prov",
                    "display": "Healthcare Provider",
                    "system": "http://terminology.hl7.org/CodeSystem/organization-type"
                  }
                ],
                "text": "Healthcare Provider"
              }
            ]
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/b0027145-32af-4030-bcb1-1f5b63d3f2e2",
          "resource": {
            "address": [
              {
                "city": "Somerville",
                "country": "US",
                "extension": [
                  {
                    "extension": [
                      {
                        "url": "latitude",
                        "valueDecimal": 42.390566
                      },
                      {
                        "url": "longitude",
                        "valueDecimal": -71.101324
                      }
                    ],
                    "url": "http://hl7.org/fhir/StructureDefinition/geolocation"
                  }
                ],
                "line": [
                  "883 Howell Lane"
                ],
                "postalCode": "02138",
                "state": "Massachusetts"
              }
            ],
            "birthDate": "2008-03-10",
            "communication": [
              {
                "language": {
                  "coding": [
                    {
                      "code": "es",
                      "display": "Spanish",
                      "system": "urn:ietf:bcp:47"
                    }
                  ],
                  "text": "Spanish"
                }
              }
            ],
            "extension": [
              {
                "extension": [
                  {
                    "url": "ombCategory",
                    "valueCoding": {
                      "code": "2054-5",
                      "display": "Black or African American",
                      "system": "urn:oid:2.16.840.1.113883.6.238"
                    }
                  },
                  {
                    "url": "text",
                    "valueString": "Black or African American"
                  }
                ],
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-race"
              },
              {
                "extension": [
                  {
                    "url": "ombCategory",
                    "valueCoding": {
                      "code": "2186-5",
                      "display": "Not Hispanic or Latino",
                      "system": "urn:oid:2.16.840.1.113883.6.238"
                    }
                  },
                  {
                    "url": "text",
                    "valueString": "Not Hispanic or Latino"
                  }
                ],
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-ethnicity"
              },
              {
                "url": "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName",
                "valueString": "Ariadna374 Lovato727"
              },
              {
                "url": "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
                "valueCode": "F"
              },
              {
                "url": "http://hl7.org/fhir/StructureDefinition/patient-birthPlace",
                "valueAddress": {
                  "city": "Portsmouth",
                  "country": "DM",
                  "state": "Saint John Parish"
                }
              },
              {
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-actor-FictionalPerson-extension",
                "valueBoolean": true
              },
              {
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-entity-FathersName-extension",
                "valueHumanName": {
                  "text": "Joaquín233 Montemayor547"
                }
              },
              {
                "url": "http://standardhealthrecord.org/fhir/StructureDefinition/shr-demographics-SocialSecurityNumber-extension",
                "valueString": "999-10-3430"
              },
              {
                "url": "http://synthetichealth.github.io/synthea/disability-adjusted-life-years",
                "valueDecimal": 0
              },
              {
                "url": "http://synthetichealth.github.io/synthea/quality-adjusted-life-years",
                "valueDecimal": 10
              }
            ],
            "gender": "female",
            "id": "b0027145-32af-4030-bcb1-1f5b63d3f2e2",
            "identifier": [
              {
                "system": "https://github.com/synthetichealth/synthea",
                "value": "c04dc343-a9f2-445c-ab4b-42b403a9cdba"
              },
              {
                "system": "http://hospital.smarthealthit.org",
                "type": {
                  "coding": [
                    {
                      "code": "MR",
                      "display": "Medical Record Number",
                      "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                    }
                  ],
                  "text": "Medical Record Number"
                },
                "value": "c04dc343-a9f2-445c-ab4b-42b403a9cdba"
              },
              {
                "system": "http://hl7.org/fhir/sid/us-ssn",
                "type": {
                  "coding": [
                    {
                      "code": "SS",
                      "display": "Social Security Number",
                      "system": "http://terminology.hl7.org/CodeSystem/v2-0203"
                    }
                  ],
                  "text": "Social Security Number"
                },
                "value": "999-10-3430"
              }
            ],
            "maritalStatus": {
              "coding": [
                {
                  "code": "S",
                  "display": "Never Married",
                  "system": "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"
                }
              ],
              "text": "Never Married"
            },
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-entity-Patient"
              ],
              "versionId": "MTcxOTUyMzQ2MzIwNzY1MDAwMA"
            },
            "multipleBirthBoolean": false,
            "name": [
              {
                "family": "Montemayor547",
                "given": [
                  "Sonia106"
                ],
                "use": "official"
              }
            ],
            "resourceType": "Patient",
            "telecom": [
              {
                "system": "phone",
                "use": "home",
                "value": "555-302-8948"
              }
            ],
            "text": {
              "div": "div xmlns=http://www.w3.org/1999/xhtml Generated by https://github.com/synthetichealth/synthea Synthea. Version identifier: 6a640b4\n .   Person seed: -8343380064104224231  Population seed: 1562179070288",
              "status": "generated"
            }
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Practitioner/d22d7490-0710-4190-bd23-43bc6bca2649",
          "resource": {
            "active": true,
            "address": [
              {
                "city": "CAMBRIDGE",
                "country": "US",
                "line": [
                  "330 MOUNT AUBURN STREET"
                ],
                "postalCode": "02138",
                "state": "MA"
              }
            ],
            "gender": "female",
            "id": "d22d7490-0710-4190-bd23-43bc6bca2649",
            "identifier": [
              {
                "system": "http://hl7.org/fhir/sid/us-npi",
                "value": "10"
              }
            ],
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "versionId": "MTcxOTUyMzQ2MzQ0NDY3NTAwMA"
            },
            "name": [
              {
                "family": "Gleason633",
                "given": [
                  "Mariam937"
                ],
                "prefix": [
                  "Dr."
                ]
              }
            ],
            "resourceType": "Practitioner"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Claim/d7628517-253d-47fa-951b-4057b71ca1fa",
          "resource": {
            "billablePeriod": {
              "end": "2015-03-02T17:06:14-08:00",
              "start": "2015-03-02T16:51:14-08:00"
            },
            "created": "2015-03-02T17:06:14-08:00",
            "id": "d7628517-253d-47fa-951b-4057b71ca1fa",
            "insurance": [
              {
                "coverage": {
                  "display": "private"
                },
                "focal": true,
                "sequence": 1
              }
            ],
            "item": [
              {
                "encounter": [
                  {
                    "reference": "Encounter/c427ce3e-7677-400e-bc06-33a8cecfdd77"
                  }
                ],
                "productOrService": {
                  "coding": [
                    {
                      "code": "185349003",
                      "display": "Encounter for check up (procedure)",
                      "system": "http://snomed.info/sct"
                    }
                  ],
                  "text": "Encounter for check up (procedure)"
                },
                "sequence": 1
              },
              {
                "informationSequence": [
                  1
                ],
                "net": {
                  "currency": "USD",
                  "value": 140.52
                },
                "productOrService": {
                  "coding": [
                    {
                      "code": "140",
                      "display": "Influenza, seasonal, injectable, preservative free",
                      "system": "http://hl7.org/fhir/sid/cvx"
                    }
                  ],
                  "text": "Influenza, seasonal, injectable, preservative free"
                },
                "sequence": 2
              }
            ],
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "versionId": "MTcxOTUyMzQ1MDIxMzU0MjAwMA"
            },
            "patient": {
              "reference": "Patient/b0027145-32af-4030-bcb1-1f5b63d3f2e2"
            },
            "priority": {
              "coding": [
                {
                  "code": "normal",
                  "system": "http://terminology.hl7.org/CodeSystem/processpriority"
                }
              ]
            },
            "provider": {
              "reference": "Organization/69176529-fd1f-3b3f-abce-a0a3626769eb"
            },
            "resourceType": "Claim",
            "status": "active",
            "supportingInfo": [
              {
                "category": {
                  "coding": [
                    {
                      "code": "info",
                      "system": "http://terminology.hl7.org/CodeSystem/claiminformationcategory"
                    }
                  ]
                },
                "sequence": 1,
                "valueReference": {
                  "reference": "Immunization/e0da797f-a3ef-4b90-9f41-3e650881e0ab"
                }
              }
            ],
            "total": {
              "currency": "USD",
              "value": 265.52
            },
            "type": {
              "coding": [
                {
                  "code": "institutional",
                  "system": "http://terminology.hl7.org/CodeSystem/claim-type"
                }
              ]
            },
            "use": "claim"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/ExplanationOfBenefit/7c6f9e0c-9773-4cc4-ab9f-cf0670c49081",
          "resource": {
            "billablePeriod": {
              "end": "2016-03-02T17:06:14-08:00",
              "start": "2015-03-02T17:06:14-08:00"
            },
            "careTeam": [
              {
                "provider": {
                  "reference": "Practitioner/d22d7490-0710-4190-bd23-43bc6bca2649"
                },
                "role": {
                  "coding": [
                    {
                      "code": "primary",
                      "display": "Primary Care Practitioner",
                      "system": "http://terminology.hl7.org/CodeSystem/claimcareteamrole"
                    }
                  ]
                },
                "sequence": 1
              }
            ],
            "claim": {
              "reference": "Claim/d7628517-253d-47fa-951b-4057b71ca1fa"
            },
            "contained": [
              {
                "id": "referral",
                "intent": "order",
                "performer": [
                  {
                    "reference": "Practitioner/d22d7490-0710-4190-bd23-43bc6bca2649"
                  }
                ],
                "requester": {
                  "reference": "Practitioner/d22d7490-0710-4190-bd23-43bc6bca2649"
                },
                "resourceType": "ServiceRequest",
                "status": "completed",
                "subject": {
                  "reference": "Patient/b0027145-32af-4030-bcb1-1f5b63d3f2e2"
                }
              },
              {
                "beneficiary": {
                  "reference": "Patient/b0027145-32af-4030-bcb1-1f5b63d3f2e2"
                },
                "id": "coverage",
                "payor": [
                  {
                    "display": "private"
                  }
                ],
                "resourceType": "Coverage",
                "status": "active",
                "type": {
                  "text": "private"
                }
              }
            ],
            "created": "2015-03-02T17:06:14-08:00",
            "id": "7c6f9e0c-9773-4cc4-ab9f-cf0670c49081",
            "identifier": [
              {
                "system": "https://bluebutton.cms.gov/resources/variables/clm_id",
                "value": "d7628517-253d-47fa-951b-4057b71ca1fa"
              },
              {
                "system": "https://bluebutton.cms.gov/resources/identifier/claim-group",
                "value": "99999999999"
              }
            ],
            "insurance": [
              {
                "coverage": {
                  "display": "private",
                  "reference": "#coverage"
                },
                "focal": true
              }
            ],
            "insurer": {
              "display": "private"
            },
            "item": [
              {
                "category": {
                  "coding": [
                    {
                      "code": "1",
                      "display": "Medical care",
                      "system": "https://bluebutton.cms.gov/resources/variables/line_cms_type_srvc_cd"
                    }
                  ]
                },
                "encounter": [
                  {
                    "reference": "Encounter/c427ce3e-7677-400e-bc06-33a8cecfdd77"
                  }
                ],
                "locationCodeableConcept": {
                  "coding": [
                    {
                      "code": "19",
                      "display": "Off Campus-Outpatient Hospital",
                      "system": "http://terminology.hl7.org/CodeSystem/ex-serviceplace"
                    }
                  ]
                },
                "productOrService": {
                  "coding": [
                    {
                      "code": "185349003",
                      "display": "Encounter for check up (procedure)",
                      "system": "http://snomed.info/sct"
                    }
                  ],
                  "text": "Encounter for check up (procedure)"
                },
                "sequence": 1,
                "servicedPeriod": {
                  "end": "2015-03-02T17:06:14-08:00",
                  "start": "2015-03-02T16:51:14-08:00"
                }
              },
              {
                "adjudication": [
                  {
                    "amount": {
                      "currency": "USD",
                      "value": 28.104000000000003
                    },
                    "category": {
                      "coding": [
                        {
                          "code": "https://bluebutton.cms.gov/resources/variables/line_coinsrnc_amt",
                          "display": "Line Beneficiary Coinsurance Amount",
                          "system": "https://bluebutton.cms.gov/resources/codesystem/adjudication"
                        }
                      ]
                    }
                  },
                  {
                    "amount": {
                      "currency": "USD",
                      "value": 112.41600000000001
                    },
                    "category": {
                      "coding": [
                        {
                          "code": "https://bluebutton.cms.gov/resources/variables/line_prvdr_pmt_amt",
                          "display": "Line Provider Payment Amount",
                          "system": "https://bluebutton.cms.gov/resources/codesystem/adjudication"
                        }
                      ]
                    }
                  },
                  {
                    "amount": {
                      "currency": "USD",
                      "value": 140.52
                    },
                    "category": {
                      "coding": [
                        {
                          "code": "https://bluebutton.cms.gov/resources/variables/line_sbmtd_chrg_amt",
                          "display": "Line Submitted Charge Amount",
                          "system": "https://bluebutton.cms.gov/resources/codesystem/adjudication"
                        }
                      ]
                    }
                  },
                  {
                    "amount": {
                      "currency": "USD",
                      "value": 140.52
                    },
                    "category": {
                      "coding": [
                        {
                          "code": "https://bluebutton.cms.gov/resources/variables/line_alowd_chrg_amt",
                          "display": "Line Allowed Charge Amount",
                          "system": "https://bluebutton.cms.gov/resources/codesystem/adjudication"
                        }
                      ]
                    }
                  },
                  {
                    "amount": {
                      "currency": "USD",
                      "value": 0
                    },
                    "category": {
                      "coding": [
                        {
                          "code": "https://bluebutton.cms.gov/resources/variables/line_bene_ptb_ddctbl_amt",
                          "display": "Line Beneficiary Part B Deductible Amount",
                          "system": "https://bluebutton.cms.gov/resources/codesystem/adjudication"
                        }
                      ]
                    }
                  },
                  {
                    "category": {
                      "coding": [
                        {
                          "code": "https://bluebutton.cms.gov/resources/variables/line_prcsg_ind_cd",
                          "display": "Line Processing Indicator Code",
                          "system": "https://bluebutton.cms.gov/resources/codesystem/adjudication"
                        }
                      ]
                    }
                  }
                ],
                "category": {
                  "coding": [
                    {
                      "code": "1",
                      "display": "Medical care",
                      "system": "https://bluebutton.cms.gov/resources/variables/line_cms_type_srvc_cd"
                    }
                  ]
                },
                "informationSequence": [
                  1
                ],
                "locationCodeableConcept": {
                  "coding": [
                    {
                      "code": "19",
                      "display": "Off Campus-Outpatient Hospital",
                      "system": "http://terminology.hl7.org/CodeSystem/ex-serviceplace"
                    }
                  ]
                },
                "net": {
                  "currency": "USD",
                  "value": 140.52
                },
                "productOrService": {
                  "coding": [
                    {
                      "code": "140",
                      "display": "Influenza, seasonal, injectable, preservative free",
                      "system": "http://hl7.org/fhir/sid/cvx"
                    }
                  ],
                  "text": "Influenza, seasonal, injectable, preservative free"
                },
                "sequence": 2,
                "servicedPeriod": {
                  "end": "2015-03-02T17:06:14-08:00",
                  "start": "2015-03-02T16:51:14-08:00"
                }
              }
            ],
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "versionId": "MTcxOTUyMzQ1NTU2NDY5MjAwMA"
            },
            "outcome": "complete",
            "patient": {
              "reference": "Patient/b0027145-32af-4030-bcb1-1f5b63d3f2e2"
            },
            "payment": {
              "amount": {
                "currency": "USD",
                "value": 112.41600000000001
              }
            },
            "provider": {
              "reference": "Practitioner/d22d7490-0710-4190-bd23-43bc6bca2649"
            },
            "referral": {
              "reference": "#referral"
            },
            "resourceType": "ExplanationOfBenefit",
            "status": "active",
            "total": [
              {
                "amount": {
                  "currency": "USD",
                  "value": 265.52
                },
                "category": {
                  "coding": [
                    {
                      "code": "submitted",
                      "display": "Submitted Amount",
                      "system": "http://terminology.hl7.org/CodeSystem/adjudication"
                    }
                  ],
                  "text": "Submitted Amount"
                }
              }
            ],
            "type": {
              "coding": [
                {
                  "code": "institutional",
                  "system": "http://terminology.hl7.org/CodeSystem/claim-type"
                }
              ]
            },
            "use": "claim"
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/622dc825-a1a5-4b84-8fa3-04b2544ac6bb",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "vital-signs",
                    "display": "vital-signs",
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "39156-5",
                  "display": "Body Mass Index",
                  "system": "http://loinc.org"
                }
              ],
              "text": "Body Mass Index"
            },
            "effectiveDateTime": "2015-03-02T16:51:14-08:00",
            "encounter": {
              "reference": "Encounter/c427ce3e-7677-400e-bc06-33a8cecfdd77"
            },
            "id": "622dc825-a1a5-4b84-8fa3-04b2544ac6bb",
            "issued": "2015-03-02T16:51:14.816-08:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-finding-Observation",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-VitalSign",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-BodyMassIndex"
              ],
              "versionId": "MTcxOTUyMzQ2MjA1Nzg4MzAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/b0027145-32af-4030-bcb1-1f5b63d3f2e2"
            },
            "valueQuantity": {
              "code": "kg/m2",
              "system": "http://unitsofmeasure.org",
              "unit": "kg/m2",
              "value": 14.784260473706514
            }
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/20120688-2c8b-4e76-9e34-a484e32e9351",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "vital-signs",
                    "display": "vital-signs",
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "8302-2",
                  "display": "Body Height",
                  "system": "http://loinc.org"
                }
              ],
              "text": "Body Height"
            },
            "effectiveDateTime": "2015-03-02T16:51:14-08:00",
            "encounter": {
              "reference": "Encounter/c427ce3e-7677-400e-bc06-33a8cecfdd77"
            },
            "id": "20120688-2c8b-4e76-9e34-a484e32e9351",
            "issued": "2015-03-02T16:51:14.816-08:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-finding-Observation",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-VitalSign",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-BodyHeight"
              ],
              "versionId": "MTcxOTUyMzQ2MjA0NDMwMDAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/b0027145-32af-4030-bcb1-1f5b63d3f2e2"
            },
            "valueQuantity": {
              "code": "cm",
              "system": "http://unitsofmeasure.org",
              "unit": "cm",
              "value": 120.50639269008305
            }
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/8100f70c-fa98-41b1-b23c-151cdea433b3",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "vital-signs",
                    "display": "vital-signs",
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "29463-7",
                  "display": "Body Weight",
                  "system": "http://loinc.org"
                }
              ],
              "text": "Body Weight"
            },
            "effectiveDateTime": "2015-03-02T16:51:14-08:00",
            "encounter": {
              "reference": "Encounter/c427ce3e-7677-400e-bc06-33a8cecfdd77"
            },
            "id": "8100f70c-fa98-41b1-b23c-151cdea433b3",
            "issued": "2015-03-02T16:51:14.816-08:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-finding-Observation",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-VitalSign",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-BodyWeight"
              ],
              "versionId": "MTcxOTUyMzQ2MjA1MTc2MjAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/b0027145-32af-4030-bcb1-1f5b63d3f2e2"
            },
            "valueQuantity": {
              "code": "kg",
              "system": "http://unitsofmeasure.org",
              "unit": "kg",
              "value": 21.469393594558884
            }
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/df225fb0-7811-466f-bd5d-57c10059ce22",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "vital-signs",
                    "display": "vital-signs",
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "72514-3",
                  "display": "Pain severity - 0-10 verbal numeric rating [Score] - Reported",
                  "system": "http://loinc.org"
                }
              ],
              "text": "Pain severity - 0-10 verbal numeric rating [Score] - Reported"
            },
            "effectiveDateTime": "2015-03-02T16:51:14-08:00",
            "encounter": {
              "reference": "Encounter/c427ce3e-7677-400e-bc06-33a8cecfdd77"
            },
            "id": "df225fb0-7811-466f-bd5d-57c10059ce22",
            "issued": "2015-03-02T16:51:14.816-08:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-finding-Observation",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-VitalSign"
              ],
              "versionId": "MTcxOTUyMzQ2MjA1MDkwOTAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/b0027145-32af-4030-bcb1-1f5b63d3f2e2"
            },
            "valueQuantity": {
              "code": "{score}",
              "system": "http://unitsofmeasure.org",
              "unit": "{score}",
              "value": 3.1080799298691533
            }
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/4415e34b-cec8-4316-98ae-fc29cea862b5",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "vital-signs",
                    "display": "vital-signs",
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "55284-4",
                  "display": "Blood Pressure",
                  "system": "http://loinc.org"
                }
              ],
              "text": "Blood Pressure"
            },
            "component": [
              {
                "code": {
                  "coding": [
                    {
                      "code": "8462-4",
                      "display": "Diastolic Blood Pressure",
                      "system": "http://loinc.org"
                    }
                  ],
                  "text": "Diastolic Blood Pressure"
                },
                "valueQuantity": {
                  "code": "mm[Hg]",
                  "system": "http://unitsofmeasure.org",
                  "unit": "mm[Hg]",
                  "value": 75.44894870094959
                }
              },
              {
                "code": {
                  "coding": [
                    {
                      "code": "8480-6",
                      "display": "Systolic Blood Pressure",
                      "system": "http://loinc.org"
                    }
                  ],
                  "text": "Systolic Blood Pressure"
                },
                "valueQuantity": {
                  "code": "mm[Hg]",
                  "system": "http://unitsofmeasure.org",
                  "unit": "mm[Hg]",
                  "value": 119.00010973273238
                }
              }
            ],
            "effectiveDateTime": "2015-03-02T16:51:14-08:00",
            "encounter": {
              "reference": "Encounter/c427ce3e-7677-400e-bc06-33a8cecfdd77"
            },
            "id": "4415e34b-cec8-4316-98ae-fc29cea862b5",
            "issued": "2015-03-02T16:51:14.816-08:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-finding-Observation",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-VitalSign",
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-vital-BloodPressure"
              ],
              "versionId": "MTcxOTUyMzQ2MjA1ODI5NDAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/b0027145-32af-4030-bcb1-1f5b63d3f2e2"
            }
          }
        },
        {
          "fullUrl": "https://healthcare.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/f151e38c-c7bf-4c34-b015-6ef9e0a947bc",
          "resource": {
            "category": [
              {
                "coding": [
                  {
                    "code": "survey",
                    "display": "survey",
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category"
                  }
                ]
              }
            ],
            "code": {
              "coding": [
                {
                  "code": "72166-2",
                  "display": "Tobacco smoking status NHIS",
                  "system": "http://loinc.org"
                }
              ],
              "text": "Tobacco smoking status NHIS"
            },
            "effectiveDateTime": "2015-03-02T16:51:14-08:00",
            "encounter": {
              "reference": "Encounter/c427ce3e-7677-400e-bc06-33a8cecfdd77"
            },
            "id": "f151e38c-c7bf-4c34-b015-6ef9e0a947bc",
            "issued": "2015-03-02T16:51:14.816-08:00",
            "meta": {
              "lastUpdated": "YYYY-MM-DDTHH:MM:SS+ZZ:ZZ",
              "profile": [
                "http://standardhealthrecord.org/fhir/StructureDefinition/shr-finding-Observation"
              ],
              "versionId": "MTcxOTUyMzQ2MjA2NDIzNzAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/b0027145-32af-4030-bcb1-1f5b63d3f2e2"
            },
            "valueCodeableConcept": {
              "coding": [
                {
                  "code": "266919005",
                  "display": "Never smoker",
                  "system": "http://snomed.info/sct"
                }
              ],
              "text": "Never smoker"
            }
          }
        }
      ],
      "total": 12
    }
    

## Getting all patient compartment resources

The following samples show how to get all resources associated with a particular patient compartment ([DSTU2](https://hl7.org/fhir/DSTU2/patient-operations.html#everything), [STU3](https://www.hl7.org/fhir/STU3/compartmentdefinition-patient.html), [R4](https://www.hl7.org/fhir/R4/compartmentdefinition-patient.html), and [R5](https://www.hl7.org/fhir/R5/compartmentdefinition-patient.html)). For more information, see [`projects.locations.datasets.fhirStores.fhir.Patient-everything`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Patient-everything).

The following REST samples work with R4 FHIR stores. The Go, Java, Node.js, and Python samples work with STU3 FHIR stores.

### Console

To view resources in a patient compartment in the FHIR Viewer, follow the below steps:

  1. In the Google Cloud console, go to the **FHIR Viewer**. 

[Go to FHIR Viewer](https://console.cloud.google.com/healthcare/fhirviewer)

  2. In the **FHIR Store** drop-down list, select a dataset, and then select a FHIR store in the dataset. 
  3. To filter the list of resource types for `Patient` resources, click the **Resource Type** field and then select **Resource Type** in the **Properties** drop-down list. Enter `Patient` as the filter value. 
  4. Click the `Patient` resource type link in the table row.
  5. In the table of resources that appears, select or [search for](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search#using_the_fhir_viewer) a patient. 
  6. An **Explore patient** button appears in the top-right; click it to view the patient compartment. 



### curl

To get the resources in a patient compartment, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The patient's ID
  * An access token



The following sample shows a `GET` request using `curl`:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID/\$everything"

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "entry": [
        {
          "resource": {
            "birthDate": "1970-01-01",
            "gender": "female",
            "id": "PATIENT_ID",
            "name": [
              {
                "family": "Smith",
                "given": [
                  "Darcy"
                ],
                "use": "official"
              }
            ],
            "resourceType": "Patient"
          }
        },
        {
          "resource": {
            "class": {
              "code": "IMP",
              "display": "inpatient encounter",
              "system": "http://hl7.org/fhir/v3/ActCode"
            },
            "id": "ENCOUNTER_ID",
            "reasonCode": [
              {
                "text": "The patient had an abnormal heart rate. She was concerned about this."
              }
            ],
            "resourceType": "Encounter",
            "status": "finished",
            "subject": {
              "reference": "Patient/PATIENT_ID"
            }
          }
        },
        {
          "resource": {
            "encounter": {
              "reference": "Encounter/ENCOUNTER_ID"
            },
            "effectiveDateTime": "2020-01-01T00:00:00+00:00",
            "id": "OBSERVATION_ID",
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/PATIENT_ID"
            },
            "valueQuantity": {
              "unit": "bpm",
              "value": BPM_VALUE
            }
          }
        }
      ],
      "resourceType": "Bundle",
      "type": "searchset"
    }
    

### PowerShell

To get the resources in a patient compartment, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The patient's ID
  * An access token



The following sample shows a `GET` request using PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -Uri 'https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/RESOURCE_ID/$everything' | ConvertTo-Json

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "entry": [
        {
          "resource": {
            "birthDate": "1970-01-01",
            "gender": "female",
            "id": "PATIENT_ID",
            "name": [
              {
                "family": "Smith",
                "given": [
                  "Darcy"
                ],
                "use": "official"
              }
            ],
            "resourceType": "Patient"
          }
        },
        {
          "resource": {
            "class": {
              "code": "IMP",
              "display": "inpatient encounter",
              "system": "http://hl7.org/fhir/v3/ActCode"
            },
            "id": "ENCOUNTER_ID",
            "reasonCode": [
              {
                "text": "The patient had an abnormal heart rate. She was concerned about this."
              }
            ],
            "resourceType": "Encounter",
            "status": "finished",
            "subject": {
              "reference": "Patient/PATIENT_ID"
            }
          }
        },
        {
          "resource": {
            "encounter": {
              "reference": "Encounter/ENCOUNTER_ID"
            },
            "effectiveDateTime": "2020-01-01T00:00:00+00:00",
            "id": "OBSERVATION_ID",
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/PATIENT_ID"
            },
            "valueQuantity": {
              "unit": "bpm",
              "value": BPM_VALUE
            }
          }
        }
      ],
      "resourceType": "Bundle",
      "type": "searchset"
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // fhirGetPatientEverything gets all resources associated with a particular
    // patient compartment.
    func fhirGetPatientEverything(w io.Writer, projectID, location, datasetID, fhirStoreID, fhirResourceID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/Patient/%s", projectID, location, datasetID, fhirStoreID, fhirResourceID)
    
    	resp, err := fhirService.PatientEverything(name).Do()
    	if err != nil {
    		return fmt.Errorf("PatientEverything: %w", err)
    	}
    
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("PatientEverything: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
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
    import org.apache.http.impl.client.HttpClients;
    
    public class FhirResourceGetPatientEverything {
      private static final String FHIR_NAME =
          "projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/Patient/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirResourceGetPatientEverything(String resourceName)
          throws IOException, URISyntaxException {
        // String resourceName =
        //    String.format(
        //        FHIR_NAME, "project-id", "region-id", "dataset-id", "store-id", "patient-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%sv1/%s/$everything", client.getRootUrl(), resourceName);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
    
        HttpUriRequest request =
            RequestBuilder.get(uriBuilder.build())
                .addHeader("Content-Type", "application/json-patch+json")
                .addHeader("Accept-Charset", "utf-8")
                .addHeader("Accept", "application/fhir+json; charset=utf-8")
                .build();
    
        // Execute the request and process the results.
        HttpResponse response = httpClient.execute(request);
        HttpEntity responseEntity = response.getEntity();
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
          System.err.print(
              String.format(
                  "Exception getting patient everythingresource: %s\n",
                  response.getStatusLine().toString()));
          responseEntity.writeTo(System.err);
          throw new RuntimeException();
        }
        System.out.println("Patient compartment results: ");
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
    
    const getPatientEverything = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const patientId = '16e8a860-33b3-49be-9b03-de979feed14a';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/Patient/${patientId}`;
      const request = {name};
    
      const patientEverything =
        await healthcare.projects.locations.datasets.fhirStores.fhir.PatientEverything(
          request
        );
      console.log(
        `Got all resources in patient ${patientId} compartment:\n`,
        JSON.stringify(patientEverything)
      );
    };
    
    getPatientEverything();

### Python
    
    
    def get_patient_everything(
        project_id,
        location,
        dataset_id,
        fhir_store_id,
        resource_id,
    ):
        """Gets all the resources in the patient compartment.
    
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
        # resource_id = 'b682d-0e-4843-a4a9-78c9ac64'  # replace with the Patient resource's ID
        url = f"{base_url}/projects/{project_id}/locations/{location}"
    
        resource_path = "{}/datasets/{}/fhirStores/{}/fhir/{}/{}".format(
            url, dataset_id, fhir_store_id, "Patient", resource_id
        )
        resource_path += "/$everything"
    
        # Sets required application/fhir+json header on the request
        headers = {"Content-Type": "application/fhir+json;charset=utf-8"}
    
        response = session.get(resource_path, headers=headers)
        response.raise_for_status()
    
        resource = response.json()
    
        print(json.dumps(resource, indent=2))
    
        return resource
    
    

### Getting patient compartment resources filtered by type or date

The following samples show how to get all resources associated with a particular [patient compartment (R4)](https://www.hl7.org/fhir/R4/compartmentdefinition-patient.html) filtered by a list of types and since a specified date and time. For more information, see [`projects.locations.datasets.fhirStores.fhir.Patient-everything`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Patient-everything).

The following REST samples work with R4 FHIR stores.

### curl

To get the resources in a patient compartment of a specified type and since a specified date, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The patient's ID
  * A query string containing a comma-separated resource type list and starting date
  * An access token



The following sample shows a `GET` request using `curl`:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID/\$everything?_type=RESOURCE_TYPES&_since=DATE"

If the request is successful, the server returns any resources that match the specified criteria in JSON format.

### PowerShell

To get the resources in a patient compartment of a specified type and since a specified date, make a `GET` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The patient's ID
  * A query string containing a comma-separated resource type list and starting date
  * An access token



The following sample shows a `GET` request using PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -Uri 'https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/RESOURCE_ID/$everything?_type=RESOURCE_TYPES&_since=DATE' | ConvertTo-Json

If the request is successful, the server returns any resources that match the specified criteria in JSON format.

## Listing FHIR resource versions

You can list the historical versions of a FHIR resource, including the current version and any deleted versions. This lets you do the following:

  * Track changes to patient records, medications, or care plans.
  * If a FHIR resource contains incorrect data, you can view historical versions to determine when the incorrect data was entered and recover the correct information.
  * Ensure regulatory compliance by providing complete audit trails.



The following REST samples work with R4 FHIR stores. The Go, Java, Node.js, and Python samples work with STU3 FHIR stores.

### Console

  1. In the Google Cloud console, go to the **FHIR viewer** page.

[Go to the FHIR viewer](https://console.cloud.google.com/healthcare/fhirviewer)

  2. In the **FHIR store** menu, select a dataset, and then select a FHIR store in the dataset.

  3. To filter the list of FHIR resource types, search for the resource types that you want to display.

  4. Click the **Resource type** field.

  5. In the **Properties** drop-down list that appears, select **Resource Type**.

  6. Enter a FHIR resource type.

  7. In the list of FHIR resource types, select a resource type.

  8. In the table of FHIR resources that appears, select or [search for](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search#using_the_fhir_viewer) a resource.

  9. To view and compare historical versions of the FHIR resource, click the **Overview** tab, and then do the following:

     1. To view historical versions of the FHIR resource, in the same row as **Version ID** , click **View historical versions**. In the **Select a resource version** pane, select the version, and then click **Confirm**. The data in the version is populated in the **Overview** , **Elements** , and **JSON** tabs.
     2. To compare two versions of the FHIR resource, in the same row as **Version ID** , click **Compare resource versions**. In the **Select resource versions to compare** pane, select two resource versions, and then click **Confirm**. The two resource versions are displayed in a diff view, with the first version you selected on the left-hand side and the second version on the right-hand side.



### REST

Use the [`projects.locations.datasets.fhirStores.fhir.history`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/history) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the FHIR store's parent dataset
  * `FHIR_STORE_ID`: the FHIR store ID
  * `RESOURCE_TYPE`: the FHIR resource type
  * `RESOURCE_ID`: the FHIR resource ID



To send your request, choose one of these options:

#### curl

The following samples show how to list all versions of an Observation resource. The Observation was updated once after its original creation to change the patient's heartbeats per minute (BPM). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/RESOURCE_TYPE/RESOURCE_ID/_history"

#### PowerShell

The following samples show how to list all versions of an Observation resource. The Observation was updated once after its original creation to change the patient's heartbeats per minute (BPM). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/RESOURCE_TYPE/RESOURCE_ID/_history" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format. In this example, it returns two versions of the Observation. In the first version, the patient's heart rate was 75 BPM. In the second version, the patient's heart rate was 85 BPM. 
    
    
    {
      "entry": [
        {
          "resource": {
            "effectiveDateTime": "2020-01-01T00:00:00+00:00",
            "id": "OBSERVATION_ID",
            "meta": {
              "lastUpdated": "2020-01-02T00:00:00+00:00",
              "versionId": "MTU0MTE5MDk5Mzk2ODcyODAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/PATIENT_ID"
            },
            "valueQuantity": {
              "unit": "bpm",
              "value": 85
            }
          }
        },
        {
          "resource": {
            "encounter": {
              "reference": "Encounter/ENCOUNTER_ID"
            },
            "effectiveDateTime": "2020-01-01T00:00:00+00:00",
            "id": "OBSERVATION_ID",
            "meta": {
              "lastUpdated": "2020-01-01T00:00:00+00:00",
              "versionId": "MTU0MTE5MDg4MTY0MzQ3MjAwMA"
            },
            "resourceType": "Observation",
            "status": "final",
            "subject": {
              "reference": "Patient/PATIENT_ID"
            },
            "valueQuantity": {
              "unit": "bpm",
              "value": 75
            }
          }
        }
      ],
      "resourceType": "Bundle",
      "type": "history"
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // listFHIRResourceHistory lists an FHIR resource's history.
    func listFHIRResourceHistory(w io.Writer, projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s", projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID)
    
    	resp, err := fhirService.History(name).Do()
    	if err != nil {
    		return fmt.Errorf("History: %w", err)
    	}
    
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("History: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
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
    import org.apache.http.impl.client.HttpClients;
    
    public class FhirResourceListHistory {
      private static final String FHIR_NAME =
          "projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirResourceListHistory(String resourceName)
          throws IOException, URISyntaxException {
        // String resourceName =
        //    String.format(
        //        FHIR_NAME, "project-id", "region-id", "dataset-id", "store-id", "resource-type",
        //  "resource-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%sv1/%s/_history", client.getRootUrl(), resourceName);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
    
        HttpUriRequest request =
            RequestBuilder.get()
                .setUri(uriBuilder.build())
                .addHeader("Content-Type", "application/fhir+json")
                .addHeader("Accept-Charset", "utf-8")
                .addHeader("Accept", "application/fhir+json; charset=utf-8")
                .build();
    
        // Execute the request and process the results.
        HttpResponse response = httpClient.execute(request);
        HttpEntity responseEntity = response.getEntity();
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
          System.err.print(
              String.format(
                  "Exception retrieving FHIR history: %s\n", response.getStatusLine().toString()));
          responseEntity.writeTo(System.err);
          throw new RuntimeException();
        }
        System.out.println("FHIR resource history retrieved: ");
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
      responseType: 'json',
    });
    
    const listFhirResourceHistory = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const resourceType = 'Patient';
      // const resourceId = '16e8a860-33b3-49be-9b03-de979feed14a';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/${resourceType}/${resourceId}/_history`;
      const request = {name};
    
      const resource =
        await healthcare.projects.locations.datasets.fhirStores.fhir.read(
          request
        );
      console.log(JSON.stringify(resource.data, null, 2));
    };
    
    listFhirResourceHistory();

### Python
    
    
    # Imports the types Dict and Any for runtime type hints.
    from typing import Any, Dict  # noqa: E402
    
    
    def list_resource_history(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
        resource_type: str,
        resource_id: str,
    ) -> Dict[str, Any]:
        """Gets the history of a resource.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample.
        See
        https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.fhirStores.fhir.html#history
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Cloud project you want
            to use.
          location: The name of the parent dataset's location.
          dataset_id: The name of the parent dataset.
          fhir_store_id: The name of the FHIR store.
          resource_type: The type of FHIR resource.
          resource_id: The "logical id" of the resource whose history you want to
            list. The ID is assigned by the server.
    
        Returns:
          A dict representing the FHIR resource.
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
        # resource_type = 'Patient'
        # resource_id = 'b682d-0e-4843-a4a9-78c9ac64'
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_resource_path = f"{fhir_store_parent}/fhirStores/{fhir_store_id}/fhir/{resource_type}/{resource_id}"
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .history(name=fhir_resource_path)
        )
        response = request.execute()
        print(
            f"History for {resource_type} resource with ID {resource_id}:\n"
            f" {json.dumps(response, indent=2)}"
        )
        return response
    
    

## Retrieving a FHIR resource version

The following samples show how to retrieve a specific version of a FHIR resource. To find a specific version, you can list the versions of the FHIR resource and then view information for that version. The version ID is contained in the `"versionId"` field. For example, see the following JSON body where the version IDs for the Observation resource in Listing FHIR resource versions are highlighted:
    
    
    {
      "entry": [
        {
          "resource": {
            "effectiveDateTime": "2020-01-01T00:00:00+00:00",
            "id": "OBSERVATION_ID",
            "meta": {
              "lastUpdated": "2020-01-02T00:00:00+00:00",
              **"versionId": "MTU0MTE5MDk5Mzk2ODcyODAwMA"**
            },
    ...
        {
          "resource": {
            "encounter": {
              "reference": "Encounter/ENCOUNTER_ID"
            },
            "effectiveDateTime": "2020-01-01T00:00:00+00:00",
            "id": "OBSERVATION_ID",
            "meta": {
              "lastUpdated": "2020-01-01T00:00:00+00:00",
              **"versionId": "MTU0MTE5MDg4MTY0MzQ3MjAwMA"**
            },
    ...
    }
    

The following samples use the resources created in Creating a FHIR resource and show how to view an Observation resource. The REST samples work with R4 FHIR stores. The Go, Node.js, and Python samples work with STU3 FHIR stores.

### Console

  1. In the Google Cloud console, go to the **FHIR viewer** page.

[Go to the FHIR viewer](https://console.cloud.google.com/healthcare/fhirviewer)

  2. In the **FHIR store** menu, select a dataset, and then select a FHIR store in the dataset.

  3. To filter the list of FHIR resource types, search for the resource types that you want to display.

  4. Click the **Resource type** field.

  5. In the **Properties** drop-down list that appears, select **Resource Type**.

  6. Enter a FHIR resource type.

  7. In the list of FHIR resource types, select a resource type.

  8. In the table of FHIR resources that appears, select or [search for](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search#using_the_fhir_viewer) a resource.

  9. To view a specific version of the FHIR resource, do the following:

     1. Click the **Overview** tab.
     2. In the same row as **Version ID** , click **View historical versions**.
     3. In the **Select a resource version** pane, select the version, and then click **Confirm**. The data in the version is populated in the **Overview** , **Elements** , and **JSON** tabs.



### REST

Use the [`projects.locations.datasets.fhirStores.fhir.vread`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/vread) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the FHIR store's parent dataset
  * `FHIR_STORE_ID`: the FHIR store ID
  * `RESOURCE_TYPE`: the FHIR resource type
  * `RESOURCE_ID`: the FHIR resource ID
  * `RESOURCE_VERSION`: the FHIR resource version



To send your request, choose one of these options:

#### curl

The following samples show how to list all versions of an Observation resource. The Observation was updated once after its original creation to change the patient's heartbeats per minute (BPM). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/RESOURCE_TYPE/RESOURCE_ID/_history/RESOURCE_VERSION"

#### PowerShell

The following samples show how to list all versions of an Observation resource. The Observation was updated once after its original creation to change the patient's heartbeats per minute (BPM). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/RESOURCE_TYPE/RESOURCE_ID/_history/RESOURCE_VERSION" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format. In this example, the first version of the Observation, where the patient's heart rate was 75 BPM, is returned. 
    
    
    {
      "encounter": {
        "reference": "Encounter/ENCOUNTER_ID"
      },
      "effectiveDateTime": "2020-01-01T00:00:00+00:00",
      "id": "OBSERVATION_ID",
      "meta": {
        "lastUpdated": "2020-01-01T00:00:00+00:00",
        "versionId": "MTU0MTE5MDg4MTY0MzQ3MjAwMA"
      },
      "resourceType": "Observation",
      "status": "final",
      "subject": {
        "reference": "Patient/PATIENT_ID"
      },
      "valueQuantity": {
        "unit": "bpm",
        "value": 75
      }
    }
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // getFHIRResourceHistory gets an FHIR resource history.
    func getFHIRResourceHistory(w io.Writer, projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID, versionID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s/_history/%s", projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID, versionID)
    
    	resp, err := fhirService.Vread(name).Do()
    	if err != nil {
    		return fmt.Errorf("Vread: %w", err)
    	}
    
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("Vread: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
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
    import org.apache.http.impl.client.HttpClients;
    
    public class FhirResourceGetHistory {
      private static final String FHIR_NAME =
          "projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirResourceGetHistory(String resourceName, String versionId)
          throws IOException, URISyntaxException {
        // String resourceName =
        //    String.format(
        //        FHIR_NAME, "project-id", "region-id", "dataset-id", "store-id", "resource-type",
        // "resource-id");
        // String versionId = "version-uuid"
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%sv1/%s/_history/%s", client.getRootUrl(), resourceName, versionId);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
    
        HttpUriRequest request =
            RequestBuilder.get()
                .setUri(uriBuilder.build())
                .addHeader("Content-Type", "application/fhir+json")
                .addHeader("Accept-Charset", "utf-8")
                .addHeader("Accept", "application/fhir+json; charset=utf-8")
                .build();
    
        // Execute the request and process the results.
        HttpResponse response = httpClient.execute(request);
        HttpEntity responseEntity = response.getEntity();
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
          System.err.print(
              String.format(
                  "Exception retrieving FHIR history: %s\n", response.getStatusLine().toString()));
          responseEntity.writeTo(System.err);
          throw new RuntimeException();
        }
        System.out.println("FHIR resource retrieved from version: ");
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
      responseType: 'json',
    });
    
    const getFhirResourceHistory = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const resourceType = 'Patient';
      // const resourceId = '16e8a860-33b3-49be-9b03-de979feed14a';
      // const versionId = 'MTU2NPg3NDgyNDAxMDc4OTAwMA';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/${resourceType}/${resourceId}/_history/${versionId}`;
      const request = {name};
    
      const resource =
        await healthcare.projects.locations.datasets.fhirStores.fhir.vread(
          request
        );
      console.log(JSON.stringify(resource.data, null, 2));
    };
    
    getFhirResourceHistory();

### Python
    
    
    # Imports the types Dict and Any for runtime type hints.
    from typing import Any, Dict  # noqa: E402
    
    
    def get_resource_history(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
        resource_type: str,
        resource_id: str,
        version_id: str,
    ) -> Dict[str, Any]:
        """Gets the contents of a version (current or historical) of a FHIR resource by version ID.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample.
        See
        https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.fhirStores.fhir.html#vread
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Cloud project you want
            to use.
          location: The name of the parent dataset's location.
          dataset_id: The name of the parent dataset.
          fhir_store_id: The name of the FHIR store.
          resource_type: The type of FHIR resource.
          resource_id: The "logical id" of the resource whose details you want to view
            at a particular version. The ID is assigned by the server.
          version_id: The ID of the version. Changes whenever the FHIR resource is
            modified.
    
        Returns:
          A dict representing the FHIR resource at the specified version.
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
        # resource_type = 'Patient'
        # resource_id = 'b682d-0e-4843-a4a9-78c9ac64'
        # version_id = 'MTY4NDQ1MDc3MDU2ODgyNzAwMA'
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_resource_path = f"{fhir_store_parent}/fhirStores/{fhir_store_id}/fhir/{resource_type}/{resource_id}/_history/{version_id}"
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .vread(name=fhir_resource_path)
        )
        response = request.execute()
        print(
            f"Got contents of {resource_type} resource with ID {resource_id} at"
            f" version {version_id}:\n {json.dumps(response, indent=2)}"
        )
    
        return response
    
    

## Deleting a FHIR resource

The following samples show how to call the [`projects.locations.datasets.fhirStores.fhir.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/delete) method to delete an Observation FHIR resource.

Regardless of whether the operation succeeds or fails, the server returns a `200 OK` HTTP status code. To check that the resource was successfully deleted, [search for](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search) or get the resource and see if it exists.

The following REST samples work with R4 FHIR stores. The Go, Java, Node.js, and Python samples work with STU3 FHIR stores.

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the FHIR store's parent dataset
  * FHIR_STORE_ID: the FHIR store ID
  * OBSERVATION_ID: the Observation resource ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/OBSERVATION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation/OBSERVATION_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

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
    
    // deleteFHIRResource deletes an FHIR resource.
    // Regardless of whether the operation succeeds or
    // fails, the server returns a 200 OK HTTP status code. To check that the
    // resource was successfully deleted, search for or get the resource and
    // see if it exists.
    func deleteFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s", projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID)
    
    	if _, err := fhirService.Delete(name).Do(); err != nil {
    		return fmt.Errorf("Delete: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted %q", name)
    
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
    import org.apache.http.impl.client.HttpClients;
    
    public class FhirResourceDelete {
      private static final String FHIR_NAME =
          "projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirResourceDelete(String resourceName)
          throws IOException, URISyntaxException {
        // String resourceName =
        //    String.format(
        //        FHIR_NAME, "project-id", "region-id", "dataset-id", "store-id", "resource-type",
        // "resource-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%sv1/%s", client.getRootUrl(), resourceName);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
    
        HttpUriRequest request =
            RequestBuilder.delete()
                .setUri(uriBuilder.build())
                .addHeader("Content-Type", "application/fhir+json")
                .addHeader("Accept-Charset", "utf-8")
                .addHeader("Accept", "application/fhir+json; charset=utf-8")
                .build();
    
        // Execute the request and process the results.
        // Regardless of whether the operation succeeds or
        // fails, the server returns a 200 OK HTTP status code. To check that the
        // resource was successfully deleted, search for or get the resource and
        // see if it exists.
        HttpResponse response = httpClient.execute(request);
        HttpEntity responseEntity = response.getEntity();
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
          String errorMessage =
              String.format(
                  "Exception deleting FHIR resource: %s\n", response.getStatusLine().toString());
          System.err.print(errorMessage);
          responseEntity.writeTo(System.err);
          throw new RuntimeException(errorMessage);
        }
        System.out.println("FHIR resource deleted.");
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
      responseType: 'json',
    });
    
    const deleteFhirResource = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const resourceType = 'Patient';
      // const resourceId = '9a664e07-79a4-4c2e-04ed-e996c75484e1';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/${resourceType}/${resourceId}`;
      const request = {name};
    
      // Regardless of whether the operation succeeds or
      // fails, the server returns a 200 OK HTTP status code. To check that the
      // resource was successfully deleted, search for or get the resource and
      // see if it exists.
      try {
        await healthcare.projects.locations.datasets.fhirStores.fhir.delete(
          request
        );
        console.log(`Deleted FHIR resource: ${resourceId}`);
      } catch (error) {
        console.error('Error deleting FHIR resource:', error.message || error);
      }
    };
    
    deleteFhirResource();

### Python
    
    
    def delete_resource(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
        resource_type: str,
        resource_id: str,
    ) -> dict:
        """Deletes a FHIR resource.
    
        Regardless of whether the operation succeeds or
        fails, the server returns a 200 OK HTTP status code. To check that the
        resource was successfully deleted, search for or get the resource and
        see if it exists.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample.
        See
        https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.fhirStores.fhir.html#delete
        for the Python API reference.
        Args:
          project_id: The project ID or project number of the Cloud project you want
            to use.
          location: The name of the parent dataset's location.
          dataset_id: The name of the parent dataset.
          fhir_store_id: The name of the FHIR store.
          resource_type: The type of the FHIR resource.
          resource_id: The "logical id" of the FHIR resource you want to delete. The
            ID is assigned by the server.
    
        Returns:
          An empty dict.
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
        # resource_type = 'Patient'
        # resource_id = 'b682d-0e-4843-a4a9-78c9ac64'
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_resource_path = f"{fhir_store_parent}/fhirStores/{fhir_store_id}/fhir/{resource_type}/{resource_id}"
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .delete(name=fhir_resource_path)
        )
        response = request.execute()
        print(f"Deleted {resource_type} resource with ID {resource_id}.")
    
        return response
    
    

### Conditionally delete a FHIR resource

In the Cloud Healthcare API v1, conditional operations exclusively use the `identifier` search parameter, if it exists for the FHIR resource type, to determine which FHIR resources match a conditional search query. 

A FHIR resource matches the query `?identifier=my-code-system|ABC-12345` if and only if the resource's `identifier.system` is `my-code-system` and its `identifier.value` is `ABC-12345`. If a FHIR resource matches the query, the Cloud Healthcare API deletes the resource.

If the query uses the `identifier` search parameter and matches multiple FHIR resources, the Cloud Healthcare API returns a `"412 - Condition not selective enough"` error. To individually delete the resources, follow these steps:

  1. [Search](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search) for each resource to get its unique server-assigned ID.
  2. Individually delete each resource using the ID.



The following samples show how to conditionally delete a FHIR resource that matches a search query, rather than identifying the FHIR resource by its ID. The search query matches and deletes an Observation resource using the Observation's identifier (`ABC-12345` in `my-code-system`).

### REST

Use the [`projects.locations.datasets.fhirStores.fhir.conditionalDelete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/conditionalDelete) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the FHIR store's parent dataset
  * `FHIR_STORE_ID`: the FHIR store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?identifier=my-code-system|ABC-12345"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Observation?identifier=my-code-system|ABC-12345" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/conditionalDelete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a successful status code (2xx) and an empty response.

## Delete historical versions of a FHIR resource

The following samples show how to delete all historical versions of a FHIR resource using the [`projects.locations.datasets.fhirStores.fhir.Resource-purge`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Resource-purge) method.

Calling the `projects.locations.datasets.fhirStores.fhir.Resource-purge` method is limited to users (callers) with the [`roles/healthcare.fhirStoreAdmin`](https://docs.cloud.google.com/healthcare-api/docs/access-control#roles) role; users with the `roles/healthcare.fhirResourceEditor` role cannot call the method. To permit a caller to delete historical versions of a FHIR resource, either:

  * Make sure that the caller has the `roles/healthcare.fhirStoreAdmin` role.
  * Create a [custom IAM role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) with the [`healthcare.fhirResources.purge`](https://docs.cloud.google.com/healthcare-api/docs/access-control#fhir_store_methods) permission and assign the role to the caller.



The samples use the resources created in Creating a FHIR resource and show how to delete the historical versions of an Observation resource.

The following REST samples work with R4 FHIR stores. The Go, Java, Node.js, and Python samples work with STU3 FHIR stores.

### REST

Use the [`projects.locations.datasets.fhirStores.fhir.Resource-purge`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Resource-purge) method.

**Important:** When making a `curl` request, replace `/$purge` in the URL with `\/$purge`. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project
  * `LOCATION`: the dataset location
  * `DATASET_ID`: the FHIR store's parent dataset
  * `FHIR_STORE_ID`: the FHIR store ID
  * `RESOURCE_TYPE`: the FHIR resource type
  * `RESOURCE_ID`: the FHIR resource ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/RESOURCE_TYPE/RESOURCE_ID/$purge"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/RESOURCE_TYPE/RESOURCE_ID/$purge" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // purgeFHIRResource purges an FHIR resources.
    func purgeFHIRResource(w io.Writer, projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s", projectID, location, datasetID, fhirStoreID, resourceType, fhirResourceID)
    
    	if _, err := fhirService.ResourcePurge(name).Do(); err != nil {
    		return fmt.Errorf("ResourcePurge: %w", err)
    	}
    
    	fmt.Fprintf(w, "Resource Purged: %q", name)
    
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
    import org.apache.http.impl.client.HttpClients;
    
    public class FhirResourceDeletePurge {
      private static final String FHIR_NAME =
          "projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirResourceDeletePurge(String resourceName)
          throws IOException, URISyntaxException {
        // String resourceName =
        //    String.format(
        //        FHIR_NAME, "project-id", "region-id", "dataset-id", "store-id", "resource-type",
        // "resource-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%sv1/%s/$purge", client.getRootUrl(), resourceName);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
    
        HttpUriRequest request =
            RequestBuilder.delete()
                .setUri(uriBuilder.build())
                .addHeader("Content-Type", "application/fhir+json")
                .addHeader("Accept-Charset", "utf-8")
                .addHeader("Accept", "application/fhir+json; charset=utf-8")
                .build();
    
        // Execute the request and process the results.
        HttpResponse response = httpClient.execute(request);
        HttpEntity responseEntity = response.getEntity();
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
          String errorMessage =
              String.format(
                  "Exception purging FHIR resource: %s\n", response.getStatusLine().toString());
          System.err.print(errorMessage);
          responseEntity.writeTo(System.err);
          throw new RuntimeException(errorMessage);
        }
        System.out.println("FHIR resource history purged (excluding current version).");
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
      responseType: 'json',
    });
    
    const deleteFhirResourcePurge = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const resourceType = 'Patient';
      // const resourceId = '9a664e07-79a4-4c2e-04ed-e996c75484e1';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/${resourceType}/${resourceId}`;
      const request = {name};
    
      try {
        await healthcare.projects.locations.datasets.fhirStores.fhir.ResourcePurge(
          request
        );
        console.log(`Purged all historical versions of resource: ${resourceId}`);
      } catch (error) {
        console.error('Error purging FHIR resource:', error.message || error);
      }
    };
    
    deleteFhirResourcePurge();

### Python
    
    
    def delete_resource_purge(
        project_id: str,
        location: str,
        dataset_id: str,
        fhir_store_id: str,
        resource_type: str,
        resource_id: str,
    ) -> dict:
        """Deletes all versions of a FHIR resource (excluding the current version).
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/fhir
        before running the sample.
        See
        https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.fhirStores.fhir.html#Resource_purge
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Cloud project you want
            to use.
          location: The name of the parent dataset's location.
          dataset_id: The name of the parent dataset.
          fhir_store_id: The name of the FHIR store.
          resource_type: The type of the FHIR resource.
          resource_id: The "logical id" of the resource. The ID is assigned by the
            server.
    
        Returns:
          An empty dict.
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
        # resource_type = 'Patient'
        # resource_id = 'b682d-0e-4843-a4a9-78c9ac64'
        fhir_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
        fhir_resource_path = f"{fhir_store_parent}/fhirStores/{fhir_store_id}/fhir/{resource_type}/{resource_id}"
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .fhir()
            .Resource_purge(name=fhir_resource_path)
        )
        response = request.execute()
        print(
            f"Deleted all versions of {resource_type} resource with ID"
            f" {resource_id} (excluding current version)."
        )
        return response
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
