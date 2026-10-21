---
url: https://docs.cloud.google.com/iam/docs/samples/iam-create-role/
title: Create a custom role \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:09.050459+00:00
---

# Create a custom role  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-create-role/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Create a custom role Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates creating a custom role.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& parent, std::string const& role_id,
       std::vector<std::string> const& included_permissions) {
      iam::IAMClient client(iam::MakeIAMConnection());
      google::iam::admin::v1::CreateRoleRequest request;
      request.set_parent("projects/" + parent);
      request.set_role_id(role_id);
      google::iam::admin::v1::Role role;
      role.set_stage(google::iam::admin::v1::Role::GA);
      for (auto const& permission : included_permissions) {
        *role.add_included_permissions() = permission;
      }
      *request.mutable_role() = role;
      auto response = client.CreateRole(request);
      if (!response) throw std::move(response).status();
      std::cout << "Role successfully created: " << response->DebugString()
                << "\n";
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.Iam.v1;
    using Google.Apis.Iam.v1.Data;
    
    public partial class CustomRoles
    {
        public static Role CreateRole(string name, string projectId, string title,
            string description, IList<string> permissions, string stage)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
    
            var role = new Role
            {
                Title = title,
                Description = description,
                IncludedPermissions = permissions,
                Stage = stage
            };
            var request = new CreateRoleRequest
            {
                Role = role,
                RoleId = name
            };
            role = service.Projects.Roles.Create(request,
                "projects/" + projectId).Execute();
            Console.WriteLine("Created role: " + role.Name);
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
    
    // createRole creates a custom role.
    func createRole(w io.Writer, projectID, name, title, description, stage string, permissions []string) (*iam.Role, error) {
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	request := &iam.CreateRoleRequest{
    		Role: &iam.Role{
    			Title:               title,
    			Description:         description,
    			IncludedPermissions: permissions,
    			Stage:               stage,
    		},
    		RoleId: name,
    	}
    	role, err := service.Projects.Roles.Create("projects/"+projectID, request).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Projects.Roles.Create: %w", err)
    	}
    	fmt.Fprintf(w, "Created role: %v", role.Name)
    	return role, nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[CreateRoleRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateRoleRequest.html);
    import com.google.iam.admin.v1.[Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html);
    import com.google.iam.admin.v1.[Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html).[RoleLaunchStage](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.RoleLaunchStage.html);
    import java.io.IOException;
    import java.util.Arrays;
    
    /** Create role. */
    public class CreateRole {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        String projectId = "your-project-id";
        String roleId = "a unique identifier (e.g. testViewer)";
        String title = "a title for your role (e.g. IAM Role Viewer)";
        String description = "a description of the role";
        Iterable<String> includedPermissions =
            Arrays.asList("roles/iam.roleViewer", "roles/logging.viewer");
    
        createRole(projectId, title, description, includedPermissions, roleId);
      }
    
      public static void createRole(
          String projectId,
          String title,
          String description,
          Iterable<String> includedPermissions,
          String roleId)
          throws IOException {
        [Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html).Builder roleBuilder =
            [Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html).newBuilder()
                .setTitle(title)
                .setDescription(description)
                .[addAllIncludedPermissions](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.Builder.html#com_google_iam_admin_v1_Role_Builder_addAllIncludedPermissions_java_lang_Iterable_java_lang_String__)(includedPermissions)
                // See launch stage enums at
                // https://cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#rolelaunchstage
                .setStage([RoleLaunchStage](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.RoleLaunchStage.html).BETA);
        [CreateRoleRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateRoleRequest.html) createRoleRequest =
            [CreateRoleRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateRoleRequest.html).newBuilder()
                .setParent("projects/" + projectId)
                .[setRoleId](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateRoleRequest.Builder.html#com_google_iam_admin_v1_CreateRoleRequest_Builder_setRoleId_java_lang_String_)(roleId)
                .setRole(roleBuilder)
                .build();
    
        // Initialize client for sending requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          [Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) result = iamClient.createRole(createRoleRequest);
          System.out.println("Created role: " + result.[getName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html#com_google_iam_admin_v1_Role_getName__)());
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List, Optional
    
    from google.api_core.exceptions import AlreadyExists, FailedPrecondition
    from google.cloud.iam_admin_v1 import [CreateRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.CreateRoleRequest.html), [IAMClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html), [Role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.html)
    
    
    def create_role(
        project_id: str, role_id: str, permissions: List[str], title: Optional[str] = None
    ) -> Role:
        """Creates iam role with given parameters.
    
        Args:
            project_id: GCP project id
            role_id: id of GCP iam role
            permissions: list of iam permissions to assign to role. f.e ["iam.roles.get", "iam.roles.list"]
            title: title for iam role. role_id will be used in case of None
    
        Returns: google.cloud.iam_admin_v1.Role object
        """
        client = IAMClient()
    
        parent = f"projects/{project_id}"
    
        request = CreateRoleRequest(
            parent=parent,
            role_id=role_id,
            role=Role(title=title, included_permissions=permissions),
        )
        try:
            role = client.[create_role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_create_role)(request)
            print(f"Created iam role: {role_id}: {role}")
            return role
        except AlreadyExists:
            print(f"Role with id [{role_id}] already exists, take some actions")
        except FailedPrecondition:
            print(
                f"Role with id [{role_id}] already exists and in deleted state, take some actions"
            )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
