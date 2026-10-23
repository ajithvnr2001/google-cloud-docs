---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-masking/
title: Character masking \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:21.143222+00:00
---

# Character masking  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-masking/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Character masking Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates masking characters.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [De-identifying sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data)
  * [Transformation reference](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference)



## Code sample

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyWithMasking
    {
        public static DeidentifyContentResponse Deidentify(string projectId, string text)
        {
            // Instantiate a client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct a request.
            var transformation = new InfoTypeTransformations.Types.InfoTypeTransformation
            {
                PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                {
                    CharacterMaskConfig = new [CharacterMaskConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CharacterMaskConfig.html)
                    {
                        MaskingCharacter = "*",
                        NumberToMask = 5,
                        ReverseOrder = false,
                    }
                }
            };
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                InspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
                {
                    InfoTypes =
                    {
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "US_SOCIAL_SECURITY_NUMBER" }
                    }
                },
                DeidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
                {
                    InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                    {
                        Transformations = { transformation }
                    }
                },
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text }
            };
    
            // Call the API.
            var response = dlp.DeidentifyContent(request);
    
            // Inspect the results.
            Console.WriteLine($"Deidentified content: {response.Item.[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)}");
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
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // mask deidentifies the input by masking all provided info types with maskingCharacter
    // and prints the result to w.
    func mask(w io.Writer, projectID, input string, infoTypeNames []string, maskingCharacter string, numberToMask int32) error {
    	// projectID := "my-project-id"
    	// input := "My SSN is 111222333"
    	// infoTypeNames := []string{"US_SOCIAL_SECURITY_NUMBER"}
    	// maskingCharacter := "+"
    	// numberToMask := 6
    	// Will print "My SSN is ++++++333"
    
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
    	// Create a configured request.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes: infoTypes,
    		},
    		DeidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    				InfoTypeTransformations: &dlppb.InfoTypeTransformations{
    					Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    						{
    							InfoTypes: []*dlppb.InfoType{}, // Match all info types.
    							PrimitiveTransformation: &dlppb.PrimitiveTransformation{
    								Transformation: &dlppb.PrimitiveTransformation_CharacterMaskConfig{
    									CharacterMaskConfig: &dlppb.CharacterMaskConfig{
    										MaskingCharacter: maskingCharacter,
    										NumberToMask:     numberToMask,
    									},
    								},
    							},
    						},
    					},
    				},
    			},
    		},
    		// The item to analyze.
    		Item: &dlppb.ContentItem{
    			DataItem: &dlppb.ContentItem_Value{
    				Value: input,
    			},
    		},
    	}
    	// Send the request.
    	r, err := client.DeidentifyContent(ctx, req)
    	if err != nil {
    		return fmt.Errorf("DeidentifyContent: %w", err)
    	}
    	// Print the result.
    	fmt.Fprint(w, r.GetItem().GetValue())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[CharacterMaskConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CharacterMaskConfig.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import java.io.IOException;
    import java.util.Arrays;
    
    public class DeIdentifyWithMasking {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToDeIdentify = "My SSN is 372819127";
        deIdentifyWithMasking(projectId, textToDeIdentify);
      }
    
      public static void deIdentifyWithMasking(String projectId, String textToDeIdentify)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Specify what content you want the service to DeIdentify
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToDeIdentify).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("US_SOCIAL_SECURITY_NUMBER").build();
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addAllInfoTypes(Arrays.asList(infoType)).build();
    
          // Specify how the info from the inspection should be masked.
          [CharacterMaskConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CharacterMaskConfig.html) characterMaskConfig =
              [CharacterMaskConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CharacterMaskConfig.html).newBuilder()
                  .[setMaskingCharacter](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CharacterMaskConfig.Builder.html#com_google_privacy_dlp_v2_CharacterMaskConfig_Builder_setMaskingCharacter_java_lang_String_)("X") // Character to replace the found info with
                  .[setNumberToMask](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CharacterMaskConfig.Builder.html#com_google_privacy_dlp_v2_CharacterMaskConfig_Builder_setNumberToMask_int_)(5) // How many characters should be masked
                  .build();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCharacterMaskConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCharacterMaskConfig_com_google_privacy_dlp_v2_CharacterMaskConfig_)(characterMaskConfig)
                  .build();
          [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
              [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html).newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) transformations =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation).build();
    
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder().setInfoTypeTransformations(transformations).build();
    
          // Combine configurations into a request for the service.
          [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html) request =
              [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(contentItem)
                  .setInspectConfig(inspectConfig)
                  .setDeidentifyConfig(deidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service
          [DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html) response = dlp.deidentifyContent(request);
    
          // Print the results
          System.out.println("Text after masking: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getValue());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project-id';
    
    // The string to deidentify
    // const string = 'My SSN is 372819127';
    
    // (Optional) The maximum number of sensitive characters to mask in a match
    // If omitted from the request or set to 0, the API will mask any matching characters
    // const numberToMask = 5;
    
    // (Optional) The character to mask matching sensitive data with
    // const maskingCharacter = 'x';
    
    // Construct deidentification request
    const item = {value: string};
    
    async function deidentifyWithMask() {
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: {
          infoTypeTransformations: {
            transformations: [
              {
                primitiveTransformation: {
                  characterMaskConfig: {
                    maskingCharacter: maskingCharacter,
                    numberToMask: numberToMask,
                  },
                },
              },
            ],
          },
        },
        item: item,
      };
    
      // Run deidentification request
      const [response] = await dlp.deidentifyContent(request);
      const deidentifiedItem = response.item;
      console.log(deidentifiedItem.value);
    }
    
    deidentifyWithMask();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\CharacterMaskConfig;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    
    /**
     * Deidentify sensitive data in a string by masking it with a character.
     *
     * @param string $callingProjectId The GCP Project ID to run the API call under
     * @param string $string           The string to deidentify
     * @param int    $numberToMask     (Optional) The maximum number of sensitive characters to mask in a match
     * @param string $maskingCharacter (Optional) The character to mask matching sensitive data with (defaults to "x")
     */
    function deidentify_mask(
        string $callingProjectId,
        string $string,
        int $numberToMask = 0,
        string $maskingCharacter = 'x'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // The infoTypes of information to mask
        $ssnInfoType = (new InfoType())
            ->setName('US_SOCIAL_SECURITY_NUMBER');
        $infoTypes = [$ssnInfoType];
    
        // Create the masking configuration object
        $maskConfig = (new CharacterMaskConfig())
            ->setMaskingCharacter($maskingCharacter)
            ->setNumberToMask($numberToMask);
    
        // Create the information transform configuration objects
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCharacterMaskConfig($maskConfig);
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setInfoTypes($infoTypes);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Create the deidentification configuration object
        $deidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations($infoTypeTransformations);
    
        $item = (new ContentItem())
            ->setValue($string);
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Run request
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($item);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print the results
        $deidentifiedValue = $response->getItem()->getValue();
        print($deidentifiedValue);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    import google.cloud.dlp
    
    
    def deidentify_with_mask(
        project: str,
        input_str: str,
        info_types: List[str],
        masking_character: str = None,
        number_to_mask: int = 0,
    ) -> None:
        """Uses the Data Loss Prevention API to deidentify sensitive data in a
        string by masking it with a character.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to deidentify (will be treated as text).
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            masking_character: The character to mask matching sensitive data with.
            number_to_mask: The maximum number of sensitive characters to mask in
                a match. If omitted or set to zero, the API will default to no
                maximum.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Construct inspect configuration dictionary
        inspect_config = {"info_types": [{"name": info_type} for info_type in info_types]}
    
        # Construct deidentify configuration dictionary
        deidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {
                        "primitive_transformation": {
                            "character_mask_config": {
                                "masking_character": masking_character,
                                "number_to_mask": number_to_mask,
                            }
                        }
                    }
                ]
            }
        }
    
        # Construct item
        item = {"value": input_str}
    
        # Call the API
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={
                "parent": parent,
                "deidentify_config": deidentify_config,
                "inspect_config": inspect_config,
                "item": item,
            }
        )
    
        # Print out the results.
        print(response.item.value)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
