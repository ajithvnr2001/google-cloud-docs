---
url: https://docs.cloud.google.com/storage/docs/rapid/use-objects-in-zonal-buckets/
title: Read and append to objects in zonal buckets \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:47.375245+00:00
---

# Read and append to objects in zonal buckets  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/rapid/use-objects-in-zonal-buckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Read and append to objects in zonal buckets Stay organized with collections  Save and categorize content based on your preferences. 

You can read from and append data to objects in zonal buckets, which are made available through [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket). Zonal buckets use the [Rapid storage class](https://docs.cloud.google.com/storage/docs/storage-classes#rapid), a high-performance storage class that's optimized for I/O-intensive workloads. Appendable objects let you incrementally add data to a file without needing to rewrite the entire object, helping you more effectively manage continuously flowing data.

This page describes how to read and make appends to objects stored in zonal buckets. It shows you how to perform the following operations:

  * Create and write to an appendable object.

  * Read appendable objects.

  * Pause, resume, and finalize appendable objects.

  * Read the tail end of appendable objects.

  * Optimize write latency with a pool of pre-opened writers.




Before you use this page, you might want to read the following resources:

  * Learn how to [create a zonal bucket](https://docs.cloud.google.com/storage/docs/rapid/create-zonal-buckets).

  * [Upload objects to a bucket](https://docs.cloud.google.com/storage/docs/uploading-objects).




## Make appendable writes to objects

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample uploads an appendable object:
    
    
    namespace gcs = google::cloud::storage;
    auto coro = [](gcs::AsyncClient& client, std::string bucket_name,
                   std::string object_name)
        -> google::cloud::future<google::storage::v2::Object> {
      auto [writer, token] =
          (co_await client.StartAppendableObjectUpload(
               gcs::BucketName(std::move(bucket_name)), std::move(object_name)))
              .value();
      std::cout << "Appendable upload started for object " << object_name << "\n";
    
      token = (co_await writer.Write(std::move(token),
                                     gcs::WritePayload("Some data\n")))
                  .value();
      std::cout << "Wrote initial data.\n";
    
      // Flush the buffered data to the service. This is not a terminal
      // operation. The writer can be used after the flush completes.
      // After a flush, the data is visible to readers.
      auto flush_status = co_await writer.Flush();
      if (!flush_status.ok()) throw std::runtime_error(flush_status.message());
    
      std::cout << "Flush completed. Persisted size is now "
                << std::get<std::int64_t>(writer.PersistedState()) << "\n";
    
      // The writer is still open. We can write more data.
      token = (co_await writer.Write(std::move(token),
                                     gcs::WritePayload("Some more data\n")))
                  .value();
      std::cout << "Wrote more data.\n";
    
      // Finalize the upload to make it a regular object.
      co_return (co_await writer.Finalize(std::move(token))).value();
    };

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample uploads an appendable object:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // createAndWriteAppendableObject creates and uploads a new appendable object in
    // a bucket with the Rapid storage class. The object will not be finalized.
    func createAndWriteAppendableObject(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.[NewGRPCClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_NewGRPCClient)(ctx, storage.[WithAppendableUploads](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_WithAppendableUploads)())
    	if err != nil {
    		return fmt.Errorf("storage.NewGRPCClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	// Create a Writer and write some data.
    	writer := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).[NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter)(ctx)
    
    	if _, err := writer.[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)([]byte("Some data\n")); err != nil {
    		return fmt.Errorf("Writer.Write: %w", err)
    	}
    
    	// Flush the buffered data to the service. This is not a terminal
    	// operation. The Writer can be used after the flush completes.
    	// After a flush, the data is visible to readers.
    	size, err := writer.[Flush](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Flush)()
    	if err != nil {
    		return fmt.Errorf("Writer.Flush: %w", err)
    	}
    	fmt.Fprintf(w, "Flush completed. Persisted size is now %d\n", size)
    
    	// The Writer is still open. We can write more data.
    	if _, err := writer.[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)([]byte("Some more data\n")); err != nil {
    		return fmt.Errorf("Writer.Write: %w", err)
    	}
    
    	// Close the Writer to flush any remaining buffered data.
    	// The object will be unfinalized, which means another writer can
    	// later append to the object.
    	if err := writer.Close(); err != nil {
    		return fmt.Errorf("Writer.Close: %w", err)
    	}
    	fmt.Fprintf(w, "Uploaded object %v\n", object)
    
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample uploads an appendable object:
    
    
    import com.google.cloud.storage.[BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html);
    import com.google.cloud.storage.[BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html).[AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html);
    import com.google.cloud.storage.[BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html);
    import com.google.cloud.storage.[BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html).[CloseAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.CloseAction.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[FlushPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.common.io.ByteStreams;
    import java.io.IOException;
    import java.nio.channels.FileChannel;
    import java.nio.channels.ReadableByteChannel;
    import java.nio.file.Paths;
    import java.util.Locale;
    
    public class CreateAndWriteAppendableObject {
      public static void createAndWriteAppendableObject(
          String bucketName, String objectName, String filePath) throws Exception {
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The path to the file to upload
        // String filePath = "path/to/your/file";
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).[grpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html#com_google_cloud_storage_StorageOptions_grpc__)().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
          [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfo = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(blobId).build();
    
          int flushSize = 64 * 1000;
          [FlushPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.html).[MaxFlushSizeFlushPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.MaxFlushSizeFlushPolicy.html) flushPolicy = [FlushPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.html).[maxFlushSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.html#com_google_cloud_storage_FlushPolicy_maxFlushSize__)(flushSize);
          [BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html) config =
              [BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html).of()
                  .[withCloseAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html#com_google_cloud_storage_BlobAppendableUploadConfig_withCloseAction_com_google_cloud_storage_BlobAppendableUploadConfig_CloseAction_)([CloseAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.CloseAction.html).FINALIZE_WHEN_CLOSING)
                  .[withFlushPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html#com_google_cloud_storage_BlobAppendableUploadConfig_withFlushPolicy_com_google_cloud_storage_FlushPolicy_)(flushPolicy);
          [BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html) uploadSession = storage.[blobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobAppendableUpload_com_google_cloud_storage_BlobInfo_com_google_cloud_storage_BlobAppendableUploadConfig_com_google_cloud_storage_Storage_BlobWriteOption____)(blobInfo, config);
          try ([AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html) channel = uploadSession.[open](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html#com_google_cloud_storage_BlobAppendableUpload_open__)();
              ReadableByteChannel readableByteChannel = FileChannel.open(Paths.get(filePath))) {
            ByteStreams.copy(readableByteChannel, channel);
            // Since the channel is in a try-with-resources block, channel.close()
            // will be implicitly called here, which triggers the finalization.
          } catch (IOException ex) {
            throw new IOException("Failed to upload to object " + blobId.[toGsUtilUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html#com_google_cloud_storage_BlobId_toGsUtilUri__)(), ex);
          }
          [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) result = storage.get(blobId);
          System.out.printf(
              Locale.US,
              "Object %s successfully uploaded",
              [result](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.spi.v1.StorageRpc.RewriteResponse.html#com_google_cloud_storage_spi_v1_StorageRpc_RewriteResponse_result).[getBlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getBlobId__)().[toGsUtilUriWithGeneration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html#com_google_cloud_storage_BlobId_toGsUtilUriWithGeneration__)());
        }
      }
    }
    

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample uploads an appendable object:
    
    
    
    async def storage_create_and_write_appendable_object(
        bucket_name, object_name, grpc_client=None
    ):
        """Uploads an appendable object to zonal bucket.
    
        grpc_client: an existing grpc_client to use, this is only for testing.
        """
    
        if grpc_client is None:
            grpc_client = AsyncGrpcClient()
        writer = AsyncAppendableObjectWriter(
            client=grpc_client,
            bucket_name=bucket_name,
            object_name=object_name,
            generation=0,  # throws `FailedPrecondition` if object already exists.
        )
        # This creates a new appendable object of size 0 and opens it for appending.
        await writer.open()
    
        # appends data to the object
        # you can perform `.append` multiple times as needed. Data will be appended
        # to the end of the object.
        await writer.append(b"Some data")
    
        # Once all appends are done, close the gRPC bidirectional stream.
        await writer.close()
    
        print(
            f"Appended object {object_name} created of size {writer.persisted_size} bytes."
        )
    
    

## Read objects

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample performs a ranged read on a single object:
    
    
    namespace gcs = google::cloud::storage;
    
    // Helper coroutine to count newlines returned by an AsyncReader.
    // This helps consume the data from the read operation.
    auto count_newlines =
        [](gcs::AsyncReader reader,
           gcs::AsyncToken token) -> google::cloud::future<std::uint64_t> {
      std::uint64_t count = 0;
      while (token.valid()) {
        auto [payload, t] = (co_await reader.Read(std::move(token))).value();
        token = std::move(t);
        for (auto const& buffer : payload.contents()) {
          count += std::count(buffer.begin(), buffer.end(), '\n');
        }
      }
      co_return count;
    };
    
    auto coro =
        [&count_newlines](
            gcs::AsyncClient& client, std::string bucket_name,
            std::string object_name) -> google::cloud::future<std::uint64_t> {
      auto descriptor =
          (co_await client.Open(gcs::BucketName(std::move(bucket_name)),
                                std::move(object_name)))
              .value();
    
      auto [reader, token] = descriptor.Read(0, 1024);
    
      co_return co_await count_newlines(std::move(reader), std::move(token));
    };

The following sample performs a full read on a single object:
    
    
    namespace gcs = google::cloud::storage;
    
    // Helper coroutine to count newlines returned by an AsyncReader.
    // This helps consume the data from the read operation.
    auto count_newlines =
        [](gcs::AsyncReader reader,
           gcs::AsyncToken token) -> google::cloud::future<std::uint64_t> {
      std::uint64_t count = 0;
      while (token.valid()) {
        auto [payload, t] = (co_await reader.Read(std::move(token))).value();
        token = std::move(t);
        for (auto const& buffer : payload.contents()) {
          count += std::count(buffer.begin(), buffer.end(), '\n');
        }
      }
      co_return count;
    };
    
    auto coro =
        [&count_newlines](
            gcs::AsyncClient& client, std::string bucket_name,
            std::string object_name) -> google::cloud::future<std::uint64_t> {
      auto descriptor =
          (co_await client.Open(gcs::BucketName(std::move(bucket_name)),
                                std::move(object_name)))
              .value();
    
      auto [reader, token] = descriptor.ReadFromOffset(0);
    
      co_return co_await count_newlines(std::move(reader), std::move(token));
    };

The following sample performs ranged reads on a single object:
    
    
    namespace gcs = google::cloud::storage;
    
    // Helper coroutine to count newlines returned by an AsyncReader.
    auto count_newlines =
        [](gcs::AsyncReader reader,
           gcs::AsyncToken token) -> google::cloud::future<std::uint64_t> {
      std::uint64_t count = 0;
      while (token.valid()) {
        auto [payload, t] = (co_await reader.Read(std::move(token))).value();
        token = std::move(t);
        for (auto const& buffer : payload.contents()) {
          count += std::count(buffer.begin(), buffer.end(), '\n');
        }
      }
      co_return count;
    };
    
    auto coro =
        [&count_newlines](
            gcs::AsyncClient& client, std::string bucket_name,
            std::string object_name) -> google::cloud::future<std::uint64_t> {
      auto descriptor =
          (co_await client.Open(gcs::BucketName(std::move(bucket_name)),
                                std::move(object_name)))
              .value();
    
      auto [r1, t1] = descriptor.Read(0, 1024);
      auto [r2, t2] = descriptor.Read(0, 1024);
      auto [r3, t3] = descriptor.Read(1024, 1024);
    
      auto c1 = count_newlines(std::move(r1), std::move(t1));
      auto c2 = count_newlines(std::move(r2), std::move(t2));
      auto c3 = count_newlines(std::move(r3), std::move(t3));
      co_return (co_await std::move(c1)) + (co_await std::move(c2)) +
          (co_await std::move(c3));
    };

The following sample performs ranged reads on multiple objects (a single read per object):
    
    
    namespace gcs = google::cloud::storage;
    
    // Helper coroutine to count newlines returned by an AsyncReader.
    auto count_newlines =
        [](gcs::AsyncReader reader,
           gcs::AsyncToken token) -> google::cloud::future<std::uint64_t> {
      std::uint64_t count = 0;
      while (token.valid()) {
        auto [payload, t] = (co_await reader.Read(std::move(token))).value();
        token = std::move(t);
        for (auto const& buffer : payload.contents()) {
          count += std::count(buffer.begin(), buffer.end(), '\n');
        }
      }
      co_return count;
    };
    
    auto coro = [&count_newlines](
                    gcs::AsyncClient& client, std::string bucket_name,
                    std::string object_name1, std::string object_name2,
                    std::string object_name3) -> google::cloud::future<void> {
      // List of object names to read (passed as arguments)
      std::vector<std::string> object_names = {object_name1, object_name2,
                                               object_name3};
      std::vector<google::cloud::future<std::uint64_t>> futures;
    
      // Start ranged reads for all objects and collect futures
      // This example opens multiple objects, not one object multiple times.
      for (auto const& name : object_names) {
        auto descriptor =
            (co_await client.Open(gcs::BucketName(bucket_name), name)).value();
        auto [reader, token] = descriptor.Read(0, 1024);
        futures.push_back(count_newlines(std::move(reader), std::move(token)));
      }
    
      // Process futures as they become ready and print results
      while (!futures.empty()) {
        bool progress_made = false;
        for (std::size_t i = 0; i < futures.size(); ++i) {
          if (futures[i].is_ready()) {  // Check if the future is ready
            auto count = futures[i].get();
            std::cout << "Object " << object_names[i] << " read returned "
                      << count << " newlines\n";
            futures.erase(futures.begin() + i);
            object_names.erase(object_names.begin() + i);
            progress_made = true;
            break;  // Restart the loop after modifying the vectors
          }
        }
        if (!progress_made) {
          std::this_thread::sleep_for(
              std::chrono::milliseconds(10));  // Avoid busy spin
        }
      }
    };

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample performs a ranged read on a single object:
    
    
    import (
    	"bytes"
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // openObjectSingleRangedRead reads a single range from an object.
    func openObjectSingleRangedRead(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) ([]byte, error) {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.[NewGRPCClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_NewGRPCClient)(ctx, storage.[WithGRPCBidiReads](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_WithGRPCBidiReads)())
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewGRPCClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	// Read the first KiB of the file and copy into a buffer.
    	r, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).[NewRangeReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewRangeReader)(ctx, 0, 1024)
    	if err != nil {
    		return nil, fmt.Errorf("NewRangeReader: %w", err)
    	}
    	defer r.Close()
    	buf := new(bytes.Buffer)
    	if _, err := io.Copy(buf, r); err != nil {
    		return nil, fmt.Errorf("copying data: %w", err)
    	}
    
    	fmt.Fprintf(w, "Read the first 1024 bytes of %v into a buffer\n", object)
    
    	return buf.[Bytes](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/transfermanager.html#cloud_google_com_go_storage_transfermanager_DownloadBuffer_Bytes)(), nil
    }
    

The following sample performs a full read on a single object:
    
    
    import (
    	"bytes"
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // openObjectReadFullObject reads a full object's data.
    func openObjectReadFullObject(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) ([]byte, error) {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.[NewGRPCClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_NewGRPCClient)(ctx, storage.[WithGRPCBidiReads](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_WithGRPCBidiReads)())
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewGRPCClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	// Read the full object and copy it into a buffer.
    	r, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).[NewReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewReader)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewReader: %w", err)
    	}
    	defer r.Close()
    	buf := new(bytes.Buffer)
    	if _, err := io.Copy(buf, r); err != nil {
    		return nil, fmt.Errorf("copying data: %w", err)
    	}
    
    	fmt.Fprintf(w, "Read the data of %v into a buffer\n", object)
    
    	return buf.[Bytes](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/transfermanager.html#cloud_google_com_go_storage_transfermanager_DownloadBuffer_Bytes)(), nil
    }
    

The following sample performs ranged reads on a single object:
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // openObjectMultipleRangedRead opens a single object using
    // MultiRangeDownloader to download multiple ranges.
    func openObjectMultipleRangedRead(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) ([][]byte, error) {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.[NewGRPCClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_NewGRPCClient)(ctx, storage.[WithGRPCBidiReads](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_WithGRPCBidiReads)())
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewGRPCClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	// Create the MultiRangeDownloader, which opens a stream to the object.
    	mrd, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).[NewMultiRangeDownloader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewMultiRangeDownloader)(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewMultiRangeDownloader: %w", err)
    	}
    
    	// Add some 1 KiB ranges to download. This call is non-blocking. The
    	// provided callback is invoked when the range download is complete.
    	// Each range writes to its own buffer and its own error slot, so the
    	// callbacks can run concurrently without any further synchronization.
    	startOffsets := []int64{0, 1024, 2048}
    	var dataBufs [3]bytes.Buffer
    	var errs [3]error
    	for i, off := range startOffsets {
    		mrd.[Add](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_MultiRangeDownloader_Add)(&dataBufs[i], off, 1024, func(off, length int64, err error) {
    			errs[i] = err
    		})
    	}
    
    	// Wait for all downloads to complete.
    	mrd.Wait()
    	if err := errors.Join(errs[:]...); err != nil {
    		return nil, fmt.Errorf("one or more downloads failed: %w", err)
    	}
    	if err := mrd.Close(); err != nil {
    		return nil, fmt.Errorf("MultiRangeDownloader.Close: %w", err)
    	}
    
    	fmt.Fprintf(w, "Read the ranges of %v into memory\n", object)
    
    	// Collect the byte slices
    	var byteSlices [][]byte
    	for i := range dataBufs {
    		byteSlices = append(byteSlices, dataBufs[i].[Bytes](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/transfermanager.html#cloud_google_com_go_storage_transfermanager_DownloadBuffer_Bytes)())
    	}
    
    	return byteSlices, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample performs a ranged read on a single object:
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html);
    import com.google.cloud.storage.[RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html);
    import com.google.cloud.storage.[ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.util.concurrent.TimeUnit;
    
    public class OpenObjectSingleRangedRead {
      public static void openObjectSingleRangedRead(
          String bucketName, String objectName, long offset, int length) throws Exception {
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The beginning of the range
        // long offset = 0
    
        // The maximum number of bytes to read from the object.
        // int length = 64;
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).[grpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html#com_google_cloud_storage_StorageOptions_grpc__)().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
          ApiFuture<BlobReadSession> futureBlobReadSession = storage.[blobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobReadSession_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____)(blobId);
    
          try ([BlobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html) blobReadSession = futureBlobReadSession.get(10, TimeUnit.SECONDS)) {
            // Define the range of bytes to read.
            [RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html) rangeSpec = [RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html).of(offset, length);
            ApiFuture<byte[]> future =
                [blobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobReadSession_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____).[readAs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html#com_google_cloud_storage_BlobReadSession__Projection_readAs_com_google_cloud_storage_ReadProjectionConfig_Projection__)([ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html).[asFutureBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html#com_google_cloud_storage_ReadProjectionConfigs_asFutureBytes__)().withRangeSpec(rangeSpec));
    
            // Wait for the read to complete.
            byte[] bytes = future.get();
    
            System.out.println(
                "Successfully read "
                    + bytes.length
                    + " bytes from object "
                    + objectName
                    + " in bucket "
                    + bucketName);
          }
        }
      }
    }

The following sample performs a full read on a single object:
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html);
    import com.google.cloud.storage.[ReadAsChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadAsChannel.html);
    import com.google.cloud.storage.[ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.nio.ByteBuffer;
    import java.nio.channels.ScatteringByteChannel;
    import java.util.Locale;
    import java.util.concurrent.TimeUnit;
    
    public class OpenObjectReadFullObject {
      public static void openObjectReadFullObject(String bucketName, String objectName)
          throws Exception {
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object to read
        // String objectName = "your-object-name";
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).[grpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html#com_google_cloud_storage_StorageOptions_grpc__)().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
          ApiFuture<BlobReadSession> futureBlobReadSession = storage.[blobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobReadSession_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____)(blobId);
    
          try ([BlobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html) blobReadSession = futureBlobReadSession.get(10, TimeUnit.SECONDS)) {
    
            [ReadAsChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadAsChannel.html) readAsChannelConfig = [ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html).[asChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html#com_google_cloud_storage_ReadProjectionConfigs_asChannel__)();
            try (ScatteringByteChannel channel = [blobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobReadSession_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____).[readAs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html#com_google_cloud_storage_BlobReadSession__Projection_readAs_com_google_cloud_storage_ReadProjectionConfig_Projection__)(readAsChannelConfig)) {
              long totalBytesRead = 0;
              ByteBuffer buffer = ByteBuffer.allocate(64 * 1024);
              int bytesRead;
    
              while ((bytesRead = channel.read(buffer)) != -1) {
                totalBytesRead += bytesRead;
                buffer.clear();
              }
    
              System.out.printf(
                  Locale.US,
                  "Successfully read a total of %d bytes from object %s%n",
                  totalBytesRead,
                  blobId.[toGsUtilUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html#com_google_cloud_storage_BlobId_toGsUtilUri__)());
            }
          }
        }
      }
    }

The following sample performs ranged reads on a single object:
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.core.[ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html);
    import com.google.cloud.storage.[RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html);
    import com.google.cloud.storage.[ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.common.collect.ImmutableList;
    import java.util.List;
    import java.util.concurrent.TimeUnit;
    
    public class OpenObjectMultipleRangedRead {
      public static void openObjectMultipleRangedRead(
          String bucketName, String objectName, long offset1, int length1, long offset2, int length2)
          throws Exception {
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The beginning of the range 1
        // long offset = 0
    
        // The maximum number of bytes to read in range 1
        // int length = 16;
    
        // The beginning of the range 2
        // long offset = 16
    
        // The maximum number of bytes to read in range 2
        // int length = 32;
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).[grpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html#com_google_cloud_storage_StorageOptions_grpc__)().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
          ApiFuture<BlobReadSession> futureBlobReadSession = storage.[blobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobReadSession_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____)(blobId);
          [RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html) rangeSpec1 = [RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html).of(offset1, length1);
          [RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html) rangeSpec2 = [RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html).of(offset2, length2);
    
          try ([BlobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html) blobReadSession = futureBlobReadSession.get(10, TimeUnit.SECONDS)) {
            ApiFuture<byte[]> future1 =
                [blobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobReadSession_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____).[readAs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html#com_google_cloud_storage_BlobReadSession__Projection_readAs_com_google_cloud_storage_ReadProjectionConfig_Projection__)([ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html).[asFutureBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html#com_google_cloud_storage_ReadProjectionConfigs_asFutureBytes__)().withRangeSpec(rangeSpec1));
            ApiFuture<byte[]> future2 =
                [blobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobReadSession_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____).[readAs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html#com_google_cloud_storage_BlobReadSession__Projection_readAs_com_google_cloud_storage_ReadProjectionConfig_Projection__)([ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html).[asFutureBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html#com_google_cloud_storage_ReadProjectionConfigs_asFutureBytes__)().withRangeSpec(rangeSpec2));
    
            List<byte[]> allBytes = [ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html).[allAsList](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html#com_google_api_core_ApiFutures__V_allAsList_java_lang_Iterable___extends_com_google_api_core_ApiFuture___extends_V___)(ImmutableList.of(future1, future2)).get();
    
            byte[] bytes1 = allBytes.get(0);
            byte[] bytes2 = allBytes.get(1);
    
            System.out.println(
                "Successfully read "
                    + bytes1.length
                    + " bytes from range 1 and "
                    + bytes2.length
                    + " bytes from range 2.");
          }
        }
      }
    }
    

The following sample performs ranged reads on multiple objects:
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.api.core.[ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html);
    import com.google.cloud.storage.[RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html);
    import com.google.cloud.storage.[ReadAsFutureBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadAsFutureBytes.html);
    import com.google.cloud.storage.[ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.common.util.concurrent.MoreExecutors;
    import java.util.ArrayList;
    import java.util.List;
    import java.util.concurrent.TimeUnit;
    
    public class OpenMultipleObjectsRangedRead {
      public static void multipleObjectsSingleRangedRead(
          String bucketName, List<String> objectNames, long startOffset, int length) throws Exception {
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS objects to read
        // List<String> objectName = Arrays.asList("object-1", "object-2", "object-3");
    
        [RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html) singleRange = [RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html).of(startOffset, length);
        [ReadAsFutureBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadAsFutureBytes.html) rangeConfig =
            [ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html).[asFutureBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html#com_google_cloud_storage_ReadProjectionConfigs_asFutureBytes__)().withRangeSpec(singleRange);
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).[grpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html#com_google_cloud_storage_StorageOptions_grpc__)().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          List<ApiFuture<byte[]>> futuresToWaitOn = new ArrayList<>();
    
          System.out.printf(
              "Initiating single ranged read [%d, %d] on %d objects...%n",
              startOffset, startOffset + length - 1, objectNames.size());
    
          for (String objectName : objectNames) {
            [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
            ApiFuture<BlobReadSession> futureReadSession = storage.[blobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobReadSession_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____)(blobId);
    
            ApiFuture<byte[]> readAndCloseFuture =
                [ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html).[transformAsync](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html#com_google_api_core_ApiFutures__I_O_transformAsync_com_google_api_core_ApiFuture_I__com_google_api_core_ApiAsyncFunction_I_O__)(
                    futureReadSession,
                    (BlobReadSession session) -> {
                      ApiFuture<byte[]> readFuture = session.readAs(rangeConfig);
    
                      readFuture.addListener(
                          () -> {
                            try {
                              session.close();
                            } catch (java.io.IOException e) {
                              System.err.println(
                                  "WARN: Background error while closing session: " + e.getMessage());
                            }
                          },
                          MoreExecutors.directExecutor());
                      return readFuture;
                    },
                    MoreExecutors.directExecutor());
    
            futuresToWaitOn.add(readAndCloseFuture);
          }
          [ApiFutures](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html).[allAsList](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFutures.html#com_google_api_core_ApiFutures__V_allAsList_java_lang_Iterable___extends_com_google_api_core_ApiFuture___extends_V___)(futuresToWaitOn).get(30, TimeUnit.SECONDS);
    
          System.out.println("All concurrent single-ranged read operations are complete.");
        }
      }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample performs a ranged read on a single object:
    
    
    async def storage_open_object_single_ranged_read(
        bucket_name, object_name, start_byte, size, grpc_client=None
    ):
        """Downloads a range of bytes from an object.
    
        grpc_client: an existing grpc_client to use, this is only for testing.
        """
        if grpc_client is None:
            grpc_client = AsyncGrpcClient()
    
        mrd = AsyncMultiRangeDownloader(grpc_client, bucket_name, object_name)
    
        try:
            # Open the object, mrd always opens in read mode.
            await mrd.open()
    
            # requested range will be downloaded into this buffer, user may provide
            # their own buffer or file-like object.
            output_buffer = BytesIO()
            await mrd.download_ranges([(start_byte, size, output_buffer)])
        finally:
            if mrd.is_stream_open:
                await mrd.close()
    
        # Downloaded size can differ from requested size if object is smaller.
        # mrd will download at most up to the end of the object.
        downloaded_size = output_buffer.getbuffer().nbytes
        print(f"Downloaded {downloaded_size} bytes from {object_name}")
    
    

The following sample performs a full read on a single object:
    
    
    async def storage_open_object_read_full_object(
        bucket_name, object_name, grpc_client=None
    ):
        """Downloads the entire content of an object using a multi-range downloader.
    
        grpc_client: an existing grpc_client to use, this is only for testing.
        """
        if grpc_client is None:
            grpc_client = AsyncGrpcClient()
    
        # mrd = Multi-Range-Downloader
        mrd = AsyncMultiRangeDownloader(grpc_client, bucket_name, object_name)
    
        try:
            # Open the object, mrd always opens in read mode.
            await mrd.open()
    
            # This could be any buffer or file-like object.
            output_buffer = BytesIO()
            # A download range of (0, 0) means to read from the beginning to the end.
            await mrd.download_ranges([(0, 0, output_buffer)])
        finally:
            if mrd.is_stream_open:
                await mrd.close()
    
        downloaded_bytes = output_buffer.getvalue()
        print(
            f"Downloaded all {len(downloaded_bytes)} bytes from object {object_name} in bucket {bucket_name}."
        )
    
    

The following sample performs ranged reads on a single object:
    
    
    async def storage_open_object_multiple_ranged_read(
        bucket_name, object_name, grpc_client=None
    ):
        """Downloads multiple ranges of bytes from a single object into different buffers.
    
        grpc_client: an existing grpc_client to use, this is only for testing.
        """
        if grpc_client is None:
            grpc_client = AsyncGrpcClient()
    
        mrd = AsyncMultiRangeDownloader(grpc_client, bucket_name, object_name)
    
        try:
            # Open the object, mrd always opens in read mode.
            await mrd.open()
    
            # Specify four different buffers to download ranges into.
            buffers = [BytesIO(), BytesIO(), BytesIO(), BytesIO()]
    
            # Define the ranges to download. Each range is a tuple of (start_byte, size, buffer).
            # All ranges will download 10 bytes from different starting positions.
            # We choose arbitrary start bytes for this example. An object should be large enough.
            # A user can choose any start byte between 0 and `object_size`.
            # If `start_bytes` is greater than `object_size`, mrd will throw an error.
            ranges = [
                (0, 10, buffers[0]),
                (20, 10, buffers[1]),
                (40, 10, buffers[2]),
                (60, 10, buffers[3]),
            ]
    
            await mrd.download_ranges(ranges)
    
        finally:
            await mrd.close()
    
        # Print the downloaded content from each buffer.
        for i, output_buffer in enumerate(buffers):
            downloaded_size = output_buffer.getbuffer().nbytes
            print(
                f"Downloaded {downloaded_size} bytes into buffer {i + 1} from start byte {ranges[i][0]}: {output_buffer.getvalue()}"
            )
    
    

The following sample performs ranged reads on multiple objects:
    
    
    async def storage_open_multiple_objects_ranged_read(
        bucket_name, object_names, grpc_client=None
    ):
        """Downloads a range of bytes from multiple objects concurrently.
    
        grpc_client: an existing grpc_client to use, this is only for testing.
        """
        if grpc_client is None:
            grpc_client = AsyncGrpcClient()
    
        async def _download_range(object_name):
            """Helper coroutine to download a range from a single object."""
            mrd = AsyncMultiRangeDownloader(grpc_client, bucket_name, object_name)
            try:
                # Open the object, mrd always opens in read mode.
                await mrd.open()
    
                # Each object downloads the first 100 bytes.
                start_byte = 0
                size = 100
    
                # requested range will be downloaded into this buffer, user may provide
                # their own buffer or file-like object.
                output_buffer = BytesIO()
                await mrd.download_ranges([(start_byte, size, output_buffer)])
            finally:
                if mrd.is_stream_open:
                    await mrd.close()
    
            # Downloaded size can differ from requested size if object is smaller.
            # mrd will download at most up to the end of the object.
            downloaded_size = output_buffer.getbuffer().nbytes
            print(f"Downloaded {downloaded_size} bytes from {object_name}")
    
        download_tasks = [_download_range(name) for name in object_names]
        await asyncio.gather(*download_tasks)
    
    

### Rust

The following sample performs a ranged read on a single object:
    
    
    use google_cloud_storage::client::Storage;
    use google_cloud_storage::model_ext::ReadRange;
    
    pub async fn sample(
        client: &Storage,
        bucket: &str,
        object: &str,
        start: u64,
        end: u64,
        destination_file_name: &str,
    ) -> anyhow::Result<()> {
        let count = end - start + 1;
        let (metadata, mut reader) = client
            .open_object(format!("projects/_/buckets/{bucket}"), object)
            .send_and_read(ReadRange::segment(start, count))
            .await?;
    
        let mut content = Vec::new();
        while let Some(data) = reader.next().await.transpose()? {
            content.extend_from_slice(&data);
        }
    
        tokio::fs::write(destination_file_name, content).await?;
    
        println!(
            "Downloaded bytes from {start} to {end} of object {object} in bucket {bucket} to {destination_file_name}."
        );
        println!("Metadata: {:?}", metadata.object());
        Ok(())
    }

The following sample performs a full read on a single object:
    
    
    use google_cloud_storage::client::Storage;
    use google_cloud_storage::model_ext::ReadRange;
    
    pub async fn sample(
        client: &Storage,
        bucket: &str,
        object: &str,
        destination_file_name: &str,
    ) -> anyhow::Result<()> {
        let (metadata, mut reader) = client
            .open_object(format!("projects/_/buckets/{bucket}"), object)
            .send_and_read(ReadRange::all())
            .await?;
    
        let mut content = Vec::new();
        while let Some(data) = reader.next().await.transpose()? {
            content.extend_from_slice(&data);
        }
    
        tokio::fs::write(destination_file_name, content).await?;
    
        println!("Downloaded object {object} in bucket {bucket} to {destination_file_name}.");
        println!("Metadata: {:?}", metadata.object());
        Ok(())
    }

The following sample performs ranged reads on a single object:
    
    
    use google_cloud_storage::client::Storage;
    use google_cloud_storage::model_ext::ReadRange;
    
    pub async fn sample(client: &Storage, bucket: &str, object: &str) -> anyhow::Result<()> {
        let bucket_name = format!("projects/_/buckets/{bucket}");
    
        // 1. Open the connection and read the first range.
        let (descriptor, mut reader) = client
            .open_object(bucket_name, object)
            .send_and_read(ReadRange::head(5))
            .await?;
    
        let mut content = Vec::new();
        while let Some(data) = reader.next().await.transpose()? {
            content.extend_from_slice(&data);
        }
        println!(
            "Read first range from {object} in {bucket}. Content: {:?}",
            String::from_utf8_lossy(&content)
        );
    
        // 2. Read another range.
        let mut reader = descriptor.read_range(ReadRange::segment(5, 5)).await;
    
        let mut content = Vec::new();
        while let Some(data) = reader.next().await.transpose()? {
            content.extend_from_slice(&data);
        }
        println!(
            "Read second range from {object} in {bucket}. Content: {:?}",
            String::from_utf8_lossy(&content)
        );
    
        println!("Metadata: {:?}", descriptor.object());
        Ok(())
    }

The following sample performs ranged reads on multiple objects:
    
    
    use google_cloud_storage::client::Storage;
    use google_cloud_storage::model_ext::ReadRange;
    use google_cloud_storage::object_descriptor::ObjectDescriptor;
    use std::collections::HashMap;
    use tokio::task::JoinSet;
    
    pub async fn sample(client: &Storage, bucket: &str, object_names: &[&str]) -> anyhow::Result<()> {
        let bucket_name = format!("projects/_/buckets/{bucket}");
    
        async fn read_footer(
            client: &Storage,
            bucket_name: &str,
            object_name: &str,
        ) -> anyhow::Result<(ObjectDescriptor, Vec<u8>, String)> {
            // Reading the last 8 bytes is common in Parquet and other column-oriented formats
            // with a footer.
            let (descriptor, mut reader) = client
                .open_object(bucket_name, object_name)
                .send_and_read(ReadRange::tail(8))
                .await?;
    
            let mut footer = Vec::new();
            while let Some(data) = reader.next().await.transpose()? {
                footer.extend_from_slice(&data);
            }
            Ok((descriptor, footer, object_name.to_string()))
        }
    
        let mut set = JoinSet::new();
        for o in object_names {
            let client = client.clone();
            let bucket_name = bucket_name.clone();
            let object_name = o.to_string();
            set.spawn(async move { read_footer(&client, &bucket_name, &object_name).await });
        }
    
        let mut descriptors = HashMap::new();
        while let Some(result) = set.join_next().await {
            let (descriptor, footer, object_name) = result??;
            println!("The footer for object {object_name} is {footer:?}");
            descriptors.insert(object_name, (descriptor, footer));
        }
    
        // Use the descriptors in the map to read more ranges.
    
        Ok(())
    }

## Pause and resume an object

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample pauses and resumes an appendable object:
    
    
    namespace gcs = google::cloud::storage;
    auto coro = [](gcs::AsyncClient& client, std::string bucket_name,
                   std::string object_name)
        -> google::cloud::future<google::storage::v2::Object> {
      // Start an appendable upload and write some data.
      auto [writer, token] = (co_await client.StartAppendableObjectUpload(
                                  gcs::BucketName(bucket_name), object_name))
                                 .value();
      std::cout << "Appendable upload started.\n";
      token = (co_await writer.Write(std::move(token),
                                     gcs::WritePayload("paused data\n")))
                  .value();
    
      // The writer is closed, but the upload is not finalized. This "pauses" the
      // upload, as the object remains appendable.
      auto close_status = co_await writer.Close();
      if (!close_status.ok()) throw std::runtime_error(close_status.message());
      std::cout << "Upload paused.\n";
    
      // To resume the upload we need the object's generation. We can use the
      // regular GCS client to get the latest metadata.
      auto regular_client = gcs::Client();
      auto metadata =
          regular_client.GetObjectMetadata(bucket_name, object_name).value();
      std::cout << "Object generation is " << metadata.generation() << "\n";
    
      // Now resume the upload.
      std::tie(writer, token) =
          (co_await client.ResumeAppendableObjectUpload(
               gcs::BucketName(bucket_name), object_name, metadata.generation()))
              .value();
      std::cout << "Upload resumed from offset "
                << std::get<std::int64_t>(writer.PersistedState()) << "\n";
    
      // Append the rest of the data.
      token = (co_await writer.Write(std::move(token),
                                     gcs::WritePayload("resumed data\n")))
                  .value();
    
      // Finalize the upload and return the object metadata.
      co_return (co_await writer.Finalize(std::move(token))).value();
    };

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample pauses and resumes an appendable object:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // pauseAndResumeAppendableUpload creates a new unfinalized appendable object in
    // a bucket with the Rapid storage class, closes the Writer, then re-opens the
    // object for writing using NewWriterFromAppendableObject.
    func pauseAndResumeAppendableUpload(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.[NewGRPCClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_NewGRPCClient)(ctx, storage.[WithAppendableUploads](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_WithAppendableUploads)())
    	if err != nil {
    		return fmt.Errorf("storage.NewGRPCClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	// Start an appendable upload and write some data.
    	writer := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).[NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter)(ctx)
    
    	if _, err := writer.[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)([]byte("Some data\n")); err != nil {
    		return fmt.Errorf("Writer.Write: %w", err)
    	}
    
    	// The writer is closed, but the upload is not finalized. This "pauses" the
    	// upload, as the object remains appendable.
    	if err := writer.Close(); err != nil {
    		return fmt.Errorf("Writer.Close: %w", err)
    	}
    	fmt.Fprintf(w, "Uploaded unfinalized object %v\n", object)
    
    	// To resume the upload we need the object's generation. We can get this
    	// from the previous Writer after close.
    	gen := writer.Attrs().[Generation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Generation)
    
    	// Now resume the upload. Writer options including finalization can be
    	// passed on calling this constructor.
    	appendWriter, offset, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).[Generation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Generation)(gen).[NewWriterFromAppendableObject](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriterFromAppendableObject)(
    		ctx, &storage.[AppendableWriterOpts](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_AppendableWriterOpts){
    			FinalizeOnClose: true,
    		},
    	)
    	if err != nil {
    		return fmt.Errorf("NewWriterFromAppendableObject: %w", err)
    	}
    	fmt.Fprintf(w, "Resuming upload from offset %v\n", offset)
    
    	// Append the rest of the data and close the Writer to finalize.
    	if _, err := append[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)r.[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)([]byte("resumed data\n")); err != nil {
    		return fmt.Errorf("appendWriter.Write: %w", err)
    	}
    	if err := appendWriter.Close(); err != nil {
    		return fmt.Errorf("Writer.Close: %w", err)
    	}
    	fmt.Fprintf(w, "Uploaded and finalized object %v\n", object)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample pauses and resumes an appendable object:
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html);
    import com.google.cloud.storage.[BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html).[AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html);
    import com.google.cloud.storage.[BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html);
    import com.google.cloud.storage.[BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html).[CloseAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.CloseAction.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageChannelUtils](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageChannelUtils.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.common.io.ByteStreams;
    import java.io.IOException;
    import java.nio.ByteBuffer;
    import java.nio.channels.FileChannel;
    import java.nio.charset.StandardCharsets;
    import java.nio.file.Paths;
    import java.util.Locale;
    
    public class PauseAndResumeAppendableObjectUpload {
      public static void pauseAndResumeAppendableObjectUpload(
          String bucketName, String objectName, String filePath) throws Exception {
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        // The path to the file to upload
        // String filePath = "path/to/your/file";
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).[grpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html#com_google_cloud_storage_StorageOptions_grpc__)().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
          [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfo = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(blobId).build();
    
          // --- Step 1: Initial string write (PAUSE) ---
          // Default close action will be CLOSE_WITHOUT_FINALIZING
          [BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html) initialConfig = [BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html).of();
          [BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html) initialUploadSession =
              storage.[blobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobAppendableUpload_com_google_cloud_storage_BlobInfo_com_google_cloud_storage_BlobAppendableUploadConfig_com_google_cloud_storage_Storage_BlobWriteOption____)(blobInfo, initialConfig);
    
          try ([AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html) channel = initialUploadSession.[open](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html#com_google_cloud_storage_BlobAppendableUpload_open__)()) {
            String initialData = "Initial data segment.\n";
            ByteBuffer buffer = ByteBuffer.[wrap](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HttpStorageRpcHasherHelper.html#com_google_cloud_storage_HttpStorageRpcHasherHelper_wrap_java_io_OutputStream_boolean_)(initialData.getBytes(StandardCharsets.UTF_8));
            long totalBytesWritten = [StorageChannelUtils](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageChannelUtils.html).[blockingEmptyTo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageChannelUtils.html#com_google_cloud_storage_StorageChannelUtils_blockingEmptyTo_java_nio_ByteBuffer_java_nio_channels_WritableByteChannel_)(buffer, channel);
            channel.[flush](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_flush__)();
    
            System.out.printf(
                Locale.US, "Wrote %d bytes (initial string) in first segment.\n", totalBytesWritten);
          } catch (IOException ex) {
            throw new IOException("Failed initial upload to object " + blobId.[toGsUtilUri](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html#com_google_cloud_storage_BlobId_toGsUtilUri__)(), ex);
          }
    
          [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) existingBlob = storage.get(blobId);
          long currentObjectSize = existingBlob.[getSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getSize__)();
          System.out.printf(
              Locale.US,
              "Initial upload paused. Currently uploaded size: %d bytes\n",
              currentObjectSize);
    
          // --- Step 2: Resume upload with file content and finalize ---
          // Use FINALIZE_WHEN_CLOSING to ensure the object is finalized on channel closure.
          [BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html) resumeConfig =
              [BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html).of().[withCloseAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html#com_google_cloud_storage_BlobAppendableUploadConfig_withCloseAction_com_google_cloud_storage_BlobAppendableUploadConfig_CloseAction_)([CloseAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.CloseAction.html).FINALIZE_WHEN_CLOSING);
          [BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html) resumeUploadSession =
              storage.[blobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobAppendableUpload_com_google_cloud_storage_BlobInfo_com_google_cloud_storage_BlobAppendableUploadConfig_com_google_cloud_storage_Storage_BlobWriteOption____)(existingBlob.[toBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html#com_google_cloud_storage_Blob_toBuilder__)().build(), resumeConfig);
    
          try (FileChannel fileChannel = FileChannel.open(Paths.get(filePath));
              [AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html) channel = resumeUploadSession.[open](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html#com_google_cloud_storage_BlobAppendableUpload_open__)()) {
            long bytesToAppend = fileChannel.size();
            System.out.printf(
                Locale.US,
                "Appending the entire file (%d bytes) after the initial string.\n",
                bytesToAppend);
    
            ByteStreams.copy(fileChannel, channel);
          }
    
          [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) result = storage.get(blobId);
          System.out.printf(
              Locale.US,
              "\nObject %s successfully resumed and finalized. Total size: %d bytes\n",
              [result](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.spi.v1.StorageRpc.RewriteResponse.html#com_google_cloud_storage_spi_v1_StorageRpc_RewriteResponse_result).[getBlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getBlobId__)().[toGsUtilUriWithGeneration](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html#com_google_cloud_storage_BlobId_toGsUtilUriWithGeneration__)(),
              [result](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.spi.v1.StorageRpc.RewriteResponse.html#com_google_cloud_storage_spi_v1_StorageRpc_RewriteResponse_result).[getSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getSize__)());
        }
      }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample pauses and resumes an appendable object:
    
    
    async def storage_pause_and_resume_appendable_upload(
        bucket_name, object_name, grpc_client=None
    ):
        """Demonstrates pausing and resuming an appendable object upload.
    
        grpc_client: an existing grpc_client to use, this is only for testing.
        """
        if grpc_client is None:
            grpc_client = AsyncGrpcClient()
    
        writer1 = AsyncAppendableObjectWriter(
            client=grpc_client,
            bucket_name=bucket_name,
            object_name=object_name,
        )
        await writer1.open()
        await writer1.append(b"First part of the data. ")
        print(f"Appended {writer1.persisted_size} bytes with the first writer.")
    
        # 2. After appending some data, close the writer to "pause" the upload.
        #  NOTE: you can pause indefinitely and still read the conetent uploaded so far using MRD.
        await writer1.close()
    
        print("First writer closed. Upload is 'paused'.")
    
        # 3. Create a new writer, passing the generation number from the previous
        #    writer. This is a precondition to ensure that the object hasn't been
        #    modified since we last accessed it.
        generation_to_resume = writer1.generation
        print(f"Generation to resume from is: {generation_to_resume}")
    
        writer2 = AsyncAppendableObjectWriter(
            client=grpc_client,
            bucket_name=bucket_name,
            object_name=object_name,
            generation=generation_to_resume,
        )
        # 4. Open the new writer.
        try:
            await writer2.open()
    
            # 5. Append some more data using the new writer.
            await writer2.append(b"Second part of the data.")
            print(f"Appended more data. Total size is now {writer2.persisted_size} bytes.")
        finally:
            # 6. Finally, close the new writer.
            if writer2._is_stream_open:
                await writer2.close()
        print("Second writer closed. Full object uploaded.")
    
    

## Finalize an object

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample finalizes an appendable object:
    
    
    namespace gcs = google::cloud::storage;
    auto coro = [](gcs::AsyncClient& client, std::string bucket_name,
                   std::string object_name)
        -> google::cloud::future<google::storage::v2::Object> {
      // Start an appendable upload.
      auto [writer, token] =
          (co_await client.StartAppendableObjectUpload(
               gcs::BucketName(std::move(bucket_name)), std::move(object_name)))
              .value();
      std::cout << "Appendable upload started. \n";
    
      // Write some data.
      token =
          (co_await writer.Write(std::move(token),
                                 gcs::WritePayload("some data to finalize\n")))
              .value();
    
      // Finalize the upload. This makes the object non-appendable.
      // No more data can be written to this writer.
      auto object = (co_await writer.Finalize(std::move(token))).value();
      std::cout << "Upload finalized.\n";
      co_return object;
    };

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample finalizes an appendable object:
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // finalizeAppendableObject creates, uploads and finalizes a new object in
    // a bucket with the Rapid storage class.
    func finalizeAppendableObject(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.[NewGRPCClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_NewGRPCClient)(ctx, storage.[WithAppendableUploads](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_WithAppendableUploads)())
    	if err != nil {
    		return fmt.Errorf("storage.NewGRPCClient: %w", err)
    	}
    	defer client.Close()
    
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    
    	// Create a Writer and set FinalizeOnClose so that the object will be
    	// finalized after the write is complete.
    	writer := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).[NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter)(ctx)
    	writer.FinalizeOnClose = true
    
    	if _, err := writer.[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)([]byte("some data to finalize\n")); err != nil {
    		return fmt.Errorf("Writer.Write: %w", err)
    	}
    
    	// Close the Writer to flush any remaining buffered data and finalize
    	// the upload. This makes the object non-appendable.
    	// No more data can be written to this object.
    	if err := writer.Close(); err != nil {
    		return fmt.Errorf("Writer.Close: %w", err)
    	}
    	fmt.Fprintf(w, "Uploaded and finalized object %v\n", object)
    
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample finalizes an appendable object:
    
    
    import com.google.cloud.storage.[Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html);
    import com.google.cloud.storage.[BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html);
    import com.google.cloud.storage.[BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class FinalizeAppendableObjectUpload {
      public static void finalizeAppendableObjectUpload(String bucketName, String objectName)
          throws Exception {
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS unfinalized appendable object
        // String objectName = "your-object-name";
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).[grpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html#com_google_cloud_storage_StorageOptions_grpc__)().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
          [Blob](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Blob.html) existingBlob = storage.get(blobId);
    
          if (existingBlob == null) {
            System.out.println("Object " + objectName + " not found in bucket " + bucketName);
            return;
          }
    
          [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfoForTakeover = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(existingBlob.[getBlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getBlobId__)()).build();
          [BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html) finalizingSession =
              storage.[blobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobAppendableUpload_com_google_cloud_storage_BlobInfo_com_google_cloud_storage_BlobAppendableUploadConfig_com_google_cloud_storage_Storage_BlobWriteOption____)(
                  blobInfoForTakeover,
                  [BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html).of()
                      .[withCloseAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html#com_google_cloud_storage_BlobAppendableUploadConfig_withCloseAction_com_google_cloud_storage_BlobAppendableUploadConfig_CloseAction_)([BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html).CloseAction.FINALIZE_WHEN_CLOSING));
    
          try ([BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html).[AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html) channel =
              finalizingSession.[open](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html#com_google_cloud_storage_BlobAppendableUpload_open__)()) {
            channel.[finalizeAndClose](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_finalizeAndClose__)();
          }
    
          System.out.println(
              "Successfully finalized object " + objectName + " in bucket " + bucketName);
        }
      }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample finalizes an appendable object:
    
    
    async def storage_finalize_appendable_object_upload(
        bucket_name, object_name, grpc_client=None
    ):
        """Creates, writes to, and finalizes an appendable object.
    
        grpc_client: an existing grpc_client to use, this is only for testing.
        """
    
        if grpc_client is None:
            grpc_client = AsyncGrpcClient()
        writer = AsyncAppendableObjectWriter(
            client=grpc_client,
            bucket_name=bucket_name,
            object_name=object_name,
            generation=0,  # throws `FailedPrecondition` if object already exists.
        )
        # This creates a new appendable object of size 0 and opens it for appending.
        await writer.open()
    
        # Appends data to the object.
        await writer.append(b"Some data")
    
        # finalize the appendable object,
        # NOTE:
        # 1. once finalized no more appends can be done to the object.
        # 2. If you don't want to finalize, you can simply call `writer.close`
        # 3. calling `.finalize()` also closes the grpc-bidi stream, calling
        #   `.close` after `.finalize` may lead to undefined behavior.
        object_resource = await writer.finalize()
    
        print(f"Appendable object {object_name} created and finalized.")
        print("Object Metadata:")
        print(object_resource)
    
    

## Read the tail of an object

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample reads the tail of an appendable object:
    
    
    namespace gcs = google::cloud::storage;
    auto coro = [](gcs::AsyncClient& client, std::string bucket_name,
                   std::string object_name) -> google::cloud::future<void> {
      // This coroutine simulates a "tail -f" command on a GCS object. It
      // repeatedly polls an appendable object for new content. In a real
      // application, the object would be written to by a separate process.
      std::cout << "Polling for content from " << object_name << "...\n\n";
    
      // Start an appendable upload. In a real application this would be done by
      // a separate process, and this application would only know the object name.
      auto [writer, token] = (co_await client.StartAppendableObjectUpload(
                                  gcs::BucketName(bucket_name), object_name))
                                 .value();
    
      std::int64_t bytes_read = 0;
      for (int i = 0; i != 2; ++i) {
        // In a real application, another process would append data here.
        // We simulate this by writing to the object.
        auto content =
            "More data for tail example, iteration " + std::to_string(i) + "\n";
        token =
            (co_await writer.Write(std::move(token), gcs::WritePayload(content)))
                .value();
        (void)co_await writer.Flush();
    
        // Poll for new content by reading from the last known offset.
        auto payload =
            (co_await client.ReadObjectRange(gcs::BucketName(bucket_name),
                                             object_name, bytes_read, -1))
                .value();
        for (auto const& buffer : payload.contents()) {
          std::cout << std::string(buffer.begin(), buffer.end());
          bytes_read += buffer.size();
        }
        // In a real application you would wait here, e.g. with a timer.
        std::this_thread::sleep_for(std::chrono::seconds(1));
      }
    };

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample reads the tail of an appendable object:
    
    
    import (
    	"bytes"
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // readAppendableObjectTail simulates a "tail -f" command on a GCS object. It
    // repeatedly polls an appendable object for new content. In a real
    // application, the object would be written to by a separate process.
    // Appendable objects require a bucket with the Rapid storage class.
    func readAppendableObjectTail(w io.Writer, bucket, object string) ([]byte, error) {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.NewGRPCClient(ctx, storage.WithGRPCBidiReads(), storage.WithAppendableUploads())
    	if err != nil {
    		return nil, fmt.Errorf("storage.NewGRPCClient: %w", err)
    	}
    	defer client.Close()
    
    	// Set a context timeout. When this timeout is reached, the read stream
    	// will be closed, so omit this to tail indefinitely.
    	ctx, cancel := context.WithTimeout(ctx, 5*time.Minute)
    	defer cancel()
    
    	// Create a new appendable object and write some data.
    	writer := client.Bucket(bucket).Object(object).If(storage.Conditions{DoesNotExist: true}).NewWriter(ctx)
    	if _, err := writer.Write([]byte("Some data\n")); err != nil {
    		return nil, fmt.Errorf("Writer.Write: %w", err)
    	}
    	if err := writer.Close(); err != nil {
    		return nil, fmt.Errorf("Writer.Close: %w", err)
    	}
    	gen := writer.Attrs().Generation
    
    	obj := client.Bucket(bucket).Object(object)
    
    	// Create the MultiRangeDownloader, which opens a read stream to the object.
    	mrd, err := obj.NewMultiRangeDownloader(ctx)
    	if err != nil {
    		return nil, fmt.Errorf("NewMultiRangeDownloader: %w", err)
    	}
    
    	// In a goroutine, poll the object. In this example we continue until all the
    	// bytes we expect to see were received, but in a real application this could
    	// continue to poll indefinitely until some signal is received.
    	var buf bytes.Buffer
    	var mrdErr error
    	done := make(chan bool)
    	go func() {
    		var currOff int64
    		// The channel is buffered so that the callback never blocks, even if
    		// we stopped waiting for the range below.
    		rangeDownloaded := make(chan error, 1)
    		for buf.Len() < 100 {
    			// Check how much data is available. The size of an unfinalized
    			// appendable object grows as more data is appended to it.
    			attrs, err := obj.Attrs(ctx)
    			if err != nil {
    				mrdErr = err
    				break
    			}
    			if attrs.Size <= currOff {
    				// Nothing new was appended yet; wait and check again.
    				time.Sleep(1 * time.Second)
    				continue
    			}
    
    			// Add the range of newly appended bytes and wait for it to be
    			// downloaded. The callback will give the actual number of bytes
    			// that were read in each iteration.
    			mrd.Add(&buf, currOff, attrs.Size-currOff, func(offset, length int64, err error) {
    				// After each range is received, update
    				// the starting offset based on how many bytes were received.
    				currOff += length
    				rangeDownloaded <- err
    			})
    			// Wait for the range download to complete with a timeout of 10s.
    			select {
    			case mrdErr = <-rangeDownloaded:
    			case <-time.After(10 * time.Second):
    				mrdErr = mrd.Error()
    				if mrdErr == nil {
    					mrdErr = errors.New("range request timed out after 10s")
    				}
    			}
    
    			if mrdErr != nil {
    				break
    			}
    			time.Sleep(1 * time.Second)
    		}
    		// After exiting the loop, close MultiRangeDownloader and signal that
    		// all ranges have been read.
    		if err := mrd.Close(); err != nil {
    			mrdErr = err
    		}
    		done <- true
    	}()
    
    	// Meanwhile, continue to write 10 bytes at a time to the object.
    	// This could be done by calling NewWriterFromAppendableObject repeatedly
    	// (as in the example) or calling Writer.Flush without closing the Writer.
    	for range 9 {
    		appendWriter, offset, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).[Generation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_Generation)(gen).[NewWriterFromAppendableObject](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriterFromAppendableObject)(ctx, nil)
    		if err != nil {
    			return nil, fmt.Errorf("NewWriterFromAppendableObject: %w", err)
    		}
    		if _, err := append[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)r.[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)([]byte("more data\n")); err != nil {
    			return nil, fmt.Errorf("appendWriter.Write: %w", err)
    		}
    		if err := appendWriter.Close(); err != nil {
    			return nil, fmt.Errorf("appendWriter.Close: %w", err)
    		}
    		fmt.Fprintf(w, "Wrote 10 bytes at offset %v\n", offset)
    	}
    
    	// Wait for tailing goroutine to exit.
    	<-done
    	if mrdErr != nil {
    		return nil, fmt.Errorf("MultiRangeDownloader: %w", mrdErr)
    	}
    	fmt.Fprintf(w, "Read %v bytes from object %v\n", buf.Len(), object)
    	return buf.[Bytes](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/transfermanager.html#cloud_google_com_go_storage_transfermanager_DownloadBuffer_Bytes)(), nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample reads the tail of an appendable object:
    
    
    import com.google.api.core.[ApiFuture](https://docs.cloud.google.com/java/docs/reference/api-common/latest/com.google.api.core.ApiFuture.html);
    import com.google.cloud.storage.[BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html);
    import com.google.cloud.storage.[BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html).[AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html);
    import com.google.cloud.storage.[BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[BlobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html);
    import com.google.cloud.storage.[FlushPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.html);
    import com.google.cloud.storage.[RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html);
    import com.google.cloud.storage.[ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageChannelUtils](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageChannelUtils.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.io.IOException;
    import java.nio.ByteBuffer;
    import java.util.concurrent.TimeUnit;
    
    public class ReadAppendableObjectTail {
      public static void readAppendableObjectTail(String bucketName, String objectName)
          throws Exception {
        // The ID of your GCS bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The ID of your GCS object
        // String objectName = "your-object-name";
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).[grpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html#com_google_cloud_storage_StorageOptions_grpc__)().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName);
          [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) info = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(blobId).build();
          int totalToWrite = 64 * 1000;
          // Define our flush policy to flush small increments
          // This is useful for demonstration purposes, but you should use more appropriate values for
          // your workload.
          int flushSize = totalToWrite / 8;
          [FlushPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.html).[MinFlushSizeFlushPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.MinFlushSizeFlushPolicy.html) flushPolicy =
              [FlushPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.html).[minFlushSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.html#com_google_cloud_storage_FlushPolicy_minFlushSize__)(flushSize).[withMaxPendingBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.MinFlushSizeFlushPolicy.html#com_google_cloud_storage_FlushPolicy_MinFlushSizeFlushPolicy_withMaxPendingBytes_long_)(flushSize);
          [BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html) appendableUploadConfig =
              [BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html).of().[withFlushPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html#com_google_cloud_storage_BlobAppendableUploadConfig_withFlushPolicy_com_google_cloud_storage_FlushPolicy_)(flushPolicy);
          [BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html) upload =
              storage.[blobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobAppendableUpload_com_google_cloud_storage_BlobInfo_com_google_cloud_storage_BlobAppendableUploadConfig_com_google_cloud_storage_Storage_BlobWriteOption____)(
                  info, appendableUploadConfig, [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobWriteOption.doesNotExist());
          // Create the object, we'll takeover to write for our example.
          upload.[open](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html#com_google_cloud_storage_BlobAppendableUpload_open__)().[closeWithoutFinalizing](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_closeWithoutFinalizing__)();
          [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) gen1 = upload.[getResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html#com_google_cloud_storage_BlobAppendableUpload_getResult__)().get();
          [BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html) takeover = storage.[blobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobAppendableUpload_com_google_cloud_storage_BlobInfo_com_google_cloud_storage_BlobAppendableUploadConfig_com_google_cloud_storage_Storage_BlobWriteOption____)(gen1, appendableUploadConfig);
    
          try ([AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html) channel = takeover.[open](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html#com_google_cloud_storage_BlobAppendableUpload_open__)()) {
            // Start a background thread to write some data on a periodic basis
            // In reality, you're application would probably be doing thing in another scope
            Thread writeThread = startWriteThread(totalToWrite, channel, flushPolicy);
            try ([BlobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html) readSession =
                storage.[blobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobReadSession_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____)(gen1.[getBlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html#com_google_cloud_storage_BlobInfo_getBlobId__)()).get(10, TimeUnit.SECONDS)) {
              int zeroCnt = 0;
              long read = 0;
              while (read < totalToWrite) {
                if (zeroCnt >= 30 && !channel.isOpen()) {
                  System.out.println("breaking");
                  break;
                }
                ApiFuture<byte[]> future =
                    readSession.[readAs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html#com_google_cloud_storage_BlobReadSession__Projection_readAs_com_google_cloud_storage_ReadProjectionConfig_Projection__)(
                        [ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html).[asFutureBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html#com_google_cloud_storage_ReadProjectionConfigs_asFutureBytes__)()
                            .withRangeSpec([RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html).of(read, flushPolicy.[getMinFlushSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.MinFlushSizeFlushPolicy.html#com_google_cloud_storage_FlushPolicy_MinFlushSizeFlushPolicy_getMinFlushSize__)())));
                byte[] bytes = future.get(20, TimeUnit.SECONDS);
    
                read += bytes.length;
                long defaultSleep = 1_500L;
                if (bytes.length == 0) {
                  zeroCnt++;
                  long millis = defaultSleep * zeroCnt;
                  System.out.println("millis = " + millis);
                  Thread.sleep(millis);
                } else {
                  zeroCnt = 0;
                  System.out.println("bytes.length = " + bytes.length + " read = " + read);
                  Thread.sleep(defaultSleep);
                }
              }
              assert read == totalToWrite : "not enough bytes";
            }
            writeThread.join();
          }
        }
      }
    
      private static Thread startWriteThread(
          int totalToWrite,
          [AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html) channel,
          [FlushPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.html).[MinFlushSizeFlushPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.MinFlushSizeFlushPolicy.html) flushPolicy) {
        Thread writeThread =
            new Thread(
                () -> {
                  try {
                    for (long written = 0; written < totalToWrite; ) {
                      byte alphaOffset = (byte) (written % 0x1a);
    
                      ByteBuffer buf = ByteBuffer.[wrap](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HttpStorageRpcHasherHelper.html#com_google_cloud_storage_HttpStorageRpcHasherHelper_wrap_java_io_OutputStream_boolean_)(new byte[] {(byte) (0x41 + alphaOffset)});
                      int w = [StorageChannelUtils](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageChannelUtils.html).[blockingEmptyTo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageChannelUtils.html#com_google_cloud_storage_StorageChannelUtils_blockingEmptyTo_java_nio_ByteBuffer_java_nio_channels_WritableByteChannel_)(buf, channel);
                      written += w;
                      if (written % flushPolicy.[getMinFlushSize](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.FlushPolicy.MinFlushSizeFlushPolicy.html#com_google_cloud_storage_FlushPolicy_MinFlushSizeFlushPolicy_getMinFlushSize__)() == 0) {
                        channel.[flush](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_flush__)();
                        Thread.sleep(40);
                      }
                    }
                    channel.[closeWithoutFinalizing](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_closeWithoutFinalizing__)();
    
                  } catch (IOException | InterruptedException e) {
                    throw new RuntimeException(e);
                  }
                });
        writeThread.start();
        return writeThread;
      }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample reads the tail of an appendable object:
    
    
    async def appender(writer: AsyncAppendableObjectWriter, duration: int):
        """Appends 10 bytes to the object every second for a given duration."""
        print("Appender started.")
        bytes_appended = 0
        start_time = time.monotonic()
        # Run the appender for the specified duration.
        while time.monotonic() - start_time < duration:
            await writer.append(BYTES_TO_APPEND)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
            bytes_appended += NUM_BYTES_TO_APPEND_EVERY_SECOND
            print(
                f"[{now}] Appended {NUM_BYTES_TO_APPEND_EVERY_SECOND} new bytes. Total appended: {bytes_appended} bytes."
            )
            await asyncio.sleep(0.1)
        print("Appender finished.")
    
    
    async def tailer(
        bucket_name: str, object_name: str, duration: int, client: AsyncGrpcClient
    ):
        """Tails the object by reading new data as it is appended."""
        print("Tailer started.")
        start_byte = 0
        start_time = time.monotonic()
        mrd = AsyncMultiRangeDownloader(client, bucket_name, object_name)
        try:
            await mrd.open()
            # Run the tailer for the specified duration.
            while time.monotonic() - start_time < duration:
                output_buffer = BytesIO()
                # A download range of (start, 0) means to read from 'start' to the end.
                await mrd.download_ranges([(start_byte, 0, output_buffer)])
    
                bytes_downloaded = output_buffer.getbuffer().nbytes
                if bytes_downloaded > 0:
                    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                    print(f"[{now}] Tailer read {bytes_downloaded} new bytes: ")
                    start_byte += bytes_downloaded
    
                await asyncio.sleep(0.1)  # Poll for new data every 0.1 seconds.
        finally:
            if mrd.is_stream_open:
                await mrd.close()
        print("Tailer finished.")
    
    
    # read_appendable_object_tail simulates a "tail -f" command on a GCS object. It
    # repeatedly polls an appendable object for new content. In a real
    # application, the object would be written to by a separate process.
    async def read_appendable_object_tail(
        bucket_name: str, object_name: str, duration: int, grpc_client=None
    ):
        """Main function to create an appendable object and run tasks.
    
        grpc_client: an existing grpc_client to use, this is only for testing.
        """
        if grpc_client is None:
            grpc_client = AsyncGrpcClient()
        writer = AsyncAppendableObjectWriter(
            client=grpc_client,
            bucket_name=bucket_name,
            object_name=object_name,
        )
        # 1. Create an empty appendable object.
        try:
            # 1. Create an empty appendable object.
            await writer.open()
            print(f"Created empty appendable object: {object_name}")
    
            # 2. Create the appender and tailer coroutines.
            appender_task = asyncio.create_task(appender(writer, duration))
            tailer_task = asyncio.create_task(
                tailer(bucket_name, object_name, duration, grpc_client)
            )
    
            # 3. Execute the coroutines concurrently.
            await asyncio.gather(appender_task, tailer_task)
        finally:
            if writer._is_stream_open:
                await writer.close()
                print("Writer closed.")
    
    

## Optimize write latency

If you maintain your own gRPC parallel write logic, consider using a pool of pre-opened writers on unfinalized appendable objects. Because each writer's object is already created and its stream is already open, your application can append data immediately instead of waiting for object creation and stream setup when it needs to write.

**Note:** In workloads with long idle periods (>60 seconds), writers in the pool might be disconnected by the server due to stream idle timeouts. Production pools should record writer creation timestamps and replace any writer that's idle for more than 60 seconds.

### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample uses a pool of pre-opened writers for a zonal bucket:
    
    
    namespace gcs = google::cloud::storage;
    auto coro = [](gcs::AsyncClient& client, std::string bucket_name,
                   std::string key_prefix,
                   int pool_size) -> google::cloud::future<void> {
      std::string const next_object_name =
          key_prefix + "_" + std::to_string(pool_size);
    
      // 1. Init pool: Sized to ensure pre-warmed writers are always available.
      std::deque<std::pair<gcs::AsyncWriter, gcs::AsyncToken>> pool;
      for (int i = 0; i < pool_size; ++i) {
        auto [writer, token] = (co_await client.StartAppendableObjectUpload(
                                    gcs::BucketName(bucket_name),
                                    key_prefix + "_" + std::to_string(i)))
                                   .value();
        pool.emplace_back(std::move(writer), std::move(token));
      }
    
      // 2. Write: Pop a pre-warmed writer and commit with the faster Flush()
      // instead of Finalize().
      auto [writer, token] = std::move(pool.front());
      pool.pop_front();
      token = (co_await writer.Write(std::move(token),
                                     gcs::WritePayload("0123456789")))
                  .value();
      auto flush_status = co_await writer.Flush();
      if (!flush_status.ok()) throw std::runtime_error(flush_status.message());
    
      // 3. Pool maintenance (run asynchronously off the critical write path):
      // Close the used writer without finalizing and refill the pool.
      auto maintain_pool = [](gcs::AsyncClient client, std::string bucket_name,
                              std::string next_object_name,
                              gcs::AsyncWriter writer)
          -> google::cloud::future<std::pair<gcs::AsyncWriter, gcs::AsyncToken>> {
        auto close_status = co_await writer.Close();
        if (!close_status.ok()) throw std::runtime_error(close_status.message());
        auto [new_writer, new_token] =
            (co_await client.StartAppendableObjectUpload(
                 gcs::BucketName(std::move(bucket_name)),
                 std::move(next_object_name)))
                .value();
        co_return {std::move(new_writer), std::move(new_token)};
      };
      auto maintenance_future =
          maintain_pool(client, bucket_name, next_object_name, std::move(writer));
    
      // 4. Read: Unfinalized objects are readable after Flush().
      gcs::ObjectDescriptor descriptor =
          (co_await client.Open(gcs::BucketName(bucket_name), key_prefix + "_0"))
              .value();
      auto [reader, read_token] = descriptor.Read(0, 10);
      std::string contents;
      while (read_token.valid()) {
        auto [payload, t] = (co_await reader.Read(std::move(read_token))).value();
        read_token = std::move(t);
        for (auto const& buffer : payload.contents()) {
          contents.append(buffer.begin(), buffer.end());
        }
      }
      std::cout << "Read unfinalized object " << key_prefix << "_0: " << contents
                << "\n";
    
      auto [new_writer, new_token] = co_await std::move(maintenance_future);
      pool.emplace_back(std::move(new_writer), std::move(new_token));
      for (auto& [rem_writer, rem_token] : pool) {
        auto close_status = co_await rem_writer.Close();
        if (!close_status.ok()) throw std::runtime_error(close_status.message());
      }
    };

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample uses a pool of pre-opened writers for a zonal bucket:
    
    
    import (
    	"context"
    	"errors"
    	"fmt"
    	"io"
    	"sync/atomic"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    // optimizeWriteLatencyPool uses a pre-warmed pool of writers for appendable
    // objects in a bucket with the Rapid storage class.
    func optimizeWriteLatencyPool(out io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucketName, keyPrefix string) error {
    	// bucketName := "bucket-name"
    	// keyPrefix := "pooled-object"
    	const poolSize = 3
    	// Pool writers live until ctx is canceled (here, on return).
    	ctx, cancel := context.WithCancel(context.Background())
    	defer cancel()
    
    	client, err := storage.[NewGRPCClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_NewGRPCClient)(ctx, storage.[WithAppendableUploads](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_WithAppendableUploads)())
    	if err != nil {
    		return fmt.Errorf("storage.NewGRPCClient: %w", err)
    	}
    	defer client.Close()
    
    	bucket := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName)
    	// Each pre-warmed writer gets the next unique object number.
    	var nextID atomic.Int64
    	newPrewarmedWriter := func() (*storage.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), error) {
    		name := fmt.Sprintf("%s_%d", keyPrefix, nextID.[Add](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_MultiRangeDownloader_Add)(1)-1)
    		w := bucket.[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(name).If(storage.[Conditions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Conditions){DoesNotExist: true}).[NewWriter](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewWriter)(ctx)
    		if _, err := w.[Flush](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Flush)(); err != nil {
    			return nil, errors.Join(fmt.Errorf("Writer.Flush(%q): %w", name, err), w.Close())
    		}
    		return w, nil
    	}
    
    	// Init pool: A buffered channel is a thread-safe FIFO queue of pre-warmed
    	// writers. Flushing incurs operation charges, so size the pool carefully.
    	pool := make(chan *storage.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), poolSize)
    	// On return, close pooled writers; unused objects remain unfinalized.
    	defer func() {
    		close(pool)
    		for w := range pool {
    			if err := w.Close(); err != nil {
    				fmt.Fprintf(out, "Writer.Close: %v\n", err)
    			}
    		}
    	}()
    
    	for range poolSize {
    		w, err := newPrewarmedWriter()
    		if err != nil {
    			return err
    		}
    		pool <- w
    	}
    
    	// Write: Take a pre-warmed writer (waiting for a refill if the pool is
    	// empty) and commit with the faster Flush() instead of blocking on Close().
    	var w *storage.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer)
    	select {
    	case w = <-pool:
    	case <-time.After(10 * time.Second):
    		return errors.New("timed out waiting for a pre-warmed writer")
    	}
    	if _, err := w.[Write](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Write)([]byte("0123456789")); err != nil {
    		return errors.Join(fmt.Errorf("Writer.Write: %w", err), w.Close())
    	}
    	if _, err := w.[Flush](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer_Flush)(); err != nil {
    		return errors.Join(fmt.Errorf("Writer.Flush: %w", err), w.Close())
    	}
    	fmt.Fprintf(out, "Wrote and flushed %q without finalizing\n", w.Name)
    
    	// Pool maintenance (run asynchronously off the critical write path):
    	// Close the used writer without finalizing and refill the pool.
    	maintenance := make(chan struct{})
    	go func(used *storage.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer)) {
    		defer close(maintenance)
    		if err := used.Close(); err != nil {
    			fmt.Fprintf(out, "Writer.Close: %v\n", err)
    		}
    		next, err := newPrewarmedWriter()
    		if err != nil {
    			fmt.Fprintf(out, "failed to pre-warm replacement writer: %v\n", err)
    			return
    		}
    		pool <- next
    	}(w)
    	// Wait for maintenance on return; runs before the pool cleanup above.
    	defer func() { <-maintenance }()
    
    	// Read: Unfinalized objects are readable after Flush().
    	r, err := bucket.[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(fmt.Sprintf("%s_0", keyPrefix)).[NewReader](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_ObjectHandle_NewReader)(ctx)
    	if err != nil {
    		return fmt.Errorf("Object.NewReader: %w", err)
    	}
    	contents, err := io.ReadAll(r)
    	if err := errors.Join(err, r.Close()); err != nil {
    		return fmt.Errorf("reading %s_0: %w", keyPrefix, err)
    	}
    
    	fmt.Fprintf(out, "Read unfinalized object %s_0: %s\n", keyPrefix, contents)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample uses a pool of pre-opened writers for a zonal bucket:
    
    
    import com.google.cloud.storage.[BlobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.html).[AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html);
    import com.google.cloud.storage.[BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html);
    import com.google.cloud.storage.[BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html).[CloseAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.CloseAction.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[BlobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html);
    import com.google.cloud.storage.[RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html);
    import com.google.cloud.storage.[ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.io.IOException;
    import java.nio.ByteBuffer;
    import java.nio.charset.StandardCharsets;
    import java.util.Queue;
    import java.util.concurrent.ConcurrentLinkedQueue;
    import java.util.concurrent.ExecutorService;
    import java.util.concurrent.Executors;
    import java.util.concurrent.Future;
    import java.util.concurrent.TimeUnit;
    
    public class OptimizeWriteLatencyPool {
      private static [AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html) newPrewarmedChannel(
          [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage, [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) info, [BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html) config) throws IOException {
        [AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html) channel =
            storage.[blobAppendableUpload](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobAppendableUpload_com_google_cloud_storage_BlobInfo_com_google_cloud_storage_BlobAppendableUploadConfig_com_google_cloud_storage_Storage_BlobWriteOption____)(info, config, [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html).BlobWriteOption.doesNotExist()).open();
        // open() is lazy. flush() creates the 0-byte object.
        try {
          channel.[flush](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_flush__)();
        } catch (IOException e) {
          // Close the channel; attach any close error to the flush error.
          try {
            channel.[closeWithoutFinalizing](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_closeWithoutFinalizing__)();
          } catch (IOException closeException) {
            e.addSuppressed(closeException);
          }
          throw e;
        }
        return channel;
      }
    
      public static void optimizeWriteLatencyPool(String bucketName, String keyPrefix)
          throws Exception {
        // The ID of your GCS zonal bucket
        // String bucketName = "your-unique-bucket-name";
    
        // The prefix for your pooled GCS objects
        // String keyPrefix = "pooled-object";
    
        int poolSize = 3;
        String nextObjectName = keyPrefix + "_" + poolSize;
        byte[] payload = "0123456789".getBytes(StandardCharsets.UTF_8);
    
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).[grpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html#com_google_cloud_storage_StorageOptions_grpc__)().build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          [BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html) config =
              [BlobAppendableUploadConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html).of().[withCloseAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.html#com_google_cloud_storage_BlobAppendableUploadConfig_withCloseAction_com_google_cloud_storage_BlobAppendableUploadConfig_CloseAction_)([CloseAction](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUploadConfig.CloseAction.html).CLOSE_WITHOUT_FINALIZING);
          Queue<AppendableUploadWriteableByteChannel> pool = new ConcurrentLinkedQueue<>();
          ExecutorService executor = Executors.newSingleThreadExecutor();
          try {
            // 1. Init pool: Flushing incurs operation charges, so size the pool carefully.
            for (int i = 0; i < poolSize; i++) {
              BlobInfo info = BlobInfo.newBuilder(bucketName, keyPrefix + "_" + i).build();
              pool.add(newPrewarmedChannel(storage, info, config));
            }
    
            // 2. Write: Pop a pre-warmed writer and commit with flush() (~1-2 ms)
            // instead of blocking on close().
            AppendableUploadWriteableByteChannel channel = pool.poll();
            if (channel == null) {
              throw new IllegalStateException("Writer pool is empty");
            }
            try {
              channel.write(ByteBuffer.wrap(payload));
              channel.flush();
            } catch (Exception e) {
              try {
                channel.closeWithoutFinalizing();
              } catch (Exception closeException) {
                e.addSuppressed(closeException);
              }
              throw e;
            }
    
            // 3. Pool maintenance (run asynchronously off the critical write path):
            // Close the used channel without finalizing and refill the pool.
            Future<Void> maintenanceFuture =
                executor.submit(
                    () -> {
                      channel.closeWithoutFinalizing();
                      BlobInfo nextInfo = BlobInfo.newBuilder(bucketName, nextObjectName).build();
                      pool.add(newPrewarmedChannel(storage, nextInfo, config));
                      return null;
                    });
    
            // 4. Read: Unfinalized objects are readable after flush().
            try ([BlobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html) readSession =
                storage
                    .[blobReadSession](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_blobReadSession_com_google_cloud_storage_BlobId_com_google_cloud_storage_Storage_BlobSourceOption____)([BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, keyPrefix + "_0"))
                    .get(10, TimeUnit.SECONDS)) {
              byte[] bytes =
                  readSession
                      .[readAs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobReadSession.html#com_google_cloud_storage_BlobReadSession__Projection_readAs_com_google_cloud_storage_ReadProjectionConfig_Projection__)(
                          [ReadProjectionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html).[asFutureBytes](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.ReadProjectionConfigs.html#com_google_cloud_storage_ReadProjectionConfigs_asFutureBytes__)()
                              .withRangeSpec([RangeSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.RangeSpec.html).of(0, payload.length)))
                      .get();
              System.out.printf(
                  "Read unfinalized object %s_0: %s%n",
                  keyPrefix, new String(bytes, StandardCharsets.UTF_8));
            }
    
            maintenanceFuture.get(10, TimeUnit.SECONDS);
          } finally {
            // Wait for in-flight maintenance so it can't add a channel after the pool is drained.
            executor.shutdown();
            executor.awaitTermination(10, TimeUnit.SECONDS);
            // Runs before the Storage client is closed by the outer try-with-resources.
            [AppendableUploadWriteableByteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html) remaining;
            while ((remaining = pool.poll()) != null) {
              try {
                remaining.[closeWithoutFinalizing](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobAppendableUpload.AppendableUploadWriteableByteChannel.html#com_google_cloud_storage_BlobAppendableUpload_AppendableUploadWriteableByteChannel_closeWithoutFinalizing__)();
              } catch (Exception e) {
                // Ignore so the remaining channels are still closed.
              }
            }
          }
        }
      }
    }
    

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 

The following sample uses a pool of pre-opened writers for a zonal bucket:
    
    
    async def storage_optimize_write_latency_pool(
        bucket_name: str, key_prefix: str, pool_size: int = 3, grpc_client=None
    ):
        """Uses a pre-warmed pool of writers for a zonal bucket.
    
        grpc_client: an existing grpc_client to use, this is only for testing.
        """
        # The ID of your GCS zonal bucket
        # bucket_name = "your-unique-bucket-name"
    
        # The prefix for your pooled GCS objects
        # key_prefix = "pooled-object"
    
        grpc_client_created = False
        if grpc_client is None:
            grpc_client = AsyncGrpcClient()
            grpc_client_created = True
    
        next_object_name = f"{key_prefix}_{pool_size}"
    
        async def new_prewarmed_writer(name: str) -> AsyncAppendableObjectWriter:
            w = AsyncAppendableObjectWriter(
                client=grpc_client,
                bucket_name=bucket_name,
                object_name=name,
                generation=0,
            )
            await w.open()  # Establishes stream and creates 0-byte object in background.
            return w
    
        # 1. Init pool: Sized to ensure pre-warmed writers are always available.
        pool = deque(
            await asyncio.gather(
                *(
                    new_prewarmed_writer(f"{key_prefix}_{i}")
                    for i in range(pool_size)
                )
            )
        )
    
        try:
            # 2. Write: Pop a pre-warmed writer; append() writes and flushes data
            # (~1-2 ms).
            writer = pool.popleft()
            await writer.append(b"0123456789")
    
            # 3. Pool maintenance (run asynchronously off the critical write path):
            # Close the used writer without finalizing and refill the pool.
            async def maintain_pool(
                used: AsyncAppendableObjectWriter, next_name: str
            ):
                await used.close(finalize_on_close=False)
                pool.append(await new_prewarmed_writer(next_name))
    
            maintenance_task = asyncio.create_task(
                maintain_pool(writer, next_object_name)
            )
    
            # 4. Read: Unfinalized objects are readable after flush().
            mrd = AsyncMultiRangeDownloader(
                grpc_client, bucket_name, f"{key_prefix}_0"
            )
            await mrd.open()
            buf = BytesIO()
            await mrd.download_ranges([(0, 0, buf)])
            await mrd.close()
    
            await maintenance_task
            print(
                f"Read unfinalized object {key_prefix}_0: "
                f"{buf.getvalue().decode('utf-8')}"
            )
        finally:
            for rem in pool:
                await rem.close(finalize_on_close=False)
            if grpc_client_created:
                await grpc_client.close()
    
    

## What's next

  * [Download objects from a bucket](https://docs.cloud.google.com/storage/docs/downloading-objects).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
