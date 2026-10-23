---
url: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-create-slate/
title: Create a slate \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:14.305194+00:00
---

# Create a slate  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-create-slate/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Samples ](https://docs.cloud.google.com/video-stitcher/docs/samples)



#  Create a slate Stay organized with collections  Save and categorize content based on your preferences. 

Slates are content that can be served when there are gaps in a live stream ad break that cannot be filled with a dynamically served ad. Create a slate to serve content during these gaps.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage slates](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-slates)
  * [Insert ads into livestreams](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-live)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using System.Threading.Tasks;
    
    public class CreateSlateSample
    {
        public async Task<Slate> CreateSlateAsync(
            string projectId, string location, string slateId, string slateUri)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [CreateSlateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateSlateRequest.html) request = new [CreateSlateRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateSlateRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, location),
                SlateId = slateId,
                Slate = new [Slate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.Slate.html)
                {
                    Uri = slateUri
                }
            };
    
            // Make the request.
            Operation<Slate, OperationMetadata> response = await client.[CreateSlateAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_CreateSlateAsync_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_Stitcher_V1_Slate_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            Operation<Slate, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    
            // Retrieve the operation result.
            return completedResponse.Result;
        }
    }
    

### Go

Before trying this sample, follow the Go setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/video/stitcher). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    
    	stitcher "cloud.google.com/go/video/stitcher/apiv1"
    	stitcherstreampb "cloud.google.com/go/video/stitcher/apiv1/stitcherpb"
    )
    
    // createSlate creates a slate. A slate is displayed when ads are not available.
    func createSlate(w io.Writer, projectID, slateID, slateURI string) error {
    	// projectID := "my-project-id"
    	// slateID := "my-slate-id"
    	// slateURI := "https://my-slate-uri/test.mp4"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.CreateSlateRequest{
    		Parent:  fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		SlateId: slateID,
    		Slate: &stitcherstreampb.Slate{
    			Uri: slateURI,
    		},
    	}
    	// Creates the slate.
    	op, err := client.CreateSlate(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateSlate: %w", err)
    	}
    	response, err := op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Slate: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateSlateRequest.html);
    import com.google.cloud.video.stitcher.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html);
    import com.google.cloud.video.stitcher.v1.[Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateSlate {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String slateId = "my-slate-id";
        String slateUri =
            "https://my-slate-uri/test.mp4"; // URI of an MP4 video with at least one audio track
    
        createSlate(projectId, location, slateId, slateUri);
      }
    
      // Creates a slate. Slates are content that can be served when there are gaps in a livestream
      // ad break that cannot be filled with a dynamically served ad. For more information, see
      // https://cloud.google.com/video-stitcher/docs/how-to/managing-slates.
      public static [Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate.html) createSlate(
          String projectId, String location, String slateId, String slateUri)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateSlateRequest.html) createSlateRequest =
              [CreateSlateRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateSlateRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html).of(projectId, location).toString())
                  .[setSlateId](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateSlateRequest.Builder.html#com_google_cloud_video_stitcher_v1_CreateSlateRequest_Builder_setSlateId_java_lang_String_)(slateId)
                  .setSlate([Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate.html).newBuilder().setUri(slateUri).build())
                  .build();
    
          [Slate](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate.html) response =
              videoStitcherServiceClient
                  .[createSlateAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html#com_google_cloud_video_stitcher_v1_VideoStitcherServiceClient_createSlateAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_stitcher_v1_LocationName_com_google_cloud_video_stitcher_v1_Slate_java_lang_String_)(createSlateRequest)
                  .get(TIMEOUT_IN_MINUTES, TimeUnit.MINUTES);
          System.out.println("Created new slate: " + response.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.Slate.html#com_google_cloud_video_stitcher_v1_Slate_getName__)());
          return response;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // location = 'us-central1';
    // slateId = 'my-slate';
    // slateUri = 'https://my-slate-uri/test.mp4';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function createSlate() {
      // Construct request
      const request = {
        parent: stitcherClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location),
        slate: {
          uri: slateUri,
        },
        slateId: slateId,
      };
      const [operation] = await stitcherClient.createSlate(request);
      const [response] = await operation.promise();
      console.log(`response.name: ${response.name}`);
    }
    
    createSlate().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\CreateSlateRequest;
    use Google\Cloud\Video\Stitcher\V1\Slate;
    
    /**
     * Creates a slate. A slate is displayed when ads are not available.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the slate
     * @param string $slateId              The name of the slate to be created
     * @param string $slateUri             The public URI for an MP4 video with at least one audio track
     */
    function create_slate(
        string $callingProjectId,
        string $location,
        string $slateId,
        string $slateUri
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $parent = $stitcherClient->locationName($callingProjectId, $location);
        $slate = new Slate();
        $slate->setUri($slateUri);
    
        // Run slate creation request
        $request = (new CreateSlateRequest())
            ->setParent($parent)
            ->setSlateId($slateId)
            ->setSlate($slate);
        $operationResponse = $stitcherClient->createSlate($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            $result = $operationResponse->getResult();
            // Print results
            printf('Slate: %s' . PHP_EOL, $result->getName());
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video import stitcher_v1
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    
    
    def create_slate(
        project_id: str, location: str, slate_id: str, slate_uri: str
    ) -> stitcher_v1.types.Slate:
        """Creates a slate.
        Args:
            project_id: The GCP project ID.
            location: The location in which to create the slate.
            slate_id: The user-defined slate ID.
            slate_uri: Uri of the video slate; must be an MP4 video with at least one audio track.
    
        Returns:
            The slate resource.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
    
        slate = stitcher_v1.types.Slate(
            uri=slate_uri,
        )
    
        operation = client.create_slate(parent=parent, slate_id=slate_id, slate=slate)
        response = operation.result()
        print(f"Slate: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Create a slate
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param slate_id [String] Your slate name (e.g. `my-slate`)
    # @param slate_uri [String] The URI of an MP4 video with at least one audio
    #   track (e.g. `https://my-slate-uri/test.mp4`)
    #
    def create_slate project_id:, location:, slate_id:, slate_uri:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
    
      # Set the slate fields.
      new_slate = {
        uri: slate_uri
      }
    
      operation = client.create_slate parent: parent, slate_id: slate_id,
                                      slate: new_slate
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print the slate name.
      puts "Slate: #{operation.response.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videostitcherapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
