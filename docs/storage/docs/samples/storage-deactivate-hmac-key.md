---
url: https://docs.cloud.google.com/storage/docs/samples/storage-deactivate-hmac-key/
title: Deactivate a service account HMAC key \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:51.143660+00:00
---

# Deactivate a service account HMAC key  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-deactivate-hmac-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Deactivate a service account HMAC key Stay organized with collections  Save and categorize content based on your preferences. 

Updates the state of a service account HMAC key to "Inactive."

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage HMAC keys for service accounts](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& access_id) {
      StatusOr<gcs::HmacKeyMetadata> updated = client.UpdateHmacKey(
          access_id, gcs::HmacKeyMetadata().set_state(
                         gcs::HmacKeyMetadata::state_inactive()));
      if (!updated) throw std::move(updated).status();
    
      if (updated->state() != gcs::HmacKeyMetadata::state_inactive()) {
        throw std::runtime_error("The HMAC key is active, this is unexpected");
      }
      std::cout << "The HMAC key is now inactive\nFull metadata: " << *updated
                << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class DeactivateHmacKeySample
    {
        public HmacKeyMetadata DeactivateHmacKey(
            string projectId = "your-project-id",
            string accessId = "your-access-id")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var metadata = storage.GetHmacKey(projectId, accessId);
            metadata.State = [HmacKeyStates](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.HmacKeyStates.html).[Inactive](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.HmacKeyStates.html#Google_Cloud_Storage_V1_HmacKeyStates_Inactive);
            var updatedMetadata = storage.UpdateHmacKey(metadata);
    
            Console.WriteLine("The HMAC key is now inactive.");
            Console.WriteLine("The HMAC key metadata is:");
            Console.WriteLine($"ID: {updatedMetadata.Id}");
            Console.WriteLine($"Access ID: {updatedMetadata.AccessId}");
            Console.WriteLine($"Project ID: {updatedMetadata.ProjectId}");
            Console.WriteLine($"Service Account Email: {updatedMetadata.ServiceAccountEmail}");
            Console.WriteLine($"State: {updatedMetadata.State}");
            Console.WriteLine($"Time Created: {updatedMetadata.TimeCreated}");
            Console.WriteLine($"Time Updated: {updatedMetadata.Updated}");
            Console.WriteLine($"ETag: {updatedMetadata.ETag}");
            return updatedMetadata;
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
    
    // deactivateHMACKey deactivates the HMAC key with the given access ID.
    func deactivateHMACKey(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), accessID string, projectID string) (*storage.[HMACKey](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_HMACKey), error) {
    	ctx := context.Background()
    
    	// Initialize client.
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close() // Closing the client safely cleans up background resources.
    
    	ctx, cancel := context.WithTimeout(ctx, time.Minute)
    	defer cancel()
    	handle := client.HMACKeyHandle(projectID, accessID)
    	key, err := handle.Update(ctx, storage.[HMACKeyAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_HMACKeyAttrsToUpdate){State: "INACTIVE"})
    	if err != nil {
    		return nil, fmt.Errorf("Update: %w", err)
    	}
    
    	fmt.Fprintln(w, "The HMAC key metadata is:")
    	fmt.Fprintf(w, "%+v", key)
    
    	return key, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[HmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.Date;
    
    public class DeactivateHmacKey {
      public static void deactivateHmacKey(String accessId, String projectId) throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // The access ID of the HMAC key.
        // String accessId = "GOOG0234230X00";
    
        // The ID of the project to which the service account belongs.
        // String projectId = "project-id";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        [HmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html).[HmacKeyMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.HmacKeyMetadata.html) metadata =
            storage.[getHmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_getHmacKey_java_lang_String_com_google_cloud_storage_Storage_GetHmacKeyOption____)(accessId, Storage.GetHmacKeyOption.projectId(projectId));
        [HmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html).[HmacKeyMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.HmacKeyMetadata.html) newMetadata =
            storage.[updateHmacKeyState](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_updateHmacKeyState_com_google_cloud_storage_HmacKey_HmacKeyMetadata_com_google_cloud_storage_HmacKey_HmacKeyState_com_google_cloud_storage_Storage_UpdateHmacKeyOption____)(metadata, [HmacKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.html).HmacKeyState.INACTIVE);
    
        System.out.println("The HMAC key is now inactive.");
        System.out.println("The HMAC key metadata is:");
        System.out.println("ID: " + newMetadata.getId());
        System.out.println("Access ID: " + newMetadata.[getAccessId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HmacKey.HmacKeyMetadata.html#com_google_cloud_storage_HmacKey_HmacKeyMetadata_getAccessId__)());
        System.out.println("Project ID: " + newMetadata.getProjectId());
        System.out.println("Service Account Email: " + newMetadata.getServiceAccount().getEmail());
        System.out.println("State: " + newMetadata.getState().toString());
        System.out.println("Time Created: " + new Date(newMetadata.getCreateTime()).toString());
        System.out.println("Time Updated: " + new Date(newMetadata.getUpdateTime()).toString());
        System.out.println("ETag: " + newMetadata.getEtag());
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
    
    // Deactivate HMAC SA Key
    async function deactivateHmacKey() {
      const hmacKey = storage.[hmacKey](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html)(hmacKeyAccessId, {projectId});
      const [hmacKeyMetadata] = await [hmacKey](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html).setMetadata({state: 'INACTIVE'});
    
      console.log('The HMAC key is now inactive.');
      console.log('The HMAC key metadata is:');
      for (const [key, value] of Object.entries(hmacKeyMetadata)) {
        console.log(`${key}: ${value}`);
      }
    }

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Deactivate an HMAC key.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     *        (e.g. 'my-project-id')
     * @param string $accessId Access ID for an inactive HMAC key.
     *        (e.g. 'GOOG0234230X00')
     */
    function deactivate_hmac_key(string $projectId, string $accessId): void
    {
        $storage = new StorageClient();
        // By default hmacKey will use the projectId used by StorageClient().
        $hmacKey = $storage->hmacKey($accessId, $projectId);
    
        $hmacKey->update('INACTIVE');
    
        print('The HMAC key is now inactive.' . PHP_EOL);
        printf('HMAC key Metadata: %s' . PHP_EOL, print_r($hmacKey->info(), true));
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def deactivate_key(access_id, project_id):
        """
        Deactivate the HMAC key with the given access ID.
        """
        # project_id = "Your Google Cloud project ID"
        # access_id = "ID of an active HMAC key"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(project=project_id)
    
        hmac_key = storage_client.[get_hmac_key_metadata](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_hmac_key_metadata)(
            access_id, project_id=project_id
        )
        [hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).[state](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.HMACKeyMetadata.html#google_cloud_storage_hmac_key_HMACKeyMetadata_state) = "INACTIVE"
        [hmac_key](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.hmac_key.html).update()
    
        print("The HMAC key is now inactive.")
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
    
    
    def deactivate_hmac_key access_id:
      # The access ID of the HMAC key
      # access_id = "GOOG0234230X00"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      # By default Storage#hmac_keys uses the Storage client project_id
      hmac_key = storage.[hmac_key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project.html) access_id
    
      hmac_key.[inactive!](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-HmacKey.html)
    
      puts "The HMAC key is now inactive."
      puts "The HMAC key metadata is:"
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
