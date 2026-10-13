---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/
title: Google.Cloud.Storage.V1 \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:36.855048+00:00
---

# Google.Cloud.Storage.V1  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.Cloud.Storage.V1 Stay organized with collections  Save and categorize content based on your preferences. 

5.0.0 (latest)  4.16.0  4.15.0  4.14.0  4.13.0  4.11.0  4.10.0  4.9.0  4.8.0  4.7.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.7.0  3.6.0  3.5.0  3.4.0 

`Google.Cloud.Storage.V1` is a.NET client library for the [Google Cloud Storage API](https://cloud.google.com/storage/). It wraps the `Google.Apis.Storage.v1` generated library, providing a higher-level API to make it easier to use.

Note: This documentation is for version `5.0.0` of the library. Some samples may not work with other versions.

## Installation

Install the `Google.Cloud.Storage.V1` package from NuGet. Add it to your project in the normal way (for example by right-clicking on the project in Visual Studio and choosing "Manage NuGet Packages...").

## Authentication

When running on Google Cloud, no action needs to be taken to authenticate.

Otherwise, the simplest way of authenticating your API calls is to set up Application Default Credentials. The credentials will automatically be used to authenticate. See [Set up Application Default Credentials](https://cloud.google.com/docs/authentication/provide-credentials-adc) for more details.

## Getting started

Common operations are exposed via the [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient) class.

## Error responses

All errors reported by the underlying API (including precondition failures) are propagated as exceptions of type [`GoogleApiException`](https://cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.GoogleApiException). See the [Cloud Storage API status and error codes documentation](https://cloud.google.com/storage/docs/json_api/v1/status-codes) for details of the HTTP status codes used.

## Client life-cycle management

In many cases you don't need to worry about disposing of `StorageClient` objects, and can create them reasonably freely - but be aware that this _can_ causes issues with memory and network connection usage. We advise you to reuse a single client object if possible. `StorageClient` is thread-safe, so in most cases a single object is the simplest option.

If your architecture requires you to frequently create new client objects, please dispose of them to help with timely resource clean-up. See [the resource clean-up guide](https://cloud.google.com/dotnet/docs/reference/help/cleanup#rest-based-apis) for more details.

## Sample code
    
    
    var client = StorageClient.Create();
    
    // Create a bucket with a globally unique name
    var bucketName = Guid.NewGuid().ToString();
    var bucket = client.CreateBucket(projectId, bucketName);
    
    // Upload some files
    var content = Encoding.UTF8.GetBytes("hello, world");
    var obj1 = client.UploadObject(bucketName, "file1.txt", "text/plain", new MemoryStream(content));
    var obj2 = client.UploadObject(bucketName, "folder1/file2.txt", "text/plain", new MemoryStream(content));
    
    // List objects
    foreach (var obj in client.ListObjects(bucketName, ""))
    {
        Console.WriteLine(obj.Name);
    }
    
    // Download file
    using (var stream = File.OpenWrite("file1.txt"))
    {
        client.DownloadObject(bucketName, "file1.txt", stream);
    }
    

## Signed URLs

Signed URLs can be created to provide limited access to specific buckets and objects to anyone in possession of the URL, regardless of whether they have a Google account.

For example, Signed URLs can be created to provide read-only access to existing objects:
    
    
    // Create a signed URL which can be used to get a specific object for one hour.
    UrlSigner urlSigner = UrlSigner.FromCredential(credential);
    string url = await urlSigner.SignAsync(bucketName, objectName, TimeSpan.FromHours(1));
    
    // Get the content at the created URL.
    HttpResponseMessage response = await httpClient.GetAsync(url);
    string content = await response.Content.ReadAsStringAsync();
    

Or write-only access to put specific object content into a bucket:
    
    
    // Create a request template that will be used to create the signed URL.
    var destination = "places/world.txt";
    UrlSigner.RequestTemplate requestTemplate = UrlSigner.RequestTemplate
        .FromBucket(bucketName)
        .WithObjectName(destination)
        .WithHttpMethod(HttpMethod.Put)
        .WithContentHeaders(new Dictionary<string, IEnumerable<string>>
        {
            { "Content-Type", new[] { "text/plain" } }
        });
    // Create options specifying for how long the signer URL will be valid.
    UrlSigner.Options options = UrlSigner.Options.FromDuration(TimeSpan.FromHours(1));
    // Create a signed URL which allows the requester to PUT data with the text/plain content-type.
    UrlSigner urlSigner = UrlSigner.FromCredential(credential);
    string url = await urlSigner.SignAsync(requestTemplate, options);
    
    // Upload the content into the bucket using the signed URL.
    string source = "world.txt";
    
    ByteArrayContent content;
    using (FileStream stream = File.OpenRead(source))
    {
        byte[] data = new byte[stream.Length];
        stream.Read(data, 0, data.Length);
        content = new ByteArrayContent(data)
        {
            Headers = { ContentType = new MediaTypeHeaderValue("text/plain") }
        };
    }
    
    HttpResponseMessage response = await httpClient.PutAsync(url, content);
    

### Supported credential types for URL signing

`Google.Apis.Auth.OAuth2.ServiceAccountCredential`, `Google.Apis.Auth.OAuth2.ComputeCredential` and `Google.Apis.Auth.OAuth2.ImpersonatedCredential` are all supported credentials from which you can build a `UrlSigner` by calling the appropiate `UrlSigner.FromCredential` method overload. `Google.Apis.Auth.OAuth2.GoogleCredential` is also supported as long as the underlying credential is one of the supported specific types. The following example demonstrates how to explicitly use a Compute credential for URL signing.
    
    
    // Create a signed URL which can be used to get a specific object for one hour.
    var computeCredential = new ComputeCredential();
    UrlSigner urlSigner = UrlSigner.FromCredential(computeCredential);
    string url = await urlSigner.SignAsync(bucketName, objectName, TimeSpan.FromHours(1));
    
    // Get the content at the created URL.
    HttpResponseMessage response = await httpClient.GetAsync(url);
    string content = await response.Content.ReadAsStringAsync();
    

When using a `UrlSigner` it's worth being aware of the underlying synchronous/asynchronous nature of the signing operations depending on the credential type the signer was created from. If you used a service account credential, signing happens locally and the signing operation is synchronous. But if you use an impersonated credential or a Compute credential, then a request to the IAM API is made for signing and the operation is asynchronous. In this case, you can still use the synchronous versions of the signing methods but they will block until the asynchronous operation has completed, which could lead to deadlocks. In general, if you are unsure of which credential was used to create a given URL signer, it is safer to use the asynchronous signing methods.

### HMAC Signed URLs

If you have access to an HMAC key, you can also sign URLs, even if you don't have access to a service account private key. See the [HMAC Keys documentation](https://cloud.google.com/storage/docs/authentication/hmackeys) and the [Signing documentation](https://cloud.google.com/storage/docs/authentication/signatures#overview) for more details. Below you can find an example on how to create HMAC signed URLs using this library:
    
    
    // Create an HmacBlobSigner from an HMAC Key ID and Secret.
    UrlSigner.IBlobSigner blobSigner = UrlSigner.HmacBlobSigner.Create(hmacKeyId, hmacKeySecret);
    // Create a URL signer from the HmacBlobSigner.
    UrlSigner urlSigner = UrlSigner.FromBlobSigner(blobSigner);
    // Create an HMAC signed URL which can be used to get a specific object for one hour.
    string url = urlSigner.Sign(bucketName, objectName, TimeSpan.FromHours(1));
    
    // Get the content at the created URL.
    HttpResponseMessage response = await httpClient.GetAsync(url);
    string content = await response.Content.ReadAsStringAsync();
    

### Signing URLs with a custom blob signer

If you need to sign URLs but none of the supported signer options apply to your use case, you can create a `UrlSigner.IBlobSigner` implementation to perform the signing part. Use the `UrlSigner.FromBlobSigner(UrlSigner.IBlobSigner)` method to obtain a URL signer that uses your custom signer implementation.

### Specifying the signing version

(V4 signing is currently beta functionality.)

Google Cloud Storage supports two signing process versions: V2 and V4. Currently the default is V2, although in the future the library may be updated to use V4 by default.

To specify the URL signing versioning, use the [UrlSigner.Options.WithSigningVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.Options#Google_Cloud_Storage_V1_UrlSigner_Options_WithSigningVersion_Google_Cloud_Storage_V1_SigningVersion_) method, specifying the signing version you wish to use. This does not change the UrlSigner it is called on; it returns a new UrlSigner that uses the specified version.

Note that V4 signing is restricted to generating URLs that are valid for at most 7 days.
    
    
    // Create a signed URL which can be used to get a specific object for one hour,
    // using the V4 signing process.
    UrlSigner urlSigner = UrlSigner.FromCredential(credential);
    string url = await urlSigner.SignAsync(bucketName, objectName, TimeSpan.FromHours(1), signingVersion: SigningVersion.V4);
    
    // Get the content at the created URL.
    HttpResponseMessage response = await httpClient.GetAsync(url);
    string content = await response.Content.ReadAsStringAsync();
    

## Uploading objects by using HTML forms

In some cases, you might need to allow your users to upload objects via HTML forms. You can create signed POST policies that specify what is and is not allowed in such scenarios. You can read the [Policy Document](https://cloud.google.com/storage/docs/authentication/signatures#policy-document) documentation to get more information on how a POST policy document should be built. You can read the [POST object](https://cloud.google.com/storage/docs/xml-api/post-object) documentation to get more details on how the forms should be built.

Below you will find some samples on how to create a signed POST policy.

Simplest approach, where you restrict the upload to a specific bucket and a specific object name.
    
    
    // Create a signed post policy which can be used to upload a specific object and
    // expires in 1 hour after creation.
    UrlSigner urlSigner = UrlSigner.FromCredential(credential);
    UrlSigner.Options options = UrlSigner.Options
        .FromDuration(TimeSpan.FromHours(1))
        .WithSigningVersion(SigningVersion.V4)
        .WithScheme("https");
    UrlSigner.PostPolicy postPolicy = UrlSigner.PostPolicy.ForBucketAndKey(bucketName, objectName);
    postPolicy.SetCustomField(UrlSigner.PostPolicyCustomElement.GoogleMetadata, "x-goog-meta-test", "data");
    
    UrlSigner.SignedPostPolicy signedPostPolicy = await urlSigner.SignAsync(postPolicy, options);
    
    // Create an HTML form including all the fields in the signed post policy.
    StringBuilder form = new StringBuilder();
    form.AppendLine($"<form action=\"{signedPostPolicy.PostUrl}\" method=\"post\" enctype=\"multipart/form-data\">");
    foreach (var field in signedPostPolicy.Fields)
    {
        form.AppendLine($"<input type=\"hidden\" name=\"{field.Key}\" value=\"{field.Value}\">");
    }
    // Include the file element. It should always be the last element in the form.
    form.AppendLine("<input name=\"file\" type=\"file\">");
    form.AppendLine("<input type=\"submit\" value=\"Upload\">");
    form.AppendLine("</form>");
    
    // You can now save the form to file and serve it as static content
    // or send it as the response to a request made to your application.
    File.WriteAllText("PostPolicySimple.html", form.ToString());
    

Enforce how browser's cache will treat the uploaded object.
    
    
    // Create a signed post policy which can be used to upload a specific object with a
    // specific cache-control value and expires in 1 hour after creation.
    UrlSigner urlSigner = UrlSigner.FromCredential(credential);
    UrlSigner.Options options = UrlSigner.Options
        .FromDuration(TimeSpan.FromHours(1))
        .WithSigningVersion(SigningVersion.V4)
        .WithScheme("https");
    UrlSigner.PostPolicy postPolicy = UrlSigner.PostPolicy.ForBucketAndKey(bucketName, objectName);
    postPolicy.SetField(UrlSigner.PostPolicyStandardElement.Acl, "public-read");
    postPolicy.SetField(UrlSigner.PostPolicyStandardElement.CacheControl, "public,max-age=86400");
    
    UrlSigner.SignedPostPolicy signedPostPolicy = await urlSigner.SignAsync(postPolicy, options);
    
    // Create an HTML form including all the fields in the signed post policy.
    StringBuilder form = new StringBuilder();
    form.AppendLine($"<form action=\"{signedPostPolicy.PostUrl}\" method=\"post\" enctype=\"multipart/form-data\">");
    foreach (var field in signedPostPolicy.Fields)
    {
        form.AppendLine($"<input type=\"hidden\" name=\"{field.Key}\" value=\"{field.Value}\">");
    }
    // Include the file element. It should always be the last element in the form.
    form.AppendLine("<input name=\"file\" type=\"file\">");
    form.AppendLine("<input type=\"submit\" value=\"Upload\">");
    form.AppendLine("</form>");
    
    // You can now save the form to file and serve it as static content
    // or send it as the response to a request made to your application.
    File.WriteAllText("PostPolicyCacheControl.html", form.ToString());
    

You can also set starts-with conditions for some form elements. This means that the posting form should contain that element with a value that matches the condition.
    
    
    // Create a signed post policy which can be used to upload a specific object and
    // expires in 10 seconds after creation.
    // It also sets a starts-with condition on the acl form element, that should be met
    // by the actual form used for posting.
    UrlSigner urlSigner = UrlSigner.FromCredential(credential);
    UrlSigner.Options options = UrlSigner.Options
        .FromDuration(TimeSpan.FromHours(1))
        .WithSigningVersion(SigningVersion.V4)
        .WithScheme("https");
    UrlSigner.PostPolicy postPolicy = UrlSigner.PostPolicy.ForBucketAndKey(bucketName, objectName);
    postPolicy.SetStartsWith(UrlSigner.PostPolicyStandardElement.Acl, "public");
    
    UrlSigner.SignedPostPolicy signedPostPolicy = await urlSigner.SignAsync(postPolicy, options);
    
    // Create an HTML form including all the fields in the signed post policy.
    StringBuilder form = new StringBuilder();
    form.AppendLine($"<form action=\"{signedPostPolicy.PostUrl}\" method=\"post\" enctype=\"multipart/form-data\">");
    foreach (var field in signedPostPolicy.Fields)
    {
        form.AppendLine($"<input type=\"hidden\" name=\"{field.Key}\" value=\"{field.Value}\">");
    }
    // Include also an acl element with a value that meets the condition set in the policy.
    form.AppendLine("<input type=\"hidden\" name=\"acl\" value=\"public-read\">");
    // Include the file element. It should always be the last element in the form.
    form.AppendLine("<input name=\"file\" type=\"file\">");
    form.AppendLine("<input type=\"submit\" value=\"Upload\">");
    form.AppendLine("</form>");
    
    // You can now save the form to file and serve it as static content
    // or send it as the response to a request made to your application.
    File.WriteAllText("PostPolicyAcl.html", form.ToString());
    

Tell the server which HTTP status code you want it to return on succes.
    
    
    // Create a signed post policy which can be used to upload a specific object and
    // expires in 1 hour after creation.
    // It also sets a specific HTTP success satus code that should be returned.
    // Only 200, 201 and 204 are allowed.
    UrlSigner urlSigner = UrlSigner.FromCredential(credential);
    UrlSigner.Options options = UrlSigner.Options
        .FromDuration(TimeSpan.FromHours(1))
        .WithSigningVersion(SigningVersion.V4)
        .WithScheme("https");
    UrlSigner.PostPolicy postPolicy = UrlSigner.PostPolicy.ForBucketAndKey(bucketName, objectName);
    postPolicy.SetField(UrlSigner.PostPolicyStandardElement.SuccessActionStatus, HttpStatusCode.OK);
    
    UrlSigner.SignedPostPolicy signedPostPolicy = await urlSigner.SignAsync(postPolicy, options);
    
    // Create an HTML form including all the fields in the signed post policy.
    StringBuilder form = new StringBuilder();
    form.AppendLine($"<form action=\"{signedPostPolicy.PostUrl}\" method=\"post\" enctype=\"multipart/form-data\">");
    foreach (var field in signedPostPolicy.Fields)
    {
        form.AppendLine($"<input type=\"hidden\" name=\"{field.Key}\" value=\"{field.Value}\">");
    }
    // Include the file element. It should always be the last element in the form.
    form.AppendLine("<input name=\"file\" type=\"file\">");
    form.AppendLine("<input type=\"submit\" value=\"Upload\">");
    form.AppendLine("</form>");
    
    // You can now save the form to file and serve it as static content
    // or send it as the response to a request made to your application.
    File.WriteAllText("PostPolicySuccessStatus.html", form.ToString());
    

## Upload URIs

In some cases, it may not make sense for client applications to have permissions to begin an upload for an object, but an authenticated service may choose to grant this ability for individual uploads. Signed URLs are one option for this. Another option is for the service to start a resumable upload session, but instead of performing the upload, sending the resulting upload URI to the client application so it can perform the upload instead. Unlike sessions initiated with a signed URL, a pre-initated upload session will force the client application to upload through the region in which the session began, which will likely be close to the service, and not necessarily the client.
    
    
    var client = StorageClient.Create();
    var source = "world.txt";
    var destination = "places/world.txt";
    var contentType = "text/plain";
    
    // var acl = PredefinedAcl.PublicRead // public
    var acl = PredefinedObjectAcl.AuthenticatedRead; // private
    var options = new UploadObjectOptions { PredefinedAcl = acl };
    var uploadUri = await client.InitiateUploadSessionAsync(bucketName, destination, contentType, contentLength: null, options);
    
    // Send uploadUri to (unauthenticated) client application, so it can perform the upload:
    using (var stream = File.OpenRead(source))
    {
        // IUploadProgress defined in Google.Apis.Upload namespace
        IProgress<IUploadProgress> progress = new Progress<IUploadProgress>(
          p => Console.WriteLine($"bytes: {p.BytesSent}, status: {p.Status}")
        );
    
        var actualUploader = ResumableUpload.CreateFromUploadUri(uploadUri, stream);
        actualUploader.ProgressChanged += progress.Report;
        await actualUploader.UploadAsync();
    }
    

## Customer-supplied encryption keys

Storage objects are always stored encrypted, but if you wish to specify your own encryption key instead of using the server-supplied one, you can do so either for all operations with a particular `StorageClient` or on individual ones.
    
    
    // Use EncryptionKey.Create if you already have a key.
    EncryptionKey key = EncryptionKey.Generate();
    
    // This will affect all relevant object-based operations by default.
    var client = StorageClient.Create(encryptionKey: key);
    var content = Encoding.UTF8.GetBytes("hello, world");
    client.UploadObject(bucketName, "encrypted.txt", "text/plain", new MemoryStream(content));
    
    // When downloading, either use a client with the same key...
    client.DownloadObject(bucketName, "encrypted.txt", new MemoryStream());
    
    // Or specify a key just for that operation.
    var client2 = StorageClient.Create();
    client2.DownloadObject(bucketName, "encrypted.txt", new MemoryStream(),
        new DownloadObjectOptions { EncryptionKey = key });
    

## Change notification via Google Cloud Pub/Sub

You can configure a bucket to send a change notification to a [Google Cloud Pub/Sub](https://cloud.google.com/pubsub/) topic when changes occur. The sample below shows how to create a Pub/Sub topic, set its permissions so that the change notifications can be published to it, and then create the notification configuration on a bucket. You'll need to add a dependency on the `Google.Cloud.PubSub.V1` NuGet package to create the topic and manage its permissions.
    
    
    // First create a Pub/Sub topic.
    PublisherServiceApiClient publisherClient = PublisherServiceApiClient.Create();
    TopicName topicName = new TopicName(projectId, topicId);
    publisherClient.CreateTopic(topicName);
    
    // Prepare the topic for Storage notifications. The Storage Service Account must have Publish permission
    // for the topic. The code below adds the service account into the "roles/pubsub.publisher" role for the topic.
    
    // Determine the Storage Service Account name to use in IAM operations.
    StorageClient storageClient = StorageClient.Create();
    string storageServiceAccount = $"serviceAccount:{storageClient.GetStorageServiceAccountEmail(projectId)}";
    
    // Fetch the IAM policy for the topic.
    GetIamPolicyRequest getPolicyRequest = new GetIamPolicyRequest { ResourceAsResourceName = topicName };
    Iam.V1.Policy policy = publisherClient.IAMPolicyClient.GetIamPolicy(getPolicyRequest);
    var role = "roles/pubsub.publisher";
    
    // Ensure the Storage Service Account is in the publisher role, setting the IAM policy for the topic
    // on the server if necessary.
    if (policy.AddRoleMember(role, storageServiceAccount))
    {
        SetIamPolicyRequest setPolicyRequest = new SetIamPolicyRequest
        {
            ResourceAsResourceName = topicName,
            Policy = policy
        };
        publisherClient.IAMPolicyClient.SetIamPolicy(setPolicyRequest);
    }
    
    // Now that the topic is ready, we can create a notification configuration for Storage
    Notification notification = new Notification
    {
        Topic = $"//pubsub.googleapis.com/{topicName}",
        PayloadFormat = "JSON_API_V1"
    };
    notification = storageClient.CreateNotification(bucket, notification);
    Console.WriteLine($"Created notification ID: {notification.Id}");
    
    

## Connecting to an emulator

`StorageClient` supports the [Firebase Storage Emulator](https://firebase.google.com/docs/emulator-suite/connect_storage).

This is configured using `StorageClientBuilder.EmulatorDetection`, as described in the [client library help page on emulators](https://cloud.google.com/dotnet/docs/reference/help/emulators).

As well as setting the `EmulatorDetection` property when building a client, you must set the `STORAGE_EMULATOR_HOST` environment variable, in the form `host:port` (or `http://host:port`), e.g. `127.0.0.1:9199`. The port is the one shown in the emulator UI; note that this is _not_ the port of the Storage Emulator user interface.

Note that the Firebase Storage Emulator only supports a limited set of operations. See [the Storage Emulator documentation](https://firebase.google.com/docs/emulator-suite/connect_storage#differences_from_google_cloud_storage) for more details.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
