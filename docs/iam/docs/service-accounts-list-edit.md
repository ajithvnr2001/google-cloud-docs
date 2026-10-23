---
url: https://docs.cloud.google.com/iam/docs/service-accounts-list-edit/
title: List and edit service accounts \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:08.892255+00:00
---

# List and edit service accounts  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/service-accounts-list-edit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  List and edit service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to list and edit service accounts using the Identity and Access Management (IAM) API, the Google Cloud console, and the `gcloud` command- line tool.

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

  * Understand [IAM service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview)




### Required roles

To get the permissions that you need to manage service accounts, ask your administrator to grant you the following IAM roles on the project: 

  * To view service accounts: [View Service Accounts ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountViewer) (`roles/iam.serviceAccountViewer`) 
  * To edit service accounts: [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

IAM basic roles also contain permissions to manage service accounts. You should not grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Listing service accounts

You can list the [user-managed service accounts](https://docs.cloud.google.com/iam/docs/service-accounts#user-managed) in a project to help you audit service accounts and keys, or as part of a custom tool for managing service accounts.

You can't list the [service agents](https://docs.cloud.google.com/iam/docs/service-agents) that might appear in your project's allow policy and audit logs. Service agents aren't located in your project, and you can't access them directly.

### Console

  1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select a project.

The **Service accounts** page lists all of the user-managed service accounts in the project you selected.




### gcloud

The `[gcloud iam service-accounts list](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list)` command lists every user-managed service account in the specified project. 

Before using any of the command data below, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud iam service-accounts list --project=PROJECT_ID

#### Windows (PowerShell)
    
    
    gcloud iam service-accounts list --project=PROJECT_ID

#### Windows (cmd.exe)
    
    
    gcloud iam service-accounts list --project=PROJECT_ID

You should receive a response similar to the following:
    
    
    DISPLAY NAME: SA_DISPLAY_NAME_1
    EMAIL: SA_NAME_1@PROJECT_ID.iam.gserviceaccount.com
    DISABLED: False
    
    DISPLAY NAME: SA_DISPLAY_NAME_2
    EMAIL: SA_NAME_2@PROJECT_ID.iam.gserviceaccount.com
    DISABLED: False
    

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& project_id) {
      iam::IAMClient client(iam::MakeIAMConnection());
      int count = 0;
      for (auto& sa : client.ListServiceAccounts("projects/" + project_id)) {
        if (!sa) throw std::move(sa).status();
        std::cout << "ServiceAccount successfully retrieved: " << sa->name()
                  << "\n";
        ++count;
      }
      if (count == 0) {
        std::cout << "No service accounts found in project: " << project_id
                  << "\n";
      }
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.Iam.v1;
    using Google.Apis.Iam.v1.Data;
    
    public partial class ServiceAccounts
    {
        public static IList<ServiceAccount> ListServiceAccounts(string projectId)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
    
            var response = service.Projects.ServiceAccounts.List(
                "projects/" + projectId).Execute();
            foreach (ServiceAccount account in response.Accounts)
            {
                Console.WriteLine("Name: " + account.Name);
                Console.WriteLine("Display Name: " + account.DisplayName);
                Console.WriteLine("Email: " + account.Email);
                Console.WriteLine();
            }
            return response.Accounts;
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
    
    // listServiceAccounts lists a project's service accounts.
    func listServiceAccounts(w io.Writer, projectID string) ([]*iam.ServiceAccount, error) {
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	response, err := service.Projects.ServiceAccounts.List("projects/" + projectID).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Projects.ServiceAccounts.List: %w", err)
    	}
    	for _, account := range response.Accounts {
    		fmt.Fprintf(w, "Listing service account: %v\n", account.Name)
    	}
    	return response.Accounts, nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html);
    import java.io.IOException;
    
    public class ListServiceAccounts {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Replace the below variables before running.
        String projectId = "your-project-id";
    
        listServiceAccounts(projectId);
      }
    
      // Lists all service accounts for the current project.
      public static [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).[ListServiceAccountsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.ListServiceAccountsPagedResponse.html) listServiceAccounts(String projectId)
              throws IOException {
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).[ListServiceAccountsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.ListServiceAccountsPagedResponse.html) response =
                  iamClient.listServiceAccounts(String.format("projects/%s", projectId));
    
          for ([ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html) account : response.iterateAll()) {
            System.out.println("Name: " + account.getName());
            System.out.println("Display name: " + account.getDisplayName());
            System.out.println("Email: " + account.getEmail() + "\n");
          }
    
          return response;
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    from typing import List
    
    from google.cloud import iam_admin_v1
    from google.cloud.iam_admin_v1 import types
    
    
    def list_service_accounts(project_id: str) -> List[iam_admin_v1.ServiceAccount]:
        """Get list of project service accounts.
    
        project_id: ID or number of the Google Cloud project you want to use.
    
        returns a list of iam_admin_v1.ServiceAccount
        """
    
        iam_admin_client = iam_admin_v1.IAMClient()
        request = types.ListServiceAccountsRequest()
        request.name = f"projects/{project_id}"
    
        accounts = iam_admin_client.list_service_accounts(request=request)
        return accounts.accounts

### REST

The `[serviceAccounts.list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/list)` method lists every user-managed service account in the specified project. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/list). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "accounts": [
        {
          "name": "projects/my-project/serviceAccounts/sa-1@my-project.iam.gserviceaccount.com",
          "projectId": "my-project",
          "uniqueId": "123456789012345678901",
          "email": "sa-1@my-project.iam.gserviceaccount.com",
          "description": "My first service account",
          "displayName": "Service account 1",
          "etag": "BwUpTsLVUkQ=",
          "oauth2ClientId": "987654321098765432109"
        },
        {
          "name": "projects/my-project/serviceAccounts/sa-2@my-project.iam.gserviceaccount.com",
          "projectId": "my-project",
          "uniqueId": "234567890123456789012",
          "email": "sa-2@my-project.iam.gserviceaccount.com",
          "description": "My second service account",
          "displayName": "Service account 2",
          "etag": "UkQpTwBVUsL=",
          "oauth2ClientId": "876543210987654321098"
        }
      ]
    }
    

