---
url: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-create-cdn-key-akamai/
title: Create a new Akamai CDN key \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:01.035421+00:00
---

# Create a new Akamai CDN key  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-create-cdn-key-akamai/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Samples ](https://docs.cloud.google.com/video-stitcher/docs/samples)



#  Create a new Akamai CDN key Stay organized with collections  Save and categorize content based on your preferences. 

Video assets are usually distributed using a content delivery network, also known as a CDN. To protect the content, video asset URLs can require a signature in order to be retrieved; this is known as URL signing. Create a CDN key to enable API access to the video asset.

## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System.Threading.Tasks;
    
    public class CreateCdnKeyAkamaiSample
    {
        public async Task<CdnKey> CreateCdnKeyAkamaiAsync(
            string projectId, string location, string cdnKeyId, string hostname,
            string akamaiTokenKey)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [CdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKey.html) cdnKey = new [CdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKey.html)
            {
                Hostname = hostname,
                AkamaiCdnKey = new [AkamaiCdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.AkamaiCdnKey.html)
                {
                    TokenKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFromUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFromUtf8_System_String_)(akamaiTokenKey)
                }
            };
    
            [CreateCdnKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateCdnKeyRequest.html) request = new [CreateCdnKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateCdnKeyRequest.html)
            {
                ParentAsLocationName = [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html).[FromProjectLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html#Google_Api_Gax_ResourceNames_LocationName_FromProjectLocation_System_String_System_String_)(projectId, location),
                CdnKeyId = cdnKeyId,
                CdnKey = cdnKey
            };
    
            // Make the request.
            Operation<CdnKey, OperationMetadata> response = await client.[CreateCdnKeyAsync](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_CreateCdnKeyAsync_Google_Api_Gax_ResourceNames_LocationName_Google_Cloud_Video_Stitcher_V1_CdnKey_System_String_Google_Api_Gax_Grpc_CallSettings_)(request);
    
            // Poll until the returned long-running operation is complete.
            Operation<CdnKey, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    
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
    
    // createCDNKeyAkamai creates an Akamai CDN key. A CDN key is used to retrieve
    // protected media.
    func createCDNKeyAkamai(w io.Writer, projectID, keyID, akamaiTokenKey string) error {
    	// projectID := "my-project-id"
    	// keyID := "my-cdn-key"
    	// akamaiTokenKey := "my-private-token-key"
    	location := "us-central1"
    	hostname := "cdn.example.com"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	req := &stitcherstreampb.CreateCdnKeyRequest{
    		Parent:   fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    		CdnKeyId: keyID,
    		CdnKey: &stitcherstreampb.CdnKey{
    			CdnKeyConfig: &stitcherstreampb.CdnKey_AkamaiCdnKey{
    				AkamaiCdnKey: &stitcherstreampb.AkamaiCdnKey{
    					TokenKey: []byte(akamaiTokenKey),
    				},
    			},
    			Hostname: hostname,
    		},
    	}
    
    	// Creates the CDN key.
    	op, err := client.CreateCdnKey(ctx, req)
    	if err != nil {
    		return fmt.Errorf("client.CreateCdnKey: %w", err)
    	}
    	response, err := op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	fmt.Fprintf(w, "CDN key: %v", response.GetName())
    	return nil
    }
    

### Java

Before trying this sample, follow the Java setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/overview). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.video.stitcher.v1.[AkamaiCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.AkamaiCdnKey.html);
    import com.google.cloud.video.stitcher.v1.[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html);
    import com.google.cloud.video.stitcher.v1.[CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest.html);
    import com.google.cloud.video.stitcher.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateCdnKeyAkamai {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String cdnKeyId = "my-cdn-key-id";
        String hostname = "cdn.example.com";
        String akamaiTokenKey = "my-token-key"; // will be converted to a byte string
    
        createCdnKeyAkamai(projectId, location, cdnKeyId, hostname, akamaiTokenKey);
      }
    
      // createCdnKeyAkamai creates an Akamai CDN key. A CDN key is used to retrieve protected media.
      public static [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html) createCdnKeyAkamai(
          String projectId, String location, String cdnKeyId, String hostname, String akamaiTokenKey)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html) cdnKey =
              [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html).newBuilder()
                  .[setHostname](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.Builder.html#com_google_cloud_video_stitcher_v1_CdnKey_Builder_setHostname_java_lang_String_)(hostname)
                  .[setAkamaiCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.Builder.html#com_google_cloud_video_stitcher_v1_CdnKey_Builder_setAkamaiCdnKey_com_google_cloud_video_stitcher_v1_AkamaiCdnKey_)(
                      [AkamaiCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.AkamaiCdnKey.html).newBuilder()
                          .[setTokenKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.AkamaiCdnKey.Builder.html#com_google_cloud_video_stitcher_v1_AkamaiCdnKey_Builder_setTokenKey_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(akamaiTokenKey))
                          .build())
                  .build();
    
          [CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest.html) createCdnKeyRequest =
              [CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html).of(projectId, location).toString())
                  .[setCdnKeyId](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest.Builder.html#com_google_cloud_video_stitcher_v1_CreateCdnKeyRequest_Builder_setCdnKeyId_java_lang_String_)(cdnKeyId)
                  .setCdnKey(cdnKey)
                  .build();
    
          [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html) result =
              videoStitcherServiceClient
                  .[createCdnKeyAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html#com_google_cloud_video_stitcher_v1_VideoStitcherServiceClient_createCdnKeyAsync__org_jspecify_annotations_Nullable_com_google_cloud_video_stitcher_v1_LocationName_com_google_cloud_video_stitcher_v1_CdnKey_java_lang_String_)(createCdnKeyRequest)
                  .get(TIMEOUT_IN_MINUTES, TimeUnit.MINUTES);
          System.out.println("Created new CDN key: " + result.[getName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html#com_google_cloud_video_stitcher_v1_CdnKey_getName__)());
          return result;
        }
      }
    }

### Node.js

Before trying this sample, follow the Node.js setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Node.js API reference documentation](https://cloud.google.com/nodejs/docs/reference/video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const location = 'us-central1';
    const hostname = 'cdn.example.com';
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // cdnKeyId = 'my-cdn-key';
    // akamaiTokenKey = 'my-token-key';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function createCdnKeyAkamai() {
      // Construct request
      const request = {
        parent: stitcherClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location),
        cdnKey: {
          hostname: hostname,
          akamaiCdnKey: {
            tokenKey: akamaiTokenKey,
          },
        },
        cdnKeyId: cdnKeyId,
      };
    
      const [operation] = await stitcherClient.createCdnKey(request);
      const [response] = await operation.promise();
      console.log(`CDN key: ${response.name}`);
    }
    
    createCdnKeyAkamai().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\AkamaiCdnKey;
    use Google\Cloud\Video\Stitcher\V1\CdnKey;
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\CreateCdnKeyRequest;
    
    /**
     * Creates an Akamai CDN key.
     *
     * @param string  $callingProjectId   The project ID to run the API call under
     * @param string  $location           The location of the CDN key
     * @param string  $cdnKeyId           The ID of the CDN key to be created
     * @param string  $hostname           The hostname of the CDN key
     * @param string  $tokenKey           The base64-encoded string token key for
     *                                    the Akamai CDN edge configuration
     */
    function create_cdn_key_akamai(
        string $callingProjectId,
        string $location,
        string $cdnKeyId,
        string $hostname,
        string $tokenKey
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $parent = $stitcherClient->locationName($callingProjectId, $location);
        $cdnKey = new CdnKey();
        $cdnKey->setHostname($hostname);
        $cloudCdn = new AkamaiCdnKey();
        $cloudCdn->setTokenKey($tokenKey);
        $cdnKey->setAkamaiCdnKey($cloudCdn);
    
        // Run CDN key creation request
        $request = (new CreateCdnKeyRequest())
            ->setParent($parent)
            ->setCdnKey($cdnKey)
            ->setCdnKeyId($cdnKeyId);
        $operationResponse = $stitcherClient->createCdnKey($request);
        $operationResponse->pollUntilComplete();
        if ($operationResponse->operationSucceeded()) {
            $result = $operationResponse->getResult();
            // Print results
            printf('CDN key: %s' . PHP_EOL, $result->getName());
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
    
    
    def create_cdn_key_akamai(
        project_id: str,
        location: str,
        cdn_key_id: str,
        hostname: str,
        akamai_token_key: str,
    ) -> stitcher_v1.types.CdnKey:
        """Creates an Akamai CDN key.
        Args:
            project_id: The GCP project ID.
            location: The location in which to create the CDN key.
            cdn_key_id: The user-defined CDN key ID.
            hostname: The hostname to which this CDN key applies.
            akamai_token_key: A base64-encoded string token key.
    
        Returns:
            The CDN key resource.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
    
        cdn_key = stitcher_v1.types.CdnKey(
            name=cdn_key_id,
            hostname=hostname,
            akamai_cdn_key=stitcher_v1.types.AkamaiCdnKey(
                token_key=akamai_token_key,
            ),
        )
    
        operation = client.create_cdn_key(
            parent=parent, cdn_key_id=cdn_key_id, cdn_key=cdn_key
        )
        response = operation.result()
        print(f"CDN key: {response.name}")
        return response
    
    

### Ruby

Before trying this sample, follow the Ruby setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API Ruby API reference documentation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-stitcher/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    require "google/cloud/video/stitcher"
    
    ##
    # Create an Akamai CDN key
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param cdn_key_id [String] The user-defined CDN key ID
    # @param hostname [String] The hostname to which this CDN key applies
    # @param akamai_token_key [String] Applies to an Akamai CDN key. A
    #   base64-encoded string token key.
    #
    def create_cdn_key_akamai project_id:, location:, cdn_key_id:, hostname:,
                              akamai_token_key:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
      # Build the path for the CDN key resource.
      cdn_key_path = client.cdn_key_path project: project_id, location: location,
                                         cdn_key: cdn_key_id
    
      # Set the CDN key fields.
      new_cdn_key = {
        name: cdn_key_path,
        hostname: hostname,
        akamai_cdn_key: {
          token_key: akamai_token_key
        }
      }
    
      operation = client.create_cdn_key parent: parent, cdn_key: new_cdn_key,
                                        cdn_key_id: cdn_key_id
    
      # The returned object is of type Gapic::Operation. You can use this
      # object to check the status of an operation, cancel it, or wait
      # for results. Here is how to block until completion:
      operation.wait_until_done!
    
      # Print the CDN key name.
      puts "CDN key: #{operation.response.name}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videostitcherapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
