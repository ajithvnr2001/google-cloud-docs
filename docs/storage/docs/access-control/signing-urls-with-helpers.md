---
url: https://docs.cloud.google.com/storage/docs/access-control/signing-urls-with-helpers/
title: V4 signing process with Cloud Storage tools \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:00:58.632896+00:00
---

# V4 signing process with Cloud Storage tools  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-control/signing-urls-with-helpers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  V4 signing process with Cloud Storage tools Stay organized with collections  Save and categorize content based on your preferences. 

V4 signing is a process you can use to generate signatures for authentication in Cloud Storage XML API requests. This page describes how to use the Google Cloud CLI and Cloud Storage client libraries to create signed URLs, using service account credentials. [Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) give time-limited read or write access to a specific Cloud Storage resource. If you want to make your own program for creating signed URLs, read [V4 signing with your own program](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-manually) instead.

Query string parameters included in a V4 signed URL are verified by the signature. If a request using the signed URL includes a query parameter that was not part of the signature, the request will fail. This lets you use parameters such as `response-content-disposition` to override object metadata for authenticated `GET` requests.

## Before you begin

Before performing the tasks in this page, complete the following steps:

  1. Enable the Service Account Credentials API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)

  2. [Create](https://docs.cloud.google.com/iam/docs/service-accounts-create) a [service account](https://docs.cloud.google.com/iam/docs/service-accounts). If you already have a service account that you want to use to sign URLs, you can skip this step.

  3. [Give the service account sufficient permission](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) such that it could perform the request that the signed URL will make. For example, if your signed URL will allow a user to read object data, the service account must itself have permission to read the object data.

For the tasks described in this guide, ask your administrator to grant one of the following IAM roles to the service account:

     * Storage Object User (`roles/storage.objectUser`): Use this role to create signed URLs for both uploading and downloading objects. This role is also required if the signed URL could overwrite an existing object.

     * Storage Object Viewer (`roles/storage.objectViewer`): Use this role if you only want to create signed URLs for downloading objects.

     * Storage Object Creator (`roles/storage.objectCreator`): Use this role if you only want to create signed URLs for uploading objects and the uploaded object won't overwrite an existing object in the bucket.

These [predefined roles](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) contain the permissions required to make signed URLs that download and upload objects. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

     * `storage.objects.get` (not required if you only want to upload objects)
     * `storage.objects.create` (not required if you only want to download objects)
     * `storage.objects.delete` (not required if you don't need to overwrite objects when uploading)

You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other predefined roles. To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

  4. Have sufficient permission to sign blobs with the service account. Ask your administrator to grant the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`).

     * If you use user credentials for authentication, you should be the principal assigned this role, and this role should be granted on the service account that will be used to create the signed URLs.

     * If you use a service account attached to a compute instance for authentication, the service account must be the principal for this role in order to impersonate itself, and this role should be granted on the project that contains the service account.

This [predefined role](https://docs.cloud.google.com/storage/docs/access-control/iam-roles) contain the permission required to sign blobs with a service account. To see the exact permission that is required, expand the **Required permissions** section:

#### Required permissions

     * `iam.serviceAccounts.signBlob`

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other predefined roles. To see which roles are associated with which permissions, refer to [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

For instructions on granting roles on projects, see [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




## Create a signed URL to download an object

To create a signed URL that can get an object from a bucket, complete the following steps:

### Command line

  1. Use the [`gcloud storage sign-url`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/sign-url) command. For example, the following command creates a signed URL that allows users to download an object for 10 minutes:
         
         gcloud storage sign-url gs://BUCKET_NAME/OBJECT_NAME --impersonate-service-account=SERVICE_ACCOUNT_EMAIL --duration=10m

Where:

     * `BUCKET_NAME` is the name of the bucket where the object is located. For example, `example-bucket`.

     * `OBJECT_NAME` is the name of the object to download. For example, `cat.jpeg`.

     * `SERVICE_ACCOUNT_EMAIL` is the email address of a [service account](https://docs.cloud.google.com/iam/docs/service-accounts) whose key will do the signing. For example, `signed-url-account@my-project.iam.gserviceaccount.com`.

If successful, your response should look like:
    
    ---
    expiration: '2023-07-14 23:19:35'
    http_verb: GET
    resource: gs://example-bucket/cat.jpeg
    signed_url: https://storage.googleapis.com/example-bucket/cat.jpeg?
    x-goog-signature=11ae9c61ca84dd0bec319f7d52a38029e5873caa2eeced0568
    ef96076258cfc1a925a9683cc907d210036b61af9e06a13bf4a15b15fab3916669b
    e2f4c9f66ea6be822bec5858af519a6da705415b5768721197be213103fa09b8a18
    8a143be77a24351517ff208a2c62cfebb78040daf1f953907080bd98f9462739d11
    1355b1d9bcf54705b862f37392c031fde0d52add1a4d3bbb98a22e8b7023f6a1623
    2e0a2dd56e524d410624d28663e557fafaf4ba0a04290a1066f894713857b429258
    d14f056066c7622baf114c124e645688e19b4df3c4a7925f580693c93fa9c1dae7f
    dff0edff7259c72f3f0eadc5a9f9f556c83c9c8dc02ee3af8d20ab634bad&x-goog
    -algorithm=GOOG4-RSA-SHA256&x-goog-credential=signed-url-account%40
    my-project.iam.gserviceaccount.com%2F20230714%2Fus%2Fstorage%2Fgoog
    4_request&x-goog-date=20230714T221935Z&x-goog-expires=600&x-goog-si
    gnedheaders=host

This URL can be used by any person to access the associated resource (in this case `cat.jpeg`) for the designated length of time (in this case, 10 minutes).




### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name, std::string const& signing_account) {
      StatusOr<std::string> signed_url = client.CreateV4SignedUrl(
          "GET", bucket_name, object_name,
          gcs::SignedUrlDuration(std::chrono::minutes(15)),
          gcs::SigningAccount(signing_account));
    
      if (!signed_url) throw std::move(signed_url).status();
      std::cout << "The signed url is: " << *signed_url << "\n\n"
                << "You can use this URL with any user agent, for example:\n"
                << "curl '" << *signed_url << "'\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Net.Http;
    
    public class GenerateV4SignedReadUrlSample
    {
        public string GenerateV4SignedReadUrl(
            string bucketName = "your-unique-bucket-name",
            string objectName = "your-object-name")
        {
            [UrlSigner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.html) urlSigner = [UrlSigner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.html).[FromCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.html#Google_Cloud_Storage_V1_UrlSigner_FromCredential_Google_Apis_Auth_OAuth2_ComputeCredential_)([GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)());
            // V4 is the default signing version.
            string url = urlSigner.[Sign](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.html#Google_Cloud_Storage_V1_UrlSigner_Sign_Google_Cloud_Storage_V1_UrlSigner_PostPolicy_Google_Cloud_Storage_V1_UrlSigner_Options_)(bucketName, objectName, TimeSpan.FromHours(1), [HttpMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.RequestTemplate.html#Google_Cloud_Storage_V1_UrlSigner_RequestTemplate_HttpMethod).Get);
            Console.WriteLine("Generated GET signed URL:");
            Console.WriteLine(url);
            Console.WriteLine("You can use this URL with any user agent, for example:");
            Console.WriteLine($"curl '{url}'");
            return url;
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
    
    // generateV4GetObjectSignedURL generates object signed URL with GET method.
    func generateV4GetObjectSignedURL(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) (string, error) {
    	// bucket := "bucket-name"
    	// object := "object-name"
    
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return "", fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// Signing a URL requires credentials authorized to sign a URL. You can pass
    	// these in through SignedURLOptions with one of the following options:
    	//    a. a Google service account private key, obtainable from the Google Developers Console
    	//    b. a Google Access ID with iam.serviceAccounts.signBlob permissions
    	//    c. a SignBytes function implementing custom signing.
    	// In this example, none of these options are used, which means the SignedURL
    	// function attempts to use the same authentication that was used to instantiate
    	// the Storage client. This authentication must include a private key or have
    	// iam.serviceAccounts.signBlob permissions.
    	opts := &storage.[SignedURLOptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_SignedURLOptions){
    		Scheme:  storage.[SigningSchemeV4](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_SigningSchemeDefault_SigningSchemeV2_SigningSchemeV4),
    		Method:  "GET",
    		Expires: time.Now().[Add](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_MultiRangeDownloader_Add)(15 * time.Minute),
    	}
    
    	u, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).SignedURL(object, opts)
    	if err != nil {
    		return "", fmt.Errorf("Bucket(%q).SignedURL: %w", bucket, err)
    	}
    
    	fmt.Fprintln(w, "Generated GET signed URL:")
    	fmt.Fprintf(w, "%q\n", u)
    	fmt.Fprintln(w, "You can use this URL with any user agent, for example:")
    	fmt.Fprintf(w, "curl %q\n", u)
    	return u, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.net.URL;
    import java.util.concurrent.TimeUnit;
    
    public class GenerateV4GetObjectSignedUrl {
      /**
       * Signing a URL requires Credentials which implement ServiceAccountSigner. These can be set
       * explicitly using the Storage.SignUrlOption.signWith(ServiceAccountSigner) option. If you don't,
       * you could also pass a service account signer to StorageOptions, i.e.
       * StorageOptions().newBuilder().setCredentials(ServiceAccountSignerCredentials). In this example,
       * neither of these options are used, which means the following code only works when the
       * credentials are defined via the environment variable GOOGLE_APPLICATION_CREDENTIALS, and those
       * credentials are authorized to sign a URL. See the documentation for Storage.signUrl for more
       * details.
       */
      public static void generateV4GetObjectSignedUrl(
          String projectId, String bucketName, String objectName) throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // String projectId = "my-project-id";
        // String bucketName = "my-bucket";
        // String objectName = "my-object";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // Define resource
        [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfo = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder([BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName)).build();
    
        URL url =
            storage.[signUrl](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_signUrl_com_google_cloud_storage_BlobInfo_long_java_util_concurrent_TimeUnit_com_google_cloud_storage_Storage_SignUrlOption____)(blobInfo, 15, TimeUnit.MINUTES, Storage.SignUrlOption.withV4Signature());
    
        System.out.println("Generated GET signed URL:");
        System.out.println(url);
        System.out.println("You can use this URL with any user agent, for example:");
        System.out.println("curl '" + url + "'");
      }
    }

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     * Note: when creating a signed URL, unless running in a GCP environment,
     * a service account must be used for authorization.
     */
    // The ID of your GCS bucket
    // const bucketName = 'your-unique-bucket-name';
    
    // The full path of your file inside the GCS bucket, e.g. 'yourFile.jpg' or 'folder1/folder2/yourFile.jpg'
    // const fileName = 'your-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function generateV4ReadSignedUrl() {
      // These options will allow temporary read access to the file
      const options = {
        version: 'v4',
        action: 'read',
        expires: Date.now() + 15 * 60 * 1000, // 15 minutes
      };
    
      // Get a v4 signed URL for reading the file
      const [url] = await storage
        .bucket(bucketName)
        .file(fileName)
        .getSignedUrl(options);
    
      console.log('Generated GET signed URL:');
      console.log(url);
      console.log('You can use this URL with any user agent, for example:');
      console.log(`curl '${url}'`);
    }
    
    generateV4ReadSignedUrl().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Generate a v4 signed URL for downloading an object.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     */
    function get_object_v4_signed_url(string $bucketName, string $objectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $url = $object->signedUrl(
            # This URL is valid for 15 minutes
            new \DateTime('15 min'),
            [
                'version' => 'v4',
            ]
        );
    
        print('Generated GET signed URL:' . PHP_EOL);
        print($url . PHP_EOL);
        print('You can use this URL with any user agent, for example:' . PHP_EOL);
        print('curl ' . $url . PHP_EOL);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import datetime
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def generate_download_signed_url_v4(bucket_name, blob_name):
        """Generates a v4 signed URL for downloading a blob.
    
        Note that this method requires a service account key file.
        """
        # bucket_name = 'your-bucket-name'
        # blob_name = 'your-object-name'
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(blob_name)
    
        url = blob.generate_signed_url(
            version="v4",
            # This URL is valid for 15 minutes
            expiration=datetime.timedelta(minutes=15),
            # Allow GET requests using this URL.
            method="GET",
        )
    
        print("Generated GET signed URL:")
        print(url)
        print("You can use this URL with any user agent, for example:")
        print(f"curl '{url}'")
        return url
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def generate_signed_url_v4 bucket_name:, file_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      storage_expiry_time = 5 * 60 # 5 minutes
    
      url = storage.signed_url bucket_name, file_name, method: "GET",
                               expires: storage_expiry_time, version: :v4
    
      puts "Generated GET signed url:"
      puts url
      puts "You can use this URL with any user agent, for example:"
      puts "curl #{url}"
    end

### Rust
    
    
    use google_cloud_storage::builder::storage::SignedUrlBuilder;
    use google_cloud_storage::http::Method;
    use std::time::Duration;
    
    pub async fn sample(bucket_name: &str, object_name: &str) -> anyhow::Result<()> {
        let signer = google_cloud_auth::credentials::Builder::default().build_signer()?;
    
        let signed_url =
            SignedUrlBuilder::for_object(format!("projects/_/buckets/{bucket_name}"), object_name)
                .with_method(Method::GET)
                .with_expiration(Duration::from_secs(15 * 60)) // 15 minutes
                .sign_with(&signer)
                .await?;
    
        println!("Generated GET signed URL:");
        println!("{signed_url}");
        println!("You can use this URL with any user agent, for example:");
        println!("curl '{signed_url}'",);
    
        Ok(())
    }

## Create a signed URL to upload an object

To create a signed URL that can upload an object to a bucket, complete the following steps:

### Command line

  1. Use the [`gcloud storage sign-url`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/sign-url) command. For example, the following command creates a signed URL that allows users to upload a file for one hour:
         
         gcloud storage sign-url gs://BUCKET_NAME/OBJECT_NAME --impersonate-service-account=SERVICE_ACCOUNT_EMAIL --http-verb=PUT --duration=1h --headers=content-type=CONTENT_TYPE

     * `BUCKET_NAME` is the name of the bucket where the object is being uploaded. For example, `example-bucket`.

     * `OBJECT_NAME` is the name to assign to the uploaded object. For example, `cat.png`.

     * `SERVICE_ACCOUNT_EMAIL` is the email address of a [service account](https://docs.cloud.google.com/iam/docs/service-accounts) whose key will do the signing. For example, `signed-url-account@my-project.iam.gserviceaccount.com`.

     * `CONTENT_TYPE` is the uploaded object's content type. For example, `image/png`.

If successful, your response should look like:
    
    ---
    expiration: '2023-07-14 23:35:47'
    http_verb: PUT
    resource: gs://example-bucket/cat.png
    signed_url: https://storage.googleapis.com/example-bucket/cat.png?
    x-goog-signature=2f670a686102963e0574f3c1a3b4d29ee4aa406c1528d42d2
    30195d17fef73834b254314de7d7990afd48538a84b66f20010e7ecd90a900490e
    6119b7e56a912f71c8d64285c40e86f31b8fec51cf8c7a61ded81de3cedac9c1ca
    b92474b7371740fdac20b2d8d092b15396f79443bbde954a4174ed11aef6c2cf5f
    a4d72a84ff60fd6003ed0a505b0e40b6207ddbaec2a15778f715c3ec7537a1b14f
    b6661b2abaa5736f1670a412ca7e2555c830591f0595c01ff95af7f2206abe2e27
    41948c16d4bd4c7cbb25f41277ece59236c06e00ca6c63ae2eb3efc22c216bb24c
    e1b8b3801d07fd3a7ed3f2df3db6e59c6fc3cc76a002335dd936efd0237cf584e3
    6&x-goog-algorithm=GOOG4-RSA-SHA256&x-goog-credential=signed-url-a
    ccount%40my-project.iam.gserviceaccount.com%2F20230714%2Fus%2Fstor
    age%2Fgoog4_request&x-goog-date=20230714T223547Z&x-goog-expires=36
    00&x-goog-signedheaders=content-type%3Bhost

This URL can be used by any person to upload a resource (in this case `cat.png`) to the specified Cloud Storage bucket for the designated length of time (in this case, 1 hour).




### Client libraries

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace gcs = ::google::cloud::storage;
    using ::google::cloud::StatusOr;
    [](gcs::Client client, std::string const& bucket_name,
       std::string const& object_name, std::string const& signing_account) {
      StatusOr<std::string> signed_url = client.CreateV4SignedUrl(
          "PUT", bucket_name, object_name,
          gcs::SignedUrlDuration(std::chrono::minutes(15)),
          gcs::AddExtensionHeader("content-type", "application/octet-stream"),
          gcs::SigningAccount(signing_account));
    
      if (!signed_url) throw std::move(signed_url).status();
      std::cout << "The signed url is: " << *signed_url << "\n\n"
                << "You can use this URL with any user agent, for example:\n"
                << "curl -X PUT -H 'Content-Type: application/octet-stream'"
                << " --upload-file my-file '" << *signed_url << "'\n";
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    using System.Collections.Generic;
    using System.Net.Http;
    
    public class GenerateV4UploadSignedUrlSample
    {
        public string GenerateV4UploadSignedUrl(
            string bucketName = "your-unique-bucket-name",
            string objectName = "your-object-name")
        {
            [UrlSigner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.html) urlSigner = [UrlSigner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.html).[FromCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.html#Google_Cloud_Storage_V1_UrlSigner_FromCredential_Google_Apis_Auth_OAuth2_ComputeCredential_)([GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)());
    
            var contentHeaders = new Dictionary<string, IEnumerable<string>>
            {
                { "Content-Type", new[] { "text/plain" } }
            };
    
            // V4 is the default signing version.
            UrlSigner.Options options = [UrlSigner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.html).[Options](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.Options.html).[FromDuration](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.Options.html#Google_Cloud_Storage_V1_UrlSigner_Options_FromDuration_System_TimeSpan_)(TimeSpan.FromHours(1));
    
            UrlSigner.RequestTemplate template = [UrlSigner](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.html).[RequestTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.RequestTemplate.html)
                .[FromBucket](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.RequestTemplate.html#Google_Cloud_Storage_V1_UrlSigner_RequestTemplate_FromBucket_System_String_)(bucketName)
                .[WithObjectName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.RequestTemplate.html#Google_Cloud_Storage_V1_UrlSigner_RequestTemplate_WithObjectName_System_String_)(objectName)
                .[WithHttpMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.RequestTemplate.html#Google_Cloud_Storage_V1_UrlSigner_RequestTemplate_WithHttpMethod_System_Net_Http_HttpMethod_)([HttpMethod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.RequestTemplate.html#Google_Cloud_Storage_V1_UrlSigner_RequestTemplate_HttpMethod).Put)
                .[WithContentHeaders](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.RequestTemplate.html#Google_Cloud_Storage_V1_UrlSigner_RequestTemplate_WithContentHeaders_System_Collections_Generic_IEnumerable_System_Collections_Generic_KeyValuePair_System_String_System_Collections_Generic_IEnumerable_System_String____)(contentHeaders);
    
            string url = urlSigner.[Sign](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.UrlSigner.html#Google_Cloud_Storage_V1_UrlSigner_Sign_Google_Cloud_Storage_V1_UrlSigner_PostPolicy_Google_Cloud_Storage_V1_UrlSigner_Options_)(template, options);
            Console.WriteLine("Generated PUT signed URL:");
            Console.WriteLine(url);
            Console.WriteLine("You can use this URL with any user agent, for example:");
            Console.WriteLine($"curl -X PUT -H 'Content-Type: text/plain' --upload-file my-file '{url}'");
            return url;
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
    
    // generateV4PutObjectSignedURL generates object signed URL with PUT method.
    func generateV4PutObjectSignedURL(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), bucket, object string) (string, error) {
    	// bucket := "bucket-name"
    	// object := "object-name"
    
    	ctx := context.Background()
    	client, err := storage.NewClient(ctx)
    	if err != nil {
    		return "", fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// Signing a URL requires credentials authorized to sign a URL. You can pass
    	// these in through SignedURLOptions with one of the following options:
    	//    a. a Google service account private key, obtainable from the Google Developers Console
    	//    b. a Google Access ID with iam.serviceAccounts.signBlob permissions
    	//    c. a SignBytes function implementing custom signing.
    	// In this example, none of these options are used, which means the SignedURL
    	// function attempts to use the same authentication that was used to instantiate
    	// the Storage client. This authentication must include a private key or have
    	// iam.serviceAccounts.signBlob permissions.
    	opts := &storage.[SignedURLOptions](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_SignedURLOptions){
    		Scheme: storage.[SigningSchemeV4](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_SigningSchemeDefault_SigningSchemeV2_SigningSchemeV4),
    		Method: "PUT",
    		Headers: []string{
    			"Content-Type:application/octet-stream",
    		},
    		Expires: time.Now().[Add](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_MultiRangeDownloader_Add)(15 * time.Minute),
    	}
    
    	u, err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucket).SignedURL(object, opts)
    	if err != nil {
    		return "", fmt.Errorf("Bucket(%q).SignedURL: %w", bucket, err)
    	}
    
    	fmt.Fprintln(w, "Generated PUT signed URL:")
    	fmt.Fprintf(w, "%q\n", u)
    	fmt.Fprintln(w, "You can use this URL with any user agent, for example:")
    	fmt.Fprintf(w, "curl -X PUT -H 'Content-Type: application/octet-stream' --upload-file my-file %q\n", u)
    	return u, nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html);
    import com.google.cloud.storage.[BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html);
    import com.google.cloud.storage.[HttpMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.HttpMethod.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    import java.net.URL;
    import java.util.HashMap;
    import java.util.Map;
    import java.util.concurrent.TimeUnit;
    
    public class GenerateV4PutObjectSignedUrl {
      /**
       * Signing a URL requires Credentials which implement ServiceAccountSigner. These can be set
       * explicitly using the Storage.SignUrlOption.signWith(ServiceAccountSigner) option. If you don't,
       * you could also pass a service account signer to StorageOptions, i.e.
       * StorageOptions().newBuilder().setCredentials(ServiceAccountSignerCredentials). In this example,
       * neither of these options are used, which means the following code only works when the
       * credentials are defined via the environment variable GOOGLE_APPLICATION_CREDENTIALS, and those
       * credentials are authorized to sign a URL. See the documentation for Storage.signUrl for more
       * details.
       */
      public static void generateV4PutObjectSignedUrl(
          String projectId, String bucketName, String objectName) throws [StorageException](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageException.html) {
        // String projectId = "my-project-id";
        // String bucketName = "my-bucket";
        // String objectName = "my-object";
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        // Define Resource
        [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html) blobInfo = [BlobInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobInfo.html).newBuilder([BlobId](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BlobId.html).of(bucketName, objectName)).build();
    
        // Generate Signed URL
        Map<String, String> extensionHeaders = new HashMap<>();
        extensionHeaders.put("Content-Type", "application/octet-stream");
    
        URL url =
            storage.[signUrl](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html#com_google_cloud_storage_Storage_signUrl_com_google_cloud_storage_BlobInfo_long_java_util_concurrent_TimeUnit_com_google_cloud_storage_Storage_SignUrlOption____)(
                blobInfo,
                15,
                TimeUnit.MINUTES,
                Storage.SignUrlOption.httpMethod(HttpMethod.PUT),
                Storage.SignUrlOption.withExtHeaders(extensionHeaders),
                Storage.SignUrlOption.withV4Signature());
    
        System.out.println("Generated PUT signed URL:");
        System.out.println(url);
        System.out.println("You can use this URL with any user agent, for example:");
        System.out.println(
            "curl -X PUT -H 'Content-Type: application/octet-stream' --upload-file my-file '"
                + url
                + "'");
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
    
    // The full path of your file inside the GCS bucket, e.g. 'yourFile.jpg' or 'folder1/folder2/yourFile.jpg'
    // const fileName = 'your-file-name';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)();
    
    async function generateV4UploadSignedUrl() {
      // These options will allow temporary uploading of the file with outgoing
      // Content-Type: application/octet-stream header.
      const options = {
        version: 'v4',
        action: 'write',
        expires: Date.now() + 15 * 60 * 1000, // 15 minutes
        contentType: 'application/octet-stream',
      };
    
      // Get a v4 signed URL for uploading file
      const [url] = await storage
        .bucket(bucketName)
        .file(fileName)
        .getSignedUrl(options);
    
      console.log('Generated PUT signed URL:');
      console.log(url);
      console.log('You can use this URL with any user agent, for example:');
      console.log(
        "curl -X PUT -H 'Content-Type: application/octet-stream' " +
          `--upload-file my-file '${url}'`
      );
    }
    
    generateV4UploadSignedUrl().catch(console.error);

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Generate a v4 signed URL for uploading an object.
     *
     * @param string $bucketName The name of your Cloud Storage bucket.
     *        (e.g. 'my-bucket')
     * @param string $objectName The name of your Cloud Storage object.
     *        (e.g. 'my-object')
     */
    function upload_object_v4_signed_url(string $bucketName, string $objectName): void
    {
        $storage = new StorageClient();
        $bucket = $storage->bucket($bucketName);
        $object = $bucket->object($objectName);
        $url = $object->signedUrl(
            # This URL is valid for 15 minutes
            new \DateTime('15 min'),
            [
                'method' => 'PUT',
                'contentType' => 'application/octet-stream',
                'version' => 'v4',
            ]
        );
    
        print('Generated PUT signed URL:' . PHP_EOL);
        print($url . PHP_EOL);
        print('You can use this URL with any user agent, for example:' . PHP_EOL);
        print("curl -X PUT -H 'Content-Type: application/octet-stream' " .
            '--upload-file my-file ' . $url . PHP_EOL);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import datetime
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def generate_upload_signed_url_v4(bucket_name, blob_name):
        """Generates a v4 signed URL for uploading a blob using HTTP PUT.
    
        Note that this method requires a service account key file.
        """
        # bucket_name = 'your-bucket-name'
        # blob_name = 'your-object-name'
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)()
        bucket = storage_client.[bucket](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html#google_cloud_storage_client_Client_bucket)(bucket_name)
        blob = bucket.blob(blob_name)
    
        url = blob.generate_signed_url(
            version="v4",
            # This URL is valid for 15 minutes
            expiration=datetime.timedelta(minutes=15),
            # Allow PUT requests using this URL.
            method="PUT",
            content_type="application/octet-stream",
        )
    
        print("Generated PUT signed URL:")
        print(url)
        print("You can use this URL with any user agent, for example:")
        print(
            "curl -X PUT -H 'Content-Type: application/octet-stream' "
            "--upload-file my-file '{}'".format(url)
        )
        return url
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    def generate_upload_signed_url_v4 bucket_name:, file_name:
      # The ID of your GCS bucket
      # bucket_name = "your-unique-bucket-name"
    
      # The ID of your GCS object
      # file_name = "your-file-name"
    
      require "google/cloud/storage"
    
      storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)
      storage_expiry_time = 5 * 60 # 5 minutes
    
      url = storage.signed_url bucket_name, file_name, method: "PUT",
                               expires: storage_expiry_time, version: :v4,
                               headers: { "Content-Type" => "text/plain" }
      puts "Generated PUT signed URL:"
      puts url
      puts "You can use this URL with any user agent, for example:"
      puts "curl -X PUT -H 'Content-Type: text/plain' --upload-file my-file '#{url}'"
    end

### Rust
    
    
    use google_cloud_storage::builder::storage::SignedUrlBuilder;
    use google_cloud_storage::http::Method;
    use std::time::Duration;
    
    pub async fn sample(bucket_name: &str, object_name: &str) -> anyhow::Result<()> {
        let signer = google_cloud_auth::credentials::Builder::default().build_signer()?;
    
        let signed_url =
            SignedUrlBuilder::for_object(format!("projects/_/buckets/{bucket_name}"), object_name)
                .with_method(Method::PUT)
                .with_expiration(Duration::from_secs(15 * 60)) // 15 minutes
                .with_header("content-type", "application/octet-stream")
                .sign_with(&signer)
                .await?;
    
        println!("Generated PUT signed URL:");
        println!("{signed_url}");
        println!("You can use this URL with any user agent, for example:");
        println!(
            "curl -X PUT -H 'Content-Type: application/octet-stream' --upload-file my-file '{signed_url}'",
        );
    
        Ok(())
    }

## Limitations

HMAC credentials aren't supported when using Cloud Storage tools to generate signed URLs.

## What's next

  * [Learn how to sign URLs with your own program](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-manually).
  * [Learn more about signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls).
  * [Learn about uploading an object with the XML API](https://docs.cloud.google.com/storage/docs/xml-api/put-object-upload).
  * [Learn about uploading objects](https://docs.cloud.google.com/storage/docs/uploading-objects).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
