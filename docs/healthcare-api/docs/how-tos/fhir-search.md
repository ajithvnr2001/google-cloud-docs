---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search/
title: Searching for FHIR resources \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:01:47.158325+00:00
---

# Searching for FHIR resources  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Searching for FHIR resources Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the basic instructions for how to search for FHIR resources in a FHIR store. Searching for FHIR resources is the primary way to query and get insights from FHIR data.

You can search for FHIR resources in the Cloud Healthcare API in the following ways:

  * Using the FHIR viewer in the Google Cloud console.
  * Using the [`projects.locations.datasets.fhirStores.fhir.search`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/search) method. The method provides the following ways of searching for FHIR resources: 
    * `GET` requests
    * `POST` requests



This page summarizes many of the commonly used search features, but is not an exhaustive list of parts of the [FHIR search specification](https://www.hl7.org/fhir/search.html) supported by the Cloud Healthcare API.

## Using the FHIR viewer

The FHIR viewer is a page in the Google Cloud console that lets you search for and [view the contents of FHIR resources](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-resources#getting_a_fhir_resource).

To search for resources in a FHIR store, complete the following steps:

  1. In the Google Cloud console, go to the **FHIR viewer** page.

[Go to the FHIR viewer](https://console.cloud.google.com/healthcare/fhirviewer)

  2. In the **FHIR Store** drop-down list, select a dataset, and then select a FHIR store in the dataset.

  3. To filter the list of resource types, search for the resource types that you want to display:

     1. Click the **Resource Type** field.

     2. In the **Properties** drop-down list that appears, select **Resource Type**.

     3. Enter a resource type.

     4. To search for another resource type, select **OR** from the **Operators** drop-down list that appears, and then enter another resource type.

  4. In the list of resource types, select the resource type that you want to search on.

  5. In the search box for the table of resources that appears, enter the value that you want to search for.




The FHIR viewer displays the search results in a table. After you select a resource, the FHIR viewer displays the contents of the resource.

When you view the contents of a resource, you can search for data inside the resource.

To search for data inside a resource, follow these steps:

  1. Select a resource.

  2. In the **FHIR viewer** pane, click the **Elements** tab.

  3. In the search box, enter the value that you want to search for.




### Downloading binary data within FHIR resources

To download the available binary data associated with a resource in the FHIR viewer, follow these steps:

  1. Select a resource.

  2. In the **FHIR viewer** pane, click the **Elements** tab.

  3. If necessary, expand the elements to access the required resource element.

  4. Click **Download File** to download the available data.




### Creating and running advanced search queries

You can use advanced search queries to search for specific FHIR resources using the [FHIR search specification](https://www.hl7.org/fhir/search.html).

To create an advanced search query, complete the following steps:

  1. On the **FHIR viewer** page, click the **Search** tab.

  2. To create a search query, click **Open query Builder**.

The **Query Selection** panel is displayed.

  3. From the **Select a FHIR resource type** list, choose the FHIR resource type you want to search for.

  4. Click **Continue**.

  5. From the **Parameter** list, select the parameter that you want to use to search for resources.

  6. From the **Modifier** list, select the modifier to apply to the query. The list only includes modifiers compatible with the data type of the selected parameter.

This is an optional selection. If no modifier is selected, then an equality check is performed.

  7. In the **Value** field, enter the value of the query parameter.

  8. To add more than one parameter value, click **OR**. This enables you to include multiple values of your resource parameter in your search query.

As you build your search query, the query is displayed on the **Query Preview** pane. To view the full URL of the search query, click **Show full path**.

  9. To add more than one parameter, click **AND**.

  10. Click **Continue**.

  11. To include resources that are referenced by the resources returned in your search query, choose the resource parameter from the **Included parameters** drop-down list.

  12. To include resources that reference the resources returned in your search query, choose the resource parameter from the **Reverse included parameters** drop-down list.

  13. Click **Done** to save your search query.

The saved search query is displayed in the **FHIR search operation** field.

  14. To search for resources with the query, click **Run Search**.

The search results are displayed in the **Search results** list. To view details of a resource returned by the search, click a resource in the list.

  15. To save the query as a query template, click **Save template** and choose **Save template** or **Save template as**. You are prompted for a name and description for the query. The query parameters are saved in a template, but any defined values are removed.




#### Example search query

The following example shows a search query that searches for Claim resources from a specific healthcare provider, Practitioner/12345, for the month of August, 2021:

  * **Parameter** : `care-team`
    * **Value** : `Practitioner/12345`
  * Operator: **AND**
  * **Parameter** : `created`
    * **Prefix** : `lt (lesser than)`
    * **Value** : `8/1/21, 12:00 AM`
  * Operator: **AND**
  * **Parameter** : `created`
    * **Prefix** : `gt (greater than)`
    * **Value** : `8/31/21, 11:59 PM`



This is configured as follows in the **Query Selection** panel and the query is previewed in the **Query Preview** pane. The query will be displayed in the **FHIR search operation** field.

**Note:** The CareTeam resource includes a reference to a Practitioner resource which is defined by including the resource type, Practitioner, before the resource's unique ID, `12345`.

![FHIR advanced search query](https://docs.cloud.google.com/static/healthcare-api/images/fhir-viewer-advanced-query.png)

#### Editing search queries

To edit a search query, do one of the following:

  * To edit the query in the query builder, click **Open Query Builder**.
  * To manually edit the query, edit the parameter values in the text box.



#### Running query templates

To run a query from a saved template, complete the following steps:

  1. Click **Saved templates**.

The **Search templates** tab of the **Query Selection** panel is displayed, showing all saved query templates.

  2. Select the query template you want to run and click **Done**.

The template's search query is displayed in the **FHIR search operation** field without any values.

  3. To define the values of your search query, edit the parameter values in the field.

  4. Click **Run Search** to search for resources with the query.




### Share FHIR resources

You can share a link to the current or historical versions of a FHIR resource.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles:

**Permissions**

  * `healthcare.fhirResources.get`



**Roles**

  * Healthcare FHIR Resource Reader (`roles/healthcare.fhirResourceReader`) 



You can ask your administrator to grant you these Identity and Access Management roles. For instructions on granting roles, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) or [Control access to Cloud Healthcare API resources](https://docs.cloud.google.com/healthcare-api/docs/controlling-access#using_cloud_iam_with_datasets). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

**Note** : If you created a Google Cloud project for this guide, then, as the project creator, you're automatically granted the Owner (`roles/owner`) IAM role, which has the permissions. You don't need to be granted any additional IAM roles. 

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

  9. In the **FHIR viewer** pane, click link **Share**. A link to share the FHIR resource is automatically copied to the clipboard.




## Using the `search` method

To search for FHIR resources with the REST API, use the [`projects.locations.datasets.fhirStores.fhir.search`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/search) method. You can call the method using `GET` or `POST` requests.

### Using the `search` method with `GET`

The following samples show how to search for resources in a given FHIR store using the [`projects.locations.datasets.fhirStores.fhir.search`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/search) method with `GET`.

### curl

To search for resources in a FHIR store, make a `GET` request and specify the following information:

  * The name of the dataset
  * The name of the FHIR store
  * The type of resource to search for
  * A query string containing the information you're searching for, as described in the Constructing a search query section
  * An access token



The following sample shows a `GET` request using `curl` to search for all patients with the last name "Smith".
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient?family:exact=Smith"

If the request is successful, the server returns the response as a FHIR `Bundle` in JSON format. The `Bundle.type` is `searchset` and the search results are entries in the `Bundle.entry` array. In this example, the request returns a single Patient resource including the data inside that resource:
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID",
          "resource": {
            "birthDate": "1970-01-01",
            "gender": "female",
            "id": "PATIENT_ID",
            "meta": {
              "lastUpdated": "LAST_UPDATED",
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
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?family%3Aexact=Smith"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
    }
    

### PowerShell

To search for resources in a FHIR store, make a `GET` request and specify the following information:

  * The name of the dataset
  * The name of the FHIR store
  * The type of resource to search for
  * A query string containing the information you're searching for, as described in the Constructing a search query section
  * An access token



The following sample shows a `GET` request using Windows PowerShell to search for all patients with the last name "Smith".
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/RESOURCE_TYPE?family:exact=Smith" | ConvertTo-Json

If the request is successful, the server returns the response as a FHIR `Bundle` in JSON format. The `Bundle.type` is `searchset` and the search results are entries in the `Bundle.entry` array. In this example, the request returns a single Patient resource including the data inside that resource:
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID",
          "resource": {
            "birthDate": "1970-01-01",
            "gender": "female",
            "id": "PATIENT_ID",
            "meta": {
              "lastUpdated": "LAST_UPDATED",
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
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?family%3Aexact=Smith"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
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
    
    

### Using the `search` method with `POST`

The following samples show how to search for resources in a given FHIR store using the [`projects.locations.datasets.fhirStores.fhir.search`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/search) method with `POST`.

### curl

To search for resources in a FHIR store, make a `POST` request and specify the following information:

  * The name of the dataset
  * The name of the FHIR store
  * The type of resource to search for
  * A query string containing the information you're searching for, as described in the Constructing a search query section
  * An access token



The following sample shows a `POST` request using `curl` to search for all patients with the last name "Smith".
    
    
    curl -X POST \
        --data "" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/fhir+json; charset=utf-8" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/_search?family:exact=Smith"

If the request is successful, the server returns the response as a FHIR `Bundle` in JSON format. The `Bundle.type` is `searchset` and the search results are entries in the `Bundle.entry` array. In this example, the request returns a single Patient resource including the data inside that resource:
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID",
          "resource": {
            "birthDate": "1970-01-01",
            "gender": "female",
            "id": "PATIENT_ID",
            "meta": {
              "lastUpdated": "LAST_UPDATED",
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
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?family%3Aexact=Smith"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
    }
    

### PowerShell

To search for resources in a FHIR store, make a `POST` request and specify the following information:

  * The name of the dataset
  * The name of the FHIR store
  * The type of resource to search for
  * A query string containing the information you're searching for, as described in the Constructing a search query section
  * An access token



The following sample shows a `POST` request using Windows PowerShell to search for all patients with the last name "Smith".
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-RestMethod `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/fhir+json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/_search?family:exact=Smith" | ConvertTo-Json

If the request is successful, the server returns the response as a FHIR `Bundle` in JSON format. The `Bundle.type` is `searchset` and the search results are entries in the `Bundle.entry` array. In this example, the request returns a single Patient resource including the data inside that resource:
    
    
    {
      "entry": [
        {
          "fullUrl": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID",
          "resource": {
            "birthDate": "1970-01-01",
            "gender": "female",
            "id": "PATIENT_ID",
            "meta": {
              "lastUpdated": "LAST_UPDATED",
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
          },
          "search": {
            "mode": "match"
          }
        }
      ],
      "link": [
        {
          "url": "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/?family%3Aexact=Smith"
        }
      ],
      "resourceType": "Bundle",
      "total": 1,
      "type": "searchset"
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
    
    public class FhirResourceSearchPost {
      private static final String FHIR_NAME =
          "projects/%s/locations/%s/datasets/%s/fhirStores/%s/fhir/%s";
      // The endpoint URL for the Healthcare API. Required for HttpClient.
      private static final String API_ENDPOINT = "https://healthcare.googleapis.com";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirResourceSearchPost(String resourceName)
          throws IOException, URISyntaxException {
        // String resourceName =
        //    String.format(
        //        FHIR_NAME, "project-id", "region-id", "dataset-id", "store-id", "resource-type");
    
        // Instantiate the client, which will be used to interact with the service.
        HttpClient httpClient = HttpClients.createDefault();
        String uri = String.format("%s/v1/%s/_search", API_ENDPOINT, resourceName);
        URIBuilder uriBuilder = new URIBuilder(uri).setParameter("access_token", getAccessToken());
        // To set additional parameters for search filtering, add them to the URIBuilder. For
        // example, to search for a Patient with the family name "Smith", specify the following:
        // uriBuilder.setParameter("family:exact", "Smith");
    
        // Set a body otherwise HttpClient complains there is no Content-Length set.
        StringEntity requestEntity = new StringEntity("");
    
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
                  "Exception searching POST FHIR resources: %s\n",
                  response.getStatusLine().toString()));
          responseEntity.writeTo(System.err);
          throw new RuntimeException();
        }
        System.out.println("FHIR resource POST search results: ");
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
    
    
    // Import google-auth-library for authentication.
    const {GoogleAuth} = require('[google-auth-library](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html)');
    
    const searchFhirResourcesPost = async () => {
      const auth = new GoogleAuth({
        scopes: 'https://www.googleapis.com/auth/cloud-platform',
      });
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const resourceType = 'Patient';
      const url = `https://healthcare.googleapis.com/v1/projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}/fhir/${resourceType}/_search`;
    
      const params = {};
      // Specify search filters in a params object. For example, to filter on a
      // Patient with the last name "Smith", set resourceType to "Patient" and
      // specify the following params:
      // params = {'family:exact' : 'Smith'};
    
      try {
        const client = await [auth](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/overview.html).[getClient](https://docs.cloud.google.com/nodejs/docs/reference/google-auth-library/latest/google-auth-library/googleauth.html)();
        const response = await client.request({
          url,
          method: 'POST',
          headers: {
            'Content-Type': 'application/fhir+json',
          },
          params,
          responseType: 'json',
        });
        const resources = response.data.entry || [];
        console.log('Resources found: ' + resources.length);
        console.log(JSON.stringify(resources, null, 2));
      } catch (error) {
        console.error(
          `Error searching ${resourceType} resources:`,
          error.response ? error.response.data : error.message
        );
      }
    };
    
    searchFhirResourcesPost();

### Python
    
    
    def search_resources_post(project_id, location, dataset_id, fhir_store_id):
        """
        Searches for resources in the given FHIR store. Uses the
        _search POST method and a query string containing the
        information to search for. In this sample, the search criteria is
        'family:exact=Smith' on a Patient resource.
    
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
        url = f"{base_url}/projects/{project_id}/locations/{location}"
    
        fhir_store_path = "{}/datasets/{}/fhirStores/{}/fhir".format(
            url, dataset_id, fhir_store_id
        )
    
        resource_path = f"{fhir_store_path}/Patient/_search?family:exact=Smith"
    
        # Sets required application/fhir+json header on the request
        headers = {"Content-Type": "application/fhir+json;charset=utf-8"}
    
        response = session.post(resource_path, headers=headers)
        response.raise_for_status()
    
        resources = response.json()
        print(
            "Using POST request, found a total of {} Patient resources:".format(
                resources["total"]
            )
        )
    
        print(json.dumps(resources, indent=2))
    
        return resources
    
    

### Constructing a search query

The query string is a series of `name=value` pairs encoded in URL form. A search combines all the pairs with a logical `AND`. Each value can be a comma-separated list of values, which are treated as a logical `OR` of those values. For example, `Patient?key1=value1&key2=value2,value3` is a search on Patient resources using the following criteria:

`(key1 = value1) AND (key2 = value2 OR key2 = value3)`

There is no syntax to perform an `OR` of two `name=value` pairs.

Each FHIR resource type defines its own search parameters in each version of FHIR. The available parameters are documented in the FHIR specification for each resource. For an example, see [FHIR R4 Patient](http://hl7.org/fhir/patient.html). You can retrieve the parameters programmatically through the [capability statement](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores.fhir/capabilities). The Cloud Healthcare API supports most search parameters; you can find exclusions through the capability statement or [FHIR conformance statement](https://docs.cloud.google.com/healthcare-api/docs/fhir).

### Pagination and sorting

The number of resources returned on each page of the FHIR search results depends on the following factors:

  * The `_count` parameter. It controls the maximum number of resources returned from the search method. For example, `_count=10` returns, at most, 10 resources matching the query. The default is 100 and the maximum value allowed is 1,000.
  * The size of the response data. A page of search results might return fewer resources than the value specified in the `_count` parameter if the size of the response is large.



If a search returns more resources than the number of resources that fits on one page, the response includes a pagination URL in the `Bundle.link` field. There might be multiple values returned in this field; the value with `Bundle.link.relation = next` indicates that you can use the corresponding `Bundle.link.url` to retrieve the next page.

The value of `Bundle.total` indicates the total number of matching resources. This value is exact if the results fit entirely in one page, but becomes a rough estimate as the number of results becomes larger than one page. You can obtain an exact total for a search that matches many results by following pagination links repeatedly until the results are exhausted.

For more information on pagination and search totals, see [Implementing pagination and search totals with FHIR search](https://docs.cloud.google.com/healthcare-api/docs/how-tos/best-practices-fhir-search).

You can sort results using the `_sort` parameter, which accepts a comma-separated list of search parameter names in priority order. You can use a `-` prefix to indicate decreasing order. For example, the following query sorts by status ascending, breaking ties by date descending, and breaking any remaining ties by category ascending:

`_sort=status,-date,category`

**Note:** A FHIR store configured to use the DSTU2 version uses a different `_sort` syntax that was present in that version of the specification. Each instance of `_sort` takes one search parameter and an optional modifier of `:asc` or `:desc`. For example, in DSTU2, to perform the same sort ordering as the previous example, use: `_sort=status&_sort:desc=date&_sort=category`.

`_sort` is only supported for search parameters of type `number`, `data`, `string`, `token`, and `quantity`. To sort using other types of search parameters (for example, `reference`), use [FHIR custom searches](https://docs.cloud.google.com/healthcare-api/docs/how-tos/\(/healthcare-api/docs/how-tos/fhir-custom-search\)) to create, for example, a `string` search parameter on the `reference` field.

### Indexing delay

FHIR resources are indexed asynchronously, so there might be a slight delay between the time a resource is created or changed, and the time when the change reflects in search results. The only exception is resource identifier data, which is indexed synchronously as a special index. As a result, searching using resource identifier is not subject to indexing delay. To use the special synchronous index, the search term for identifier should be in the pattern `identifier=[system]|[value]` or `identifier=[value]`, and any of the following search result parameters can be used:

  * `_count`
  * `_include`
  * `_revinclude`
  * `_summary`
  * `_elements`



If your query contains any other search parameters, the standard asynchronous index will be used instead. Note that searching against the special index is optimized for resolving a small number of matches. The search isn't optimized if your identifier search criteria matches a large number (i.e. more than 2,000) of resources. For a search query that will match a large number of resources, you can avoiding using the special synchronous index by including an additional `_sort` parameter in your query. Use `_sort=-_lastUpdated` if you want to keep the default sorting order.

### Searching across all resource types

Certain search parameters, shown by a leading underscore like `_id`, apply to all resource types. These all-resource parameters are listed in the FHIR specification for the [Resource type](http://hl7.org/fhir/resource.html#search).

When using these search parameters, you can perform a search across multiple resource types by omitting the resource type from the request path. For example, using `GET .../fhir?_id=1234` instead of `GET .../fhir/Patient?_id=1234` searches across all FHIR resources instead of only a Patient resource. You can use the special parameter `_type` with this type of request to limit the results to a comma-separated list of resource types. For example, the following query only returns matching results for `Observation` and `Condition` resources:

`GET .../fhir?_tag=active&_type=Observation,Condition`

### Data types

Each search parameter defined by FHIR has a data type, which includes primitive types such as the following:

  * String
  * Number
  * Date



Data types also include the following complex types:

  * Token
  * Reference
  * Quantity



Each data type has its own syntax for specifying values. Each data type supports modifiers that alter how the search is performed.

The following sections show how to use data types. For more details on additional data types, value syntaxes, and modifiers, see [Advanced FHIR search features](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir-advanced-search).

#### Number

Searches on integer or floating point values. To change the comparator, prefix the value with one of the following modifiers:

  * `ne`
  * `lt`
  * `le`
  * `gt`
  * `ge`



For example, use `[parameter]=100` for equality, or use `[parameter]=ge100` for greater than or equal to 100.

#### Date

Searches on any type of date, time, or period. The date parameter format is the following:
    
    
    yyyy-mm-ddThh:mm:ss[Z|(+|-)hh:mm]
    

The same prefix modifiers used for number apply.

#### String

Defaults to a prefix search that is insensitive to case, accents, or other diacritical marks.

**Note:** Punctuation characters split a search into multiple words, and the punctuation characters themselves are ignored.

#### Token

Searches for an exact string match of a "code". You can scope the search to the URI of a "system" indicating the value set the code is taken from using the following format:
    
    
    [parameter]=[system]|[code]
    

For example, the following search matches a code of 10738-3, but only when qualified as a value from a coding system with the specified URI:
    
    
    code=http://hl7.org/fhir/ValueSet/observation-codes|10738-3
    

#### Quantity

Searches for a numeric value using the same prefix modifiers as number. You can qualify the search with a specific system and code indicating the units of the value in following format:
    
    
    [parameter]=[prefix][number]|[system]|[code]
    

For example, the following query searches for quantity values less than 9.1 that have the specified unit system and code:
    
    
    value-quantity=lt9.1|http://unitsofmeasure.org|mg
    

#### Reference

Searches for references between resources. You can use the following queries for references to resources inside a FHIR store:

  * `[parameter]=[id]`
  * `[parameter]=[type]/[id]`



You can use `[parameter]=[url]` to specify references by URL that might be outside the FHIR store.

### Search parameter handling

By default, the search method applies "lenient" handling, which ignores parameters that the search does not recognize. The search method performs the search using any remaining parameters in the request, which might return more resources than expected.

The response includes the following:

  * A value in `Bundle.link` with a value of `Bundle.link.relation = self`
  * A `Bundle.link.url` of a URL containing only the parameters that were successfully applied to the search. You can inspect this value to determine whether any parameters were ignored.



You can set the request HTTP header to `Prefer: handling=strict` on a search request. Setting the header causes the FHIR store to return an error on any unrecognized parameter.

**Note:** Setting the FHIR store option [`defaultSearchHandlingStrict`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores#FhirStore.FIELDS.default_search_handling_strict) changes this default to `strict` for all search requests unless an individual request uses the HTTP header `Prefer: handling=lenient` to choose lenient.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
