---
url: https://docs.cloud.google.com/storage/docs/samples/storage-list-hmac-keys/
title: List HMAC keys \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:32:29.745870+00:00
---

# List HMAC keys  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-list-hmac-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  List HMAC keys Stay organized with collections  Save and categorize content based on your preferences. 

List the HMAC keys in a project.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage HMAC keys for service accounts](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client) {
      int count = 0;
      gcs::ListHmacKeysReader hmac_keys_list = client.ListHmacKeys();
      for (auto& key : hmac_keys_list) {
        if (!key) throw std::move(key).status();
    
        std::cout << "service_account_email = " << key->service_account_email()
                  << "\naccess_id = " << key->access_id() << "\n";
        ++count;
      }
      if (count == 0) {
        std::cout << "No HMAC keys in default project\n";
      }
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class ListHmacKeysSample
    {
        public IEnumerable<HmacKeyMetadata> ListHmacKeys(string projectId = "your-project-id")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var keys = storage.ListHmacKeys(projectId);
    
            foreach (var key in keys)
            {
                Console.WriteLine($"Service Account Email: {key.ServiceAccountEmail}");
                Console.WriteLine($"Access ID: {key.AccessId}");
            }
            return keys;
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
    	"google.golang.org/api/iterator"
    )
    
    // listHMACKeys lists all HMAC keys associated with the project.
    func listHMACKeys(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectID string) ([]*storage.[HMACKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_HMACKey), error) {
    	ctx := context.Background()
    
    	// Initialize client.
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close() // Closing the client safely cleans up background resources.
    
    	ctx, cancel := context.WithTimeout(ctx, time.Minute)
    	defer cancel()
    	iter := client.[ListHMACKeys](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_ListHMACKeys)(ctx, projectID)
    	var keys []*storage.[HMACKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_HMACKey)
    	for {
    		key, err := iter.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return nil, fmt.Errorf("ListHMACKeys: %w", err)
    		}
    		fmt.Fprintf(w, "Service Account Email: %s\n", key.ServiceAccountEmail)
    		fmt.Fprintf(w, "Access ID: %s\n", key.AccessID)
    
    		keys = append(keys, key)
    	}
    
    	return keys, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.storage.[HmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class ListHmacKeys {
      public static void listHmacKeys(String projectId) throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The ID of the project to which the service account belongs.
        // String projectId = "project-id";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        Page<HmacKey.[HmacKeyMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.HmacKeyMetadata.html)> page =
            storage.[listHmacKeys](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_listHmacKeys_com_google_cloud_storage_Storage_ListHmacKeysOption____)(Storage.ListHmacKeysOption.projectId(projectId));
    
        for ([HmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html).[HmacKeyMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.HmacKeyMetadata.html) metadata : page.iterateAll()) {
          System.out.println("Service Account Email: " + metadata.getServiceAccount().getEmail());
          System.out.println("Access ID: " + metadata.[getAccessId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.HmacKeyMetadata.html#com_google_cloud_storage_HmacKey_HmacKeyMetadata_getAccessId__)());
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of the project to which the service account belongs
    // const projectId = 'project-id';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // List HMAC SA Keys' Metadata
    async function listHmacKeys() {
      const [hmacKeys] = await storage.[getHmacKeys](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html)({projectId});
    
      // hmacKeys is an array of HmacKey objects.
      for (const hmacKey of hmacKeys) {
        console.log(
          `Service Account Email: ${[hmacKey](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html).metadata.serviceAccountEmail}`
        );
        console.log(`Access Id: ${[hmacKey](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html).metadata.[accessId](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/hmackeymetadata.html)}`);
      }
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * List HMAC keys.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     *        (e.g. 'my-project-id')
     */
    function list_hmac_keys(string $projectId): void
    {
        $storage = new StorageClient();
        // By default hmacKeys will use the projectId used by StorageClient() to list HMAC Keys.
        $hmacKeys = $storage->hmacKeys(['projectId' => $projectId]);
    
        printf('HMAC Key\'s:' . PHP_EOL);
        foreach ($hmacKeys as $hmacKey) {
            printf('Service Account Email: %s' . PHP_EOL, $hmacKey->info()['serviceAccountEmail']);
            printf('Access Id: %s' . PHP_EOL, $hmacKey->info()['accessId']);
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def list_keys(project_id):
        """
        List all HMAC keys associated with the project.
        """
        # project_id = "Your Google Cloud project ID"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(project=project_id)
        hmac_keys = storage_client.[list_hmac_keys](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_list_hmac_keys)(project_id=project_id)
        print("HMAC Keys:")
        for hmac_key in hmac_keys:
            print(
                f"Service Account Email: {[hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).[service_account_email](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_service_account_email)}"
            )
            print(f"Access ID: {[hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).[access_id](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_access_id)}")
        return hmac_keys
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def list_hmac_keys
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      # By default Storage#hmac_keys uses the Storage client project_id
      hmac_keys = storage.[hmac_keys](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project.html)
    
      puts "HMAC Keys:"
      hmac_keys.all do |hmac_key|
        puts "Service Account Email: #{hmac_key.service_account_email}"
        puts "Access ID: #{hmac_key.[access_id](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-HmacKey.html)}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
