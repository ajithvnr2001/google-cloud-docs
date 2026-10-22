---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-managing/
title: Creating and managing consent stores \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:33.920397+00:00
---

# Creating and managing consent stores  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-managing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Creating and managing consent stores Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to create and manage consent stores.

The Consent Management API is a tool for recording user consents, managing actions based on those consents, and maintaining associated documentation and records.

The organization using the Consent Management API is responsible for obtaining and maintaining the required consents necessary to permit the processing of any data through the Consent Management API.

The Consent Management API fulfills the role of a policy decision point. Policy enforcement must be implemented in the application or through a proxy. For more information, see [Attribute-based access control](https://en.wikipedia.org/wiki/Attribute-based_access_control#Architecture).

## Set up permissions

To use the features in this guide, you must have the `roles/healthcare.consentStoreAdmin` [role](https://docs.cloud.google.com/iam/docs/overview#roles). However, to perform additional useful operations with the Consent Management API, additional permissions might be required. See Access control for more details.

## Creating a consent store

Consent stores are the top-level resources that contain all information related to the configuration and operation of the Consent Management API. Consent stores belong to a Cloud Healthcare API [dataset](https://docs.cloud.google.com/healthcare-api/docs/concepts/projects-datasets-data-stores), which is assigned to a [region](https://docs.cloud.google.com/healthcare-api/docs/concepts/regions) when it is created. This region is the geographic location in which your consent store operates.

### Console

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset where you want to create a consent store.

  3. Click **Create data store**.

  4. Select **Consent** as the data store type.

  5. In the **ID** field, enter a name of your choice that's unique in your dataset. If the name is not unique, the store creation fails.

  6. Click **Next**.

  7. In **Configure your Consent Store** select one of the following options to determine when consents in your store expire:

     * **No default expiration time** means that, by default, consents do not expire.
     * **Default expiration time** means that, by default, consents expire after the number of days defined in the **Expiration time** field.
  8. To allow new consent resources to be created using [`consentStores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/patch), click **Allow consent creation on update**.

  9. Click **Next**.

  10. Click **Add label** to define optional key and value [labels](https://docs.cloud.google.com/healthcare-api/docs/how-tos/labeling-resources) to organize your Google Cloud resources.

  11. Click **Create**.




### gcloud

To create a consent store, run the [`gcloud healthcare consent-stores create`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/create) command.

Before using any of the command data below, make the following replacements: 

  * LOCATION: the dataset location
  * DATASET_ID: the consent store's parent dataset
  * CONSENT_STORE_ID: an identifier for the consent store. The consent store ID must have the following: 
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
    
    
    gcloud healthcare consent-stores create CONSENT_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores create CONSENT_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores create CONSENT_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION

You should receive a response similar to the following:

#### Response
    
    
    Created consentStore [CONSENT_STORE_ID].

### REST

To create a consent store, use the [`projects.locations.datasets.consentStores.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/create) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the consent store's parent dataset
  * CONSENT_STORE_ID: an identifier for the consent store. The consent store ID must have the following: 
    * A unique ID in its dataset
    * A Unicode string of 1-256 characters consisting of the following:
      * Numbers
      * Letters
      * Underscores
      * Dashes
      * Periods
  * DEFAULT_CONSENT_EXPIRATION_DURATION: an optional default time, specified in seconds, until consents created in this store expire. This duration must be at least 24 hours (86400 seconds) and must be in the format `DEFAULT_CONSENT_EXPIRATION_DURATIONs`.
  * ENABLE_CONSENT_CREATE_ON_UPDATE: an optional boolean that determines whether requests to patch a non-existent consent resource using [`consentStores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/patch) should create that resource. Default is `FALSE`.



Request JSON body: 
    
    
    {
      "defaultConsentTtl": "DEFAULT_CONSENT_EXPIRATION_DURATIONs",
      "enableConsentCreateOnUpdate": "ENABLE_CONSENT_CREATE_ON_UPDATE"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "defaultConsentTtl": "DEFAULT_CONSENT_EXPIRATION_DURATIONs",
      "enableConsentCreateOnUpdate": "ENABLE_CONSENT_CREATE_ON_UPDATE"
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores?consentStoreId=CONSENT_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "defaultConsentTtl": "DEFAULT_CONSENT_EXPIRATION_DURATIONs",
      "enableConsentCreateOnUpdate": "ENABLE_CONSENT_CREATE_ON_UPDATE"
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores?consentStoreId=CONSENT_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID",
      "defaultConsentTtl": "DEFAULT_CONSENT_EXPIRATION_DURATION",
      "enableConsentCreateOnUpdate": ENABLE_CONSENT_CREATE_ON_UPDATE
    }
    

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const createConsentStore = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const consentStoreId = 'my-consent-store';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
      const request = {parent, consentStoreId};
    
      await healthcare.projects.locations.datasets.consentStores.create(request);
      console.log(`Created consent store: ${consentStoreId}`);
    };
    
    createConsentStore();

### Python
    
    
    def create_consent_store(
        project_id: str, location: str, dataset_id: str, consent_store_id: str
    ):
        """Creates a new consent store within the parent dataset.
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/consent
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
        # dataset_id = 'my-dataset'  # replace with the consent store's parent dataset ID
        # consent_store_id = 'my-consent-store'  # replace with the consent store's ID
        consent_store_parent = (
            f"projects/{project_id}/locations/{location}/datasets/{dataset_id}"
        )
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .consentStores()
            .create(parent=consent_store_parent, body={}, consentStoreId=consent_store_id)
        )
    
        response = request.execute()
        print(f"Created consent store: {consent_store_id}")
        return response
    
    

## Editing a consent store

After you create a consent store, you can update it. For example, you can add or remove labels to organize your consent stores.

The following samples show how to edit a consent store.

### Console

To edit a consent store, complete the following steps: 

  1. In the Google Cloud console, go to the **Datasets** page.

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the consent store you want to edit.
  3. In the **Data stores** list, click the data store you want to edit.
  4. To edit the consent store's configuration, click the edit icon next to **Consent Store Configuration**.  
  
For more information on the consent store's configuration options, see [Creating a consent store](https://cloud.google.com/healthcare-api/docs/how-tos/consent-managing#creating_a_consent_store).
  5. To add one or more labels to the store, click  edit  **Labels** , click **Add label** , and enter the key/value label. For more information on resource labels, see [Using resource labels](https://cloud.google.com/healthcare-api/docs/how-tos/labeling-resources#adding_a_label).
  6. Click **Save**. 



### gcloud

To edit a consent store, run the [`gcloud healthcare consent-stores update`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/update) command.

Before using any of the command data below, make the following replacements: 

  * LOCATION: the dataset location
  * DATASET_ID: the consent store's parent dataset
  * CONSENT_STORE_ID: the consent store ID
  * KEY: the key in a key-value pair used to organize consent stores. See [`labels`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#ConsentStore.FIELDS.labels) for label requirements and limitations.
  * VALUE: the value in a key-value pair used to organize consent stores. See [`labels`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#ConsentStore.FIELDS.labels) for label requirements and limitations.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores update CONSENT_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION \
      --update-labels=KEY=VALUE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores update CONSENT_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION `
      --update-labels=KEY=VALUE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores update CONSENT_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION ^
      --update-labels=KEY=VALUE

You should receive a response similar to the following:

#### Response
    
    
    Updated consentStore [CONSENT_STORE_ID].
    labels:
      KEY: VALUE
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID
    

### REST

To edit a consent store, use the [`projects.locations.datasets.consentStores.patch`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/patch) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the consent store's parent dataset
  * CONSENT_STORE_ID: the consent store ID
  * KEY: the key in a key-value pair used to organize consent stores. See [`labels`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#ConsentStore.FIELDS.labels) for label requirements and limitations.
  * VALUE: the value in a key-value pair used to organize consent stores. See [`labels`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#ConsentStore.FIELDS.labels) for label requirements and limitations.



Request JSON body: 
    
    
    {
      "labels": {
        "KEY": "VALUE"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    cat > request.json << 'EOF'
    {
      "labels": {
        "KEY": "VALUE"
      }
    }
    EOF

Then execute the following command to send your REST request: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID?updateMask=labels"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`. Run the following command in the terminal to create or overwrite this file in the current directory: 
    
    
    @'
    {
      "labels": {
        "KEY": "VALUE"
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
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID?updateMask=labels" | Select-Object -Expand Content

#### APIs Explorer

Copy the request body and open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/patch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID",
      "labels": {
        "KEY": "VALUE"
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
    
    const patchConsentStore = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const consentStoreId = 'my-consent-store';
      // const defaultConsentTtl = '172800s' Must be at least 24 hours, specified
      // in seconds, appended with 's' character.
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/consentStores/${consentStoreId}`;
      const request = {
        name,
        updateMask: 'defaultConsentTtl',
        resource: {
          defaultConsentTtl: defaultConsentTtl,
        },
      };
    
      await healthcare.projects.locations.datasets.consentStores.patch(request);
      console.log(
        `Patched consent store ${consentStoreId} with default consent time-to-live ${defaultConsentTtl}`
      );
    };
    
    patchConsentStore();

### Python
    
    
    def patch_consent_store(
        project_id: str,
        location: str,
        dataset_id: str,
        consent_store_id: str,
        default_consent_ttl,
    ):
        """Updates the consent store.
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/consent
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
        # dataset_id = 'my-dataset'  # replace with the consent store's parent dataset ID
        # consent_store_id = 'my-consent-store'  # replace with the consent store's ID
        # default_consent_ttl = '172800s'  # replace with a default TTL
        consent_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        consent_store_name = "{}/consentStores/{}".format(
            consent_store_parent, consent_store_id
        )
    
        # Updates the default time-to-live (TTL) of consents in the consent store.
        # Updating the TTL does not affect the expiration time of existing consents.
        # Specify as a duration in seconds with up to nine fractional digits,
        # terminated by "s", for example "172800s".
        # Minimum value is 24 hours, or "86400s" in seconds.
        patch = {"defaultConsentTtl": default_consent_ttl}
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .consentStores()
            .patch(name=consent_store_name, updateMask="defaultConsentTtl", body=patch)
        )
    
        response = request.execute()
        print(
            "Patched consent store {} with new default consent TTL: {}".format(
                consent_store_id, default_consent_ttl
            )
        )
    
        return response
    
    

## Getting consent store details

The following samples show how to get details about a consent store.

### Console

To view a consent store's details:

  1. In the Google Cloud console, go to the **Datasets** page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the consent store you want to view.
  3. Click the name of the consent store.

The **Data store details** page displays the details of the selected a consent store.




### gcloud

To get details about a consent store, run the [`gcloud healthcare consent-stores describe`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/describe) command.

Before using any of the command data below, make the following replacements: 

  * LOCATION: the dataset location
  * DATASET_ID: the consent store's parent dataset
  * CONSENT_STORE_ID: the consent store ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores describe CONSENT_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores describe CONSENT_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores describe CONSENT_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION

If you configured any fields in the [`ConsentStore`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#resource:-consentstore) resource, they also appear in the response. 

#### Response
    
    
    name: projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID
    

### REST

To get details about a consent store, use the [`projects.locations.datasets.consentStores.get`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/get) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the consent store's parent dataset
  * CONSENT_STORE_ID: the consent store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If you configured any fields in the [`ConsentStore`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#resource-consentstore) resource, they also appear in the response. 

#### Response
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID"
    }
    

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const getConsentStore = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const consentStoreId = 'my-consent-store';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/consentStores/${consentStoreId}`;
      const request = {name};
    
      const consentStore =
        await healthcare.projects.locations.datasets.consentStores.get(request);
      console.log(consentStore.data);
    };
    
    getConsentStore();

### Python
    
    
    def get_consent_store(
        project_id: str, location: str, dataset_id: str, consent_store_id: str
    ):
        """Gets the specified consent store.
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/consent
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
        # dataset_id = 'my-dataset'  # replace with the consent store's parent dataset ID
        # consent_store_id = 'my-consent-store'  # replace with the consent store's ID
        consent_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        consent_store_name = "{}/consentStores/{}".format(
            consent_store_parent, consent_store_id
        )
    
        consent_stores = client.projects().locations().datasets().consentStores()
        consent_store = consent_stores.get(name=consent_store_name).execute()
    
        print(json.dumps(consent_store, indent=2))
        return consent_store
    
    

## Listing the consent stores in a dataset

The following samples show how to list the consent stores in a dataset.

### Console

To view the data stores in a dataset: 

  1. In the Google Cloud console, go to the **Datasets** page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the data store you want to view. 



### gcloud

To list the consent stores in a dataset, run the [`gcloud healthcare consent-stores list`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/list) command.

Before using any of the command data below, make the following replacements: 

  * DATASET_ID: the consent store's parent dataset
  * LOCATION: the dataset location



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores list --dataset=DATASET_ID \
      --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores list --dataset=DATASET_ID `
      --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores list --dataset=DATASET_ID ^
      --location=LOCATION

If you configured any fields in the [`ConsentStore`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#resource:-consentstore) resource, they also appear in the response. 
    
    
    ID               LABELS  LOCATION
    CONSENT_STORE_ID           LOCATION
    

### REST

To list the consent stores in a dataset, use the [`projects.locations.datasets.consentStores.list`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/list) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * DATASET_ID: the consent store's parent dataset
  * LOCATION: the dataset location



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

If you configured any fields in the [`ConsentStore`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores#resource-consentstore) resource, they also appear in the response. 

#### Response
    
    
    {
      "consentStores": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID"
        },
        {
          ...
        }
      ]
    }
    

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const listConsentStores = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      const parent = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
      const request = {parent};
    
      const consentStores =
        await healthcare.projects.locations.datasets.consentStores.list(request);
      console.log(JSON.stringify(consentStores.data));
    };
    
    listConsentStores();

### Python
    
    
    def list_consent_stores(project_id, location, dataset_id):
        """Lists the consent stores in the given dataset.
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/consent
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
        # dataset_id = 'my-dataset'  # replace with the consent store's parent dataset ID
        consent_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
    
        consent_stores = (
            client.projects()
            .locations()
            .datasets()
            .consentStores()
            .list(parent=consent_store_parent)
            .execute()
            .get("consentStores", [])
        )
    
        for consent_store in consent_stores:
            print(consent_store)
    
        return consent_stores
    
    

## Deleting a consent store

**Caution:** Deleting a consent store also deletes the resources in the consent store. If deleted, these resources cannot be recovered.

The following samples show how to delete a consent store.

### Console

To delete a data store: 

  1. In the Google Cloud console, go to the **Datasets** page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset containing the data store you want to delete.
  3. Choose **Delete** from the **Actions** drop-down list for the data store that you want to delete. 
  4. To confirm, type the data store name and then click **Delete**. 



### gcloud

To delete a consent store, run the [`gcloud healthcare consent-stores delete`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/delete) command.

Before using any of the command data below, make the following replacements: 

  * LOCATION: the dataset location
  * DATASET_ID: the consent store's parent dataset
  * CONSENT_STORE_ID: the consent store ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores delete CONSENT_STORE_ID \
      --dataset=DATASET_ID \
      --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores delete CONSENT_STORE_ID `
      --dataset=DATASET_ID `
      --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud healthcare consent-stores delete CONSENT_STORE_ID ^
      --dataset=DATASET_ID ^
      --location=LOCATION

To confirm, type **Y**. You should receive a response similar to the following. 
    
    
    Deleted consentStore [CONSENT_STORE_ID].
    

### REST

To delete a consent store, use the [`projects.locations.datasets.consentStores.delete`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/delete) method.

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the ID of your Google Cloud project
  * LOCATION: the dataset location
  * DATASET_ID: the consent store's parent dataset
  * CONSENT_STORE_ID: the consent store ID



To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID" | Select-Object -Expand Content

#### APIs Explorer

Open the [method reference page](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/delete). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:

#### Response
    
    
    {}

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const deleteConsentStore = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const consentStoreId = 'my-consent-store';
      const name = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/consentStores/${consentStoreId}`;
      const request = {name};
    
      await healthcare.projects.locations.datasets.consentStores.delete(request);
      console.log(`Deleted consent store: ${consentStoreId}`);
    };
    
    deleteConsentStore();

### Python
    
    
    def delete_consent_store(
        project_id: str, location: str, dataset_id: str, consent_store_id: str
    ):
        """Deletes the specified consent store.
        See https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/consent
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
        # dataset_id = 'my-dataset'  # replace with the consent store's parent dataset ID
        # consent_store_id = 'my-consent-store'  # replace with the consent store's ID
        consent_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        consent_store_name = "{}/consentStores/{}".format(
            consent_store_parent, consent_store_id
        )
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .consentStores()
            .delete(name=consent_store_name)
        )
    
        response = request.execute()
        print(f"Deleted consent store: {consent_store_id}")
        return response
    
    

## Audit logging

The Consent Management API writes the following types of audit logs:

  * Admin Activity: record operations that modify the configuration or metadata of a resource. You can't disable Admin Activity audit logs.
  * Data Access: contain API calls that read the configuration or metadata of resources, as well as external API calls that create, modify, or read customer-provided resource data. These logs must be enabled. For example, Data Access audit logs can be used to log what service made an [access determination request](https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-access-determination), what information was provided in that request, and how the API responded to that request. For more information on Data Access audit logs, see [Configuring Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access). For more information about audit logging in the Cloud Healthcare API, visit [Viewing Cloud Audit Logs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/audit-logging).



For more information on audit logs for the Consent Management API, see [Viewing Cloud Audit Logs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/audit-logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
