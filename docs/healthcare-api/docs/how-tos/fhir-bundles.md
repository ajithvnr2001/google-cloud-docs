---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bundles/
title: Managing FHIR resources using FHIR bundles \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:39.537385+00:00
---

# Managing FHIR resources using FHIR bundles  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-bundles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Managing FHIR resources using FHIR bundles Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to manage FHIR resources by executing [FHIR bundles](https://www.hl7.org/fhir/bundle.html), which are a collection of FHIR resources and operations to perform on those FHIR resources.

The [`ExecuteBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle) method implements the FHIR standard batch/transaction interaction ([DSTU2](https://hl7.org/fhir/dstu2/http.html#transaction), [STU3](https://hl7.org/fhir/STU3/http.html#transaction), [R4](https://hl7.org/fhir/r4/http.html#transaction), and [R5](https://hl7.org/fhir/r5/http.html#transaction)) and history operations.

## FHIR bundles

A FHIR bundle contains an array of entries, each of which represents an operation, such as create, update, or delete, on a resource, such as an Observation or a Patient. See the [detailed descriptions for the elements in the Bundle resource](https://www.hl7.org/fhir/bundle-definitions.html#Bundle).

When you execute a FHIR bundle, the bundle type determines how the operations in the bundle are performed. The following bundle types are available:

  * `batch`: executes the operations as multiple independent requests.
  * `transaction`: executes the operations as multiple requests that depend on one another.
  * `history`: inserts the entries into a resource's history.



For example, suppose that a transaction bundle includes creating a Patient resource and an Observation resource. If the Patient resource creation request fails, then the Observation resource is not created.

**Important:** FHIR stores only support the UTF-8 character set. Resources that contain characters not in the UTF-8 character set are rejected.

If an operation fails when the bundle type is `batch`, the Cloud Healthcare API executes the remaining operations in the bundle. If an operation fails when the bundle type is `transaction`, the Cloud Healthcare API stops executing operations and rolls back the transaction.

### History bundles

History bundles are custom extensions to the FHIR standard that support backup and restore use cases, such as synchronization. You can use history bundles to insert or replace resource versions in a FHIR resource's history. You can only remove resource versions using the [`Resource-purge`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/Resource-purge) method. The `history` bundle is executed as a single transaction with a limit of 100 entries per bundle. If a resource version in the `history` bundle has a timestamp greater than the latest version in the FHIR store, then the latest version will be updated accordingly. If the `history` bundle is inserted successfully, an empty response is returned, otherwise an `OperationOutcome` is returned describing the failure.

Support for history bundles isn't enabled by default. A FHIR store administrator must set `enableHistoryModifications` to `true` on the [FHIR store configuration](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1beta1/projects.locations.datasets.fhirStores). You can't use history bundles if `disableResourceVersioning` is set to `true` on the FHIR store configuration.

History bundles are provided in the same format in which they are returned from the [`fhir.history`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/history) method. To be valid, each bundle entry requires a resource ID, modification timestamp, and status. Additionally, all entries must have the same resource ID. The resource ID is provided with the `resource.id` field or the `request.url` field. If fields are provided, the provided resource ID be the same. The resource timestamp is provided with the `meta.lastUpdated` field in the resource or the `response.lastModified` field.

## Granting permissions for executing bundles

The `datasets.fhirStores.fhir.executeBundle` permission role is required to execute bundles. To grant this permission, use the `healthcare.fhirResourceReader` role. For the steps to grant this permission, see [Modifying a policy](https://docs.cloud.google.com/healthcare-api/docs/how-tos/controlling-access#modifying_a_policy_3).

To execute history bundles, the `datasets.fhirStores.fhir.import` permission role is also required.

The Cloud Healthcare API checks permissions for each operation in the bundle. If you have `healthcare.fhirResources.create` permission but not `healthcare.fhirResources.update` permission, you can only execute bundles containing `healthcare.fhirResources.create` operations.

## Executing a bundle

To execute a FHIR bundle, use the [`projects.locations.datasets.fhirStores.fhir.executeBundle`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/executeBundle) method.

In the following samples, BUNDLE.json is the path and filename to a JSON-encoded FHIR bundle. You can also include the bundle in the request body.

The following sample Bundle creates a Patient resource and deletes another Patient resource:
    
    
    {
      "resourceType": "Bundle",
      "id": "bundle-transaction",
      "meta": {
        "lastUpdated": "2018-03-11T11:22:16Z"
      },
      "type": "transaction",
      "entry": [
        {
          "resource": {
            "resourceType": "Patient",
            "name": [
              {
                "family": "Smith",
                "given": [
                  "Darcy"
                ]
              }
            ],
            "gender": "female",
            "address": [
              {
                "line": [
                  "123 Main St."
                ],
                "city": "Anycity",
                "state": "CA",
                "postalCode": "12345"
              }
            ]
          },
          "request": {
            "method": "POST",
            "url": "Patient"
          }
        },
        {
          "request": {
            "method": "DELETE",
            "url": "Patient/1234567890"
          }
        }
      ]
    }
    

The following samples show how to execute a bundle.

### curl

To execute a bundle, make a `POST` request and specify the following information:

  * The name and location of the parent dataset and FHIR store
  * The location of the bundle file on your local machine
  * An access token



The following sample shows a `POST` request using curl:
    
    
    curl -X POST \
        -H "Content-Type: application/fhir+json; charset=utf-8" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        --data @BUNDLE_FILE.json \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir"

Regardless of the outcome of the individual operations, after executing a batch bundle, the server returns a JSON-encoded representation of a `Bundle` resource of type `batch-response`. The `Bundle` resource contains one entry for each entry in the request with the outcome of processing the entry, which could be a mix of success and error results.

If a transaction bundle is successful, the server returns a JSON-encoded representation of a `Bundle` resource of type `transaction-response` containing one entry for each entry in the request with the successful outcome of the operation.

If an error occurs while executing a transaction bundle, the response body does not contain a bundle. Instead, it contains a JSON-encoded `OperationOutcome` resource describing the reason for the error. Successful operations that were rolled back are not reported in the response.

The following sample bundle is the output from successfully executing the above example. The first entry indicates the success of the operation to create a Patient and includes the ID of the new resource. The second entry indicates the success of the delete operation.
    
    
    {
      "entry": [
        {
          "response": {
            "location": projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/RESOURCE/RESOURCE_ID,
            "status": "201 Created"
          }
        },
        {
          "response": {
            "status": "200 OK"
          }
        }
      ],
      "resourceType": "Bundle",
      "type": "transaction-response"
    }
    

### PowerShell

To execute a bundle, make a `POST` request and specify the following information:

  * The name and location of the parent dataset and FHIR store
  * The location of the bundle file on your local machine
  * An access token



The following sample shows a `POST` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/fhir+json" `
      -InFile BUNDLE_FILE.json `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir" | ConvertTo-Json

Regardless of the outcome of the individual operations, after executing a batch bundle, the server returns a JSON-encoded representation of a `Bundle` resource of type `batch-response`. The `Bundle` resource contains one entry for each entry in the request with the outcome of processing the entry, which could be a mix of success and error results.

If a transaction bundle is successful, the server returns a JSON-encoded representation of a `Bundle` resource of type `transaction-response` containing one entry for each entry in the request with the successful outcome of the operation.

If an error occurs while executing a transaction bundle, the response body does not contain a bundle. Instead, it contains a JSON-encoded `OperationOutcome` resource describing the reason for the error. Successful operations that were rolled back are not reported in the response.

The following sample bundle is the output from successfully executing the above example. The first entry indicates the success of the operation to create a Patient and includes the ID of the new resource. The second entry indicates the success of the delete operation.
    
    
    {
      "entry": [
        {
          "response": {
            "etag": "ETAG",
            "lastModified": "2020-08-03T04:12:47.312669+00:00",
            "location": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/RESOURCE/RESOURCE_ID",
            "status": "201 Created"
          }
        },
        {
          "response": {
            "etag": "ETAG",
            "lastModified": "2020-08-03T04:12:47.312669+00:00",
            "status": "200 OK"
          }
        }
      ],
      "resourceType": "Bundle",
      "type": "transaction-response"
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
    
    // fhirExecuteBundle executes an FHIR bundle.
    func fhirExecuteBundle(w io.Writer, projectID, location, datasetID, fhirStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores.Fhir
    
    	payload := map[string]interface{}{
    		"resourceType": "Bundle",
    		"type":         "transaction",
    		"entry": []map[string]interface{}{
    			{
    				"resource": map[string]interface{}{
    					"resourceType": "Patient",
    					"active":       true,
    				},
    				"request": map[string]interface{}{
    					"method": "POST",
    					"url":    "Patient",
    				},
    			},
    		},
    	}
    	jsonPayload, err := json.Marshal(payload)
    	if err != nil {
    		return fmt.Errorf("json.Encode: %w", err)
    	}
    
    	parent := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    
    	call := fhirService.ExecuteBundle(parent, bytes.NewReader(jsonPayload))
    	call.Header().Set("Content-Type", "application/fhir+json;charset=utf-8")
    	resp, err := call.Do()
    	if err != nil {
    		return fmt.Errorf("executeBundle: %w", err)
    	}
    	defer resp.Body.Close()
    
    	respBytes, err := io.ReadAll(resp.Body)
    	if err != nil {
    		return fmt.Errorf("could not read response: %w", err)
    	}
    
    	if resp.StatusCode > 299 {
    		return fmt.Errorf("create: status %d %s: %s", resp.StatusCode, resp.Status, respBytes)
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
    
    public class FhirStoreExecuteBundle {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStoreExecuteBundle(String fhirStoreName, String data)
          throws IOException, URISyntaxException {
        // String fhirStoreName =
        //    String.format(
        //        FHIR_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-fhir-id");
        // String data = "{\"resourceType\": \"Bundle\",\"type\": \"batch\",\"entry\": []}"
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
        HttpClient httpClient = HttpClients.createDefault();
        String baseUri = String.format("%sv1/%s/fhir", client.getRootUrl(), fhirStoreName);
        URIBuilder uriBuilder = new URIBuilder(baseUri).setParameter("access_token", getAccessToken());
        StringEntity requestEntity = new StringEntity(data);
    
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
        if (response.getStatusLine().getStatusCode() != HttpStatus.SC_OK) {
          System.err.print(
              String.format(
                  "Exception executing FHIR bundle: %s\n", response.getStatusLine().toString()));
          responseEntity.writeTo(System.err);
          throw new RuntimeException();
        }
        System.out.print("FHIR bundle executed: ");
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

A sample bundle file is available in the code sample's [GitHub repository](https://github.com/GoogleCloudPlatform/nodejs-docs-samples/blob/master/healthcare/fhir/resources/bundle.json). 
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
      headers: {'Content-Type': 'application/fhir+json'},
    });
    const fs = require('fs');
    
    async function executeFhirBundle() {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const bundleFile = 'bundle.json';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}`;
    
      const bundle = JSON.parse(fs.readFileSync(bundleFile));
    
      const request = {parent, requestBody: bundle};
      const resource =
        await healthcare.projects.locations.datasets.fhirStores.fhir.executeBundle(
          request
        );
      console.log('FHIR bundle executed');
      console.log(resource.data);
    }
    
    executeFhirBundle();

