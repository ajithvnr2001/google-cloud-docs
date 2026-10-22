---
url: https://docs.cloud.google.com/iam/docs/samples/iam-create-key/
title: Create a service account key \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:14.438575+00:00
---

# Create a service account key  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-create-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Create a service account key Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates creating a service account key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    return [](std::string const& name) {
      iam::IAMClient client(iam::MakeIAMConnection());
      auto response = client.CreateServiceAccountKey(
          name,
          google::iam::admin::v1::ServiceAccountPrivateKeyType::
              TYPE_GOOGLE_CREDENTIALS_FILE,
          google::iam::admin::v1::ServiceAccountKeyAlgorithm::KEY_ALG_RSA_2048);
      if (!response) throw std::move(response).status();
      std::cout << "ServiceAccountKey successfully created: "
                << response->DebugString() << "\n"
                << "Please save the key in a secure location, as they cannot "
                   "be downloaded later\n";
      return response->name();
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Text;
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.Iam.v1;
    using Google.Apis.Iam.v1.Data;
    
    public partial class ServiceAccountKeys
    {
        public static ServiceAccountKey CreateKey(string serviceAccountEmail)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
    
            var key = service.Projects.ServiceAccounts.Keys.Create(
                new CreateServiceAccountKeyRequest(),
                "projects/-/serviceAccounts/" + serviceAccountEmail)
                .Execute();
    
            // The PrivateKeyData field contains the base64-encoded service account key
            // in JSON format.
            // TODO(Developer): Save the below key (jsonKeyFile) to a secure location.
            //  You cannot download it later.
            byte[] valueBytes = System.Convert.FromBase64String(key.PrivateKeyData);
            string jsonKeyContent = Encoding.UTF8.GetString(valueBytes);
    
            Console.WriteLine("Key created successfully");
            return key;
        }
    }

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/iam/admin/apiv1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	// "encoding/base64"
    	"fmt"
    	"io"
    
    	iam "google.golang.org/api/iam/v1"
    )
    
    // createKey creates a service account key.
    func createKey(w io.Writer, serviceAccountEmail string) (*iam.ServiceAccountKey, error) {
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	resource := "projects/-/serviceAccounts/" + serviceAccountEmail
    	request := &iam.CreateServiceAccountKeyRequest{}
    	key, err := service.Projects.ServiceAccounts.Keys.Create(resource, request).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Projects.ServiceAccounts.Keys.Create: %w", err)
    	}
    	// The PrivateKeyData field contains the base64-encoded service account key
    	// in JSON format.
    	// TODO(Developer): Save the below key (jsonKeyFile) to a secure location.
    	// You cannot download it later.
    	// jsonKeyFile, _ := base64.StdEncoding.DecodeString(key.PrivateKeyData)
    	fmt.Fprintf(w, "Key created successfully")
    	return key, nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.gson.Gson;
    import com.google.iam.admin.v1.[CreateServiceAccountKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateServiceAccountKeyRequest.html);
    import com.google.iam.admin.v1.[ServiceAccountKey](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountKey.html);
    import java.io.IOException;
    
    public class CreateServiceAccountKey {
    
      public static void main(String[] args) throws IOException {
        // TODO(Developer): Replace the below variables before running.
        String projectId = "your-project-id";
        String serviceAccountName = "your-service-account-name";
    
        [ServiceAccountKey](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountKey.html) key = createKey(projectId, serviceAccountName);
        Gson gson = new Gson();
    
        // System.out.println("Service account key: " + gson.toJson(key));
      }
    
      // Creates a key for a service account.
      public static [ServiceAccountKey](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountKey.html) createKey(String projectId, String accountName)
              throws IOException {
        String email = String.format("%s@%s.iam.gserviceaccount.com", accountName, projectId);
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          [CreateServiceAccountKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateServiceAccountKeyRequest.html) req = [CreateServiceAccountKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.CreateServiceAccountKeyRequest.html).newBuilder()
                  .setName(String.format("projects/%s/serviceAccounts/%s", projectId, email))
                  .build();
          [ServiceAccountKey](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountKey.html) createdKey = iamClient.createServiceAccountKey(req);
          System.out.println("Key created successfully");
    
          return createdKey;
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import iam_admin_v1
    from google.cloud.iam_admin_v1 import types
    
    
    def create_key(project_id: str, account: str) -> types.ServiceAccountKey:
        """
        Creates a key for a service account.
    
        project_id: ID or number of the Google Cloud project you want to use.
        account: ID or email which is unique identifier of the service account.
        """
    
        iam_admin_client = iam_admin_v1.IAMClient()
        request = types.CreateServiceAccountKeyRequest()
        request.name = f"projects/{project_id}/serviceAccounts/{account}"
    
        key = iam_admin_client.create_service_account_key(request=request)
    
        # The private_key_data field contains the stringified service account key
        # in JSON format. You cannot download it again later.
        # If you want to get the value, you can do it in a following way:
        # import json
        # json_key_data = json.loads(key.private_key_data)
        # key_id = json_key_data["private_key_id"]
    
        return key

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
