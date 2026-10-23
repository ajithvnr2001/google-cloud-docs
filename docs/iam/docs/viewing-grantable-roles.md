---
url: https://docs.cloud.google.com/iam/docs/viewing-grantable-roles/
title: Viewing the grantable roles on resources \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:42.236705+00:00
---

# Viewing the grantable roles on resources  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/viewing-grantable-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Viewing the grantable roles on resources Stay organized with collections  Save and categorize content based on your preferences. 

Before you grant an Identity and Access Management (IAM) role to a user for a resource, you might want to know what roles are available to grant on a particular resource.

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




### Required roles

To get the permissions that you need to list grantable roles, ask your administrator to grant you the [Security Reviewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`) IAM role on the resource that you want to list grantable roles for. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This role contains the `getIamPolicy` permissions for all resource types. To list grantable roles, you need the `getIamPolicy` permission for the resource that you want to list grantable roles for—for example, to list grantable roles for a project, you need the `resourcemanager.projects.getIamPolicy` permission. 

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Understanding what roles are grantable

A role is grantable on or above a resource if it contains any permissions for that resource type. For example, the `storage.admin` role grants permissions to the `storage.buckets.get` and `storage.objects.get` APIs, so it is grantable on the _Storage Buckets_ and _Storage Objects_ resource types.

Roles can also be granted "above" the resource types that their permissions are defined for. In other words, roles for lower-level resources can be granted on a resource that is higher in the Google Cloud resource hierarchy. For example, the `storage.admin` role can also be granted at the project or organization levels, in addition to _Storage Buckets_.

Permissions granted by a role only affect resources at the specified level or below; they do not affect higher-level or peer resources. Additionally, when a role is granted on a resource, only permissions applicable to the given resource are granted, regardless of the role's name, description, or other permissions it contains. For example, assigning the role `resourcemanager.organizationAdmin` (which grants the permission `resourcemanager.projects.list`) to a user on the project level only grants them permissions for that specific project. It will **not** allow them to list or administer all projects in the organization. Similarly, assigning the `compute.admin` role on a specific Compute Engine instance only grants permissions for that instance, not others in the project.

## Listing grantable roles

You can list grantable roles using the Google Cloud console, the Google Cloud CLI, the IAM API, or the IAM client libraries.

The Google Cloud console always lists all grantable roles for the resource you're viewing. The Google Cloud CLI, IAM API, and client libraries only list grantable roles for [enabled APIs](https://docs.cloud.google.com/service-usage/docs/enable-disable#enabling).

### Console

To view grantable roles for a project, folder, or organization, do the following:

  1. In the Google Cloud console, go to the **IAM** page.

[ Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

  2. Click **Select a project** at the top of the page.

  3. Select the project, folder, or organization for which you want to view grantable roles.

  4. Click person_add **Grant access**.

  5. Click **Select a role**. This menu displays all the roles, including any custom roles, that you can grant on this resource.




To view grantable roles for other resource types, do the following:

  1. In the Google Cloud console, go to the page listing the resource for which you want to view grantable roles.

For example, to manage access to a Compute Engine instance, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox next to the resource for which you want to view grantable roles.

  3. Ensure that the info panel is visible. If it is not visible, click **Show info panel**.

  4. Click person_add **Add principal**.

  5. Click **Select a role**. This menu displays all the roles, including any custom roles, that you can grant on this resource.




### gcloud

Use the [`gcloud iam list-grantable-roles`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/list-grantable-roles) command to return a list of all roles that can be applied to a given resource.
    
    
    gcloud iam list-grantable-roles full-resource-name
    

Depending on the desired resource, a large number of roles may be returned. To limit the results, you can specify a [filter expression](https://docs.cloud.google.com/sdk/gcloud/reference/topic/filters).

The output will look something like:
    
    
    description: Full control of all Compute Engine resources.
    name: roles/compute.admin
    title: Compute Admin
    ---
    description: Full control of Compute Engine instance resources.
    name: roles/compute.instanceAdmin
    title: Compute Instance Admin
    
    # Additional results here...
    

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
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

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
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

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
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

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
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

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 
    
    
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
    
    

### REST

The `[roles.queryGrantableRoles](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles/queryGrantableRoles)` method returns a list of all roles grantable on a resource. 

Before using any of the request data, make the following replacements: 

  * `FULL_RESOURCE_NAME`: A URI consisting of the service name and the path to the resource. For examples, see [Full resource names](https://docs.cloud.google.com/iam/docs/full-resource-names).



HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v1/roles:queryGrantableRoles

Request JSON body: 
    
    
    {
      "fullResourceName": "FULL_RESOURCE_NAME"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iam.googleapis.com/v1/roles:queryGrantableRoles"

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
        -Uri "https://iam.googleapis.com/v1/roles:queryGrantableRoles" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/roles/queryGrantableRoles). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "roles": [
        {
          "name": "roles/compute.admin",
          "title": "Compute Admin",
          "description": "Full control of all Compute Engine resources."
        },
        {
          "name": "roles/compute.instanceAdmin",
          "title": "Compute Instance Admin (beta)",
          "description": "Full control of Compute Engine instance resources."
        }
      ]
    }
    

In the examples above, the _full resource name_ is a scheme-less URI consisting of a DNS-compatible API service name and a resource path.

For example, to return all roles grantable on a project, use:
    
    
    //cloudresourcemanager.googleapis.com/projects/project-id
    

Lower-level resources have a more detailed fully qualified name. For example, use the following to return all roles grantable on a Compute Engine instance:
    
    
    //compute.googleapis.com/projects/project-id/zones/zone-name/instances/instance-id
    

## What's next

  * Read about the available [IAM roles](https://docs.cloud.google.com/iam/docs/understanding-roles).
  * Find out how to [choose the most appropriate predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).
  * Learn how to [grant, change, and revoke a principal's access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * See [examples of resource names](https://docs.cloud.google.com/iam/docs/resource-names) for different types of resources.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
