---
url: https://docs.cloud.google.com/storage/docs/getting-service-agent/
title: Get the Cloud Storage service agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:51.763385+00:00
---

# Get the Cloud Storage service agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/getting-service-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Get the Cloud Storage service agent Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to find the email address of a project's Cloud Storage service agent, which is a specialized service account created and managed by Cloud Storage. For an overview of Cloud Storage service agents, including when they're created and how they're used, see [Service Accounts for Cloud Storage](https://docs.cloud.google.com/storage/docs/projects#service-accounts). For a general overview of service accounts in Google Cloud, see [Service Accounts](https://docs.cloud.google.com/iam/docs/service-accounts).

## Before you begin

In order to get the required permissions for finding the email address of a project's service agent, ask your administrator to grant you the View Service Accounts (`roles/iam.serviceAccountViewer`) role on the project.

This predefined role contains the `resourcemanager.projects.get` permission, which is required to access the service agent of a project. You can also get this permission with other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles). To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

For instructions on using roles to control access to projects, see [Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Get the email address of a project's Cloud Storage service agent

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Settings** page.  


[Go to Settings](https://console.cloud.google.com/storage/settings)

  2. In the **Project Access** tab, the email address appears in the **Cloud Storage Service Account** section.




### Command line

Use the [`gcloud storage service-agent`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/service-agent) command:
    
    
    gcloud storage service-agent --project=PROJECT_IDENTIFIER

where `PROJECT_IDENTIFIER` is the ID or number of the relevant project. For example, `my-project`.

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client) {
      StatusOr<gcs::ServiceAccount> account = client.GetServiceAccount();
      if (!account) throw std::move(account).status();
    
      std::cout << "The service account details are " << *account << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class GetStorageServiceAccountSample
    {
    	public string GetStorageServiceAccount(string projectId = "your-project-id")
    	{
    		var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    
    		var serviceAccountEmail = storage.GetStorageServiceAccountEmail(projectId);
    
    		Console.WriteLine($"The GCS service account for project {projectId} is: {serviceAccountEmail}.");
    		return serviceAccountEmail;
    	}
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // getServiceAccount gets the default Cloud Storage service account email address.
    func getServiceAccount(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectID string) error {
    	// projectID := "my-project-id"
    
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	serviceAccount, err := client.[ServiceAccount](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_ServiceAccount)(ctx, projectID)
    	if err != nil {
    		return fmt.Errorf("ServiceAccount: %w", err)
    	}
    
    	fmt.Fprintf(w, "The GCS service account for project %v is: %v\n", projectID, serviceAccount)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ServiceAccount.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class GetServiceAccount {
      public static void getServiceAccount(String projectId) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ServiceAccount.html) serviceAccount = storage.[getServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_getServiceAccount_java_lang_String_)(projectId);
        System.out.println(
            "The GCS service account for project " + projectId + " is: " + [serviceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.ListHmacKeysOption.html#com_google_cloud_storage_Storage_ListHmacKeysOption_serviceAccount__org_checkerframework_checker_nullness_qual_NonNull_com_google_cloud_storage_ServiceAccount_).[getEmail](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ServiceAccount.html#com_google_cloud_storage_ServiceAccount_getEmail__)());
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCP project
    // const projectId = 'your-project-id';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)({
      projectId,
    });
    
    async function getServiceAccount() {
      const [serviceAccount] = await storage.[getServiceAccount](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html)();
      console.log(
        `The GCS service account for project ${projectId} is: ${serviceAccount.[emailAddress](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/serviceaccount.html)}`
      );
    }
    
    getServiceAccount().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Get the current service account email.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     *        (e.g. 'my-project-id')
     */
    function get_service_account(string $projectId): void
    {
        $storage = new StorageClient([
            'projectId' => $projectId,
        ]);
    
        $serviceAccountEmail = $storage->getServiceAccount();
    
        printf('The GCS service account email for project %s is %s', $projectId, $serviceAccountEmail);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def get_service_account():
        """Get the service account email"""
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        email = storage_client.[get_service_account_email](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_service_account_email)()
        print(
            f"The GCS service account for project {storage_client.[project](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_project)} is: {email} "
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def get_service_account
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      email = storage.service_account_email
    
      puts "The GCS service account for project #{storage.project_id} is: #{email}"
    end

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the JSON API with a [`GET` serviceAccount](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount/get) request:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://storage.googleapis.com/storage/v1/projects/PROJECT_ID/serviceAccount"

Where `PROJECT_ID` is the ID or number of the relevant project. For example, `my-project`.




## What's next

  * Learn about [service accounts and service agents in Cloud Storage](https://docs.cloud.google.com/storage/docs/projects#service-accounts).
  * [Assign a Cloud Key Management Service encryption key](https://docs.cloud.google.com/storage/docs/encryption/using-customer-managed-keys#service-agent-access) to a service agent.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
