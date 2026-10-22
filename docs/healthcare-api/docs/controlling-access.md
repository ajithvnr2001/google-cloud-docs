---
url: https://docs.cloud.google.com/healthcare-api/docs/controlling-access/
title: Controlling access to Cloud Healthcare API resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:30:45.281023+00:00
---

# Controlling access to Cloud Healthcare API resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/controlling-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Controlling access to Cloud Healthcare API resources Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to control access to Cloud Healthcare API datasets and data stores using [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) permissions. IAM lets you control who has access to your datasets and data stores. To learn more about IAM for the Cloud Healthcare API, see [Access control](https://docs.cloud.google.com/healthcare-api/docs/access-control).

## Overview of IAM policies

Access to a resource is managed through an IAM _policy_. A policy contains an array, called `bindings`. This array contains a collection of _bindings_ , which are associations between principals, such as a user account or service account, and a role. Policies are represented using JSON or YAML.

The following sample policy shows `user-1@example.com` that has been granted the `roles/healthcare.datasetAdmin` role and `user-2@example.com` and `service-account-13@appspot.gserviceaccount.com` have been granted the `roles/healthcare.datasetViewer` role:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.datasetAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.datasetViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }

To update a policy for a resource, use the [read-modify-write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#overview_of_cloud_iam_policy) pattern. There are no separate methods for creating, modifying, and revoking user access.

To update a policy, complete the following steps:

  1. Read the current policy by calling the resource's `getIamPolicy()` method. For example, to read a dataset's current policy, call [`projects.locations.datasets.getIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/getIamPolicy).
  2. Edit the returned policy, either by using a text editor or programmatically, to add or remove any applicable principals and their role grants.
  3. Write the updated policy by calling the resource's `setIamPolicy()` method. For example, to write a dataset's updated policy, call [`projects.locations.datasets.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/setIamPolicy).



## Using IAM with consent stores

The following sections show how to get, modify, and set a policy for a consent store. These sections use the following sample policy as a starting point:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.consentStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.consentReader",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }

### Getting a policy

The following samples show how to read a consent store-level IAM policy. For more information, see [`projects.locations.datasets.consentStores.getIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/getIamPolicy).

### Console

To view the IAM policy for a consent store: 

  1. In the Google Cloud console, go to the Datasets page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the ID of the dataset that contains the consent store and then select the consent store that you want to get a policy for.
  3. Click **Show info panel**. 
  4. To view the principals assigned to a role, expand the role. 



### gcloud

To view the IAM policy for a consent store, run the [`gcloud healthcare consent-stores get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/get-iam-policy) command. Specify the consent store name, the dataset name, and the location.
    
    
    gcloud healthcare consent-stores get-iam-policy CONSENT_STORE_ID \
        --dataset=DATASET_ID \
        --location=LOCATION

If the request is successful, the bindings are displayed.
    
    
    bindings:
    - members:
      - user:user-1@example.com
      role: roles/healthcare.consentStoreAdmin
      - serviceAccount:service-account-13@appspot.gserviceaccount.com
      - user:user-2@example.com
      role: roles/healthcare.consentReader
    etag: bytes
    version: VERSION_NUMBER
    

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const getConsentStoreIamPolicy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const consentStoreId = 'my-consent-store';
      const resource_ = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/consentStores/${consentStoreId}`;
      const request = {resource_};
    
      const consentStore =
        await healthcare.projects.locations.datasets.consentStores.getIamPolicy(
          request
        );
      console.log(
        'Got consent store IAM policy:',
        JSON.stringify(consentStore.data, null, 2)
      );
    };
    
    getConsentStoreIamPolicy();

### Python
    
    
    def get_consent_store_iam_policy(
        project_id: str, location: str, dataset_id: str, consent_store_id: str
    ):
        """Gets the IAM policy for the specified consent store.
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
            .getIamPolicy(resource=consent_store_name)
        )
        response = request.execute()
    
        print("etag: {}".format(response.get("name")))
        return response
    
    

### curl

To read the IAM policy for a consent store, make a `GET` request and specify the name of the dataset, the name of the consent store, and an access token.

The following sample shows a `GET` request using `curl`:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID:getIamPolicy"

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.consentStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.consentReader",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }
    

### PowerShell

To read the IAM policy for a consent store, make a `GET` request and specify the name of the dataset, the name of the consent store, and an access token.

The following sample shows a `GET` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID:getIamPolicy" | Select-Object -Expand Content

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.consentStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.consentReader",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }
    

### Modifying a policy

The following samples grant a new user the `roles/healthcare.consentReader` role. For more information, see [`projects.locations.datasets.consentStores.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/setIamPolicy).

### Setting a policy

### Console

To set a consent store-level IAM policy, complete the following steps:

  1. In the Google Cloud console, go to the Datasets page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the ID of the dataset that contains the consent store and then select the consent store that you want to set a policy for.
  3. Click **Show info panel**.
  4. Click **Add principal**. 
  5. In the **New principals** field, enter one or more identities that need access to the consent store.
  6. In the **Select a role** list, under **Cloud Healthcare** , select the permission that you want to grant. For example, Healthcare Consent Store Viewer.
  7. Click **Save**.



### gcloud

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.consentReader` binding:
    
    
    {
      "role":"roles/healthcare.consentReader",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, run the appropriate `set-iam-policy` command to make the changes. To set a consent store-level policy, run the [`gcloud healthcare consent-stores set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/consent-stores/set-iam-policy) command. Specify the consent store name, the dataset name, the location, and the path to the policy file that you created.
    
    
    gcloud healthcare consent-stores set-iam-policy CONSENT_STORE_ID \
        --dataset=DATASET_ID \
        --location=LOCATION \
        POLICY_FILE_NAME

If the request is successful, the consent store name and the bindings are displayed.
    
    
    Updated IAM policy for consentStore [CONSENT_STORE_ID].
    bindings:
    - members:
      - user:user-1@example.com
      role: roles/healthcare.consentStoreAdmin
      - serviceAccount:service-account-13@appspot.gserviceaccount.com
      - user:user-2@example.com
      - user:NEW_USER_EMAIL_ADDRESS
      role: roles/healthcare.consentReader
    etag: bytes
    version: VERSION_NUMBER
    

### Node.js
    
    
    const google = require('@googleapis/healthcare');
    const healthcare = google.healthcare({
      version: 'v1',
      auth: new google.auth.GoogleAuth({
        scopes: ['https://www.googleapis.com/auth/cloud-platform'],
      }),
    });
    
    const setConsentStoreIamPolicy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const consentStoreId = 'my-consent-store';
      // const member = 'user:example@gmail.com';
      // const role = 'roles/healthcare.consentStoreViewer';
      const resource_ = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/consentStores/${consentStoreId}`;
      const request = {
        resource_,
        resource: {
          policy: {
            bindings: [
              {
                members: member,
                role: role,
              },
            ],
          },
        },
      };
    
      const consentStore =
        await healthcare.projects.locations.datasets.consentStores.setIamPolicy(
          request
        );
      console.log(
        'Set consent store IAM policy:',
        JSON.stringify(consentStore.data, null, 2)
      );
    };
    
    setConsentStoreIamPolicy();

### Python
    
    
    def set_consent_store_iam_policy(
        project_id: str,
        location: str,
        dataset_id: str,
        consent_store_id: str,
        member,
        role,
        etag=None,
    ):
        """Sets the IAM policy for the specified consent store.
        A single member will be assigned a single role. A member can be any of:
        - allUsers, that is, anyone
        - allAuthenticatedUsers, anyone authenticated with a Google account
        - user:email, as in 'user:somebody@example.com'
        - group:email, as in 'group:admins@example.com'
        - domain:domainname, as in 'domain:example.com'
        - serviceAccount:email,
            as in 'serviceAccount:my-other-app@appspot.gserviceaccount.com'
        A role can be any IAM role, such as 'roles/viewer', 'roles/owner',
        or 'roles/editor'
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
        # member = 'myemail@example.com'  # replace with an authorized member
        # role = 'roles/viewer'  # replace with a Healthcare API IAM role
        consent_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        consent_store_name = "{}/consentStores/{}".format(
            consent_store_parent, consent_store_id
        )
    
        policy = {"bindings": [{"role": role, "members": [member]}]}
    
        if etag is not None:
            policy["etag"] = etag
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .consentStores()
            .setIamPolicy(resource=consent_store_name, body={"policy": policy})
        )
        response = request.execute()
    
        print("etag: {}".format(response.get("name")))
        print("bindings: {}".format(response.get("bindings")))
        return response
    
    

### curl

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.consentReader` binding:
    
    
    {
      "role":"roles/healthcare.consentReader",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, call [`projects.locations.datasets.consentStores.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/setIamPolicy) to make the updates.

To set a consent store-level IAM policy, make a `POST` request and specify the name of the dataset, the name of the consent store, the policy, and an access token.

The following sample shows a `POST` request using `curl` to grant a new user the existing `roles/healthcare.consentReader` role:

The policy can be written directly in the request, as shown here, or it can be passed in as a JSON or YAML file. For examples of how to format a policy as JSON or YAML, see [`Policy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Policy). 
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'policy': {
            'bindings': [
              {
                'role':'roles/healthcare.consentStoreAdmin',
                'members': [
                  'user:user-1@example.com'
                ]
              },
              {
                'role':'roles/healthcare.consentReader',
                'members': [
                  'serviceAccount:service-account-13@appspot.gserviceaccount.com',
                  'user:user-2@example.com',
                  'user:NEW_USER_EMAIL_ADDRESS'
                ]
              }
            ]
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID:setIamPolicy"

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.consentStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.consentReader",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com",
            "user:NEW_USER_EMAIL_ADDRESS"
          ]
        }
      ]
    }
    

