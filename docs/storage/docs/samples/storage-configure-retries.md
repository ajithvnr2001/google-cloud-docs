---
url: https://docs.cloud.google.com/storage/docs/samples/storage-configure-retries/
title: Demonstrate retry configuration \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:54.703373+00:00
---

# Demonstrate retry configuration  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/samples/storage-configure-retries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Samples ](https://docs.cloud.google.com/storage/docs/samples)



#  Demonstrate retry configuration Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrate retry configuration

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Retry strategy](https://docs.cloud.google.com/storage/docs/retry-strategy)



## Code sample

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    // Create the client configuration:
    auto options = google::cloud::Options{};
    // Retries only idempotent operations.
    options.set<gcs::IdempotencyPolicyOption>(
        gcs::StrictIdempotencyPolicy().clone());
    // On error, it backs off for a random delay between [1, 3] seconds, then [3,
    // 9] seconds, then [9, 27] seconds, etc. The backoff time never grows larger
    // than 1 minute.
    options.set<gcs::BackoffPolicyOption>(
        gcs::ExponentialBackoffPolicy(
            /*initial_delay=*/std::chrono::seconds(1),
            /*maximum_delay=*/std::chrono::minutes(1),
            /*scaling=*/3.0)
            .clone());
    // Retries all operations for up to 5 minutes, including any backoff time.
    options.set<gcs::RetryPolicyOption>(
        gcs::LimitedTimeRetryPolicy(std::chrono::minutes(5)).clone());
    return gcs::Client(std::move(options));

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"time"
    
    	"cloud.google.com/go/storage"
    	"github.com/googleapis/gax-go/v2"
    )
    
    // configureRetries configures a custom retry strategy for a single API call.
    func configureRetries(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) error {
    	// bucket := "bucket-name"
    	// object := "object-name"
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// Configure retries for all operations using this ObjectHandle. Retries may
    	// also be configured on the BucketHandle or Client types.
    	o := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).[Object](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Object)(object).Retryer(
    		// Use WithBackoff to control the timing of the exponential backoff.
    		storage.[WithBackoff](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetryOption_WithBackoff)(gax.Backoff{
    			// Set the initial retry delay to a maximum of 2 seconds. The length of
    			// pauses between retries is subject to random jitter.
    			Initial: 2 * time.Second,
    			// Set the maximum retry delay to 60 seconds.
    			Max: 60 * time.Second,
    			// Set the backoff multiplier to 3.0.
    			Multiplier: 3,
    		}),
    		// Use WithPolicy to customize retry so that all requests are retried even
    		// if they are non-idempotent.
    		storage.[WithPolicy](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetryOption_WithPolicy)(storage.[RetryAlways](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_RetryIdempotent_RetryAlways_RetryNever)),
    	)
    
    	// Use context timeouts to set an overall deadline on the call, including all
    	// potential retries.
    	ctx, cancel := context.WithTimeout(ctx, 500*time.Second)
    	defer cancel()
    
    	// Delete an object using the specified retry policy.
    	if err := o.Delete(ctx); err != nil {
    		return fmt.Errorf("Object(%q).Delete: %w", object, err)
    	}
    	fmt.Fprintf(w, "Blob %v deleted with a customized retry strategy.\n", object)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.api.gax.retrying.[RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html);
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import com.google.cloud.storage.[StorageRetryStrategy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRetryStrategy.html);
    import org.threeten.bp.Duration;
    
    public final class ConfigureRetries {
      public static void main(String[] args) {
        String bucketName = "my-bucket";
        String blobName = "blob/to/delete";
        deleteBlob(bucketName, blobName);
      }
    
      static void deleteBlob(String bucketName, String blobName) {
        // Customize retry behavior
        [RetrySettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.html) retrySettings =
            [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).getDefaultRetrySettings().toBuilder()
                // Set the max number of attempts to 10 (initial attempt plus 9 retries)
                .[setMaxAttempts](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setMaxAttempts_int_)(10)
                // Set the backoff multiplier to 3.0
                .[setRetryDelayMultiplier](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setRetryDelayMultiplier_double_)(3.0)
                // Set the max duration of all attempts to 5 minutes
                .[setTotalTimeout](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder.html#com_google_api_gax_retrying_RetrySettings_Builder_setTotalTimeout_org_threeten_bp_Duration_)(Duration.ofMinutes(5))
                .build();
    
        [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) alwaysRetryStorageOptions =
            [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder()
                // Customize retry so all requests are retried even if they are non-idempotent.
                .setStorageRetryStrategy([StorageRetryStrategy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRetryStrategy.html).[getUniformStorageRetryStrategy](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageRetryStrategy.html#com_google_cloud_storage_StorageRetryStrategy_getUniformStorageRetryStrategy__)())
                // provide the previously configured retrySettings
                .setRetrySettings(retrySettings)
                .build();
    
        // Instantiate a client
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = alwaysRetryStorageOptions.[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // Delete the blob
        [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html) blobId = [BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, blobName);
        boolean success = storage.[delete](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_delete_com_google_cloud_storage_BlobId_)(blobId);
    
        System.out.printf(
            "Deletion of Blob %s completed %s.%n", blobId, success ? "successfully" : "unsuccessfully");
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
    
    // The ID of your GCS file
    // const fileName = 'your-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)({
      retryOptions: {
        // If this is false, requests will not retry and the parameters
        // below will not affect retry behavior.
        autoRetry: true,
        // The multiplier by which to increase the delay time between the
        // completion of failed requests, and the initiation of the subsequent
        // retrying request.
        retryDelayMultiplier: 3,
        // The total time between an initial request getting sent and its timeout.
        // After timeout, an error will be returned regardless of any retry attempts
        // made during this time period.
        totalTimeout: 500,
        // The maximum delay time between requests. When this value is reached,
        // retryDelayMultiplier will no longer be used to increase delay time.
        maxRetryDelay: 60,
        // The maximum number of automatic retries attempted before returning
        // the error.
        maxRetries: 5,
        // Will respect other retry settings and attempt to always retry
        // conditionally idempotent operations, regardless of precondition
        idempotencyStrategy: IdempotencyStrategy.RetryAlways,
      },
    });
    console.log(
      'Functions are customized to be retried according to the following parameters:'
    );
    console.log(`Auto Retry: ${storage.retryOptions.autoRetry}`);
    console.log(
      `Retry delay multiplier: ${storage.retryOptions.retryDelayMultiplier}`
    );
    console.log(`Total timeout: ${storage.retryOptions.totalTimeout}`);
    console.log(`Maximum retry delay: ${storage.retryOptions.maxRetryDelay}`);
    console.log(`Maximum retries: ${storage.retryOptions.maxRetries}`);
    console.log(
      `Idempotency strategy: ${storage.retryOptions.idempotencyStrategy}`
    );
    
    async function deleteFileWithCustomizedRetrySetting() {
      await storage.bucket(bucketName).file(fileName).delete();
      console.log(`File ${fileName} deleted with a customized retry strategy.`);
    }
    
    deleteFileWithCustomizedRetrySetting();

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Configures retries with customizations.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     */
    function configure_retries(string $bucketName): void
    {
        $storage = new StorageClient([
            // The maximum number of automatic retries attempted before returning
            // the error.
            // Default: 3
            'retries' => 10,
    
            // Exponential backoff settings
            // Retry strategy to signify that we never want to retry an operation
            // even if the error is retryable.
            // Default: StorageClient::RETRY_IDEMPOTENT
            'retryStrategy' => StorageClient::RETRY_ALWAYS,
    
            // Executes a delay
            // Defaults to utilizing `usleep`.
            // Function signature should match: `function (int $delay) : void`.
            // This function is mostly used internally, so the tests don't wait
            // the time of the delay to run.
            'restDelayFunction' => function ($delay) {
                usleep($delay);
            },
    
            // Sets the conditions for determining how long to wait between attempts to retry.
            // Function signature should match: `function (int $attempt) : int`.
            // Allows to change the initial retry delay, retry delay multiplier and maximum retry delay.
            'restCalcDelayFunction' => fn ($attempt) => ($attempt + 1) * 100,
    
            // Sets the conditions for whether or not a request should attempt to retry.
            // Function signature should match: `function (\Exception $ex) : bool`.
            'restRetryFunction' => function (\Exception $e) {
                // Custom logic: ex. only retry if the error code is 404.
                return $e->getCode() === 404;
            },
    
            // Runs after the restRetryFunction. This might be used to simply consume the
            // exception and $arguments b/w retries. This returns the new $arguments thus allowing
            // modification on demand for $arguments. For ex: changing the headers in b/w retries.
            'restRetryListener' => function (\Exception $e, $retryAttempt, &$arguments) {
                // logic
            },
        ]);
        $bucket = $storage->bucket($bucketName);
        $operationRetriesOverrides = [
            // The maximum number of automatic retries attempted before returning
            // the error.
            // Default: 3
            'retries' => 10,
    
            // Exponential backoff settings
            // Retry strategy to signify that we never want to retry an operation
            // even if the error is retryable.
            // Default: StorageClient::RETRY_IDEMPOTENT
            'retryStrategy' => StorageClient::RETRY_ALWAYS,
    
            // Executes a delay
            // Defaults to utilizing `usleep`.
            // Function signature should match: `function (int $delay) : void`.
            // This function is mostly used internally, so the tests don't wait
            // the time of the delay to run.
            'restDelayFunction' => function ($delay) {
                usleep($delay);
            },
    
            // Sets the conditions for determining how long to wait between attempts to retry.
            // Function signature should match: `function (int $attempt) : int`.
            // Allows to change the initial retry delay, retry delay multiplier and maximum retry delay.
            'restCalcDelayFunction' => fn ($attempt) => ($attempt + 1) * 100,
    
            // Sets the conditions for whether or not a request should attempt to retry.
            // Function signature should match: `function (\Exception $ex) : bool`.
            'restRetryFunction' => function (\Exception $e) {
                // Custom logic: ex. only retry if the error code is 404.
                return $e->getCode() === 404;
            },
    
            // Runs after the restRetryFunction. This might be used to simply consume the
            // exception and $arguments b/w retries. This returns the new $arguments thus allowing
            // modification on demand for $arguments. For ex: changing the headers in b/w retries.
            'restRetryListener' => function (\Exception $e, $retryAttempt, &$arguments) {
                // logic
            },
        ];
        foreach ($bucket->objects($operationRetriesOverrides) as $object) {
            printf('Object: %s' . PHP_EOL, $object->name());
        }
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    from google.cloud.storage.retry import DEFAULT_RETRY
    
    
    def configure_retries(bucket_name, blob_name):
        """Configures retries with customizations."""
        # The ID of your GCS bucket
        # bucket_name = "your-bucket-name"
        # The ID of your GCS object
        # blob_name = "your-object-name"
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(blob_name)
    
        # Customize retry with a timeout of 500 seconds (default=120 seconds).
        modified_retry = DEFAULT_RETRY.with_timeout(500.0)
        # Customize retry with an initial wait time of 1.5 (default=1.0).
        # Customize retry with a wait time multiplier per iteration of 1.2 (default=2.0).
        # Customize retry with a maximum wait time of 45.0 (default=60.0).
        modified_retry = modified_retry.with_delay(initial=1.5, multiplier=1.2, maximum=45.0)
    
        # blob.delete() uses DEFAULT_RETRY by default.
        # Pass in modified_retry to override the default retry behavior.
        print(
            f"The following library method is customized to be retried according to the following configurations: {modified_retry}"
        )
    
        blob.delete(retry=modified_retry)
        print(f"Blob {blob_name} deleted with a customized retry strategy.")
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def configure_retries bucket_name: nil, file_name: nil
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      require "google/cloud/storage"
    
      # Creates a client
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)(
    
        # The maximum number of automatic retries attempted before returning
        # the error.
        #
        # Customize retry configuration with the maximum retry attempt of 5.
        retries: 5,
    
        # The total time in seconds that requests are allowed to keep being retried.
        # After max_elapsed_time, an error will be returned regardless of any
        # retry attempts made during this time period.
        #
        # Customize retry configuration with maximum elapsed time of 500 seconds.
        max_elapsed_time: 500,
    
        # The initial interval between the completion of failed requests, and the
        # initiation of the subsequent retrying request.
        #
        # Customize retry configuration with an initial interval of 1.5 seconds.
        base_interval: 1.5,
    
        # The maximum interval between requests. When this value is reached,
        # multiplier will no longer be used to increase the interval.
        #
        # Customize retry configuration with maximum interval of 45.0 seconds.
        max_interval: 45,
    
        # The multiplier by which to increase the interval between the completion
        # of failed requests, and the initiation of the subsequent retrying request.
        #
        # Customize retry configuration with an interval multiplier per iteration of 1.2.
        multiplier: 1.2
      )
    
      # Uses the retry configuration set during the client initialization above with 5 retries
      file = storage.service.get_file bucket_name, file_name
    
      # Maximum retry attempt can be overridden for each operation using options parameter.
      storage.service.delete_file bucket_name, file_name, options: { retries: 4 }
      puts "File #{file.name} deleted with a customized retry strategy."
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=storage). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
