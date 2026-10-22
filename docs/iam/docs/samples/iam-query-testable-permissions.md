---
url: https://docs.cloud.google.com/iam/docs/samples/iam-query-testable-permissions/
title: Query testable permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:43.513670+00:00
---

# Query testable permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-query-testable-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Query testable permissions Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates listing the permissions that are valid for a resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& resource) {
      iam::IAMClient client(iam::MakeIAMConnection());
      google::iam::admin::v1::QueryTestablePermissionsRequest request;
      request.set_full_resource_name(resource);
      int count = 0;
      for (auto& permission : client.QueryTestablePermissions(request)) {
        if (!permission) throw std::move(permission).status();
        std::cout << "Permission successfully retrieved: " << permission->name()
                  << "\n";
        ++count;
      }
      if (count == 0) {
        std::cout << "No testable permissions found in resource: " << resource
                  << "\n";
      }
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
        public static IList<Permission> QueryTestablePermissions(
            string fullResourceName)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
    
            var request = new QueryTestablePermissionsRequest
            {
                FullResourceName = fullResourceName
            };
            var response = service.Permissions.QueryTestablePermissions(request)
                .Execute();
            foreach (var p in response.Permissions)
            {
                Console.WriteLine(p.Name);
            }
            return response.Permissions;
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
    
    // queryTestablePermissions lists testable permissions on a resource.
    func queryTestablePermissions(w io.Writer, fullResourceName string) ([]*iam.Permission, error) {
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	request := &iam.QueryTestablePermissionsRequest{
    		FullResourceName: fullResourceName,
    	}
    	response, err := service.Permissions.QueryTestablePermissions(request).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Permissions.QueryTestablePermissions: %w", err)
    	}
    	for _, p := range response.Permissions {
    		fmt.Fprintf(w, "Found permissions: %v", p.Name)
    	}
    	return response.Permissions, nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).[QueryTestablePermissionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.QueryTestablePermissionsPagedResponse.html);
    import com.google.iam.admin.v1.[QueryTestablePermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.QueryTestablePermissionsRequest.html);
    import java.io.IOException;
    
    /** View available permissions in a project. */
    public class QueryTestablePermissions {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variable before running the sample.
        // Full resource names can take one of the following forms:
        // cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        // cloudresourcemanager.googleapis.com/organizations/NUMERIC_ID
        String fullResourceName = "your-full-resource-name";
    
        queryTestablePermissions(fullResourceName);
      }
    
      public static void queryTestablePermissions(String fullResourceName) throws IOException {
        [QueryTestablePermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.QueryTestablePermissionsRequest.html) queryTestablePermissionsRequest =
            [QueryTestablePermissionsRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.QueryTestablePermissionsRequest.html).newBuilder().setFullResourceName(fullResourceName).build();
    
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          [QueryTestablePermissionsPagedResponse](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.QueryTestablePermissionsPagedResponse.html) queryTestablePermissionsPagedResponse =
              iamClient.queryTestablePermissions(queryTestablePermissionsRequest);
          queryTestablePermissionsPagedResponse
              .iterateAll()
              .forEach(permission -> System.out.println(permission.getName()));
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    from typing import List
    
    from google.cloud import [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest)
    from google.iam.v1 import iam_policy_pb2, policy_pb2
    
    
    def query_testable_permissions(
        project_id: str, permissions: List[str]
    ) -> policy_pb2.Policy:
        """Tests IAM permissions of the caller.
    
        project_id: ID or number of the Google Cloud project you want to use.
        permissions: List of permissions to get.
        """
    
        client = [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html)()
        request = iam_policy_pb2.TestIamPermissionsRequest()
        request.resource = f"projects/{project_id}"
        request.permissions.extend(permissions)
    
        permissions_reponse = client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_test_iam_permissions)(request)
        print(permissions_reponse)
        return permissions_reponse.permissions

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