### PowerShell

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.consentReader` binding:
    
    
    {
      "role":"roles/healthcare.consentReader",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, call [`projects.locations.datasets.consentStores.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/setIamPolicy) to make the updates.

To set a consent store-level IAM policy, make a `POST` request and specify the name of the dataset, the name of the consent store, the policy, and an access token.

The following sample shows a `POST` request using Windows PowerShell to grant a new user the existing `roles/healthcare.consentReader` role:

The policy can be written directly in the request, as shown here, or it can be passed in as a JSON or YAML file. For examples of how to format a policy as JSON or YAML, see [`Policy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Policy). 
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'policy': {
          'bindings': [
            {
              'role': 'roles/healthcare.consentStoreAdmin',
              'members': [
                'user:user-1@example.com',
              ]
            },
            {
              'role': 'roles/healthcare.consentReader',
              'members': [
                'serviceAccount:service-account-13@appspot.gserviceaccount.com',
                'user:user-2@example.com',
                'user:NEW_USER_EMAIL_ADDRESS'
              ]
            }
          ]
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID:setIamPolicy" | Select-Object -Expand Content

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.consentStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.consentReader",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com",
            "user:NEW_USER_EMAIL_ADDRESS"
          ]
        }
      ]
    }
    

## Using IAM with datasets

The following sections show how to get, modify, and set a policy for a dataset. These sections use the following sample policy as a starting point:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.datasetAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.datasetViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }

### Getting a policy

The following samples show how to read a dataset-level IAM policy. For more information, see [`projects.locations.datasets.getIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/getIamPolicy).

### curl

To read the IAM policy for a dataset, make a `GET` request and specify the name of the dataset and an access token.

The following sample shows a `GET` request using `curl`:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID:getIamPolicy"

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.datasetAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.datasetViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }
    

### PowerShell

To view the IAM policy for a dataset, make a `GET` request and specify the name of the dataset and an access token.

The following sample shows a `GET` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID:getIamPolicy" | Select-Object -Expand Content

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.datasetAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.datasetViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }
    

### Console

To view the IAM policy for a dataset: 

  1. In the Google Cloud console, go to the Datasets page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select a dataset and then click **Show info panel**. 
  3. To view the principals assigned to a role, expand the role. 



### gcloud

To view the IAM policy for a dataset, run the [`gcloud healthcare datasets get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/datasets/get-iam-policy) command. Specify the dataset name and the location.
    
    
    gcloud healthcare datasets get-iam-policy DATASET_ID \
        --location=LOCATION

If the request is successful, the bindings are displayed.
    
    
    bindings:
    - members:
      - serviceAccount:service-account-13@appspot.gserviceaccount.com
      - user:user-2@example.com
      role: roles/healthcare.datasetViewer
    etag: bytes
    version: VERSION_NUMBER
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // datasetIAMPolicy gets the dataset's IAM policy.
    func datasetIAMPolicy(w io.Writer, projectID, location, datasetID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	datasetsService := healthcareService.Projects.Locations.Datasets
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s", projectID, location, datasetID)
    
    	policy, err := datasetsService.GetIamPolicy(name).Do()
    	if err != nil {
    		return fmt.Errorf("GetIamPolicy: %w", err)
    	}
    
    	fmt.Fprintf(w, "IAM Policy etag: %v\n", policy.Etag)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.Policy;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class DatasetGetIamPolicy {
      private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void datasetGetIamPolicy(String datasetName) throws IOException {
        // String datasetName =
        //     String.format(DATASET_NAME, "your-project-id", "your-region-id", "your-dataset-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Datasets.GetIamPolicy request =
            client.projects().locations().datasets().getIamPolicy(datasetName);
    
        // Execute the request and process the results.
        Policy policy = request.execute();
        System.out.println("Dataset IAMPolicy retrieved: \n" + policy.toPrettyString());
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
    
    const getDatasetIamPolicy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      const resource_ = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
      const request = {resource_};
    
      const dataset =
        await healthcare.projects.locations.datasets.getIamPolicy(request);
      console.log(
        'Got dataset IAM policy:',
        JSON.stringify(dataset.data, null, 2)
      );
    };
    
    getDatasetIamPolicy();

### Python
    
    
    # Imports the Dict and Any types for runtime type hints.
    from typing import Any, Dict
    
    
    def get_dataset_iam_policy(
        project_id: str, location: str, dataset_id: str
    ) -> Dict[str, Any]:
        """Gets the IAM policy for the specified dataset.
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/datasets
        before running the sample.
        See https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.html#getIamPolicy
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Google Cloud project you want
              to use.
          location: The name of the dataset's location.
          dataset_id: The ID of the dataset containing the IAM policy to get.
    
        Returns:
          A dictionary representing an IAM policy.
        """
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
        dataset_name = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
    
        request = (
            client.projects().locations().datasets().getIamPolicy(resource=dataset_name)
        )
    
        try:
            response = request.execute()
            print("etag: {}".format(response.get("name")))
            return response
        except HttpError as err:
            raise err
    
    

### Modifying a policy

The following samples grant a new user the `roles/healthcare.datasetViewer` role:

### Setting a policy

### Console

To set a dataset-level IAM policy, complete the following steps:

  1. In the Google Cloud console, go to the Datasets page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Select the dataset that you want to set a policy for and then click **Show info panel**.
  3. Click **Add principal**.
  4. In the **New principals** field, enter one or more identities that need access to the dataset.
  5. In the **Select a role** list, under **Cloud Healthcare** , select the permission that you want to grant. For example, Healthcare Dataset Viewer.
  6. Click **Save**.



### gcloud

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.datasetViewer` binding:
    
    
    {
      "role":"roles/healthcare.datasetViewer",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, run the appropriate `set-iam-policy` command to make the changes. To set a dataset-level policy, run the [`gcloud healthcare datasets set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/datasets/set-iam-policy) command. Specify the dataset name, the location, and the path to the policy file that you created.
    
    
    gcloud healthcare datasets set-iam-policy DATASET_ID \
        --location=LOCATION \
        POLICY_FILE_NAME

If the request is successful, the dataset name and the bindings are displayed.
    
    
    Updated IAM policy for dataset [DATASET_ID].
    bindings:
    - members:
      - serviceAccount:service-account-13@appspot.gserviceaccount.com
      - user:user-2@example.com
      role: roles/healthcare.datasetAdmin
      - user:user-1@example.com
      - user:NEW_USER_EMAIL_ADDRESS
      role: roles/healthcare.datasetViewer
    etag: bytes
    version: VERSION_NUMBER
    

### curl

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.datasetViewer` binding:
    
    
    {
      "role":"roles/healthcare.datasetViewer",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, call [`projects.locations.datasets.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/setIamPolicy) to make the updates.

To set a dataset-level IAM policy, make a `POST` request and specify the name of the dataset, the policy, and an access token.

The following sample shows a `POST` request using `curl` to grant a new user the existing `roles/healthcare.datasetViewer` role:

The policy can be written directly in the request, as shown here, or it can be passed in as a JSON or YAML file. For examples of how to format a policy as JSON or YAML, see [`Policy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Policy). 
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'policy': {
            'bindings': [
              {
                'role':'roles/healthcare.datasetAdmin',
                'members': [
                  'user:user-1@example.com'
                ]
              },
              {
                'role':'roles/healthcare.datasetViewer',
                'members': [
                  'serviceAccount:service-account-13@appspot.gserviceaccount.com',
                  'user:user-2@example.com',
                  'user:NEW_USER_EMAIL_ADDRESS'
                ]
              }
            ]
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID:setIamPolicy"

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.datasetAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.datasetViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com",
            "user:NEW_USER_EMAIL_ADDRESS"
          ]
        }
      ]
    }
    

### PowerShell

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.datasetViewer` binding:
    
    
    {
      "role":"roles/healthcare.datasetViewer",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, call [`projects.locations.datasets.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets/setIamPolicy) to make the updates.

