---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-redact-image-all-infotypes/
title: Redact sensitive data from an image using default infoTypes \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:24.081712+00:00
---

# Redact sensitive data from an image using default infoTypes  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-redact-image-all-infotypes/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Redact sensitive data from an image using default infoTypes Stay organized with collections  Save and categorize content based on your preferences. 

Redact the default infoTypes from this image.

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
    
    public class RedactSensitiveDataFromImageUsingDefaultInfoTypes
    {
        public static RedactImageResponse RedactImage(
            string projectId,
            string originalImagePath,
            string redactedImagePath)
        {
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the content item.
            var byteContentItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
            {
                Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[ImagePng](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_ImagePng),
                Data = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromStream_System_IO_Stream_)(new FileStream(originalImagePath, FileMode.[Open](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.FeatureSet.Types.EnumType.html#Google_Protobuf_Reflection_FeatureSet_Types_EnumType_Open)))
            };
    
            // Construct the Redact request to be sent by the client. Do not specify the type of info to redact.
            var request = new [RedactImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactImageRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                ByteItem = byteContentItem
            };
    
            // Call the API.
            var response = dlp.RedactImage(request);
    
            // Inspect the response.
            Console.WriteLine($"Redacted image written to: {redactedImagePath}");
    
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
    
    // redactImageFileAllInfoTypes redact sensitive data from an image using default infoTypes.
    func redactImageFileAllInfoTypes(w io.Writer, projectID, inputPath, outputPath string) error {
    	// projectId := "my-project-id"
    	// inputPath := "testdata/image.jpg"
    	// outputPath := "testdata/test-output-image-file-all-infoType.jpeg"
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed,
    	// call the Close method to cleanup its resources.
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return err
    	}
    
    	// Closing the client safely cleans up background resources.
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Read the image file.
    	fileBytes, err := os.ReadFile(inputPath)
    	if err != nil {
    		fmt.Fprintf(w, "os.ReadFile: %v", err)
    		return err
    	}
    
    	// Specify the content to be redacted.
    	byteItem := &dlppb.ByteContentItem{
    		Type: dlppb.[ByteContentItem_IMAGE_JPEG](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL),
    		Data: fileBytes,
    	}
    
    	// Construct the Redact request to be sent by the client.
    	// Do not specify the type of info to redact.
    	req := &dlppb.RedactImageRequest{
    		Parent:   fmt.Sprintf("projects/%s/locations/global", projectID),
    		ByteItem: byteItem,
    	}
    
    	// Send the request.
    	resp, err := client.RedactImage(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Write the output file.
    	if err := os.WriteFile(outputPath, resp.GetRedactedImage(), 0644); err != nil {
    		return err
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
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[RedactImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.html);
    import com.google.privacy.dlp.v2.[RedactImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageResponse.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.FileOutputStream;
    import java.io.IOException;
    
    class RedactImageFileAllInfoTypes {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String inputPath = "src/test/resources/sensitive-data-image.jpeg";
        String outputPath = "sensitive-data-image-redacted.jpeg";
        redactImageFileAllInfoTypes(projectId, inputPath, outputPath);
      }
    
      static void redactImageFileAllInfoTypes(String projectId, String inputPath, String outputPath)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the content to be redacted.
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) fileBytes = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[readFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_readFrom_java_io_InputStream_)(new FileInputStream(inputPath));
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder().setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).IMAGE_JPEG).[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)(fileBytes).build();
    
          // Construct the Redact request to be sent by the client.
          // Do not specify the type of info to redact.
          [RedactImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.html) request =
              [RedactImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setByteItem(byteItem)
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
    
    // The local path to save the resulting image to.
    // const outputPath = 'result.png';
    
    async function redactImage() {
      // Specify the content to be redacted.
      const fileTypeConstant =
        ['image/jpeg', 'image/bmp', 'image/png', 'image/svg'].indexOf(
          mime.getType(filepath)
        ) + 1;
      const fileBytes = Buffer.from(fs.readFileSync(filepath)).toString('base64');
    
      // Construct the Redact request to be sent by the client.
      // Do not specify the type of info to redact.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        byteItem: {
          type: fileTypeConstant,
          data: fileBytes,
        },
      };
    
      // Use the client to send the API request.
      const [response] = await dlp.redactImage(request);
    
      // Parse the response and process results.
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
    use Google\Cloud\Dlp\V2\RedactImageRequest;
    
    /**
     * Redact sensitive data from an image using default infoTypes.
     *
     * @param string $callingProjectId    The project ID to run the API call under.
     * @param string $imagePath           The local filepath of the image to inspect.
     * @param string $outputPath          The local filepath to save the resulting image to.
     */
    function redact_image_all_infotypes(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $imagePath = './test/data/test.png',
        string $outputPath = './test/data/redact_image_all_infotypes.png'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Read image file into a buffer.
        $imageRef = fopen($imagePath, 'rb');
        $imageBytes = fread($imageRef, filesize($imagePath));
        fclose($imageRef);
    
        // Get the image's content type.
        $typeConstant = (int) array_search(
            mime_content_type($imagePath),
            [false, 'image/jpeg', 'image/bmp', 'image/png', 'image/svg']
        );
    
        // Create the byte-storing object.
        $byteContent = (new ByteContentItem())
            ->setType($typeConstant)
            ->setData($imageBytes);
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Run request.
        $redactImageRequest = (new RedactImageRequest())
            ->setParent($parent)
            ->setByteItem($byteContent);
        $response = $dlp->redactImage($redactImageRequest);
    
        // Save result to file.
        file_put_contents($outputPath, $response->getRedactedImage());
    
        // Print completion message.
        printf('Redacted image saved to %s ' . PHP_EOL, $outputPath);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.dlp
    
    
    def redact_image_all_info_types(
        project: str,
        filename: str,
        output_filename: str,
    ) -> None:
        """Uses the Data Loss Prevention API to redact protected data in an image.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            filename: The path to the file to inspect.
            output_filename: The path to which the redacted image will be written.
                A full list of info type categories can be fetched from the API.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the byte_item, containing the file's byte data.
        with open(filename, mode="rb") as f:
            byte_item = {"type_": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[FileType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.FileType.html).IMAGE, "data": f.read()}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[redact_image](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_redact_image)(
            request={
                "parent": parent,
                "byte_item": byte_item,
            }
        )
    
        # Write out the results.
        with open(output_filename, mode="wb") as f:
            f.write(response.redacted_image)
        print(f"Wrote {len(response.redacted_image)} to {output_filename}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
