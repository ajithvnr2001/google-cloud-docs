---
url: https://docs.cloud.google.com/storage/docs/samples/storage-delete-hmac-key/
title: Delete an HMAC key \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:29.338176+00:00
---

# Delete an HMAC key  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-delete-hmac-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Delete an HMAC key Stay organized with collections  Save and categorize content based on your preferences. 

Delete an HMAC key based on the access ID.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage HMAC keys for service accounts](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](gcs::Client client, std::string const& access_id) {
      google::cloud::Status status = client.DeleteHmacKey(access_id);
      if (!status.ok()) throw std::runtime_error(status.message());
    
      std::cout << "The key is deleted, though it may still appear"
                << " in ListHmacKeys() results.\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class DeleteHmacKeySample
    {
        public void DeleteHmacKey(
            string projectId = "your-project-id",
            string accessId = "your-access-id")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            storage.DeleteHmacKey(projectId, accessId);
    
            Console.WriteLine($"Key {accessId} was deleted.");
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
    
    // deleteHMACKey deletes the HMAC key with the given access ID. Key must have state
    // INACTIVE in order to succeed.
    func deleteHMACKey(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), accessID string, projectID string) error {
    	ctx := context.Background()
    
    	// Initialize client.
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close() // Closing the client safely cleans up background resources.
    
    	handle := client.HMACKeyHandle(projectID, accessID)
    	ctx, cancel := context.WithTimeout(ctx, time.Minute)
    	defer cancel()
    	if err = handle.Delete(ctx); err != nil {
    		return fmt.Errorf("Delete: %w", err)
    	}
    
    	fmt.Fprintln(w, "The key is deleted, though it may still appear in ListHMACKeys results.")
    
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[HmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class DeleteHmacKey {
      public static void deleteHmacKey(String accessId, String projectId) throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
    
        // The access ID of the HMAC key.
        // String accessId = "GOOG0234230X00";
    
        // The ID of the project to which the service account belongs.
        // String projectId = "project-id";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        [HmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html).[HmacKeyMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.HmacKeyMetadata.html) metadata =
            storage.[getHmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_getHmacKey_java_lang_String_com_google_cloud_storage_Storage_GetHmacKeyOption____)(accessId, Storage.GetHmacKeyOption.projectId(projectId));
        storage.[deleteHmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_deleteHmacKey_com_google_cloud_storage_HmacKey_HmacKeyMetadata_com_google_cloud_storage_Storage_DeleteHmacKeyOption____)(metadata);
    
        System.out.println(
            "The key is deleted, though it will still appear in "
                + "getHmacKeys() results if called with showDeletedKey.");
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The access ID of the HMAC key
    // const hmacKeyAccessId = 'GOOG0234230X00';
    
    // The ID of the project to which the service account belongs
    // const projectId = 'project-id';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Delete HMAC SA Key
    async function deleteHmacKey() {
      const hmacKey = storage.[hmacKey](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html)(hmacKeyAccessId, {projectId});
      await [hmacKey](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html).delete();
    
      console.log(
        'The key is deleted, though it may still appear in getHmacKeys() results.'
      );
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Delete an HMAC key.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     *        (e.g. 'my-project-id')
     * @param string $accessId Access ID for an HMAC key. (e.g. 'GOOG0234230X00')
     */
    function delete_hmac_key(string $projectId, string $accessId): void
    {
        $storage = new StorageClient();
        // By default hmacKey will use the projectId used by StorageClient().
        $hmacKey = $storage->hmacKey($accessId, $projectId);
    
        $hmacKey->delete();
        print(
            'The key is deleted, though it may still appear in the results of calls ' .
            'to StorageClient.hmacKeys([\'showDeletedKeys\' => true])' . PHP_EOL
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def delete_key(access_id, project_id):
        """
        Delete the HMAC key with the given access ID. Key must have state INACTIVE
        in order to succeed.
        """
        # project_id = "Your Google Cloud project ID"
        # access_id = "ID of an HMAC key (must be in INACTIVE state)"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(project=project_id)
    
        hmac_key = storage_client.[get_hmac_key_metadata](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_hmac_key_metadata)(
            access_id, project_id=project_id
        )
        [hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).delete()
    
        print(
            "The key is deleted, though it may still appear in list_hmac_keys()"
            " results."
        )
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def delete_hmac_key access_id:
      # The access ID of the HMAC key
      # access_id = "GOOG0234230X00"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      # By default Storage#hmac_keys uses the Storage client project_id
      hmac_key = storage.[hmac_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project.html) access_id
    
      hmac_key.[delete!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-HmacKey.html)
    
      puts "The key is deleted, though it may still appear in Client#hmac_keys results."
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
