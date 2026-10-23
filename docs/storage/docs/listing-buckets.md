---
url: https://docs.cloud.google.com/storage/docs/listing-buckets/
title: Listing buckets \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:57.162297+00:00
---

# Listing buckets  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/listing-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Listing buckets Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to list the Cloud Storage [buckets](https://docs.cloud.google.com/storage/docs/buckets) in a project, which are ordered in the list lexicographically by name.

## Before you begin

To get the permissions that you need to list buckets, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) IAM role or the Viewer (`roles/viewer`) basic role on the project that contains the buckets you want to list.

For more information about granting roles for projects, see [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

The roles contain the `storage.buckets.list` permission, which is required to list buckets. You can also get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

## List the buckets in a project

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)




Buckets that are part of the selected project appear in the list.

Optionally, use [filtering and sorting](https://docs.cloud.google.com/storage/docs/cloud-console#sort-filter) to limit and organize the results in your list.

### Command line

**Note:** Cloud Shell provisions a temporary virtual machine. If you want to upload objects to Cloud Storage or download objects from Cloud Storage, use a local development environment.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. In your development environment, run the [`gcloud storage ls`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/ls) command:
         
         gcloud storage ls

The response looks like the following example:
         
         gs://BUCKET_NAME1/
           gs://BUCKET_NAME2/
           gs://BUCKET_NAME3/
           ...




### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample lists all available buckets. If a location is temporarily unavailable, the response also includes the names of any buckets that can't be reached.
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client) {
      int count = 0;
      gcs::ListBucketsExtendedReader bucket_list = client.ListBucketsExtended();
      for (auto&& result : bucket_list) {
        if (!result) throw std::move(result).status();
    
        for (auto const& bucket_metadata : result->buckets) {
          std::cout << bucket_metadata.name() << "\n";
          ++count;
        }
        for (auto const& unreachable : result->unreachable) {
          std::cout << "Unreachable location: " << unreachable << "\n";
        }
      }
    
      if (count == 0) {
        std::cout << "No buckets in default project\n";
      }
    }

The following sample lists all buckets. If a location is temporarily unavailable, the service returns an error.
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client) {
      int count = 0;
      gcs::ListBucketsReader bucket_list = client.ListBuckets();
      for (auto&& bucket_metadata : bucket_list) {
        if (!bucket_metadata) throw std::move(bucket_metadata).status();
    
        std::cout << bucket_metadata->name() << "\n";
        ++count;
      }
    
      if (count == 0) {
        std::cout << "No buckets in default project\n";
      }
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample lists all available buckets. If a location is temporarily unavailable, the response also includes the names of any buckets that can't be reached.
    
    
    using [Google.Api.Gax](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.html);
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Linq;
    
    public class ListBucketsWithPartialSuccessSample
    {
        /// <summary>
        /// Lists buckets, returning both the reachable buckets and the resource names of buckets from unreachable locations when specific regions are unreachable.
        /// </summary>
        /// <param name="projectId">The ID of the project to list the buckets.</param>
        public (IReadOnlyList<Bucket> Reachable, IReadOnlyList<string> Unreachable) ListBucketsWithPartialSuccess
            (string projectId = "your-project-id")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var pagedResult = storage.ListBuckets(projectId, options: new [ListBucketsOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.ListBucketsOptions.html)
            {
                ReturnPartialSuccess = true
            });
    
            var reachableBuckets = new List<Bucket>();
            var unreachableBuckets = new List<string>();
    
            foreach (var page in pagedResult.AsRawResponses())
            {
                reachableBuckets.AddRange(page.Items ?? Enumerable.Empty<Bucket>());
                unreachableBuckets.AddRange(page.Unreachable ?? Enumerable.Empty<string>());
            }
    
            Console.WriteLine("Buckets:");
            foreach (var bucket in reachableBuckets)
            {
                Console.WriteLine(bucket.Name);
            }
    
            if (unreachableBuckets.Any())
            {
                Console.WriteLine("The Resource Names of Buckets from Unreachable Locations:");
                foreach (var bucket in unreachableBuckets)
                {
                    Console.WriteLine(bucket);
                }
            }
            return (reachableBuckets, unreachableBuckets);
        }
    }

