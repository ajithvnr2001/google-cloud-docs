---
url: https://docs.cloud.google.com/storage/docs/samples/storage-cors-configuration/
title: Configure CORS for a bucket \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:32:24.733064+00:00
---

# Configure CORS for a bucket  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-cors-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Configure CORS for a bucket Stay organized with collections  Save and categorize content based on your preferences. 

Add a CORS configuration to a Cloud Storage bucket.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Set up and view CORS configurations](https://docs.cloud.google.com/storage/docs/using-cors)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& origin) {
      StatusOr<gcs::BucketMetadata> original =
          client.GetBucketMetadata(bucket_name);
    
      if (!original) throw std::move(original).status();
      std::vector<gcs::CorsEntry> cors_configuration;
      cors_configuration.emplace_back(
          gcs::CorsEntry{3600, {"GET"}, {origin}, {"Content-Type"}});
    
      StatusOr<gcs::BucketMetadata> patched = client.PatchBucket(
          bucket_name,
          gcs::BucketMetadataPatchBuilder().SetCors(cors_configuration),
          gcs::IfMetagenerationMatch(original->metageneration()));
      if (!patched) throw std::move(patched).status();
    
      if (patched->cors().empty()) {
        std::cout << "Cors configuration is not set for bucket "
                  << patched->name() << "\n";
        return;
      }
    
      std::cout << "Cors configuration successfully set for bucket "
                << patched->name() << "\nNew cors configuration: ";
      for (auto const& cors_entry : patched->cors()) {
        std::cout << "\n  " << cors_entry << "\n";
      }
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    using static Google.Apis.Storage.v1.Data.Bucket;
    
    public class BucketAddCorsConfigurationSample
    {
        public Bucket BucketAddCorsConfiguration(string bucketName = "your-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            var bucket = storage.GetBucket(bucketName);
    
            CorsData corsData = new CorsData
            {
                Origin = new string[] { "*" },
                ResponseHeader = new string[] { "Content-Type", "x-goog-resumable" },
                Method = new string[] { "PUT", "POST" },
                MaxAgeSeconds = 3600 //One Hour
            };
    
            if (bucket.Cors == null)
            {
                bucket.Cors = new List<CorsData>();
            }
            bucket.Cors.Add(corsData);
    
            bucket = storage.UpdateBucket(bucket);
            Console.WriteLine($"bucketName {bucketName} was updated with a CORS config to allow {string.Join(",", corsData.Method)} requests from" +
                $" {string.Join(",", corsData.[Origin](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UploadObjectOptions.html#Google_Cloud_Storage_V1_UploadObjectOptions_Origin))} sharing {string.Join(",", corsData.ResponseHeader)} responseHeader" +
                $" responses across origins.");
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
    
    // setBucketCORSConfiguration sets a CORS configuration on a bucket.
    func setBucketCORSConfiguration(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string, maxAge time.Duration, methods, origins, responseHeaders []string) error {
    	// bucketName := "bucket-name"
    	// maxAge := time.Hour
    	// methods := []string{"GET"}
    	// origins := []string{"some-origin.com"}
    	// responseHeaders := []string{"Content-Type"}
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
    		CORS: []storage.[CORS](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_CORS){
    			{
    				MaxAge:          maxAge,
    				Methods:         methods,
    				Origins:         origins,
    				ResponseHeaders: responseHeaders,
    			}},
    	}
    	if _, err := bucket.Update(ctx, bucketAttrsToUpdate); err != nil {
    		return fmt.Errorf("Bucket(%q).Update: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Bucket %v was updated with a CORS config to allow %v requests from %v sharing %v responses across origins\n", bucketName, methods, origins, responseHeaders)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[Cors](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Cors.html);
    import com.google.cloud.storage.[HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HttpMethod.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.common.collect.ImmutableList;
    
    public class ConfigureBucketCors {
      public static void configureBucketCors(
          String projectId,
          String bucketName,
          String origin,
          String responseHeader,
          Integer maxAgeSeconds) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The origin for this CORS config to allow requests from
        // String origin = "http://example.appspot.com";
    
        // The response header to share across origins
        // String responseHeader = "Content-Type";
    
        // The maximum amount of time the browser can make requests before it must repeat preflighted
        // requests
        // Integer maxAgeSeconds = 3600;
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName);
    
        // See the HttpMethod documentation for other HTTP methods available:
        // https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/urlfetch/HTTPMethod
        [HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HttpMethod.html) method = [HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HttpMethod.html).GET;
    
        [Cors](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Cors.html) cors =
            [Cors](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Cors.html).newBuilder()
                .[setOrigins](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Cors.Builder.html#com_google_cloud_storage_Cors_Builder_setOrigins_java_lang_Iterable_com_google_cloud_storage_Cors_Origin__)(ImmutableList.of([Cors](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Cors.html).Origin.of(origin)))
                .[setMethods](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Cors.Builder.html#com_google_cloud_storage_Cors_Builder_setMethods_java_lang_Iterable_com_google_cloud_storage_HttpMethod__)(ImmutableList.of(method))
                .[setResponseHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Cors.Builder.html#com_google_cloud_storage_Cors_Builder_setResponseHeaders_java_lang_Iterable_java_lang_String__)(ImmutableList.of(responseHeader))
                .[setMaxAgeSeconds](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Cors.Builder.html#com_google_cloud_storage_Cors_Builder_setMaxAgeSeconds_java_lang_Integer_)(maxAgeSeconds)
                .build();
    
        bucket.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html#com_google_cloud_storage_Bucket_toBuilder__)().setCors(ImmutableList.of(cors)).build().update();
    
        System.out.println(
            "Bucket "
                + bucketName
                + " was updated with a CORS config to allow GET requests from "
                + origin
                + " sharing "
                + responseHeader
                + " responses across origins");
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The origin for this CORS config to allow requests from
    // const origin = 'http://example.appspot.com';
    
    // The response header to share across origins
    // const responseHeader = 'Content-Type';
    
    // The maximum amount of time the browser can make requests before it must
    // repeat preflighted requests
    // const maxAgeSeconds = 3600;
    
    // The name of the method
    // See the HttpMethod documentation for other HTTP methods available:
    // https://cloud.google.com/appengine/docs/standard/java/javadoc/com/google/appengine/api/urlfetch/HTTPMethod
    // const method = 'GET';
    
    async function configureBucketCors() {
      await storage.bucket(bucketName).[setCorsConfiguration](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)([
        {
          maxAgeSeconds,
          method: [method],
          origin: [origin],
          responseHeader: [responseHeader],
        },
      ]);
    
      console.log(`Bucket ${bucketName} was updated with a CORS config
          to allow ${method} requests from ${origin} sharing 
          ${responseHeader} responses across origins`);
    }
    
    configureBucketCors().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Update the CORS configuration of a bucket.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $method The HTTP method for the CORS config. (e.g. 'GET')
     * @param string $origin The origin from which the CORS config will allow requests.
     *        (e.g. 'http://example.appspot.com')
     * @param string $responseHeader The response header to share across origins.
     *        (e.g. 'Content-Type')
     * @param int $maxAgeSeconds The maximum amount of time the browser can make
     *        (e.g. 3600)
     *     requests before it must repeat preflighted requests.
     */
    function cors_configuration(string $bucketName, string $method, string $origin, string $responseHeader, int $maxAgeSeconds): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $bucket->update([
            'cors' => [
                [
                    'method' => [$method],
                    'origin' => [$origin],
                    'responseHeader' => [$responseHeader],
                    'maxAgeSeconds' => $maxAgeSeconds,
                ]
            ]
        ]);
    
        printf(
            'Bucket %s was updated with a CORS config to allow GET requests from ' .
            '%s sharing %s responses across origins.',
            $bucketName,
            $origin,
            $responseHeader
        );
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def cors_configuration(bucket_name):
        """Set a bucket's CORS policies configuration."""
        # bucket_name = "your-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[get_bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_get_bucket)(bucket_name)
        bucket.[cors](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_cors) = [
            {
                "origin": ["*"],
                "responseHeader": [
                    "Content-Type",
                    "x-goog-resumable"],
                "method": ['PUT', 'POST'],
                "maxAgeSeconds": 3600
            }
        ]
        bucket.patch()
    
        print(f"Set CORS policies for bucket {bucket.name} is {bucket.[cors](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.bucket.Bucket.html#google_cloud_storage_bucket_Bucket_cors)}")
        return bucket
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def cors_configuration bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      bucket.cors do |c|
        c.[add_rule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket-Cors.html) ["*"],
                   ["PUT", "POST"],
                   headers: [
                     "Content-Type",
                     "x-goog-resumable"
                   ],
                   max_age: 3600
      end
    
      puts "Set CORS policies for bucket #{bucket_name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
