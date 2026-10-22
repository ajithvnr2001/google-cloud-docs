---
url: https://docs.cloud.google.com/storage/docs/samples/storage-control-quickstart-sample/
title: Storage Control Quickstart Sample \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:56.679178+00:00
---

# Storage Control Quickstart Sample  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-control-quickstart-sample/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Storage Control Quickstart Sample Stay organized with collections  Save and categorize content based on your preferences. 

Quickstart sample using the storage control client

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Use the Storage Control API](https://docs.cloud.google.com/storage/docs/reference/storage_control_quickstart)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    #include "google/cloud/storagecontrol/v2/storage_control_client.h"
    #include <iostream>
    
    int main(int argc, char* argv[]) try {
      if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " bucket-id\n";
        return 1;
      }
      auto const name =
          std::string{"projects/_/buckets/"} + argv[1] + "/storageLayout";
    
      namespace storagecontrol = ::google::cloud::storagecontrol_v2;
      auto client = storagecontrol::StorageControlClient(
          storagecontrol::MakeStorageControlConnection());
    
      auto layout = client.GetStorageLayout(name);
      if (!layout) throw std::move(layout).status();
      std::cout << layout->DebugString() << "\n";
    
      return 0;
    } catch (google::cloud::Status const& status) {
      std::cerr << "google::cloud::Status thrown: " << status << "\n";
      return 1;
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.html);
    using System;
    
    public class StorageControlQuickstartSample
    {
        public StorageLayout StorageControlQuickstart(string bucketName = "your-unique-bucket-name")
        {
            [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html) storageControl = [StorageControlClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_Create)();
    
            // Using "_" for projectId means global bucket namespace
            var layoutName = new [StorageLayoutName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayoutName.html)("_", bucketName);
            [StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout.html) response = storageControl.[GetStorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageControlClient.html#Google_Cloud_Storage_Control_V2_StorageControlClient_GetStorageLayout_Google_Cloud_Storage_Control_V2_GetStorageLayoutRequest_Google_Api_Gax_Grpc_CallSettings_)(layoutName);
    
            Console.WriteLine($"Bucket {bucketName} has location type {response.[LocationType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout.html#Google_Cloud_Storage_Control_V2_StorageLayout_LocationType)}");
            return response;
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    // This sample demonstrates how to set up and make an API call with the
    // Storage Control client.
    package main
    
    import (
    	"context"
    	"flag"
    	"fmt"
    	"log"
    	"time"
    
    	control "cloud.google.com/go/storage/control/apiv2"
    	controlpb "cloud.google.com/go/storage/control/apiv2/controlpb"
    )
    
    func main() {
    	// Set this flag to an existing Cloud Storage bucket when running the sample.
    	bucketName := flag.String("bucket", "", "Cloud Storage bucket name")
    	flag.Parse()
    	log.Printf("bucket : %v", *bucketName)
    
    	ctx := context.Background()
    
    	// Create a client.
    	client, err := control.NewStorageControlClient(ctx)
    	if err != nil {
    		log.Fatalf("failed to create client: %v", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/control/apiv2.html#cloud_google_com_go_storage_control_apiv2_StorageControlClient_Close)()
    
    	// Create a request to get the storage layout for the bucket.
    	req := &controlpb.GetStorageLayoutRequest{
    		Name: fmt.Sprintf("projects/_/buckets/%v/storageLayout", *bucketName),
    	}
    
    	// Set a context timeout and send the request.
    	ctx, cancel := context.WithTimeout(ctx, 30*time.Second)
    	defer cancel()
    
    	res, err := client.GetStorageLayout(ctx, req)
    	if err != nil {
    		log.Fatalf("GetStorageLayout: %v", err)
    	}
    
    	// Use response.
    	fmt.Printf("Bucket %v has location type %v", bucketName, res.LocationType)
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.storage.control.v2.[GetStorageLayoutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetStorageLayoutRequest.html);
    import com.google.storage.control.v2.[StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html);
    import com.google.storage.control.v2.[StorageLayout](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageLayout.html);
    import com.google.storage.control.v2.[StorageLayoutName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageLayoutName.html);
    
    public class QuickstartStorageControlSample {
      public static void main(String... args) throws Exception {
        String bucketName = args[0]; // "your-bucket-name";
    
        // Instantiates a client in a try-with-resource to automatically cleanup underlying resources
        try ([StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html) storageControlClient = [StorageControlClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageControlClient.html).create()) {
          [GetStorageLayoutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetStorageLayoutRequest.html) request =
              [GetStorageLayoutRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.GetStorageLayoutRequest.html).newBuilder()
                  // Set project to "_" to signify global bucket
                  .setName([StorageLayoutName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageLayoutName.html).format("_", bucketName))
                  .build();
          [StorageLayout](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageLayout.html) response = storageControlClient.getStorageLayout(request);
          System.out.printf("Performed getStorageLayout request for %s%n", response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.storage.control.v2.StorageLayout.html#com_google_storage_control_v2_StorageLayout_getName__)());
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * This snippet has been automatically generated and should be regarded as a code template only.
     * It will require modifications to work.
     * It may require correct/in-range values for request initialization.
     * TODO(developer): Uncomment these variables before running the sample.
     */
    /**
     *  Required. Name of the bucket for which to get the layout
     */
    // const bucketName = 'abc123'
    
    // Imports the Control library
    const {StorageControlClient} = require('[@google-cloud/storage-control](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/overview.html)').v2;
    
    // Instantiates a client
    const controlClient = new [StorageControlClient](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/storagecontrolclient.html)();
    
    async function callGetStorageLayout() {
      // Construct request
      const request = {
        name: `projects/_/buckets/${bucketName}/storageLayout`,
      };
    
      // Run request
      const [layout] = await controlClient.getStorageLayout(request);
    
      // Use response
      console.log(
        `Bucket ${bucketName} has location type ${layout.locationType}.`
      );
    }
    
    callGetStorageLayout();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    // Includes the autoloader for libraries installed with composer
    require __DIR__ . '/../vendor/autoload.php';
    
    // Imports the Google Cloud client library
    use Google\Cloud\Storage\Control\V2\Client\StorageControlClient;
    use Google\Cloud\Storage\Control\V2\GetStorageLayoutRequest;
    
    // Instantiates a client
    $storageControlClient = new StorageControlClient();
    
    // The name for the new bucket
    $bucketName = 'my-new-bucket';
    
    // Set project to "_" to signify global bucket
    $formattedName = $storageControlClient->storageLayoutName('_', $bucketName);
    $request = (new GetStorageLayoutRequest())->setName($formattedName);
    
    $response = $storageControlClient->getStorageLayout($request);
    
    echo 'Performed get_storage_layout request for ' . $response->getName() . PHP_EOL;

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)
    
    
    def storage_control_quickstart(bucket_name: str) -> None:
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        storage_control_client = [storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest).[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)()
        # The storage layout path uses the global access pattern, in which
        # the “_” denotes this bucket exists in the global namespace.
        layout_path = stor[storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)r[StorageControlClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html)rage_layout_path(
            project="_", bucket=bucket_name
        )
        request = stor[storage_control_v2](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest)S[GetStorageLayoutRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.types.GetStorageLayoutRequest.html)      name=layout_path,
        )
        response = storstorage_control_client.[get_storage_layout](https://docs.cloud.google.com/python/docs/reference/google-cloud-storage-control/latest/google.cloud.storage_control_v2.services.storage_control.StorageControlClient.html#google_cloud_storage_control_v2_services_storage_control_StorageControlClient_get_storage_layout)uest=request)
    
        print(f"Performed get_storage_layout request for {response.name}")
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def quickstart bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage/control"
    
      storage_control = Google::Cloud::Storage::Control.storage_control
    
      # The storage layout path uses the global access pattern, in which the "_"
      # denotes this bucket exists in the global namespace.
      layout_path = storage_control.storage_layout_path project: "_", bucket: bucket_name
    
      request = Google::Cloud::Storage::Control::V2::GetStorageLayoutRequest.new name: layout_path
    
      response = storage_control.get_storage_layout request
    
      puts "Performed get_storage_layout request for #{response.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
