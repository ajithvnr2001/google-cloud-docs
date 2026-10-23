---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-image-listed-infotypes/
title: Inspect an image for sensitive data with listed infoTypes \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:37.386030+00:00
---

# Inspect an image for sensitive data with listed infoTypes  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-image-listed-infotypes/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Inspect an image for sensitive data with listed infoTypes Stay organized with collections  Save and categorize content based on your preferences. 

If you want to inspect an image for only certain sensitive data types, specify their corresponding built-in infoTypes.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Inspect images for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-images)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.IO;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    
    public class InspectImageForSensitiveDataWithListedInfoTypes
    {
        public static InspectContentResponse InspectImage(
            string projectId,
            string filePath)
        {
            // Instantiate dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the content item by providing the image file and its type.
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html)
            {
                ByteItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
                {
                    Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[ImagePng](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_ImagePng),
                    Data = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromStream_System_IO_Stream_)(new FileStream(filePath, FileMode.[Open](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Reflection.FeatureSet.Types.EnumType.html#Google_Protobuf_Reflection_FeatureSet_Types_EnumType_Open)))
                }
            };
    
            // Specify the type of info the inspection will look for.
            var infoTypes = new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[]
            {
                new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_NUMBER" },
                new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" },
                new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "US_SOCIAL_SECURITY_NUMBER" }
            };
    
            // Construct the Inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infoTypes },
                IncludeQuote = true
            };
    
            // Construct the request.
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                InspectConfig = inspectConfig,
                Item = contentItem
            };
    
            // Call the API.
            [InspectContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html) response = dlp.InspectContent(request);
    
            // Inspect the response.
            var resultFindings = response.[Result](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html#Google_Cloud_Dlp_V2_InspectContentResponse_Result).Findings;
    
            Console.WriteLine($"Findings: {resultFindings.Count}");
    
            foreach (var f in resultFindings)
            {
                var data = from location in f.[Location](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Location.html).[ContentLocations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Location.html#Google_Cloud_Dlp_V2_Location_ContentLocations)
                           from b in location.[ImageLocation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageLocation.html).[BoundingBoxes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ImageLocation.html#Google_Cloud_Dlp_V2_ImageLocation_BoundingBoxes)
                           select new { b.[Height](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BoundingBox.html#Google_Cloud_Dlp_V2_BoundingBox_Height), b.[Width](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BoundingBox.html#Google_Cloud_Dlp_V2_BoundingBox_Width), b.Top, b.[Left](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BoundingBox.html#Google_Cloud_Dlp_V2_BoundingBox_Left) };
    
                Console.WriteLine("Info type: " + f.[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html).Name);
                Console.WriteLine("\tQuote: " + f.Quote);
                Console.WriteLine("\tImageLocations: " + string.Join(",", data));
                Console.WriteLine("\tLikelihood: " + f.[Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html));
            }
    
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
    
    // inspectImageFileListedInfoTypes inspects an image for sensitive data listed infoTypes.
    func inspectImageFileListedInfoTypes(w io.Writer, projectID, filePath string) error {
    	// projectId := "my-project-id"
    	// filePath := "testdata/image.jpg"
    
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
    
    	// Read a image file
    	data, err := os.ReadFile(filePath)
    	if err != nil {
    		return err
    	}
    
    	// Specify the type and content to be inspected.
    	item := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_ByteItem{
    			ByteItem: &dlppb.ByteContentItem{
    				Type: dlppb.[ByteContentItem_IMAGE_JPEG](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL),
    				Data: data,
    			},
    		},
    	}
    
    	// Construct the configuration for the Inspect request.
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: "PHONE_NUMBER"},
    			{Name: "EMAIL_ADDRESS"},
    			{Name: "US_SOCIAL_SECURITY_NUMBER"},
    		},
    		IncludeQuote: true,
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.InspectContentRequest{
    		Parent:        fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:          item,
    		InspectConfig: inspectConfig,
    	}
    
    	// Send the request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Process the results.
    	fmt.Fprintf(w, "Findings: %d\n", len(resp.Result.Findings))
    	for _, f := range resp.Result.Findings {
    		fmt.Fprintf(w, "\tQuote: %s\n", f.Quote)
    		fmt.Fprintf(w, "\tInfo type: %s\n", f.InfoType.Name)
    		fmt.Fprintf(w, "\tLikelihood: %s\n", f.Likelihood)
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html);
    import com.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).[BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.FileInputStream;
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    class InspectImageFileListedInfoTypes {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "my-project-id";
        String inputPath = "src/test/resources/sensitive-data-image.jpeg";
        inspectImageFileListedInfoTypes(projectId, inputPath);
      }
    
      static void inspectImageFileListedInfoTypes(String projectId, String inputPath)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the content to be inspected.
          [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html) fileBytes = [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[readFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_readFrom_java_io_InputStream_)(new FileInputStream(inputPath));
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder().setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).IMAGE_JPEG).[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)(fileBytes).build();
    
          // Specify the type of info the inspection will look for.
          List<InfoType> infoTypes = new ArrayList<>();
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          for (String typeName :
              new String[] {"US_SOCIAL_SECURITY_NUMBER", "EMAIL_ADDRESS", "PHONE_NUMBER"}) {
            infoTypes.add([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(typeName).build());
          }
    
          // Construct the configuration for the Inspect request.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addAllInfoTypes(infoTypes).build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem([ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build())
                  .setInspectConfig(inspectConfig)
                  .build();
    
          // Use the client to send the API request.
          [InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html) response = dlp.inspectContent(request);
    
          // Parse the response and process results.
          System.out.println("Findings: " + response.[getResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html#com_google_privacy_dlp_v2_InspectContentResponse_getResult__)().getFindingsCount());
          for ([Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html) f : response.[getResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html#com_google_privacy_dlp_v2_InspectContentResponse_getResult__)().getFindingsList()) {
            System.out.println("\tQuote: " + f.getQuote());
            System.out.println("\tInfo type: " + f.getInfoType().getName());
            System.out.println("\tLikelihood: " + f.getLikelihood());
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    const mime = require('mime');
    const fs = require('fs');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const imagePath = './test.pdf';
    
    // InfoTypes
    const infoTypes = [
      {name: 'PHONE_NUMBER'},
      {name: 'EMAIL_ADDRESS'},
      {name: 'US_SOCIAL_SECURITY_NUMBER'},
    ];
    
    async function inspectImageFileListedInfoTypes() {
      let fileBytes = null;
      let fileTypeConstant = null;
      try {
        // Load Image
        fileTypeConstant =
          ['image/jpeg', 'image/bmp', 'image/png', 'image/svg'].indexOf(
            mime.getType(imagePath)
          ) + 1;
        fileBytes = Buffer.from(fs.readFileSync(imagePath)).toString('base64');
      } catch (error) {
        console.log(error);
        return;
      }
      // Specify item to inspect
      const item = {
        byteItem: {
          type: fileTypeConstant,
          data: fileBytes,
        },
      };
    
      // Specify inspect configuration to match information with mentioned infotypes.
      const inspectConfig = {
        infoTypes: infoTypes,
        includeQuote: true,
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: inspectConfig,
        item: item,
      };
    
      // Use the client to send the request.
      const [response] = await dlp.inspectContent(request);
    
      // Print Findings
      const findings = response.result.findings;
      if (findings.length > 0) {
        console.log(`Findings: ${findings.length}\n`);
        findings.forEach(finding => {
          console.log(`InfoType: ${finding.infoType.name}`);
          console.log(`\tQuote: ${finding.quote}`);
          console.log(`\tLikelihood: ${finding.likelihood} \n`);
        });
      } else {
        console.log('No findings.');
      }
    }
    inspectImageFileListedInfoTypes();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\ByteContentItem;
    use Google\Cloud\Dlp\V2\ByteContentItem\BytesType;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\Likelihood;
    
    /**
     * Inspect an image for sensitive data with listed infoTypes.
     * If you want to inspect an image for only certain sensitive data types, specify their corresponding
     * built-in infoTypes.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     * @param string $inputPath         The image path to inspect.
     */
    function inspect_image_listed_infotypes(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $inputPath = './test/data/test.png'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Get the bytes of the file.
        $fileBytes = (new ByteContentItem())
            ->setType(BytesType::IMAGE_PNG)
            ->setData(file_get_contents($inputPath));
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new ContentItem())
            ->setByteItem($fileBytes);
    
        // Create inspect config configuration.
        $inspectConfig = (new InspectConfig())
            // The infoTypes of information to match.
            ->setInfoTypes([
                (new InfoType())->setName('PHONE_NUMBER'),
                (new InfoType())->setName('EMAIL_ADDRESS'),
                (new InfoType())->setName('US_SOCIAL_SECURITY_NUMBER')
            ]);
    
        // Run request.
        $inspectContentRequest = (new InspectContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->inspectContent($inspectContentRequest);
    
        // Print the results.
        $findings = $response->getResult()->getFindings();
        if (count($findings) == 0) {
            printf('No findings.' . PHP_EOL);
        } else {
            printf('Findings:' . PHP_EOL);
            foreach ($findings as $finding) {
                printf('  Info type: %s' . PHP_EOL, $finding->getInfoType()->getName());
                printf('  Likelihood: %s' . PHP_EOL, Likelihood::name($finding->getLikelihood()));
            }
        }
    }
    

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    import google.cloud.dlp
    
    
    def inspect_image_file_listed_infotypes(
        project: str,
        filename: str,
        info_types: List[str],
        include_quote: bool = True,
    ) -> None:
        """Uses the Data Loss Prevention API to analyze strings in an image for
        data matching the given infoTypes.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            filename: The path of the image file to inspect.
            info_types:  A list of strings representing infoTypes to look for.
                A full list of info type categories can be fetched from the API.
            include_quote: Boolean for whether to display a matching snippet of
                the detected information in the results.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries.
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Construct the configuration dictionary.
        inspect_config = {
            "info_types": info_types,
            "include_quote": include_quote,
        }
    
        # Construct the byte_item, containing the image file's byte data.
        with open(filename, mode="rb") as f:
            byte_item = {"type_": "IMAGE", "data": f.read()}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={
                "parent": parent,
                "inspect_config": inspect_config,
                "item": {"byte_item": byte_item},
            }
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Info type: {finding.info_type.name}")
                if include_quote:
                    print(f"Quote: {finding.quote}")
                print(f"Likelihood: {finding.likelihood} \n")
        else:
            print("No findings.")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
