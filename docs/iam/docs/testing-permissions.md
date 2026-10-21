---
url: https://docs.cloud.google.com/iam/docs/testing-permissions/
title: Test permissions for custom user interfaces \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:14.306139+00:00
---

# Test permissions for custom user interfaces  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/testing-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Test permissions for custom user interfaces Stay organized with collections  Save and categorize content based on your preferences. 

Most Google Cloud resources expose the `testIamPermissions()` method, which allows you to programmatically check whether the currently authenticated caller has been granted one or more specific IAM permissions on the resource. The `testIamPermissions()` method takes a resource identifier and a set of permissions as input parameters, and returns the set of permissions that the caller is allowed.

You can use the `testIamPermissions()` method to determine whether a user should have access to an administrative tool in a web application. For example, you can use this method to decide, based on the user's permissions, whether to display detailed information about a Google Cloud resource.

**Note:** If you need to test a permission so that you can troubleshoot access to a resource, use the [Policy Troubleshooter](https://docs.cloud.google.com/iam/docs/troubleshooting-access) instead.

For example, to determine if the currently authenticated user has the permission to delete a project, call the [`projects.testIamPermissions()`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/testIamPermissions) method by providing the project ID (such as `foo-project`) and the `resourcemanager.projects.delete` permission as input parameters. If the caller has been granted the `resourcemanager.projects.delete` permission, it will be listed in the response body. If the caller does not have this permission, the response body will list no permissions.

The `testIamPermissions()` method is intended for third-party graphical user interfaces (GUIs) that need to display Google Cloud resources based on what the authenticated user has permissions to see. For example, the Google Cloud console internally uses the `testIamPermissions()` method to determine what resources and functionality are visible to you after authenticating. Different users are typically granted different permissions, and the Google Cloud console hides or exposes items accordingly.

## Before you begin

  * Enable the Resource Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Set up authentication.

Select the tab for how you plan to use the samples on this page:

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




### Required roles

No IAM role is required to test permissions.

## How to test permissions

This example shows how to test the `resourcemanager.projects.get` and `resourcemanager.projects.delete` permissions for a [Google Cloud project](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects). To test permissions for other Google Cloud resources, use the `testIamPermissions()` method exposed by each resource. For example, you can test the IAM permissions for a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/testIamPermissions).

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& name, std::vector<std::string> const& permissions) {
      iam::IAMClient client(iam::MakeIAMConnection());
      auto response = client.TestIamPermissions(name, permissions);
      if (!response) throw std::move(response).status();
      std::cout << "Permissions successfully tested: " << response->DebugString()
                << "\n";
    }

### C#

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

IAM tests the permissions of the service account that you are using to generate credentials. 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.CloudResourceManager.v1;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static IList<String> TestIamPermissions(string projectId)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(CloudResourceManagerService.Scope.CloudPlatform);
            var service = new CloudResourceManagerService(
                new CloudResourceManagerService.Initializer
                {
                    HttpClientInitializer = credential
                });
    
            TestIamPermissionsRequest requestBody = new TestIamPermissionsRequest();
            var permissions = new List<string>() { "resourcemanager.projects.get", "resourcemanager.projects.delete" };
            requestBody.Permissions = new List<string>(permissions);
            var returnedPermissions = service.Projects.TestIamPermissions(requestBody, projectId).Execute().Permissions;
    
            return returnedPermissions;
        }
    }

### Java

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