The following sample lists all buckets. If a location is temporarily unavailable, the service returns an error.
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class ListBucketsSample
    {
        public IEnumerable<Bucket> ListBuckets(string projectId = "your-project-id")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var buckets = storage.ListBuckets(projectId);
            Console.WriteLine("Buckets:");
            foreach (var bucket in buckets)
            {
                Console.WriteLine(bucket.Name);
            }
            return buckets;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample lists all available buckets. If a location is temporarily unavailable, the response also includes the names of any buckets that can't be reached.
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    	"google.golang.org/api/iterator"
    )
    
    // listBucketsPartialSuccess lists buckets in the project. If ReturnPartialSuccess
    // is true, the iterator will return reachable buckets and a list of
    // unreachable bucket resource names.
    func listBucketsPartialSuccess(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectID string) error {
    	// projectID := "my-project-id"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*30)
    	defer cancel()
    
    	it := client.[Buckets](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Buckets)(ctx, projectID)
    	// Enable returning unreachable buckets.
    	it.ReturnPartialSuccess = true
    
    	fmt.Fprintln(w, "Reachable buckets:")
    	for {
    		battrs, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			// Errors here usually indicate a problem with the overall list operation
    			// or connection, such as a network issue, rather than individual
    			// buckets being unreachable. Unreachable buckets due to issues like
    			// regional outages or permission issues are typically reported via the
    			// Unreachable() method below.
    			return err
    		}
    		fmt.Fprintf(w, "- %v\n", battrs.Name)
    	}
    
    	// Retrieve the list of buckets that were unreachable.
    	unreachable := it.[Unreachable](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketIterator_Unreachable)()
    	if len(unreachable) > 0 {
    		fmt.Fprintln(w, "\nUnreachable buckets:")
    		for _, r := range unreachable {
    			fmt.Fprintf(w, "- %v\n", r)
    		}
    	} else {
    		fmt.Fprintln(w, "\nNo unreachable buckets.")
    	}
    
    	return nil
    }
    

