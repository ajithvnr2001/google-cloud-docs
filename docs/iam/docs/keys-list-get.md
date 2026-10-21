---
url: https://docs.cloud.google.com/iam/docs/keys-list-get/
title: List and get service account keys \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:05.431617+00:00
---

# List and get service account keys  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/keys-list-get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  List and get service account keys Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to list and get service account keys using the Google Cloud console, the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud), the [Identity and Access Management API](https://docs.cloud.google.com/iam/docs/reference/rest), or one of the [Google Cloud Client Libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries).

**Note:** If you need to access resources from a workload that runs outside of Google Cloud, such as on Amazon Web Services (AWS) or Microsoft Azure, consider using [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) instead of service account keys. Federation lets your workloads access resources directly, using a short-lived access token, and eliminates the maintenance and security burden associated with service account keys. 

## Before you begin

  * Enable the IAM API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Set up authentication.

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### C#

To use the .NET samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### C++

To use the C++ samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Go

To use the Go samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

  * Understand [service account credentials](https://docs.cloud.google.com/iam/docs/service-account-creds).




### Required roles

To get the permissions that you need to list and get service account keys, ask your administrator to grant you the [View Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountViewer) (`roles/iam.serviceAccountViewer`) IAM role on either the project or the service account whose keys you want to manage. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

IAM basic roles also contain permissions to manage service account keys. You should not grant basic roles in a production environment, but you can grant them in a development or test environment. 

## List service account keys

You can list the service account keys for a service account using the Google Cloud console, the gcloud CLI, the [`serviceAccount.keys.list()`](https://docs.cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys/list) method, or one of the [client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries).

The `serviceAccount.keys.list()` method is commonly used to audit service accounts and keys, or to build custom tooling for managing service accounts.

To find out which project your key belongs to, you can download the key as a JSON file and look at that file.

You might see keys listed that you did not create. These are keys created by Google and used by the Service Account Credentials API. To learn more, see [Google-owned and managed key pairs](https://docs.cloud.google.com/iam/docs/service-account-creds#google-managed-keys).

### Console

  1. In the Google Cloud console, go to the **Service accounts** page. 

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts?walkthrough_id=iam--list-service-account-keys&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. Select a project.
  3. On the **Service accounts** page, click the email address of the service account whose keys you want to list.
  4. Click **Keys**. The Google Cloud console displays a list of keys for the service account.



### gcloud

Execute the [`gcloud iam service-accounts keys list`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list) command to list service account keys.

Replace the following values:

  * `SA_NAME`: The name of the service account to list keys for.
  * `PROJECT_ID`: Your Google Cloud project ID.


    
    
    gcloud iam service-accounts keys list \
        --iam-account=SA_NAME@PROJECT_ID.iam.gserviceaccount.com
    

Output:

KEY_ID | CREATED_AT | EXPIRES_AT | DISABLED | DISABLE_REASON | EXTENDED_STATUS  
---|---|---|---|---|---  
8e6e3936d7024646f8ceb39792006c07f4a9760c | 2021-01-01T21:01:42Z | 9999-12-31T23:59:59Z |  |  |   
937c98f870f5c8db970af527aa3c12fd88b1c20a | 2021-01-01T20:55:40Z | 9999-12-31T23:59:59Z | True | USER INITIATED |   
937c98f870f5c8db970af527aa3c12fd88b1c20a | 2021-01-01T20:55:40Z | 9999-12-31T23:59:59Z | True | EXPOSED | ['key':'SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_EXPOSED' 'value':'{exposure URL}']  
  
### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& service_account_name,
       std::vector<std::string> const& key_type_labels) {
      iam::IAMClient client(iam::MakeIAMConnection());
      std::vector<google::iam::admin::v1::ListServiceAccountKeysRequest::KeyType>
          key_types;
      for (auto const& type : key_type_labels) {
        if (type == "USER_MANAGED") {
          key_types.push_back(google::iam::admin::v1::
                                  ListServiceAccountKeysRequest::USER_MANAGED);
        } else if (type == "SYSTEM_MANAGED") {
          key_types.push_back(google::iam::admin::v1::
                                  ListServiceAccountKeysRequest::SYSTEM_MANAGED);
        }
      }
      auto response =
          client.ListServiceAccountKeys(service_account_name, key_types);
      if (!response) throw std::move(response).status();
      std::cout << "ServiceAccountKeys successfully retrieved: "
                << response->DebugString() << "\n";
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.Iam.v1;
    using Google.Apis.Iam.v1.Data;
    
    public partial class ServiceAccountKeys
    {
        public static IList<ServiceAccountKey> ListKeys(string serviceAccountEmail)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
    
            var response = service.Projects.ServiceAccounts.Keys
                .List($"projects/-/serviceAccounts/{serviceAccountEmail}")
                .Execute();
            foreach (ServiceAccountKey key in response.Keys)
            {
                Console.WriteLine("Key: " + key.Name);
            }
            return response.Keys;
        }
    }
    

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/iam/admin/apiv1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	iam "google.golang.org/api/iam/v1"
    )
    
    // listKey lists a service account's keys.
    func listKeys(w io.Writer, serviceAccountEmail string) ([]*iam.ServiceAccountKey, error) {
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	resource := "projects/-/serviceAccounts/" + serviceAccountEmail
    	response, err := service.Projects.ServiceAccounts.Keys.List(resource).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Projects.ServiceAccounts.Keys.List: %w", err)
    	}
    	for _, key := range response.Keys {
    		fmt.Fprintf(w, "Listing key: %v", key.Name)
    	}
    	return response.Keys, nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[ListServiceAccountKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ListServiceAccountKeysRequest.html);
    import com.google.iam.admin.v1.[ServiceAccountKey](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountKey.html);
    import java.io.IOException;
    import java.util.List;
    
    public class ListServiceAccountKeys {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Replace the below variables before running.
        String projectId = "your-project-id";
        String serviceAccountName = "your-service-account-name";
    
        List<ServiceAccountKey> keys = listKeys(projectId, serviceAccountName);
        keys.forEach(key -> System.out.println("Key: " + key.getName()));
      }
    
      // Lists all keys for a service account.
      public static List<ServiceAccountKey> listKeys(String projectId, String accountName)
              throws IOException {
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        String email = String.format("%s@%s.iam.gserviceaccount.com", accountName, projectId);
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          [ListServiceAccountKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ListServiceAccountKeysRequest.html) req = [ListServiceAccountKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ListServiceAccountKeysRequest.html).newBuilder()
                  .setName(String.format("projects/%s/serviceAccounts/%s", projectId, email))
                  .build();
    
          return iamClient.listServiceAccountKeys(req).getKeysList();
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    from typing import List
    
    from google.cloud import iam_admin_v1
    from google.cloud.iam_admin_v1 import types
    
    
    def list_keys(project_id: str, account: str) -> List[iam_admin_v1.ServiceAccountKey]:
        """Lists a key for a service account.
    
        project_id: ID or number of the Google Cloud project you want to use.
        account: ID or email which is unique identifier of the service account.
        """
    
        iam_admin_client = iam_admin_v1.IAMClient()
        request = types.ListServiceAccountKeysRequest()
        request.name = f"projects/{project_id}/serviceAccounts/{account}"
    
        response = iam_admin_client.list_service_account_keys(request=request)
        return response.keys

### REST

The `[projects.serviceAccounts.keys.list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/list)` method lists all of the service account keys for a service account. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_NAME`: The name of the service account whose keys you want to list.
  * `KEY_TYPES`: Optional. A comma-separated list of key types that you want to include in the response. The key type indicates whether a key is user-managed (`USER_MANAGED`) or system-managed (`SYSTEM_MANAGED`). If left blank, all keys are returned. 



HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys?keyTypes=KEY_TYPES

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys?keyTypes=KEY_TYPES"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys?keyTypes=KEY_TYPES" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "keys": [
        {
          "name": "projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com/keys/90c48f61c65cd56224a12ab18e6ee9ca9c3aee7c",
          "validAfterTime": "2020-03-04T17:39:47Z",
          "validBeforeTime": "9999-12-31T23:59:59Z",
          "keyAlgorithm": "KEY_ALG_RSA_2048",
          "keyOrigin": "GOOGLE_PROVIDED",
          "keyType": "USER_MANAGED"
        },
        {
          "name": "projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com/keys/e5e3800831ac1adc8a5849da7d827b4724b1fce8",
          "validAfterTime": "2020-03-31T23:50:09Z",
          "validBeforeTime": "9999-12-31T23:59:59Z",
          "keyAlgorithm": "KEY_ALG_RSA_2048",
          "keyOrigin": "GOOGLE_PROVIDED",
          "keyType": "USER_MANAGED"
        },
        {
          "name": "projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com/keys/b97699f042b8eee6a846f4f96259fbcd13e2682e",
          "validAfterTime": "2020-05-17T18:58:13Z",
          "validBeforeTime": "9999-12-31T23:59:59Z",
          "keyAlgorithm": "KEY_ALG_RSA_2048",
          "keyOrigin": "GOOGLE_PROVIDED",
          "keyType": "USER_MANAGED",
          "disabled": true
          "disable_reason": "SERVICE_ACCOUNT_KEY_DISABLE_REASON_EXPOSED"
          "extended_status": "SERVICE_ACCOUNT_KEY_EXTENDED_STATUS_KEY_EXPOSED"
          "extended_status_message": "exposed at: https://www.github.com/SomePublicRepo"
        }
      ]
    }
    

## Get a service account key

You can use the gcloud CLI or the REST API to get the public key data for a service account key. In addition, you can use the Google Cloud console, the gcloud CLI, or the REST API to get metadata for the key, such as the algorithm that the key uses and whether the key is managed by you or by Google.

Some applications or tools might need access to the public key data or metadata for a service account key for things like auditing and interoperability with external systems. For example, [Terraform](https://docs.cloud.google.com/docs/terraform/terraform-overview) might need to verify that the state of a service account key in Google Cloud matches what's defined in the Terraform configuration file.

**Note:** You cannot get the private key data for a service account key. This data is available only when the key is created.

### Console

**To get the public key data for a service account key:**

Use the gcloud CLI or the REST API. This data is not available in the Google Cloud console.

**To get metadata for a service account key:**

  1. In the Google Cloud console, go to the **Service accounts** page. 

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts?walkthrough_id=iam--get-service-account-keys&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. Select a project.
  3. On the **Service accounts** page, click the email address of the service account whose keys you want to list.
  4. Click **Keys**. The Google Cloud console displays a list of keys for the service account, including metadata for each key.



### gcloud

**To get the public key data for a service account key:**

Run the [`gcloud beta iam service-accounts keys get-public-key`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/iam/service-accounts/keys/get-public-key) command:
    
    
    gcloud beta iam service-accounts keys get-public-key KEY_ID \
        --iam-account=SA_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --output-file=FILENAME

Provide the following values:

  * `KEY_ID`: The ID of the public key you want to get. To find the key's ID, list all keys for the service account, identify the key that you want to get, and then copy its ID.
  * `SA_NAME`: The name of the service account whose public key you want to get.
  * `PROJECT_ID`: Your Google Cloud project ID.
  * `FILENAME`: The file in which to save the public key data.



By default, the public key data is saved in X.509 PEM format. To get the raw public key, run the command with the additional flag `--type=raw`.

For example, the following command gets the public key data for the key `c97cc34494c07c9b483701f28368f20145b9ef97`, which belongs to the service account `my-service-account@my-project.iam.gserviceaccount.com`, then saves the public key data to the file `public_key.pem`:
    
    
    gcloud beta iam service-accounts keys get-public-key \
        c97cc34494c07c9b483701f28368f20145b9ef97 \
        --iam-account=my-service-account@my-project.iam.gserviceaccount.com \
        --output-file=public_key.pem
    

**To get metadata for a service account key:**

Run the [`gcloud iam service-accounts keys list`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/keys/list) command:
    
    
    gcloud iam service-accounts keys list --iam-account=SA_NAME \
        --filter="name~KEY_ID" --format=json

Provide the following values:

  * `SA_NAME`: The name of the service account for which you want key metadata.
  * `KEY_ID`: The ID of the key for which you want metadata.



For example, the following command gets metadata for the key `c97cc34494c07c9b483701f28368f20145b9ef97`, which belongs to the service account `my-service-account@my-project.iam.gserviceaccount.com`:
    
    
    gcloud iam service-accounts keys list \
        --iam-account=my-service-account@my-project.iam.gserviceaccount.com \
        --filter="name~c97cc34494c07c9b483701f28368f20145b9ef97" --format=json
    

### REST

The `[projects.serviceAccounts.keys.get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/get)` method returns information about a public key for a service account. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_NAME`: The name of the service account whose public key you want to get.
  * `KEY_ID`: The ID of the public key you want to get. To find the key's ID, list all keys for the service account, identify the key that you want to get, and then copy its ID from the end of the `name` field. The key's ID is everything after `keys/`. 
  * `KEY_TYPE`: The format in which to return the public key. Use `TYPE_X509_PEM_FILE` for X.509 PEM format or `TYPE_RAW_PUBLIC_KEY` for the raw public key. If you omit this query parameter, the method returns metadata for the key, but it does not return the public key data.



HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys/KEY_ID?publicKeyType=KEY_TYPE

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys/KEY_ID?publicKeyType=KEY_TYPE"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com/keys/KEY_ID?publicKeyType=KEY_TYPE" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys/get). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com/keys/f4a83933ac07cf52bb74e0e66d99662a09f51a36",
      "validAfterTime": "2021-12-10T17:32:06Z",
      "validBeforeTime": "9999-12-31T23:59:59Z",
      "publicKeyData": "LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSUMvRENDQWVTZ0F3SUJBZ0lJT2lCdm9hR09nV0F3RFFZSktvWklodmNOQVFFRkJRQXdJREVlTUJ3R0ExVUUKQXhNVk1UQXhNVGsxTlRFMk5UWXlPRGszTmpFek1qQXpNQ0FYRFRJeE1USXhNREUzTXpJd05sb1lEems1T1RreApNak14TWpNMU9UVTVXakFnTVI0d0hBWURWUVFERXhVeE1ERXhPVFUxTVRZMU5qSTRPVGMyTVRNeU1ETXdnZ0VpCk1BMEdDU3FHU0liM0RRRUJBUVVBQTRJQkR3QXdnZ0VLQW9JQkFRQzdzeDBFcXVUMGNwSXhlczl1SW0yRy9DS3EKdnc4YTl2a2JkaWZZbDZHSDh1ZUxEWDhGNHVUeEVQMkNzU3JLTHZtOFo2My9IVUxnWjBtQXByb0JlM08vaVR1ZwpmYVZ0NVNtakhvWm9YQ1lpbjR0MS93SkpvdDhrRFdPeDZhOEdieUdqZ215ak8yYk1XdEtaQ2dqeGZ3cUV0MmN3CklnajA5VzJKYTlHTWRsdVA0VGVubTRKSkJoaFpFbTJ1bVAwYVZZdkRnUWF5d0RCYnJuNG8yY0EzSWplRDZGM1gKK0VHRDNKU0s4VW02Sk5sM21adGp6VWNZSHBrYkF0U1A2ZDI5d1RmZkdIRFY0THJRWlM3bG15d3hsb3p5WnpaawpCOFpHckMzSkF1MVNVRTdQOTN6bWtFb1B6MlRUNWhaYXZMWFQ5TGM2SExiRklRVHFnVEJVWHlNMkpIcGZBZ01CCkFBR2pPREEyTUF3R0ExVWRFd0VCL3dRQ01BQXdEZ1lEVlIwUEFRSC9CQVFEQWdlQU1CWUdBMVVkSlFFQi93UU0KTUFvR0NDc0dBUVVGQndNQ01BMEdDU3FHU0liM0RRRUJCUVVBQTRJQkFRQkhPNXlpUDY3NkE4UEN2RjdRSzdFMApYZVljbzdsSStFZkowaGJrWVlmdUtnSENPcXcvd3FBbCtOSithanljT2FPWDFPMlRZN3ZOc05pR2t3eWc2QXdqCklhL1NHVjd3NkxpS2JldFRuSVp4UlhRY25lcnVvZEwycUR5eWphMDJJSXJVTmVKY1o0MVJBNXRTL3NkcTFGNm4KM0NjSXFoZTI1OTA4TUNna3cwaFB1K0VLbFF6R1B5T3pVRHBLdXg0cnRBaHJTYTBUVW1wbEMxdTJnUk1YRkF6aApWUjU0V2dNa2tabURyalBNeWdBS3JmNkd0bHo2VHRTYTVLb1BWdGpsWExUQkxaSnlhdk4zc1F2dFlBK1NFQWpWCnA1N1ZabFBYZmR0dWN4ekJaOC9zS25SOHNyYU5hVWFjamg1NEE1Nm1URTE3b0IyUWkrTHBJUTYvNnVqVnNXaUYKLS0tLS1FTkQgQ0VSVElGSUNBVEUtLS0tLQo=",
      "keyAlgorithm": "KEY_ALG_RSA_2048",
      "keyOrigin": "GOOGLE_PROVIDED",
      "keyType": "USER_MANAGED"
    }
    

## What's next

  * Learn how to [create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete).
  * Learn how to [disable and enable service account keys](https://docs.cloud.google.com/iam/docs/keys-disable-enable).
  * Learn about [alternatives to service account keys for authentication](https://docs.cloud.google.com/docs/authentication#auth-decision-tree).
  * Learn how to use service account keys to [authenticate as a service account](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises#wlif-key).
  * Understand the [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
