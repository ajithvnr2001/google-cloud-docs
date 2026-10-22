---
url: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-configure-connection-pool/
title: Configure connection pools \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:12.059646+00:00
---

# Configure connection pools  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/samples/bigtable-configure-connection-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Samples ](https://docs.cloud.google.com/bigtable/docs/samples)



#  Configure connection pools Stay organized with collections  Save and categorize content based on your preferences. 

Configure connection pools

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Configure connection pools](https://docs.cloud.google.com/bigtable/docs/configure-connection-pools)



## Code sample

### C++

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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

### Go

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

### Java

To learn how to install and use the client library for Bigtable, see [Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries). 

To authenticate to Bigtable, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
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
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=bigtable). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
