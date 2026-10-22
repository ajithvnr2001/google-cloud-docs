---
url: https://docs.cloud.google.com/livestream/docs/samples/livestream-delete-input/
title: Delete an input endpoint \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:37.096755+00:00
---

# Delete an input endpoint  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/samples/livestream-delete-input/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Samples ](https://docs.cloud.google.com/livestream/docs/samples)



#  Delete an input endpoint Stay organized with collections  Save and categorize content based on your preferences. 

Delete a live stream input endpoint resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage input endpoints](https://docs.cloud.google.com/livestream/docs/how-to/create-input-endpoints)
  * [Quickstart for an HLS live stream](https://docs.cloud.google.com/livestream/docs/quickstarts/quickstart-hls)
  * [Quickstart for an MPEG-DASH live stream](https://docs.cloud.google.com/livestream/docs/quickstarts/quickstart-dash)



## Code sample

### C#

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.LiveStream.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System.Threading.Tasks;
    
    public class DeleteInputSample
    {
        public async Task DeleteInputAsync(
             string projectId, string locationId, string inputId)
        {
            // Create the client.
            [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html) client = [LivestreamServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_Create)();
    
            [DeleteInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.DeleteInputRequest.html) request = new [DeleteInputRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.DeleteInputRequest.html)
            {
                InputName = [InputName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.InputName.html).[FromProjectLocationInput](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.InputName.html#Google_Cloud_Video_LiveStream_V1_InputName_FromProjectLocationInput_System_String_System_String_System_String_)(projectId, locationId, inputId)
            };
    
            // Make the request.
            Operation<Empty, OperationMetadata> response = await client.[DeleteInputAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.LiveStream.V1/latest/Google.Cloud.Video.LiveStream.V1.LivestreamServiceClient.html#Google_Cloud_Video_LiveStream_V1_LivestreamServiceClient_DeleteInputAsync_Google_Cloud_Video_LiveStream_V1_DeleteInputRequest_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            await response.PollUntilCompletedAsync();
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
    
    // deleteInput deletes a previously-created input endpoint.
    func deleteInput(w io.Writer, projectID, location, inputID string) error {
    	// projectID := "my-project-id"
    	// location := "us-central1"
    	// inputID := "my-input"
    	ctx := context.Background()
    	client, err := livestream.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/livestream/apiv1.html#cloud_google_com_go_video_livestream_apiv1_Client_Close)()
    
    	req := &livestreampb.DeleteInputRequest{
    		Name: fmt.Sprintf("projects/%s/locations/%s/inputs/%s", projectID, location, inputID),
    	}
    
    	op, err := client.DeleteInput(ctx, req)
    	if err != nil {
    		return fmt.Errorf("DeleteInput: %w", err)
    	}
    	err = op.Wait(ctx)
    	if err != nil {
    		return fmt.Errorf("Wait: %w", err)
    	}
    
    	fmt.Fprintf(w, "Deleted input")
    	return nil
    }
    

### Java

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/overview). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.livestream.v1.[DeleteInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteInputRequest.html);
    import com.google.cloud.video.livestream.v1.[InputName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.InputName.html);
    import com.google.cloud.video.livestream.v1.[LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteInput {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String inputId = "my-input-id";
    
        deleteInput(projectId, location, inputId);
      }
    
      public static void deleteInput(String projectId, String location, String inputId)
          throws InterruptedException, ExecutionException, TimeoutException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        [LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html) livestreamServiceClient = [LivestreamServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html).create();
        var deleteInputRequest =
            [DeleteInputRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.DeleteInputRequest.html).newBuilder()
                .setName([InputName](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.InputName.html).of(projectId, location, inputId).toString())
                .build();
        // First API call in a project can take up to 10 minutes.
        livestreamServiceClient.[deleteInputAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-live-stream/latest/com.google.cloud.video.livestream.v1.LivestreamServiceClient.html#com_google_cloud_video_livestream_v1_LivestreamServiceClient_deleteInputAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_livestream_v1_InputName_)(deleteInputRequest).get(10, TimeUnit.MINUTES);
        System.out.println("Deleted input");
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
    // inputId = 'my-input';
    
    // Imports the Livestream library
    const {LivestreamServiceClient} = require('[@google-cloud/livestream](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)').v1;
    
    // Instantiates a client
    const livestreamServiceClient = new [LivestreamServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/overview.html)();
    
    async function deleteInput() {
      // Construct request
      const request = {
        name: livestreamServiceClient.[inputPath](https://docs.cloud.google.com/nodejs/docs/reference/livestream/latest/livestream/v1.livestreamserviceclient.html)(projectId, location, inputId),
      };
    
      // Run request
      const [operation] = await livestreamServiceClient.deleteInput(request);
      await operation.promise();
      console.log('Deleted input');
    }
    
    deleteInput();

### PHP

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videolivestream/readme). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\LiveStream\V1\Client\LivestreamServiceClient;
    use Google\Cloud\Video\LiveStream\V1\DeleteInputRequest;
    
    /**
     * Deletes an input.
     *
     * @param string  $callingProjectId   The project ID to run the API call under
     * @param string  $location           The location of the input
     * @param string  $inputId            The ID of the input to be deleted
     */
    function delete_input(
        string $callingProjectId,
        string $location,
        string $inputId
    ): void {
        // Instantiate a client.
        $livestreamClient = new LivestreamServiceClient();
        $formattedName = $livestreamClient->inputName($callingProjectId, $location, $inputId);
    
        // Run the input deletion request. The response is a long-running operation ID.
        $request = (new DeleteInputRequest())
            ->setName($formattedName);
        $operationResponse = $livestreamClient->deleteInput($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            // Print status
            printf('Deleted input %s' . PHP_EOL, $inputId);
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
    }

### Python

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/livestream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video.live_stream_v1.services.livestream_service import (
        LivestreamServiceClient,
    )
    from google.protobuf import empty_pb2 as empty
    
    
    def delete_input(project_id: str, location: str, input_id: str) -> empty.Empty:
        """Deletes an input.
        Args:
            project_id: The GCP project ID.
            location: The location of the input.
            input_id: The user-defined input ID."""
    
        client = LivestreamServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/inputs/{input_id}"
        operation = client.delete_input(name=name)
        response = operation.result(600)
        print("Deleted input")
    
        return response
    
    

### Ruby

To learn how to install and use the client library for Live Stream API, see [Live Stream API client libraries](https://docs.cloud.google.com/livestream/docs/reference/libraries). For more information, see the [Live Stream API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-live_stream/latest). 

To authenticate to Live Stream API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/live_stream"
    
    ##
    # Delete an input endpoint
    #
    # @param project_id [String] Your Google Cloud project (e.g. "my-project")
    # @param location [String] The location (e.g. "us-central1")
    # @param input_id [String] Your input name (e.g. "my-input")
    #
    def delete_input project_id:, location:, input_id:
      # Create a Live Stream client.
      client = Google::Cloud::Video::LiveStream.livestream_service
    
      # Build the resource name of the input.
      name = client.input_path project: project_id, location: location, input: input_id
    
      # Delete the input.
      operation = client.delete_input name: name
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print a success message.
      puts "Deleted input"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=livestreamapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
