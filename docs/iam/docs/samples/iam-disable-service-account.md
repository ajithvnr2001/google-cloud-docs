---
url: https://docs.cloud.google.com/iam/docs/samples/iam-disable-service-account/
title: Disable a service account \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:30.580830+00:00
---

# Disable a service account  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-disable-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Disable a service account Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates disabling a service account.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Disable and enable service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& name) {
      iam::IAMClient client(iam::MakeIAMConnection());
      google::iam::admin::v1::DisableServiceAccountRequest request;
      request.set_name(name);
      auto response = client.DisableServiceAccount(request);
      if (!response.ok()) throw std::runtime_error(response.message());
      std::cout << "ServiceAccount successfully disabled.\n";
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.Iam.v1;
    using Google.Apis.Iam.v1.Data;
    
    public partial class ServiceAccounts
    {
        public static void DisableServiceAccount(string email)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
    
            var request = new DisableServiceAccountRequest();
    
            string resource = "projects/-/serviceAccounts/" + email;
            service.Projects.ServiceAccounts.Disable(request, resource).Execute();
            Console.WriteLine("Disabled service account: " + email);
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
    
    // disableServiceAccount disables a service account.
    func disableServiceAccount(w io.Writer, email string) error {
    	// email:= service-account@your-project.iam.gserviceaccount.com
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	request := &iam.DisableServiceAccountRequest{}
    	_, err = service.Projects.ServiceAccounts.Disable("projects/-/serviceAccounts/"+email, request).Do()
    	if err != nil {
    		return fmt.Errorf("Projects.ServiceAccounts.Disable: %w", err)
    	}
    	fmt.Fprintf(w, "Disabled service account: %v", email)
    	return nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[DisableServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.DisableServiceAccountRequest.html);
    import java.io.IOException;
    
    public class DisableServiceAccount {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Replace the below variables before running.
        String projectId = "your-project-id";
        String serviceAccountName = "your-service-account-name";
    
        disableServiceAccount(projectId, serviceAccountName);
      }
    
      // Disables a service account.
      public static void disableServiceAccount(String projectId, String accountName)
              throws IOException {
        String email = String.format("%s@%s.iam.gserviceaccount.com", accountName, projectId);
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          iamClient.disableServiceAccount([DisableServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.DisableServiceAccountRequest.html).newBuilder()
                  .setName(String.format("projects/%s/serviceAccounts/%s", projectId, email))
                  .build());
    
          System.out.println("Disabled service account: " + accountName);
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import time
    
    from google.cloud import iam_admin_v1
    from google.cloud.iam_admin_v1 import types
    
    
    def disable_service_account(project_id: str, account: str) -> types.ServiceAccount:
        """Disables a service account.
    
        project_id: ID or number of the Google Cloud project you want to use.
        account: ID or email which is unique identifier of the service account.
        """
    
        iam_admin_client = iam_admin_v1.IAMClient()
        request = types.DisableServiceAccountRequest()
        name = f"projects/{project_id}/serviceAccounts/{account}"
        request.name = name
    
        iam_admin_client.disable_service_account(request=request)
        time.sleep(5)  # waiting to make sure changes applied
    
        get_request = types.GetServiceAccountRequest()
        get_request.name = name
    
        service_account = iam_admin_client.get_service_account(request=get_request)
        if service_account.disabled:
            print(f"Disabled service account: {account}")
        return service_account

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
