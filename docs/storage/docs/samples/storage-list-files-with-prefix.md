---
url: https://docs.cloud.google.com/storage/docs/samples/storage-list-files-with-prefix/
title: List the objects in a bucket using a prefix filter \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:29.394794+00:00
---

# List the objects in a bucket using a prefix filter  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-list-files-with-prefix/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  List the objects in a bucket using a prefix filter Stay organized with collections  Save and categorize content based on your preferences. 

List the objects in a Cloud Storage bucket using a prefix.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [List objects](https://docs.cloud.google.com/storage/docs/listing-objects)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& bucket_prefix) {
      for (auto&& object_metadata :
           client.ListObjects(bucket_name, gcs::Prefix(bucket_prefix))) {
        if (!object_metadata) throw std::move(object_metadata).status();
    
        std::cout << "bucket_name=" << object_metadata->bucket()
                  << ", object_name=" << object_metadata->name() << "\n";
      }
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class ListFilesWithPrefixSample
    {
        /// <summary>
        /// Prefixes and delimiters can be used to emulate directory listings.
        /// Prefixes can be used to filter objects starting with prefix.
        /// The delimiter argument can be used to restrict the results to only the
        /// objects in the given "directory". Without the delimiter, the entire  tree
        /// under the prefix is returned.
        /// For example, given these objects:
        ///   a/1.txt
        ///   a/b/2.txt
        ///
        /// If you just specify prefix="a/", you'll get back:
        ///   a/1.txt
        ///   a/b/2.txt
        ///
        /// However, if you specify prefix="a/" and delimiter="/", you'll get back:
        ///   a/1.txt
        /// </summary>
        /// <param name="bucketName">The bucket to list the objects from.</param>
        /// <param name="prefix">The prefix to match. Only objects with names that start with this string will
        /// be returned. This parameter may be null or empty, in which case no filtering
        /// is performed.</param>
        /// <param name="delimiter">Used to list in "directory mode". Only objects whose names (aside from the prefix)
        /// do not contain the delimiter will be returned.</param>
        public IEnumerable<Google.Apis.Storage.v1.Data.Object> ListFilesWithPrefix(
            string bucketName = "your-unique-bucket-name",
            string prefix = "your-prefix",
            string delimiter = "your-delimiter")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var options = new [ListObjectsOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.ListObjectsOptions.html) { Delimiter = delimiter };
            var storageObjects = storage.ListObjects(bucketName, prefix, options);
            Console.WriteLine($"Objects in bucket {bucketName} with prefix {prefix}:");
            foreach (var storageObject in storageObjects)
            {
                Console.WriteLine(storageObject.Name);
            }
            return storageObjects;
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
    
    // listFilesWithPrefix lists objects using prefix and delimeter.
    func listFilesWithPrefix(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, prefix, delim string) error {
    	// bucket := "bucket-name"
    	// prefix := "/foo"
    	// delim := "_"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// Prefixes and delimiters can be used to emulate directory listings.
    	// Prefixes can be used to filter objects starting with prefix.
    	// The delimiter argument can be used to restrict the results to only the
    	// objects in the given "directory". Without the delimiter, the entire tree
    	// under the prefix is returned.
    	//
    	// For example, given these blobs:
    	//   /a/1.txt
    	//   /a/b/2.txt
    	//
    	// If you just specify prefix="a/", you'll get back:
    	//   /a/1.txt
    	//   /a/b/2.txt
    	//
    	// However, if you specify prefix="a/" and delim="/", you'll get back:
    	//   /a/1.txt
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	it := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Objects](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Objects)(ctx, &storage.[Query](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Query){
    		Prefix:    prefix,
    		Delimiter: delim,
    	})
    	for {
    		attrs, err := it.Next()
    		if err == iterator.Done {
    			break
    		}
    		if err != nil {
    			return fmt.Errorf("Bucket(%q).Objects(): %w", bucket, err)
    		}
    		fmt.Fprintln(w, attrs.Name)
    	}
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.paging.[Page](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.paging.Page.html);
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class ListObjectsWithPrefix {
      public static void listObjectsWithPrefix(
          String projectId, String bucketName, String directoryPrefix) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The directory prefix to search for
        // String directoryPrefix = "myDirectory/"
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        /**
         * Using the Storage.BlobListOption.currentDirectory() option here causes the results to display
         * in a "directory-like" mode, showing what objects are in the directory you've specified, as
         * well as what other directories exist in that directory. For example, given these blobs:
         *
         * <p>a/1.txt a/b/2.txt a/b/3.txt
         *
         * <p>If you specify prefix = "a/" and don't use Storage.BlobListOption.currentDirectory(),
         * you'll get back:
         *
         * <p>a/1.txt a/b/2.txt a/b/3.txt
         *
         * <p>However, if you specify prefix = "a/" and do use
         * Storage.BlobListOption.currentDirectory(), you'll get back:
         *
         * <p>a/1.txt a/b/
         *
         * <p>Because a/1.txt is the only file in the a/ directory and a/b/ is a directory inside the
         * /a/ directory.
         */
        Page<Blob> blobs =
            storage.[list](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_list_com_google_cloud_storage_Storage_BucketListOption____)(
                bucketName,
                Storage.BlobListOption.prefix(directoryPrefix),
                Storage.BlobListOption.currentDirectory());
    
        for ([Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) blob : blobs.iterateAll()) {
          System.out.println(blob.getName());
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The directory prefix to search for
    // const prefix = 'myDirectory/';
    
    // The delimiter to use
    // const delimiter = '/';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function listFilesByPrefix() {
      /**
       * This can be used to list all blobs in a "folder", e.g. "public/".
       *
       * The delimiter argument can be used to restrict the results to only the
       * "files" in the given "folder". Without the delimiter, the entire tree under
       * the prefix is returned. For example, given these blobs:
       *
       *   /a/1.txt
       *   /a/b/2.txt
       *
       * If you just specify prefix = 'a/', you'll get back:
       *
       *   /a/1.txt
       *   /a/b/2.txt
       *
       * However, if you specify prefix='a/' and delimiter='/', you'll get back:
       *
       *   /a/1.txt
       */
      const options = {
        prefix: prefix,
      };
    
      if (delimiter) {
        options.delimiter = delimiter;
      }
    
      // Lists files in the bucket, filtered by a prefix
      const [files] = await storage.bucket(bucketName).[getFiles](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)(options);
    
      console.log('Files:');
      files.forEach(file => {
        console.log(file.name);
      });
    }
    
    listFilesByPrefix().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * List Cloud Storage bucket objects with specified prefix.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $directoryPrefix the prefix to use in the list objects API call.
     *        (e.g. 'myDirectory/')
     */
    function list_objects_with_prefix(string $bucketName, string $directoryPrefix): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $options = ['prefix' => $directoryPrefix];
        foreach ($bucket->objects($options) as $object) {
            printf('Object: %s' . PHP_EOL, $object->name());
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def list_blobs_with_prefix(bucket_name, prefix, delimiter=None):
        """Lists all the blobs in the bucket that begin with the prefix.
    
        This can be used to list all blobs in a "folder", e.g. "public/".
    
        The delimiter argument can be used to restrict the results to only the
        "files" in the given "folder". Without the delimiter, the entire tree under
        the prefix is returned. For example, given these blobs:
    
            a/1.txt
            a/b/2.txt
    
        If you specify prefix ='a/', without a delimiter, you'll get back:
    
            a/1.txt
            a/b/2.txt
    
        However, if you specify prefix='a/' and delimiter='/', you'll get back
        only the file directly under 'a/':
    
            a/1.txt
    
        As part of the response, you'll also get back a blobs.prefixes entity
        that lists the "subfolders" under `a/`:
    
            a/b/
    
    
        Note: If you only want to list prefixes a/b/ and don't want to iterate over
        blobs, you can do
    
        ```
        for page in blobs.pages:
            print(page.prefixes)
        ```
        """
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        # Note: Client.list_blobs requires at least package version 1.17.0.
        blobs = storage_client.[list_blobs](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_list_blobs)(
            bucket_name, prefix=prefix, delimiter=delimiter
        )
    
        # Note: The call returns a response only when the iterator is consumed.
        print("Blobs:")
        for blob in blobs:
            print(blob.name)
    
        if delimiter:
            print("Prefixes:")
            for prefix in blobs.prefixes:
                print(prefix)
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def list_files_with_prefix bucket_name:, prefix:, delimiter: nil
      # Lists all the files in the bucket that begin with the prefix.
      #
      # This can be used to list all files in a "folder", e.g. "public/".
      #
      # The delimiter argument can be used to restrict the results to only the
      # "files" in the given "folder". Without the delimiter, the entire tree under
      # the prefix is returned. For example, given these files:
      #
      #     a/1.txt
      #     a/b/2.txt
      #
      # If you just specify `prefix: "a"`, you will get back:
      #
      #     a/1.txt
      #     a/b/2.txt
      #
      # However, if you specify `prefix: "a"` and `delimiter: "/"`, you will get back:
      #
      #     a/1.txt
    
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The directory prefix to search for
      # prefix = "a"
    
      # The delimiter to be used to restrict the results
      # delimiter = "/"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name
      files   = bucket.[files](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) prefix: prefix, delimiter: delimiter
    
      files.[each](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Policy-Bindings.html) do |file|
        puts file.name
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
