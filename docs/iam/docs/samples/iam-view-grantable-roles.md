---
url: https://docs.cloud.google.com/iam/docs/samples/iam-view-grantable-roles/
title: View grantable roles \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:58.895557+00:00
---

# View grantable roles  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-view-grantable-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  View grantable roles Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates viewing the roles that you can grant on a specific resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Viewing the grantable roles on resources](https://docs.cloud.google.com/iam/docs/viewing-grantable-roles)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& resource) {
      iam::IAMClient client(iam::MakeIAMConnection());
      int count = 0;
      for (auto& role : client.QueryGrantableRoles(resource)) {
        if (!role) throw std::move(role).status();
        std::cout << "Role successfully retrieved: " << role->name() << "\n";
        ++count;
      }
      if (count == 0) {
        std::cout << "No grantable roles found in resource: " << resource << "\n";
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
        public static IList<Role> ViewGrantableRoles(string fullResourceName)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
    
            var request = new QueryGrantableRolesRequest
            {
                FullResourceName = fullResourceName
            };
            var response = service.Roles.QueryGrantableRoles(request).Execute();
            foreach (var role in response.Roles)
            {
                Console.WriteLine("Title: " + role.Title);
                Console.WriteLine("Name: " + role.Name);
                Console.WriteLine("Description: " + role.Description);
                Console.WriteLine();
            }
            return response.Roles;
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
    
    // viewGrantableRoles lists roles grantable on a resource.
    func viewGrantableRoles(w io.Writer, fullResourceName string) ([]*iam.Role, error) {
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	request := &iam.QueryGrantableRolesRequest{
    		FullResourceName: fullResourceName,
    	}
    	response, err := service.Roles.QueryGrantableRoles(request).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Roles.QueryGrantableRoles: %w", err)
    	}
    	for _, role := range response.Roles {
    		fmt.Fprintf(w, "Found grantable role: %v\n", role.Name)
    	}
    	return response.Roles, err
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    QueryGrantableRolesRequest request = new QueryGrantableRolesRequest();
    request.setFullResourceName(fullResourceName);
    
    QueryGrantableRolesResponse response = service.roles().queryGrantableRoles(request).execute();
    
    for (Role role : response.getRoles()) {
      System.out.println("Title: " + role.getTitle());
      System.out.println("Name: " + role.getName());
      System.out.println("Description: " + role.getDescription());
      System.out.println();
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def view_grantable_roles(full_resource_name: str) -> None:
        roles = (
            service.roles()
            .queryGrantableRoles(body={"fullResourceName": full_resource_name})
            .execute()
        )
    
        for role in roles["roles"]:
            if "title" in role:
                print("Title: " + role["title"])
            print("Name: " + role["name"])
            if "description" in role:
                print("Description: " + role["description"])
            print(" ")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