To set a dataset-level IAM policy, make a `POST` request and specify the name of the dataset, the policy, and an access token.

The following sample shows a `POST` request using Windows PowerShell to grant a new user the existing `roles/healthcare.datasetViewer` role:

The policy can be written directly in the request, as shown here, or it can be passed in as a JSON or YAML file. For examples of how to format a policy as JSON or YAML, see [`Policy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Policy). 
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'policy': {
          'bindings': [
            {
              'role': 'roles/healthcare.datasetAdmin',
              'members': [
                'user:user-1@example.com'
              ]
            },
            {
              'role': 'roles/healthcare.datasetViewer',
              'members': [
                'serviceAccount:service-account-13@appspot.gserviceaccount.com',
                'user:user-2@example.com',
                'user:NEW_USER_EMAIL_ADDRESS'
              ]
            }
          ]
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID:setIamPolicy" | Select-Object -Expand Content

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.datasetAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.datasetViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com",
            "user:NEW_USER_EMAIL_ADDRESS"
          ]
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
    
    // setDatasetIAMPolicy sets an IAM policy for the dataset.
    func setDatasetIAMPolicy(w io.Writer, projectID, location, datasetID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	datasetsService := healthcareService.Projects.Locations.Datasets
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s", projectID, location, datasetID)
    
    	policy, err := datasetsService.GetIamPolicy(name).Do()
    	if err != nil {
    		return fmt.Errorf("GetIamPolicy: %w", err)
    	}
    
    	policy.Bindings = append(policy.Bindings, &healthcare.Binding{
    		Members: []string{"user:example@example.com"},
    		Role:    "roles/viewer",
    	})
    
    	req := &healthcare.SetIamPolicyRequest{
    		Policy: policy,
    	}
    
    	policy, err = datasetsService.SetIamPolicy(name, req).Do()
    	if err != nil {
    		return fmt.Errorf("SetIamPolicy: %w", err)
    	}
    
    	fmt.Fprintf(w, "IAM Policy etag: %v", policy.Etag)
    	return nil
    }
    

### Java
    
    
    import com.google.api.client.http.[HttpRequestInitializer](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.HttpRequestInitializer.html);
    import com.google.api.client.http.javanet.[NetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.http.javanet.NetHttpTransport.html);
    import com.google.api.client.json.[JsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.JsonFactory.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.healthcare.v1.CloudHealthcare;
    import com.google.api.services.healthcare.v1.CloudHealthcare.Projects.Locations.Datasets;
    import com.google.api.services.healthcare.v1.CloudHealthcareScopes;
    import com.google.api.services.healthcare.v1.model.Binding;
    import com.google.api.services.healthcare.v1.model.Policy;
    import com.google.api.services.healthcare.v1.model.SetIamPolicyRequest;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.Collections;
    
    public class DatasetSetIamPolicy {
      private static final String DATASET_NAME = "projects/%s/locations/%s/datasets/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void datasetSetIamPolicy(String datasetName) throws IOException {
        // String datasetName =
        //     String.format(DATASET_NAME, "your-project-id", "your-region-id", "your-dataset-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure the IAMPolicy to apply to the dataset.
        // For more information on understanding IAM roles, see the following:
        // https://cloud.google.com/iam/docs/understanding-roles
        Binding binding =
            new Binding()
                .setRole("roles/healthcare.datasetViewer")
                .setMembers(Arrays.asList("domain:google.com"));
        Policy policy = new Policy().setBindings(Arrays.asList(binding));
        SetIamPolicyRequest policyRequest = new SetIamPolicyRequest().setPolicy(policy);
    
        // Create request and configure any parameters.
        Datasets.SetIamPolicy request =
            client.projects().locations().datasets().setIamPolicy(datasetName, policyRequest);
    
        // Execute the request and process the results.
        Policy updatedPolicy = request.execute();
        System.out.println("Dataset policy has been updated: " + updatedPolicy.toPrettyString());
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
    
    const setDatasetIamPolicy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const member = 'user:example@gmail.com';
      // const role = 'roles/healthcare.datasetViewer';
      const resource_ = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}`;
      const request = {
        resource_,
        resource: {
          policy: {
            bindings: [
              {
                members: member,
                role: role,
              },
            ],
          },
        },
      };
    
      const dataset =
        await healthcare.projects.locations.datasets.setIamPolicy(request);
      console.log(
        'Set dataset IAM policy:',
        JSON.stringify(dataset.data, null, 2)
      );
    };
    
    setDatasetIamPolicy();

### Python
    
    
    # Imports the Dict and Any types for runtime type hints.
    from typing import Any, Dict
    
    def set_dataset_iam_policy(
        project_id: str,
        location: str,
        dataset_id: str,
        member: str,
        role: str,
        etag: str = None,
    ) -> Dict[str, Any]:
        """Sets the IAM policy for the specified dataset.
    
            A single member will be assigned a single role. A member can be any of:
    
            - allUsers, that is, anyone
            - allAuthenticatedUsers, anyone authenticated with a Google account
            - user:email, as in 'user:somebody@example.com'
            - group:email, as in 'group:admins@example.com'
            - domain:domainname, as in 'domain:example.com'
            - serviceAccount:email,
                as in 'serviceAccount:my-other-app@appspot.gserviceaccount.com'
    
            A role can be any IAM role, such as 'roles/viewer', 'roles/owner',
            or 'roles/editor'
    
        See
        https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/healthcare/api-client/v1/datasets
        before running the sample.
        See https://googleapis.github.io/google-api-python-client/docs/dyn/healthcare_v1.projects.locations.datasets.html#setIamPolicy
        for the Python API reference.
    
        Args:
          project_id: The project ID or project number of the Google Cloud project you want
              to use.
          location: The name of the dataset's location.
          dataset_id: The ID of the dataset containing the IAM policy to set.
          member: The principals to grant access for a Google Cloud resource.
          role: The role to assign to the list of 'members'.
          etag: The 'etag' returned in a previous getIamPolicy request to ensure that
            setIamPolicy changes apply to the same policy version.
    
        Returns:
          A dictionary representing an IAM policy.
        """
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
        dataset_name = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
    
        # TODO(developer): Uncomment these lines and replace with your values.
        # role = 'roles/viewer'
        # member = 'serviceAccount:group@example.com'
        policy = {"bindings": [{"role": role, "members": [member]}]}
    
        if etag is not None:
            policy["etag"] = etag
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .setIamPolicy(resource=dataset_name, body={"policy": policy})
        )
        try:
            response = request.execute()
            print("etag: {}".format(response.get("name")))
            print("bindings: {}".format(response.get("bindings")))
            return response
        except HttpError as err:
            raise err
    
    

## Using IAM with DICOM stores

The following sections show how to get, modify, and set a policy for a DICOM store. These sections use the following sample policy as a starting point:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.dicomStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.dicomViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }

### Getting a policy

The following samples show how to read a DICOM store-level IAM policy. For more information, see [`projects.locations.datasets.dicomStores.getIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/getIamPolicy).

### Console

To view the IAM policy for a DICOM store: 

  1. In the Google Cloud console, go to the Datasets page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the ID of the dataset that contains the DICOM store and then select the DICOM store that you want to get a policy for.
  3. Click **Show info panel**. 
  4. To view the principals assigned to a role, expand the role. 



### gcloud

To view the IAM policy for a DICOM store, run the [`gcloud healthcare dicom-stores get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/get-iam-policy) command. Specify the DICOM store name, the dataset name, and the location.
    
    
    gcloud healthcare dicom-stores get-iam-policy DICOM_STORE_ID \
        --dataset=DATASET_ID \
        --location=LOCATION

