---
url: https://docs.cloud.google.com/iam/docs/samples/iam-test-permissions/
title: Test permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:02.403931+00:00
---

# Test permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-test-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Test permissions Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates testing whether the caller has specified permissions.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Test permissions for custom user interfaces](https://docs.cloud.google.com/iam/docs/testing-permissions)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& name, std::vector<std::string> const& permissions) {
      iam::IAMClient client(iam::MakeIAMConnection());
      auto response = client.TestIamPermissions(name, permissions);
      if (!response) throw std::move(response).status();
      std::cout << "Permissions successfully tested: " << response->DebugString()
                << "\n";
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
