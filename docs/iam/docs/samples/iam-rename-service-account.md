---
url: https://docs.cloud.google.com/iam/docs/samples/iam-rename-service-account/
title: Rename a service account \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:11.350853+00:00
---

# Rename a service account  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/samples/iam-rename-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Samples ](https://docs.cloud.google.com/iam/docs/samples)



#  Rename a service account Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates renaming a service account.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [List and edit service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit)



## Code sample

### C++

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/iam/latest). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    namespace iam = ::google::cloud::iam_admin_v1;
    [](std::string const& name, std::string const& display_name) {
      iam::IAMClient client(iam::MakeIAMConnection());
      google::iam::admin::v1::PatchServiceAccountRequest request;
      google::iam::admin::v1::ServiceAccount service_account;
      service_account.set_name(name);
      service_account.set_display_name(display_name);
      google::protobuf::FieldMask update_mask;
      *update_mask.add_paths() = "display_name";
      *request.mutable_service_account() = service_account;
      *request.mutable_update_mask() = update_mask;
      auto response = client.PatchServiceAccount(request);
      if (!response) throw std::move(response).status();
      std::cout << "ServiceAccount successfully updated: "
                << response->DebugString() << "\n";
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
        public static ServiceAccount RenameServiceAccount(string email,
            string newDisplayName)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(IamService.Scope.CloudPlatform);
            var service = new IamService(new IamService.Initializer
            {
                HttpClientInitializer = credential
            });
    
            // First, get a ServiceAccount using List() or Get().
            string resource = "projects/-/serviceAccounts/" + email;
            var serviceAccount = service.Projects.ServiceAccounts.Get(resource)
                .Execute();
            // Then you can update the display name.
            serviceAccount.DisplayName = newDisplayName;
            serviceAccount = service.Projects.ServiceAccounts.Update(
                serviceAccount, resource).Execute();
            Console.WriteLine($"Updated display name for {serviceAccount.Email} " +
                "to: " + serviceAccount.DisplayName);
            return serviceAccount;
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
    
    // renameServiceAccount renames a service account.
    func renameServiceAccount(w io.Writer, email, newDisplayName string) (*iam.ServiceAccount, error) {
    	ctx := context.Background()
    	service, err := iam.NewService(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("iam.NewService: %w", err)
    	}
    
    	// First, get a ServiceAccount using List() or Get().
    	resource := "projects/-/serviceAccounts/" + email
    	serviceAccount, err := service.Projects.ServiceAccounts.Get(resource).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Projects.ServiceAccounts.Get: %w", err)
    	}
    	// Then you can update the display name.
    	serviceAccount.DisplayName = newDisplayName
    	serviceAccount, err = service.Projects.ServiceAccounts.Update(resource, serviceAccount).Do()
    	if err != nil {
    		return nil, fmt.Errorf("Projects.ServiceAccounts.Update: %w", err)
    	}
    
    	fmt.Fprintf(w, "Updated service account: %v", serviceAccount.Email)
    	return serviceAccount, nil
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[GetServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.GetServiceAccountRequest.html);
    import com.google.iam.admin.v1.[PatchServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.PatchServiceAccountRequest.html);
    import com.google.iam.admin.v1.[ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html);
    import com.google.iam.admin.v1.[ServiceAccountName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    
    public class RenameServiceAccount {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        String projectId = "your-project-id";
        String serviceAccountName = "my-service-account-name";
        String displayName = "your-new-display-name";
    
        renameServiceAccount(projectId, serviceAccountName, displayName);
      }
    
      // Changes a service account's display name.
      public static [ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html) renameServiceAccount(String projectId, String serviceAccountName,
                                                        String displayName) throws IOException {
        // Construct the service account email.
        // You can modify the ".iam.gserviceaccount.com" to match the service account name in which
        // you want to delete the key.
        // See, https://cloud.google.com/iam/docs/creating-managing-service-account-keys?hl=en#deleting
        String serviceAccountEmail = serviceAccountName + "@" + projectId + ".iam.gserviceaccount.com";
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          // First, get a service account using getServiceAccount or listServiceAccounts
          [GetServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.GetServiceAccountRequest.html) serviceAccountRequest = [GetServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.GetServiceAccountRequest.html).newBuilder()
                  .setName([ServiceAccountName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html).of(projectId, serviceAccountEmail).toString())
                  .build();
          [ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html) serviceAccount = iamClient.getServiceAccount(serviceAccountRequest);
    
          // You can patch only the `display_name` and `description` fields. You must use
          //  the `update_mask` field to specify which of these fields you want to patch.
          serviceAccount = serviceAccount.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html#com_google_iam_admin_v1_ServiceAccount_toBuilder__)().[setDisplayName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.Builder.html#com_google_iam_admin_v1_ServiceAccount_Builder_setDisplayName_java_lang_String_)(displayName).build();
          [PatchServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.PatchServiceAccountRequest.html) patchServiceAccountRequest =
                  [PatchServiceAccountRequest](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.PatchServiceAccountRequest.html).newBuilder()
                          .setServiceAccount(serviceAccount)
                          .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("display_name").build())
                          .build();
          serviceAccount = iamClient.patchServiceAccount(patchServiceAccountRequest);
    
          System.out.println(
                  "Updated display name for "
                          + serviceAccount.[getName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html#com_google_iam_admin_v1_ServiceAccount_getName__)()
                          + " to: "
                          + serviceAccount.[getDisplayName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccount.html#com_google_iam_admin_v1_ServiceAccount_getDisplayName__)());
          return serviceAccount;
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import iam_admin_v1
    from google.cloud.iam_admin_v1 import [types](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.html)
    
    
    def rename_service_account(
        project_id: str, account: str, new_name: str
    ) -> types.ServiceAccount:
        """Renames service account display name.
    
        project_id: ID or number of the Google Cloud project you want to use.
        account: ID or email which is unique identifier of the service account.
        new_name: New display name of the service account.
        """
    
        iam_admin_client = iam_admin_v1.[IAMClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html)()
    
        get_request = [types](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.html).[GetServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetServiceAccountRequest.html)()
        get_request.name = f"projects/{project_id}/serviceAccounts/{account}"
        service_account = iam_admin_client.[get_service_account](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_get_service_account)(request=get_request)
    
        service_account.display_name = new_name
    
        request = [types](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.html).[PatchServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.PatchServiceAccountRequest.html)()
        request.service_account = service_account
        # You can patch only the `display_name` and `description` fields.
        # You must use the `update_mask` field to specify which of these fields
        # you want to patch.
        # To successfully set update mask you need to transform
        # snake_case field to camelCase.
        # e.g. `display_name` will become `displayName`
        request.update_mask = "displayName"
    
        updated_account = iam_admin_client.[patch_service_account](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_patch_service_account)(request=request)
        return updated_account

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=identityandaccessmanagement). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