If the request is successful, the bindings are displayed.
    
    
    bindings:
    - members:
      - user:user-1@example.com
      role: roles/healthcare.dicomStoreAdmin
      - serviceAccount:service-account-13@appspot.gserviceaccount.com
      - user:user-2@example.com
      role: roles/healthcare.dicomViewer
    etag: bytes
    version: VERSION_NUMBER
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // getDICOMIAMPolicy gets the DICOM store's IAM policy.
    func getDICOMIAMPolicy(w io.Writer, projectID, location, datasetID, dicomStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	dicomService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	policy, err := dicomService.GetIamPolicy(name).Do()
    	if err != nil {
    		return fmt.Errorf("GetIamPolicy: %w", err)
    	}
    
    	fmt.Fprintf(w, "IAM Policy etag: %v\n", policy.Etag)
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
    import com.google.api.services.healthcare.v1.model.Policy;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class DicomStoreGetIamPolicy {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomStoreGetIamPolicy(String dicomStoreName) throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        DicomStores.GetIamPolicy request =
            client.projects().locations().datasets().dicomStores().getIamPolicy(dicomStoreName);
    
        // Execute the request and process the results.
        Policy policy = request.execute();
        System.out.println("DICOM store IAMPolicy retrieved: \n" + policy.toPrettyString());
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
    
    const getDicomStoreIamPolicy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      const resource_ = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const request = {resource_};
    
      const dicomStore =
        await healthcare.projects.locations.datasets.dicomStores.getIamPolicy(
          request
        );
      console.log(
        'Got DICOM store IAM policy:',
        JSON.stringify(dicomStore.data, null, 2)
      );
    };
    
    getDicomStoreIamPolicy();

### Python
    
    
    def get_dicom_store_iam_policy(project_id, location, dataset_id, dicom_store_id):
        """Gets the IAM policy for the specified DICOM store.
    
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
            .getIamPolicy(resource=dicom_store_name)
        )
        response = request.execute()
    
        print("etag: {}".format(response.get("name")))
        return response
    
    

### curl

To read the IAM policy for a DICOM store, make a `GET` request and specify the name of the dataset, the name of the DICOM store, and an access token.

The following sample shows a `GET` request using `curl`:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:getIamPolicy"

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.dicomStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.dicomViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }
    

### PowerShell

To read the IAM policy for a DICOM store, make a `GET` request and specify the name of the dataset, the name of the DICOM store, and an access token.

The following sample shows a `GET` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:getIamPolicy" | Select-Object -Expand Content

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.dicomStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.dicomViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }
    

### Modifying a policy

The following samples grant a new user the `roles/healthcare.dicomViewer` role. For more information, see [`projects.locations.datasets.dicomStores.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/setIamPolicy).

### Setting a policy

### Console

To set a DICOM store-level IAM policy, complete the following steps:

  1. In the Google Cloud console, go to the Datasets page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the ID of the dataset that contains the DICOM store and then select the DICOM store that you want to set a policy for.
  3. Click **Show info panel**.
  4. Click **Add principal**. 
  5. In the **New principals** field, enter one or more identities that need access to the DICOM store.
  6. In the **Select a role** list, under **Cloud Healthcare** , select the permission that you want to grant. For example, Healthcare DICOM Store Viewer.
  7. Click **Save**.



### gcloud

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.dicomViewer` binding:
    
    
    {
      "role":"roles/healthcare.dicomViewer",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, run the appropriate `set-iam-policy` command to make the changes. To set a DICOM store-level policy, run the [`gcloud healthcare dicom-stores set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/dicom-stores/set-iam-policy) command. Specify the DICOM store name, the dataset name, the location, and the path to the policy file that you created.
    
    
    gcloud healthcare dicom-stores set-iam-policy DICOM_STORE_ID \
        --dataset=DATASET_ID \
        --location=LOCATION \
        POLICY_FILE_NAME

If the request is successful, the DICOM store name and the bindings are displayed.
    
    
    Updated IAM policy for dicomStore [DICOM_STORE_ID].
    bindings:
    - members:
      - user:user-1@example.com
      role: roles/healthcare.dicomStoreAdmin
      - serviceAccount:service-account-13@appspot.gserviceaccount.com
      - user:user-2@example.com
      - user:NEW_USER_EMAIL_ADDRESS
      role: roles/healthcare.dicomViewer
    etag: bytes
    version: VERSION_NUMBER
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // setDICOMIAMPolicy sets the DICOM store's IAM policy.
    func setDICOMIAMPolicy(w io.Writer, projectID, location, datasetID, dicomStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	dicomService := healthcareService.Projects.Locations.Datasets.DicomStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/dicomStores/%s", projectID, location, datasetID, dicomStoreID)
    
    	policy, err := dicomService.GetIamPolicy(name).Do()
    	if err != nil {
    		return fmt.Errorf("GetIamPolicy: %w", err)
    	}
    
    	policy.Bindings = append(policy.Bindings, &healthcare.Binding{
    		Members: []string{"user:example@example.com"},
    		Role:    "roles/viewer",
    	})
    
    	req := &healthcare.SetIamPolicyRequest{
    		Policy: policy,
    	}
    
    	policy, err = dicomService.SetIamPolicy(name, req).Do()
    	if err != nil {
    		return fmt.Errorf("SetIamPolicy: %w", err)
    	}
    
    	fmt.Fprintf(w, "IAM Policy etag: %v\n", policy.Etag)
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
    import com.google.api.services.healthcare.v1.model.Binding;
    import com.google.api.services.healthcare.v1.model.Policy;
    import com.google.api.services.healthcare.v1.model.SetIamPolicyRequest;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.Collections;
    
    public class DicomStoreSetIamPolicy {
      private static final String DICOM_NAME = "projects/%s/locations/%s/datasets/%s/dicomStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void dicomStoreSetIamPolicy(String dicomStoreName) throws IOException {
        // String dicomStoreName =
        //    String.format(
        //        DICOM_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-dicom-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure the IAMPolicy to apply to the store.
        // For more information on understanding IAM roles, see the following:
        // https://cloud.google.com/iam/docs/understanding-roles
        Binding binding =
            new Binding()
                .setRole("roles/healthcare.dicomStoreAdmin")
                .setMembers(Arrays.asList("domain:google.com"));
        Policy policy = new Policy().setBindings(Arrays.asList(binding));
        SetIamPolicyRequest policyRequest = new SetIamPolicyRequest().setPolicy(policy);
    
        // Create request and configure any parameters.
        DicomStores.SetIamPolicy request =
            client
                .projects()
                .locations()
                .datasets()
                .dicomStores()
                .setIamPolicy(dicomStoreName, policyRequest);
    
        // Execute the request and process the results.
        Policy updatedPolicy = request.execute();
        System.out.println("DICOM policy has been updated: " + updatedPolicy.toPrettyString());
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
    
    const setDicomStoreIamPolicy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      // const member = 'user:example@gmail.com';
      // const role = 'roles/healthcare.dicomStoreViewer';
      const resource_ = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/dicomStores/${dicomStoreId}`;
      const request = {
        resource_,
        resource: {
          policy: {
            bindings: [
              {
                members: member,
                role: role,
              },
            ],
          },
        },
      };
    
      const dicomStore =
        await healthcare.projects.locations.datasets.dicomStores.setIamPolicy(
          request
        );
      console.log(
        'Set DICOM store IAM policy:',
        JSON.stringify(dicomStore.data, null, 2)
      );
    };
    
    setDicomStoreIamPolicy();

### Python
    
    
    def set_dicom_store_iam_policy(
        project_id, location, dataset_id, dicom_store_id, member, role, etag=None
    ):
        """Sets the IAM policy for the specified DICOM store.
    
        A single member will be assigned a single role. A member can be any of:
    
        - allUsers, that is, anyone
        - allAuthenticatedUsers, anyone authenticated with a Google account
        - user:email, as in 'user:somebody@example.com'
        - group:email, as in 'group:admins@example.com'
        - domain:domainname, as in 'domain:example.com'
        - serviceAccount:email,
            as in 'serviceAccount:my-other-app@appspot.gserviceaccount.com'
    
        A role can be any IAM role, such as 'roles/viewer', 'roles/owner',
        or 'roles/editor'
    
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
        # member = 'myemail@example.com'  # replace with an authorized member
        # role = 'roles/viewer'  # replace with a Healthcare API IAM role
        dicom_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        dicom_store_name = f"{dicom_store_parent}/dicomStores/{dicom_store_id}"
    
        policy = {"bindings": [{"role": role, "members": [member]}]}
    
        if etag is not None:
            policy["etag"] = etag
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .dicomStores()
            .setIamPolicy(resource=dicom_store_name, body={"policy": policy})
        )
        response = request.execute()
    
        print("etag: {}".format(response.get("name")))
        print("bindings: {}".format(response.get("bindings")))
        return response
    
    

### curl

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.dicomViewer` binding:
    
    
    {
      "role":"roles/healthcare.dicomViewer",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, call [`projects.locations.datasets.dicomStores.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/setIamPolicy) to make the updates.

To set a DICOM store-level IAM policy, make a `POST` request and specify the name of the dataset, the name of the DICOM store, the policy, and an access token.

The following sample shows a `POST` request using `curl` to grant a new user the existing `roles/healthcare.dicomViewer` role:

