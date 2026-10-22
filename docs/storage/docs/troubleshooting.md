---
url: https://docs.cloud.google.com/storage/docs/troubleshooting/
title: Troubleshooting \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:29:23.694776+00:00
---

# Troubleshooting  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page describes troubleshooting methods for common errors you may encounter while using Cloud Storage.

See the [Google Cloud Personalized Service Health Dashboard](https://status.cloud.google.com/summary) for information about incidents affecting Google Cloud services such as Cloud Storage.

## Logging raw requests

**Important:** Never share your credentials. When you print out HTTP protocol details, your authentication credentials, such as OAuth 2.0 tokens, are visible in the headers. If you need to post request or response details to a message board or need to supply them for troubleshooting, make sure that you sanitize or revoke any credentials that appear as part of the output.

When using tools such as `gcloud` or the Cloud Storage client libraries, much of the request and response information is handled by the tool. However, it is sometimes useful to see details to aid in troubleshooting or when posting questions to forums such as [Stack Overflow](https://stackoverflow.com/questions/tagged/google-cloud-storage). Use the following instructions to return request and response headers for your tool:

### Console

Viewing request and response information depends on the browser you're using to access the Google Cloud console. For the Google Chrome browser:

  1. Click Chrome's **main menu** button (_more_vert_).

  2. Select **More Tools**.

  3. Click **Developer Tools**.

  4. In the pane that appears, click the **Network** tab.




### Command line

Use global debugging flags in your request. For example:
    
    
    gcloud storage ls gs://my-bucket/my-object --log-http --verbosity=debug

### Client libraries

### C++

  * Set the environment variable `CLOUD_STORAGE_ENABLE_TRACING=http` to get the full HTTP traffic.

  * Set the environment variable CLOUD_STORAGE_ENABLE_CLOG=yes to get logging of each RPC.




### C#

Add a logger by using the `ApplicationContext.RegisterLogger` method, and set logging options on the `HttpClient` message handler. For more information, see the [C# client library reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest).

### Go

Set the environment variable `GODEBUG=http2debug=1`. For more information, see the [Go package net/http](https://golang.org/pkg/net/http/).

If you want to log the request body as well, [use a custom HTTP client](https://pkg.go.dev/google.golang.org/api/option#WithHTTPClient).

### Java

  1. Create a file named "logging.properties" with the following contents:
         
         # Properties file which configures the operation of the JDK logging facility.
         # The system will look for this config file to be specified as a system property:
         # -Djava.util.logging.config.file=${project_loc:googleplus-simple-cmdline-sample}/logging.properties
         
         # Set up the console handler (uncomment "level" to show more fine-grained messages)
         handlers = java.util.logging.ConsoleHandler
         java.util.logging.ConsoleHandler.level = CONFIG
         
         # Set up logging of HTTP requests and responses (uncomment "level" to show)
         com.google.api.client.http.level = CONFIG

  2. Use logging.properties with Maven
         
         mvn -Djava.util.logging.config.file=path/to/logging.properties insert_command




For more information, see [Pluggable HTTP Transport](https://googleapis.github.io/google-http-java-client/http-transport.html).

### Node.js

Set the environment variable `NODE_DEBUG=https` before calling the Node script.

### PHP

Provide your own HTTP handler to the client using [`httpHandler`](https://docs.cloud.google.com/php/docs/reference/cloud-storage/latest/StorageClient) and set up middleware to log the request and response.

### Python

Use the [logging module](https://docs.python.org/3/library/logging.html). For example:
    
    
    import logging
    import http.client
    
    logging.basicConfig(level=logging.DEBUG)
    http.client.HTTPConnection.debuglevel=5

### Ruby

At the top of your `.rb file` after `require "google/cloud/storage"`, add the following:
    
    
    ruby
    Google::Apis.logger.level = Logger::DEBUG

## Adding custom headers

Adding custom headers to requests is a common tool for debugging purposes, such as for enabling debug headers or for tracing a request. The following example shows how to set request headers for different Cloud Storage tools:

### Command line

Use the `--additional-headers` flag, which is available for most commands. For example:
    
    
    gcloud storage objects describe gs://my-bucket/my-object --additional-headers=HEADER_NAME=HEADER_VALUE

Where `HEADER_NAME` and `HEADER_VALUE` define the header you are adding to the request.

**Note:** The `--additional-headers` flag is not available for all `gcloud storage` commands, such as commands working with Identity and Access Management (IAM) policies and `buckets notifications` commands.

### Client libraries

### C++
    
    
    namespace gcs = google::cloud::storage;
    gcs::Client client = ...;
    client.AnyFunction(... args ..., gcs::CustomHeader("header-name", "value"));
    

**Note:** The C++ client library supports only one custom header at a time.

### C#

The following sample adds a custom header to every request made by the client library.
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    
    var client = [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html#Google_Cloud_Storage_V1_StorageClient_Create)();
    client.Service.HttpClient.DefaultRequestHeaders.Add("custom-header", "custom-value");
    
    var buckets = client.ListBuckets("my-project-id");
    foreach (var bucket in buckets)
    
    {
      Console.WriteLine(bucket.Name);
    }
    

### Go

You can add custom headers to any API call made by the Storage package by using [callctx.SetHeaders](https://pkg.go.dev/github.com/googleapis/gax-go/v2/callctx#SetHeaders) on the context which is passed to the method.
    
    
    package main
    
    import (
      "context"
    
      "cloud.google.com/go/storage"
      "github.com/googleapis/gax-go/v2/callctx"
    )
    
    func main() {
      ctx := context.Background()
    
      client, err := storage.NewClient(ctx)
      if err != nil {
        // Handle error.
      }
      ctx = callctx.SetHeaders(ctx, "X-Custom-Header", "value")
    
      // Use client as usual with the context and the additional headers will be sent.
      _, err = client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)("my-bucket").Attrs(ctx)
      if err != nil {
        // Handle error.
      }
    }
    

### Java
    
    
    import com.google.api.gax.rpc.[FixedHeaderProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.FixedHeaderProvider.html);
    import com.google.api.gax.rpc.[HeaderProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.HeaderProvider.html);
    import com.google.cloud.[WriteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.WriteChannel.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    import java.io.IOException;
    import java.nio.ByteBuffer;
    import static java.nio.charset.StandardCharsets.UTF_8;
    
    public class Example {
    
      public void main([String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) args[]) throws IOException {
        [HeaderProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.HeaderProvider.html) headerProvider =
                [FixedHeaderProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.FixedHeaderProvider.html).create("custom-header", "custom-value");
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).getDefaultInstance()
                .toBuilder()
                .setHeaderProvider(headerProvider)
                .build().getService();
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) bucketName = "example-bucket";
        [String](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.common.Type.String.html) blobName = "test-custom-header";
    
        // Use client with custom header
        [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blob = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder(bucketName, blobName).build();
        byte[] stringBytes;
        try ([WriteChannel](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.WriteChannel.html) writer = storage.[writer](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_writer_com_google_cloud_storage_BlobInfo_com_google_cloud_storage_Storage_BlobWriteOption____)(blob)) {
          stringBytes = "hello world".getBytes(UTF_8);
          writer.write(ByteBuffer.wrap(stringBytes));
        }
      }
    }
    

### Node.js
    
    
    const storage = new Storage();
    
    storage.interceptors.push({
      request: requestConfig => {
        Object.assign(requestConfig.headers, {
          'X-Custom-Header': 'value',
          });
        return requestConfig;
      },
    });
    

### PHP

All method calls which trigger http requests accept an optional `$restOptions` argument as the last argument. You can provide custom headers on a per-request basis, or on a per-client basis.
    
    
    use Google\Cloud\Storage\StorageClient;
    
    $client = new StorageClient([
       'restOptions' => [
           'headers' => [
               'x-foo' => 'bat'
           ]
       ]
    ]);
    
    $bucket = $client->bucket('my-bucket');
    
    $bucket->info([
       'restOptions' => [
           'headers' => [
               'x-foo' => 'bar'
           ]
       ]
    ]);
    

### Python
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(
        extra_headers={
            "x-custom-header": "value"
        }
    )
    

### Ruby
    
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
    
    storage.[add_custom_headers](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage-Project.html) { 'X-Custom-Header'=> 'value' }
    

### Rust
    
    
    use google_cloud_gax::options::RequestOptionsBuilder;
    use google_cloud_storage::client::Storage;
    use google_cloud_storage::client::StorageControl;
    use http::header::{HeaderName, HeaderValue};
    
    pub async fn sample(bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "hello-world.txt";
    
        // Set a client-level custom header on the Storage data plane client.
        let client = Storage::builder()
            .with_custom_header(
                HeaderName::from_static("x-custom-header"),
                HeaderValue::from_static("custom-value"),
            )
            .build()
            .await?;
    
        let reader = client
            .read_object(format!("projects/_/buckets/{bucket_id}"), NAME)
            .send()
            .await?;
        println!("Object highlights: {:?}", reader.object());
    
        // Set a request-level custom header on a StorageControl RPC request.
        let control = StorageControl::builder().build().await?;
        let bucket = control
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .with_custom_header(
                HeaderName::from_static("x-custom-header"),
                HeaderValue::from_static("custom-value"),
            )
            .send()
            .await?;
        println!("Bucket {bucket_id} metadata is {bucket:?}");
    
        Ok(())
    }

## Accessing buckets with a CORS configuration

If you have set a CORS configuration on your bucket and notice that incoming requests from client browsers are failing, try the following troubleshooting steps:

  1. [Review the CORS configuration](https://docs.cloud.google.com/storage/docs/using-cors#viewing-cors-bucket) on the target bucket. If there are multiple CORS configuration entries, make sure that the request values you use for troubleshooting map to values in a single CORS configuration entry.

  2. When testing issuing a CORS request, check that you are not making a request to the `storage.cloud.google.com` endpoint, which doesn't allow CORS requests. For more information about supported endpoints for CORS, see [Cloud Storage CORS support](https://docs.cloud.google.com/storage/docs/cross-origin#server-side-support).

  3. Review a request and response using the tool of your choice. In a Chrome browser, you can use the standard developer tools to see this information:

     1. Click the Chrome menu (_more_vert_) on the browser toolbar.
     2. Select **More Tools** > **Developer Tools**.
     3. Click the **Network** tab.
     4. From your application or command line, send the request.
     5. In the pane displaying the network activity, locate the request.
     6. In the **Name** column, click the name corresponding to the request.
     7. Click the **Headers** tab to see the response headers, or the **Response** tab to see the content of the response.

If you don't see a request and response, it's possible that your browser has cached an earlier failed preflight request attempt. Clearing your browser's cache should also clear the preflight cache. If it doesn't, set the `MaxAgeSec` value in your CORS configuration to a lower value than the default value of `3600` (60 minutes), wait for however long the old `MaxAgeSec` was, then try the request again. This performs a new preflight request, which fetches the new CORS configuration and purges the cache entries. Once you have debugged your problem, raise `MaxAgeSec` back to a higher value to reduce the preflight traffic to your bucket.

  4. Ensure that the request has an `Origin` header and that the header value matches at least one of the `Origins` values in the bucket's CORS configuration. Note that the scheme, host, and port of the values must match exactly. Some examples of acceptable matches are the following:

     * `http://origin.example.com` matches `http://origin.example.com:80` (because 80 is the default HTTP port) but doesn't match `https://origin.example.com`, `http://origin.example.com:8080`, `http://origin.example.com:5151`, or `http://sub.origin.example.com`.

     * `https://example.com:443` matches `https://example.com` but not `http://example.com` or `http://example.com:443`.

     * `http://localhost:8080` only matches exactly `http://localhost:8080` and doesn't match `http://localhost:5555` or `http://localhost.example.com:8080`.

  5. For simple requests, ensure that the HTTP method of the request matches at least one of the `Methods` values in the bucket's CORS configuration. For preflight requests, ensure that the method specified in `Access-Control-Request-Method` matches at least one of the `Methods` values.

  6. For preflight requests, check if it includes one or more `Access-Control-Request-Header` headers. If so, ensure that each `Access-Control-Request-Header` value matches a `ResponseHeader` value in the bucket's CORS configuration. All headers named in the `Access-Control-Request-Header` must be in the CORS configuration for the preflight request to succeed and include CORS headers in the response.




## Error codes

The following are common HTTP status codes you may encounter.

### 301: Moved Permanently

**Issue** : I'm [setting up a static website](https://docs.cloud.google.com/storage/docs/hosting-static-website), and accessing a directory path returns an empty object and a `301` HTTP response code.

**Solution** : If your browser downloads a zero byte object and you get a `301` HTTP response code when accessing a directory, such as `http://www.example.com/dir/`, your bucket most likely contains an empty object of that name. To check that this is the case and fix the issue:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the **Activate Cloud Shell** button at the top of the Google Cloud console.
  3. Run `gcloud storage ls --recursive gs://www.example.com/dir/`. If the output includes `http://www.example.com/dir/`, you have an empty object at that location.
  4. Remove the empty object with the command: `gcloud storage rm gs://www.example.com/dir/`



You can now access `http://www.example.com/dir/` and have it return that directory's `index.html` file instead of the empty object.

### 400: Bad Request

**Issue** : While performing a [resumable upload](https://docs.cloud.google.com/storage/docs/resumable-uploads), I received this error and the message `Failed to parse Content-Range header.`

**Solution** : The value you used in your `Content-Range` header is invalid. For example, `Content-Range: */*` is invalid and instead should be specified as `Content-Range: bytes */*`. If you receive this error, your current resumable upload is no longer active, and you must start a new resumable upload.

### 400: Storage Intelligence specific errors

For solutions to common errors encountered when configuring or managing Storage Intelligence, Storage Insights, and Storage batch operations, see [Troubleshooting Storage Intelligence issues](https://docs.cloud.google.com/storage/docs/storage-intelligence/troubleshooting).

### 401: Unauthorized

**Issue** : Requests to a public bucket directly, or using Cloud CDN, are failing with a `HTTP 401: Unauthorized` and an `Authentication Required` response.

**Solution** : Check that your client, or any intermediate proxy, is not adding an `Authorization` header to requests to Cloud Storage. Any request with an `Authorization` header, even if empty, is validated as if it were an authentication attempt.

### 403: Account Disabled

**Issue** : I tried to create a bucket but got a `403 Account Disabled` error.

**Solution** : This error indicates that you have not yet turned on billing for the associated project. For steps for enabling billing, see [Enable billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_a_project).

If billing is turned on and you continue to receive this error message, you can reach out to [support](https://support.google.com/cloud/answer/6282346) with your [project ID](https://docs.cloud.google.com/docs/overview#projects) and a description of your problem.

### 403: Forbidden

**Issue** : I should have permission to access a certain bucket or object, but when I attempt to do so, I get a `403 - Forbidden` error with a message that is similar to: `example@email.com doesn't have storage.objects.get access to the Google Cloud Storage object`.

**Solution** : You are missing an IAM permission for the bucket or object that is required to complete the request. If you expect to be able to make the request but can't, perform the following checks:

  1. Is the grantee referenced in the error message the one you expected? If the error message refers to an unexpected email address or to "Anonymous caller", then your request is not using the credentials you intended. This could be because the tool you are using to make the request was set up with the credentials from another alias or entity, or it could be because the request is being made on your behalf by a [service account](https://docs.cloud.google.com/storage/docs/projects#service-accounts).

  2. Is the permission referenced in the error message one thought you needed? If the permission is unexpected, it's likely because the tool you're using requires additional access in order to complete your request. For example, in order to bulk delete objects in a bucket, `gcloud` must first construct a list of objects in the bucket to delete. This portion of the bulk delete action requires the `storage.objects.list` permission, which might be surprising, given that the goal is object deletion, which normally requires only the `storage.objects.delete` permission. If this is the cause of your error message, make sure you're granted [IAM roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles) that have the additional necessary permissions.

  3. Are you granted the IAM role on the intended resource or parent resource? For example, if you're granted the `Storage Object Viewer` role for a project and you're trying to download an object, make sure the object is in a bucket that's in the project; you might inadvertently have the `Storage Object Viewer` permission for a different project.

  4. Is your permission to access a certain bucket or object given through a [convenience value](https://docs.cloud.google.com/storage/docs/access-control/iam#convenience-values)? The removal of access granted to a convenience value can cause previously enabled principals to lose access to resources.

For example, say jane@example.com has the Owner (`roles/owner`) basic role for a project named `my-example-project`, and the project's IAM policy grants the Storage Object Creator (`roles/storage.objectCreator`) role to the convenience value `projectOwner:my-example-project`. Consequently, jane@example.com has the permissions associated with the Storage Object Creator role for buckets within `my-example-project`. If this grant gets removed, jane@example.com loses the permissions associated with the Storage Object Creator role.

In such a scenario, you can regain access to the bucket or object by granting yourself the necessary bucket-level or object-level permissions required to perform the actions you need.

  5. Is there an [IAM Deny policy](https://docs.cloud.google.com/iam/docs/deny-overview) that prevents you from using certain permissions? You can contact your organization administrator to find out whether an IAM Deny policy has been put in place.




### 403: Permission Denied

**Issue** : Permission denied error when you configure or manage the [Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/troubleshooting) configuration for a resource.

**Solution** : If you receive a permission denied error with a message similar to `permission storage.intelligenceConfigs.update` when you [configure and manage Storage Intelligence](https://docs.cloud.google.com/storage/docs/storage-intelligence/troubleshooting) for a resource, see the permission section for the operation you want to perform. To resolve this issue, grant the appropriate permissions. You can grant permissions in _any_ of the following ways:

  * Grant IAM permissions at the same [Google Cloud resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) resource that you are enabling Storage Intelligence on.
  * Ensure that a resource higher in the Google Cloud resource hierarchy passes the permissions to the child resource.



### 409: Conflict

**Issue** : I tried to create a bucket but received the following error: 
    
    
    409 Conflict. Sorry, that name is not available. Please try a different one.

**Solution** : The bucket name you tried to use (e.g. `gs://cats` or `gs://dogs`) is already taken. Cloud Storage has a global namespace so you may not name a bucket with the same name as an existing bucket. Choose a name that is not being used.

### 412: Custom constraints violated

**Issue** : My requests are being rejected with a `412 orgpolicy` error.

**Issue** : My requests are being rejected with a `412 Multiple constraints were violated` error.

**Solution** : Check with your security administrator team to see if the bucket to which you're sending requests is being affected by an organization policy that uses a custom constraint. Your bucket might also be affected by different organization policies that conflict with one another. For example, where one policy specifies that buckets must have the Standard storage class and another policy specifies that buckets must have the Coldline storage class.

### 429: Too Many Requests

**Issue** : My requests are being rejected with a `429 Too Many Requests` error.

**Solution** : You are hitting a limit to the number of requests Cloud Storage allows for a given resource. See the [Cloud Storage quotas](https://docs.cloud.google.com/storage/quotas) for a discussion of limits in Cloud Storage.

  * If your workload consists of 1000's of requests per second to a bucket, see [Request rate and access distribution guidelines](https://docs.cloud.google.com/storage/docs/request-rate) for a discussion of best practices, including ramping up your workload gradually and avoiding sequential filenames.

  * If your workload is potentially using 50 Gbps or more of network egress to specific locations, [check your bandwidth usage](https://docs.cloud.google.com/storage/docs/bandwidth-usage#bandwidth-monitoring) to ensure you're not encountering a bandwidth quota.




## Object context errors

This section describes common errors you might experience when working with [object contexts](https://docs.cloud.google.com/storage/docs/object-contexts).

### 400: Object Context Limit Exceeded

**Issue** : The error indicates that the object has exceeded the limit of 50 contexts.

**Solution** : You have exceeded the [limit](https://docs.cloud.google.com/storage/quotas#objects) for object contexts per object. Reduce the number of context key-value pairs and try again.

### 400: Object Context Key Or Value Size Limit Exceeded

**Issue** : The error indicates that the size of an object context key or value exceeds the limit of 256 bytes.

**Solution** : Each object context key and value must be 256 bytes or less (UTF-8 encoded). Shorten the key or value and try again.

### 400: Object Context Key Or Value Aggregate Size Limit Exceeded

**Issue** : The error indicates that the aggregate size of all object context keys and values exceeds the limit.

**Solution** : The total size of all context keys and values for an object must not exceed 25 KiB (25,600 bytes). Reduce the total amount of context data and try again.

### 400: Object Context Key Or Value Forbidden Characters

**Issue** : The error indicates that the object context key or value contains forbidden characters.

**Solution** : Object context keys and values can't contain single quotes (`'`), double quotes (`"`), backslashes (`\`), or forward slashes (`/`). Review your contexts and remove any invalid characters.

### 400: Object Context Key Or Value Must Start With an Alphanumeric Character

**Issue** : The error indicates that the object context key or value doesn't start with an alphanumeric character.

**Solution** : Object context keys and values must start with a letter or a decimal digit.

### 400: Object Context Key Or Value Empty

**Issue** : The error indicates that an object context key or value can't be empty.

**Solution** : Provide a non-empty string for both the key and the value of your object contexts.

### 400: Object Context Key Or Value Invalid UTF-8

**Issue** : The error indicates that an object context key or value is not a valid UTF-8 string.

**Solution** : Verify that all characters in your context keys and values are encoded using UTF-8.

### 400: Object Context Key Reserved Prefix

**Issue** : The error indicates that the object context key begins with a reserved prefix.

**Solution** : Certain prefixes are reserved for system use. Avoid using restricted prefixes, such as `goog`, in your context keys.

### 400: Object can't Have More Than 50 Drop Context Groups

**Issue** : The error indicates that the `drop_context_groups` parameter can't have more than 50 values.

**Solution** : Reduce the number of values in the `drop_context_groups` parameter and try again.

### 400: Invalid Value For Drop Context Groups Field

**Issue** : The error indicates that the `drop_context_groups` parameter contains an invalid value.

**Solution** : The only accepted value for the `drop_context_groups` parameter is `custom`.

## Diagnosing Google Cloud console errors

**Issue** : When using the Google Cloud console to perform an operation, I get a generic error message. For example, I see an error message when trying to delete a bucket, but I don't see details for why the operation failed.

**Solution** : Use the Google Cloud console's notifications to see detailed information about the failed operation:

  1. Click the **Notifications** button (_notifications_) in the Google Cloud console header.

A drop-down displays the most recent operations performed by the Google Cloud console.

  2. Click the item you want to find out more about.

A page opens up and displays detailed information about the operation.

  3. Click each row to expand the detailed error information.




**Issue** : When using the Google Cloud console, I don't see a particular column displayed.

**Solution** : To see a particular column displayed in the Google Cloud console, click the **Column display options** icon (view_column) and select the column you want displayed.

## Simulated folders and managed folders

**Issue** : I deleted some objects in my bucket, and now the folder that contained them doesn't appear in the Google Cloud console.

**Solution** : While the Google Cloud console displays your bucket's contents as if there was a directory structure, [folders don't fundamentally exist](https://docs.cloud.google.com/storage/docs/objects#namespace) in Cloud Storage. As a result, when you remove all objects with a common prefix from a bucket, the folder icon representing that group of objects no longer appears in the Google Cloud console.

**Issue** : I can't create managed folders.

**Solution** : To [create managed folders](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders), make sure the following requirements are met:

  * You have an IAM role that contains the `storage.managedfolders.create` permission, such as the Storage Object Admin (`roles/storage.objectAdmin`) role. For instructions on granting roles, see [Use IAM permissions](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions).

  * Uniform bucket-level access is [enabled on the bucket](https://docs.cloud.google.com/storage/docs/using-uniform-bucket-level-access) in which you want to create managed folders.

  * There are no IAM Conditions on the bucket or the project that use the bucket resource type (`storage.googleapis.com/Bucket`) or the object resource type (`storage.googleapis.com/Object`). If any bucket within a project has an IAM Condition that uses either of these resource types, managed folders can't be created in any of the buckets within that project, even if the condition is later removed.




**Issue** : I can't disable uniform bucket-level access because there are managed folders in my bucket.

**Solution** : Uniform bucket-level access can't be disabled if there are [managed folders](https://docs.cloud.google.com/storage/docs/managed-folders) in the bucket. To disable uniform bucket-level access, you'll need to first [delete all managed folders](https://docs.cloud.google.com/storage/docs/creating-managing-managed-folders#delete) in the bucket.

## Static website errors

The following are common issues that you may encounter when [setting up a bucket to host a static website](https://docs.cloud.google.com/storage/docs/hosting-static-website).

### HTTPS serving

**Issue** : I want to serve my content over HTTPS without using a [load balancer](https://docs.cloud.google.com/load-balancing/docs/https).

**Solution** : You can serve static content through HTTPS using direct URIs such as `https://storage.googleapis.com/my-bucket/my-object`. For other options to serve your content through a custom domain over SSL, you can:

  * Use a [third-party Content Delivery Network](https://docs.cloud.google.com/network-connectivity/docs/cdn-interconnect) with Cloud Storage.
  * Serve your static website content from [Firebase Hosting](https://firebase.google.com/docs/hosting/) instead of Cloud Storage.



### Inaccessible page

**Issue** : I get an `Access denied` error message for a web page served by my website.

**Solution** : Check that the object is shared publicly. If it is not, see [Making Data Public](https://docs.cloud.google.com/storage/docs/access-control/making-data-public) for instructions on how to do this.

If you previously uploaded and shared an object, but then upload a new version of it, then you must reshare the object publicly. This is because the public permission is replaced with the new upload.

### Content download

**Issue** : I am prompted to download my page's content, instead of being able to view it in my browser.

**Solution** : If you specify a `MainPageSuffix` as an object that doesn't have a web content type, site visitors are prompted to download the content instead of being able to see served page content. To resolve this issue, update the [`Content-Type`](https://docs.cloud.google.com/storage/docs/metadata#content-type) metadata entry to a suitable value, such as `text/html`. For instructions, see [Editing object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#edit).

## Make data public

**Issue** : I'm trying to make my data public but I get an organization policy error.

**Solution** : Some [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#constraints) can prevent you from making your data public. For example, the Domain Restricted Sharing constraint (`constraints/iam.allowedPolicyMemberDomains`) restricts resource sharing based on the organization's domain. For organization policy failures, contact your administrator to grant you the project or bucket-level permissions to allow resource sharing by [editing the organization policy for the organization, folder, or project resource](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints). If you continue to see this error after overriding the organization policy, then you might need to wait a few minutes for the change to take effect.

**Issue** : I get a permission error when I attempt to [make my data public](https://docs.cloud.google.com/storage/docs/access-control/making-data-public).

**Solution** : Make sure that you have the `storage.buckets.setIamPolicy` permission or the `storage.objects.setIamPolicy` permission. These permissions are granted, for example, in the [Storage Admin (`roles/storage.admin`) role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles#standard-roles). If you have the `storage.buckets.setIamPolicy` permission or the `storage.objects.setIamPolicy` permission and you still get an error, your bucket might be subject to [public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention), which doesn't allow access to `allUsers` or `allAuthenticatedUsers`. Public access prevention might be set on the bucket directly, or it might be enforced through an [organization policy](https://docs.cloud.google.com/storage/docs/org-policy-constraints#public-access-prevention) that is set at a higher level.

## Latency

The following are common latency issues you might encounter. In addition, the [Google Cloud Service Health Dashboard](https://status.cloud.google.com/summary) provides information about incidents affecting Google Cloud services such as Cloud Storage.

### Upload or download latency

**Issue** : I'm seeing increased latency when uploading or downloading.

**Solution** : Consider the following common causes of upload and download latency:

  * CPU or memory constraints: The affected environment's operating system should have tooling to measure local resource consumption such as CPU usage and memory usage.

  * Disk IO constraints: The performance impact might be caused by local disk IO.

  * Geographical distance: Performance can be impacted by the physical separation of your Cloud Storage bucket and affected environment, particularly in cross-continental cases. Testing with a bucket located in the same region as your affected environment can identify the extent to which geographic separation is contributing to your latency.

    * If applicable, the affected environment's DNS resolver should use the [EDNS(0) protocol](https://datatracker.ietf.org/doc/html/rfc6891) so that requests from the environment are routed through an appropriate Google Front End.



### CLI or client library latency

**Issue** : I'm seeing increased latency when accessing Cloud Storage with the Google Cloud CLI or one of the [client libraries](https://docs.cloud.google.com/storage/docs/reference/libraries).

**Solution** : The gcloud CLI and the client libraries [automatically retry](https://docs.cloud.google.com/storage/docs/retry-strategy#tools) requests when it's useful to do so, and this behavior can effectively increase latency as seen from the end user. Use the Cloud Monitoring metric [`storage.googleapis.com/api/request_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#storage/api/request_count) to see if Cloud Storage is consistently serving a retryable response code, such as `429` or `5xx`.

## Proxy servers

**Issue** : I'm connecting through a proxy server. What do I need to do?

**Solution** : To access Cloud Storage through a proxy server, you must allow access to these domains:

  * `accounts.google.com` for creating OAuth2 authentication tokens
  * `oauth2.googleapis.com` for performing OAuth2 token exchanges
  * `*.googleapis.com` for storage requests



If your proxy server or security policy doesn't support allowlisting by domain and instead only supports allowlisting by IP network block, we strongly recommend that you configure your proxy server for all Google IP address ranges. You can find the address ranges by querying WHOIS data at [ARIN](http://whois.arin.net/rest/org/GOGL?showDetails=true). As a best practice, you should periodically review your proxy settings to ensure they match Google's IP addresses.

We don't recommend configuring your proxy with individual IP addresses you obtain from one-time lookups of `oauth2.googleapis.com` and `storage.googleapis.com`. Because Google services are exposed using DNS names that map to a large number of IP addresses that can change over time, configuring your proxy based on a one-time lookup may lead to failures to connect to Cloud Storage.

If your requests are being routed through a proxy server, you may need to check with your network administrator to ensure that the `Authorization` header containing your credentials is not stripped out by the proxy. Without the `Authorization` header, your requests are rejected and you receive a `MissingSecurityHeader` error.

## What's next

  * [Find answers to additional questions in the Cloud Storage FAQ](https://docs.cloud.google.com/storage/docs/faq).
  * [Learn about your support options](https://docs.cloud.google.com/support-hub).
  * Explore how [Error Reporting](https://docs.cloud.google.com/error-reporting) can help you identify and understand your Cloud Storage errors.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