### Python

A sample bundle file is available in the code sample's [GitHub repository](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/healthcare/api-client/v1/fhir/resources/execute_bundle.json). 
    
    
    def execute_bundle(
        project_id,
        location,
        dataset_id,
        fhir_store_id,
        bundle,
    ):
        """Executes the operations in the given bundle.
    
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
        # bundle = 'bundle.json'  # replace with the bundle file
        url = f"{base_url}/projects/{project_id}/locations/{location}"
    
        resource_path = "{}/datasets/{}/fhirStores/{}/fhir".format(
            url, dataset_id, fhir_store_id
        )
    
        headers = {"Content-Type": "application/fhir+json;charset=utf-8"}
    
        with open(bundle) as bundle_file:
            bundle_file_content = bundle_file.read()
    
        response = session.post(resource_path, headers=headers, data=bundle_file_content)
        response.raise_for_status()
    
        resource = response.json()
    
        print(f"Executed bundle from file: {bundle}")
        print(json.dumps(resource, indent=2))
    
        return resource
    
    

## Make a `PATCH` request

You can use FHIR bundles to make JSON `PATCH` requests on FHIR resources. See [Executing a `PATCH` request in a FHIR bundle](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources#executing_a_patch_request_in_a_fhir_bundle) for more information.

## Resolving references to resources created in a bundle

Resources in a transaction bundle can contain references to resources that don't exist in the target system but are created during bundle execution. The Cloud Healthcare API resolves the association between the resources using the `entry.fullUrl` field. References that match the `entry.fullUrl` value of another resource in the bundle are rewritten to the ID of the corresponding resource in the store. This succeeds regardless of the ordering of the operations in the bundle.

**Note:** This functionality only applies to `transaction` bundles. In `batch` bundles with referential integrity enabled, the resources referenced when an object is created must exist in the target system. For more information, see [FHIR referential integrity](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-referential-integrity).

The Cloud Healthcare API accepts the `fullUrl` in the following formats:

  * `urn:uuid:UUID`
  * `urn:oid:OID`
  * any URL
  * a resource name in the format `RESOURCE_TYPE/RESOURCE_ID`, such as `Patient/123`. Using this format is not recommended because the `fullUrl` is a placeholder local to the bundle. This can create confusion if a resource in the store has the same name but the resource in the bundle resolves to a different name as a result of a create operation.



The following sample bundle creates a Patient resource and an Observation resource that refers to the Patient resource.
    
    
    {
      "resourceType": "Bundle",
      "type": "transaction",
      "entry":[
        {
          "request": {
            "method":"POST",
            "url":"Patient"
          },
          "fullUrl": "urn:uuid:05efabf0-4be2-4561-91ce-51548425acb9",
          "resource": {
            "resourceType":"Patient",
            "gender":"male"
          }
        },
        {
          "request": {
            "method":"POST",
            "url":"Observation"
          },
          "resource": {
            "resourceType":"Observation",
            "subject": {
              "reference": "urn:uuid:05efabf0-4be2-4561-91ce-51548425acb9"
            },
            "status":"preliminary",
            "code": {
              "text":"heart rate"
            }
          }
        }
      ]
    }
    

The following samples show how to execute a bundle.

### curl

A sample bundle file is available in the code sample's [GitHub repository](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/healthcare/api-client/v1/fhir/resources/execute_bundle.json). 

To execute a bundle, make a POST request and specify the following information:

  * The name and location of the parent dataset and FHIR store
  * The location of the Bundle file in Cloud Storage
  * An access token



The following sample shows a `POST` request using curl:
    
    
    curl -X POST \
        -H "Content-Type: application/fhir+json; charset=utf-8" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        --data @BUNDLE_FILE.json \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir"

The following sample bundle is the output from successfully executing the above example. The first entry indicates the success of the operation to create a Patient and includes the ID of the new resource. The second entry indicates the success of the operation to create the Observation and includes the ID of the new resource.
    
    
    {
      "entry": [
        {
          "response": {
            "etag": "ETAG1",
            "lastModified": "2020-08-04T16:14:14.273976+00:00",
            "location": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/REGION/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID/_history/HISTORY_ID",
            "status": "201 Created"
          }
        },
        {
          "response": {
            "etag": "ETAG",
            "lastModified": "2020-08-04T16:14:14.273976+00:00",
            "location": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/REGION/fhirStores/FHIR_STORE_ID/fhir/Observation/OBSERVATION_ID/_history/HISTORY_ID",
            "status": "201 Created"
          }
        }
      ],
      "resourceType": "Bundle",
      "type": "transaction-response"
    }
    

### PowerShell

A sample bundle file is available in the code sample's [GitHub repository](https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/healthcare/api-client/v1/fhir/resources/execute_bundle.json). 

To execute a bundle, make a POST request and specify the following information:

  * The name and location of the parent dataset and FHIR store
  * The location of the Bundle file in Cloud Storage
  * An access token



The following sample shows a `POST` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/fhir+json" `
      -InFile BUNDLE_FILE.json `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir" | ConvertTo-Json

The following sample bundle is the output from successfully executing the above example. The first entry indicates the success of the operation to create a Patient and includes the ID of the new resource. The second entry indicates the success of the operation to create the Observation and includes the ID of the new resource.
    
    
    {
      "entry": [
        {
          "response": {
            "etag": "ETAG1",
            "lastModified": "2020-08-04T16:14:14.273976+00:00",
            "location": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/REGION/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID/_history/HISTORY_ID",
            "status": "201 Created"
          }
        },
        {
          "response": {
            "etag": "ETAG",
            "lastModified": "2020-08-04T16:14:14.273976+00:00",
            "location": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/datasets/REGION/fhirStores/FHIR_STORE_ID/fhir/Observation/OBSERVATION_ID/_history/HISTORY_ID",
            "status": "201 Created"
          }
        }
      ],
      "resourceType": "Bundle",
      "type": "transaction-response"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
