---
url: https://docs.cloud.google.com/storage/docs/samples/storage-create-hmac-key/
title: Create a service account HMAC key \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:30.218934+00:00
---

# Create a service account HMAC key  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-create-hmac-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Create a service account HMAC key Stay organized with collections  Save and categorize content based on your preferences. 

Create a service account HMAC key.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage HMAC keys for service accounts](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    return [](gcs::Client client, std::string const& service_account_email) {
      StatusOr<std::pair<gcs::HmacKeyMetadata, std::string>> key_info =
          client.CreateHmacKey(service_account_email);
      if (!key_info) throw std::move(key_info).status();
    
      std::cout << "The base64 encoded secret is: " << key_info->second
                << "\nDo not miss that secret, there is no API to recover it."
                << "\nThe HMAC key metadata is: " << key_info->first << "\n";
      return key_info->first.access_id();
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class CreateHmacKeySample
    {
        public HmacKey CreateHmacKey(
            string projectId = "your-project-id",
            string serviceAccountEmail = "dev@iam.gserviceaccount.com")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var key = storage.CreateHmacKey(projectId, serviceAccountEmail);
    
            var secret = key.Secret;
            var metadata = key.Metadata;
    
            Console.WriteLine($"The Base64 encoded secret is: {secret}");
            Console.WriteLine("Make sure to save that secret, there's no API to recover it.");
            Console.WriteLine("The HMAC key metadata is:");
            Console.WriteLine($"ID: {metadata.Id}");
            Console.WriteLine($"Access ID: {metadata.AccessId}");
            Console.WriteLine($"Project ID: {metadata.ProjectId}");
            Console.WriteLine($"Service Account Email: {metadata.ServiceAccountEmail}");
            Console.WriteLine($"State: {metadata.State}");
            Console.WriteLine($"Time Created: {metadata.TimeCreated}");
            Console.WriteLine($"Time Updated: {metadata.Updated}");
            Console.WriteLine($"ETag: {metadata.ETag}");
            return key;
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
    
    // createHMACKey creates a new HMAC key using the given project and service account.
    func createHMACKey(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectID string, serviceAccountEmail string) (*storage.[HMACKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_HMACKey), error) {
    	ctx := context.Background()
    
    	// Initialize client.
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close() // Closing the client safely cleans up background resources.
    
    	ctx, cancel := context.WithTimeout(ctx, time.Minute)
    	defer cancel()
    	key, err := client.[CreateHMACKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_CreateHMACKey)(ctx, projectID, serviceAccountEmail)
    	if err != nil {
    		return nil, fmt.Errorf("CreateHMACKey: %w", err)
    	}
    
    	fmt.Fprintf(w, "%s\n", key)
    	fmt.Fprintf(w, "The base64 encoded secret is %s\n", key.Secret)
    	fmt.Fprintln(w, "Do not miss that secret, there is no API to recover it.")
    	fmt.Fprintln(w, "The HMAC key metadata is")
    	fmt.Fprintf(w, "%+v", key)
    
    	return key, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[HmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html);
    import com.google.cloud.storage.[ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ServiceAccount.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.Date;
    
    public class CreateHmacKey {
      public static void createHmacKey(String serviceAccountEmail, String projectId)
          throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
    
        // The service account email for which the new HMAC key will be created.
        // String serviceAccountEmail = "service-account@iam.gserviceaccount.com";
    
        // The ID of the project to which the service account belongs.
        // String projectId = "project-id";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        [ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ServiceAccount.html) account = [ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ServiceAccount.html).of(serviceAccountEmail);
        [HmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html) hmacKey =
            storage.[createHmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_createHmacKey_com_google_cloud_storage_ServiceAccount_com_google_cloud_storage_Storage_CreateHmacKeyOption____)(account, Storage.CreateHmacKeyOption.projectId(projectId));
    
        String secret = hmacKey.[getSecretKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html#com_google_cloud_storage_HmacKey_getSecretKey__)();
        [HmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html).[HmacKeyMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.HmacKeyMetadata.html) metadata = hmacKey.[getMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html#com_google_cloud_storage_HmacKey_getMetadata__)();
    
        System.out.println("The Base64 encoded secret is: " + secret);
        System.out.println("Do not lose that secret, there is no API to recover it.");
        System.out.println("The HMAC key metadata is:");
        System.out.println("ID: " + metadata.getId());
        System.out.println("Access ID: " + metadata.[getAccessId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.HmacKeyMetadata.html#com_google_cloud_storage_HmacKey_HmacKeyMetadata_getAccessId__)());
        System.out.println("Project ID: " + metadata.getProjectId());
        System.out.println("Service Account Email: " + metadata.getServiceAccount().getEmail());
        System.out.println("State: " + metadata.getState().toString());
        System.out.println("Time Created: " + new Date(metadata.getCreateTime()).toString());
        System.out.println("Time Updated: " + new Date(metadata.getUpdateTime()).toString());
        System.out.println("ETag: " + metadata.getEtag());
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The service account email for which the new HMAC key will be created
    // const serviceAccountEmail = 'service-account@iam.gserviceaccount.com';
    
    // The ID of the project to which the service account belongs
    // const projectId = 'project-id';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Create HMAC SA Key
    async function createHmacKey() {
      const [hmacKey, secret] = await storage.[createHmacKey](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html)(serviceAccountEmail, {
        projectId,
      });
    
      console.log(`The base64 encoded secret is: ${secret}`);
      console.log('Do not miss that secret, there is no API to recover it.');
      console.log('The HMAC key metadata is:');
      for (const [key, value] of Object.entries([hmacKey](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html).metadata)) {
        console.log(`${key}: ${value}`);
      }
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Create a new HMAC key.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     *        (e.g. 'my-project-id')
     * @param string $serviceAccountEmail Service account email to associate with the new HMAC key.
     *        (e.g. 'service-account@iam.gserviceaccount.com')
     */
    function create_hmac_key(string $projectId, string $serviceAccountEmail): void
    {
        $storage = new StorageClient();
        // By default createHmacKey will use the projectId used by StorageClient().
        $hmacKeyCreated = $storage->createHmacKey($serviceAccountEmail, ['projectId' => $projectId]);
    
        printf('The base64 encoded secret is: %s' . PHP_EOL, $hmacKeyCreated->secret());
        print('Do not miss that secret, there is no API to recover it.' . PHP_EOL);
        printf('HMAC key Metadata: %s' . PHP_EOL, print_r($hmacKeyCreated->hmacKey()->info(), true));
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def create_key(project_id, service_account_email):
        """
        Create a new HMAC key using the given project and service account.
        """
        # project_id = 'Your Google Cloud project ID'
        # service_account_email = 'Service account used to generate the HMAC key'
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(project=project_id)
    
        hmac_key, secret = storage_client.[create_hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_create_hmac_key)(
            service_account_email=service_account_email, project_id=project_id
        )
    
        print(f"The base64 encoded secret is {secret}")
        print("Do not miss that secret, there is no API to recover it.")
        print("The HMAC key metadata is:")
        print(f"Service Account Email: {[hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).[service_account_email](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_service_account_email)}")
        print(f"Key ID: {[hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).id}")
        print(f"Access ID: {[hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).[access_id](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_access_id)}")
        print(f"Project ID: {[hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).[project](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_project)}")
        print(f"State: {[hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state)}")
        print(f"Created At: {[hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).time_created}")
        print(f"Updated At: {[hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).updated}")
        print(f"Etag: {[hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).etag}")
        return hmac_key
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def create_hmac_key service_account_email:
      # The service account email used to generate an HMAC key
      # service_account_email = "service-my-project-number@gs-project-accounts.iam.gserviceaccount.com"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      # By default Storage#create_hmac_key uses the Storage client project_id
      hmac_key = storage.[create_hmac_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project.html) service_account_email
    
      puts "The base64 encoded secret is: #{hmac_key.[secret](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-HmacKey.html)}"
      puts "Do not miss that secret, there is no API to recover it."
      puts "\nThe HMAC key metadata is:"
      puts "Key ID:                #{hmac_key.id}"
      puts "Service Account Email: #{hmac_key.service_account_email}"
      puts "Access ID:             #{hmac_key.[access_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-HmacKey.html)}"
      puts "Project ID:            #{hmac_key.project_id}"
      puts "Active:                #{hmac_key.[active?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-HmacKey.html)}"
      puts "Created At:            #{hmac_key.created_at}"
      puts "Updated At:            #{hmac_key.updated_at}"
      puts "Etag:                  #{hmac_key.etag}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
