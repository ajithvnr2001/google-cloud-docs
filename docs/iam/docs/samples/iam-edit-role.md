---
url: https://docs.cloud.google.com/iam/docs/samples/iam-edit-role/
title: Edit a custom role \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:12.279621+00:00
---

# Edit a custom role  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-edit-role/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Edit a custom role Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates editing a custom role.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& name, std::string const& title) {
      iam::IAMClient client(iam::MakeIAMConnection());
      google::iam::admin::v1::UpdateRoleRequest request;
      request.set_name(name);
      google::iam::admin::v1::Role role;
      role.set_title(title);
      google::protobuf::FieldMask update_mask;
      *update_mask.add_paths() = "title";
      *request.mutable_role() = role;
      *request.mutable_update_mask() = update_mask;
      auto response = client.UpdateRole(request);
      if (!response) throw std::move(response).status();
      std::cout << "Role successfully updated: " << response->DebugString()
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
        public static Role EditRole(string name, string projectId, string newTitle,
            string newDescription, IList<string> newPermissions, string newStage)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
            // First, get a Role using List() or Get().
            string resource = $"projects/{projectId}/roles/{name}";
            var role = service.Projects.Roles.Get(resource).Execute();
            // Then you can update its fields.
            role.Title = newTitle;
            role.Description = newDescription;
            role.IncludedPermissions = newPermissions;
            role.Stage = newStage;
            role = service.Projects.Roles.Patch(role, resource).Execute();
            Console.WriteLine("Updated role: " + role.Name);
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
    
    // editRole modifies a custom role.
    func editRole(w io.Writer, projectID, name, newTitle, newDescription, newStage string, newPermissions []string) (*iam.Role, error) {
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	resource := "projects/" + projectID + "/roles/" + name
    	role, err := service.Projects.Roles.Get(resource).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Projects.Roles.Get: %w", err)
    	}
    	role.Title = newTitle
    	role.Description = newDescription
    	role.IncludedPermissions = newPermissions
    	role.Stage = newStage
    	role, err = service.Projects.Roles.Patch(resource, role).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Projects.Roles.Patch: %w", err)
    	}
    	fmt.Fprintf(w, "Updated role: %v", role.Name)
    	return role, nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html);
    import com.google.iam.admin.v1.[Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html).[RoleLaunchStage](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.RoleLaunchStage.html);
    import com.google.iam.admin.v1.[UpdateRoleRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UpdateRoleRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    /** Edit role metadata. Specifically, update description and launch stage. */
    public class EditRole {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // Role ID must point to an existing role.
        String projectId = "your-project-id";
        String roleId = "a unique identifier (e.g. testViewer)";
        String description = "a new description of the role";
    
        editRole(projectId, roleId, description);
      }
    
      public static void editRole(String projectId, String roleId, String description)
          throws IOException {
        String roleName = "projects/" + projectId + "/roles/" + roleId;
        [Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html).Builder roleBuilder =
            [Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html).newBuilder()
                .setName(roleName)
                .setDescription(description)
                // See launch stage enums at
                // https://cloud.google.com/iam/docs/reference/rpc/google.iam.admin.v1#rolelaunchstage
                .setStage([RoleLaunchStage](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.RoleLaunchStage.html).GA);
        [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html) fieldMask = [FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("description").[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("stage").build();
        [UpdateRoleRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UpdateRoleRequest.html) updateRoleRequest =
            [UpdateRoleRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.UpdateRoleRequest.html).newBuilder()
                .setName(roleName)
                .setRole(roleBuilder)
                .setUpdateMask(fieldMask)
                .build();
    
        // Initialize client for sending requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          [Role](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.Role.html) result = iamClient.updateRole(updateRoleRequest);
          System.out.println("Edited role:\n" + result);
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.exceptions import NotFound
    from google.cloud.iam_admin_v1 import [IAMClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html), [Role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.html), [UpdateRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UpdateRoleRequest.html)
    
    from snippets.get_role import get_role
    
    
    def edit_role(role: Role) -> Role:
        """Edits an existing IAM role in a GCP project.
    
        Args:
            role: google.cloud.iam_admin_v1.Role object to be updated
    
        Returns: Updated google.cloud.iam_admin_v1.Role object
        """
        client = IAMClient()
        request = UpdateRoleRequest(name=role.name, role=role)
        try:
            role = client.[update_role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_update_role)(request)
            print(f"Edited role: {role.name}: {role}")
            return role
        except NotFound:
            print(f"Role [{role.name}] not found, take some actions")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