The following sample lists all buckets. If a location is temporarily unavailable, the service returns an error.
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    	"google.golang.org/api/iterator"
    )
    
    // listBuckets lists buckets in the project.
    func listBuckets(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), projectID string) ([]string, error) {
    	// projectID := "my-project-id"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*30)
    	defer cancel()
    
    	var buckets []string
    	it := client.[Buckets](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Buckets)(ctx, projectID)
    	for {
    		battrs, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return nil, err
    		}
    		buckets = append(buckets, battrs.Name)
    		fmt.Fprintf(w, "Bucket: %v\n", battrs.Name)
    	}
    	return buckets, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample lists all available buckets. If a location is temporarily unavailable, the response also includes the names of any buckets that can't be reached.
    
    
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class ListBucketsWithPartialSuccess {
      public static void listBucketsWithPartialSuccess(String projectId) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        Page<Bucket> buckets = storage.[list](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_list_com_google_cloud_storage_Storage_BucketListOption____)(Storage.BucketListOption.returnPartialSuccess(true));
    
        // Retrieve the list of buckets that are unreachable due to issues like regional outages or
        // permission issues
        System.out.println("Unreachable buckets: \n");
        for ([Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket : buckets.iterateAll()) {
          if (Boolean.TRUE.equals(bucket.[isUnreachable](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html#com_google_cloud_storage_BucketInfo_isUnreachable__)())) {
            System.out.println(bucket.getName());
          }
        }
      }
    }

The following sample lists all buckets. If a location is temporarily unavailable, the service returns an error.
    
    
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class ListBuckets {
      public static void listBuckets(String projectId) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        Page<Bucket> buckets = storage.[list](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_list_com_google_cloud_storage_Storage_BucketListOption____)();
    
        for ([Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket : buckets.iterateAll()) {
          System.out.println(bucket.getName());
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample lists all available buckets. If a location is temporarily unavailable, the response also includes the names of any buckets that can't be reached.
    
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function listBucketsPartialSuccess() {
      const option = {
        returnPartialSuccess: true,
        maxResults: 5,
      };
      const [buckets, nextQuery, apiResponse] = await storage.[getBuckets](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html)(option);
    
      if (nextQuery && nextQuery.pageToken) {
        console.log(`Next Page Token: ${nextQuery.pageToken}`);
      }
    
      console.log('\nBuckets:');
      buckets.forEach(bucket => {
        if (bucket.unreachable) {
          console.log(`${bucket.name} (unreachable: ${bucket.unreachable})`);
        } else {
          console.log(`${bucket.name}`);
        }
      });
    
      if (apiResponse.unreachable && apiResponse.unreachable.length > 0) {
        console.log('\nUnreachable Buckets:');
        apiResponse.unreachable.forEach(item => {
          console.log(item);
        });
      }
    }
    
    listBucketsPartialSuccess().catch(console.error);

The following sample lists all buckets. If a location is temporarily unavailable, the service returns an error.
    
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function listBuckets() {
      const [buckets] = await storage.[getBuckets](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/storage_2.html)();
    
      console.log('Buckets:');
      buckets.forEach(bucket => {
        console.log(bucket.name);
      });
    }
    
    listBuckets().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample lists all available buckets. If a location is temporarily unavailable, the response also includes the names of any buckets that can't be reached.
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Retrieves a list of buckets while gracefully handling regional downtime.
     */
    function list_buckets_partial_success(): void
    {
        $storage = new StorageClient();
        $options = [ 'returnPartialSuccess' => true ];
        $buckets = $storage->buckets($options);
    
        // Check for unreachable locations first
        // Note: unreachable() returns an array of strings for buckets in unavailable regions
        if ($unreachable = $buckets->unreachable()) {
            foreach ($unreachable as $location) {
                printf('Unreachable Bucket: %s' . PHP_EOL, $location);
            }
        }
    
        // Iterate through the buckets that were successfully retrieved
        foreach ($buckets as $bucket) {
            printf('Bucket: %s' . PHP_EOL, $bucket->name());
        }
    }

The following sample lists all buckets. If a location is temporarily unavailable, the service returns an error.
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * List all Cloud Storage buckets for the current project.
     */
    function list_buckets(): void
    {
        $storage = new StorageClient();
        foreach ($storage->buckets() as $bucket) {
            printf('Bucket: %s' . PHP_EOL, $bucket->name());
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample lists all available buckets. If a location is temporarily unavailable, the response also includes the names of any buckets that can't be reached.
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def list_buckets_with_partial_success():
        """Lists buckets and includes unreachable buckets in the response."""
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        buckets_iterator = storage_client.[list_buckets](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_list_buckets)(return_partial_success=True)
    
        for page in buckets_iterator.pages:
            if page.unreachable:
                print("Unreachable locations in this page:")
                for location in page.unreachable:
                    print(location)
    
            print("Reachable buckets in this page:")
            for bucket in page:
                print(bucket.name)
    
    

The following sample lists all buckets. If a location is temporarily unavailable, the service returns an error.
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def list_buckets():
        """Lists all buckets."""
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        buckets = storage_client.[list_buckets](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_list_buckets)()
    
        for bucket in buckets:
            print(bucket.name)
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample lists all available buckets. If a location is temporarily unavailable, the response also includes the names of any buckets that can't be reached.
    
    
    # Demonstrates listing Google Cloud Storage buckets with support for partial success.
    #
    # This method initializes a Google Cloud Storage client and requests a list of buckets.
    # When `return_partial_success` is true, the API will return available buckets
    # and a list of any buckets that were unreachable.
    #
    # @param return_partial_success_flag [Boolean] Whether to allow partial success from the API.
    #   - true: returns the available buckets and populates `unreachable` with bucket names if any.
    #   - false: throws an error if any buckets are unreachable.
    def list_buckets_with_partial_success return_partial_success_flag:
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket_list = storage.buckets return_partial_success: return_partial_success_flag
    
      puts "Reachable buckets:"
      # limiting the bucket count to be printed to 10 for brevity
      bucket_list.take(10).[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |bucket|
        puts bucket.name
      end
    
      if bucket_list.unreachable
        puts "\nUnreachable buckets:"
        # limiting the bucket count to be printed to 10 for brevity
        bucket_list.unreachable.take(10).[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |unreachable_bucket_name|
          puts unreachable_bucket_name
        end
      end
    end

The following sample lists all buckets. If a location is temporarily unavailable, the service returns an error.
    
    
    def list_buckets
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
      storage.buckets.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |bucket|
        puts bucket.name
      end
    end

### Rust

The following sample lists all buckets. If a location is temporarily unavailable, the service returns an error.
    
    
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, project_id: &str) -> anyhow::Result<()> {
        use google_cloud_gax::paginator::ItemPaginator;
    
        let mut items = client
            .list_buckets()
            .set_parent(format!("projects/{project_id}"))
            .by_item();
        while let Some(bucket) = items.next().await.transpose()? {
            println!("{bucket:?}");
        }
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [request to list buckets](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/list):
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/storage/v1/b?project=PROJECT_IDENTIFIER&returnPartialSuccess=RETURN_PARTIAL_SUCCESS_BOOLEAN"

Replace the following:

     * `PROJECT_IDENTIFIER`: the ID or number of the project containing the buckets you want to list. For example, `my-project`.
     * `RETURN_PARTIAL_SUCCESS_BOOLEAN`: set this value to `true` if you want to return a list of buckets even when some buckets can't be reached because a location is temporarily unavailable. If set to `false`, the request returns a list of buckets only if all locations can be reached, otherwise it returns an error. The default is `false`.



### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`GET` Service](https://docs.cloud.google.com/storage/docs/xml-api/get-service) request:
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "x-goog-project-id: PROJECT_ID" \
           "https://storage.googleapis.com"

Replace `PROJECT_ID` with the ID of the project containing the buckets you want to list. For example, `my-project`.




## What's next

  * [Get information about a bucket's size](https://docs.cloud.google.com/storage/docs/getting-bucket-size).
  * [List the objects in a bucket](https://docs.cloud.google.com/storage/docs/listing-objects).
  * [Move or rename a bucket](https://docs.cloud.google.com/storage/docs/moving-buckets).
  * [Delete a bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets).
  * Learn how to [paginate results](https://docs.cloud.google.com/storage/docs/paginate-results).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
