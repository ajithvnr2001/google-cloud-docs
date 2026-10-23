---
url: https://docs.cloud.google.com/storage/docs/samples/storage-define-bucket-website-configuration/
title: Set the website configuration on a bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:41.688136+00:00
---

# Set the website configuration on a bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-define-bucket-website-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Set the website configuration on a bucket Stay organized with collections  Save and categorize content based on your preferences. 

Set the static website configuration for a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Host a static website](https://docs.cloud.google.com/storage/docs/hosting-static-website)
  * [Hosting a static website using HTTP](https://docs.cloud.google.com/storage/docs/hosting-static-website-http)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& main_page_suffix, std::string const& not_found_page) {
      StatusOr<gcs::BucketMetadata> original =
          client.GetBucketMetadata(bucket_name);
    
      if (!original) throw std::move(original).status();
      StatusOr<gcs::BucketMetadata> patched = client.PatchBucket(
          bucket_name,
          gcs::BucketMetadataPatchBuilder().SetWebsite(
              gcs::BucketWebsite{main_page_suffix, not_found_page}),
          gcs::IfMetagenerationMatch(original->metageneration()));
      if (!patched) throw std::move(patched).status();
    
      if (!patched->has_website()) {
        std::cout << "Static website configuration is not set for bucket "
                  << patched->name() << "\n";
        return;
      }
    
      std::cout << "Static website configuration successfully set for bucket "
                << patched->name() << "\nNew main page suffix is: "
                << patched->website().main_page_suffix
                << "\nNew not found page is: "
                << patched->website().not_found_page << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class BucketWebsiteConfigurationSample
    {
        public Bucket BucketWebsiteConfiguration(
            string bucketName = "your-bucket-name",
            string mainPageSuffix = "index.html",
            string notFoundPage = "404.html")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
    
            if (bucket.Website == null)
            {
                bucket.Website = new Bucket.WebsiteData();
            }
            bucket.Website.MainPageSuffix = mainPageSuffix;
            bucket.Website.NotFoundPage = notFoundPage;
    
            bucket = storage.UpdateBucket(bucket);
            Console.WriteLine($"Static website bucket {bucketName} is set up to use {mainPageSuffix} as the index page and {notFoundPage} as the 404 not found page.");
            return bucket;
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
    
    // setBucketWebsiteInfo sets website configuration on a bucket.
    func setBucketWebsiteInfo(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName, indexPage, notFoundPage string) error {
    	// bucketName := "www.example.com"
    	// indexPage := "index.html"
    	// notFoundPage := "404.html"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	bucketAttrsToUpdate := storage.[BucketAttrsToUpdate](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketAttrsToUpdate){
    		Website: &storage.[BucketWebsite](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketWebsite){
    			MainPageSuffix: indexPage,
    			NotFoundPage:   notFoundPage,
    		},
    	}
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Static website bucket %v is set up to use %v as the index page and %v as the 404 page\n", bucketName, indexPage, notFoundPage)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class SetBucketWebsiteInfo {
      public static void setBucketWesbiteInfo(
          String projectId, String bucketName, String indexPage, String notFoundPage) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your static website bucket
        // String bucketName = "www.example.com";
    
        // The index page for a static website bucket
        // String indexPage = "index.html";
    
        // The 404 page for a static website bucket
        // String notFoundPage = "404.html";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
        bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)().setIndexPage(indexPage).setNotFoundPage(notFoundPage).build().update();
    
        System.out.println(
            "Static website bucket "
                + bucketName
                + " is set up to use "
                + indexPage
                + " as the index page and "
                + notFoundPage
                + " as the 404 page");
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
    
    // The name of the main page
    // const mainPageSuffix = 'http://example.com';
    
    // The Name of a 404 page
    // const notFoundPage = 'http://example.com/404.html';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function addBucketWebsiteConfiguration() {
      await storage.bucket(bucketName).setMetadata({
        website: {
          mainPageSuffix,
          notFoundPage,
        },
      });
    
      console.log(
        `Static website bucket ${bucketName} is set up to use ${mainPageSuffix} as the index page and ${notFoundPage} as the 404 page`
      );
    }
    
    addBucketWebsiteConfiguration().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Update the given bucket's website configuration.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $indexPageObject the name of an object in the bucket to use as
     *        (e.g. 'index.html')
     *     an index page for a static website bucket.
     * @param string $notFoundPageObject the name of an object in the bucket to use
     *        (e.g. '404.html')
     *     as the 404 Not Found page.
     */
    function define_bucket_website_configuration(string $bucketName, string $indexPageObject, string $notFoundPageObject): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $bucket->update([
            'website' => [
                'mainPageSuffix' => $indexPageObject,
                'notFoundPage' => $notFoundPageObject
            ]
        ]);
    
        printf(
            'Static website bucket %s is set up to use %s as the index page and %s as the 404 page.',
            $bucketName,
            $indexPageObject,
            $notFoundPageObject
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def define_bucket_website_configuration(bucket_name, main_page_suffix, not_found_page):
        """Configure website-related properties of bucket"""
        # bucket_name = "your-bucket-name"
        # main_page_suffix = "index.html"
        # not_found_page = "404.html"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
    
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        bucket.[configure_website](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_configure_website)(main_page_suffix, not_found_page)
        bucket.patch()
    
        print(
            "Static website bucket {} is set up to use {} as the index page and {} as the 404 page".format(
                bucket.name, main_page_suffix, not_found_page
            )
        )
        return bucket
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def define_bucket_website_configuration bucket_name:, main_page_suffix:, not_found_page:
      # The ID of your static website bucket
      # bucket_name = "www.example.com"
    
      # The index page for a static website bucket
      # main_page_suffix = "index.html"
    
      # The 404 page for a static website bucket
      # not_found_page = "404.html"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      bucket.update do |b|
        b.[website_main](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = main_page_suffix
        b.[website_404](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = not_found_page
      end
    
      puts "Static website bucket #{bucket_name} is set up to use #{main_page_suffix} as the index page and " \
           "#{not_found_page} as the 404 page"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
