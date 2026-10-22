---
url: https://docs.cloud.google.com/iam/docs/samples/iam-list-keys/
title: List service account keys \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:11.489758+00:00
---

# List service account keys  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-list-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  List service account keys Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates listing service account keys.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [List and get service account keys](https://docs.cloud.google.com/iam/docs/keys-list-get)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& service_account_name,
       std::vector<std::string> const& key_type_labels) {
      iam::IAMClient client(iam::MakeIAMConnection());
      std::vector<google::iam::admin::v1::ListServiceAccountKeysRequest::KeyType>
          key_types;
      for (auto const& type : key_type_labels) {
        if (type == "USER_MANAGED") {
          key_types.push_back(google::iam::admin::v1::
                                  ListServiceAccountKeysRequest::USER_MANAGED);
        } else if (type == "SYSTEM_MANAGED") {
          key_types.push_back(google::iam::admin::v1::
                                  ListServiceAccountKeysRequest::SYSTEM_MANAGED);
        }
      }
      auto response =
          client.ListServiceAccountKeys(service_account_name, key_types);
      if (!response) throw std::move(response).status();
      std::cout << "ServiceAccountKeys successfully retrieved: "
                << response->DebugString() << "\n";
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.Iam.v1;
    using Google.Apis.Iam.v1.Data;
    
    public partial class ServiceAccountKeys
    {
        public static IList<ServiceAccountKey> ListKeys(string serviceAccountEmail)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
    
            var response = service.Projects.ServiceAccounts.Keys
                .List($"projects/-/serviceAccounts/{serviceAccountEmail}")
                .Execute();
            foreach (ServiceAccountKey key in response.Keys)
            {
                Console.WriteLine("Key: " + key.Name);
            }
            return response.Keys;
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
    
    // listKey lists a service account's keys.
    func listKeys(w io.Writer, serviceAccountEmail string) ([]*iam.ServiceAccountKey, error) {
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	resource := "projects/-/serviceAccounts/" + serviceAccountEmail
    	response, err := service.Projects.ServiceAccounts.Keys.List(resource).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Projects.ServiceAccounts.Keys.List: %w", err)
    	}
    	for _, key := range response.Keys {
    		fmt.Fprintf(w, "Listing key: %v", key.Name)
    	}
    	return response.Keys, nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[ListServiceAccountKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ListServiceAccountKeysRequest.html);
    import com.google.iam.admin.v1.[ServiceAccountKey](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountKey.html);
    import java.io.IOException;
    import java.util.List;
    
    public class ListServiceAccountKeys {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Replace the below variables before running.
        String projectId = "your-project-id";
        String serviceAccountName = "your-service-account-name";
    
        List<ServiceAccountKey> keys = listKeys(projectId, serviceAccountName);
        keys.forEach(key -> System.out.println("Key: " + key.getName()));
      }
    
      // Lists all keys for a service account.
      public static List<ServiceAccountKey> listKeys(String projectId, String accountName)
              throws IOException {
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        String email = String.format("%s@%s.iam.gserviceaccount.com", accountName, projectId);
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          [ListServiceAccountKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ListServiceAccountKeysRequest.html) req = [ListServiceAccountKeysRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ListServiceAccountKeysRequest.html).newBuilder()
                  .setName(String.format("projects/%s/serviceAccounts/%s", projectId, email))
                  .build();
    
          return iamClient.listServiceAccountKeys(req).getKeysList();
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    from google.cloud import iam_admin_v1
    from google.cloud.iam_admin_v1 import types
    
    
    def list_keys(project_id: str, account: str) -> List[iam_admin_v1.ServiceAccountKey]:
        """Lists a key for a service account.
    
        project_id: ID or number of the Google Cloud project you want to use.
        account: ID or email which is unique identifier of the service account.
        """
    
        iam_admin_client = iam_admin_v1.IAMClient()
        request = types.ListServiceAccountKeysRequest()
        request.name = f"projects/{project_id}/serviceAccounts/{account}"
    
        response = iam_admin_client.list_service_account_keys(request=request)
        return response.keys

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