The policy can be written directly in the request, as shown here, or it can be passed in as a JSON or YAML file. For examples of how to format a policy as JSON or YAML, see [`Policy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Policy). 
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'policy': {
            'bindings': [
              {
                'role':'roles/healthcare.dicomStoreAdmin',
                'members': [
                  'user:user-1@example.com'
                ]
              },
              {
                'role':'roles/healthcare.dicomViewer',
                'members': [
                  'serviceAccount:service-account-13@appspot.gserviceaccount.com',
                  'user:user-2@example.com',
                  'user:NEW_USER_EMAIL_ADDRESS'
                ]
              }
            ]
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:setIamPolicy"

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.dicomStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.dicomViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com",
            "user:NEW_USER_EMAIL_ADDRESS"
          ]
        }
      ]
    }
    

### PowerShell

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.dicomViewer` binding:
    
    
    {
      "role":"roles/healthcare.dicomViewer",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, call [`projects.locations.datasets.dicomStores.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.dicomStores/setIamPolicy) to make the updates.

To set a DICOM store-level IAM policy, make a `POST` request and specify the name of the dataset, the name of the DICOM store, the policy, and an access token.

The following sample shows a `POST` request using Windows PowerShell to grant a new user the existing `roles/healthcare.dicomViewer` role:

The policy can be written directly in the request, as shown here, or it can be passed in as a JSON or YAML file. For examples of how to format a policy as JSON or YAML, see [`Policy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Policy). 
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'policy': {
          'bindings': [
            {
              'role': 'roles/healthcare.dicomStoreAdmin',
              'members': [
                'user:user-1@example.com',
              ]
            },
            {
              'role': 'roles/healthcare.dicomViewer',
              'members': [
                'serviceAccount:service-account-13@appspot.gserviceaccount.com',
                'user:user-2@example.com',
                'user:NEW_USER_EMAIL_ADDRESS'
              ]
            }
          ]
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/dicomStores/DICOM_STORE_ID:setIamPolicy" | Select-Object -Expand Content

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.dicomStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.dicomViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com",
            "user:NEW_USER_EMAIL_ADDRESS"
          ]
        }
      ]
    }
    

## Using IAM with FHIR stores

The following sections show how to get, modify, and set a policy for a FHIR store. These sections use the following sample policy as a starting point:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.fhirStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.fhirResourceReader",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }

### Getting a policy

The following samples show how to read a FHIR store-level IAM policy. For more information, see [`projects.locations.datasets.fhirStores.getIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/getIamPolicy).

### Console

To view the IAM policy for a FHIR store: 

  1. In the Google Cloud console, go to the Datasets page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the ID of the dataset that contains the FHIR store and then select the FHIR store that you want to get a policy for.
  3. Click **Show info panel**. 
  4. To view the principals assigned to a role, expand the role. 



### gcloud

To view the IAM policy for a FHIR store, run the [`gcloud healthcare fhir-stores get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/get-iam-policy) command. Specify FHIR store name, the dataset name, and the location.
    
    
    gcloud healthcare fhir-stores get-iam-policy FHIR_STORE_ID \
        --dataset=DATASET_ID \
        --location=LOCATION

If the request is successful, the bindings are displayed.
    
    
    bindings:
    - members:
      - user:user-1@example.com
      role: roles/healthcare.fhirStoreAdmin
      - serviceAccount:service-account-13@appspot.gserviceaccount.com
      - user:user-2@example.com
      role: roles/healthcare.fhirResourceReader
    etag: bytes
    version: VERSION_NUMBER
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // getFHIRIAMPolicy gets the FHIR store's IAM policy.
    func getFHIRIAMPolicy(w io.Writer, projectID, location, datasetID, fhirStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    
    	policy, err := fhirService.GetIamPolicy(name).Do()
    	if err != nil {
    		return fmt.Errorf("GetIamPolicy: %w", err)
    	}
    
    	fmt.Fprintf(w, "IAM Policy etag: %v\n", policy.Etag)
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
    import com.google.api.services.healthcare.v1.model.Policy;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class FhirStoreGetIamPolicy {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStoreGetIamPolicy(String fhirStoreName) throws IOException {
        // String fhirStoreName =
        //    String.format(
        //        FHIR_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-fhir-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        FhirStores.GetIamPolicy request =
            client.projects().locations().datasets().fhirStores().getIamPolicy(fhirStoreName);
    
        // Execute the request and process the results.
        Policy policy = request.execute();
        System.out.println("FHIR store IAMPolicy retrieved: \n" + policy.toPrettyString());
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
    
    const getFhirStoreIamPolicy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      const resource_ = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}`;
      const request = {resource_};
    
      try {
        const fhirStore =
          await healthcare.projects.locations.datasets.fhirStores.getIamPolicy(
            request
          );
        console.log(
          'Got FHIR store IAM policy:',
          JSON.stringify(fhirStore.data, null, 2)
        );
      } catch (error) {
        console.error(
          'Error getting FHIR store IAM policy:',
          error.message || error
        );
      }
    };
    
    getFhirStoreIamPolicy();

### Python
    
    
    def get_fhir_store_iam_policy(project_id, location, dataset_id, fhir_store_id):
        """Gets the IAM policy for the specified FHIR store.
    
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
        fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .getIamPolicy(resource=fhir_store_name)
        )
        response = request.execute()
    
        print("etag: {}".format(response.get("name")))
        return response
    
    

### curl

To read the IAM policy for a FHIR store, make a `POST` request and specify the name of the dataset, the name of the FHIR store, and an access token.

The following sample shows a `POST` request using `curl`:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:getIamPolicy"

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.fhirStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.fhirResourceReader",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }
    

### PowerShell

To read the IAM policy for a FHIR store, make a `POST` request and specify the name of the dataset, the name of the FHIR store, and an access token.

The following sample shows a `POST` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:getIamPolicy" | Select-Object -Expand Content

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.fhirStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.fhirResourceReader",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }
    

### Modifying a policy

The following samples grant a new user the `roles/healthcare.fhirResourceReader` role. For more information, see [`projects.locations.datasets.fhirStores.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/setIamPolicy).

### Setting a policy

### Console

To set a FHIR store-level IAM policy, complete the following steps:

  1. In the Google Cloud console, go to the Datasets page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the ID of the dataset that contains the FHIR store and then select the FHIR store that you want to set a policy for. 
  3. Click **Show info panel**.
  4. Click **Add principal**.
  5. In the **New principals** field, enter one or more identities that need access to the FHIR store.
  6. In the **Select a role** list, under **Cloud Healthcare** , select the permission that you want to grant. For example, Healthcare FHIR Resource Reader.
  7. Click **Save**.



### gcloud

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.fhirResourceReader` binding:
    
    
    {
      "role":"roles/healthcare.fhirResourceReader",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, run the appropriate `set-iam-policy` command to make the changes. To set a FHIR store-level policy, run the [`gcloud healthcare fhir-stores set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/fhir-stores/set-iam-policy) command. Specify the FHIR store name, the dataset name, the location, and the path to the policy file that you created.
    
    
    gcloud healthcare fhir-stores set-iam-policy FHIR_STORE_ID \
        --dataset=DATASET_ID \
        --location=LOCATION \
        POLICY_FILE_NAME

