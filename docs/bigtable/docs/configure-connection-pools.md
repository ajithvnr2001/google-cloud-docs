---
url: https://docs.cloud.google.com/bigtable/docs/configure-connection-pools/
title: Configure connection pools \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:17.617616+00:00
---

# Configure connection pools  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/configure-connection-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure connection pools

Some Cloud Bigtable client libraries let you configure the number of gRPC channels in a client's connection pool, also known as a channel pool. **In most cases, the default configuration is correct, and there is no need to change it.**

Connection pools are automatically resized as needed when you use the Cloud Bigtable client library for Java version 2.23.0 or later, and when you use the Cloud Bigtable HBase client for Java version 2.9.1 or later.

This page describes how to determine the optimal connection pool size for your application, and it presents code snippets that show how to configure the connection pools.

Before you read this page, read the overview of [Bigtable connection pools](https://docs.cloud.google.com/bigtable/docs/connection-pools) to learn how they work and whether you should change yours.

The following client libraries offer connection pooling and let you configure the number of pools:

  * [Go client library for Cloud Bigtable](https://pkg.go.dev/github.com/GoogleCloudPlatform/golang-samples/bigtable/connectionpool)
  * [Cloud Bigtable HBase client for Java](https://github.com/googleapis/java-bigtable-hbase/blob/main/README.md)
  * [Cloud Bigtable client library for Java](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_setChannelPoolSettings_com_google_api_gax_grpc_ChannelPoolSettings__)
  * [Cloud Bigtable C++ client library](https://googleapis.dev/cpp/google-cloud-common/latest/grpc__options_8h.html)



## Determine the best connection pool size

Ideally, to leave room for traffic fluctuations, a connection pool has about twice the number of connections it takes for maximum saturation. Because a connection can handle a maximum of 100 concurrent requests, between 10 and 50 outstanding requests per connection is optimal. This concept is described in more detail in [Connection pools](https://docs.cloud.google.com/bigtable/docs/connection-pools).

Monitor your traffic after making changes and adjust the number of connections in your pool if necessary.

The following steps help you calculate the optimal number of connections in your channel pool using client-side metrics such as those available from [OpenCensus](https://opencensus.io/guides/grpc/java/#examining-metrics).

  1. From your client-side metrics, gather the following information: 
     1. The maximum number of queries per second (QPS) per client when your application is running a typical workload.
     2. The average latency (the response time for a single request) in ms.
  2. Determine the number of requests that you can send serially per second by dividing 1,000 by the average latency value.
  3. Divide the QPS in seconds by the number of serial requests per second.
  4. Divide the result by 50 requests per channel to determine the minimum optimal channel pool size. (If your calculation is less than 2, use at least 2 channels anyway, to ensure redundancy.)
  5. Divide the same result by 10 requests per channel to determine the maximum optimal channel pool size.



These steps are expressed in the following equations:

  * (QPS sec ÷ (1,000 ÷ latency ms)) ÷ 50 streams = Minimum optimal number of connections

  * (QPS sec ÷ (1,000 ÷ latency ms)) ÷ 10 streams = Maximum optimal number of connections




### Example

Your application typically sends 50,000 requests per second, and the average latency is 10 ms. Divide 1,000 by 10 ms to determine that you can send 100 requests serially per second. Divide that number into 50,000 to get the parallelism needed to send 50,000 QPS: 500. Each channel can have at most 100 requests out concurrently, and your target channel utilization is between 10 and 50 concurrent streams. Therefore, to calculate the minimum, divide 500 by 50 to get 10. To find the maximum, divide 500 by 10 to get 50. This means that your channel pool size for this example should be between 10 and 50 connections.

## Set the pool size

The following code samples demonstrate how to configure the number of pools in the client libraries that let you set the pool size.

### Go
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	"cloud.google.com/go/bigtable"
    	"google.golang.org/api/option"
    )
    
    func configureConnectionPool(w io.Writer, projectID, instanceID string) error {
    	// projectID := "my-project-id"
    	// instanceID := "my-instance-id"
    	ctx := context.Background()
    
    	// Set up Bigtable data operations client.
    	poolSize := 10
    	client, err := bigtable.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/bigtable/latest/index.html#cloud_google_com_go_bigtable_Client_NewClient)(ctx, projectID, instanceID, option.WithGRPCConnectionPool(poolSize))
    	defer client.Close()
    
    	if err != nil {
    		return fmt.Errorf("bigtable.NewClient: %w", err)
    	}
    
    	fmt.Fprintf(w, "Connected with pool size of %d", poolSize)
    
    	return nil
    }
    

### HBase

This sample is applicable only for client library versions earlier than 2.9.1, when automatic resizing was introduced.
    
    
    
    import static com.google.cloud.bigtable.hbase.BigtableOptionsFactory.BIGTABLE_DATA_CHANNEL_COUNT_KEY;
    
    import com.google.cloud.bigtable.hbase.BigtableConfiguration;
    import org.apache.hadoop.conf.Configuration;
    import org.apache.hadoop.hbase.client.Connection;
    
    public class ConfigureConnectionPool {
    
      public static void configureConnectionPool(String projectId, String instanceId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
        Configuration config = BigtableConfiguration.configure(projectId, instanceId);
        config.setInt(BIGTABLE_DATA_CHANNEL_COUNT_KEY, 10);
        try (Connection connection = BigtableConfiguration.connect(config)) {
          int poolSize = connection.getConfiguration().getInt(BIGTABLE_DATA_CHANNEL_COUNT_KEY, 0);
    
          System.out.println(String.format("Connected with pool size of %d", poolSize));
        } catch (Exception e) {
          System.out.println("Error during ConfigureConnectionPool: \n" + e.toString());
        }
      }
    }
    

### Java

This sample is applicable only for client library versions earlier than 2.23.0, when automatic resizing was introduced.
    
    
    import com.google.api.gax.grpc.[InstantiatingGrpcChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.html);
    import com.google.cloud.bigtable.data.v2.[BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html);
    import com.google.cloud.bigtable.data.v2.[BigtableDataSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html);
    import com.google.cloud.bigtable.data.v2.stub.EnhancedBigtableStubSettings;
    import java.io.IOException;
    
    public class ConfigureConnectionPool {
    
      public static void configureConnectionPool(String projectId, String instanceId) {
        // String projectId = "my-project-id";
        // String instanceId = "my-instance-id";
    
        [BigtableDataSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html).Builder settingsBuilder =
            [BigtableDataSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html).newBuilder().[setProjectId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.Builder.html#com_google_cloud_bigtable_data_v2_BigtableDataSettings_Builder_setProjectId_java_lang_String_)(projectId).[setInstanceId](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.Builder.html#com_google_cloud_bigtable_data_v2_BigtableDataSettings_Builder_setInstanceId_java_lang_String_)(instanceId);
    
        settingsBuilder
            .[stubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.Builder.html#com_google_cloud_bigtable_data_v2_BigtableDataSettings_Builder_stubSettings__)()
            .setTransportChannelProvider(
                EnhancedBigtableStubSettings.defaultGrpcTransportProviderBuilder()
                    .[setPoolSize](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder.html#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_setPoolSize_int_)(10)
                    .build());
    
        [BigtableDataSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html) settings = settingsBuilder.build();
        try ([BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html) dataClient = [BigtableDataClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataClient.html).create(settings)) {
          [InstantiatingGrpcChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.html) provider =
              ([InstantiatingGrpcChannelProvider](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.html))
                  settings.[getStubSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/com.google.cloud.bigtable.data.v2.BigtableDataSettings.html#com_google_cloud_bigtable_data_v2_BigtableDataSettings_getStubSettings__)().getTransportChannelProvider();
    
          int poolSize = provider.[toBuilder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.html#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_toBuilder__)().[getPoolSize](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.grpc.InstantiatingGrpcChannelProvider.Builder.html#com_google_api_gax_grpc_InstantiatingGrpcChannelProvider_Builder_getPoolSize__)();
    
          System.out.println(String.format("Connected with pool size of %d", poolSize));
        } catch (IOException e) {
          System.out.println("Error during ConfigureConnectionPool: \n" + e.toString());
        }
      }
    }
    

### C++
    
    
    namespace cbt = ::google::cloud::bigtable;
    namespace gc = ::google::cloud;
    [](std::string const& project_id, std::string const& instance_id,
       std::string const& table_id) {
      auto constexpr kPoolSize = 10;
      auto options = gc::Options{}.set<gc::GrpcNumChannelsOption>(kPoolSize);
      cbt::Table table(
          cbt::MakeDataConnection(
              {cbt::InstanceResource(gc::Project(project_id), instance_id)},
              std::move(options)),
          cbt::TableResource(project_id, instance_id, table_id));
      std::cout << "Connected with channel pool size of " << kPoolSize << "\n";
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
