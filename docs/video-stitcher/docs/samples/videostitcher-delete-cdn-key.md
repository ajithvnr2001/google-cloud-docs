---
url: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-delete-cdn-key/
title: Delete a CDN key \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:22.590641+00:00
---

# Delete a CDN key  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-delete-cdn-key/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Samples ](https://docs.cloud.google.com/video-stitcher/docs/samples)



#  Delete a CDN key Stay organized with collections  Save and categorize content based on your preferences. 

Delete a Video Stitcher CDN key resource. 

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage CDN keys](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys)
  * [Insert ads into livestreams](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-live)
  * [Insert ads into VOD assets](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf.WellKnownTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.html);
    using System.Threading.Tasks;
    
    public class DeleteCdnKeySample
    {
        public async Task DeleteCdnKeyAsync(
            string projectId, string location, string cdnKeyId)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [DeleteCdnKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.DeleteCdnKeyRequest.html) request = new [DeleteCdnKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.DeleteCdnKeyRequest.html)
            {
                CdnKeyName = [CdnKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKeyName.html).[FromProjectLocationCdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKeyName.html#Google_Cloud_Video_Stitcher_V1_CdnKeyName_FromProjectLocationCdnKey_System_String_System_String_System_String_)(projectId, location, cdnKeyId)
            };
    
            // Make the request.
            Operation<Empty, OperationMetadata> response = await client.[DeleteCdnKeyAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_DeleteCdnKeyAsync_Google_Cloud_Video_Stitcher_V1_CdnKeyName_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            await response.PollUntilCompletedAsync();
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
    
    // deleteCDNKey deletes a CDN key.
    func deleteCDNKey(w io.Writer, projectID, keyID string) error {
    	// projectID := "my-project-id"
    	// keyID := "my-cdn-key"
    	location := "us-central1"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	name := fmt.Sprintf("projects/%s/locations/%s/cdnKeys/%s", projectID, location, keyID)
    
    	req := &stitcherstreampb.DeleteCdnKeyRequest{
    		Name: name,
    	}
    	// Deletes the CDN key.
    	op, err := client.DeleteCdnKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.DeleteCdnKey: %w", err)
    	}
    	err = op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "Deleted CDN key")
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[CdnKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKeyName.html);
    import com.google.cloud.video.stitcher.v1.[DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class DeleteCdnKey {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String cdnKeyId = "my-cdn-key-id";
    
        deleteCdnKey(projectId, location, cdnKeyId);
      }
    
      // Deletes a CDN key.
      public static void deleteCdnKey(String projectId, String location, String cdnKeyId)
          throws InterruptedException, ExecutionException, TimeoutException, IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest.html) deleteCdnKeyRequest =
              [DeleteCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.DeleteCdnKeyRequest.html).newBuilder()
                  .setName([CdnKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKeyName.html).of(projectId, location, cdnKeyId).toString())
                  .build();
    
          videoStitcherServiceClient
              .[deleteCdnKeyAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html#com_google_cloud_video_stitcher_v1_VideoStitcherServiceClient_deleteCdnKeyAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_stitcher_v1_CdnKeyName_)(deleteCdnKeyRequest)
              .get(TIMEOUT_IN_MINUTES, TimeUnit.MINUTES);
          System.out.println("Deleted CDN key");
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
    // cdnKeyId = 'my-cdn-key';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function deleteCdnKey() {
      // Construct request
      const request = {
        name: stitcherClient.[cdnKeyPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location, cdnKeyId),
      };
      const [operation] = await stitcherClient.deleteCdnKey(request);
      await operation.promise();
      console.log('Deleted CDN key');
    }
    
    deleteCdnKey().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\DeleteCdnKeyRequest;
    
    /**
     * Deletes a CDN key.
     *
     * @param string $callingProjectId     The project ID to run the API call under
     * @param string $location             The location of the CDN key
     * @param string $cdnKeyId             The ID of the CDN key
     */
    function delete_cdn_key(
        string $callingProjectId,
        string $location,
        string $cdnKeyId
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $formattedName = $stitcherClient->cdnKeyName($callingProjectId, $location, $cdnKeyId);
        $request = (new DeleteCdnKeyRequest())
            ->setName($formattedName);
        $operationResponse = $stitcherClient->deleteCdnKey($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            // Print status
            printf('Deleted CDN key %s' . PHP_EOL, $cdnKeyId);
        } else {
            $error = $operationResponse->getError();
            // handleError($error)
        }
    }

### Python

Before trying this sample, follow the Python setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import argparse
    
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        VideoStitcherServiceClient,
    )
    from google.protobuf import empty_pb2 as empty
    
    
    def delete_cdn_key(project_id: str, location: str, cdn_key_id: str) -> empty.Empty:
        """Deletes a CDN key.
        Args:
            project_id: The GCP project ID.
            location: The location of the CDN key.
            cdn_key_id: The user-defined CDN key ID."""
    
        client = VideoStitcherServiceClient()
    
        name = f"projects/{project_id}/locations/{location}/cdnKeys/{cdn_key_id}"
        operation = client.delete_cdn_key(name=name)
        response = operation.result()
        print("Deleted CDN key")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Delete a CDN key
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param cdn_key_id [String] Your CDN key name (e.g. `my-cdn-key`)
    #
    def delete_cdn_key project_id:, location:, cdn_key_id:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the CDN key.
      name = client.cdn_key_path project: project_id, location: location,
                                 cdn_key: cdn_key_id
    
      # Delete the CDN key.
      operation = client.delete_cdn_key name: name
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print a success message.
      puts "Deleted CDN key"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videostitcherapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
