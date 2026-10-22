---
url: https://docs.cloud.google.com/storage/docs/retry-strategy/
title: Retry strategy \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:36.074645+00:00
---

# Retry strategy  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/retry-strategy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Retry strategy Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how Cloud Storage tools retry failed requests and how to customize the behavior of retries. It also describes considerations for retrying requests.

## Overview

There are two factors that determine whether or not a request is safe to retry:

  * The _response_ that you receive from the request.

  * The _idempotency_ of the request.




### Response

The response that you receive from your request indicates whether or not it's useful to retry the request. Responses related to transient problems are generally retryable. On the other hand, response related to permanent errors indicate you need to make changes, such as authorization or configuration changes, before it's useful to try the request again. The following responses indicate transient problems that are useful to retry:

  * HTTP `408`, `429`, and `5xx` response codes.
  * Socket timeouts and TCP disconnects.



For more information, see the status and error codes for [JSON](https://docs.cloud.google.com/storage/docs/json_api/v1/status-codes) and [XML](https://docs.cloud.google.com/storage/docs/xml-api/reference-status).

### Idempotency

Requests that are _idempotent_ can be executed repeatedly without changing the final state of the targeted resource, resulting in the same end state each time. For example, list operations are always idempotent, because such requests don't modify resources. On the other hand, creating a new Pub/Sub notification is never idempotent, because it creates a new notification ID each time the request succeeds.

The following are examples of conditions that make an operation idempotent:

  * The operation has the same observable effect on the targeted resource even when continually requested.

  * The operation only succeeds once.

  * The operation has no observable effect on the state of the targeted resource.




When you receive a retryable response, you should consider the idempotency of the request, because retrying requests that are not idempotent can lead to race conditions and other conflicts.

#### Conditional idempotency

A subset of requests are _conditionally idempotent_ , which means they are only idempotent if they include specific optional arguments. Operations that are conditionally safe to retry should only be retried by default if the condition case passes. Cloud Storage accepts [preconditions and ETags](https://docs.cloud.google.com/storage/docs/request-preconditions) as condition cases for requests.

## Idempotency of operations

The following table lists the Cloud Storage operations that fall into each category of idempotency.

Idempotency | Operations  
---|---  
Always idempotent | 

  * All get and list requests
  * Insert or delete buckets
  * Test bucket IAM policies and permissions
  * Lock retention policies
  * Delete an HMAC key or Pub/Sub notification

  
Conditionally idempotent | 

  * Update/patch requests for buckets with `IfMetagenerationMatch`1 or `etag`1 as HTTP precondition
  * Update/patch requests for objects with `IfMetagenerationMatch`1 or `etag`1 as HTTP precondition
  * Set a bucket IAM policy with `etag`1 as HTTP precondition or in resource body
  * Update an HMAC key with `etag`1 as HTTP precondition or in resource body
  * Insert, copy, compose, or rewrite objects with `ifGenerationMatch`1
  * Delete an object with `ifGenerationMatch`1 (or with a generation number for object versions)

  
Never idempotent | 

  * Create an HMAC key
  * Create a Pub/Sub notification
  * Create, delete, or send patch/update requests for bucket and object ACLs or default object ACLs

  
  
1This field is available for use in the JSON API. For fields available for use in the client libraries, see the relevant [client library documentation](https://docs.cloud.google.com/storage/docs/retry-strategy#tools).

## How Cloud Storage tools implement retry strategies

### Console

The Google Cloud console sends requests to Cloud Storage on your behalf and handles any necessary backoff.

### Command line

[`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage) retry the errors listed in the Response section without requiring you to take additional action. You might have to take action for other errors, such as the following:

  * Invalid credentials or insufficient permissions.

  * Network unreachable because of a proxy configuration problem.




For retryable errors, the gcloud CLI retries requests using a [truncated binary exponential backoff strategy](https://en.wikipedia.org/wiki/Exponential_backoff). The default number of maximum retries is 32 for the gcloud CLI.

### Client libraries

### C++

By default, operations support retries for the following HTTP error codes, as well as any socket errors that indicate the connection was lost or never successfully established.

  * `408 Request Timeout`
  * `429 Too Many Requests`
  * `500 Internal Server Error`
  * `502 Bad Gateway`
  * `503 Service Unavailable`
  * `504 Gateway Timeout`



All exponential backoff and retry settings in the C++ library are configurable. If the algorithms implemented in the library don't support your needs, you can provide custom code to implement your own strategies.

Setting | Default value  
---|---  
Auto retry | True  
Maximum time retrying a request | 15 minutes  
Initial wait (backoff) time | 1 second  
Wait time multiplier per iteration | 2  
Maximum amount of wait time | 5 minutes  
  
By default, the C++ library retries all operations with retryable errors, even those that are never idempotent and can delete or create multiple resources when repeatedly successful. To only retry idempotent operations, use the `google::cloud::storage::StrictIdempotencyPolicy` class.

### C#

The C# client library uses [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) by default.

### Go

By default, operations support retries for the following errors:

  * Connection errors: 
    * [`io.ErrUnexpectedEOF`](https://pkg.go.dev/io#ErrUnexpectedEOF): This may occur due to transient network issues.
    * [`url.Error`](https://pkg.go.dev/net/url#Error) containing `connection refused`: This may occur due to transient network issues.
    * [`url.Error`](https://pkg.go.dev/net/url#Error) containing `connection reset by peer`: This means that Google Cloud has reset the connection.
    * [`net.ErrClosed`](https://pkg.go.dev/net#ErrClosed): This means that Google Cloud has closed the connection.
  * HTTP codes: 
    * `408 Request Timeout`
    * `429 Too Many Requests`
    * `500 Internal Server Error`
    * `502 Bad Gateway`
    * `503 Service Unavailable`
    * `504 Gateway Timeout`
  * Errors that implement the `Temporary()` interface and give a value of `err.Temporary() == true`
  * Any of the above errors that have been wrapped using [Go 1.13 error wrapping](https://go.dev/blog/go1.13-errors)



All exponential backoff settings in the Go library are configurable. By default, operations in Go use the following settings for exponential backoff (defaults are taken from [gax](https://pkg.go.dev/github.com/googleapis/gax-go/v2#Backoff)):

Setting | Default value (in seconds)  
---|---  
Auto retry | True if idempotent  
Max number of attempts | No limit  
Initial retry delay | 1 second  
Retry delay multiplier | 2.0  
Maximum retry delay | 30 seconds  
Total timeout (resumable upload chunk) | 32 seconds  
Total timeout (all other operations) | No limit  
  
In general, retrying continues indefinitely unless the controlling context is canceled, the client is closed, or a non-transient error is received. To stop retries from continuing, use context timeouts or cancellation. The only exception to this behavior is when [performing resumable uploads](https://docs.cloud.google.com/storage/docs/performing-resumable-uploads) using [Writer](https://pkg.go.dev/cloud.google.com/go/storage#Writer), where the data is large enough that it requires multiple requests. In this scenario, each chunk times out and stops retrying after 32 seconds by default. You can adjust the default timeout by changing `Writer.ChunkRetryDeadline`.

There is a [subset of Go operations](https://docs.cloud.google.com/storage/docs/retry-strategy#idempotency-operations) that are conditionally idempotent (conditionally safe to retry). These operations only retry if they meet specific conditions:

  * `GenerationMatch` or `Generation`

    * Safe to retry if a `GenerationMatch` precondition was applied to the call, or if `ObjectHandle.Generation` was set.
  * `MetagenerationMatch`

    * Safe to retry if a `MetagenerationMatch` precondition was applied to the call.
  * `Etag`

    * Safe to retry if the method inserts an `etag` into the JSON request body. Only used in `HMACKeyHandle.Update` when `HmacKeyMetadata.Etag` has been set.



`RetryPolicy` is set to `RetryPolicy.RetryIdempotent` by default. See [Customize retries](https://docs.cloud.google.com/storage/docs/retry-strategy#customize-retries) for examples on how to modify the default retry behavior.

### Java

By default, operations support retries for the following errors:

  * Connection errors: 
    * `Connection reset by peer`: This means that Google Cloud has reset the connection.
    * `Unexpected connection closure`: This means Google Cloud has closed the connection.
  * HTTP codes: 
    * `408 Request Timeout`
    * `429 Too Many Requests`
    * `500 Internal Server Error`
    * `502 Bad Gateway`
    * `503 Service Unavailable`
    * `504 Gateway Timeout`



All exponential backoff settings in the Java library are configurable. By default, operations through Java use the following settings for exponential backoff:

Setting | Default value (in seconds)  
---|---  
Auto retry | True if idempotent  
Max number of attempts | 6  
Initial retry delay | 1 second  
Retry delay multiplier | 2.0  
Maximum retry delay | 32 seconds  
Total Timeout | 50 seconds  
Initial RPC Timeout | 50 seconds  
RPC Timeout Multiplier | 1.0  
Max RPC Timeout | 50 seconds  
Connect Timeout | 20 seconds  
Read Timeout | 20 seconds  
  
For more information about the settings, see the Java reference documentation for [`RetrySettings.Builder`](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings.Builder) and [`HttpTransportOptions.Builder`](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.http.HttpTransportOptions.Builder).

There is a [subset of Java operations](https://docs.cloud.google.com/storage/docs/retry-strategy#idempotency-operations) that are conditionally idempotent (conditionally safe to retry). These operations only retry if they include specific arguments:

  * `ifGenerationMatch` or `generation`

    * Safe to retry if `ifGenerationMatch` or `generation` was passed in as an option to the method.
  * `ifMetagenerationMatch`

    * Safe to retry if `ifMetagenerationMatch` was passed in as an option.



`StorageOptions.setStorageRetryStrategy` is set to `StorageRetryStrategy#getDefaultStorageRetryStrategy` by default. See [Customize retries](https://docs.cloud.google.com/storage/docs/retry-strategy#customize-retries) for examples on how to modify the default retry behavior.

### Node.js

By default, operations support retries for the following error codes:

  * Connection errors: 
    * `EAI_again`: This is a DNS lookup error. For more information, see the [`getaddrinfo` documentation](https://man7.org/linux/man-pages/man3/getaddrinfo.3.html).
    * `Connection reset by peer`: This means that Google Cloud has reset the connection.
    * `Unexpected connection closure`: This means Google Cloud has closed the connection.
  * HTTP codes: 
    * `408 Request Timeout`
    * `429 Too Many Requests`
    * `500 Internal Server Error`
    * `502 Bad Gateway`
    * `503 Service Unavailable`
    * `504 Gateway Timeout`



All exponential backoff settings in the Node.js library are configurable. By default, operations through Node.js use the following settings for exponential backoff:

Setting | Default value (in seconds)  
---|---  
Auto retry | True if idempotent  
Maximum number of retries | 3  
Initial wait time | 1 second  
Wait time multiplier per iteration | 2  
Maximum amount of wait time | 64 seconds  
Default deadline | 600 seconds  
  
There is a [subset of Node.js operations](https://docs.cloud.google.com/storage/docs/retry-strategy#idempotency-operations) that are conditionally idempotent (conditionally safe to retry). These operations only retry if they include specific arguments:

  * `ifGenerationMatch` or `generation`

    * Safe to retry if `ifGenerationMatch` or `generation` was passed in as an option to the method. Often, methods only accept one of these two parameters.
  * `ifMetagenerationMatch`

    * Safe to retry if `ifMetagenerationMatch` was passed in as an option.



`retryOptions.idempotencyStrategy` is set to `IdempotencyStrategy.RetryConditional` by default. See [Customize retries](https://docs.cloud.google.com/storage/docs/retry-strategy#customize-retries) for examples on how to modify the default retry behavior.

### PHP

The PHP client library uses [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff) by default.

By default, operations support retries for the following error codes:

  * Connection errors: 
    * `connetion-refused`: This may occur due to transient network issues.
    * `connection-reset`: This means that Google Cloud has reset the connection.
  * HTTP codes: 
    * `200`: for partial download cases
    * `408 Request Timeout`
    * `429 Too Many Requests`
    * `500 Internal Server Error`
    * `502 Bad Gateway`
    * `503 Service Unavailable`
    * `504 Gateway Timeout`



Some exponential backoff settings in the PHP library are configurable. By default, operations through PHP use the following settings for exponential backoff:

Setting | Default value (in seconds)  
---|---  
Auto retry | True if idempotent  
Initial retry delay | 1 second  
Retry delay multiplier | 2.0  
Maximum retry delay | 60 seconds  
Request timeout | 0 with REST, 60 with gRPC  
Default number of retries | 3  
  
There is a [subset of PHP operations](https://docs.cloud.google.com/storage/docs/retry-strategy#idempotency-operations) that are conditionally idempotent (conditionally safe to retry). These operations only retry if they include specific arguments:

  * `ifGenerationMatch` or `generation`

    * Safe to retry if `ifGenerationMatch` or `generation` was passed in as an option to the method. Often, methods only accept one of these two parameters.
  * `ifMetagenerationMatch`

    * Safe to retry if `ifMetagenerationMatch` was passed in as an option.



When creating `StorageClient` the `StorageClient::RETRY_IDEMPOTENT` strategy is used by default. See [Customize retries](https://docs.cloud.google.com/storage/docs/retry-strategy#customize-retries) for examples on how to modify the default retry behavior.

### Python

By default, operations support retries for the following error codes:

  * Connection errors: 
    * `requests.exceptions.ConnectionError`
    * `requests.exceptions.ChunkedEncodingError` (only for operations that fetch or send payload data to objects, like uploads and downloads)
    * `ConnectionError`
    * `http.client.ResponseNotReady`
    * `urllib3.exceptions.TimeoutError`
  * HTTP codes: 
    * `408 Request Timeout`
    * `429 Too Many Requests`
    * `500 Internal Server Error`
    * `502 Bad Gateway`
    * `503 Service Unavailable`
    * `504 Gateway Timeout`



Operations through Python use the following default settings for exponential backoff:

Setting | Default value (in seconds)  
---|---  
Auto retry | True if idempotent  
Initial wait time | 1  
Wait time multiplier per iteration | 2  
Maximum amount of wait time | 60  
Default deadline | 120  
  
In addition to Cloud Storage operations that are always idempotent, the Python client library automatically retries [Objects: insert](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/insert), [Objects: delete](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/delete), and [Objects: patch](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/patch) by default.

There is a [subset of Python operations](https://docs.cloud.google.com/storage/docs/retry-strategy#idempotency-operations) that are conditionally idempotent (conditionally safe to retry) when they include specific arguments. These operations only retry if a [condition case](https://github.com/googleapis/python-storage/blob/1dc6d647b86466bf133fe03ec8d76c541e19c632/google/cloud/storage/retry.py#L60) passes:

  * `DEFAULT_RETRY_IF_GENERATION_SPECIFIED`

    * Safe to retry if `generation` or `if_generation_match` was passed in as an argument to the method. Often methods only accept one of these two parameters.
  * `DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED`

    * Safe to retry if `if_metageneration_match` was passed in as an argument to the method.
  * `DEFAULT_RETRY_IF_ETAG_IN_JSON`

    * Safe to retry if the method inserts an `etag` into the JSON request body. For `HMACKeyMetadata.update()` this means etag must be set on the `HMACKeyMetadata` object itself. For the `set_iam_policy()` method on other classes, this means the etag must be set in the "policy" argument passed into the method.



### Ruby

By default, operations support retries for the following error codes:

  * Connection errors: 
    * `SocketError`
    * `HTTPClient::TimeoutError`
    * `Errno::ECONNREFUSED`
    * `HTTPClient::KeepAliveDisconnected`
  * HTTP codes: 
    * `408 Request Timeout`
    * `429 Too Many Requests`
    * `5xx Server Error`



All exponential backoff settings in the Ruby client library are configurable. By default, operations through the Ruby client library use the following settings for exponential backoff:

Setting | Default value  
---|---  
Auto retry | True  
Max number of retries | 3  
Initial wait time | 1 second  
Wait time multiplier per iteration | 2  
Maximum amount of wait time | 60 seconds  
Default deadline | 900 seconds  
  
There is a [subset of Ruby operations](https://docs.cloud.google.com/storage/docs/retry-strategy#idempotency-operations) that are conditionally idempotent (conditionally safe to retry) when they include specific arguments:

  * `if_generation_match` or `generation`

    * Safe to retry if the `generation` or `if_generation_match` parameter is passed in as an argument to the method. Often methods only accept one of these two parameters.
  * `if_metageneration_match`

    * Safe to retry if the `if_metageneration_match` parameter is passed in as an option.



By default, all idempotent operations are retried, and conditionally idempotent operations are retried only if the condition case passes. Non-idempotent operations are not retried. See [Customize retries](https://docs.cloud.google.com/storage/docs/retry-strategy#customize-retries) for examples on how to modify the default retry behavior.

### REST APIs

When calling the JSON or XML API directly, you should use the exponential backoff algorithm to implement your own retry strategy.

## Customizing retries

### Console

You cannot customize the behavior of retries using the Google Cloud console.

### Command line

For `gcloud storage` commands, you can control the retry strategy by creating a [named configuration](https://docs.cloud.google.com/sdk/gcloud/reference/topic/configurations) and setting some or all of the following properties:

Setting | Default value (in seconds)  
---|---  
`base_retry_delay` | 1  
`exponential_sleep_multiplier` | 2  
`max_retries` | 32  
`max_retry_delay` | 32  
  
You then apply the defined configuration either on a per-command basis by using the [`--configuration` project-wide flag](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration) or for all Google Cloud CLI commands by using the [`gcloud config set` command](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).

### Client libraries

### C++

To customize the retry behavior, provide values for the following options when you initialize the `google::cloud::storage::Client` object:

  * `google::cloud::storage::RetryPolicyOption`: The library provides `google::cloud::storage::LimitedErrorCountRetryPolicy` and `google::cloud::storage::LimitedTimeRetryPolicy` classes. You can provide your own class, which must implement the `google::cloud::RetryPolicy` interface.

  * `google::cloud::storage::BackoffPolicyOption`: The library provides the `google::cloud::storage::ExponentialBackoffPolicy` class. You can provide your own class, which must implement the `google::cloud::storage::BackoffPolicy` interface.

  * `google::cloud::storage::IdempotencyPolicyOption`: The library provides the `google::cloud::storage::StrictIdempotencyPolicy` and `google::cloud::storage::AlwaysRetryIdempotencyPolicy` classes. You can provide your own class, which must implement the `google::cloud::storage::IdempotencyPolicy` interface.




For more information, see the [C++ client library reference documentation](https://googleapis.dev/cpp/google-cloud-storage/latest/structgoogle_1_1cloud_1_1storage_1_1RetryPolicyOption.html). 
    
    
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

### C#

You cannot customize the default retry strategy used by the C# client library.

### Go

When you initialize a storage client, a default retry configuration will be set. Unless they're overridden, the options in the config are set to the default values. Users can configure non-default retry behavior for a single library call (using [BucketHandle.Retryer](https://pkg.go.dev/cloud.google.com/go/storage#BucketHandle.Retryer) and [ObjectHandle.Retryer](https://pkg.go.dev/cloud.google.com/go/storage#ObjectHandle.Retryer)) or for all calls made by a client (using [Client.SetRetry](https://pkg.go.dev/cloud.google.com/go/storage#Client.SetRetry)). To modify retry behavior, pass in the relevant [RetryOptions](https://pkg.go.dev/cloud.google.com/go/storage#RetryOption) to one of these methods.

See the following code sample to learn how to customize your retry behavior.
    
    
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

When you initialize [`Storage`](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage), an instance of [`RetrySettings`](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetrySettings) is initialized as well. Unless they are overridden, the options in the `RetrySettings` are set to the default values. To modify the default automatic retry behavior, pass the custom `StorageRetryStrategy` into the `StorageOptions` used to construct the `Storage` instance. To modify any of the other scalar parameters, pass a custom `RetrySettings` into the `StorageOptions` used to construct the `Storage` instance.

See the following example to learn how to customize your retry behavior:
    
    
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

When you initialize Cloud Storage, a retryOptions config file is initialized as well. Unless they're overridden, the options in the config are set to the default values. To modify the default retry behavior, pass the custom retry configuration [`retryOptions`](https://googleapis.dev/nodejs/storage/latest/global.html#StorageOptions) into the storage constructor upon initialization. The Node.js client library can automatically use backoff strategies to retry requests with the [`autoRetry`](https://googleapis.dev/nodejs/storage/latest/global.html#StorageOptions) parameter.

See the following code sample to learn how to customize your retry behavior.
    
    
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

When you initialize a storage client, a default retry configuration will be set. Unless they're overridden, the options in the config are set to the default values. Users can configure non-default retry behavior for a client or a single operation call by passing override options in an array.

See the following code sample to learn how to customize your retry behavior.
    
    
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

To modify the default retry behavior, create a copy of the `google.cloud.storage.retry.DEFAULT_RETRY` object by calling it with a `with_BEHAVIOR` method. The Python client library automatically uses backoff strategies to retry requests if you include the `DEFAULT_RETRY` parameter.

Note that `with_predicate` is not supported for operations that fetch or send payload data to objects, like uploads and downloads. It's recommended that you modify attributes one by one. For more information, see the [google-api-core Retry reference](https://googleapis.dev/python/google-api-core/latest/retry.html).

To configure your own conditional retry, create a [`ConditionalRetryPolicy`](https://github.com/googleapis/python-storage/blob/1dc6d647b86466bf133fe03ec8d76c541e19c632/google/cloud/storage/retry.py#L60) object and wrap your custom `Retry` object with `DEFAULT_RETRY_IF_GENERATION_SPECIFIED`, `DEFAULT_RETRY_IF_METAGENERATION_SPECIFIED`, or `DEFAULT_RETRY_IF_ETAG_IN_JSON`.

See the following code sample to learn how to customize your retry behavior.
    
    
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

When you initialize the storage client, all retry configurations are set to the values shown in the table above. To modify the default retry behavior, pass retry configurations while initializing the storage client.

To override the number of retries for a particular operation, pass `retries` in the `options` parameter of the operation.
    
    
    def configure_retries bucket_name: nil, file_name: nil
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      require "google/cloud/storage"
    
      # Creates a client
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)(
    
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

### REST APIs

Use the exponential backoff algorithm to implement your own retry strategy.

## Exponential backoff algorithm

An [exponential backoff algorithm](https://en.wikipedia.org/wiki/Exponential_backoff) retries requests using exponentially increasing waiting times between requests, up to a maximum backoff time. You should generally use exponential backoff with jitter to retry requests that meet both the response and idempotency criteria. For best practices implementing automatic retries with exponential backoff, see [Addressing Cascading Failures](https://sre.google/sre-book/addressing-cascading-failures/).

## Retry anti-patterns

It is recommended to use or customize the built-in retry mechanisms where applicable; see [customizing retries](https://docs.cloud.google.com/storage/docs/retry-strategy#customize-retries). Whether you are using the default retry mechanisms, customizing them, or implementing your own retry logic, it's crucial to avoid the following common [anti-patterns](https://en.wikipedia.org/wiki/Anti-pattern) as they can exacerbate issues rather than resolve them.

#### Retrying without backoff

Retrying requests immediately or with very short delays can lead to cascading failures which are failures that might trigger other failures.

**How to avoid this** : Implement exponential backoff with jitter. This strategy progressively increases the wait time between retries and adds a random element to prevent retries from overwhelming the service.

#### Unconditionally retrying non-idempotent operations

Repeatedly executing operations that are not idempotent can lead to unintended side effects, such as unintended overwrites or deletions of data.

**How to avoid this** : Thoroughly understand the idempotency characteristics of each operation as detailed in the [idempotency of operations](https://docs.cloud.google.com/storage/docs/retry-strategy#idempotency-operations) section. For non-idempotent operations, ensure your retry logic can handle potential duplicates or avoid retrying them altogether. Be cautious with retries that may lead to race conditions.

#### Retrying unretryable errors

Treating all errors as able to be tried again can be problematic. Some errors for example, authorization failures or invalid requests are persistent and retrying them without addressing the underlying cause won't be successful and may result in applications getting caught in an infinite loop.

**How to avoid this** : Categorize errors into transient (retryable) and permanent (non-retryable). Only retry transient errors like `408`, `429`, and `5xx` HTTP codes, or specific connection issues. For permanent errors, log them and handle the underlying cause appropriately.

#### Ignoring retry limits

Retrying indefinitely can lead to resource exhaustion in your application or continuously send requests to a service that won't recover without intervention.

**How to avoid this** : Tailor retry limits to the nature of your workload. For latency sensitive workloads, consider setting a total maximum retry duration to ensure a timely response or failure. For batch workloads, which might tolerate longer retry periods for transient server side errors, consider setting a higher total retry limit.

#### Unnecessarily layering retries

Adding custom application level retry logic on top of the existing retry mechanisms can lead to an excessive number of retry attempts. For example, if your application retries an operation three times, and the underlying client library also retries it three times for each of your application's attempts, you could end up with nine retry attempts. Sending high amounts of retries for errors that cannot be retried might lead to request throttling, limiting the throughput of all workloads. High numbers of retries might also increase latency of requests without improving the success rate.

**How to avoid this** : We recommend using and configuring the built-in retry mechanisms. If you must implement application-level retries, like for specific business logic that spans multiple operations, do so with a clear understanding of the underlying retry behavior. Consider disabling or significantly limiting retries in one of the layers to prevent multiplicative effects.

## What's next

  * Learn more about [request preconditions](https://docs.cloud.google.com/storage/docs/request-preconditions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
