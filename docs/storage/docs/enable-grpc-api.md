---
url: https://docs.cloud.google.com/storage/docs/enable-grpc-api/
title: Connect to Cloud Storage using gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:32.872288+00:00
---

# Connect to Cloud Storage using gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/enable-grpc-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Connect to Cloud Storage using gRPC Stay organized with collections  Save and categorize content based on your preferences. 

You can connect to Cloud Storage by using [gRPC](https://grpc.io/), a high-performance, open source universal RPC framework developed by Google that uses Protocol Buffers to define services. gRPC uses [direct connectivity](https://docs.cloud.google.com/storage/docs/direct-connectivity) between [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances) and Cloud Storage buckets, which bypasses [Google Front Ends](https://docs.cloud.google.com/docs/security/infrastructure/design#google-frontend-service) (GFEs) to reduce latency. For analytics workloads on Google Cloud, gRPC improves Cloud Storage read performance only when the Compute Engine instance and the Cloud Storage bucket are in the same region.

## Supported clients

You can connect to Cloud Storage using gRPC through the following supported clients:

  * [Cloud Storage connector on Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage#connect-to-cloud-storage-using-grpc).

  * [Apache Beam I/O connector on Dataflow](https://beam.apache.org/documentation/io/connectors/) for [read](https://docs.cloud.google.com/dataflow/docs/guides/read-from-cloud-storage#enable-connector-grpc) and [write](https://docs.cloud.google.com/dataflow/docs/guides/write-to-cloud-storage#enable-connector-grpc) requests.

  * Cloud Storage C++, Go, and Java client libraries. For instructions on enabling gRPC for these client libraries, see Enable gRPC on client library.

  * [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview). You can use Cloud Storage FUSE as a client by specifying `grpc` in the [`client-protocol` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#client-protocol) using a Cloud Storage FUSE configuration file or the [`--client-protocol` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#client-protocol) using the Cloud Storage FUSE CLI. To use gRPC with Cloud Storage FUSE, we recommend using [Cloud Storage FUSE versions 2.10.0](https://github.com/GoogleCloudPlatform/gcsfuse/releases/tag/v2.10.0) or later.




## Enable gRPC on a client library

### C++

### Before you begin

  1. Ensure you have the following versions installed:

     * gRPC version 1.65.1 or later

     * C++ client library version v2.30.0 or later

     * C++ version 14 or later

For installation instructions, see [Setting up a C++ development environment](https://docs.cloud.google.com/cpp/docs/setup).

  2. [Set up authentication](https://docs.cloud.google.com/storage/docs/reference/libraries#authentication).

  3. Ensure each Compute Engine instance has a [service account](https://docs.cloud.google.com/compute/docs/instances/change-service-account) attached to it, even if the service account has no permissions. This service account is used to represent the Compute Engine instance in the [Application Layer Transport Security (ALTS)](https://docs.cloud.google.com/security/encryption-in-transit/application-layer-transport-security) handshake process and is required for [direct connectivity](https://docs.cloud.google.com/storage/docs/direct-connectivity).




### Configure the C++ client library

  1. Create a gRPC client using `gcs::MakeGrpcClient()`:
         
         namespace gcs = google::cloud::storage;
           void App() {
            auto client = gcs::MakeGrpcClient();
         
           // application code
         
           }
         

The C++ client library automatically uses [direct connectivity](https://docs.cloud.google.com/storage/docs/direct-connectivity) when it detects that the application is running on Google Cloud.

  2. To configure the C++ client library to use gRPC, enable the Cloud Storage gRPC client to update your build system configuration for CMake or Bazel.

### CMake

     1. Enable the Cloud Storage gRPC client plugin at compile-time.
            
            cmake -DGOOGLE_CLOUD_CPP_ENABLE=storage_grpc [other options here]
            

     2. In your codebase, for the `target_link_libraries()` command replace `google-cloud-cpp::storage` with `google-cloud-cpp::storage_grpc`

For example, the quickstart program for gRPC uses the following code:
            
            add_executable(quickstart_grpc quickstart_grpc.cc)
            target_link_libraries(quickstart_grpc google-cloud-cpp::storage_grpc)
            

### Bazel

Replace the dependencies from `@google_cloud_cpp//:storage` to `@google_cloud_cpp//:storage_grpc`.

For example, the quickstart program for gRPC uses the following code:
    
    cc_binary(
          name = "quickstart",
          srcs = [
              "quickstart.cc",
          ],
          deps = [
              "@com_github_googleapis_google_cloud_cpp//:storage_grpc",
          ],
      )
    




### Java

### Before you begin

  1. Ensure you have the following versions installed:

     * Java client libraries:

       * `com.google.cloud:google-cloud-storage:2.43.1` or later.
       * `com.google.cloud:libraries-bom:26.48` or later.
     * Java 8 or later

For installation instructions, see [Setting up a Java development environment](https://docs.cloud.google.com/java/docs/setup).

  2. [Set up authentication](https://docs.cloud.google.com/storage/docs/reference/libraries#authentication).

  3. Ensure each Compute Engine instance has a [service account](https://docs.cloud.google.com/compute/docs/instances/change-service-account) attached to it, even if the service account has no permissions. This service account is used to represent the Compute Engine instance in the [Application Layer Transport Security (ALTS)](https://docs.cloud.google.com/security/encryption-in-transit/application-layer-transport-security) handshake process and is required for [direct connectivity](https://docs.cloud.google.com/storage/docs/direct-connectivity).




### Update your project to use the BOM

To make sure that your projects have compatible versions of Google Cloud client libraries, use the versions specified in the [Google Cloud libraries Bill of Materials (BOM)](https://docs.cloud.google.com/java/docs/bom). To update your project to use the BOM, use any of the following methods:

  * Standalone Cloud Storage
  * Cloud Storage with other Google Cloud libraries



#### Standalone Cloud Storage

If you are using the Cloud Storage client library independently (without other Google Cloud libraries), use the Cloud Storage client library-specific BOM.

### Maven

Import the BOM in the `dependencyManagement` section of your `pom.xml` file.

The following example shows how you would import the BOM and include the `google-cloud-storage` artifact.
    
    
    <dependencyManagement>
      <dependencies>
      <dependency>
       <groupId>com.google.cloud</groupId>
       <artifactId>google-cloud-storage-bom</artifactId>
       <version>2.43.1</version>
       <type>pom</type>
       <scope>import</scope>
      </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
       <groupId>com.google.cloud</groupId>
       <artifactId>google-cloud-storage</artifactId>
      </dependency>
    </dependencies>
    

### Gradle

Add a platform dependency on `com.google.cloud:google-cloud-storage-bom`:
    
    
    implementation platform('com.google.cloud:google-cloud-storage-bom:2.43.1')
    implementation 'com.google.cloud:google-cloud-storage'
    

#### Cloud Storage with other Google Cloud libraries

If you are using the Cloud Storage client library along with other Google Cloud libraries, use the Google Cloud client libraries BOM.

### Maven

Import the BOM in the `dependencyManagement` section of your `pom.xml` file.

The following example shows how to import the BOM and include the `libraries-bom` artifact.
    
    
    <dependencyManagement>
      <dependencies>
      <dependency>
       <groupId>com.google.cloud</groupId>
       <artifactId>libraries-bom</artifactId>
       <version>26.48.0</version>
       <type>pom</type>
       <scope>import</scope>
      </dependency>
      </dependencies>
    </dependencyManagement>
    
    <dependencies>
      <dependency>
       <groupId>com.google.cloud</groupId>
       <artifactId>google-cloud-storage</artifactId>
      </dependency>
    </dependencies>
    

### Gradle

Add a platform dependency on `com.google.cloud:libraries-bom`:
    
    
    implementation platform('com.google.cloud:libraries-bom:26.48.0')
    implementation 'com.google.cloud:google-cloud-storage'
    

### Create a gRPC client

The following sample uses a gRPC centric builder. The gRPC Java client automatically uses direct connectivity when it detects that the application is running on Google Cloud.
    
    
    // Imports the Google Cloud client library
    import com.google.cloud.storage.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html);
    import com.google.cloud.storage.[BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    public class QuickstartGrpcSample {
      public static void main(String... args) throws Exception {
    
        // Create an instance of options which will use the Google Cloud Storage gRPC API for all
        // operations
        [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html) options = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).[grpc](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html#com_google_cloud_storage_StorageOptions_grpc__)().build();
    
        // Instantiates a client in a try-with-resource to automatically cleanup underlying resources
        try ([Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storage = options.[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)()) {
          // The name for the new bucket
          String bucketName = args[0]; // "my-new-bucket";
    
          // Creates the new bucket using a request to the gRPC API
          [Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Bucket.html) bucket = storage.create([BucketInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.BucketInfo.html).of(bucketName));
    
          System.out.printf("Bucket %s created.%n", bucket.getName());
        }
      }
    }

### Go

### Before you begin

  1. [Setup your development environment](https://docs.cloud.google.com/go/docs/setup).

  2. Ensure you use [Cloud Storage Go client library](https://pkg.go.dev/cloud.google.com/go/storage/) version 1.46.0 or later.

  3. [Set up authentication](https://docs.cloud.google.com/storage/docs/reference/libraries#authentication).

  4. Ensure each Compute Engine instance has a [service account](https://docs.cloud.google.com/compute/docs/instances/change-service-account) attached to it, even if the service account has no permissions. This service account is used to represent the Compute Engine instance in the [Application Layer Transport Security (ALTS)](https://docs.cloud.google.com/security/encryption-in-transit/application-layer-transport-security) handshake process and is required for [direct connectivity](https://docs.cloud.google.com/storage/docs/direct-connectivity).




### Create a gRPC client

To use the client, you need to call the [`NewGRPCClient`](https://pkg.go.dev/cloud.google.com/go/storage#NewGRPCClient) constructor in your application instead of [`NewClient`](https://pkg.go.dev/cloud.google.com/go/storage#NewClient).
    
    
    // Sample storage-quickstart creates a Google Cloud Storage bucket using
    // gRPC API.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    	"time"
    
    	"cloud.google.com/go/storage"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Use your Google Cloud Platform project ID and Cloud Storage bucket
    	projectID := "project-id"
    	bucketName := "bucket-name"
    
    	// Creates a gRPC enabled client.
    	client, err := storage.[NewGRPCClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_NewGRPCClient)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.Close()
    
    	// Creates the new bucket.
    	ctx, cancel := context.WithTimeout(ctx, time.Second*10)
    	defer cancel()
    	if err := client.[Bucket](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Bucket)(bucketName).[Create](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_BucketHandle_Create)(ctx, projectID, nil); err != nil {
    		log.Fatalf("Failed to create bucket: %v", err)
    	}
    
    	fmt.Printf("Bucket %v created.\n", bucketName)
    }
    

The Go client library automatically uses direct connectivity when it detects that the application is running on Google Cloud.

For information about how to use a gRPC client, see [gRPC API](https://pkg.go.dev/cloud.google.com/go/storage#hdr-gRPC_API).

## Configure VPC Service Controls

If you are using Virtual Private Cloud with restricted virtual IP addresses ([VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview)) to enhance the security of your network, you need to update your firewall rules to enable [direct connectivity](https://docs.cloud.google.com/storage/docs/direct-connectivity) for optimal performance between your Compute Engine instance and Cloud Storage bucket.

To do so, add allowlist firewall rules to permit traffic on all ports for the following CIDR blocks:

  * For IPv4 traffic: `34.126.0.0/18`
  * For IPv6 traffic: `2001:4860:8040::/42`



In addition to the preceding rules, retain the existing allowlist rule for `199.36.153.4/30`.

If you have restrictions on firewall rule modifications and you cannot update them, then you can force the traffic to avoid direct connectivity by using `storage.googleapis.com` as the Cloud Storage endpoint instead of `google-c2p://storage.googleapis.com`.

For example, for C++ use, `.set<google::cloud::EndpointOption>(storage.googleapis.com)` instead of `google-c2p:///storage.googleapis.com`.

**Note:** VPC networks have a default [maximum transmission unit (MTU)](https://www.wikipedia.org/wiki/Maximum_transmission_unit) of `1460` bytes. For improved throughput, we recommend increasing the default MTU to at least `4096` bytes. For more information about network MTUs, see the [maximum transmission unit overview](https://docs.cloud.google.com/vpc/docs/mtu).

## Enable observability for gRPC related requests

You can configure Cloud Storage client libraries to to generate gRPC related metrics in Cloud Monitoring. The gRPC related metrics can help you to do the following:

  * Monitor and optimize the performance of gRPC requests to Cloud Storage.

  * Troubleshoot and debug issues.

  * Gain insights into your application's usage and behavior.




For information about how to generate gRPC related metrics, see [Use client-side metrics](https://docs.cloud.google.com/storage/docs/client-side-metrics).

If gathering metrics isn't necessary for your use case, you can choose to opt-out of metrics collection. For instructions, see [Opt-out of client-side metrics](https://docs.cloud.google.com/storage/docs/client-side-metrics#opt_out_of_client-side_metrics).

## Limitations

  * IPv6 requests cannot be sent over [legacy networks](https://docs.cloud.google.com/vpc/docs/legacy).

  * Direct connectivity is not supported when using the following GKE versions on IPv4-only clusters:

    * 1.28, 1.28.0-gke.100 or later until 1.28.5-gke.1199000
    * 1.27, 1.27.4-gke.1900 or later
    * 1.26, 1.26.10-gke.1238000 or later
    * 1.25, 1.25.15-gke.1045000 or later
  * gRPC does not support the [`notifications`](https://docs.cloud.google.com/storage/docs/json_api/v1/notifications), [`hmacKeys`](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/hmacKeys), and [`serviceAccount`](https://docs.cloud.google.com/storage/docs/json_api/v1/projects/serviceAccount) methods.

  * HTTP-specific client constructor options, such as [WithHTTPClient](https://pkg.go.dev/google.golang.org/api/option#WithHTTPClient), are not supported for [Go](https://go.dev/) client library.

  * The gRPC API is not supported with [regional endpoints](https://docs.cloud.google.com/storage/docs/regional-endpoints).




## Troubleshooting direct connectivity

To learn how to check for direct connectivity and troubleshoot when it's not available, see [Direct connectivity](https://docs.cloud.google.com/storage/docs/direct-connectivity).

## What's next

  * [Connect to the Cloud Storage connector on Managed Service for Apache Spark using gRPC](https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-storage#connect-to-cloud-storage-using-grpc).
  * [Enable gRPC on Apache Beam I/O connector on Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/read-from-cloud-storage#enable-connector-grpc).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