If the request is successful, the FHIR store name and the bindings are displayed.
    
    
    Updated IAM policy for fhirStore [FHIR_STORE_ID].
    bindings:
    - members:
      - serviceAccount:service-account-13@appspot.gserviceaccount.com
      - user:user-2@example.com
      - user:NEW_USER_EMAIL_ADDRESS
      role: roles/healthcare.fhirResourceReader
    etag: bytes
    version: VERSION_NUMBER
    

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	healthcare "google.golang.org/api/healthcare/v1"
    )
    
    // setFHIRIAMPolicy sets the FHIR store's IAM policy.
    func setFHIRIAMPolicy(w io.Writer, projectID, location, datasetID, fhirStoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	fhirService := healthcareService.Projects.Locations.Datasets.FhirStores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/fhirStores/%s", projectID, location, datasetID, fhirStoreID)
    
    	policy, err := fhirService.GetIamPolicy(name).Do()
    	if err != nil {
    		return fmt.Errorf("GetIamPolicy: %w", err)
    	}
    
    	policy.Bindings = append(policy.Bindings, &healthcare.Binding{
    		Members: []string{"user:example@example.com"},
    		Role:    "roles/viewer",
    	})
    
    	req := &healthcare.SetIamPolicyRequest{
    		Policy: policy,
    	}
    
    	policy, err = fhirService.SetIamPolicy(name, req).Do()
    	if err != nil {
    		return fmt.Errorf("SetIamPolicy: %w", err)
    	}
    
    	fmt.Fprintf(w, "IAM Policy version: %v\n", policy.Version)
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
    import com.google.api.services.healthcare.v1.model.Binding;
    import com.google.api.services.healthcare.v1.model.Policy;
    import com.google.api.services.healthcare.v1.model.SetIamPolicyRequest;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.Collections;
    
    public class FhirStoreSetIamPolicy {
      private static final String FHIR_NAME = "projects/%s/locations/%s/datasets/%s/fhirStores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void fhirStoreSetIamPolicy(String fhirStoreName) throws IOException {
        // String fhirStoreName =
        //    String.format(
        //        FHIR_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-fhir-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure the IAMPolicy to apply to the store.
        // For more information on understanding IAM roles, see the following:
        // https://cloud.google.com/iam/docs/understanding-roles
        Binding binding =
            new Binding()
                .setRole("roles/healthcare.fhirResourceReader")
                .setMembers(Arrays.asList("domain:google.com"));
        Policy policy = new Policy().setBindings(Arrays.asList(binding));
        SetIamPolicyRequest policyRequest = new SetIamPolicyRequest().setPolicy(policy);
    
        // Create request and configure any parameters.
        FhirStores.SetIamPolicy request =
            client
                .projects()
                .locations()
                .datasets()
                .fhirStores()
                .setIamPolicy(fhirStoreName, policyRequest);
    
        // Execute the request and process the results.
        Policy updatedPolicy = request.execute();
        System.out.println("FHIR policy has been updated: " + updatedPolicy.toPrettyString());
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
    
    const setFhirStoreIamPolicy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const fhirStoreId = 'my-fhir-store';
      // const member = 'user:example@gmail.com';
      // const role = 'roles/healthcare.fhirStoreViewer';
      const resource_ = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/fhirStores/${fhirStoreId}`;
      const request = {
        resource_,
        resource: {
          policy: {
            bindings: [
              {
                members: [member],
                role: role,
              },
            ],
          },
        },
      };
    
      const fhirStore =
        await healthcare.projects.locations.datasets.fhirStores.setIamPolicy(
          request
        );
      console.log(
        'Set FHIR store IAM policy:',
        JSON.stringify(fhirStore.data, null, 2)
      );
    };
    
    setFhirStoreIamPolicy();

### Python
    
    
    def set_fhir_store_iam_policy(
        project_id,
        location,
        dataset_id,
        fhir_store_id,
        member,
        role,
        etag=None,
    ):
        """Sets the IAM policy for the specified FHIR store.
            A single member will be assigned a single role. A member can be any of:
            - allUsers, that is, anyone
            - allAuthenticatedUsers, anyone authenticated with a Google account
            - user:email, as in 'user:somebody@example.com'
            - group:email, as in 'group:admins@example.com'
            - domain:domainname, as in 'domain:example.com'
            - serviceAccount:email,
                as in 'serviceAccount:my-other-app@appspot.gserviceaccount.com'
            A role can be any IAM role, such as 'roles/viewer', 'roles/owner',
            or 'roles/editor'
    
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
        # member = 'myemail@example.com'  # replace with an authorized member
        # role = 'roles/viewer'  # replace with a Healthcare API IAM role
        fhir_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        fhir_store_name = f"{fhir_store_parent}/fhirStores/{fhir_store_id}"
    
        policy = {"bindings": [{"role": role, "members": [member]}]}
    
        if etag is not None:
            policy["etag"] = etag
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .fhirStores()
            .setIamPolicy(resource=fhir_store_name, body={"policy": policy})
        )
        response = request.execute()
    
        print("etag: {}".format(response.get("name")))
        print("bindings: {}".format(response.get("bindings")))
        return response
    
    

### curl

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.fhirResourceReader` binding:
    
    
    {
      "role":"roles/healthcare.fhirResourceReader",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, call [`projects.locations.datasets.fhirStores.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/setIamPolicy) to make the updates.

To set a FHIR store-level IAM policy, make a `POST` request and specify the name of the dataset, the name of the FHIR store, the policy, and an access token.

The following sample shows a `POST` request using `curl` to grant a new user the existing `roles/healthcare.fhirResourceReader` role:

The policy can be written directly in the request, as shown here, or it can be passed in as a JSON or YAML file. For examples of how to format a policy as JSON or YAML, see [`Policy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Policy). 
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'policy': {
            'bindings': [
              {
                'role':'roles/healthcare.fhirStoreAdmin',
                'members': [
                  'user:user-1@example.com'
                ]
              },
              {
                'role':'roles/healthcare.fhirResourceReader',
                'members': [
                  'serviceAccount:service-account-13@appspot.gserviceaccount.com',
                  'user:user-2@example.com',
                  'user:NEW_USER_EMAIL_ADDRESS'
                ]
              }
            ]
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:setIamPolicy"

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.fhirStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.fhirResourceViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com",
            "user:NEW_USER_EMAIL_ADDRESS"
          ]
        }
      ]
    }
    

### PowerShell

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.fhirResourceReader` binding:
    
    
    {
      "role":"roles/healthcare.fhirResourceReader",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, call [`projects.locations.datasets.fhirStores.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.fhirStores/setIamPolicy) to make the updates.

To set a FHIR store-level IAM policy, make a `POST` request and specify the name of the dataset, the name of the FHIR store, the policy, and an access token.

The following sample shows a `POST` request using Windows PowerShell to grant a new user the existing `roles/healthcare.fhirResourceReader` role:

The policy can be written directly in the request, as shown here, or it can be passed in as a JSON or YAML file. For examples of how to format a policy as JSON or YAML, see [`Policy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Policy). 
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'policy': {
          'bindings': [
            {
              'role': 'roles/healthcare.fhirStoreAdmin',
              'members': [
                'user:user-1@example.com',
              ]
            },
            {
              'role': 'roles/healthcare.fhirResourceReader',
              'members': [
                'serviceAccount:service-account-13@appspot.gserviceaccount.com',
                'user:user-2@example.com',
                'user:NEW_USER_EMAIL_ADDRESS'
              ]
            }
          ]
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID:setIamPolicy" | Select-Object -Expand Content

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.fhirStoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.fhirResourceViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com",
            "user:NEW_USER_EMAIL_ADDRESS"
          ]
        }
      ]
    }
    

## Using IAM with HL7v2 stores

The following sections show how to get, modify, and set a policy for an HL7v2 store. These sections use the following sample policy as a starting point:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.hl7V2StoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.hl7V2Consumer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }

### Getting a policy

The following samples show how to read an HL7v2 store-level IAM policy. For more information, see [`projects.locations.datasets.hl7V2Stores.getIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/getIamPolicy).

### Console

To view the IAM policy for an HL7v2 store: 

  1. In the Google Cloud console, go to the Datasets page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the ID of the dataset that contains the HL7v2 store and then select the HL7v2 store that you want to get a policy for.
  3. Click **Show info panel**. 
  4. To view the principals assigned to a role, expand the role. 



### gcloud

To view the IAM policy for an HL7v2 store, run the [`hl7v2-stores get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/get-iam-policy) command. Specify the HL7v2 store name, the dataset name, and the location.
    
    
    gcloud healthcare hl7v2-stores get-iam-policy HL7V2_STORE_ID \
        --dataset=DATASET_ID \
        --location=LOCATION

If the request is successful, the bindings are displayed.
    
    
    bindings:
    - members:
      - user:user-1@example.com
      role: roles/healthcare.hl7v2StoreAdmin
      - serviceAccount:service-account-13@appspot.gserviceaccount.com
      - user:user-2@example.com
      role: roles/healthcare.hl7v2Consumer
    etag: bytes
    version: VERSION_NUMBER
    

### curl

To read the IAM policy for an HL7v2 store, make a `GET` request and specify the name of the dataset, the name of the HL7v2 store, and an access token.

The following sample shows a `GET` request using `curl`:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:getIamPolicy"

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.hl7V2StoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.hl7V2Consumer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
        }
      ]
    }
    

### PowerShell

To read the IAM policy for an HL7v2 store, make a `GET` request and specify the name of the dataset, the name of the HL7v2 store, and an access token.

The following sample shows a `GET` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:getIamPolicy" | Select-Object -Expand Content

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.hl7V2StoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.hl7V2Consumer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com"
          ]
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
    
    // hl7V2IAMPolicy gets the IAM policy.
    func hl7V2IAMPolicy(w io.Writer, projectID, location, datasetID, hl7V2StoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s", projectID, location, datasetID, hl7V2StoreID)
    
    	policy, err := storesService.GetIamPolicy(name).Do()
    	if err != nil {
    		return fmt.Errorf("GetIamPolicy: %w", err)
    	}
    
    	fmt.Fprintf(w, "IAM policy etag: %q\n", policy.Etag)
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
    import com.google.api.services.healthcare.v1.model.Policy;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Collections;
    
    public class Hl7v2StoreGetIamPolicy {
      private static final String HL7v2_NAME = "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2StoreGetIamPolicy(String hl7v2StoreName) throws IOException {
        // String hl7v2StoreName =
        //    String.format(
        //        HL7v2_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-hl7v2-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Create request and configure any parameters.
        Hl7V2Stores.GetIamPolicy request =
            client.projects().locations().datasets().hl7V2Stores().getIamPolicy(hl7v2StoreName);
    
        // Execute the request and process the results.
        Policy policy = request.execute();
        System.out.println("HL7v2 store IAMPolicy retrieved: \n" + policy.toPrettyString());
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
    
    const getHl7v2StoreIamPolicy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const hl7v2StoreId = 'my-hl7v2-store';
      const resource_ = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}`;
      const request = {resource_};
    
      const hl7v2Store =
        await healthcare.projects.locations.datasets.hl7V2Stores.getIamPolicy(
          request
        );
      console.log(
        'Got HL7v2 store IAM policy:',
        JSON.stringify(hl7v2Store.data, null, 2)
      );
    };
    
    getHl7v2StoreIamPolicy();

