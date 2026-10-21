---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-redact-image/
title: Redact an image \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:53.744280+00:00
---

# Redact an image  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-redact-image/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Redact an image Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates redacting sensitive data from an image.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Redact sensitive data from images](https://docs.cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System;
    using System.IO;
    
    public class RedactImage
    {
        public static RedactImageResponse Redact(string projectId, string originalImagePath, string redactedImagePath)
        {
            var request = new [RedactImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactImageRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                InspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
                {
                    MinLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Likely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Likely),
                    IncludeQuote = true,
                    InfoTypes =
                    {
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_NUMBER" },
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" },
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "CREDIT_CARD_NUMBER" }
                    }
                },
                ByteItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
                {
                    Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[ImagePng](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_ImagePng),
                    Data = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromStream_System_IO_Stream_)(new FileStream(originalImagePath, FileMode.[Open](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.FeatureSet.Types.EnumType.html#Google_Protobuf_Reflection_FeatureSet_Types_EnumType_Open)))
                },
            };
    
            var client = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
            var response = client.RedactImage(request);
    
            Console.WriteLine($"Extracted text: {response.[ExtractedText](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactImageResponse.html#Google_Cloud_Dlp_V2_RedactImageResponse_ExtractedText)}");
    
            // Writes redacted image into file
            response.[RedactedImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactImageResponse.html#Google_Cloud_Dlp_V2_RedactImageResponse_RedactedImage).WriteTo(new FileStream(redactedImagePath, FileMode.[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create), FileAccess.Write));
    
            return response;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // redactImage blacks out the identified portions of the input image (with type bytesType)
    // and stores the result in outputPath.
    func redactImage(w io.Writer, projectID string, infoTypeNames []string, bytesType dlppb.ByteContentItem_BytesType, inputPath, outputPath string) error {
    	// projectID := "my-project-id"
    	// infoTypeNames := []string{"US_SOCIAL_SECURITY_NUMBER"}
    	// bytesType := dlppb.ByteContentItem_IMAGE_PNG
    	// inputPath := /tmp/input
    	// outputPath := /tmp/output
    
    	ctx := context.Background()
    
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Convert the info type strings to a list of InfoTypes.
    	var infoTypes []*dlppb.InfoType
    	for _, it := range infoTypeNames {
    		infoTypes = append(infoTypes, &dlppb.InfoType{Name: it})
    	}
    
    	// Convert the info type strings to a list of types to redact in the image.
    	var redactInfoTypes []*dlppb.RedactImageRequest_ImageRedactionConfig
    	for _, it := range infoTypeNames {
    		redactInfoTypes = append(redactInfoTypes, &dlppb.RedactImageRequest_ImageRedactionConfig{
    			Target: &dlppb.RedactImageRequest_ImageRedactionConfig_InfoType{
    				InfoType: &dlppb.InfoType{Name: it},
    			},
    		})
    	}
    
    	// Read the input file.
    	b, err := os.ReadFile(inputPath)
    	if err != nil {
    		return fmt.Errorf("os.ReadFile: %w", err)
    	}
    
    	// Create a configured request.
    	req := &dlppb.RedactImageRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes:     infoTypes,
    			MinLikelihood: dlppb.[Likelihood_POSSIBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    		},
    		// The item to analyze.
    		ByteItem: &dlppb.ByteContentItem{
    			Type: bytesType,
    			Data: b,
    		},
    		ImageRedactionConfigs: redactInfoTypes,
    	}
    	// Send the request.
    	resp, err := client.RedactImage(ctx, req)
    	if err != nil {
    		return fmt.Errorf("RedactImage: %w", err)
    	}
    	// Write the output file.
    	if err := os.WriteFile(outputPath, resp.GetRedactedImage(), 0644); err != nil {
    		return fmt.Errorf("os.WriteFile: %w", err)
    	}
    	fmt.Fprintf(w, "Wrote output to %s", outputPath)
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html);
    import com.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).[BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[RedactImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.html);
    import com.google.privacy.dlp.v2.[RedactImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageResponse.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.FileOutputStream;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    class RedactImageFile {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String inputPath = "src/test/resources/test.png";
        String outputPath = "redacted.png";
        redactImageFile(projectId, inputPath, outputPath);
      }
    
      static void redactImageFile(String projectId, String inputPath, String outputPath)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the content to be inspected.
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) fileBytes = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[readFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_readFrom_java_io_InputStream_)(new FileInputStream(inputPath));
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder().setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).IMAGE).[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)(fileBytes).build();
    
          // Specify the type of info and likelihood necessary to redact.
          List<InfoType> infoTypes = new ArrayList<>();
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          for (String typeName : new String[] {"PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER"}) {
            infoTypes.add([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(typeName).build());
          }
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .setMinLikelihood([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).LIKELY)
                  .build();
    
          // Construct the Redact request to be sent by the client.
          [RedactImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.html) request =
              [RedactImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setByteItem(byteItem)
                  .setInspectConfig(config)
                  .build();
    
          // Use the client to send the API request.
          [RedactImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageResponse.html) response = dlp.redactImage(request);
    
          // Parse the response and process results.
          FileOutputStream redacted = new FileOutputStream(outputPath);
          redacted.write(response.[getRedactedImage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageResponse.html#com_google_privacy_dlp_v2_RedactImageResponse_getRedactedImage__)().toByteArray());
          redacted.[close](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html#com_google_cloud_dlp_v2_DlpServiceClient_close__)();
          System.out.println("Redacted image written to " + outputPath);
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Imports required Node.js libraries
    const mime = require('mime');
    const fs = require('fs');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The path to a local file to inspect. Can be a JPG or PNG image file.
    // const filepath = 'path/to/image.png';
    
    // The minimum likelihood required before redacting a match
    // const minLikelihood = 'LIKELIHOOD_UNSPECIFIED';
    
    // The infoTypes of information to redact
    // const infoTypes = [{ name: 'EMAIL_ADDRESS' }, { name: 'PHONE_NUMBER' }];
    
    // The local path to save the resulting image to.
    // const outputPath = 'result.png';
    async function redactImage() {
      const imageRedactionConfigs = infoTypes.map(infoType => {
        return {infoType: infoType};
      });
    
      // Load image
      const fileTypeConstant =
        ['image/jpeg', 'image/bmp', 'image/png', 'image/svg'].indexOf(
          mime.getType(filepath)
        ) + 1;
      const fileBytes = Buffer.from(fs.readFileSync(filepath)).toString('base64');
    
      // Construct image redaction request
      const request = {
        parent: `projects/${projectId}/locations/global`,
        byteItem: {
          type: fileTypeConstant,
          data: fileBytes,
        },
        inspectConfig: {
          minLikelihood: minLikelihood,
          infoTypes: infoTypes,
        },
        imageRedactionConfigs: imageRedactionConfigs,
      };
    
      // Run image redaction request
      const [response] = await dlp.redactImage(request);
      const image = response.redactedImage;
      fs.writeFileSync(outputPath, image);
      console.log(`Saved image redaction results to path: ${outputPath}`);
    }
    redactImage();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\ByteContentItem;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\RedactImageRequest;
    use Google\Cloud\Dlp\V2\RedactImageRequest\ImageRedactionConfig;
    
    /**
     * Redact sensitive data from an image.
     *
     * @param string $callingProjectId    The project ID to run the API call under
     * @param string $imagePath           The local filepath of the image to inspect
     * @param string $outputPath          The local filepath to save the resulting image to
     */
    function redact_image(
        string $callingProjectId,
        string $imagePath,
        string $outputPath
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // The infoTypes of information to match
        $phoneNumberInfoType = (new InfoType())
            ->setName('PHONE_NUMBER');
        $infoTypes = [$phoneNumberInfoType];
    
        // The minimum likelihood required before returning a match
        $minLikelihood = likelihood::LIKELIHOOD_UNSPECIFIED;
    
        // Whether to include the matching string in the response
        $includeQuote = true;
    
        // Create the configuration object
        $inspectConfig = (new InspectConfig())
            ->setMinLikelihood($minLikelihood)
            ->setInfoTypes($infoTypes);
    
        // Read image file into a buffer
        $imageRef = fopen($imagePath, 'rb');
        $imageBytes = fread($imageRef, filesize($imagePath));
        fclose($imageRef);
    
        // Get the image's content type
        $typeConstant = (int) array_search(
            mime_content_type($imagePath),
            [false, 'image/jpeg', 'image/bmp', 'image/png', 'image/svg']
        );
    
        // Create the byte-storing object
        $byteContent = (new ByteContentItem())
            ->setType($typeConstant)
            ->setData($imageBytes);
    
        // Create the image redaction config objects
        $imageRedactionConfigs = [];
        foreach ($infoTypes as $infoType) {
            $config = (new ImageRedactionConfig())
                ->setInfoType($infoType);
            $imageRedactionConfigs[] = $config;
        }
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Run request
        $redactImageRequest = (new RedactImageRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setByteItem($byteContent)
            ->setImageRedactionConfigs($imageRedactionConfigs);
        $response = $dlp->redactImage($redactImageRequest);
    
        // Save result to file
        file_put_contents($outputPath, $response->getRedactedImage());
    
        // Print completion message
        print('Redacted image saved to ' . $outputPath . PHP_EOL);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import mimetypes
    from typing import List
    
    import google.cloud.dlp
    
    
    def redact_image(
        project: str,
        filename: str,
        output_filename: str,
        info_types: List[str],
        min_likelihood: str = None,
        mime_type: str = None,
    ) -> None:
        """Uses the Data Loss Prevention API to redact protected data in an image.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            filename: The path to the file to inspect.
            output_filename: The path to which the redacted image will be written.
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            min_likelihood: A string representing the minimum likelihood threshold
                that constitutes a match. One of: 'LIKELIHOOD_UNSPECIFIED',
                'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY_LIKELY'.
            mime_type: The MIME type of the file. If not specified, the type is
                inferred via the Python standard library's mimetypes module.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries (protos are also accepted).
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Prepare image_redaction_configs, a list of dictionaries. Each dictionary
        # contains an info_type and optionally the color used for the replacement.
        # The color is omitted in this sample, so the default (black) will be used.
        image_redaction_configs = []
    
        if info_types is not None:
            for info_type in info_types:
                image_redaction_configs.append({"info_type": info_type})
    
        # Construct the configuration dictionary. Keys which are None may
        # optionally be omitted entirely.
        inspect_config = {
            "min_likelihood": min_likelihood,
            "info_types": info_types,
        }
    
        # If mime_type is not specified, guess it from the filename.
        if mime_type is None:
            mime_guess = mimetypes.MimeTypes().guess_type(filename)
            mime_type = mime_guess[0] or "application/octet-stream"
    
        # Select the content type index from the list of supported types.
        # https://github.com/googleapis/googleapis/blob/master/google/privacy/dlp/v2/dlp.proto / message ByteContentItem
        supported_content_types = {
            None: 0,  # "Unspecified" or BYTES_TYPE_UNSPECIFIED
            "image/jpeg": 1,  # IMAGE_JPEG
            "image/bmp": 2,  # IMAGE_BMP
            "image/png": 3,  # IMAGE_PNG
            "image/svg": 4,  # IMAGE_SVG - Adjusted to "image/svg+xml" for correct MIME type
            "text/plain": 5,  # TEXT_UTF8
            # Note: No specific MIME type for general "image", mapping to IMAGE for any image type not specified
            "image": 6,  # IMAGE - Any image type
            "application/msword": 7,  # WORD_DOCUMENT
            "application/pdf": 8,  # PDF
            "application/powerpoint": 9,  # POWERPOINT_DOCUMENT
            "application/msexcel": 10,  # EXCEL_DOCUMENT
            "application/avro": 11,  # AVRO
            "text/csv": 12,  # CSV
            "text/tsv": 13,  # TSV
        }
        content_type_index = supported_content_types.get(mime_type, 0)
    
        # Construct the byte_item, containing the file's byte data.
        with open(filename, mode="rb") as f:
            byte_item = {"type_": content_type_index, "data": f.read()}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[redact_image](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_redact_image)(
            request={
                "parent": parent,
                "inspect_config": inspect_config,
                "image_redaction_configs": image_redaction_configs,
                "byte_item": byte_item,
            }
        )
    
        # Write out the results.
        with open(output_filename, mode="wb") as f:
            f.write(response.redacted_image)
        print(
            "Wrote {byte_count} to {filename}".format(
                byte_count=len(response.redacted_image), filename=output_filename
            )
        )
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
