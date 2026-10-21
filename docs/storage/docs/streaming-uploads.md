---
url: https://docs.cloud.google.com/storage/docs/streaming-uploads/
title: Streaming uploads \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:13.379458+00:00
---

# Streaming uploads  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/streaming-uploads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Streaming uploads Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage supports streaming data to a bucket without requiring that the data first be saved to a file. This is useful when you want to upload data but don't know the final size at the start of the upload, such as when generating the upload data from a process, or when compressing an object on-the-fly.

## Using checksum validation when streaming

Because a checksum can only be supplied in the initial request of an upload, it's often not feasible to use Cloud Storage's [checksum validation](https://docs.cloud.google.com/storage/docs/data-validation) when streaming. It's recommended that you always use checksum validation, and you can manually do so after a streaming upload completes; however, validating after the transfer completes means that any corrupted data is accessible during the time it takes to confirm the corruption and remove it.

If you require checksum validation prior to the upload completing and the data becoming accessible, then you shouldn't use a streaming upload. You should use a different [upload option](https://docs.cloud.google.com/storage/docs/uploads) that performs checksum validation prior to finalizing the object.

## Required roles

To get the permissions that you need to stream uploads, ask your administrator to grant you one of the following roles:

  * For uploads that include an [Object Retention Lock](https://docs.cloud.google.com/storage/docs/object-lock), ask your administrator to grant you the Storage Object Admin (`roles/storage.objectAdmin`) IAM role for the bucket.

  * For all other cases, ask your administrator to grant you the Storage Object User (`roles/storage.objectUser`) IAM role for the bucket.




These predefined roles contain the permissions required to stream uploads to Cloud Storage. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.objects.create`
  * `storage.objects.delete`
    * This permission is only required for uploads that overwrite an existing object.
  * `storage.objects.list`
    * This permission is only required for using the Google Cloud CLI to perform the instructions on this page.
  * `storage.objects.setRetention`
    * This permission is only required for uploads that include an Object Retention Lock.



You can also get these permissions with other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions) or [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles).

For information about granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

## Stream an upload

The following examples show how to perform a streaming upload from a process to a Cloud Storage object:

### Console

The Google Cloud console does not support streaming uploads. Use the gcloud CLI instead.

### Command line

  1. Pipe the data to the [`gcloud storage cp` command](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) and use a dash for the source URL:
         
         PROCESS_NAME | gcloud storage cp - gs://BUCKET_NAME/OBJECT_NAME

Where:

     * `PROCESS_NAME` is the name of the process from which you are collecting data. For example, `collect_measurements`.
     * `BUCKET_NAME` is the name of the bucket containing the object. For example, `my_app_bucket`.
     * `OBJECT_NAME` is the name of the object that is created from the data. For example, `data_measurements`.



### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name, int desired_line_count) {
      std::string const text = "Lorem ipsum dolor sit amet";
      gcs::ObjectWriteStream stream =
          client.WriteObject(bucket_name, object_name);
    
      for (int lineno = 0; lineno != desired_line_count; ++lineno) {
        // Add 1 to the counter, because it is conventional to number lines
        // starting at 1.
        stream << (lineno + 1) << ": " << text << "\n";
      }
    
      stream.Close();
    
      StatusOr<gcs::ObjectMetadata> metadata = std::move(stream).metadata();
      if (!metadata) throw std::move(metadata).status();
      std::cout << "Successfully wrote to object " << metadata->name()
                << " its size is: " << metadata->size()
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
    	"bytes"
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // streamFileUpload uploads an object via a stream.
    func streamFileUpload(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	b := []byte("Hello world.")
    	buf := bytes.NewBuffer(b)
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*50)
    	defer cancel()
    
    	// Upload an object with storage.Writer.
    	wc := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).[NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter)(ctx)
    	wc.ChunkSize = 0 // note retries are not supported for chunk size 0.
    
    	if _, err = io.Copy(wc, buf); err != nil {
    		return fmt.Errorf("io.Copy: %w", err)
    	}
    	// Data can continue to be added to the file until the writer is closed.
    	if err := wc.Close(); err != nil {
    		return fmt.Errorf("Writer.Close: %w", err)
    	}
    	fmt.Fprintf(w, "%v uploaded to %v.\n", object, bucket)
    
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.[WriteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.WriteChannel.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.io.IOException;
    import java.nio.ByteBuffer;
    import java.nio.charset.StandardCharsets;
    
    public class StreamObjectUpload {
    
      public static void streamObjectUpload(
          [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) projectId, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bucketName, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) objectName, [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) contents) throws IOException {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The string of contents you wish to upload
        // String contents = "Hello world!";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().getService();
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
        [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfo = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(blobId).build();
        byte[] content = contents.getBytes(StandardCharsets.UTF_8);
        try ([WriteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.WriteChannel.html) writer = storage.[writer](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_writer_com_google_cloud_storage_BlobInfo_com_google_cloud_storage_Storage_BlobWriteOption____)(blobInfo)) {
          writer.write(ByteBuffer.wrap(content));
          System.out.println(
              "Wrote to " + objectName + " in bucket " + bucketName + " using a WriteChannel.");
        }
      }
    }
    

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The new ID for your GCS file
    // const destFileName = 'your-new-file-name';
    
    // The content to be uploaded in the GCS file
    // const contents = 'your file content';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Import Node.js stream
    const stream = require('stream');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    // Get a reference to the bucket
    const myBucket = storage.bucket(bucketName);
    
    // Create a reference to a file object
    const file = myBucket.file(destFileName);
    
    // Create a pass through stream from a string
    const passthroughStream = new stream.PassThrough();
    passthroughStream.write(contents);
    passthroughStream.end();
    
    async function streamFileUpload() {
      passthroughStream.pipe(file.[createWriteStream](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/storage/file_2.html)()).on('finish', () => {
        // The file upload is complete
      });
    
      console.log(`${destFileName} uploaded to ${bucketName}`);
    }
    
    streamFileUpload().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    use Google\Cloud\Storage\WriteStream;
    
    /**
     * Upload a chunked file stream.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     * @param string $contents The contents to upload via stream chunks.
     *        (e.g. 'these are my contents')
     */
    function upload_object_stream(string $bucketName, string $objectName, string $contents): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $writeStream = new WriteStream(null, [
            'chunkSize' => 1024 * 256, // 256KB
        ]);
        $uploader = $bucket->getStreamableUploader($writeStream, [
            'name' => $objectName,
        ]);
        $writeStream->setUploader($uploader);
        $stream = fopen('data://text/plain,' . $contents, 'r');
        while (($line = stream_get_line($stream, 1024 * 256)) !== false) {
            $writeStream->write($line);
        }
        $writeStream->close();
    
        printf('Uploaded %s to gs://%s/%s' . PHP_EOL, $contents, $bucketName, $objectName);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def upload_blob_from_stream(bucket_name, file_obj, destination_blob_name):
        """Uploads bytes from a stream or other file-like object to a blob."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
    
        # The stream or file (file-like object) from which to read
        # import io
        # file_obj = io.BytesIO()
        # file_obj.write(b"This is test data.")
    
        # The desired name of the uploaded GCS object (blob)
        # destination_blob_name = "storage-object-name"
    
        # Construct a client-side representation of the blob.
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(destination_blob_name)
    
        # Rewind the stream to the beginning. This step can be omitted if the input
        # stream will always be at a correct position.
        file_obj.seek(0)
    
        # Upload data from the stream to your bucket.
        blob.[upload_from_file](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_file)(file_obj)
    
        print(
            f"Stream data uploaded to {destination_blob_name} in bucket {bucket_name}."
        )
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    # The ID of your GCS bucket
    # bucket_name = "your-unique-bucket-name"
    
    # The stream or file (file-like object) from which to read
    # local_file_obj = StringIO.new "This is test data."
    
    # Name of a file in the Storage bucket
    # file_name   = "some_file.txt"
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    bucket  = storage.bucket bucket_name
    
    local_file_obj.rewind
    bucket.[create_file](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Bucket.html) local_file_obj, file_name
    
    puts "Stream data uploaded to #{file_name} in bucket #{bucket_name}"

### Rust
    
    
    use bytes::Bytes;
    use google_cloud_storage::{client::Storage, streaming_source::StreamingSource};
    
    pub async fn sample(client: &Storage, bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "object-to-upload.txt";
        let payload = Payload(100);
        let object = client
            .write_object(format!("projects/_/buckets/{bucket_id}"), NAME, payload)
            .set_if_generation_match(0)
            .send_buffered()
            .await?;
        println!("successfully uploaded object {NAME} to bucket {bucket_id}: {object:?}");
        Ok(())
    }
    
    struct Payload(i32);
    
    impl StreamingSource for Payload {
        type Error = std::convert::Infallible;
        async fn next(&mut self) -> Option<Result<bytes::Bytes, Self::Error>> {
            if self.0 <= 0 {
                return None;
            }
            let value = format!("still have to send {} lines\n", self.0);
            self.0 -= 1;
            Some(Ok(Bytes::from_owner(value)))
        }
    }

### REST APIs

### JSON API

To perform a streaming upload, use one of the following methods:

  * A [resumable upload](https://docs.cloud.google.com/storage/docs/resumable-uploads), with the following adjustments:

    * When uploading the file data itself, use a [multiple chunk upload](https://docs.cloud.google.com/storage/docs/performing-resumable-uploads#chunked-upload).

    * Since you don't know the total file size until you get to the final chunk, use a `*` for the total file size in the `Content-Range` header of intermediate chunks.

For example, if the first chunk you upload has a size of 512 KiB, the `Content-Range` header for the chunk is `bytes 0-524287/*`. If your upload has 64000 bytes remaining after the first chunk, you then send a final chunk that contains the remaining bytes and has a `Content-Range` header with the value `bytes 524288-588287/588288`.

  * A [single-request upload](https://docs.cloud.google.com/storage/docs/uploading-objects), with the following adjustments:

    * Include a [`Transfer-Encoding: chunked` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#chunked), and exclude the [`Content-Length` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength).

    * Construct the request according to the [specification](https://datatracker.ietf.org/doc/html/rfc7230#section-4.1), sending the object data in chunks as it becomes available.




### XML API

To perform a streaming upload, use one of the following methods:

  * An [XML API multipart upload](https://docs.cloud.google.com/storage/docs/multipart-uploads)

  * A [resumable upload](https://docs.cloud.google.com/storage/docs/resumable-uploads), with the following adjustments:

    * When uploading the file data itself, use a [multiple chunk upload](https://docs.cloud.google.com/storage/docs/performing-resumable-uploads#chunked-upload).

    * Since you don't know the total file size until you get to the final chunk, use a `*` for the total file size in the `Content-Range` header of intermediate chunks.

For example, if the first chunk you upload has a size of 512 KiB, the `Content-Range` header for the chunk is `bytes 0-524287/*`. If your upload has 64000 bytes remaining after the first chunk, you then send a final chunk that contains the remaining bytes and has a `Content-Range` header with the value `bytes 524288-588287/588288`.

  * A [single-request upload](https://docs.cloud.google.com/storage/docs/uploading-objects), with the following adjustments:

    * Include a [`Transfer-Encoding: chunked` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#chunked), and exclude the [`Content-Length` header](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#contentlength).

    * Construct the request according to the [specification](https://datatracker.ietf.org/doc/html/rfc7230#section-4.1), sending the object data in chunks as it becomes available.




## What's next

  * [Stream a download](https://docs.cloud.google.com/storage/docs/streaming-reads).
  * Learn more about [decompressive transcoding](https://docs.cloud.google.com/storage/docs/transcoding#decompressive_transcoding).
  * Learn more about [object uploads](https://docs.cloud.google.com/storage/docs/uploads).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