### Python
    
    
    def get_hl7v2_store_iam_policy(project_id, location, dataset_id, hl7v2_store_id):
        """Gets the IAM policy for the specified HL7v2 store.
    
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
            .getIamPolicy(resource=hl7v2_store_name)
        )
        response = request.execute()
    
        print("etag: {}".format(response.get("name")))
        return response
    
    

### Modifying a policy

The following samples grant a new user the `roles/healthcare.hl7V2Consumer` role. For more information, see [`projects.locations.datasets.hl7V2Stores.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/setIamPolicy).

### Setting a policy

### Console

To set an HL7v2 store-level IAM policy, complete the following steps:

  1. In the Google Cloud console, go to the Datasets page. 

[Go to Datasets](https://console.cloud.google.com/healthcare/browser)

  2. Click the ID of the dataset that contains the HL7v2 store and then select the HL7v2 store that you want to set a policy for.
  3. Click **Show info panel**.
  4. Click **Add principal**. 
  5. In the **New principals** field, enter one or more identities that need access to the HL7v2 store.
  6. In the **Select a role** list, under **Cloud Healthcare** , select the permission that you want to grant. For example, Healthcare HL7v2 Message Consumer.
  7. Click **Save**.



### gcloud

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.hl7V2Consumer` binding:
    
    
    {
      "role":"roles/healthcare.hl7V2Consumer",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, run the appropriate `set-iam-policy` command to make the changes. To set an HL7v2 store-level policy, run the [`gcloud healthcare hl7v2-stores set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/healthcare/hl7v2-stores/set-iam-policy) command. Specify the HL7v2 store name, the dataset name, the location, and the path to the policy file that you created.
    
    
    gcloud healthcare hl7v2-stores set-iam-policy HL7V2_STORE_ID \
        --dataset=DATASET_ID \
        --location=LOCATION \
        POLICY_FILE_NAME

If the request is successful, the HL7v2 store name and the bindings are displayed.
    
    
    Updated IAM policy for hl7v2Store [HL7V2_STORE_ID].
    bindings:
    - members:
      - user:user-1@example.com
      role: roles/healthcare.hl7v2StoreAdmin
      - serviceAccount:service-account-13@appspot.gserviceaccount.com
      - user:user-2@example.com
      - user:NEW_USER_EMAIL_ADDRESS
      role: roles/healthcare.hl7v2Consumer
    etag: bytes
    version: VERSION_NUMBER
    

### curl

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.hl7V2Consumer` binding:
    
    
    {
      "role":"roles/healthcare.hl7V2Consumer",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, call [`projects.locations.datasets.hl7V2Stores.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/setIamPolicy) to make the updates.

To set an HL7v2 store-level IAM policy, make a `POST` request and specify the name of the dataset, the name of the HL7v2 store, the policy, and an access token.

The following sample shows a `POST` request using `curl` to grant a new user the existing `roles/healthcare.hl7V2Consumer` role.

The policy can be written directly in the request, as shown here, or it can be passed in as a JSON or YAML file. For examples of how to format a policy as JSON or YAML, see [`Policy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Policy). 
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'policy': {
            'bindings': [
              {
                'role':'roles/healthcare.hl7V2StoreAdmin',
                'members': [
                  'user:user-1@example.com'
                ]
              },
              {
                'role':'roles/healthcare.hl7V2Consumer',
                'members': [
                  'serviceAccount:service-account-13@appspot.gserviceaccount.com',
                  'user:user-2@example.com',
                  'user:NEW_USER_EMAIL_ADDRESS'
                ]
              }
            ]
          }
        }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:setIamPolicy"

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.hl7V2StoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.hl7V2Consumer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com",
            "user:NEW_USER_EMAIL_ADDRESS"
          ]
        }
      ]
    }
    

### PowerShell

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new user the role, append their email address to the `members` array under the `roles/healthcare.hl7V2Consumer` binding:
    
    
    {
      "role":"roles/healthcare.hl7V2Consumer",
      "members": [
        "serviceAccount:service-account-13@appspot.gserviceaccount.com",
        "user:user-2@example.com",
        "user:NEW_USER_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, call [`projects.locations.datasets.hl7V2Stores.setIamPolicy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores/setIamPolicy) to make the updates.

To set an HL7v2 store-level IAM policy, make a `POST` request and specify the name of the dataset, the name of the HL7v2 store, the policy, and an access token.

The following sample shows a `POST` request using `curl` to grant a new user the existing `roles/healthcare.hl7V2Consumer` role:

The policy can be written directly in the request, as shown here, or it can be passed in as a JSON or YAML file. For examples of how to format a policy as JSON or YAML, see [`Policy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Policy). 
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'policy': {
          'bindings': [
            {
              'role': 'roles/healthcare.hl7V2StoreAdmin',
              'members': [
                'user:user-1@example.com',
              ]
            },
            {
              'role': 'roles/healthcare.hl7V2Consumer',
              'members': [
                'serviceAccount:service-account-13@appspot.gserviceaccount.com',
                'user:user-2@example.com',
                'user:NEW_USER_EMAIL_ADDRESS'
              ]
            }
          ]
        }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID:setIamPolicy" | Select-Object -Expand Content

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.hl7V2StoreAdmin",
          "members": [
            "user:user-1@example.com"
          ]
        },
        {
          "role":"roles/healthcare.hl7V2Consumer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "user:user-2@example.com",
            "user:NEW_USER_EMAIL_ADDRESS"
          ]
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
    
    // setHL7V2IAMPolicy sets an IAM policy.
    func setHL7V2IAMPolicy(w io.Writer, projectID, location, datasetID, hl7V2StoreID string) error {
    	ctx := context.Background()
    
    	healthcareService, err := healthcare.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("healthcare.NewService: %w", err)
    	}
    
    	storesService := healthcareService.Projects.Locations.Datasets.Hl7V2Stores
    
    	name := fmt.Sprintf("projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s", projectID, location, datasetID, hl7V2StoreID)
    
    	policy, err := storesService.GetIamPolicy(name).Do()
    	if err != nil {
    		return fmt.Errorf("GetIamPolicy: %w", err)
    	}
    
    	policy.Bindings = append(policy.Bindings, &healthcare.Binding{
    		Members: []string{"user:example@example.com"},
    		Role:    "roles/viewer",
    	})
    
    	req := &healthcare.SetIamPolicyRequest{
    		Policy: policy,
    	}
    
    	policy, err = storesService.SetIamPolicy(name, req).Do()
    	if err != nil {
    		return fmt.Errorf("SetIamPolicy: %w", err)
    	}
    
    	fmt.Fprintf(w, "Sucessfully set IAM Policy.\n")
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
    import com.google.api.services.healthcare.v1.model.Binding;
    import com.google.api.services.healthcare.v1.model.Policy;
    import com.google.api.services.healthcare.v1.model.SetIamPolicyRequest;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.Collections;
    
    public class Hl7v2StoreSetIamPolicy {
      private static final String HL7v2_NAME = "projects/%s/locations/%s/datasets/%s/hl7V2Stores/%s";
      private static final JsonFactory JSON_FACTORY = new GsonFactory();
      private static final NetHttpTransport HTTP_TRANSPORT = new NetHttpTransport();
    
      public static void hl7v2StoreSetIamPolicy(String hl7v2StoreName) throws IOException {
        // String hl7v2StoreName =
        //    String.format(
        //        HL7v2_NAME, "your-project-id", "your-region-id", "your-dataset-id", "your-hl7v2-id");
    
        // Initialize the client, which will be used to interact with the service.
        CloudHealthcare client = createClient();
    
        // Configure the IAMPolicy to apply to the store.
        // For more information on understanding IAM roles, see the following:
        // https://cloud.google.com/iam/docs/understanding-roles
        Binding binding =
            new Binding()
                .setRole("roles/healthcare.hl7V2Consumer")
                .setMembers(Arrays.asList("domain:google.com"));
        Policy policy = new Policy().setBindings(Arrays.asList(binding));
        SetIamPolicyRequest policyRequest = new SetIamPolicyRequest().setPolicy(policy);
    
        // Create request and configure any parameters.
        Hl7V2Stores.SetIamPolicy request =
            client
                .projects()
                .locations()
                .datasets()
                .hl7V2Stores()
                .setIamPolicy(hl7v2StoreName, policyRequest);
    
        // Execute the request and process the results.
        Policy updatedPolicy = request.execute();
        System.out.println("HL7v2 policy has been updated: " + updatedPolicy.toPrettyString());
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
    
    const setHl7v2StoreIamPolicy = async () => {
      // TODO(developer): uncomment these lines before running the sample
      // const cloudRegion = 'us-central1';
      // const projectId = 'adjective-noun-123';
      // const datasetId = 'my-dataset';
      // const dicomStoreId = 'my-dicom-store';
      // const member = 'user:example@gmail.com';
      // const role = 'roles/healthcare.hl7V2StoreViewer';
      const resource_ = `projects/${projectId}/locations/${cloudRegion}/datasets/${datasetId}/hl7V2Stores/${hl7v2StoreId}`;
      const request = {
        resource_,
        resource: {
          policy: {
            bindings: [
              {
                members: member,
                role: role,
              },
            ],
          },
        },
      };
    
      const hl7v2Store =
        await healthcare.projects.locations.datasets.hl7V2Stores.setIamPolicy(
          request
        );
      console.log(
        'Set HL7v2 store IAM policy:',
        JSON.stringify(hl7v2Store.data, null, 2)
      );
    };
    
    setHl7v2StoreIamPolicy();

### Python
    
    
    def set_hl7v2_store_iam_policy(
        project_id, location, dataset_id, hl7v2_store_id, member, role, etag=None
    ):
        """Sets the IAM policy for the specified HL7v2 store.
            A single member will be assigned a single role. A member can be any of:
            - allUsers, that is, anyone
            - allAuthenticatedUsers, anyone authenticated with a Google account
            - user:email, as in 'user:somebody@example.com'
            - group:email, as in 'group:admins@example.com'
            - domain:domainname, as in 'domain:example.com'
            - serviceAccount:email,
                as in 'serviceAccount:my-other-app@appspot.gserviceaccount.com'
            A role can be any IAM role, such as 'roles/viewer', 'roles/owner',
            or 'roles/editor'.
    
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
        # member = 'myemail@example.com'  # replace with an authorized member
        # role = 'roles/viewer'  # replace with a Healthcare API IAM role
        hl7v2_store_parent = "projects/{}/locations/{}/datasets/{}".format(
            project_id, location, dataset_id
        )
        hl7v2_store_name = f"{hl7v2_store_parent}/hl7V2Stores/{hl7v2_store_id}"
    
        policy = {"bindings": [{"role": role, "members": [member]}]}
    
        if etag is not None:
            policy["etag"] = etag
    
        request = (
            client.projects()
            .locations()
            .datasets()
            .hl7V2Stores()
            .setIamPolicy(resource=hl7v2_store_name, body={"policy": policy})
        )
        response = request.execute()
    
        print("etag: {}".format(response.get("name")))
        print("bindings: {}".format(response.get("bindings")))
        return response
    
    

