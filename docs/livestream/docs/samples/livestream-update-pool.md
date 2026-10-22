---
url: https://docs.cloud.google.com/livestream/docs/samples/livestream-update-pool/
title: Update a pool \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:47.569324+00:00
---

# Update a pool  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/samples/livestream-update-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Samples ](https://docs.cloud.google.com/livestream/docs/samples)



#  Update a pool Stay organized with collections  Save and categorize content based on your preferences. 

Update a live stream pool resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage pools](https://docs.cloud.google.com/livestream/docs/how-to/create-pools)



## Code sample

### C#

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.LiveStream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System.Threading.Tasks;
    
    public class UpdatePoolSample
    {
        public async Task UpdatePoolAsync(
             string projectId, string locationId, string poolId, string peeredNetwork)
        {
            // Create the client.
            [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html) client = [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_Create)();
    
            [UpdatePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.UpdatePoolRequest.html) request = new [UpdatePoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.UpdatePoolRequest.html)
            {
                Pool = new [Pool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Pool.html)
                {
                    PoolName = [PoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.PoolName.html).[FromProjectLocationPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.PoolName.html#Google_Cloud_Video_LiveStream_V1_PoolName_FromProjectLocationPool_System_String_System_String_System_String_)(projectId, locationId, poolId),
                    NetworkConfig = new Pool.Types.NetworkConfig
                    {
                        PeeredNetwork = peeredNetwork
                    }
                },
                UpdateMask = new [FieldMask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html) { Paths = { "network_config" } }
            };
    
            // Make the request.
            Operation<Pool, OperationMetadata> response = await client.[UpdatePoolAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_UpdatePoolAsync_Google_Cloud_Video_LiveStream_V1_Pool_Google_Protobuf_WellKnownTypes_FieldMask_Google_Api_Gax_Grpc_CallSettings_)(request);
            // Get the name of the operation.
            string operationName = response.Name;
            // This name can be stored, then the long-running operation retrieved later by name.
            Operation<Pool, OperationMetadata> retrievedResponse = await client.[PollOnceUpdatePoolAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_PollOnceUpdatePoolAsync_System_String_Google_Api_Gax_Grpc_CallSettings_)(operationName);
            // Check if the retrieved long-running operation has completed.
            if (retrievedResponse.IsCompleted)
            {
                // If it has completed, then access the result.
                _ = retrievedResponse.Result;
            }
        }
    }

### Go

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/livestream). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	livestream "cloud.google.com/go/video/livestream/apiv1"
    	"cloud.google.com/go/video/livestream/apiv1/livestreampb"
    	"google.golang.org/protobuf/types/known/fieldmaskpb"
    )
    
    // updatePool updates the pool's peered network.
    func updatePool(w io.Writer, projectID, location, poolID, peeredNetwork string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// poolID := "default"
    	// peeredNetwork :=  "projects/my-network-project-number/global/networks/my-network-name"
    	ctx := context.Background()
    	client, err := livestream.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_Close)()
    
    	req := &livestreampb.UpdatePoolRequest{
    		Pool: &livestreampb.Pool{
    			Name: fmt.Sprintf("projects/%s/locations/%s/pools/%s", projectID, location, poolID),
    			NetworkConfig: &livestreampb.Pool_NetworkConfig{
    				PeeredNetwork: peeredNetwork,
    			},
    		},
    		UpdateMask: &fieldmaskpb.FieldMask{
    			Paths: []string{
    				"network_config",
    			},
    		},
    	}
    	// Updates the pool.
    	op, err := client.UpdatePool(ctx, req)
    	if err != nil {
    		return fmt.Errorf("UpdatePool: %w", err)
    	}
    	response, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "Updated pool: %v", response.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/overview). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.livestream.v1.[LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html);
    import com.google.cloud.video.livestream.v1.[Pool](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool.html);
    import com.google.cloud.video.livestream.v1.[Pool](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool.html).[NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool.NetworkConfig.html);
    import com.google.cloud.video.livestream.v1.[PoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.PoolName.html);
    import com.google.cloud.video.livestream.v1.[UpdatePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdatePoolRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class UpdatePool {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String poolId = "default";
        String peeredNetwork = "";
    
        updatePool(projectId, location, poolId, peeredNetwork);
      }
    
      public static void updatePool(String projectId, String location, String poolId,
          String peeredNetwork)
          throws InterruptedException, ExecutionException, TimeoutException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        [LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html) livestreamServiceClient = [LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html).create();
        var updatePoolRequest =
            [UpdatePoolRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.UpdatePoolRequest.html).newBuilder()
                .setPool(
                    [Pool](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool.html).newBuilder()
                        .setName([PoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.PoolName.html).of(projectId, location, poolId).toString())
                        .[setNetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool.Builder.html#com_google_cloud_video_livestream_v1_Pool_Builder_setNetworkConfig_com_google_cloud_video_livestream_v1_Pool_NetworkConfig_)(
                            [NetworkConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool.NetworkConfig.html).newBuilder()
                                .[setPeeredNetwork](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool.NetworkConfig.Builder.html#com_google_cloud_video_livestream_v1_Pool_NetworkConfig_Builder_setPeeredNetwork_java_lang_String_)(peeredNetwork)
                                .build()
    
                        ))
                .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addPaths_java_lang_String_)("network_config").build())
                .build();
        // Update pool can take 20+ minutes.
        [Pool](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool.html) result =
            livestreamServiceClient.[updatePoolAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html#com_google_cloud_video_livestream_v1_LivestreamServiceClient_updatePoolAsync_com_google_cloud_video_livestream_v1_Pool_com_google_protobuf_FieldMask_)(updatePoolRequest).get(20, TimeUnit.MINUTES);
        System.out.println("Updated pool: " + result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool.html#com_google_cloud_video_livestream_v1_Pool_getName__)());
        livestreamServiceClient.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html#com_google_cloud_video_livestream_v1_LivestreamServiceClient_close__)();
      }
    }

