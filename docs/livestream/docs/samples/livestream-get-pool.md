---
url: https://docs.cloud.google.com/livestream/docs/samples/livestream-get-pool/
title: Get a pool \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:36.672795+00:00
---

# Get a pool  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/samples/livestream-get-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Samples ](https://docs.cloud.google.com/livestream/docs/samples)



#  Get a pool Stay organized with collections  Save and categorize content based on your preferences. 

Get details for a live stream pool resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage pools](https://docs.cloud.google.com/livestream/docs/how-to/create-pools)



## Code sample

### C#

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.LiveStream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.html);
    
    public class GetPoolSample
    {
        public Pool GetPool(
             string projectId, string locationId, string poolId)
        {
            // Create the client.
            [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html) client = [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_Create)();
    
            [GetPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.GetPoolRequest.html) request = new [GetPoolRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.GetPoolRequest.html)
            {
                PoolName = [PoolName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.PoolName.html).[FromProjectLocationPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.PoolName.html#Google_Cloud_Video_LiveStream_V1_PoolName_FromProjectLocationPool_System_String_System_String_System_String_)(projectId, locationId, poolId)
            };
    
            // Make the request.
            [Pool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Pool.html) response = client.[GetPool](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_GetPool_Google_Cloud_Video_LiveStream_V1_GetPoolRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
            return response;
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
    )
    
    // getPool gets a pool.
    func getPool(w io.Writer, projectID, location, poolID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// poolID := "default"
    	ctx := context.Background()
    	client, err := livestream.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_Close)()
    
    	req := &livestreampb.GetPoolRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/pools/%s", projectID, location, poolID),
    	}
    
    	response, err := client.GetPool(ctx, req)
    	if err != nil {
    		return fmt.Errorf("GetPool: %w", err)
    	}
    
    	fmt.Fprintf(w, "Pool: %v", response.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/overview). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.livestream.v1.[LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html);
    import com.google.cloud.video.livestream.v1.[Pool](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool.html);
    import com.google.cloud.video.livestream.v1.[PoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.PoolName.html);
    import java.io.IOException;
    
    public class GetPool {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String poolId = "default"; // only 1 pool supported per location
    
        getPool(projectId, location, poolId);
      }
    
      public static void getPool(String projectId, String location, String poolId)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. In this example, try-with-resources is used
        // which automatically calls close() on the client to clean up resources.
        try ([LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html) livestreamServiceClient = [LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html).create()) {
          [PoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.PoolName.html) name = [PoolName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.PoolName.html).of(projectId, location, poolId);
          [Pool](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool.html) response = livestreamServiceClient.getPool(name);
          System.out.println("Pool: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Pool.html#com_google_cloud_video_livestream_v1_Pool_getName__)());
        }
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
    
    // Imports the Livestream library
    const {LivestreamServiceClient} = require('[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)').v1;
    
    // Instantiates a client
    const livestreamServiceClient = new [LivestreamServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)();
    
    async function getPool() {
      // Construct request
      const request = {
        name: livestreamServiceClient.[poolPath](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/v1.livestreamserviceclient.html)(projectId, location, poolId),
      };
      const [pool] = await livestreamServiceClient.getPool(request);
      console.log(`Pool: ${pool.name}`);
    }
    
    getPool();

### PHP

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videolivestream/readme). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\LiveStream\V1\Client\LivestreamServiceClient;
    use Google\Cloud\Video\LiveStream\V1\GetPoolRequest;
    
    /**
     * Gets a pool.
     *
     * @param string  $callingProjectId   The project ID to run the API call under
     * @param string  $location           The location of the pool
     * @param string  $poolId             The ID of the pool
     */
    function get_pool(
        string $callingProjectId,
        string $location,
        string $poolId
    ): void {
        // Instantiate a client.
        $livestreamClient = new LivestreamServiceClient();
        $formattedName = $livestreamClient->poolName($callingProjectId, $location, $poolId);
    
        // Get the pool.
        $request = (new GetPoolRequest())
            ->setName($formattedName);
        $response = $livestreamClient->getPool($request);
        // Print results
        printf('Pool: %s' . PHP_EOL, $response->getName());
    }

### Python

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/livestream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import live_stream_v1
    from google.cloud.video.live_stream_v1.services.livestream_service import (
        LivestreamServiceClient,
    )
    
    
    def get_pool(project_id: str, location: str, pool_id: str) -> live_stream_v1.types.Pool:
        """Gets a pool.
        Args:
            project_id: The GCP project ID.
            location: The location of the pool.
            pool_id: The user-defined pool ID."""
    
        client = LivestreamServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/pools/{pool_id}"
        response = client.get_pool(name=name)
        print(f"Pool: {response.name}")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/live_stream"
    
    ##
    # Get the pool
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param location [String] The location (e.g. "us-central1")
    # @param pool_id [String] Your pool name (e.g. "default")
    #
    def get_pool project_id:, location:, pool_id:
      # Create a Live Stream client.
      client = Google::Cloud::Video::LiveStream.livestream_service
    
      # Build the resource name of the pool.
      name = client.pool_path project: project_id, location: location, pool: pool_id
    
      # Get the pool.
      pool = client.get_pool name: name
    
      # Print the pool name.
      puts "Pool: #{pool.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=livestreamapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