IAM tests the permissions of the service account that you are using to generate credentials. 
    
    
    import com.google.api.client.googleapis.javanet.[GoogleNetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.javanet.GoogleNetHttpTransport.html);
    import com.google.api.client.json.gson.[GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html);
    import com.google.api.services.cloudresourcemanager.v3.CloudResourceManager;
    import com.google.api.services.cloudresourcemanager.v3.model.TestIamPermissionsRequest;
    import com.google.api.services.cloudresourcemanager.v3.model.TestIamPermissionsResponse;
    import com.google.api.services.iam.v1.IamScopes;
    import com.google.auth.http.[HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html);
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import java.io.IOException;
    import java.security.GeneralSecurityException;
    import java.util.Arrays;
    import java.util.Collections;
    import java.util.List;
    
    public class TestPermissions {
    
      // Tests if the caller has the listed permissions.
      public static void testPermissions(String projectId) {
        // projectId = "my-project-id"
    
        CloudResourceManager service = null;
        try {
          service = createCloudResourceManagerService();
        } catch (IOException | GeneralSecurityException e) {
          System.out.println("Unable to initialize service: \n" + e.toString());
          return;
        }
    
        List<String> permissionsList =
            Arrays.asList("resourcemanager.projects.get", "resourcemanager.projects.delete");
    
        TestIamPermissionsRequest requestBody =
            new TestIamPermissionsRequest().setPermissions(permissionsList);
        try {
          TestIamPermissionsResponse testIamPermissionsResponse =
              service.projects().testIamPermissions(projectId, requestBody).execute();
    
          System.out.println(
              "Of the permissions listed in the request, the caller has the following: "
                  + testIamPermissionsResponse.getPermissions().toString());
        } catch (IOException e) {
          System.out.println("Unable to test permissions: \n" + e.toString());
        }
      }
    
      public static CloudResourceManager createCloudResourceManagerService()
          throws IOException, GeneralSecurityException {
        // Use the Application Default Credentials strategy for authentication. For more info, see:
        // https://cloud.google.com/docs/authentication/production#finding_credentials_automatically
        [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credential =
            [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)()
                .createScoped(Collections.singleton(IamScopes.CLOUD_PLATFORM));
    
        CloudResourceManager service =
            new CloudResourceManager.Builder(
                    [GoogleNetHttpTransport](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.javanet.GoogleNetHttpTransport.html).[newTrustedTransport](https://docs.cloud.google.com/java/docs/reference/google-api-client/latest/com.google.api.client.googleapis.javanet.GoogleNetHttpTransport.html#com_google_api_client_googleapis_javanet_GoogleNetHttpTransport_newTrustedTransport__)(),
                    [GsonFactory](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html).[getDefaultInstance](https://docs.cloud.google.com/java/docs/reference/google-http-client/latest/com.google.api.client.json.gson.GsonFactory.html#com_google_api_client_json_gson_GsonFactory_getDefaultInstance__)(),
                    new [HttpCredentialsAdapter](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.http.HttpCredentialsAdapter.html)(credential))
                .setApplicationName("service-accounts")
                .build();
        return service;
      }
    }

### Python

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

IAM tests the permissions of the service account that you are using to generate credentials. 
    
    
    def test_permissions(project_id: str) -> List[str]:
        """Tests IAM permissions of currently authenticated user to a project."""
    
        projects_client = resourcemanager_v3.ProjectsClient()
        if not project_id.startswith("projects/"):
            project_id = "projects/" + project_id
    
        owned_permissions = projects_client.test_iam_permissions(
            resource=project_id,
            permissions=["resourcemanager.projects.get", "resourcemanager.projects.delete"],
        ).permissions
    
        print("Currently authenticated user has following permissions:", owned_permissions)
        return owned_permissions

### REST

In this example, the user has an IAM role that allows them to get information about a project, but not to delete projects.

The Resource Manager API's `[projects.testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/testIamPermissions)` method accepts a list of permissions and tests which of the permissions a principal has. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.



HTTP method and URL: 
    
    
    POST https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:testIamPermissions

Request JSON body: 
    
    
    {
      "permissions":  [
        "resourcemanager.projects.get",
        "resourcemanager.projects.delete"
      ]
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:testIamPermissions"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID:testIamPermissions" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/testIamPermissions). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "permissions": [
        "resourcemanager.projects.get"
      ]
    }
    

## What's next

Learn how to [grant, change, and revoke access to principals](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