## Edit a service account

The display name (friendly name) and description of a service account are commonly used to capture additional information about the service account, such as the purpose of the service account or a contact person for the account.

### Console

  1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select a project.

  3. Click the email address of the service account that you want to rename.

  4. Enter the new name in the **Name** box, then click **Save**.




### gcloud

The `[gcloud iam service-accounts update](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/update)` command updates a service account. 

Before using any of the command data below, make the following replacements: 

  * `SA_NAME`: The alphanumeric ID of your service account. This name must be between 6 and 30 characters, and can contain lowercase alphanumeric characters and dashes.
  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * Replace at least one of the following:
    * `UPDATED_DISPLAY_NAME`: A new display name for your service account.
    * `UPDATED_DESCRIPTION`: A new description for your service account.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud iam service-accounts update \
        SA_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --project=PROJECT_ID
        --description="UPDATED_SA_DESCRIPTION" \
        --display-name="UPDATED_DISPLAY_NAME"

#### Windows (PowerShell)
    
    
    gcloud iam service-accounts update `
        SA_NAME@PROJECT_ID.iam.gserviceaccount.com `
        --project=PROJECT_ID
        --description="UPDATED_SA_DESCRIPTION" `
        --display-name="UPDATED_DISPLAY_NAME"

#### Windows (cmd.exe)
    
    
    gcloud iam service-accounts update ^
        SA_NAME@PROJECT_ID.iam.gserviceaccount.com ^
        --project=PROJECT_ID
        --description="UPDATED_SA_DESCRIPTION" ^
        --display-name="UPDATED_DISPLAY_NAME"

You should receive a response similar to the following:
    
    
    Updated serviceAccount [SA_NAME@PROJECT_ID.iam.gserviceaccount.com].
    description: UPDATED_SA_DESCRIPTION
    displayName: UPDATED_DISPLAY_NAME
    name: projects/PROJECT_ID/serviceAccounts/SA_NAME@PROJECT_ID.iam.gserviceaccount.com
    

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& name, std::string const& display_name) {
      iam::IAMClient client(iam::MakeIAMConnection());
      google::iam::admin::v1::PatchServiceAccountRequest request;
      google::iam::admin::v1::ServiceAccount service_account;
      service_account.set_name(name);
      service_account.set_display_name(display_name);
      google::protobuf::FieldMask update_mask;
      *update_mask.add_paths() = "display_name";
      *request.mutable_service_account() = service_account;
      *request.mutable_update_mask() = update_mask;
      auto response = client.PatchServiceAccount(request);
      if (!response) throw std::move(response).status();
      std::cout << "ServiceAccount successfully updated: "
                << response->DebugString() << "\n";
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    using System;
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.Iam.v1;
    using Google.Apis.Iam.v1.Data;
    
    public partial class ServiceAccounts
    {
        public static ServiceAccount RenameServiceAccount(string email,
            string newDisplayName)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
    
            // First, get a ServiceAccount using List() or Get().
            string resource = "projects/-/serviceAccounts/" + email;
            var serviceAccount = service.Projects.ServiceAccounts.Get(resource)
                .Execute();
            // Then you can update the display name.
            serviceAccount.DisplayName = newDisplayName;
            serviceAccount = service.Projects.ServiceAccounts.Update(
                serviceAccount, resource).Execute();
            Console.WriteLine($"Updated display name for {serviceAccount.Email} " +
                "to: " + serviceAccount.DisplayName);
            return serviceAccount;
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
    
    // renameServiceAccount renames a service account.
    func renameServiceAccount(w io.Writer, email, newDisplayName string) (*iam.ServiceAccount, error) {
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	// First, get a ServiceAccount using List() or Get().
    	resource := "projects/-/serviceAccounts/" + email
    	serviceAccount, err := service.Projects.ServiceAccounts.Get(resource).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Projects.ServiceAccounts.Get: %w", err)
    	}
    	// Then you can update the display name.
    	serviceAccount.DisplayName = newDisplayName
    	serviceAccount, err = service.Projects.ServiceAccounts.Update(resource, serviceAccount).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Projects.ServiceAccounts.Update: %w", err)
    	}
    
    	fmt.Fprintf(w, "Updated service account: %v", serviceAccount.Email)
    	return serviceAccount, nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[GetServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.GetServiceAccountRequest.html);
    import com.google.iam.admin.v1.[PatchServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.PatchServiceAccountRequest.html);
    import com.google.iam.admin.v1.[ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html);
    import com.google.iam.admin.v1.[ServiceAccountName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class RenameServiceAccount {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        String projectId = "your-project-id";
        String serviceAccountName = "my-service-account-name";
        String displayName = "your-new-display-name";
    
        renameServiceAccount(projectId, serviceAccountName, displayName);
      }
    
      // Changes a service account's display name.
      public static [ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html) renameServiceAccount(String projectId, String serviceAccountName,
                                                        String displayName) throws IOException {
        // Construct the service account email.
        // You can modify the ".iam.gserviceaccount.com" to match the service account name in which
        // you want to delete the key.
        // See, https://cloud.google.com/iam/docs/creating-managing-service-account-keys?hl=en#deleting
        String serviceAccountEmail = serviceAccountName + "@" + projectId + ".iam.gserviceaccount.com";
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          // First, get a service account using getServiceAccount or listServiceAccounts
          [GetServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.GetServiceAccountRequest.html) serviceAccountRequest = [GetServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.GetServiceAccountRequest.html).newBuilder()
                  .setName([ServiceAccountName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html).of(projectId, serviceAccountEmail).toString())
                  .build();
          [ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html) serviceAccount = iamClient.getServiceAccount(serviceAccountRequest);
    
          // You can patch only the `display_name` and `description` fields. You must use
          //  the `update_mask` field to specify which of these fields you want to patch.
          serviceAccount = serviceAccount.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html#com_google_iam_admin_v1_ServiceAccount_toBuilder__)().[setDisplayName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.Builder.html#com_google_iam_admin_v1_ServiceAccount_Builder_setDisplayName_java_lang_String_)(displayName).build();
          [PatchServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.PatchServiceAccountRequest.html) patchServiceAccountRequest =
                  [PatchServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.PatchServiceAccountRequest.html).newBuilder()
                          .setServiceAccount(serviceAccount)
                          .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("display_name").build())
                          .build();
          serviceAccount = iamClient.patchServiceAccount(patchServiceAccountRequest);
    
          System.out.println(
                  "Updated display name for "
                          + serviceAccount.[getName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html#com_google_iam_admin_v1_ServiceAccount_getName__)()
                          + " to: "
                          + serviceAccount.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html#com_google_iam_admin_v1_ServiceAccount_getDisplayName__)());
          return serviceAccount;
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    from google.cloud import iam_admin_v1
    from google.cloud.iam_admin_v1 import [types](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.html)
    
    
    def rename_service_account(
        project_id: str, account: str, new_name: str
    ) -> types.ServiceAccount:
        """Renames service account display name.
    
        project_id: ID or number of the Google Cloud project you want to use.
        account: ID or email which is unique identifier of the service account.
        new_name: New display name of the service account.
        """
    
        iam_admin_client = iam_admin_v1.[IAMClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html)()
    
        get_request = [types](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.html).[GetServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetServiceAccountRequest.html)()
        get_request.name = f"projects/{project_id}/serviceAccounts/{account}"
        service_account = iam_admin_client.[get_service_account](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_get_service_account)(request=get_request)
    
        service_account.display_name = new_name
    
        request = [types](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.html).[PatchServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.PatchServiceAccountRequest.html)()
        request.service_account = service_account
        # You can patch only the `display_name` and `description` fields.
        # You must use the `update_mask` field to specify which of these fields
        # you want to patch.
        # To successfully set update mask you need to transform
        # snake_case field to camelCase.
        # e.g. `display_name` will become `displayName`
        request.update_mask = "displayName"
    
        updated_account = iam_admin_client.[patch_service_account](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_patch_service_account)(request=request)
        return updated_account

### REST

The `[serviceAccounts.patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/patch)` method updates a service account. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_ID`: The ID of your service account. This can either be the service account's email address in the form `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`, or the service account's unique numeric ID.
  * `SA_NAME`: The alphanumeric ID of your service account. This name must be between 6 and 30 characters, and can contain lowercase alphanumeric characters and dashes.
  * Replace at least one of the following:
    * `UPDATED_DISPLAY_NAME`: A new display name for your service account.
    * `UPDATED_DESCRIPTION`: A new description for your service account.



HTTP method and URL: 
    
    
    PATCH https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_ID

Request JSON body: 
    
    
    {
      "serviceAccount": {
        "email": "SA_NAME@PROJECT_ID.iam.gserviceaccount.com",
        "displayName": "UPDATED_DISPLAY_NAME",
        "description": "UPDATED_DESCRIPTION"
      },
      "updateMask": "displayName,description"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_ID" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/patch). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com",
      "displayName": "My updated service account",
      "description": "An updated description of my service account"
    }
    

## What's next

  * Learn how to [disable and enable service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable).
  * Review the process for [granting IAM roles to all types of principals](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access), including service accounts. 
  * Explore how you can use [role recommendations](https://docs.cloud.google.com/iam/docs/recommender-overview) to downscope permissions for all principals, including service accounts. 
  * Understand how to [attach service accounts to resources](https://docs.cloud.google.com/iam/docs/attach-service-accounts).
  * Get [best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
