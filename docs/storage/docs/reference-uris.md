---
url: https://docs.cloud.google.com/storage/docs/reference-uris/
title: Request endpoints \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:56:08.269663+00:00
---

# Request endpoints  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/reference-uris/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Request endpoints Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the different request endpoints you can use to access Cloud Storage. Cloud Storage supports HTTP/1.1, HTTP/2, and HTTP/3 protocols. An endpoint is the location where Cloud Storage can be accessed, written as a URL.

**Note:** The Cloud Storage URLs described on this page are subject to change.

## Typical API requests

### JSON API

When making [JSON API requests](https://docs.cloud.google.com/storage/docs/json_api/v1) directly to Cloud Storage, use the following endpoints:

  * For general JSON API requests, excluding object uploads, use the following endpoint, replacing `PATH_TO_RESOURCE` with the appropriate value:
        
        https://storage.googleapis.com/storage/v1/PATH_TO_RESOURCE

  * For JSON API object uploads, use the following endpoint, replacing `BUCKET_NAME` with the appropriate value:
        
        https://storage.googleapis.com/upload/storage/v1/b/BUCKET_NAME/o

  * For [batched requests](https://docs.cloud.google.com/storage/docs/batch), use the following endpoint, replacing `PATH_TO_RESOURCE` with the appropriate value:
        
        https://storage.googleapis.com/batch/storage/v1/PATH_TO_RESOURCE

  * Optionally, for JSON API object downloads, you can use the following endpoint, replacing `BUCKET_NAME` and `OBJECT_NAME` with the appropriate values:
        
        https://storage.googleapis.com/download/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME?alt=media




JSON API endpoints only accept HTTPS requests.

**Note:** An `https://www.googleapis.com` endpoint is also supported for the JSON API and is returned in the `selfLink` metadata field for an object, but `https://storage.googleapis.com` is the preferred endpoint for better performance and availability. Similarly, an `https://content-storage.googleapis.com` endpoint is supported for downloads and is returned in the `mediaLink` metadata field for an object, but is also not recommended for use.

### XML API

**Important:** If you intend to serve content through a browser, note that the XML API serves content from the same origin as the request endpoint. If you need to serve content from a unique origin, consider using the JSON API or Authenticated browser downloads.

When making [XML API requests](https://docs.cloud.google.com/storage/docs/xml-api/reference-methods) directly to Cloud Storage, use the _virtual hosted-style_ or _path-style_ endpoint, replacing `BUCKET_NAME` and `OBJECT_NAME` with the appropriate values:

  * Virtual hosted-style endpoint: 
        
        https://BUCKET_NAME.storage.googleapis.com/OBJECT_NAME

  * Path-style endpoint: 
        
        https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME


**Note:** Virtual hosted-style endpoints cannot be used to access [domain-named buckets](https://docs.cloud.google.com/storage/docs/domain-name-verification). Use either path-style endpoints or a redirect instead.

XML API endpoints support secure sockets layer (SSL) encryption, which means you can use either HTTP or HTTPS. Using HTTPS is recommended, especially if you [authenticate](https://docs.cloud.google.com/storage/docs/authentication) to Cloud Storage using OAuth 2.0.

### gRPC

You can use [gRPC](https://docs.cloud.google.com/storage/docs/enable-grpc-api), a high performance, open source universal RPC framework developed by Google, to interact with Cloud Storage. gRPC clients connect to a service endpoint. For Google Cloud services like Cloud Storage, this is typically a DNS address on the `googleapis.com` domain (for example, `storage.googleapis.com`) and uses standard secure ports such as `443`. Using gRPC can provide improved performance and efficient streaming capabilities.

To use gRPC to interact with Cloud Storage, you need to enable it on [Cloud Client Libraries](https://docs.cloud.google.com/storage/docs/reference/libraries).

Enable gRPC on a client library using one of the following supported languages:

  * [C++ client library](https://docs.cloud.google.com/storage/docs/enable-grpc-api#grpc-cpp)

  * [Java client library](https://docs.cloud.google.com/storage/docs/enable-grpc-api#grpc-java)

  * [Go client library](https://docs.cloud.google.com/storage/docs/enable-grpc-api#grpc-go)




For connections through a proxy, see the [Troubleshooting topic](https://docs.cloud.google.com/storage/docs/troubleshooting#proxy-server) for recommended practices.

### Encoding URL path parts

In addition to general considerations for [bucket naming](https://docs.cloud.google.com/storage/docs/buckets#naming) and [object naming](https://docs.cloud.google.com/storage/docs/objects#naming), to ensure compatibility across Cloud Storage tools, you should encode the following characters when they appear in either the object name or query string of a request URL:

`!`, `#`, `$`, `&`, `'`, `(`, `)`, `*`, `+`, `,`, `/`, `:`, `;`, `=`, `?`, `@`, `[`, `]`, and space characters.

For example, if you send a [JSON API `GET` request](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) for the object named `foo??bar` in the bucket `example-bucket`, then your request URL should be:
    
    
    GET https://storage.googleapis.com/storage/v1/b/example-bucket/o/foo%3f%3fbar

Note that not all of the listed characters must be encoded in every scenario. Additionally, encoding is typically handled for you by client libraries, such as the [Cloud Storage Client Libraries](https://docs.cloud.google.com/storage/docs/reference/libraries), so you can pass the raw object name when using such tools.

For more information about using percent-encoding, see [Section 3.3 Path](https://datatracker.ietf.org/doc/html/rfc3986#section-3.3) in RFC 3986.

## Google Cloud console endpoints

When using the Google Cloud console, you access different resources using the following URLs:

Resource | URL  
---|---  
Bucket list for a project | `https://console.cloud.google.com/storage/browser?project=PROJECT_ID`  
Object list for a bucket | `https://console.cloud.google.com/storage/browser/BUCKET_NAME`  
Details for an object | `https://console.cloud.google.com/storage/browser/_details/BUCKET_NAME/OBJECT_NAME`  
Data for an object | See Authenticated browser downloads  
  
## gcloud endpoints

[`gcloud storage` commands](https://docs.cloud.google.com/sdk/gcloud/reference/storage) use JSON API endpoints. Endpoint usage is managed on your behalf by the gcloud CLI.

## Client library endpoints

Cloud Storage client libraries manage request endpoints automatically. Optionally, you can set the request endpoint manually. This can be useful when you want to use a specific endpoint, or for testing, such as when you want to use a local emulator:

### C++

For more information, see the [Cloud Storage C++ API reference documentation](https://docs.cloud.google.com/cpp/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    namespace g = ::google::cloud;
    namespace gcs = ::google::cloud::storage;
    [](std::string const& bucket_name, std::string const& object_name) {
      // NOTE: the CLOUD_STORAGE_EMULATOR_HOST environment variable overrides any
      //     value provided here.
      auto client = gcs::Client(g::Options{}.set<gcs::RestEndpointOption>(
          "https://storage.googleapis.com"));
      PerformSomeOperations(client, bucket_name, object_name);
    }

### C#

For more information, see the [Cloud Storage C# API reference documentation](https://cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    using [Google.Cloud.Storage.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.html);
    using System;
    
    public class SetClientEndpointSample
    {
        public [StorageClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClient.html) SetClientEndpoint(string endpoint) => new [StorageClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClientBuilder.html)
        {
            BaseUri = endpoint
        }.[Build](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.V1/latest/Google.Cloud.Storage.V1.StorageClientBuilder.html#Google_Cloud_Storage_V1_StorageClientBuilder_Build)();
    }
    

### Go

For more information, see the [Cloud Storage Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/storage). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/storage"
    	"google.golang.org/api/option"
    )
    
    // setClientEndpoint sets the request endpoint.
    func setClientEndpoint(w io.[Writer](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Writer), customEndpoint string, opts ...option.ClientOption) error {
    	// customEndpoint := "https://my-custom-endpoint.example.com/storage/v1/"
    	// opts := []option.ClientOption{}
    	ctx := context.Background()
    
    	// Add the custom endpoint option to any other desired options passed to storage.NewClient.
    	opts = append(opts, option.WithEndpoint(customEndpoint))
    	client, err := storage.NewClient(ctx, opts...)
    	if err != nil {
    		return fmt.Errorf("storage.NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// Use the client as per your custom endpoint, for example, attempt to get a bucket's metadata.
    	client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)("bucket-name").Attrs(ctx)
    	return nil
    }
    

### Java

For more information, see the [Cloud Storage Java API reference documentation](https://cloud.google.com/java/docs/reference/google-cloud-storage/latest/overview). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class SetClientEndpoint {
    
      public static void setClientEndpoint(String projectId, String endpoint) {
        // The ID of your GCP project
        // String projectId = "your-project-id";
    
        // The endpoint you wish to target
        // String endpoint = "https://storage.googleapis.com"
    
        [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage =
            [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId(projectId).setHost(endpoint).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    
        System.out.println(
            "Storage Client initialized with endpoint " + storage.getOptions().getHost());
      }
    }
    

### Node.js

For more information, see the [Cloud Storage Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // The custom endpoint to which requests should be made
    // const apiEndpoint = 'https://yourcustomendpoint.com';
    
    // Imports the Google Cloud client library
    const {Storage} = require('[@google-cloud/storage](https://docs.cloud.google.com/nodejs/docs/reference/storage/latest/overview.html)');
    
    // Creates a client
    const storage = new [Storage](https://docs.cloud.google.com/nodejs/docs/reference/storage-control/latest/storage-control/protos.google.storage.v2.storage-class.html)({
      apiEndpoint: apiEndpoint,
      useAuthWithCustomEndpoint: true,
    });
    
    console.log(`Client initiated with endpoint: ${storage.apiEndpoint}.`);
    

### PHP

For more information, see the [Cloud Storage PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/storage/storageclient). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    use Google\Cloud\Storage\StorageClient;
    
    /**
     * Sets a custom endpoint for storage client.
     *
     * @param string $projectId The ID of your Google Cloud Platform project.
     *        (e.g. 'my-project-id')
     * @param string $endpoint The endpoint for storage client to target.
     *        (e.g. 'https://storage.googleapis.com')
     */
    function set_client_endpoint(
        string $projectId,
        string $endpoint
    ): void {
        $storage = new StorageClient([
            'projectId' => $projectId,
            'apiEndpoint' => $endpoint,
        ]);
    
        // fetching apiEndpoint and baseUri from StorageClient is excluded for brevity
        # ...
        print('Storage Client initialized.' . PHP_EOL);
    }

### Python

For more information, see the [Cloud Storage Python API reference documentation](https://cloud.google.com/python/docs/reference/storage/latest). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    
    
    def set_client_endpoint(api_endpoint):
        """Initiates client with specified endpoint."""
        # api_endpoint = 'https://storage.googleapis.com'
    
        storage_client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(client_options={'api_endpoint': api_endpoint})
    
        print(f"client initiated with endpoint: {storage_client._connection.API_BASE_URL}")
    
        return storage_client
    
    

### Ruby

For more information, see the [Cloud Storage Ruby API reference documentation](https://googleapis.dev/ruby/google-cloud-storage/latest/Google/Cloud/Storage.html). 

To authenticate to Cloud Storage, set up Application Default Credentials. For more information, see [Set up authentication for client libraries](https://docs.cloud.google.com/storage/docs/authentication#client-libs). 
    
    
    # api_endpoint = "https://storage.googleapis.com"
    
    require "google/cloud/storage"
    
    storage = Google::Cloud::[Storage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control/latest/Google-Cloud-Storage.html).[new](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage/latest/Google-Cloud-Storage.html)(
      endpoint: api_endpoint
    )
    
    puts "Client initiated with endpoint #{storage.service.service.root_url}"

### Rust
    
    
    use google_cloud_storage::client::Storage;
    use google_cloud_storage::client::StorageControl;
    
    pub async fn sample(bucket_id: &str) -> anyhow::Result<()> {
        const NAME: &str = "hello-world.txt";
        let client = Storage::builder()
            .with_endpoint("https://www.googleapis.com")
            .build()
            .await?;
        // Use the `Storage` client as usual:
        let reader = client
            .read_object(format!("projects/_/buckets/{bucket_id}"), NAME)
            .send()
            .await?;
        println!("Object highlights: {:?}", reader.object());
    
        let control = StorageControl::builder()
            .with_endpoint("https://www.googleapis.com")
            .build()
            .await?;
        // Use the `StorageControl` client as usual:
        let bucket = control
            .get_bucket()
            .set_name(format!("projects/_/buckets/{bucket_id}"))
            .send()
            .await?;
        println!("Bucket {bucket_id} metadata is {bucket:?}");
    
        Ok(())
    }

## Custom domains

If you own your own domain, you can map its URIs to one or more Google Cloud services, including Cloud Storage buckets. The term _bucket-bound hostname_ is sometimes used to describe this Cloud Storage request endpoint. To connect a custom domain to a Cloud Storage bucket, you create either an `A` or `CNAME` redirect in your DNS record.

### `A` records

When connecting a custom domain to a Cloud Storage bucket, you generally should use an `A` record.

  * `A` records support `HTTPS` requests.
  * `A` records can be used to send traffic coming from a single hostname to multiple buckets as well as to other Google Cloud services.
  * `A` records do not place any restrictions on your bucket name.



The drawback to using `A` records is that they require additional setup and use of additional Google Cloud resources. See [Setting up your load balancer and SSL certificate](https://docs.cloud.google.com/storage/docs/hosting-static-website#lb-ssl) for a guide to using custom domains with `A` records.

### `CNAME` records

When connecting a custom domain to a Cloud Storage bucket, you can use a `CNAME` record, but note that doing so has certain limitations:

  * `CNAME` records only support `HTTP` requests.
  * `CNAME` records can only direct traffic from a given hostname to a single bucket.
  * `CNAME` records require the hostname and the associated bucket name to match, and you must [validate your bucket name](https://docs.cloud.google.com/storage/docs/domain-name-verification).
  * `CNAME` records can only be used for subdomains, such as `www.mydomain.com`, not top-level domains such as `mydomain.com`.



When using `CNAME` records, the hostname portion of your `CNAME` record must be set to the following:
    
    
    c.storage.googleapis.com.

For example, say your domain is `example.com`, and you want to make travel maps available to your customers. You can create a bucket in Cloud Storage called `travel-maps.example.com`, and then create a `CNAME` record in DNS that redirects requests from `travel-maps.example.com` to the Cloud Storage URI. To do this, you publish the following `CNAME` record in DNS:
    
    
    NAME                      TYPE     DATA
    travel-maps               CNAME    c.storage.googleapis.com.

By doing this, your customers can use the following URL to access a map of Paris:
    
    
    http://travel-maps.example.com/paris.jpg

Your domain registration service should have a way for you to administer your domain, including adding a `CNAME` resource record. For example, if you use Cloud DNS, instructions for adding resource records can be found on the [Add, modify, and delete records](https://docs.cloud.google.com/dns/docs/records) page.

## Authenticated browser downloads

Authenticated browser downloads use cookie-based authentication. Cookie-based authentication asks users to sign in to their user account to establish their identity. The specified account must have appropriate permission to download the object. For example, if you are using Identity and Access Management to control access to your objects, the user's account should have the `storage.objects.viewer` permission, which is [granted in the Storage Object Viewer role](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions#bucket-add).

To download an object using cookie-based authentication, use the following URL, replacing `BUCKET_NAME` and `OBJECT_NAME` with the appropriate values:
    
    
    https://storage.cloud.google.com/BUCKET_NAME/OBJECT_NAME

For example, if you shared an image `london.jpg` from your bucket `example-maps`, the URL would be:
    
    
    https://storage.cloud.google.com/example-maps/london.jpg

After successfully signing in, you are redirected to the requested content. The URL for this content has the format `https://ALPHANUMERIC_SEQUENCE-apidata.googleusercontent.com/download/storage/v1/b/BUCKET_NAME/o/OBJECT_NAME`.

Using HTTPS is required when performing authenticated browser downloads; attempts to use HTTP redirect to HTTPS.

### Access to public objects

All requests to the `storage.cloud.google.com` URI require authentication. This applies even when `allUsers` have permission to access an object. If you want users to download anonymously accessible objects without authenticating, use the XML API path-style endpoint:
    
    
    https://storage.googleapis.com/BUCKET_NAME/OBJECT_NAME

For details and examples, see [Accessing Public Data](https://docs.cloud.google.com/storage/docs/access-public-data).

## Mutual TLS support

[Mutual TLS (mTLS)](https://docs.cloud.google.com/chrome-enterprise-premium/docs/understand-mtls) is an industry standard protocol for mutual authentication between a client and a server. Cloud Storage supports the following mTLS endpoints: 

  * JSON API requests: `storage.mtls.googleapis.com`

  * XML API requests: `storage.mtls.googleapis.com`

  * Authenticated browser downloads: `storage.mtls.cloud.google.com`




## What's next

  * [Upload a file to Cloud Storage](https://docs.cloud.google.com/storage/docs/uploading-objects).
  * [Download a file from Cloud Storage](https://docs.cloud.google.com/storage/docs/downloading-objects).
  * [Host a static website](https://docs.cloud.google.com/storage/docs/hosting-static-website).
  * Learn about options to [control access to your data](https://docs.cloud.google.com/storage/docs/access-control).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
