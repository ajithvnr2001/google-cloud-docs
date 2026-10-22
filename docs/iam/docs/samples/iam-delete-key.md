---
url: https://docs.cloud.google.com/iam/docs/samples/iam-delete-key/
title: Delete a service account key \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:41.773044+00:00
---

# Delete a service account key  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-delete-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Delete a service account key Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates deleting a service account key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and delete service account keys](https://docs.cloud.google.com/iam/docs/keys-create-delete)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& name) {
      iam::IAMClient client(iam::MakeIAMConnection());
      auto response = client.DeleteServiceAccountKey(name);
      if (!response.ok()) throw std::runtime_error(response.message());
      std::cout << "ServiceAccountKey successfully deleted.\n";
    }

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.Iam.v1;
    using Google.Apis.Iam.v1.Data;
    
    public partial class ServiceAccountKeys
    {
        public static void DeleteKey(string fullKeyName)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
    
            service.Projects.ServiceAccounts.Keys.Delete(fullKeyName).Execute();
            Console.WriteLine("Deleted key: " + fullKeyName);
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
    
    // deleteKey deletes a service account key.
    func deleteKey(w io.Writer, fullKeyName string) error {
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	_, err = service.Projects.ServiceAccounts.Keys.Delete(fullKeyName).Do()
    	if err != nil {
    		return fmt.Errorf("Projects.ServiceAccounts.Keys.Delete: %w", err)
    	}
    	fmt.Fprintf(w, "Deleted key: %v", fullKeyName)
    	return nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[DeleteServiceAccountKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.DeleteServiceAccountKeyRequest.html);
    import com.google.iam.admin.v1.[KeyName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.KeyName.html);
    import java.io.IOException;
    
    public class DeleteServiceAccountKey {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        String projectId = "your-project-id";
        String serviceAccountName = "my-service-account-name";
        String serviceAccountKeyId = "service-account-key-id";
    
        deleteKey(projectId, serviceAccountName, serviceAccountKeyId);
      }
    
      // Deletes a service account key.
      public static void deleteKey(String projectId, String accountName,
                                   String serviceAccountKeyId) throws IOException {
        //Initialize client that will be used to send requests.
        //This client only needs to be created once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
    
          //Construct the service account email.
          //You can modify the ".iam.gserviceaccount.com" to match the service account name in which
          //you want to delete the key.
          //See, https://cloud.google.com/iam/docs/creating-managing-service-account-keys#deleting
    
          String accountEmail = String.format("%s@%s.iam.gserviceaccount.com", accountName, projectId);
    
          String name = [KeyName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.KeyName.html).of(projectId, accountEmail, serviceAccountKeyId).toString();
    
          [DeleteServiceAccountKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.DeleteServiceAccountKeyRequest.html) request = [DeleteServiceAccountKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.DeleteServiceAccountKeyRequest.html).newBuilder()
                  .setName(name)
                  .build();
    
          // Then you can delete the key
          iamClient.deleteServiceAccountKey(request);
    
          System.out.println("Deleted key: " + serviceAccountKeyId);
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import iam_admin_v1
    from google.cloud.iam_admin_v1 import [types](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.html)
    
    
    def delete_key(project_id: str, account: str, key_id: str) -> None:
        """Deletes a key for a service account.
    
        project_id: ID or number of the Google Cloud project you want to use.
        account: ID or email which is unique identifier of the service account.
        key_id: unique ID of the key.
        """
    
        iam_admin_client = iam_admin_v1.[IAMClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html)()
        request = [types](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.html).[DeleteServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteServiceAccountKeyRequest.html)()
        request.name = f"projects/{project_id}/serviceAccounts/{account}/keys/{key_id}"
    
        iam_admin_client.[delete_service_account_key](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_delete_service_account_key)(request=request)
        print(f"Deleted key: {key_id}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
