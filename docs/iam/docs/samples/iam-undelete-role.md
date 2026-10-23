---
url: https://docs.cloud.google.com/iam/docs/samples/iam-undelete-role/
title: Restore a deleted custom role \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:01.974890+00:00
---

# Restore a deleted custom role  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-undelete-role/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Restore a deleted custom role Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates restoring a custom role.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& name) {
      iam::IAMClient client(iam::MakeIAMConnection());
      google::iam::admin::v1::UndeleteRoleRequest request;
      request.set_name(name);
      auto response = client.UndeleteRole(request);
      if (!response) throw std::move(response).status();
      std::cout << "Role successfully undeleted: " << response->DebugString()
                << "\n";
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.Iam.v1;
    using Google.Apis.Iam.v1.Data;
    
    public partial class CustomRoles
    {
        public static Role UndeleteRole(string name, string projectId)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
    
            string resource = $"projects/{projectId}/roles/{name}";
            var role = service.Projects.Roles.Undelete(
                new UndeleteRoleRequest(), resource).Execute();
            Console.WriteLine("Undeleted role: " + role.Name);
            return role;
        }
    }
    

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/iam/admin/apiv1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	iam "google.golang.org/api/iam/v1"
    )
    
    // undeleteRole restores a deleted custom role.
    func undeleteRole(w io.Writer, projectID, name string) (*iam.Role, error) {
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	resource := "projects/" + projectID + "/roles/" + name
    	request := &iam.UndeleteRoleRequest{}
    	role, err := service.Projects.Roles.Undelete(resource, request).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Projects.Roles.Undelete: %w", err)
    	}
    	fmt.Fprintf(w, "Undeleted role: %v", role.Name)
    	return role, nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html);
    import com.google.iam.admin.v1.[UndeleteRoleRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UndeleteRoleRequest.html);
    import java.io.IOException;
    
    /**
     * Undelete a role to return it to its previous state. Undeleting only works on roles that were
     * deleted in the past 7 days.
     */
    public class UndeleteRole {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // Role ID must point to a role that was deleted in the past 7 days.
        String projectId = "your-project-id";
        String roleId = "a unique identifier (e.g. testViewer)";
    
        undeleteRole(projectId, roleId);
      }
    
      public static void undeleteRole(String projectId, String roleId) throws IOException {
        String roleName = "projects/" + projectId + "/roles/" + roleId;
        [UndeleteRoleRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UndeleteRoleRequest.html) undeleteRoleRequest =
            [UndeleteRoleRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UndeleteRoleRequest.html).newBuilder().setName(roleName).build();
    
        // Initialize client for sending requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          [Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) result = iamClient.undeleteRole(undeleteRoleRequest);
          System.out.println("Undeleted role:\n" + result);
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.exceptions import FailedPrecondition, NotFound
    from google.cloud.iam_admin_v1 import (
        [DeleteRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteRoleRequest.html),
        [IAMClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html),
        [Role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.html),
        [UndeleteRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UndeleteRoleRequest.html),
    )
    def undelete_role(project_id: str, role_id: str) -> Role:
        """Undeleted deleted iam role in GCP project.
    
        Args:
            project_id: GCP project id
            role_id: id of GCP iam role
        """
        client = IAMClient()
        name = f"projects/{project_id}/roles/{role_id}"
        request = UndeleteRoleRequest(name=name)
        try:
            role = client.[undelete_role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_undelete_role)(request)
            print(f"Undeleted role: {role_id}: {role}")
            return role
        except NotFound:
            print(f"Role with id [{role_id}] not found, take some actions")
        except FailedPrecondition as err:
            print(f"Role with id [{role_id}] is not deleted, take some actions)", err)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