### Node.js

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/livestream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    // poolId = 'my-pool';
    // peeredNetwork = 'projects/my-network-project-number/global/networks/my-network-name';
    
    // Imports the Livestream library
    const {LivestreamServiceClient} = require('[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)').v1;
    
    // Instantiates a client
    const livestreamServiceClient = new [LivestreamServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)();
    
    async function updatePool() {
      // Construct request
      const request = {
        pool: {
          name: livestreamServiceClient.[poolPath](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/v1.livestreamserviceclient.html)(projectId, location, poolId),
          networkConfig: {
            peeredNetwork: peeredNetwork,
          },
        },
        updateMask: {
          paths: ['network_config'],
        },
      };
    
      // Run request
      const [operation] = await livestreamServiceClient.updatePool(request);
      const response = await operation.promise();
      const [pool] = response;
      console.log(`Updated pool: ${pool.name}`);
    }
    
    updatePool();

### PHP

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videolivestream/readme). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\LiveStream\V1\Pool;
    use Google\Cloud\Video\LiveStream\V1\Client\LivestreamServiceClient;
    use Google\Cloud\Video\LiveStream\V1\UpdatePoolRequest;
    use Google\Protobuf\FieldMask;
    
    /**
     * Updates a pool.
     *
     * @param string  $callingProjectId   The project ID to run the API call under
     * @param string  $location           The location of the pool
     * @param string  $poolId             The ID of the pool to be updated
     * @param string  $peeredNetwork      The updated peer network
     */
    function update_pool(
        string $callingProjectId,
        string $location,
        string $poolId,
        string $peeredNetwork
    ): void {
        // Instantiate a client.
        $livestreamClient = new LivestreamServiceClient();
    
        $formattedName = $livestreamClient->poolName($callingProjectId, $location, $poolId);
        $pool = (new Pool())
            ->setName($formattedName)
            ->setNetworkConfig(
                (new Pool\NetworkConfig())
                    ->setPeeredNetwork($peeredNetwork));
    
        $updateMask = new FieldMask([
            'paths' => ['network_config']
        ]);
    
        // Run the pool update request. The response is a long-running operation ID.
        $request = (new UpdatePoolRequest())
            ->setPool($pool)
            ->setUpdateMask($updateMask);
        $operationResponse = $livestreamClient->updatePool($request);
    
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            $result = $operationResponse->getResult();
            // Print results
            printf('Updated pool: %s' . PHP_EOL, $result->getName());
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
    }

### Python

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/livestream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import live_stream_v1
    from google.cloud.video.live_stream_v1.services.livestream_service import (
        LivestreamServiceClient,
    )
    from google.protobuf import field_mask_pb2 as field_mask
    
    
    def update_pool(
        project_id: str, location: str, pool_id: str, peered_network: str
    ) -> live_stream_v1.types.Pool:
        """Updates an pool.
        Args:
            project_id: The GCP project ID.
            location: The location of the pool.
            pool_id: The user-defined pool ID.
            peered_network: The updated peer network (e.g.,
            'projects/my-network-project-number/global/networks/my-network-name')."""
    
        client = LivestreamServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/pools/{pool_id}"
    
        pool = live_stream_v1.types.Pool(
            name=name,
            network_config=live_stream_v1.types.Pool.NetworkConfig(
                peered_network=peered_network,
            ),
        )
        update_mask = field_mask.FieldMask(paths=["network_config"])
    
        operation = client.update_pool(pool=pool, update_mask=update_mask)
        response = operation.result()
        print(f"Updated pool: {response.name}")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/live_stream"
    
    ##
    # Update the pool's peered network
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param location [String] The location (e.g. "us-central1")
    # @param pool_id [String] Your pool name (e.g. "my-pool")
    # @param peered_network [String] The updated peer network
    #   (e.g. "projects/my-network-project-number/global/networks/my-network-name")
    #
    def update_pool project_id:, location:, pool_id:, peered_network:
      # Create a Live Stream client.
      client = Google::Cloud::Video::LiveStream.livestream_service
    
      # Build the resource name of the pool.
      name = client.pool_path project: project_id, location: location, pool: pool_id
    
      # Set the update mask.
      update_mask = { paths: ["network_config"] }
    
      # Update the pool's peered network.
      update_pool = {
        name: name,
        network_config: {
          peered_network: peered_network
        }
      }
    
      operation = client.update_pool update_mask: update_mask, pool: update_pool
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print the pool name.
      puts "Updated pool: #{operation.response.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=livestreamapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
