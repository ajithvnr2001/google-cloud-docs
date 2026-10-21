---
url: https://docs.cloud.google.com/storage/docs/hosting-static-website-http/
title: Hosting a static website using HTTP \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:15.382167+00:00
---

# Hosting a static website using HTTP  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/hosting-static-website-http/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)



Send feedback 

#  Hosting a static website using HTTP Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial describes how to configure a Cloud Storage bucket to host a static website for a domain you own. Static web pages can contain client-side technologies such as HTML, CSS, and JavaScript. They cannot contain dynamic content such as server-side scripts like PHP.

This tutorial shows you how to serve content over HTTP. For a tutorial that uses HTTPS, see [Hosting a static website](https://docs.cloud.google.com/storage/docs/hosting-static-website).

For examples and tips on static web pages, including how to host static assets for a dynamic website, see the [Static Website page](https://docs.cloud.google.com/storage/docs/static-website).

**Caution:** This tutorial makes content available to the public internet. We recommend that you don't serve content that contains sensitive or private data from your Cloud Storage bucket.

## Objectives

In this tutorial you will: 

  * Point your domain to Cloud Storage by using a `CNAME` record.
  * Create a bucket that is linked to your domain.
  * Upload and share your site's files.
  * Test the website.



## Costs

This tutorial uses the following billable component of Google Cloud:

  * Cloud Storage



See the [Monitoring your storage charges tip](https://docs.cloud.google.com/storage/docs/static-website#tip-charges) for details on what charges may be incurred when hosting a static website, and see the [Pricing](https://docs.cloud.google.com/storage/pricing) page for details on Cloud Storage costs.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Have a domain that you own or manage. If you don't have an existing domain, there are many services through which you can register a new domain, such as [Cloud Domains](https://docs.cloud.google.com/domains/docs). 

This tutorial uses the domain `example.com`.

  7. [Verify that you own or manage the domain that you will be using](https://docs.cloud.google.com/storage/docs/domain-name-verification#verification). Make sure you are verifying the top-level domain, such as `example.com`, and not a subdomain, such as `www.example.com`. 

**Note** : If you own the domain you are associating to a bucket, you might have already performed this step in the past. If you purchased your domain through Cloud Domains, verification is automatic.




## Connecting your domain to Cloud Storage

To connect your domain to Cloud Storage, create a `CNAME` record through your domain registration service. A `CNAME` record is a type of DNS record. It directs traffic that requests a URL from your domain to the resources you want to serve, in this case objects in your Cloud Storage buckets. For `www.example.com`, the `CNAME` record might contain the following information:
    
    
    NAME                  TYPE     DATA
    www                   CNAME    c.storage.googleapis.com.
    

For more information about `CNAME` redirects, see [URI for `CNAME` aliasing](https://docs.cloud.google.com/storage/docs/request-endpoints#cname).

To connect your domain to Cloud Storage:

  1. Create a `CNAME` record that points to `c.storage.googleapis.com.`.

Your domain registration service should have a way for you to administer your domain, including adding a `CNAME` record. For example, if you use Cloud DNS, instructions for adding resource records can be found on the [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records) page.

**Note:** DNS does not support creating a CNAME record on a root domain, such as `example.com`, so in most cases, you must [create your `CNAME` record on a subdomain](https://docs.cloud.google.com/storage/docs/static-website#tip-subdomain), such as `www.example.com` or `myblog.example.com`. Some DNS providers offer a non-standard feature that allows a root domain to be aliased to another name without the use of `CNAME`. Consult your DNS provider documentation to determine if such a feature is available.



## Creating a bucket

Create a bucket whose name matches the `CNAME` you created for your domain.

For example, if you added a `CNAME` record pointing from the `www` subdomain of `example.com` to `c.storage.googleapis.com.`, then the Google Cloud CLI command to create a bucket with the name `www.example.com` would look similar to the following:
    
    
    gcloud storage buckets create gs://www.example.com --location=US

For complete instructions to creating buckets with different tools, see [Create buckets](https://docs.cloud.google.com/storage/docs/creating-buckets).

## Uploading your site's files

To add to your bucket the files you want your website to serve:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you created.

  3. Click the **Upload files** button in the **Objects** tab.

  4. In the file dialog, browse to the desired file and select it.




After the upload completes, you should see the file name along with file information displayed in the bucket.

### Command line

Use the [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command to copy files to your bucket. For example, to copy the file `index.html` from its current location `Desktop`:
    
    
    gcloud storage cp Desktop/index.html gs://www.example.com

If successful, the response looks like the following example:
    
    
    Completed files 1/1 | 164.3kiB/164.3kiB

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& file_name,
       std::string const& bucket_name, std::string const& object_name) {
      // Note that the client library automatically computes a hash on the
      // client-side to verify data integrity during transmission.
      StatusOr<gcs::ObjectMetadata> metadata = client.UploadFile(
          file_name, bucket_name, object_name, gcs::IfGenerationMatch(0));
      if (!metadata) throw std::move(metadata).status();
    
      std::cout << "Uploaded " << file_name << " to object " << metadata->name()
                << " in bucket " << metadata->bucket()
                << "\nFull metadata: " << *metadata << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.IO;
    
    public class UploadFileSample
    {
        public void UploadFile(
            string bucketName = "your-unique-bucket-name",
            string localPath = "my-local-path/my-file-name",
            string objectName = "my-file-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
            using var fileStream = File.OpenRead(localPath);
            storage.UploadObject(bucketName, objectName, null, fileStream);
            Console.WriteLine($"Uploaded {objectName}.");
        }
    }
    

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // uploadFile uploads an object.
    func uploadFile(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// Open local file.
    	f, err := os.Open("notes.txt")
    	if err != nil {
    		return fmt.Errorf("os.Open: %w", err)
    	}
    	defer f.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*50)
    	defer cancel()
    
    	o := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object)
    
    	// Optional: set a generation-match precondition to avoid potential race
    	// conditions and data corruptions. The request to upload is aborted if the
    	// object's generation number does not match your precondition.
    	// For an object that does not yet exist, set the DoesNotExist precondition.
    	o = o.If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){DoesNotExist: true})
    	// If the live object already exists in your bucket, set instead a
    	// generation-match precondition using the live object's generation number.
    	// attrs, err := o.Attrs(ctx)
    	// if err != nil {
    	// 	return fmt.Errorf("object.Attrs: %w", err)
    	// }
    	// o = o.If(storage.Conditions{GenerationMatch: attrs.Generation})
    
    	// Upload an object with storage.Writer.
    	wc := o.[NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter)(ctx)
    	if _, err = io.Copy(wc, f); err != nil {
    		return fmt.Errorf("io.Copy: %w", err)
    	}
    	if err := wc.Close(); err != nil {
    		return fmt.Errorf("Writer.Close: %w", err)
    	}
    	fmt.Fprintf(w, "Blob %v uploaded.\n", object)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample uploads an individual object:
    
    
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.io.IOException;
    import java.nio.file.Paths;
    
    public class UploadObject {
      public static void uploadObject(
          String projectId, String bucketName, String objectName, String filePath) throws IOException {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The path to your file to upload
        // String filePath = "path/to/your/file"
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfo = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(blobId).build();
    
        // Optional: set a generation-match precondition to avoid potential race
        // conditions and data corruptions. The request returns a 412 error if the
        // preconditions are not met.
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobWriteOption precondition;
        if (storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, objectName) == null) {
          // For a target object that does not yet exist, set the DoesNotExist precondition.
          // This will cause the request to fail if the object is created before the request runs.
          precondition = [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobWriteOption.doesNotExist();
        } else {
          // If the destination already exists in your bucket, instead set a generation-match
          // precondition. This will cause the request to fail if the existing object's generation
          // changes before the request runs.
          precondition =
              [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobWriteOption.generationMatch(
                  storage.[get](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_get_com_google_cloud_storage_BlobId_)(bucketName, objectName).getGeneration());
        }
        storage.[createFrom](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_createFrom_com_google_cloud_storage_BlobInfo_java_io_InputStream_com_google_cloud_storage_Storage_BlobWriteOption____)(blobInfo, Paths.get(filePath), precondition);
    
        System.out.println(
            "File " + filePath + " uploaded to bucket " + bucketName + " as " + objectName);
      }
    }

The following sample uploads multiple objects concurrently:
    
    
    import com.google.cloud.storage.transfermanager.[ParallelUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html);
    import com.google.cloud.storage.transfermanager.[TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html);
    import com.google.cloud.storage.transfermanager.[TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html);
    import com.google.cloud.storage.transfermanager.[UploadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.html);
    import java.io.IOException;
    import java.nio.file.Path;
    import java.util.List;
    
    class UploadMany {
    
      public static void uploadManyFiles(String bucketName, List<Path> files) throws IOException {
        [TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html) transferManager = [TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html).newBuilder().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [ParallelUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html) parallelUploadConfig =
            [ParallelUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html).newBuilder().setBucketName(bucketName).build();
        List<UploadResult> results =
            transferManager.[uploadFiles](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html#com_google_cloud_storage_transfermanager_TransferManager_uploadFiles_java_util_List_java_nio_file_Path__com_google_cloud_storage_transfermanager_ParallelUploadConfig_)(files, parallelUploadConfig).[getUploadResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadJob.html#com_google_cloud_storage_transfermanager_UploadJob_getUploadResults__)();
        for ([UploadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.html) result : results) {
          System.out.println(
              "Upload for "
                  + result.getInput().getName()
                  + " completed with status "
                  + result.getStatus());
        }
      }
    }

The following sample uploads all objects with a common prefix concurrently:
    
    
    import com.google.cloud.storage.transfermanager.[ParallelUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html);
    import com.google.cloud.storage.transfermanager.[TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html);
    import com.google.cloud.storage.transfermanager.[TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html);
    import com.google.cloud.storage.transfermanager.[UploadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.stream.Stream;
    
    class UploadDirectory {
    
      public static void uploadDirectoryContents(String bucketName, Path sourceDirectory)
          throws IOException {
        [TransferManager](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html) transferManager = [TransferManagerConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html).newBuilder().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
        [ParallelUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html) parallelUploadConfig =
            [ParallelUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.ParallelUploadConfig.html).newBuilder().setBucketName(bucketName).build();
    
        // Create a list to store the file paths
        List<Path> filePaths = new ArrayList<>();
        // Get all files in the directory
        // try-with-resource to ensure pathStream is closed
        try (Stream<Path> pathStream = Files.walk(sourceDirectory)) {
          pathStream.filter(Files::isRegularFile).forEach(filePaths::add);
        }
        List<UploadResult> results =
            transferManager.[uploadFiles](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManager.html#com_google_cloud_storage_transfermanager_TransferManager_uploadFiles_java_util_List_java_nio_file_Path__com_google_cloud_storage_transfermanager_ParallelUploadConfig_)(filePaths, parallelUploadConfig).[getUploadResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadJob.html#com_google_cloud_storage_transfermanager_UploadJob_getUploadResults__)();
        for ([UploadResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.UploadResult.html) result : results) {
          System.out.println(
              "Upload for "
                  + result.getInput().getName()
                  + " completed with status "
                  + result.getStatus());
        }
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample uploads an individual object:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The path to your file to upload
    // const filePath = 'path/to/your/file';
    
    // The new ID for your GCS file
    // const destFileName = 'your-new-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function uploadFile() {
      const options = {
        destination: destFileName,
        // Optional:
        // Set a generation-match precondition to avoid potential race conditions
        // and data corruptions. The request to upload is aborted if the object's
        // generation number does not match your precondition. For a destination
        // object that does not yet exist, set the ifGenerationMatch precondition to 0
        // If the destination object already exists in your bucket, set instead a
        // generation-match precondition using its generation number.
        preconditionOpts: {ifGenerationMatch: generationMatchPrecondition},
      };
    
      await storage.bucket(bucketName).[upload](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/bucket.html)(filePath, options);
      console.log(`${filePath} uploaded to ${bucketName}`);
    }
    
    uploadFile().catch(console.error);

The following sample uploads multiple objects concurrently:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The ID of the first GCS file to upload
    // const firstFilePath = 'your-first-file-name';
    
    // The ID of the second GCS file to upload
    // const secondFilePath = 'your-second-file-name';
    
    // Imports the Google Cloud client library
    const {Storage, TransferManager} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Creates a transfer manager client
    const transferManager = new [TransferManager](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/transfermanager.html)(storage.bucket(bucketName));
    
    async function uploadManyFilesWithTransferManager() {
      // Uploads the files
      await transferManager.[uploadManyFiles](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/transfermanager.html)([firstFilePath, secondFilePath]);
    
      for (const filePath of [firstFilePath, secondFilePath]) {
        console.log(`${filePath} uploaded to ${bucketName}.`);
      }
    }
    
    uploadManyFilesWithTransferManager().catch(console.error);

The following sample uploads all objects with a common prefix concurrently:
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The local directory to upload
    // const directoryName = 'your-directory';
    
    // Imports the Google Cloud client library
    const {Storage, TransferManager} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Creates a transfer manager client
    const transferManager = new [TransferManager](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/transfermanager.html)(storage.bucket(bucketName));
    
    async function uploadDirectoryWithTransferManager() {
      // Uploads the directory
      await transferManager.[uploadManyFiles](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/transfermanager.html)(directoryName);
    
      console.log(`${directoryName} uploaded to ${bucketName}.`);
    }
    
    uploadDirectoryWithTransferManager().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Upload a file.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $source The path to the file to upload.
     *        (e.g. '/path/to/your/file')
     */
    function upload_object(string $bucketName, string $objectName, string $source): void
    {
        $storage = new StorageClient();
        if (!$file = fopen($source, 'r')) {
            throw new \InvalidArgumentException('Unable to open file for reading');
        }
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->upload($file, [
            'name' => $objectName
        ]);
        printf('Uploaded %s to gs://%s/%s' . PHP_EOL, basename($source), $bucketName, $objectName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample uploads an individual object:
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def upload_blob(bucket_name, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
        # The path to your file to upload
        # source_file_name = "local/path/to/file"
        # The ID of your GCS object
        # destination_blob_name = "storage-object-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(destination_blob_name)
    
        # Optional: set a generation-match precondition to avoid potential race conditions
        # and data corruptions. The request to upload is aborted if the object's
        # generation number does not match your precondition. For a destination
        # object that does not yet exist, set the if_generation_match precondition to 0.
        # If the destination object already exists in your bucket, set instead a
        # generation-match precondition using its generation number.
        generation_match_precondition = 0
    
        blob.[upload_from_filename](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_filename)(source_file_name, if_generation_match=generation_match_precondition)
    
        print(
            f"File {source_file_name} uploaded to {destination_blob_name}."
        )
    
    

The following sample uploads multiple objects concurrently:
    
    
    def upload_many_blobs_with_transfer_manager(
        bucket_name, filenames, source_directory="", workers=8
    ):
        """Upload every file in a list to a bucket, concurrently in a process pool.
    
        Each blob name is derived from the filename, not including the
        `source_directory` parameter. For complete control of the blob name for each
        file (and other aspects of individual blob metadata), use
        transfer_manager.upload_many() instead.
        """
    
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # A list (or other iterable) of filenames to upload.
        # filenames = ["file_1.txt", "file_2.txt"]
    
        # The directory on your computer that is the root of all of the files in the
        # list of filenames. This string is prepended (with os.path.join()) to each
        # filename to get the full path to the file. Relative paths and absolute
        # paths are both accepted. This string is not included in the name of the
        # uploaded blob; it is only used to find the source files. An empty string
        # means "the current working directory". Note that this parameter allows
        # directory traversal (e.g. "/", "../") and is not intended for unsanitized
        # end user input.
        # source_directory=""
    
        # The maximum number of processes to use for the operation. The performance
        # impact of this value depends on the use case, but smaller files usually
        # benefit from a higher number of processes. Each additional process occupies
        # some CPU and memory resources until finished. Threads can be used instead
        # of processes by passing `worker_type=transfer_manager.THREAD`.
        # workers=8
    
        from google.cloud.storage import [Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html), [transfer_manager](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)
    
        storage_client = Client()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        results = [transfer_manager](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html).[upload_many_from_filenames](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)(
            bucket, filenames, source_directory=source_directory, max_workers=workers
        )
    
        for name, result in zip(filenames, results):
            # The results list is either `None` or an exception for each filename in
            # the input list, in order.
    
            if isinstance(result, Exception):
                print("Failed to upload {} due to exception: {}".format(name, result))
            else:
                print("Uploaded {} to {}.".format(name, bucket.name))

The following sample uploads all objects with a common prefix concurrently:
    
    
    def upload_directory_with_transfer_manager(bucket_name, source_directory, workers=8):
        """Upload every file in a directory, including all files in subdirectories.
    
        Each blob name is derived from the filename, not including the `directory`
        parameter itself. For complete control of the blob name for each file (and
        other aspects of individual blob metadata), use
        transfer_manager.upload_many() instead.
        """
    
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # The directory on your computer to upload. Files in the directory and its
        # subdirectories will be uploaded. An empty string means "the current
        # working directory".
        # source_directory=""
    
        # The maximum number of processes to use for the operation. The performance
        # impact of this value depends on the use case, but smaller files usually
        # benefit from a higher number of processes. Each additional process occupies
        # some CPU and memory resources until finished. Threads can be used instead
        # of processes by passing `worker_type=transfer_manager.THREAD`.
        # workers=8
    
        from pathlib import Path
    
        from google.cloud.storage import [Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html), [transfer_manager](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)
    
        storage_client = Client()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        # Generate a list of paths (in string form) relative to the `directory`.
        # This can be done in a single list comprehension, but is expanded into
        # multiple lines here for clarity.
    
        # First, recursively get all files in `directory` as Path objects.
        directory_as_path_obj = Path(source_directory)
        paths = directory_as_path_obj.rglob("*")
    
        # Filter so the list only includes files, not directories themselves.
        file_paths = [path for path in paths if path.is_file()]
    
        # These paths are relative to the current working directory. Next, make them
        # relative to `directory`
        relative_paths = [path.relative_to(source_directory) for path in file_paths]
    
        # Finally, convert them all to strings.
        string_paths = [str(path) for path in relative_paths]
    
        print("Found {} files.".format(len(string_paths)))
    
        # Start the upload.
        results = [transfer_manager](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html).[upload_many_from_filenames](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.transfer_manager.html)(
            bucket, string_paths, source_directory=source_directory, max_workers=workers
        )
    
        for name, result in zip(string_paths, results):
            # The results list is either `None` or an exception for each filename in
            # the input list, in order.
    
            if isinstance(result, Exception):
                print("Failed to upload {} due to exception: {}".format(name, result))
            else:
                print("Uploaded {} to {}.".format(name, bucket.name))

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def upload_file bucket_name:, local_file_path:, file_name: nil
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The path to your file to upload
      # local_file_path = "/local/path/to/file.txt"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket  = storage.bucket bucket_name, skip_lookup: true
    
      file = bucket.[create_file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) local_file_path, file_name
    
      puts "Uploaded #{local_file_path} as #{file.name} in bucket #{bucket_name}"
    end

### Rust
    
    
    use google_cloud_storage::client::Storage;
    
    pub async fn sample(
        client: &Storage,
        bucket: &str,
        object: &str,
        file_path: &str,
    ) -> Result<(), anyhow::Error> {
        let payload = tokio::fs::File::open(file_path).await?;
        let _result = client
            .write_object(format!("projects/_/buckets/{bucket}"), object, payload)
            .send_unbuffered()
            .await?;
    
        println!("Uploaded {file_path} to {object} in bucket {bucket}.");
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`POST` Object](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/insert) request. For the index page of www.example.com:
         
         curl -X POST --data-binary @index.html \
           -H "Content-Type: text/html" \
           -H "Authorization: $(gcloud auth print-access-token)" \
           "https://storage.googleapis.com/upload/storage/v1/b/www.example.com/o?uploadType=media&name=index.html"




### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`PUT` Object](https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload) request. For the index page of www.example.com:
         
         curl -X PUT --data-binary @index.html \
           -H "Authorization: $(gcloud auth print-access-token)" \
           -H "Content-Type: text/html" \
           "https://storage.googleapis.com/www.example.com/index.html"




## Sharing your files

To make all objects in a bucket readable to everyone on the public internet:

**Caution:** Before making your bucket publicly accessible, make sure that the files in your bucket do not contain sensitive or private information.

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket that you want to make public.

  3. Select the **Permissions** tab near the top of the page.

  4. If the **Public access** pane reads **Not public** , click the button labeled **Remove public access prevention** , and click **Confirm** in the dialog that appears.

  5. Click the _add_box_ **Grant access** button.

The _Add principals_ dialog box appears.

  6. In the **New principals** field, enter `allUsers`.

  7. In the **Select a role** drop down, select the **Cloud Storage** sub-menu, and click the **Storage Object Viewer** option.

  8. Click **Save**.

  9. Click **Allow public access**.




Once shared publicly, a **link** icon appears for each object in the _public access_ column. You can click this icon to get the URL for the object.

### Command line

Use the [`buckets add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/add-iam-policy-binding) command:
    
    
    gcloud storage buckets add-iam-policy-binding gs://www.example.com --member=allUsers --role=roles/storage.objectViewer

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name) {
      auto current_policy = client.GetNativeBucketIamPolicy(
          bucket_name, gcs::RequestedPolicyVersion(3));
      if (!current_policy) throw std::move(current_policy).status();
    
      current_policy->set_version(3);
      current_policy->bindings().emplace_back(
          gcs::NativeIamBinding("roles/storage.objectViewer", {"allUsers"}));
    
      auto updated =
          client.SetNativeBucketIamPolicy(bucket_name, *current_policy);
      if (!updated) throw std::move(updated).status();
    
      std::cout << "Policy successfully updated: " << *updated << "\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using Google.Apis.Storage.v1.Data;
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    
    public class MakeBucketPublicSample
    {
        public void MakeBucketPublic(string bucketName = "your-unique-bucket-name")
        {
            var storage = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    
            Policy policy = storage.GetBucketIamPolicy(bucketName);
    
            policy.Bindings.Add(new Policy.BindingsData
            {
                Role = "roles/storage.objectViewer",
                Members = new List<string> { "allUsers" }
            });
    
            storage.SetBucketIamPolicy(bucketName, policy);
            Console.WriteLine(bucketName + " is now public ");
        }
    }

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/iam"
    	"cloud.google.com/go/iam/apiv1/iampb"
    	"cloud.google.com/go/storage"
    )
    
    // setBucketPublicIAM makes all objects in a bucket publicly readable.
    func setBucketPublicIAM(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName string) error {
    	// bucketName := "bucket-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	policy, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_IAM)().[V3](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_Handle_V3)().Policy(ctx)
    	if err != nil {
    		return fmt.Errorf("Bucket(%q).IAM().V3().Policy: %w", bucketName, err)
    	}
    	role := "roles/storage.objectViewer"
    	policy.Bindings = append(policy.Bindings, &iampb.Binding{
    		Role:    role,
    		Members: []string{iam.[AllUsers](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_AllUsers_AllAuthenticatedUsers)},
    	})
    	if err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).[IAM](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_IAM)().[V3](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/iam/latest/index.html#cloud_google_com_go_iam_Handle_V3)().SetPolicy(ctx, policy); err != nil {
    		return fmt.Errorf("Bucket(%q).IAM().SetPolicy: %w", bucketName, err)
    	}
    	fmt.Fprintf(w, "Bucket %v is now publicly readable\n", bucketName)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.[Identity](https://docs.cloud.google.com/java/docs/reference/google-cloud-storageinsights/latest/com.google.cloud.storageinsights.v1.Identity.html);
    import com.google.cloud.[Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.cloud.storage.[StorageRoles](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRoles.html);
    
    public class MakeBucketPublic {
      public static void makeBucketPublic([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bucketName) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().getService();
        [Policy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Policy.html) originalPolicy = storage.[getIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_getIamPolicy_java_lang_String_com_google_cloud_storage_Storage_BucketSourceOption____)(bucketName);
        storage.[setIamPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_setIamPolicy_java_lang_String_com_google_cloud_Policy_com_google_cloud_storage_Storage_BucketSourceOption____)(
            bucketName,
            originalPolicy.toBuilder()
                .addIdentity(StorageRoles.objectViewer(), Identity.allUsers()) // All users can view
                .build());
    
        System.out.println("Bucket " + bucketName + " is now publicly readable");
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
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function makeBucketPublic() {
      await storage.bucket(bucketName).makePublic();
    
      console.log(`Bucket ${bucketName} is now publicly readable`);
    }
    
    makeBucketPublic().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Update the specified bucket's IAM configuration to make it publicly accessible.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function set_bucket_public_iam(string $bucketName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
    
        $policy = $bucket->iam()->policy(['requestedPolicyVersion' => 3]);
        $policy['version'] = 3;
    
        $role = 'roles/storage.objectViewer';
        $members = ['allUsers'];
    
        $policy['bindings'][] = [
            'role' => $role,
            'members' => $members
        ];
    
        $bucket->iam()->setPolicy($policy);
    
        printf('Bucket %s is now public', $bucketName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from typing import List
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def set_bucket_public_iam(
        bucket_name: str = "your-bucket-name",
        members: List[str] = ["allUsers"],
    ):
        """Set a public IAM Policy to bucket"""
        # bucket_name = "your-bucket-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
    
        policy = bucket.get_iam_policy(requested_policy_version=3)
        policy.bindings.append(
            {"role": "roles/storage.objectViewer", "members": members}
        )
    
        bucket.set_iam_policy(policy)
    
        print(f"Bucket {bucket.name} is now publicly readable")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def set_bucket_public_iam bucket_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      bucket.[policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) do |p|
        p.[add](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-PolicyV1.html) "roles/storage.objectViewer", "allUsers"
      end
    
      puts "Bucket #{bucket_name} is now publicly readable"
    end

### Rust
    
    
    use google_cloud_iam_v1::model::{Binding, GetPolicyOptions};
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(client: &StorageControl, bucket_id: &str) -> anyhow::Result<()> {
        let mut policy = client
            .get_iam_policy()
            .set_resource(format!("projects/_/buckets/{bucket_id}"))
            .set_options(GetPolicyOptions::new().set_requested_policy_version(3))
            .send()
            .await?;
        policy.version = 3;
        policy.bindings.push(
            Binding::new()
                .set_role("roles/storage.objectViewer")
                .set_members(["allUsers"]),
        );
        let updated_policy = client
            .set_iam_policy()
            .set_resource(format!("projects/_/buckets/{bucket_id}"))
            .set_policy(policy)
            .send()
            .await?;
        println!(
            "Successfully set public IAM policy for bucket {}",
            bucket_id
        );
        println!("The updated policy is: {:?}", updated_policy);
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that contains the following information:
         
         {
           "bindings":[
             {
               "role": "roles/storage.objectViewer",
               "members":["allUsers"]
             }
           ]
         }

  3. Use [`cURL`](https://docs.cloud.google.com/storage/docs/static-website#tip-charges) to call the [JSON API](https://docs.cloud.google.com/storage/docs/access-control/create-manage-lists#defaultobjects) with a [`PUT` Bucket](https://docs.cloud.google.com/storage/pricing) request:
         
         curl -X PUT --data-binary @JSON_FILE_NAME \
           -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/BUCKET_NAME/iam"

Where:

     * `JSON_FILE_NAME` is the path for the JSON file that you created in Step 2.
     * `BUCKET_NAME` is the name of the bucket whose objects you want to make public. For example, `my-bucket`.



### XML API

Making all objects in a bucket publicly readable is not supported by the XML API. Use the Google Cloud console or `gcloud storage` instead.

**Note:** `roles/storage.objectViewer` includes permission to list the objects in the bucket.

If wanted, you can alternatively [make portions of your bucket publicly accessible](https://docs.cloud.google.com/storage/docs/access-control/making-data-public#managed-folders).

Visitors receive a `http 403` response code when requesting the URL for a non-public or non-existent file. See the next section for information on how to add an error page that uses a `http 404` response code.

## Recommended: Assigning specialty pages

You can assign an index page suffix, which is controlled by the `MainPageSuffix` property and a custom error page, which is controlled by the `NotFoundPage` property. Assigning either is optional, but without an index page, nothing is served when users access your top-level site, for example, `http://www.example.com`. For more information, see [Website configuration examples](https://docs.cloud.google.com/storage/docs/static-website#examples).

In the following sample, the `MainPageSuffix` is set to `index.html` and `NotFoundPage` is set to `404.html`:

### Console

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, find the bucket you created.

  3. Click the **Bucket overflow** menu (_more_vert_) associated with the bucket and select **Edit website configuration**.

  4. In the website configuration dialog, specify the main page and error page.

  5. Click **Save**.


**Note:** View, change, or remove these settings from the **Edit website configuration** menu.

### Command line

Use the [`buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/buckets/update) command with the `--web-main-page-suffix` and `--web-error-page` flags:
    
    
    gcloud storage buckets update gs://www.example.com --web-main-page-suffix=index.html --web-error-page=404.html

If successful, the command returns:
    
    
    Updating gs://www.example.com/...
      Completed 1

**Note:** Change or remove these settings with additional `buckets update` commands and view these settings with the `buckets describe` command.

### Client libraries

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
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      bucket = storage.bucket bucket_name
    
      bucket.update do |b|
        b.[website_main](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = main_page_suffix
        b.[website_404](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) = not_found_page
      end
    
      puts "Static website bucket #{bucket_name} is set up to use #{main_page_suffix} as the index page and " \
           "#{not_found_page} as the 404 page"
    end

### Rust
    
    
    use google_cloud_storage::client::StorageControl;
    use google_cloud_storage::model::bucket::Website;
    use google_cloud_wkt::FieldMask;
    
    pub async fn sample(
        client: &StorageControl,
        bucket_id: &str,
        main_page_suffix: &str,
        not_found_page: &str,
    ) -> anyhow::Result<()> {
        let bucket = client
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        let metageneration = bucket.metageneration;
        let website = Website::new()
            .set_main_page_suffix(main_page_suffix)
            .set_not_found_page(not_found_page);
        let bucket = client
            .update_bucket()
            .set_bucket(bucket.set_website(website))
            .set_if_metageneration_match(metageneration)
            .set_update_mask(FieldMask::default().set_paths(["website"]))
            .send()
            .await?;
        println!(
            "Website configuration for bucket {} defined as: {:?}",
            bucket_id, bucket.website
        );
        Ok(())
    }

### REST APIs

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create a JSON file that sets the `mainPageSuffix` and `notFoundPage` properties in a `website` object to the desired pages:
         
         {
           "website":{
             "mainPageSuffix": "index.html",
             "notFoundPage": "404.html"
           }
         }

  3. Use [`cURL`](http://curl.haxx.se/) to call the [JSON API](https://docs.cloud.google.com/storage/docs/json_api) with a [`PATCH` Bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets/patch) request. For www.example.com:
         
         curl -X PATCH --data-binary @web-config.json \
           -H "Authorization: $(gcloud auth print-access-token)" \
           -H "Content-Type: application/json" \
           "https://storage.googleapis.com/storage/v1/b/www.example.com"




### XML API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. Create an XML file that sets the `MainPageSuffix` and `NotFoundPage` elements in a `WebsiteConfiguration` element to the desired pages:
         
         <WebsiteConfiguration>
           <MainPageSuffix>index.html</MainPageSuffix>
           <NotFoundPage>404.html</NotFoundPage>
         </WebsiteConfiguration>

  3. Use [`cURL`](http://curl.haxx.se/) to call the [XML API](https://docs.cloud.google.com/storage/docs/xml-api/overview) with a [`PUT` Bucket](https://docs.cloud.google.com/storage/docs/xml-api/put-bucket-metadata) request and `websiteConfig` query string parameter. For www.example.com:
         
         curl -X PUT --data-binary @web-config.xml \
           -H "Authorization: $(gcloud auth print-access-token)" \
           https://storage.googleapis.com/www.example.com?websiteConfig


**Note:** Change or remove these settings with additional `PUT` requests and view these settings with a `GET` request.

## Testing the website

**Note:** Depending on your domain registration service, it may take hours or longer for your `CNAME` record to begin routing requests to your Cloud Storage bucket.

Verify that content is served from the bucket by requesting the domain name in a browser. You can do this with a path to an object or with just the domain name, if you set the `MainPageSuffix` property.

For example, if you have an object named `test.html` stored in a bucket named `www.example.com`, check that it's accessible by going to `www.example.com/test.html` in your browser.

## Clean up

After you finish the tutorial, you can clean up the resources that you created so that they stop using quota and incurring charges. The following sections describe how to delete or turn off these resources. 

### Deleting the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 

**Note:** If you do not want to delete the entire project, you can alternatively [delete the bucket](https://docs.cloud.google.com/storage/docs/deleting-buckets) that you used for hosting your website.

## What's next

  * [See examples and tips for using buckets to host a static website](https://docs.cloud.google.com/storage/docs/static-website).
  * [Visit the troubleshooting section for hosting a static website](https://docs.cloud.google.com/storage/docs/troubleshooting#static-website).
  * [Learn about hosting static assets for a dynamic website](https://docs.cloud.google.com/storage/docs/static-website#tip-dynamic).
  * [Learn about all web serving options](https://docs.cloud.google.com/solutions/web-serving-overview).
  * [Try Google Cloud jump start solutions that use Cloud Storage](https://docs.cloud.google.com/architecture/storage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
