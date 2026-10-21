---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-redact-image-colored-infotypes/
title: Redact data from an image with color-coded infoTypes \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:57.253064+00:00
---

# Redact data from an image with color-coded infoTypes  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-redact-image-colored-infotypes/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Redact data from an image with color-coded infoTypes Stay organized with collections  Save and categorize content based on your preferences. 

Redacting infoTypes from an image with color coding.

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
    
    public class RedactImageWithColorCodedInfoTypes
    {
        public static RedactImageResponse RedactImage(
            string projectId,
            string originalImagePath,
            string redactedImagePath)
        {
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the content item by providing the image and its type.
            var byteContentItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
            {
                Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[ImagePng](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_ImagePng),
                Data = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromStream_System_IO_Stream_)(new FileStream(originalImagePath, FileMode.[Open](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.FeatureSet.Types.EnumType.html#Google_Protobuf_Reflection_FeatureSet_Types_EnumType_Open)))
            };
    
            // Define types of info and associate each one with a different color to redact config.
            var ssnRedactionConfig = new RedactImageRequest.Types.ImageRedactionConfig
            {
                InfoType = new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "US_SOCIAL_SECURITY_NUMBER" },
                RedactionColor = new [Color](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Color.html)
                {
                    Red = 0.3f,
                    Green = 0.1f,
                    Blue = 0.6f
                }
            };
    
            var emailRedactionConfig = new RedactImageRequest.Types.ImageRedactionConfig
            {
                InfoType = new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" },
                RedactionColor = new [Color](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Color.html)
                {
                    Red = 0.5f,
                    Green = 0.5f,
                    Blue = 1f
                }
            };
    
            var phoneRedactionConfig = new RedactImageRequest.Types.ImageRedactionConfig
            {
                InfoType = new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_NUMBER" },
                RedactionColor = new [Color](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Color.html)
                {
                    Red = 1f,
                    Green = 0f,
                    Blue = 0.6f
                }
            };
    
            // Construct the Redact request to be sent by the client. Do not specify the type of info to redact.
            var request = new [RedactImageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactImageRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                ImageRedactionConfigs = { ssnRedactionConfig, emailRedactionConfig, phoneRedactionConfig },
                ByteItem = byteContentItem
            };
    
            // Call the API.
            [RedactImageResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactImageResponse.html) response = dlp.RedactImage(request);
    
            // Writes redacted image into file
            response.[RedactedImage](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactImageResponse.html#Google_Cloud_Dlp_V2_RedactImageResponse_RedactedImage).WriteTo(new FileStream(redactedImagePath, FileMode.[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create), FileAccess.Write));
    
            Console.WriteLine($"Redacted image written to: {redactedImagePath}");
    
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
    
    // redactImageFileColoredInfoTypes redacts data from an image with color-coded infoTypes.
    func redactImageFileColoredInfoTypes(w io.Writer, projectID, inputPath, outputPath string) error {
    	// projectId := "my-project-id"
    	// inputPath := "testdata/image.jpg"
    	// outputPath := "testdata/test-output-image-file-colored-infoType.jpeg"
    
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
    
    	// read the image file
    	fileBytes, err := os.ReadFile(inputPath)
    	if err != nil {
    		return err
    	}
    
    	// Specify the content to be redacted.
    	byteItem := &dlppb.ByteContentItem{
    		Type: dlppb.[ByteContentItem_IMAGE_JPEG](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL),
    		Data: fileBytes,
    	}
    
    	// Define types of info to redact associate each one with a different color.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
    
    	ssnRedactionConfig := &dlppb.RedactImageRequest_ImageRedactionConfig{
    		Target: &dlppb.RedactImageRequest_ImageRedactionConfig_InfoType{
    			InfoType: &dlppb.InfoType{
    				Name: "US_SOCIAL_SECURITY_NUMBER",
    			},
    		},
    		RedactionColor: &dlppb.Color{
    			Red:   0.3,
    			Green: 0.1,
    			Blue:  0.6,
    		},
    	}
    
    	emailRedactionConfig := &dlppb.RedactImageRequest_ImageRedactionConfig{
    		Target: &dlppb.RedactImageRequest_ImageRedactionConfig_InfoType{
    			InfoType: &dlppb.InfoType{
    				Name: "EMAIL_ADDRESS",
    			},
    		},
    		RedactionColor: &dlppb.Color{
    			Red:   0.5,
    			Green: 0.5,
    			Blue:  1,
    		},
    	}
    
    	phoneRedactionConfig := &dlppb.RedactImageRequest_ImageRedactionConfig{
    		Target: &dlppb.RedactImageRequest_ImageRedactionConfig_InfoType{
    			InfoType: &dlppb.InfoType{
    				Name: "PHONE_NUMBER",
    			},
    		},
    		RedactionColor: &dlppb.Color{
    			Red:   1,
    			Green: 0,
    			Blue:  0.6,
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.RedactImageRequest{
    		Parent:   fmt.Sprintf("projects/%s/locations/global", projectID),
    		ByteItem: byteItem,
    		ImageRedactionConfigs: []*dlppb.RedactImageRequest_ImageRedactionConfig{
    			emailRedactionConfig,
    			phoneRedactionConfig,
    			ssnRedactionConfig,
    		},
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
    import com.google.privacy.dlp.v2.[Color](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[RedactImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.html);
    import com.google.privacy.dlp.v2.[RedactImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.html).[ImageRedactionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.ImageRedactionConfig.html);
    import com.google.privacy.dlp.v2.[RedactImageResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageResponse.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.FileOutputStream;
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    import java.util.stream.Collectors;
    
    class RedactImageFileColoredInfoTypes {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String inputPath = "src/test/resources/test.png";
        String outputPath = "redacted.png";
        redactImageFileColoredInfoTypes(projectId, inputPath, outputPath);
      }
    
      static void redactImageFileColoredInfoTypes(String projectId, String inputPath, String outputPath)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the content to be redacted.
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) fileBytes = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[readFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_readFrom_java_io_InputStream_)(new FileInputStream(inputPath));
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder().setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).IMAGE_JPEG).[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)(fileBytes).build();
    
          // Define types of info to redact associate each one with a different color.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          [ImageRedactionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.ImageRedactionConfig.html) ssnRedactionConfig =
              [ImageRedactionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.ImageRedactionConfig.html).newBuilder()
                  .setInfoType([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("US_SOCIAL_SECURITY_NUMBER").build())
                  .setRedactionColor([Color](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.html).newBuilder().[setRed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.Builder.html#com_google_privacy_dlp_v2_Color_Builder_setRed_float_)(.3f).[setGreen](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.Builder.html#com_google_privacy_dlp_v2_Color_Builder_setGreen_float_)(.1f).[setBlue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.Builder.html#com_google_privacy_dlp_v2_Color_Builder_setBlue_float_)(.6f).build())
                  .build();
          [ImageRedactionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.ImageRedactionConfig.html) emailRedactionConfig =
              [ImageRedactionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.ImageRedactionConfig.html).newBuilder()
                  .setInfoType([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("EMAIL_ADDRESS").build())
                  .setRedactionColor([Color](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.html).newBuilder().[setRed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.Builder.html#com_google_privacy_dlp_v2_Color_Builder_setRed_float_)(.5f).[setGreen](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.Builder.html#com_google_privacy_dlp_v2_Color_Builder_setGreen_float_)(.5f).[setBlue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.Builder.html#com_google_privacy_dlp_v2_Color_Builder_setBlue_float_)(1).build())
                  .build();
          [ImageRedactionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.ImageRedactionConfig.html) phoneRedactionConfig =
              [ImageRedactionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.ImageRedactionConfig.html).newBuilder()
                  .setInfoType([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PHONE_NUMBER").build())
                  .setRedactionColor([Color](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.html).newBuilder().[setRed](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.Builder.html#com_google_privacy_dlp_v2_Color_Builder_setRed_float_)(1).[setGreen](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.Builder.html#com_google_privacy_dlp_v2_Color_Builder_setGreen_float_)(0).[setBlue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Color.Builder.html#com_google_privacy_dlp_v2_Color_Builder_setBlue_float_)(.6f).build())
                  .build();
    
          // Create collection of all redact configurations.
          List<ImageRedactionConfig> imageRedactionConfigs =
              Arrays.asList(ssnRedactionConfig, emailRedactionConfig, phoneRedactionConfig);
    
          // List types of info to search for.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(
                      imageRedactionConfigs.stream()
                          .map(ImageRedactionConfig::getInfoType)
                          .collect(Collectors.toList()))
                  .build();
    
          // Construct the Redact request to be sent by the client.
          [RedactImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.html) request =
              [RedactImageRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setByteItem(byteItem)
                  .[addAllImageRedactionConfigs](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactImageRequest.Builder.html#com_google_privacy_dlp_v2_RedactImageRequest_Builder_addAllImageRedactionConfigs_java_lang_Iterable___extends_com_google_privacy_dlp_v2_RedactImageRequest_ImageRedactionConfig__)(imageRedactionConfigs)
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
    
    // The local path to save the resulting image to.
    // const outputPath = 'result.png';
    
    async function redactImageColoredInfoType() {
      // Define types of info to redact associate each one with a different color.
      const imageRedactionConfigs = [
        {
          infoType: {name: 'US_SOCIAL_SECURITY_NUMBER'},
          redactionColor: {red: 0.3, green: 0.1, blue: 0.6},
        },
        {
          infoType: {name: 'EMAIL_ADDRESS'},
          redactionColor: {red: 0.5, green: 0.5, blue: 1},
        },
        {
          infoType: {name: 'PHONE_NUMBER'},
          redactionColor: {red: 1, green: 0, blue: 0.6},
        },
      ];
    
      // Load image
      const fileTypeConstant =
        ['image/jpeg', 'image/bmp', 'image/png', 'image/svg'].indexOf(
          mime.getType(filepath)
        ) + 1;
      const fileBytes = Buffer.from(fs.readFileSync(filepath)).toString('base64');
    
      // Construct the Redact request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        byteItem: {
          type: fileTypeConstant,
          data: fileBytes,
        },
        imageRedactionConfigs: imageRedactionConfigs,
      };
    
      // Send the request and receive response from the service.
      const [response] = await dlp.redactImage(request);
      const image = response.redactedImage;
      fs.writeFileSync(outputPath, image);
      console.log(`Saved image redaction results to path: ${outputPath}`);
    }
    redactImageColoredInfoType();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\ByteContentItem;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\Color;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\RedactImageRequest;
    use Google\Cloud\Dlp\V2\RedactImageRequest\ImageRedactionConfig;
    
    /**
     * Redact data from an image with color-coded infoTypes.
     *
     * @param string $callingProjectId    The project ID to run the API call under.
     * @param string $imagePath           The local filepath of the image to inspect.
     * @param string $outputPath          The local filepath to save the resulting image to.
     */
    function redact_image_colored_infotypes(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $imagePath = './test/data/test.png',
        string $outputPath = './test/data/sensitive-data-image-redacted-color-coding.png'
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
    
        // Define the types of information to redact and associate each one with a different color.
        $ssnInfotype = (new InfoType())
            ->setName('US_SOCIAL_SECURITY_NUMBER');
        $emailInfotype = (new InfoType())
            ->setName('EMAIL_ADDRESS');
        $phoneInfotype = (new InfoType())
            ->setName('PHONE_NUMBER');
        $infotypes = [$ssnInfotype, $emailInfotype, $phoneInfotype];
    
        $ssnRedactionConfig = (new ImageRedactionConfig())
            ->setInfoType($ssnInfotype)
            ->setRedactionColor((new Color())
                ->setRed(.3)
                ->setGreen(.1)
                ->setBlue(.6));
    
        $emailRedactionConfig = (new ImageRedactionConfig())
            ->setInfoType($emailInfotype)
            ->setRedactionColor((new Color())
                ->setRed(.5)
                ->setGreen(.5)
                ->setBlue(1));
    
        $phoneRedactionConfig = (new ImageRedactionConfig())
            ->setInfoType($phoneInfotype)
            ->setRedactionColor((new Color())
                ->setRed(1)
                ->setGreen(0)
                ->setBlue(.6));
    
        $imageRedactionConfigs = [$ssnRedactionConfig, $emailRedactionConfig, $phoneRedactionConfig];
    
        // Create the configuration object.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes($infotypes);
        $parent = "projects/$callingProjectId/locations/global";
    
        // Run request.
        $redactImageRequest = (new RedactImageRequest())
            ->setParent($parent)
            ->setByteItem($byteContent)
            ->setInspectConfig($inspectConfig)
            ->setImageRedactionConfigs($imageRedactionConfigs);
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
    
    
    def redact_image_with_colored_info_types(
        project: str,
        filename: str,
        output_filename: str,
    ) -> None:
        """Uses the Data Loss Prevention API to redact protected data in an image by
        color coding the infoTypes.
           Args:
               project: The Google Cloud project id to use as a parent resource.
               filename: The path of the image file to inspect.
               output_filename: The path to which the redacted image will be written.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare image_redaction_configs, a list of dictionaries. Each dictionary
        # contains an infoType and the color used for the replacement.
    
        ssn_redaction_config = {
            "info_type": {"name": "US_SOCIAL_SECURITY_NUMBER"},
            "redaction_color": {
                "red": 0.3,
                "green": 0.1,
                "blue": 0.6,
            },
        }
    
        email_redaction_config = {
            "info_type": {"name": "EMAIL_ADDRESS"},
            "redaction_color": {
                "red": 0.5,
                "green": 0.5,
                "blue": 1.0,
            },
        }
    
        phone_redaction_config = {
            "info_type": {"name": "PHONE_NUMBER"},
            "redaction_color": {
                "red": 1.0,
                "green": 0.0,
                "blue": 0.6,
            },
        }
    
        image_redaction_configs = [
            ssn_redaction_config,
            email_redaction_config,
            phone_redaction_config,
        ]
    
        # Construct the configuration dictionary.
        inspect_config = {"info_types": [_i["info_type"] for _i in image_redaction_configs]}
    
        # Construct the byte_item, containing the file's byte data.
        with open(filename, mode="rb") as f:
            byte_item = {"type_": "IMAGE", "data": f.read()}
    
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
    
        byte_count = len(response.redacted_image)
        print(f"Wrote {byte_count} to {output_filename}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