## Using IAM with the Healthcare Natural Language API

The following sections show how to get, modify, and set a policy for the Healthcare Natural Language API. These sections use the following sample policy as a starting point:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.nlpServiceViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com"
          ]
        }
      ]
    }

### Getting a policy

The following samples show how to read a project-level IAM policy. For more information, see the [`projects.getIamPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy) method.

### curl

To read the IAM policy for a project, make a `POST` request and specify the name of the project and an access token.

The following sample shows a `POST` request using `curl`:
    
    
    curl -X GET \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy"

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.nlpServiceViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com"
          ]
        }
      ]
    }
    

### PowerShell

To view the IAM policy for a project, make a `POST` request and specify the name of the project and an access token.

The following sample shows a `POST` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -Uri "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:getIamPolicy" | Select-Object -Expand Content

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.nlpServiceViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com"
          ]
        }
      ]
    }
    

### Console

To view the IAM policy for a project, complete the following steps:

  1. In the Google Cloud console, go to the IAM page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. To view the principals assigned to a role, click **Roles** and then expand the role. 



### gcloud

To view the IAM policy for a project, run the [`gcloud projects get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy) command. Specify the project name in the request.
    
    
    gcloud projects get-iam-policy PROJECT_ID 

If the request is successful, the bindings are displayed.
    
    
    bindings:
    - members:
      - serviceAccount:service-account-13@appspot.gserviceaccount.com
      role: roles/healthcare.nlpServiceViewer
    etag: bytes
    version: VERSION_NUMBER
    

### Modifying a policy

The following samples grant a service the `roles/healthcare.nlpServiceViewer` role. For more information, see [`projects.setIamPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy).

### Setting a policy

### Console

To set a project-level IAM policy, complete the following steps:

  1. In the Google Cloud console, go to the IAM page. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Click the **Edit** button next to the principal or click **Add principal** and then, in the **New principals** field, enter one or more identities that need access to the project.
  3. In the **Select a role** list, under **Cloud Healthcare** , select Healthcare Natural Language Service Viewer.
  4. Click **Save**.



### gcloud

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new service account the role, add the service account's email address to the `members` array under the `roles/healthcare.nlpServiceViewer` binding:
    
    
    {
      "role":"roles/healthcare.nlpServiceViewer",
      "members": [
          "serviceAccount:service-account-13@appspot.gserviceaccount.com",
          "serviceAccount:NEW_SERVICE_ACCOUNT_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, run the [`gcloud projects set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy) command to make the changes. Specify the project and the path to the policy file that you created.
    
    
    gcloud projects set-iam-policy PROJECT_STORE_ID \
        POLICY_FILE_NAME 

If the request is successful, the project name and the bindings are displayed.
    
    
    Updated IAM policy for project [PROJECT_ID].
    bindings:
    - members:
      - serviceAccount:service-account-13@appspot.gserviceaccount.com
      - serviceAccount:NEW_USER_EMAIL_ADDRESS
      role: roles/healthcare.nlpServiceViewer
    etag: bytes
    version: VERSION_NUMBER
    

### curl

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new service account the role, add the service account's email address to the `members` array under the `roles/healthcare.nlpServiceViewer` binding:
    
    
    {
      "role":"roles/healthcare.nlpServiceViewer",
      "members": [
          "serviceAccount:service-account-13@appspot.gserviceaccount.com",
          "serviceAccount:NEW_SERVICE_ACCOUNT_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, call [`projects.setIamPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy) to make the updates.

To set a project-level IAM policy, make a `POST` request and specify the project name, the policy, and an access token.

The following sample shows a `POST` request using `curl` to grant a new user the existing `roles/healthcare.nlpServiceViewer` role:

The policy can be written directly in the request, as shown here, or it can be passed in as a JSON or YAML file. For examples of how to format a policy as JSON or YAML, see [`Policy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Policy). 
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'policy': {
            'bindings': [
              {
                'role':'roles/healthcare.nlpServiceViewer',
                'members': [
                  'serviceAccount:service-account-13@appspot.gserviceaccount.com'
                ]
              }
            ]
          }
        }" "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy"

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.nlpServiceViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com"
          ]
        }
      ]
    }
    

### PowerShell

Grant or revoke roles to users by modifying the policy that you retrieved, programmatically or using a text editor. The `etag` value changes when the policy changes, so you must specify the current value. 

To grant a new service account the role, add the service account's email address to the `members` array under the `roles/healthcare.nlpServiceViewer` binding:
    
    
    {
      "role":"roles/healthcare.nlpServiceViewer",
      "members": [
          "serviceAccount:service-account-13@appspot.gserviceaccount.com",
          "serviceAccount:NEW_SERVICE_ACCOUNT_EMAIL_ADDRESS"
      ]
    }

To revoke a principal's access, delete their email address from the `members` array. To revoke access from the last principal that has a role, delete the `bindings` array for the role. You cannot have an empty `bindings` array in your policy. 

After you have modified the policy to grant the applicable roles, call [`projects.setIamPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy) to make the updates.

To set a project-level IAM policy, make a `POST` request and specify the project name, the policy, and an access token.

The following sample shows a `POST` request using `curl` to grant a new user the existing `roles/healthcare.nlpServiceViewer` role:

The policy can be written directly in the request, as shown here, or it can be passed in as a JSON or YAML file. For examples of how to format a policy as JSON or YAML, see [`Policy`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/Shared.Types/Policy). 
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
        'policy': {
          'bindings': [
            {
              'role': 'roles/healthcare.nlpServiceViewer',
              'members': [
                'serviceAccount:service-account-13@appspot.gserviceaccount.com',
                'serviceAccount:NEW_USER_EMAIL_ADDRESS'
              ]
            }
          ]
        }
      }" `
      -Uri "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:setIamPolicy" | Select-Object -Expand Content

The response is the following:
    
    
    {
      "etag":"bytes",
      "bindings": [
        {
          "role":"roles/healthcare.nlpServiceViewer",
          "members": [
            "serviceAccount:service-account-13@appspot.gserviceaccount.com",
            "serviceAccount:NEW_USER_EMAIL_ADDRESS"
          ]
        }
      ]
    }
    

## What's next

  * [Read about the read-modify-write pattern using IAM policies](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#overview_of_cloud_iam_policy).
  * [View the available Cloud Healthcare API roles](https://docs.cloud.google.com/healthcare-api/docs/access-control#roles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
