---
url: https://docs.cloud.google.com/livestream/docs/samples/livestream-create-asset/
title: Create an asset \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:02.449964+00:00
---

# Create an asset  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/samples/livestream-create-asset/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Samples ](https://docs.cloud.google.com/livestream/docs/samples)



#  Create an asset Stay organized with collections  Save and categorize content based on your preferences. 

Create an asset resource. Assets are video or images that can be used with the Live Stream API. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage assets](https://docs.cloud.google.com/livestream/docs/how-to/create-assets)
  * [Insert a slate into a live stream](https://docs.cloud.google.com/livestream/docs/how-to/insert-slate)



## Code sample

### C#

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.LiveStream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System.Threading.Tasks;
    
    public class CreateAssetSample
    {
        public async Task<Asset> CreateAssetAsync(
             string projectId, string locationId, string assetId, string assetUri)
        {
            // Create the client.
            [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html) client = [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_Create)();
    
            [CreateAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.CreateAssetRequest.html) request = new [CreateAssetRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.CreateAssetRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, locationId),
                AssetId = assetId,
                Asset = new [Asset](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.Asset.html)
                {
                    Video = new Asset.Types.VideoAsset
                    {
                        Uri = assetUri
                    }
                }
            };
    
            // Make the request.
            Operation<Asset, OperationMetadata> response = await client.[CreateAssetAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_CreateAssetAsync_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_LiveStream_V1_Asset_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            Operation<Asset, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    
            // Retrieve the operation result.
            return completedResponse.Result;
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
    
    // createAsset creates an asset. This asset references a video file
    // in Cloud Storage.
    func createAsset(w io.Writer, projectID, location, assetID, assetURI string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// assetID := "my-asset"
    	// assetURI := "gs://my-bucket/my-video.mp4"
    	ctx := context.Background()
    	client, err := livestream.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_Close)()
    
    	req := &livestreampb.CreateAssetRequest{
    		Parent:  fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		AssetId: assetID,
    		Asset: &livestreampb.Asset{
    			Resource: &livestreampb.Asset_Video{
    				Video: &livestreampb.Asset_VideoAsset{
    					Uri: assetURI,
    				},
    			},
    		},
    	}
    	// Creates the asset.
    	op, err := client.CreateAsset(ctx, req)
    	if err != nil {
    		return fmt.Errorf("CreateAsset: %w", err)
    	}
    	response, err := op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "Asset: %v", response.Name)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/overview). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.livestream.v1.[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Asset.html);
    import com.google.cloud.video.livestream.v1.[Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Asset.html).[VideoAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Asset.VideoAsset.html);
    import com.google.cloud.video.livestream.v1.[CreateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateAssetRequest.html);
    import com.google.cloud.video.livestream.v1.[LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html);
    import com.google.cloud.video.livestream.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LocationName.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateAsset {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String assetId = "my-asset-id";
        String assetUri = "gs://my-bucket/my-video.mp4";
    
        createAsset(projectId, location, assetId, assetUri);
      }
    
      public static void createAsset(String projectId, String location, String assetId, String assetUri)
          throws InterruptedException, ExecutionException, TimeoutException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        [LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html) livestreamServiceClient = [LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html).create();
        var createAssetRequest =
            [CreateAssetRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateAssetRequest.html).newBuilder()
                .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LocationName.html).of(projectId, location).toString())
                .[setAssetId](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.CreateAssetRequest.Builder.html#com_google_cloud_video_livestream_v1_CreateAssetRequest_Builder_setAssetId_java_lang_String_)(assetId)
                .setAsset(
                    [Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Asset.html).newBuilder()
                        .[setVideo](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Asset.Builder.html#com_google_cloud_video_livestream_v1_Asset_Builder_setVideo_com_google_cloud_video_livestream_v1_Asset_VideoAsset_)(
                            [VideoAsset](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Asset.VideoAsset.html).newBuilder()
                                .setUri(assetUri)
                                .build())
                        .build())
                .build();
        // First API call in a project can take up to 15 minutes.
        [Asset](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Asset.html) result =
            livestreamServiceClient.[createAssetAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html#com_google_cloud_video_livestream_v1_LivestreamServiceClient_createAssetAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_livestream_v1_LocationName_com_google_cloud_video_livestream_v1_Asset_java_lang_String_)(createAssetRequest).get(15, TimeUnit.MINUTES);
        System.out.println("Asset: " + result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.Asset.html#com_google_cloud_video_livestream_v1_Asset_getName__)());
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
    // assetId = 'my-asset';
    // assetUri = 'gs://my-bucket/my-video.mp4';
    
    // Imports the Livestream library
    const {LivestreamServiceClient} = require('[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)').v1;
    
    // Instantiates a client
    const livestreamServiceClient = new [LivestreamServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)();
    
    async function createAsset() {
      // Construct request
      const request = {
        parent: livestreamServiceClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/v1.livestreamserviceclient.html)(projectId, location),
        assetId: assetId,
        asset: {
          video: {
            uri: assetUri,
          },
        },
      };
    
      // Run request
      const [operation] = await livestreamServiceClient.createAsset(request);
      const response = await operation.promise();
      const [asset] = response;
      console.log(`Asset: ${asset.name}`);
    }
    
    createAsset();

### PHP

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videolivestream/readme). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\LiveStream\V1\Asset;
    use Google\Cloud\Video\LiveStream\V1\Client\LivestreamServiceClient;
    use Google\Cloud\Video\LiveStream\V1\CreateAssetRequest;
    
    /**
     * Creates an asset. You can use an asset to create a slate.
     *
     * @param string  $callingProjectId   The project ID to run the API call under
     * @param string  $location           The location of the asset
     * @param string  $assetId            The ID of the asset to be created
     * @param string  $assetUri           The Cloud Storage URI of the asset
     */
    function create_asset(
        string $callingProjectId,
        string $location,
        string $assetId,
        string $assetUri
    ): void {
        // Instantiate a client.
        $livestreamClient = new LivestreamServiceClient();
    
        $parent = $livestreamClient->locationName($callingProjectId, $location);
        $asset = (new Asset())
            ->setVideo(
                (new Asset\VideoAsset())
                    ->setUri($assetUri));
    
        // Run the asset creation request. The response is a long-running operation ID.
        $request = (new CreateAssetRequest())
            ->setParent($parent)
            ->setAsset($asset)
            ->setAssetId($assetId);
        $operationResponse = $livestreamClient->createAsset($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            $result = $operationResponse->getResult();
            // Print results
            printf('Asset: %s' . PHP_EOL, $result->getName());
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
    
    
    def create_asset(
        project_id: str, location: str, asset_id: str, asset_uri: str
    ) -> live_stream_v1.types.Asset:
        """Creates an asset.
        Args:
            project_id: The GCP project ID.
            location: The location in which to create the asset.
            asset_id: The user-defined asset ID.
            asset_uri: The asset URI (e.g., 'gs://my-bucket/my-video.mp4')."""
    
        client = LivestreamServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
    
        asset = live_stream_v1.types.Asset(
            video=live_stream_v1.types.Asset.VideoAsset(
                uri=asset_uri,
            )
        )
        operation = client.create_asset(parent=parent, asset=asset, asset_id=asset_id)
        response = operation.result(600)
        print(f"Asset: {response.name}")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/live_stream"
    
    ##
    # Create an asset
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param location [String] The location (e.g. "us-central1")
    # @param asset_id [String] Your asset name (e.g. "my-asset")
    # @param asset_uri [String] Your asset URI (e.g. "gs://my-bucket/my-video.mp4")
    #
    def create_asset project_id:, location:, asset_id:, asset_uri:
      # Create a Live Stream client.
      client = Google::Cloud::Video::LiveStream.livestream_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
    
      # Set the asset fields.
      new_asset = {
        video: {
          uri: asset_uri
        }
      }
    
      operation = client.create_asset parent: parent, asset: new_asset, asset_id: asset_id
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print the asset name.
      puts "Asset: #{operation.response.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=livestreamapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
