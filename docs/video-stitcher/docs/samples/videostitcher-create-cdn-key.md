---
url: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-create-cdn-key/
title: Create a new CDN key \u00a0|\u00a0 Video Stitcher API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:01:18.819505+00:00
---

# Create a new CDN key  |  Video Stitcher API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-stitcher/docs/samples/videostitcher-create-cdn-key/

To enable the Video Stitcher API for your project, please reach out to your Account Representative or contact [Sales](https://cloud.google.com/contact) to learn more. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Stitcher API ](https://docs.cloud.google.com/video-stitcher/docs)
  * [ Samples ](https://docs.cloud.google.com/video-stitcher/docs/samples)



#  Create a new CDN key Stay organized with collections  Save and categorize content based on your preferences. 

Video assets are usually distributed using a content delivery network, also known as a CDN. To protect the content, video asset URLs can require a signature in order to be retrieved; this is known as URL signing. Create a CDN key to enable API access to the video asset.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create and manage CDN keys](https://docs.cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys)
  * [Insert ads into livestreams](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-live)
  * [Insert ads into VOD assets](https://docs.cloud.google.com/video-stitcher/docs/quickstarts/inserting-ads-into-vod)



## Code sample

### C#

Before trying this sample, follow the C# setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API C# API reference documentation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.html);
    using [Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System.Threading.Tasks;
    
    public class CreateCdnKeySample
    {
        public async Task<CdnKey> CreateCdnKeyAsync(
        string projectId, string location, string cdnKeyId, string hostname,
        string keyName, string privateKey, bool isMediaCdn)
        {
            // Create the client.
            [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html) client = [VideoStitcherServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VideoStitcherServiceClient.html#Google_Cloud_Video_Stitcher_V1_VideoStitcherServiceClient_Create)();
    
            [CdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKey.html) cdnKey = new [CdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKey.html)
            {
                Hostname = hostname
            };
    
            if (isMediaCdn)
            {
                cdnKey.[MediaCdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKey.html#Google_Cloud_Video_Stitcher_V1_CdnKey_MediaCdnKey) = new [MediaCdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.MediaCdnKey.html)
                {
                    KeyName = keyName,
                    PrivateKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFromUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFromUtf8_System_String_)(privateKey)
                };
            }
            else
            {
                cdnKey.[GoogleCdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CdnKey.html#Google_Cloud_Video_Stitcher_V1_CdnKey_GoogleCdnKey) = new [GoogleCdnKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.GoogleCdnKey.html)
                {
                    KeyName = keyName,
                    PrivateKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFromUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFromUtf8_System_String_)(privateKey)
                };
            }
    
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
    
    // createCDNKey creates a CDN key. A CDN key is used to retrieve protected media.
    // If isMediaCDN is true, create a Media CDN key. If false, create a Cloud
    // CDN key. To create a privateKey value for Media CDN, see
    // https://cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn.
    func createCDNKey(w io.Writer, projectID, keyID, privateKey string, isMediaCDN bool) error {
    	// projectID := "my-project-id"
    	// keyID := "my-cdn-key"
    	// privateKey := "my-private-key"
    	// isMediaCDN := true
    	location := "us-central1"
    	hostname := "cdn.example.com"
    	keyName := "cdn-key"
    	ctx := context.Background()
    	client, err := stitcher.[NewVideoStitcherClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_NewVideoStitcherClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("stitcher.NewVideoStitcherClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/video/latest/stitcher/apiv1.html#cloud_google_com_go_video_stitcher_apiv1_VideoStitcherClient_Close)()
    
    	var req *stitcherstreampb.CreateCdnKeyRequest
    	if isMediaCDN {
    		req = &stitcherstreampb.CreateCdnKeyRequest{
    			Parent:   fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    			CdnKeyId: keyID,
    			CdnKey: &stitcherstreampb.CdnKey{
    				CdnKeyConfig: &stitcherstreampb.CdnKey_MediaCdnKey{
    					MediaCdnKey: &stitcherstreampb.MediaCdnKey{
    						KeyName:    keyName,
    						PrivateKey: []byte(privateKey),
    					},
    				},
    				Hostname: hostname,
    			},
    		}
    	} else {
    		req = &stitcherstreampb.CreateCdnKeyRequest{
    			Parent:   fmt.Sprintf("projects/%s/locations/%s", projectID, location),
    			CdnKeyId: keyID,
    			CdnKey: &stitcherstreampb.CdnKey{
    				CdnKeyConfig: &stitcherstreampb.CdnKey_GoogleCdnKey{
    					GoogleCdnKey: &stitcherstreampb.GoogleCdnKey{
    						KeyName:    keyName,
    						PrivateKey: []byte(privateKey),
    					},
    				},
    				Hostname: hostname,
    			},
    		}
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
    
    
    import com.google.cloud.video.stitcher.v1.[CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html);
    import com.google.cloud.video.stitcher.v1.[CreateCdnKeyRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CreateCdnKeyRequest.html);
    import com.google.cloud.video.stitcher.v1.[GoogleCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GoogleCdnKey.html);
    import com.google.cloud.video.stitcher.v1.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.LocationName.html);
    import com.google.cloud.video.stitcher.v1.[MediaCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.MediaCdnKey.html);
    import com.google.cloud.video.stitcher.v1.[VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    import java.util.concurrent.TimeUnit;
    import java.util.concurrent.TimeoutException;
    
    public class CreateCdnKey {
    
      private static final int TIMEOUT_IN_MINUTES = 2;
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String location = "us-central1";
        String cdnKeyId = "my-cdn-key-id";
        String hostname = "cdn.example.com";
        String keyName = "my-key";
        // To create a privateKey value for Media CDN, see
        // https://cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn.
        String privateKey = "my-private-key"; // will be converted to a byte string
        Boolean isMediaCdn = true;
    
        createCdnKey(projectId, location, cdnKeyId, hostname, keyName, privateKey, isMediaCdn);
      }
    
      // createCdnKey creates a Media CDN key or a Cloud CDN key. A CDN key is used to retrieve
      // protected media.
      public static [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html) createCdnKey(
          String projectId,
          String location,
          String cdnKeyId,
          String hostname,
          String keyName,
          String privateKey,
          Boolean isMediaCdn)
          throws IOException, ExecutionException, InterruptedException, TimeoutException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests.
        try ([VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html) videoStitcherServiceClient =
            [VideoStitcherServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.VideoStitcherServiceClient.html).create()) {
          [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html) cdnKey;
          if (isMediaCdn) {
            cdnKey =
                [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html).newBuilder()
                    .[setHostname](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.Builder.html#com_google_cloud_video_stitcher_v1_CdnKey_Builder_setHostname_java_lang_String_)(hostname)
                    .[setMediaCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.Builder.html#com_google_cloud_video_stitcher_v1_CdnKey_Builder_setMediaCdnKey_com_google_cloud_video_stitcher_v1_MediaCdnKey_)(
                        [MediaCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.MediaCdnKey.html).newBuilder()
                            .setKeyName(keyName)
                            .setPrivateKey([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(privateKey))
                            .build())
                    .build();
          } else {
            cdnKey =
                [CdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.html).newBuilder()
                    .[setHostname](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.Builder.html#com_google_cloud_video_stitcher_v1_CdnKey_Builder_setHostname_java_lang_String_)(hostname)
                    .[setGoogleCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.CdnKey.Builder.html#com_google_cloud_video_stitcher_v1_CdnKey_Builder_setGoogleCdnKey_com_google_cloud_video_stitcher_v1_GoogleCdnKey_)(
                        [GoogleCdnKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-video-stitcher/latest/com.google.cloud.video.stitcher.v1.GoogleCdnKey.html).newBuilder()
                            .setKeyName(keyName)
                            .setPrivateKey([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(privateKey))
                            .build())
                    .build();
          }
    
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
    const keyName = 'cdn-key';
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // projectId = 'my-project-id';
    // cdnKeyId = 'my-cdn-key';
    // privateKey = 'my-private-key';
    
    // Imports the Video Stitcher library
    const {VideoStitcherServiceClient} =
      require('[@google-cloud/video-stitcher](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)').v1;
    // Instantiates a client
    const stitcherClient = new [VideoStitcherServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/overview.html)();
    
    async function createCdnKey() {
      // Construct request
      const request = {
        parent: stitcherClient.[locationPath](https://docs.cloud.google.com/nodejs/docs/reference/video-stitcher/latest/video-stitcher/v1.videostitcherserviceclient.html)(projectId, location),
        cdnKey: {
          hostname: hostname,
        },
        cdnKeyId: cdnKeyId,
      };
    
      if (isMediaCdn === 'true') {
        request.cdnKey.mediaCdnKey = {
          keyName: keyName,
          privateKey: privateKey,
        };
      } else {
        request.cdnKey.googleCdnKey = {
          keyName: keyName,
          privateKey: privateKey,
        };
      }
    
      const [operation] = await stitcherClient.createCdnKey(request);
      const [response] = await operation.promise();
      console.log(`CDN key: ${response.name}`);
    }
    
    createCdnKey().catch(err => {
      console.error(err.message);
      process.exitCode = 1;
    });

### PHP

Before trying this sample, follow the PHP setup instructions in the [Video Stitcher API quickstart using client libraries](https://docs.cloud.google.com/video-stitcher/docs/reference/libraries). For more information, see the [Video Stitcher API PHP API reference documentation](https://googleapis.github.io/google-cloud-php/#/docs/google-cloud/latest/videostitcher/readme). 

To authenticate to Video Stitcher API, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Video\Stitcher\V1\CdnKey;
    use Google\Cloud\Video\Stitcher\V1\Client\VideoStitcherServiceClient;
    use Google\Cloud\Video\Stitcher\V1\CreateCdnKeyRequest;
    use Google\Cloud\Video\Stitcher\V1\GoogleCdnKey;
    use Google\Cloud\Video\Stitcher\V1\MediaCdnKey;
    
    /**
     * Creates a CDN key. Cloud CDN keys and Media CDN keys are supported.
     *
     * @param string  $callingProjectId   The project ID to run the API call under
     * @param string  $location           The location of the CDN key
     * @param string  $cdnKeyId           The ID of the CDN key to be created
     * @param string  $hostname           The hostname of the CDN key
     * @param string  $keyName            For a Media CDN key, this is the keyset name.
     *                                    For a Cloud CDN key, this is the public name of the
     *                                    CDN key.
     * @param string  $privateKey         For a Media CDN key, this is a 64-byte Ed25519 private
     *                                    key encoded as a base64-encoded string. See
     *                                    https://cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn
     *                                    for more information. For a Cloud CDN key,
     *                                    this is a base64-encoded string secret.
     * @param bool    $isMediaCdn         If true, create a Media CDN key. If false,
     *                                    create a Cloud CDN key.
     */
    function create_cdn_key(
        string $callingProjectId,
        string $location,
        string $cdnKeyId,
        string $hostname,
        string $keyName,
        string $privateKey,
        bool $isMediaCdn
    ): void {
        // Instantiate a client.
        $stitcherClient = new VideoStitcherServiceClient();
    
        $parent = $stitcherClient->locationName($callingProjectId, $location);
        $cdnKey = new CdnKey();
        $cdnKey->setHostname($hostname);
    
        if ($isMediaCdn == true) {
            $cloudCdn = new MediaCdnKey();
            $cdnKey->setMediaCdnKey($cloudCdn);
        } else {
            $cloudCdn = new GoogleCdnKey();
            $cdnKey->setGoogleCdnKey($cloudCdn);
        }
        $cloudCdn->setKeyName($keyName);
        $cloudCdn->setPrivateKey($privateKey);
    
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
    
    from google.cloud.video import [stitcher_v1](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest)
    from google.cloud.video.stitcher_v1.services.video_stitcher_service import (
        [VideoStitcherServiceClient](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.services.video_stitcher_service.VideoStitcherServiceClient.html),
    )
    
    
    def create_cdn_key(
        project_id: str,
        location: str,
        cdn_key_id: str,
        hostname: str,
        key_name: str,
        private_key: str,
        is_cloud_cdn: bool,
    ) -> stitcher_v1.types.CdnKey:
        """Creates a Cloud CDN or Media CDN key.
        Args:
            project_id: The GCP project ID.
            location: The location in which to create the CDN key.
            cdn_key_id: The user-defined CDN key ID.
            hostname: The hostname to which this CDN key applies.
            key_name: For a Media CDN key, this is the keyset name.
                      For a Cloud CDN key, this is the public name of the CDN key.
            private_key: For a Media CDN key, this is a 64-byte Ed25519 private
                         key encoded as a base64-encoded string.
                         See https://cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn
                         for more information. For a Cloud CDN key, this is a base64-encoded string secret.
            is_cloud_cdn: If true, create a Cloud CDN key. If false, create a Media CDN key.
    
        Returns:
            The CDN key resource.
        """
    
        client = VideoStitcherServiceClient()
    
        parent = f"projects/{project_id}/locations/{location}"
    
        cdn_key = [stitcher_v1](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest).[types](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.html).[CdnKey](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.CdnKey.html)(
            name=cdn_key_id,
            hostname=hostname,
        )
    
        if is_cloud_cdn:
            cdn_key.google_cdn_key = [stitcher_v1](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest).[types](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.html).[GoogleCdnKey](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.GoogleCdnKey.html)(
                key_name=key_name,
                private_key=private_key,
            )
        else:
            cdn_key.media_cdn_key = [stitcher_v1](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest).[types](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.html).[MediaCdnKey](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.types.MediaCdnKey.html)(
                key_name=key_name,
                private_key=private_key,
            )
    
        operation = client.[create_cdn_key](https://docs.cloud.google.com/python/docs/reference/videostitcher/latest/google.cloud.video.stitcher_v1.services.video_stitcher_service.VideoStitcherServiceClient.html#google_cloud_video_stitcher_v1_services_video_stitcher_service_VideoStitcherServiceClient_create_cdn_key)(
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
    # Create a Media CDN or Cloud CDN key
    #
    # @param project_id [String] Your Google Cloud project (e.g. `my-project`)
    # @param location [String] The location (e.g. `us-central1`)
    # @param cdn_key_id [String] The user-defined CDN key ID
    # @param hostname [String] The hostname to which this CDN key applies
    # @param key_name [String] For a Media CDN key, this is the keyset name.
    #   For a Cloud CDN key, this is the public name of the CDN key.
    # @param private_key [String] For a Media CDN key, this is a 64-byte Ed25519
    #   private key encoded as a base64-encoded string. See
    #   https://cloud.google.com/video-stitcher/docs/how-to/managing-cdn-keys#create-private-key-media-cdn
    #   for more information. For a Cloud CDN key, this is a base64-encoded string
    #   secret.
    # @param is_media_cdn [Boolean] If true, create a Media CDN key. If false,
    #  create a Cloud CDN key.
    #
    def create_cdn_key project_id:, location:, cdn_key_id:, hostname:, key_name:,
                       private_key:, is_media_cdn:
      # Create a Video Stitcher client.
      client = Google::Cloud::Video::Stitcher.video_stitcher_service
    
      # Build the resource name of the parent.
      parent = client.location_path project: project_id, location: location
      # Build the path for the CDN key resource.
      cdn_key_path = client.cdn_key_path project: project_id, location: location,
                                         cdn_key: cdn_key_id
    
      # Set the CDN key fields.
      new_cdn_key = if is_media_cdn
                      {
                        name: cdn_key_path,
                        hostname: hostname,
                        media_cdn_key: {
                          key_name: key_name,
                          private_key: private_key
                        }
                      }
                    else
                      {
                        name: cdn_key_path,
                        hostname: hostname,
                        google_cdn_key: {
                          key_name: key_name,
                          private_key: private_key
                        }
                      }
                    end
    
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
