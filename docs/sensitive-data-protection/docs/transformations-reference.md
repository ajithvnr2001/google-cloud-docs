---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference/
title: Transformation reference \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:54.831639+00:00
---

# Transformation reference  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Transformation reference Stay organized with collections  Save and categorize content based on your preferences. 

This topic covers the available de-identification techniques, or transformations, in Sensitive Data Protection.

## Types of de-identification techniques

Choosing the de-identification transformation you want to use depends on the kind of data you want to de-identify and for what purpose you're de-identifying the data. The de-identification techniques that Sensitive Data Protection supports fall into the following general categories:

  * Redaction: Deletes all or part of a detected sensitive value.
  * Replacement: Replaces a detected sensitive value with a specified surrogate value.
  * Masking: Replaces a number of characters of a sensitive value with a specified surrogate character, such as a hash (#) or asterisk (*).
  * Crypto-based tokenization: Encrypts the original sensitive data value using a cryptographic key. Sensitive Data Protection supports several types of tokenization, including transformations that can be reversed, or "re-identified."
  * Bucketing: "Generalizes" a sensitive value by replacing it with a range of values. (For example, replacing a specific age with an age range, or temperatures with ranges corresponding to "Hot," "Medium," and "Cold.")
  * Date shifting: Shifts sensitive date values by a random amount of time.
  * Time extraction: Extracts or preserves specified portions of date and time values.



The remainder of this topic covers each different type of de-identification transformation and provides examples of their use.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

## Transformation methods

The following table lists the transformations that Sensitive Data Protection provides to de-identify sensitive data:

Transformation | Object | Description | Can Reverse1 | Referential Integrity2 | Input Type  
---|---|---|---|---|---  
Redaction | `RedactConfig` | Redacts a value by removing it. |  |  | Any  
Replacement | `ReplaceValueConfig` | Replaces each input value with a given value. |  |  | Any  
Replace with dictionary | `ReplaceDictionaryConfig ` | Replaces an input value with a value that is randomly selected from a word list. |  |  | Any  
Replace with infoType | `ReplaceWithInfoTypeConfig` | Replaces an input value with the name of its infoType. |  |  | Any  
Mask with character | `CharacterMaskConfig` | Masks a string either fully or partially by replacing a given number of characters with a specified fixed character. |  |  | Any  
Pseudonymization by replacing input value with cryptographic hash | `CryptoHashConfig` | Replaces input values with a 32-byte hexadecimal string generated using a given data encryption key. See [pseudonymization conceptual documentation](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization) to learn more. |  | ✔ | Strings or integers  
Pseudonymization by replacing with cryptographic format preserving token | `CryptoReplaceFfxFpeConfig` |  Important: Don't use the `CryptoReplaceFfxFpeConfig` method, except when preserving the input alphabet space and size is a requirement. The `CryptoReplaceFfxFpeConfig` method can run very slowly, and it has limitations on the size of the alphabet and number of tokens, making it less flexible than using the `CryptoDeterministicConfig` method. The `CryptoDeterministicConfig` method has no limitations on the input and is much faster. To learn more, see [Pseudonymization](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization).  Replaces an input value with a token, or surrogate value, of the same length using format-preserving encryption (FPE) with the FFX mode of operation. This allows the output to be used in systems that have format validation on length. This is useful for legacy systems where string length must be maintained. Important: For input that varies in length or has length greater than 32 bytes, use `CryptoDeterministicConfig`. To remain secure the following limits are recommended by the [ National Institute of Standards and Technology](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38G.pdf): 

  * radix^max_size <= 2^128.
  * radix^min_len >= 100

| ✔ | ✔ | Strings or integers with a limited number of characters and of uniform length. The alphabet must be made up of at least 2 characters and contain no more than 95.   
Pseudonymization by replacing with cryptographic token | `CryptoDeterministicConfig` | Replaces an input value with a token, or surrogate value, of the same length using [AES in Synthetic Initialization Vector mode (AES-SIV)](https://tools.ietf.org/html/rfc5297). This transformation method, unlike format-preserving tokenization, has no limitation on supported string character sets, generates identical tokens for each instance of an identical input value, and uses [surrogates](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#surrogatetype) to enable re-identification given the original encryption key. | ✔ | ✔ | Any  
Bucket values based on fixed size ranges | `FixedSizeBucketingConfig` | Masks input values by replacing them with buckets, or ranges within which the input value falls. |  |  | Any  
Bucket values based on custom size ranges | `BucketingConfig` | Buckets input values based on user-configurable ranges and replacement values. |  |  | Any  
Date Shifting | `DateShiftConfig` | Shifts dates by a random number of days, with the option to be consistent for the same context. |  | ✔   
Preserves sequence and duration | Dates/Times  
Extract time data | `TimePartConfig` | Extracts or preserves a portion of `Date`, `Timestamp`, and `TimeOfDay` values. |  |  | Dates/Times  
  
#### Footnotes

1 Reversible transformations can be reversed to re-identify the sensitive data using the [`content.reidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/reidentify) method. 

2 Referential integrity allows for records to maintain their relationship to one another while still de-identifying the data. For example, given the same crypto key and context, the data will be replaced with the same obfuscuted form each time it is transformed allowing for connections between records to be preserved. 

### Redaction

If you want to simply remove sensitive data from your input content, Sensitive Data Protection supports a redaction transformation ([`RedactConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#redactconfig) in the DLP API).

For example, suppose you want to perform a simple redaction of all `EMAIL_ADDRESS` infoTypes, and the following string is sent to Sensitive Data Protection:
    
    
    My name is Alicia Abernathy, and my email address is aabernathy@example.com.

The returned string will be the following:
    
    
    My name is Alicia Abernathy, and my email address is .

The following JSON example and code in several languages shows how to form the API request and what the DLP API returns.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyDataUsingRedactWithMatchedInputValues
    {
        public static DeidentifyContentResponse Deidentify(
            string projectId,
            string text,
            IEnumerable<InfoType> infoTypes = null)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[] { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" } } },
            };
    
            // Construct redact config.
            var redactConfig = new [RedactConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RedactConfig.html)();
    
            // Construct deidentify config using redact config.
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations =
                    {
                        new InfoTypeTransformations.Types.InfoTypeTransformation
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                RedactConfig = redactConfig
                            }
                        }
                    }
                }
            };
    
            // Construct a request.
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                DeidentifyConfig = deidentifyConfig,
                InspectConfig = inspectConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text }
            };
    
            // Call the API.
            var response = dlp.DeidentifyContent(request);
    
            // Check the deidentified content.
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
    
    // deidentifyWithRedact de-identify the data by redacting with matched input values
    func deidentifyWithRedact(w io.Writer, projectID, inputStr string, infoTypeNames []string) error {
    	// projectID := "my-project-id"
    	// inputStr := "My name is Alicia Abernathy, and my email address is aabernathy@example.com."
    	// infoTypeNames := []string{"EMAIL_ADDRESS"}
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed,
    	// call the Close method to cleanup its resources.
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    
    	// Closing the client safely cleans up background resources.
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Specify the content to be inspected.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{
    			Value: inputStr,
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	var infoTypes []*dlppb.InfoType
    	for _, it := range infoTypeNames {
    		infoTypes = append(infoTypes, &dlppb.InfoType{Name: it})
    	}
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes: infoTypes,
    	}
    
    	// Define type of de-identification.
    	primitiveTransformation := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_RedactConfig{
    			RedactConfig: &dlppb.RedactConfig{},
    		},
    	}
    
    	// Associate de-identification type with info type.
    	transformation := &dlppb.InfoTypeTransformations_InfoTypeTransformation{
    		InfoTypes:               infoTypes,
    		PrimitiveTransformation: primitiveTransformation,
    	}
    
    	// Construct the configuration for the Redact request and list all desired transformations.
    	redactConfig := &dlppb.DeidentifyConfig{
    		Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    			InfoTypeTransformations: &dlppb.InfoTypeTransformations{
    				Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    					transformation,
    				},
    			},
    		},
    	}
    
    	// Create a configured request.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: redactConfig,
    		InspectConfig:    inspectConfig,
    		Item:             contentItem,
    	}
    
    	// Send the request.
    	resp, err := client.DeidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result.
    	fmt.Fprintf(w, "output: %v", resp.GetItem().GetValue())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
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
    import com.google.privacy.dlp.v2.[RedactConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactConfig.html);
    
    public class DeIdentifyWithRedaction {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect =
            "My name is Alicia Abernathy, and my email address is aabernathy@example.com.";
        deIdentifyWithRedaction(projectId, textToInspect);
      }
    
      // Inspects the provided text.
      public static void deIdentifyWithRedaction(String projectId, String textToRedact) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the content to be inspected.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToRedact).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("EMAIL_ADDRESS").build();
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addInfoTypes(infoType).build();
          // Define type of deidentification.
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setRedactConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setRedactConfig_com_google_privacy_dlp_v2_RedactConfig_)([RedactConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RedactConfig.html).getDefaultInstance())
                  .build();
          // Associate deidentification type with info type.
          [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) transformation =
              [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html).newBuilder()
                  .addInfoTypes(infoType)
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
          // Construct the configuration for the Redact request and list all desired transformations.
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) redactConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder()
                  .setInfoTypeTransformations(
                      [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(transformation))
                  .build();
    
          // Construct the Redact request to be sent by the client.
          [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html) request =
              [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setDeidentifyConfig(redactConfig)
                  .setInspectConfig(inspectConfig)
                  .build();
    
          // Use the client to send the API request.
          [DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html) response = dlp.deidentifyContent(request);
    
          // Parse the response and process results
          System.out.println("Text after redaction: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getValue());
        } catch (Exception e) {
          System.out.println("Error during inspectString: \n" + e.toString());
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
    
    // TODO(developer): Replace these variables before running the sample.
    // const projectId = "your-project-id";
    
    // The string to deidentify
    // const string =
    //   'My name is Alicia Abernathy, and my email address is aabernathy@example.com.';
    
    // The infoTypes of information to match
    // See https://cloud.google.com/dlp/docs/concepts-infotypes for more information
    // about supported infoTypes.
    // const infoTypes = [{name: 'EMAIL_ADDRESS'}];
    
    async function deIdentifyRedaction() {
      // Construct deidentify configuration
      const deidentifyConfig = {
        infoTypeTransformations: {
          transformations: [
            {
              infoTypes: infoTypes,
              primitiveTransformation: {
                redactConfig: {},
              },
            },
          ],
        },
      };
    
      // Construct inspect configuration
      const inspectConfig = {
        infoTypes: infoTypes,
      };
    
      // Construct Item
      const item = {
        value: string,
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        item,
        deidentifyConfig,
        inspectConfig,
      };
    
      // Send the request and receive response from the service
      const [response] = await dlp.deidentifyContent(request);
    
      // Print the results
      console.log(`Text after redaction: ${response.item.value}`);
    }
    
    deIdentifyRedaction();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\RedactConfig;
    
    /**
     * De-identify data: Redacting with matched input values
     * Uses the Data Loss Prevention API to de-identify sensitive data in a string by redacting matched input values.
     *
     * @param string $callingProjectId      The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect         The string to deidentify (will be treated as text).
     */
    function deidentify_redact(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $textToInspect = 'My name is Alicia Abernathy, and my email address is aabernathy@example.com.'
    
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Specify the content to be de-identify.
        $contentItem = (new ContentItem())
            ->setValue($textToInspect);
    
        // Specify the type of info the inspection will look for.
        $infoType = (new InfoType())
            ->setName('EMAIL_ADDRESS');
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes([$infoType]);
    
        // Define type of de-identification.
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setRedactConfig(new RedactConfig());
    
        // Associate de-identification type with info type.
        $transformation = (new InfoTypeTransformation())
            ->setInfoTypes([$infoType])
            ->setPrimitiveTransformation($primitiveTransformation);
    
        // Construct the configuration for the Redact request and list all desired transformations.
        $deidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations((new InfoTypeTransformations())
                ->setTransformations([$transformation]));
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Run request
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setInspectConfig($inspectConfig)
            ->setItem($contentItem);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print results
        printf('Text after redaction: %s', $response->getItem()->getValue());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    import google.cloud.dlp
    
    
    def deidentify_with_redact(
        project: str,
        input_str: str,
        info_types: List[str],
    ) -> None:
        """Uses the Data Loss Prevention API to deidentify sensitive data in a
        string by redacting matched input values.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to deidentify (will be treated as text).
            info_types: A list of strings representing info types to look for.
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
                "transformations": [{"primitive_transformation": {"redact_config": {}}}]
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
    
    

### REST

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.

**HTTP method and URL**
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/content:deidentify
    

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

**JSON input**
    
    
    {
      "item":{
        "value":"My name is Alicia Abernathy, and my email address is aabernathy@example.com."
      },
      "deidentifyConfig":{
        "infoTypeTransformations":{
          "transformations":[
            {
              "infoTypes":[
                {
                  "name":"EMAIL_ADDRESS"
                }
              ],
              "primitiveTransformation":{
                "redactConfig":{
                }
              }
            }
          ]
        }
      },
      "inspectConfig":{
        "infoTypes":[
          {
            "name":"EMAIL_ADDRESS"
          }
        ]
      }
    }
    

**JSON output**
    
    
    {
      "item":{
        "value":"My name is Alicia Abernathy, and my email address is ."
      },
      "overview":{
        "transformedBytes":"22",
        "transformationSummaries":[
          {
            "infoType":{
              "name":"EMAIL_ADDRESS"
            },
            "transformation":{
              "redactConfig":{
              }
            },
            "results":[
              {
                "count":"1",
                "code":"SUCCESS"
              }
            ],
            "transformedBytes":"22"
          }
        ]
      }
    }
    

### Replacement

The replacement transformations replace each input value with either a given token value or with the name of its infoType.

#### Basic replacement

The basic replacement transformation ([`ReplaceValueConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#replacevalueconfig) in the DLP API) replaces detected sensitive data values with a value that you specify. For example, suppose you've told Sensitive Data Protection to use "[fake@example.com]" to replace all detected `EMAIL_ADDRESS` infoTypes, and the following string is sent to Sensitive Data Protection:
    
    
    My name is Alicia Abernathy, and my email address is aabernathy@example.com.

The returned string is the following:
    
    
    My name is Alicia Abernathy, and my email address is [fake@example.com].

The following JSON example and code in several languages shows how to form the API request and what the DLP API returns.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyWithReplacement
    {
        public static DeidentifyContentResponse Deidentify(
            string projectId,
            string text,
            string replaceText = null,
            IEnumerable<InfoType> infoTypes = null)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Set the info type if null.
            var infotypes = infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[] { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" } };
    
            // Construct the inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infotypes }
            };
    
            // Construct the replace value config.
            var replaceConfig = new [ReplaceValueConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReplaceValueConfig.html)
            {
                NewValue = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = replaceText ?? "[email-address]" }
            };
    
            // Construct the deidentify config using replace value config.
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations =
                    {
                        new InfoTypeTransformations.Types.InfoTypeTransformation
                        {
                            InfoTypes = { infotypes },
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                ReplaceConfig = replaceConfig
                            }
                        }
                    },
                }
            };
    
            // Construct the request.
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                DeidentifyConfig = deidentifyConfig,
                InspectConfig = inspectConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text }
            };
    
            // Call the API.
            var response = dlp.DeidentifyContent(request);
    
            // Check the deidentified content.
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
    
    // deidentifyWithReplacement de-identifies sensitive data by replacing matched input values
    func deidentifyWithReplacement(w io.Writer, projectID, inputStr string, infoTypeNames []string, replaceVal string) error {
    	// projectId := "your-project-id"
    	// inputStr := "My name is Alicia Abernathy, and my email address is aabernathy@example.com."
    	// infoTypeNames := []string{"EMAIL_ADDRESS"}
    	// replaceVal := "[email-address]"
    
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
    
    	// item to be analyzed
    	item := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{Value: inputStr},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	var infoTypes []*dlppb.InfoType
    	for _, v := range infoTypeNames {
    		infoTypes = append(infoTypes, &dlppb.InfoType{Name: v})
    	}
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes: infoTypes,
    	}
    
    	// Specify replacement string to be used for the finding.
    	replaceValueConfig := &dlppb.ReplaceValueConfig{
    		NewValue: &dlppb.Value{
    			Type: &dlppb.Value_StringValue{
    				StringValue: replaceVal,
    			},
    		},
    	}
    
    	// Define type of de-identification as replacement.
    	primitiveTransformation := &dlppb.PrimitiveTransformation_ReplaceConfig{
    		ReplaceConfig: replaceValueConfig,
    	}
    
    	// Associate de-identification type with info type.
    	infoTypeTransformation := &dlppb.InfoTypeTransformations_InfoTypeTransformation{
    		InfoTypes: infoTypes,
    		PrimitiveTransformation: &dlppb.PrimitiveTransformation{
    			Transformation: primitiveTransformation,
    		},
    	}
    
    	deIdentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    			InfoTypeTransformations: &dlppb.InfoTypeTransformations{
    				Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    					infoTypeTransformation,
    				},
    			},
    		},
    	}
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: deIdentifyConfig,
    		InspectConfig:    inspectConfig,
    		Item:             item,
    	}
    
    	// Send the request.
    	resp, err := client.DeidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the results.
    	fmt.Fprintf(w, "output : %v", resp.GetItem().GetValue())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
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
    import com.google.privacy.dlp.v2.[ReplaceValueConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceValueConfig.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    
    public class DeIdentifyWithReplacement {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect =
            "My name is Alicia Abernathy, and my email address is aabernathy@example.com.";
        deIdentifyWithReplacement(projectId, textToInspect);
      }
    
      // Inspects the provided text.
      public static void deIdentifyWithReplacement(String projectId, String textToRedact) {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the content to be inspected.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToRedact).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("EMAIL_ADDRESS").build();
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addInfoTypes(infoType).build();
          // Specify replacement string to be used for the finding.
          [ReplaceValueConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceValueConfig.html) replaceValueConfig =
              [ReplaceValueConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceValueConfig.html).newBuilder()
                  .[setNewValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceValueConfig.Builder.html#com_google_privacy_dlp_v2_ReplaceValueConfig_Builder_setNewValue_com_google_privacy_dlp_v2_Value_)([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("[email-address]").build())
                  .build();
          // Define type of deidentification as replacement.
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder().[setReplaceConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setReplaceConfig_com_google_privacy_dlp_v2_ReplaceValueConfig_)(replaceValueConfig).build();
          // Associate deidentification type with info type.
          [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) transformation =
              [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html).newBuilder()
                  .addInfoTypes(infoType)
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
          // Construct the configuration for the Redact request and list all desired transformations.
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) redactConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder()
                  .setInfoTypeTransformations(
                      [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(transformation))
                  .build();
    
          // Construct the Redact request to be sent by the client.
          [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html) request =
              [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setDeidentifyConfig(redactConfig)
                  .setInspectConfig(inspectConfig)
                  .build();
    
          // Use the client to send the API request.
          [DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html) response = dlp.deidentifyContent(request);
    
          // Parse the response and process results
          System.out.println("Text after redaction: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getValue());
        } catch (Exception e) {
          System.out.println("Error during inspectString: \n" + e.toString());
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
    // const projectId = 'my-project';
    
    // The string to deidentify
    // const string = 'My SSN is 372819127';
    
    // The string to replace sensitive information with
    // const replacement = "[REDACTED]"
    
    async function deidentifyWithReplacement() {
      // Construct deidentification request
      const item = {value: string};
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: {
          infoTypeTransformations: {
            transformations: [
              {
                primitiveTransformation: {
                  replaceConfig: {
                    newValue: {
                      stringValue: replacement,
                    },
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
    
    deidentifyWithReplacement();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\ReplaceValueConfig;
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * De-identify sensitive data: Replacing matched input values.
     * Uses the Data Loss Prevention API to de-identify sensitive data in a string by replacing matched input values with a value that you specify.
     *
     * @param string $callingProjectId  The Google Cloud project id to use as a parent resource.
     * @param string $string            The string to deidentify (will be treated as text).
     */
    
    function deidentify_replace(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $string = 'My name is Alicia Abernathy, and my email address is aabernathy@example.com.'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Specify the content to be deidentify.
        $content = (new ContentItem())
            ->setValue($string);
    
        // Specify the type of info the inspection will look for.
        $emailAddressInfoType = (new InfoType())
            ->setName('EMAIL_ADDRESS');
    
        // Create the configuration object
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes([$emailAddressInfoType]);
    
        // Specify replacement string to be used for the finding.
        $replaceValueConfig = (new ReplaceValueConfig())
            ->setNewValue((new Value())
                ->setStringValue('[email-address]'));
    
        // Define type of deidentification as replacement.
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setReplaceConfig($replaceValueConfig);
    
        // Associate deidentification type with info type.
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setInfoTypes([$emailAddressInfoType]);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Construct the configuration for the Redact request and list all desired transformations.
        $deidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations($infoTypeTransformations);
    
        // Run request
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($content)
            ->setInspectConfig($inspectConfig);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print the results
        printf('Deidentified content: %s' . PHP_EOL, $response->getItem()->getValue());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    import google.cloud.dlp
    
    
    def deidentify_with_replace(
        project: str,
        input_str: str,
        info_types: List[str],
        replacement_str: str = "REPLACEMENT_STR",
    ) -> None:
        """Uses the Data Loss Prevention API to deidentify sensitive data in a
        string by replacing matched input values with a value you specify.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to deidentify (will be treated as text).
            info_types: A list of strings representing info types to look for.
            replacement_str: The string to replace all values that match given
                info types.
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
                            "replace_config": {
                                "new_value": {"string_value": replacement_str}
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
    
    

### REST

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.

**HTTP method and URL**
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/content:deidentify
    

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

**JSON input**
    
    
    {
      "item":{
        "value":"My name is Alicia Abernathy, and my email address is aabernathy@example.com."
      },
      "deidentifyConfig":{
        "infoTypeTransformations":{
          "transformations":[
            {
              "infoTypes":[
                {
                  "name":"EMAIL_ADDRESS"
                }
              ],
              "primitiveTransformation":{
                "replaceConfig":{
                  "newValue":{
                    "stringValue":"[email-address]"
                  }
                }
              }
            }
          ]
        }
      },
      "inspectConfig":{
        "infoTypes":[
          {
            "name":"EMAIL_ADDRESS"
          }
        ]
      }
    }
    

**JSON output**
    
    
    {
      "item":{
        "value":"My name is Alicia Abernathy, and my email address is [email-address]."
      },
      "overview":{
        "transformedBytes":"22",
        "transformationSummaries":[
          {
            "infoType":{
              "name":"EMAIL_ADDRESS"
            },
            "transformation":{
              "replaceConfig":{
                "newValue":{
                  "stringValue":"[email-address]"
                }
              }
            },
            "results":[
              {
                "count":"1",
                "code":"SUCCESS"
              }
            ],
            "transformedBytes":"22"
          }
        ]
      }
    }
    

#### Dictionary replacement

Dictionary replacement ([`ReplaceDictionaryConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#ReplaceDictionaryConfig)) replaces each piece of detected sensitive data with a value that Sensitive Data Protection randomly selects from a list of words that you provide. This transformation method is useful if you want to use realistic surrogate values.

Suppose you want Sensitive Data Protection to detect email addresses and replace each detected value with one of three surrogate email addresses.

You send the following input string to Sensitive Data Protection along with the list of surrogate email addresses:

**Input string**
    
    
    My name is Alicia Abernathy, and my email address is aabernathy@example.com.

**Word list**

  * izumi@example.com
  * alex@example.com
  * tal@example.com



The returned string can be any of the following:
    
    
    My name is Alicia Abernathy, and my email address is izumi@example.com.
    
    
    My name is Alicia Abernathy, and my email address is alex@example.com.
    
    
    My name is Alicia Abernathy, and my email address is tal@example.com.

The following JSON example shows how to form the API request and what the DLP API returns.

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.

**HTTP method and URL**
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/content:deidentify
    

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

**JSON input**
    
    
    {
      "item": {
        "value": "My name is Alicia Abernathy, and my email address is aabernathy@example.com."
      },
      "deidentifyConfig": {
        "infoTypeTransformations": {
          "transformations": [
            {
              "infoTypes": [
                {
                  "name": "EMAIL_ADDRESS"
                }
              ],
              "primitiveTransformation": {
                "replaceDictionaryConfig": {
                  "wordList": {
                    "words": [
                      "izumi@example.com",
                      "alex@example.com",
                      "tal@example.com"
                    ]
                  }
                }
              }
            }
          ]
        }
      },
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "EMAIL_ADDRESS"
          }
        ]
      }
    }
    

**JSON output**
    
    
    {
      "item": {
        "value": "My name is Alicia Abernathy, and my email address is izumi@example.com."
      },
      "overview": {
        "transformedBytes": "22",
        "transformationSummaries": [
          {
            "infoType": {
              "name": "EMAIL_ADDRESS"
            },
            "transformation": {
              "replaceDictionaryConfig": {
                "wordList": {
                  "words": [
                    "izumi@example.com",
                    "alex@example.com",
                    "tal@example.com"
                  ]
                }
              }
            },
            "results": [
              {
                "count": "1",
                "code": "SUCCESS"
              }
            ],
            "transformedBytes": "22"
          }
        ]
      }
    }
    

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyDataUsingDictionaryReplacement
    {
        public static DeidentifyContentResponse Deidentify(
            string projectId,
            string text,
            IEnumerable<InfoType> infoTypes = null,
            IEnumerable<string> words = null)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct inspect config by specifying the type of info to be inspected.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[] { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" } } },
            };
    
            // Construct dictionary replace config by specifying the list of value which will
            // be replaced by any mentioned values below.
            var replaceConfig = new [ReplaceDictionaryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReplaceDictionaryConfig.html)
            {
                WordList = new CustomInfoType.Types.Dictionary.Types.WordList
                {
                    Words =
                    {
                        words ?? new string[]
                        {
                            "izumi@example.com", "alex@example.com", "tal@example.com"
                        }
                    }
                }
            };
    
            // Construct deidentify config using above created replace config.
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations =
                    {
                        new InfoTypeTransformations.Types.InfoTypeTransformation
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                ReplaceDictionaryConfig = replaceConfig
                            }
                        }
                    }
                }
            };
    
            // Construct a request.
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                DeidentifyConfig = deidentifyConfig,
                InspectConfig = inspectConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text }
            };
    
            // Call the API.
            var response = dlp.DeidentifyContent(request);
    
            // Check the deidentified content.
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
    
    // deidentifyDataReplaceWithDictionary de-identifies sensitive data in a string by replacing
    // each piece of detected sensitive data with a value that Cloud DLP randomly selects from
    // a list of words that you provide.
    func deidentifyDataReplaceWithDictionary(w io.Writer, projectID, textToDeIdentify string) error {
    	// projectId := "my-project-id"
    	// textToDeIdentify := "My name is Alicia Abernathy, and my email address is aabernathy@example.com."
    
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
    
    	// Specify the content to be inspected.
    	item := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{
    			Value: textToDeIdentify,
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	infoType := &dlppb.InfoType{
    		Name: "EMAIL_ADDRESS",
    	}
    
    	// Specify the infotypes to be inspected.
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes: []*dlppb.InfoType{
    			infoType,
    		},
    	}
    
    	// Specify list of values which will be randomly picked to replace identified email addresses.
    	wordList := &dlppb.ReplaceDictionaryConfig_WordList{
    		WordList: &dlppb.CustomInfoType_Dictionary_WordList{
    			Words: []string{"izumi@example.com", "alex@example.com"},
    		},
    	}
    
    	// Specify the Dictionary to use for selecting replacement values for the finding.
    	replaceDictionaryConfig := &dlppb.ReplaceDictionaryConfig{
    		Type: wordList,
    	}
    
    	// Define type of de-identification as replacement with items from dictionary.
    	primitiveTransformation := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_ReplaceDictionaryConfig{
    			ReplaceDictionaryConfig: replaceDictionaryConfig,
    		},
    	}
    
    	transformation := &dlppb.InfoTypeTransformations_InfoTypeTransformation{
    		InfoTypes: []*dlppb.InfoType{
    			infoType,
    		},
    		PrimitiveTransformation: primitiveTransformation,
    	}
    
    	// Combine configurations into a request for the service.
    	deIdentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    			InfoTypeTransformations: &dlppb.InfoTypeTransformations{
    				Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    					transformation,
    				},
    			},
    		},
    	}
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: deIdentifyConfig,
    		InspectConfig:    inspectConfig,
    		Item:             item,
    	}
    
    	// Send the request.
    	resp, err := client.DeidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the results.
    	fmt.Fprint(w, "output: ", resp.GetItem().GetValue())
    	return nil
    
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).[WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[ReplaceDictionaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceDictionaryConfig.html);
    import java.io.IOException;
    
    public class DeIdentifyDataReplaceWithDictionary {
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The string to de-identify
        String textToDeIdentify =
            "My name is Charlie and email address is charlie@example.com.";
        deidentifyDataReplaceWithDictionary(projectId, textToDeIdentify);
      }
    
      // Performs data de-identification by replacing identified email addresses in a given text with
      // randomly selected values from a dictionary.
      public static void deidentifyDataReplaceWithDictionary(String projectId, String textToDeIdentify)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to de-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToDeIdentify).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("EMAIL_ADDRESS").build();
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().addInfoTypes(infoType).build();
    
          // Specify list of value which will randomly replace identified email addresses.
          [WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html) wordList =
              [WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html).newBuilder().[addWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Dictionary_WordList_Builder_addWords_java_lang_String_)("izumi@example.com").[addWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Dictionary_WordList_Builder_addWords_java_lang_String_)("alex@example.com").build();
    
          // Specify the dictionary to use for selecting replacement values for the finding.
          [ReplaceDictionaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceDictionaryConfig.html) replaceDictionaryConfig =
              [ReplaceDictionaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceDictionaryConfig.html).newBuilder().setWordList(wordList).build();
    
          // Define type of de-identification as replacement with items from dictionary.
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setReplaceDictionaryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setReplaceDictionaryConfig_com_google_privacy_dlp_v2_ReplaceDictionaryConfig_)(replaceDictionaryConfig)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) transformation =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).InfoTypeTransformation.newBuilder()
                  .addInfoTypes(infoType)
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
    
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder()
                  .setInfoTypeTransformations(
                      [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(transformation))
                  .build();
    
          // Combine configurations into a request for the service.
          [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html) request =
              [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setDeidentifyConfig(deidentifyConfig)
                  .setInspectConfig(inspectConfig)
                  .build();
    
          // Use the client to send the API request.
          [DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html) response = dlp.deidentifyContent(request);
    
          // Parse the response and process results.
          System.out.print("Text after de-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getValue());
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
    // const projectId = 'my-project';
    
    // The string to de-identify
    // const string = 'My name is Alicia Abernathy, and my email address is aabernathy@example.com.';
    
    // The infoTypes of information to match
    // const infoTypes = [{ name: 'EMAIL_ADDRESS' }];
    
    // The words to replace sensitive information with
    // const words = ['izumi@example.com', 'alex@example.com', 'tal@example.com'];
    
    async function deidentifyWithDictionaryReplacement() {
      // Construct word list to be used for replacement
      const wordList = {
        words: words,
      };
      // Construct item to de-identify
      const item = {value: string};
    
      // Specify replacement dictionary config using word list.
      const replaceDictionaryConfig = {
        wordList: wordList,
      };
    
      // Associate replacement dictionary config with infotype transformation.
      const infoTypeTransformations = {
        transformations: [
          {
            infoTypes: infoTypes,
            primitiveTransformation: {
              replaceDictionaryConfig: replaceDictionaryConfig,
            },
          },
        ],
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: {
          infoTypeTransformations: infoTypeTransformations,
        },
        item: item,
      };
    
      // Run de-identification request.
      const [response] = await dlp.deidentifyContent(request);
      const deidentifiedItem = response.item;
    
      // Print results.
      console.log(deidentifiedItem.value);
    }
    
    deidentifyWithDictionaryReplacement();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary\WordList;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\ReplaceDictionaryConfig;
    
    /**
     * Dictionary replacement
     * Dictionary replacement (ReplaceDictionaryConfig) replaces each piece of detected sensitive data with a
     * value that Cloud DLP randomly selects from a list of words that you provide. This transformation method
     * is useful if you want to use realistic surrogate values.Suppose you want Cloud DLP to detect email addresses
     * and replace each detected value with one of three surrogate email addresses.
     *
     * @param string $callingProjectId  The project ID to run the API call under.
     * @param string $textToDeIdentify  The String you want the service to DeIdentify.
     */
    function deidentify_dictionary_replacement(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $textToDeIdentify = 'My name is Charlie and email address is charlie@example.com.'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Specify what content you want the service to de-identify.
        $contentItem = (new ContentItem())
            ->setValue($textToDeIdentify);
    
        // Specify the type of info the inspection will look for.
        // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
        $emailAddress = (new InfoType())
            ->setName('EMAIL_ADDRESS');
    
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes([$emailAddress]);
    
        // Define type of de-identification as replacement with items from dictionary.
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setReplaceDictionaryConfig(
                // Specify the dictionary to use for selecting replacement values for the finding.
                (new ReplaceDictionaryConfig())
                    ->setWordList(
                        // Specify list of value which will randomly replace identified email addresses.
                        (new WordList())
                            ->setWords(['izumi@example.com', 'alex@example.com', 'tal@example.com'])
                    )
            );
    
        $transformation = (new InfoTypeTransformation())
            ->setInfoTypes([$emailAddress])
            ->setPrimitiveTransformation($primitiveTransformation);
    
        // Construct the configuration for the de-identification request and list all desired transformations.
        $deidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations(
                (new InfoTypeTransformations())
                    ->setTransformations([$transformation])
            );
    
        // Send the request and receive response from the service.
        $parent = "projects/$callingProjectId/locations/global";
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setInspectConfig($inspectConfig)
            ->setItem($contentItem);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print the results.
        printf('Text after replace with infotype config: %s', $response->getItem()->getValue());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    import google.cloud.dlp
    
    
    def deindentify_with_dictionary_replacement(
        project: str,
        input_str: str,
        info_types: List[str],
        word_list: List[str],
    ) -> None:
        """Uses the Data Loss Prevention API to de-identify sensitive data in a
        string by replacing each piece of detected sensitive data with a value
        that Cloud DLP randomly selects from a list of words that you provide.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to deidentify (will be treated as text).
            info_types: A list of strings representing infoTypes to look for.
            word_list: List of words or phrases to search for in the data.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct list of info types
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Construct deidentify configuration dictionary
        deidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {
                        "info_types": info_types,
                        "primitive_transformation": {
                            "replace_dictionary_config": {"word_list": {"words": word_list}}
                        },
                    }
                ]
            }
        }
    
        # Construct the `item`
        item = {"value": input_str}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={
                "parent": parent,
                "deidentify_config": deidentify_config,
                "inspect_config": {"info_types": info_types},
                "item": item,
            }
        )
    
        # Print out the results.
        print(f"De-identified Content: {response.item.value}")
    
    

#### InfoType replacement

You can also specify an infoType replacement ([`ReplaceWithInfoTypeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#replacewithinfotypeconfig) in the DLP API). This transformation does the same thing as the basic replacement transformation, but it replaces each detected sensitive data value with the infoType of the detected value.

For example, suppose you've told Sensitive Data Protection to detect both email addresses and last names, and to replace each detected value with the value's infoType. You send the following string to Sensitive Data Protection:
    
    
    My name is Alicia Abernathy, and my email address is aabernathy@example.com.

The returned string is the following:
    
    
    My name is Alicia LAST_NAME, and my email address is EMAIL_ADDRESS.

### Masking

You can configure Sensitive Data Protection to completely or partially mask a detected sensitive value ([`CharacterMaskConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#charactermaskconfig) in the DLP API) by replacing each character with a fixed single masking character such as an asterisk (*) or hash (#). Masking can start from the beginning or end of the string. This transformation also works with number types such as long integers.

Sensitive Data Protection's masking transformation has the following options you can specify:

  * Masking character (The `maskingCharacter` argument in the DLP API): The character to use to mask each character of a sensitive value. For example, you could specify an asterisk (*) or dollar sign ($) to mask a series of numbers such as those in a credit card number.
  * The number of characters to mask (`numberToMask`): If you don't specify this value, all characters will be masked.
  * Whether to reverse the order (`reverseOrder`): Whether to mask characters in reverse order. Reversing the order causes characters in matched values to be masked from the end toward the beginning of the value.
  * Characters to ignore (`charactersToIgnore`): One or more characters to skip when masking values. For example, you can tell Sensitive Data Protection to leave hyphens in place when masking a telephone number. You can also specify a group of common characters ([`CharsToIgnore`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#DeidentifyTemplate.CharsToIgnore)) to ignore when masking.



Suppose you send the following string to Sensitive Data Protection and instruct it to use the character masking transformation on email addresses:
    
    
    My name is Alicia Abernathy, and my email address is aabernathy@example.com.

With the masking character sent to '#,' the characters to ignore set to the common character set, and otherwise default settings, Sensitive Data Protection returns the following:
    
    
    My name is Alicia Abernathy, and my email address is ##########@#######.###.

The following JSON and code examples demonstrate how the masking transformation works.

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
    

### REST

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.

**HTTP method and URL**
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/content:deidentify
    

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

**JSON input**
    
    
    {
      "item":{
        "value":"My name is Alicia Abernathy, and my email address is aabernathy@example.com."
      },
      "deidentifyConfig":{
        "infoTypeTransformations":{
          "transformations":[
            {
              "infoTypes":[
                {
                  "name":"EMAIL_ADDRESS"
                }
              ],
              "primitiveTransformation":{
                "characterMaskConfig":{
                  "maskingCharacter":"#",
                  "reverseOrder":false,
                  "charactersToIgnore":[
                    {
                      "charactersToSkip":".@"
                    }
                  ]
                }
              }
            }
          ]
        }
      },
      "inspectConfig":{
        "infoTypes":[
          {
            "name":"EMAIL_ADDRESS"
          }
        ]
      }
    }
    

**JSON output**
    
    
    {
      "item":{
        "value":"My name is Alicia Abernathy, and my email address is ##########@#######.###."
      },
      "overview":{
        "transformedBytes":"22",
        "transformationSummaries":[
          {
            "infoType":{
              "name":"EMAIL_ADDRESS"
            },
            "transformation":{
              "characterMaskConfig":{
                "maskingCharacter":"#",
                "charactersToIgnore":[
                  {
                    "charactersToSkip":".@"
                  }
                ]
              }
            },
            "results":[
              {
                "count":"1",
                "code":"SUCCESS"
              }
            ],
            "transformedBytes":"22"
          }
        ]
      }
    }
    

### Crypto-based tokenization transformations

Crypto-based tokenization (also referred to as "pseudonymization") transformations are de-identification methods that replace the original sensitive data values with encrypted values. Sensitive Data Protection supports the following types of tokenization, including transformations that can be reversed and allow for re-identification:

  * Cryptographic hashing: Given a [`CryptoKey`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptokey), Sensitive Data Protection uses a SHA-256-based message authentication code ([HMAC-SHA-256](https://tools.ietf.org/html/rfc4634)) on the input value, and then replaces the input value with the hashed value encoded in base64. Unlike other types of crypto-based transformations, this type of transformation isn't reversible.
  * Format preserving encryption: Replaces an input value with a token that has been generated using [format-preserving encryption (FPE)](https://en.wikipedia.org/wiki/Format-preserving_encryption) with the FFX mode of operation. This transformation method produces a token that is limited to the same alphabet as the input value and is the same length as the input value. FPE also supports re-identification given the original encryption key.
  * Deterministic encryption: Replaces an input value with a token that has been generated using [AES in Synthetic Initialization Vector mode (AES-SIV)](https://tools.ietf.org/html/rfc5297). This transformation method has no limitation on supported string character sets, generates identical tokens for each instance of an identical input value, and uses surrogates to enable re-identification given the original encryption key.



**Note:** When you use Cloud KMS for cryptographic operations, [charges apply](https://cloud.google.com/kms/pricing). In addition, when you use a [Cloud HSM](https://docs.cloud.google.com/kms/docs/hsm) key or a [Cloud EKM](https://docs.cloud.google.com/kms/docs/ekm) key, you consume Cloud KMS quota on the project that contains the key. In contrast, if you're using a software Cloud KMS key with Sensitive Data Protection, no quota values apply. For more information, see [Quotas](https://docs.cloud.google.com/kms/quotas) in the Cloud KMS documentation.

#### Cryptographic hashing

The cryptographic hashing transformation ([`CryptoHashConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptohashconfig) in the DLP API) takes an input value (a piece of sensitive data that Sensitive Data Protection has detected) and replaces it with a hashed value. The hash value is generated by using a SHA-256-based message authentication code ([HMAC-SHA-256](https://tools.ietf.org/html/rfc4634)) ) on the input value with a [`CryptoKey`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptokey).

Sensitive Data Protection outputs a base64-encoded representation of the hashed input value in the place of the original value.

Before using the cryptographic hashing transformation, keep in mind the following:

  * The input value is not encrypted but hashed.
  * This transformation can't be reversed. That is, given the hashed output value of the transformation and the original cryptographic key, there is no way to restore the original value.
  * Currently, only string and integer values can be hashed.
  * The hashed output of the transformation is always the same length, depending on the size of the cryptographic key. For example, if you use the cryptographic hashing transformation on 10-digit phone numbers, each phone number will be replaced by a fixed-length base64-encoded hash value.



#### Format-preserving encryption

The format-preserving encryption (FPE) transformation method ([`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptoreplaceffxfpeconfig) in the DLP API) takes an input value (a piece of sensitive data that Sensitive Data Protection has detected), encrypts it using format-preserving encryption in FFX mode and a [`CryptoKey`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptokey), and then replaces the original value with the encrypted value, or token.

The input value:

  * Must be at least two characters long (or the empty string).
  * Must be encoded as ASCII.
  * Comprised of the characters specified by an "alphabet," which is the set of between 2 and 95 allowed characters in the input value. For more information, see the alphabet field in [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptoreplaceffxfpeconfig).



The generated token:

  * Is the encrypted input value.
  * Preserves the character set ("alphabet") and length of the input value post-encryption.
  * Is computed using format-preserving encryption in FFX mode keyed on the specified cryptographic key.
  * Isn't necessarily unique, as each instance of the same input value de-identifies to the same token. This enables referential integrity, and therefore enables more efficient searching of de-identified data. You can change this behavior by using context "tweaks," as described in [Contexts](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization#contexts).



If there are multiple instances of an input value in the source content, each one will be de-identified to the same token. FPE preserves both length and alphabet space (the character set), which is limited to 95 characters. You can change this behavior by using context "tweaks," which can improve security. The addition of a context tweak to the transformation enables Sensitive Data Protection to de-identify multiple instances of the same input value to different tokens. If you don't need to preserve the length and alphabet space of the original values, use deterministic encryption, described below.

Sensitive Data Protection computes the replacement token using a cryptographic key. You provide this key in one of three ways:

  * By embedding it unencrypted in the API request. This is not recommended.
  * By requesting that Sensitive Data Protection generate it.
  * By embedding it encrypted in the API request.



If you choose to embed the key in the API request, you need to create a key and wrap (encrypt) it using a Cloud Key Management Service (Cloud KMS) key. For more information, see [Create a wrapped key](https://docs.cloud.google.com/sensitive-data-protection/docs/create-wrapped-key). The value returned is a base64-encoded string by default. To set this value in Sensitive Data Protection, you must decode it into a byte string. The following code snippets highlight how to do this in several languages. End-to-end examples are provided following these snippets.

### Java
    
    
    KmsWrappedCryptoKey.newBuilder()
        .setWrappedKey(ByteString.copyFrom(BaseEncoding.base64().decode(wrappedKey)))
    

### Python
    
    
    # The wrapped key is base64-encoded, but the library expects a binary
    # string, so decode it here.
    import base64
    wrapped_key = base64.b64decode(wrapped_key)
    

### PHP
    
    
    // Create the wrapped crypto key configuration object
    $kmsWrappedCryptoKey = (new KmsWrappedCryptoKey())
        ->setWrappedKey(base64_decode($wrappedKey))
        ->setCryptoKeyName($keyName);
    

### C#
    
    
    WrappedKey = ByteString.FromBase64(wrappedKey)
    

For more information about encrypting and decrypting data using Cloud KMS, see [Encrypting and Decrypting Data](https://docs.cloud.google.com/kms/docs/encrypt-decrypt).

##### Format-preserving encryption examples: de-identification

This example uses the [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptoreplaceffxfpeconfig) transformation method to de-identify sensitive data. For more information, see Format-preserving encryption on this page.

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.common.io.BaseEncoding;
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html);
    import com.google.privacy.dlp.v2.[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html);
    import com.google.privacy.dlp.v2.[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).[FfxCommonNativeAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.Arrays;
    
    public class DeIdentifyWithFpe {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToDeIdentify = "I'm Gary and my SSN is 552096781";
        String kmsKeyName =
            "projects/YOUR_PROJECT/"
                + "locations/YOUR_KEYRING_REGION/"
                + "keyRings/YOUR_KEYRING_NAME/"
                + "cryptoKeys/YOUR_KEY_NAME";
        String wrappedAesKey = "YOUR_ENCRYPTED_AES_256_KEY";
        deIdentifyWithFpe(projectId, textToDeIdentify, kmsKeyName, wrappedAesKey);
      }
    
      public static void deIdentifyWithFpe(
          String projectId, String textToDeIdentify, String kmsKeyName, String wrappedAesKey)
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
    
          // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it
          [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html) kmsWrappedCryptoKey =
              [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html).newBuilder()
                  .[setWrappedKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setWrappedKey_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(BaseEncoding.base64().decode(wrappedAesKey)))
                  .[setCryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setCryptoKeyName_java_lang_String_)(kmsKeyName)
                  .build();
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder().[setKmsWrapped](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setKmsWrapped_com_google_privacy_dlp_v2_KmsWrappedCryptoKey_)(kmsWrappedCryptoKey).build();
    
          // Specify how the info from the inspection should be encrypted.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) surrogateInfoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("SSN_TOKEN").build();
          [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html) cryptoReplaceFfxFpeConfig =
              [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).newBuilder()
                  .setCryptoKey(cryptoKey)
                  // Set of characters in the input text. For more info, see
                  // https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.FfxCommonNativeAlphabet
                  .[setCommonAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.Builder.html#com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_Builder_setCommonAlphabet_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_FfxCommonNativeAlphabet_)([FfxCommonNativeAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet.html).NUMERIC)
                  .setSurrogateInfoType(surrogateInfoType)
                  .build();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoReplaceFfxFpeConfig_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_)(cryptoReplaceFfxFpeConfig)
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
          System.out.println(
              "Text after format-preserving encryption: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getValue());
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
    // const projectId = 'my-project';
    
    // The string to deidentify
    // const string = 'My SSN is 372819127';
    
    // The set of characters to replace sensitive ones with
    // For more information, see https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#ffxcommonnativealphabet
    // const alphabet = 'ALPHA_NUMERIC';
    
    // The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key
    // const keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME';
    
    // The encrypted ('wrapped') AES-256 key to use
    // This key should be encrypted using the Cloud KMS key specified above
    // const wrappedKey = 'YOUR_ENCRYPTED_AES_256_KEY'
    
    // (Optional) The name of the surrogate custom info type to use
    // Only necessary if you want to reverse the deidentification process
    // Can be essentially any arbitrary string, as long as it doesn't appear
    // in your dataset otherwise.
    // const surrogateType = 'SOME_INFO_TYPE_DEID';
    
    async function deidentifyWithFpe() {
      // Construct FPE config
      const cryptoReplaceFfxFpeConfig = {
        cryptoKey: {
          kmsWrapped: {
            wrappedKey: wrappedKey,
            cryptoKeyName: keyName,
          },
        },
        commonAlphabet: alphabet,
      };
      if (surrogateType) {
        cryptoReplaceFfxFpeConfig.surrogateInfoType = {
          name: surrogateType,
        };
      }
    
      // Construct deidentification request
      const item = {value: string};
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: {
          infoTypeTransformations: {
            transformations: [
              {
                primitiveTransformation: {
                  cryptoReplaceFfxFpeConfig: cryptoReplaceFfxFpeConfig,
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
    deidentifyWithFpe();

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    from typing import List
    
    import google.cloud.dlp
    
    
    def deidentify_with_fpe(
        project: str,
        input_str: str,
        info_types: List[str],
        alphabet: str = None,
        surrogate_type: str = None,
        key_name: str = None,
        wrapped_key: str = None,
    ) -> None:
        """Uses the Data Loss Prevention API to deidentify sensitive data in a
        string using Format Preserving Encryption (FPE).
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to deidentify (will be treated as text).
            info_types: A list of strings representing info types to look for.
            alphabet: The set of characters to replace sensitive ones with. For
                more information, see https://cloud.google.com/dlp/docs/reference/
                rest/v2beta2/organizations.deidentifyTemplates#ffxcommonnativealphabet
            surrogate_type: The name of the surrogate custom info type to use. Only
                necessary if you want to reverse the deidentification process. Can
                be essentially any arbitrary string, as long as it doesn't appear
                in your dataset otherwise.
            key_name: The name of the Cloud KMS key used to encrypt ('wrap') the
                AES-256 key. Example:
                key_name = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/
                keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
            wrapped_key: The encrypted ('wrapped') AES-256 key to use. This key
                should be encrypted using the Cloud KMS key specified by key_name.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # The wrapped key is base64-encoded, but the library expects a binary
        # string, so decode it here.
        wrapped_key = base64.b64decode(wrapped_key)
    
        # Construct FPE configuration dictionary
        crypto_replace_ffx_fpe_config = {
            "crypto_key": {
                "kms_wrapped": {"wrapped_key": wrapped_key, "crypto_key_name": key_name}
            },
            "common_alphabet": alphabet,
        }
    
        # Add surrogate type
        if surrogate_type:
            crypto_replace_ffx_fpe_config["surrogate_info_type"] = {"name": surrogate_type}
    
        # Construct inspect configuration dictionary
        inspect_config = {"info_types": [{"name": info_type} for info_type in info_types]}
    
        # Construct deidentify configuration dictionary
        deidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {
                        "primitive_transformation": {
                            "crypto_replace_ffx_fpe_config": crypto_replace_ffx_fpe_config
                        }
                    }
                ]
            }
        }
    
        # Convert string to item
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
    
        # Print results
        print(response.item.value)
    
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // deidentifyFPE deidentifies the input with FPE (Format Preserving Encryption).
    // keyFileName is the file name with the KMS wrapped key and cryptoKeyName is the
    // full KMS key resource name used to wrap the key. surrogateInfoType is an
    // optional identifier needed for reidentification. surrogateInfoType can be any
    // value not found in your input.
    // Info types can be found with the infoTypes.list method or on https://cloud.google.com/dlp/docs/infotypes-reference
    func deidentifyFPE(w io.Writer, projectID, input string, infoTypeNames []string, kmsKeyName, wrappedAESKey, surrogateInfoType string) error {
    	// projectID := "my-project-id"
    	// input := "My SSN is 123456789"
    	// infoTypeNames := []string{"US_SOCIAL_SECURITY_NUMBER"}
    	// kmsKeyName := "projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME"
    	// wrappedAESKey := "YOUR_ENCRYPTED_AES_256_KEY"
    	// surrogateInfoType := "AGE"
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
    
    	// Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
    	kmsWrappedCryptoKey, err := base64.StdEncoding.DecodeString(wrappedAESKey)
    	if err != nil {
    		return err
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
    								Transformation: &dlppb.PrimitiveTransformation_CryptoReplaceFfxFpeConfig{
    									CryptoReplaceFfxFpeConfig: &dlppb.CryptoReplaceFfxFpeConfig{
    										CryptoKey: &dlppb.CryptoKey{
    											Source: &dlppb.CryptoKey_KmsWrapped{
    												KmsWrapped: &dlppb.KmsWrappedCryptoKey{
    													WrappedKey:    kmsWrappedCryptoKey,
    													CryptoKeyName: kmsKeyName,
    												},
    											},
    										},
    										// Set the alphabet used for the output.
    										Alphabet: &dlppb.CryptoReplaceFfxFpeConfig_CommonAlphabet{
    											CommonAlphabet: dlppb.[CryptoReplaceFfxFpeConfig_ALPHA_NUMERIC](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_CryptoReplaceFfxFpeConfig_FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED_CryptoReplaceFfxFpeConfig_NUMERIC_CryptoReplaceFfxFpeConfig_HEXADECIMAL_CryptoReplaceFfxFpeConfig_UPPER_CASE_ALPHA_NUMERIC_CryptoReplaceFfxFpeConfig_ALPHA_NUMERIC),
    										},
    										// Set the surrogate info type, used for reidentification.
    										SurrogateInfoType: &dlppb.InfoType{
    											Name: surrogateInfoType,
    										},
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
    

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoKey;
    use Google\Cloud\Dlp\V2\CryptoReplaceFfxFpeConfig;
    use Google\Cloud\Dlp\V2\CryptoReplaceFfxFpeConfig\FfxCommonNativeAlphabet;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\KmsWrappedCryptoKey;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    
    /**
     * Deidentify a string using Format-Preserving Encryption (FPE).
     *
     * @param string $callingProjectId  The GCP Project ID to run the API call under
     * @param string $string            The string to deidentify
     * @param string $keyName           The name of the Cloud KMS key used to encrypt (wrap) the AES-256 key
     * @param string $wrappedKey        The name of the Cloud KMS key use, encrypted with the KMS key in $keyName
     * @param string $surrogateTypeName (Optional) surrogate custom info type to enable reidentification
     */
    function deidentify_fpe(
        string $callingProjectId,
        string $string,
        string $keyName,
        string $wrappedKey,
        string $surrogateTypeName = ''
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // The infoTypes of information to mask
        $ssnInfoType = (new InfoType())
            ->setName('US_SOCIAL_SECURITY_NUMBER');
        $infoTypes = [$ssnInfoType];
    
        // Create the wrapped crypto key configuration object
        $kmsWrappedCryptoKey = (new KmsWrappedCryptoKey())
            ->setWrappedKey(base64_decode($wrappedKey))
            ->setCryptoKeyName($keyName);
    
        // The set of characters to replace sensitive ones with
        // For more information, see https://cloud.google.com/dlp/docs/reference/rest/V2/organizations.deidentifyTemplates#ffxcommonnativealphabet
        $commonAlphabet = FfxCommonNativeAlphabet::NUMERIC;
    
        // Create the crypto key configuration object
        $cryptoKey = (new CryptoKey())
            ->setKmsWrapped($kmsWrappedCryptoKey);
    
        // Create the crypto FFX FPE configuration object
        $cryptoReplaceFfxFpeConfig = (new CryptoReplaceFfxFpeConfig())
            ->setCryptoKey($cryptoKey)
            ->setCommonAlphabet($commonAlphabet);
    
        if ($surrogateTypeName) {
            $surrogateType = (new InfoType())
                ->setName($surrogateTypeName);
            $cryptoReplaceFfxFpeConfig->setSurrogateInfoType($surrogateType);
        }
    
        // Create the information transform configuration objects
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCryptoReplaceFfxFpeConfig($cryptoReplaceFfxFpeConfig);
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setInfoTypes($infoTypes);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Create the deidentification configuration object
        $deidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations($infoTypeTransformations);
    
        $content = (new ContentItem())
            ->setValue($string);
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Run request
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($content);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print the results
        $deidentifiedValue = $response->getItem()->getValue();
        print($deidentifiedValue);
    }

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using static Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types;
    
    public class DeidentifyWithFpe
    {
        public static DeidentifyContentResponse Deidentify(
            string projectId,
            string dataValue,
            IEnumerable<InfoType> infoTypes,
            string keyName,
            string wrappedKey,
            [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html) alphabet)
        {
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations =
                    {
                        new InfoTypeTransformations.Types.InfoTypeTransformation
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                CryptoReplaceFfxFpeConfig = new [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.html)
                                {
                                    CommonAlphabet = alphabet,
                                    CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                                    {
                                        KmsWrapped = new [KmsWrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KmsWrappedCryptoKey.html)
                                        {
                                            CryptoKeyName = keyName,
                                            WrappedKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromBase64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromBase64_System_String_) (wrappedKey)
                                        }
                                    },
                                    SurrogateInfoType = new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)
                                    {
                                        Name = "TOKEN"
                                    }
                                }
                            }
                        }
                    }
                }
            };
    
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
            var response = dlp.DeidentifyContent(
                new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
                {
                    Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                    InspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
                    {
                        InfoTypes = { infoTypes }
                    },
                    DeidentifyConfig = deidentifyConfig,
                    Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = dataValue }
                });
    
            Console.WriteLine($"Deidentified content: {response.Item.[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)}");
            return response;
        }
    }
    

##### Format-preserving encryption examples: de-identification with surrogate type

This example uses the [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptoreplaceffxfpeconfig) transformation method to de-identify sensitive data. For more information, see Format-preserving encryption on this page.

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // deidentifyFreeTextWithFPEUsingSurrogate de-identifies free text with FPE by using a surrogate
    func deidentifyFreeTextWithFPEUsingSurrogate(w io.Writer, projectID, inputStr, infoType, surrogateType, unwrappedKey string) error {
    	// projectId := "your-project-id"
    	// inputStr := "My phone number is 9824376677"
    	// infoType := "PHONE_NUMBER"
    	// surrogateType := "PHONE_TOKEN"
    	// unwrappedKey := "The base64-encoded AES-256 key to use"
    
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
    
    	// decoding the unwrapped key
    	keyDecode, err := base64.StdEncoding.DecodeString(unwrappedKey)
    	if err != nil {
    		return err
    	}
    
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: infoType},
    		},
    		MinLikelihood: dlppb.[Likelihood_UNLIKELY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    	}
    
    	// specify the content to be de-identified
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{
    			Value: inputStr,
    		},
    	}
    
    	// Specify how the content should be encrypted.
    	cryptoReplaceConfig := &dlppb.CryptoReplaceFfxFpeConfig{
    		CryptoKey: &dlppb.CryptoKey{
    			Source: &dlppb.CryptoKey_Unwrapped{
    				Unwrapped: &dlppb.UnwrappedCryptoKey{
    					Key: keyDecode,
    				},
    			},
    		},
    		Alphabet: &dlppb.CryptoReplaceFfxFpeConfig_CommonAlphabet{
    			CommonAlphabet: dlppb.[CryptoReplaceFfxFpeConfig_NUMERIC](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_CryptoReplaceFfxFpeConfig_FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED_CryptoReplaceFfxFpeConfig_NUMERIC_CryptoReplaceFfxFpeConfig_HEXADECIMAL_CryptoReplaceFfxFpeConfig_UPPER_CASE_ALPHA_NUMERIC_CryptoReplaceFfxFpeConfig_ALPHA_NUMERIC),
    		},
    		SurrogateInfoType: &dlppb.InfoType{
    			Name: surrogateType,
    		},
    	}
    
    	// Apply crypto replace config to primitive transformation.
    	primitiveTransformation := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_CryptoReplaceFfxFpeConfig{
    			CryptoReplaceFfxFpeConfig: cryptoReplaceConfig,
    		},
    	}
    
    	infoTypeTransformation := &dlppb.DeidentifyConfig_InfoTypeTransformations{
    		InfoTypeTransformations: &dlppb.InfoTypeTransformations{
    			Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    				{
    					InfoTypes: []*dlppb.InfoType{
    						{Name: infoType},
    					},
    					PrimitiveTransformation: primitiveTransformation,
    				},
    			},
    		},
    	}
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: infoTypeTransformation,
    		},
    		InspectConfig: inspectConfig,
    		Item:          contentItem,
    	}
    
    	// Send the request.
    	resp, err := client.DeidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the results.
    	fmt.Fprintf(w, "output: %v", resp.GetItem().GetValue())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.common.io.BaseEncoding;
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html);
    import com.google.privacy.dlp.v2.[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[UnwrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.UnwrappedCryptoKey.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.Base64;
    import java.util.Collections;
    import javax.crypto.KeyGenerator;
    import javax.crypto.SecretKey;
    
    public class DeidentifyFreeTextWithFpeUsingSurrogate {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
    
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The string to de-identify.
        String textToDeIdentify = "My phone number is 4359916732";
        // The base64-encoded key to use.
        String base64EncodedKey = "your-base64-encoded-key";
    
        deIdentifyWithFpeSurrogate(projectId, textToDeIdentify, base64EncodedKey);
      }
    
      /**
       * Uses the Data Loss Prevention API to deidentify sensitive data in a string using Format
       * Preserving Encryption (FPE).The encryption is performed with an unwrapped key.
       *
       * @param projectId The Google Cloud project id to use as a parent resource.
       * @param textToDeIdentify The string to deidentify.
       * @param unwrappedKey The base64-encoded AES-256 key to use.
       */
      public static String deIdentifyWithFpeSurrogate(
          String projectId, String textToDeIdentify, String unwrappedKey) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Set the text to be de-identified.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToDeIdentify).build();
    
          // Specify the InfoType the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder()
                  .setName("PHONE_NUMBER").build();
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                      .addAllInfoTypes(Collections.singletonList(infoType)).build();
    
          // Specify an unwrapped crypto key.
          [UnwrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.UnwrappedCryptoKey.html) unwrappedCryptoKey =
              [UnwrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.UnwrappedCryptoKey.html).newBuilder()
                  .setKey([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(BaseEncoding.base64().decode(unwrappedKey)))
                  .build();
    
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder().[setUnwrapped](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setUnwrapped_com_google_privacy_dlp_v2_UnwrappedCryptoKey_)(unwrappedCryptoKey).build();
    
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) surrogateInfoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PHONE_TOKEN").build();
    
          // Specify how the info from the inspection should be encrypted.
          [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html) cryptoReplaceFfxFpeConfig =
              [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).newBuilder()
                  .setCryptoKey(cryptoKey)
                  // Set of characters in the input text. For more info, see
                  // https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.FfxCommonNativeAlphabet
                  .[setCommonAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.Builder.html#com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_Builder_setCommonAlphabet_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_FfxCommonNativeAlphabet_)([CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).FfxCommonNativeAlphabet.NUMERIC)
                  .setSurrogateInfoType(surrogateInfoType)
                  .build();
    
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoReplaceFfxFpeConfig_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_)(cryptoReplaceFfxFpeConfig)
                  .build();
    
          [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
              [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html).newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) transformations =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder()
                      .[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation).build();
    
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder()
                      .setInfoTypeTransformations(transformations).build();
    
          // Combine configurations into a request for the service.
          [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html) request =
              [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(contentItem)
                  .setInspectConfig(inspectConfig)
                  .setDeidentifyConfig(deidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service.
          [DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html) response = dlp.deidentifyContent(request);
    
          // Print the results.
          System.out.println("Text after de-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getValue());
    
          return response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getValue();
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
    // const projectId = 'my-project';
    
    // The string to de-identify
    // const string = 'My phone number is 4359916732';
    
    // The set of characters to replace sensitive ones with
    // For more information, see https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#ffxcommonnativealphabet
    // const alphabet = 'NUMERIC';
    
    // InfoTypes
    // const infoTypes = [{name: 'PHONE_NUMBER'}];
    
    // Surrogate Type
    // const surrogateType = 'PHONE_TOKEN';
    
    // The base64-encoded AES-256 key to use
    // const unwrappedKey = 'YWJjZGVmZ2hpamtsbW5vcA==';
    
    async function deidentifyWithFpeSurrogate() {
      // Specify an unwrapped crypto key.
      unwrappedKey = Buffer.from(unwrappedKey, 'base64');
    
      // Specify how the info from the inspection should be encrypted.
      const cryptoReplaceFfxFpeConfig = {
        cryptoKey: {
          unwrapped: {
            key: unwrappedKey,
          },
        },
        commonAlphabet: alphabet,
        surrogateInfoType: {name: surrogateType},
      };
    
      // Construct the inspect configuration.
      const inspectConfig = {
        infoTypes: infoTypes,
        minLikelihood: DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[UNLIKELY](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
      };
    
      // Set the text to be de-identified.
      const item = {value: string};
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: {
          infoTypeTransformations: {
            transformations: [
              {
                primitiveTransformation: {
                  cryptoReplaceFfxFpeConfig: cryptoReplaceFfxFpeConfig,
                },
              },
            ],
          },
        },
        item: item,
        inspectConfig: inspectConfig,
      };
      // Run de-identification request
      const [response] = await dlp.deidentifyContent(request);
      const deidentifiedItem = response.item;
      // Print results
      console.log(deidentifiedItem.value);
    }
    deidentifyWithFpeSurrogate();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Deidentify free text with fpe using surrogate.
     * Uses the Data Loss Prevention API to de-identify sensitive data in a string using format-preserving
     * encryption (FPE). The encryption is performed with an unwrapped key.
     *
     * @param string $callingProjectId  The GCP Project ID to run the API call under.
     * @param string $string            The string to deidentify (will be treated as text).
     * @param string $unwrappedKey      The base64-encoded AES-256 key to use.
     * @param string $surrogateTypeName The name of the surrogate custom info type to use.
     * Can be essentially any arbitrary string, as long as it doesn't appear in your dataset otherwise.
     */
    function deidentify_free_text_with_fpe_using_surrogate(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $string = 'My PHONE NUMBER IS 731997681',
        string $unwrappedKey = 'YWJjZGVmZ2hpamtsbW5vcA==',
        string $surrogateTypeName = 'PHONE_TOKEN'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Specify an unwrapped crypto key.
        $unwrapped = (new UnwrappedCryptoKey())
            ->setKey(base64_decode($unwrappedKey));
    
        $cryptoKey = (new CryptoKey())
            ->setUnwrapped($unwrapped);
    
        // Create the surrogate type configuration object.
        $surrogateType = (new InfoType())
            ->setName($surrogateTypeName);
    
        // The set of characters to replace sensitive ones with.
        // For more information, see https://cloud.google.com/dlp/docs/reference/rest/V2/organizations.deidentifyTemplates#ffxcommonnativealphabet
        $commonAlphabet = FfxCommonNativeAlphabet::NUMERIC;
    
        // Specify how to decrypt the previously de-identified information.
        $cryptoReplaceFfxFpeConfig = (new CryptoReplaceFfxFpeConfig())
            ->setCryptoKey($cryptoKey)
            ->setCommonAlphabet($commonAlphabet)
            ->setSurrogateInfoType($surrogateType);
    
        // Create the information transform configuration objects.
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCryptoReplaceFfxFpeConfig($cryptoReplaceFfxFpeConfig);
    
        // The infoTypes of information to mask.
        $infoType = (new InfoType())
            ->setName('PHONE_NUMBER');
        $infoTypes = [$infoType];
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setInfoTypes($infoTypes);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Create the deidentification configuration object.
        $deidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations($infoTypeTransformations);
    
        // Specify the content to be de-identify.
        $content = (new ContentItem())
            ->setValue($string);
    
        // Create the configuration object.
        $inspectConfig = (new InspectConfig())
            /* Construct the inspect config, trying to finding all PII with likelihood
            higher than UNLIKELY */
            ->setMinLikelihood(likelihood::UNLIKELY)
            ->setInfoTypes($infoTypes);
    
        // Run request.
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($content)
            ->setInspectConfig($inspectConfig);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print the results.
        printf($response->getItem()->getValue());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    
    import google.cloud.dlp
    
    
    def deidentify_free_text_with_fpe_using_surrogate(
        project: str,
        input_str: str,
        alphabet: str = "NUMERIC",
        info_type: str = "PHONE_NUMBER",
        surrogate_type: str = "PHONE_TOKEN",
        unwrapped_key: str = "YWJjZGVmZ2hpamtsbW5vcA==",
    ) -> None:
        """Uses the Data Loss Prevention API to deidentify sensitive data in a
           string using Format Preserving Encryption (FPE).
           The encryption is performed with an unwrapped key.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to deidentify (will be treated as text).
            alphabet: The set of characters to replace sensitive ones with. For
                more information, see https://cloud.google.com/dlp/docs/reference/
                rest/v2beta2/organizations.deidentifyTemplates#ffxcommonnativealphabet
            info_type: The name of the info type to de-identify
            surrogate_type: The name of the surrogate custom info type to use. Can
                be essentially any arbitrary string, as long as it doesn't appear
                in your dataset otherwise.
            unwrapped_key: The base64-encoded AES-256 key to use.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # The wrapped key is base64-encoded, but the library expects a binary
        # string, so decode it here.
        unwrapped_key = base64.b64decode(unwrapped_key)
    
        # Construct de-identify config
        transformation = {
            "info_types": [{"name": info_type}],
            "primitive_transformation": {
                "crypto_replace_ffx_fpe_config": {
                    "crypto_key": {"unwrapped": {"key": unwrapped_key}},
                    "common_alphabet": alphabet,
                    "surrogate_info_type": {"name": surrogate_type},
                }
            },
        }
    
        deidentify_config = {
            "info_type_transformations": {"transformations": [transformation]}
        }
    
        # Construct the inspect config, trying to finding all PII with likelihood
        # higher than UNLIKELY
        inspect_config = {
            "info_types": [{"name": info_type}],
            "min_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).UNLIKELY,
        }
    
        # Convert string to item
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
    
        # Print results
        print(response.item.value)
    
    

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using static Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types;
    
    public class DeidentifyFreeTextWithFpeUsingSurrogate
    {
        public static DeidentifyContentResponse Deidentify(
            string projectId,
            string text,
            string unwrappedKey,
            IEnumerable<InfoType> infoTypes = null,
            [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html) alphabet = [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html).Numeric,
            [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) surrogateType = null)
        {
            // Instantiate a client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Specify the type of info to be inspected and construct the inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes =
                {
                    infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[]
                    {
                        new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_NUMBER" }
                    }
                },
                MinLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Unlikely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Unlikely)
            };
    
            // Construct the crypto replace ffxfpe config by providing the unwrapped crypto key.
            var cryptoReplaceFfxFpeConfig = new [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.html)
            {
                CommonAlphabet = alphabet,
                CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                {
                    Unwrapped = new [UnwrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UnwrappedCryptoKey.html)
                    {
                        Key = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromBase64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromBase64_System_String_)(unwrappedKey)
                    }
                },
                SurrogateInfoType = surrogateType ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_TOKEN" }
            };
    
            // Construct the deidentify config using crypto config created above.
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations =
                    {
                        new InfoTypeTransformations.Types.InfoTypeTransformation
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                CryptoReplaceFfxFpeConfig = cryptoReplaceFfxFpeConfig
                            }
                        }
                    }
                }
            };
    
            // Construct the request.
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                DeidentifyConfig = deidentifyConfig,
                InspectConfig = inspectConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text }
            };
    
            // Call the API.
            [DeidentifyContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentResponse.html) response = dlp.DeidentifyContent(request);
    
            // Check the de-identified content.
            Console.WriteLine($"De-identified content: {response.[Item](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentResponse.html#Google_Cloud_Dlp_V2_DeidentifyContentResponse_Item).[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)}");
            return response;
        }
    }
    
    

##### Format-preserving encryption examples: de-identification of sensitive data in tables

This example uses the [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptoreplaceffxfpeconfig) transformation method to de-identify sensitive data in tables. For more information, see Format-preserving encryption on this page.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using static Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types;
    
    public class DeidentifyTableWithFpe
    {
        public static Table DeidentifyTable(
            string projectId,
            string keyName,
            string wrappedKey,
            [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html) alphabet = [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html).Numeric,
            [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html) tableToInspect = null)
        {
            // Instantiate a client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the table if null.
            if (tableToInspect == null)
            {
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "11111" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "2015" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "$10" }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "33333" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "2016" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "$20" }
                };
                var row3 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "22222" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "2016" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "$15" }
                };
    
                tableToInspect = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                {
                    Headers =
                    {
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Employee ID" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Date" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Compensation" }
                    },
                    Rows =
                    {
                        new Table.Types.Row { Values = { row1 } },
                        new Table.Types.Row { Values = { row2 } },
                        new Table.Types.Row { Values = { row3 } }
                    }
                };
            }
    
            // Provide the table and construct the content item.
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Table = tableToInspect };
    
            // Specify an encrypted AES-256 key and the name of the Cloud KMS Key that
            // encrypted it and specify how it should be encrypted.
            var cryptoReplaceFfxFpeConfig = new [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.html)
            {
                CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                {
                    KmsWrapped = new [KmsWrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KmsWrappedCryptoKey.html)
                    {
                        CryptoKeyName = keyName,
                        WrappedKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromBase64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromBase64_System_String_)(wrappedKey)
                    }
                },
                CommonAlphabet = alphabet
            };
    
            // Specify fields to be encrypted.
            var fields = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html)[] { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Employee ID" } };
    
            // Construct the deidentify config using crypto replace config created above.
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                RecordTransformations = new [RecordTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformations.html)
                {
                    FieldTransformations =
                    {
                        new [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.html)
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                CryptoReplaceFfxFpeConfig = cryptoReplaceFfxFpeConfig
                            },
                            Fields = { fields }
                        }
                    }
                }
            };
    
            // Construct the request.
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                DeidentifyConfig = deidentifyConfig,
                Item = contentItem,
            };
    
            // Call the API.
            [DeidentifyContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentResponse.html) response = dlp.DeidentifyContent(request);
    
            // Inspect the response.
            Console.WriteLine(response.[Item](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentResponse.html#Google_Cloud_Dlp_V2_DeidentifyContentResponse_Item).[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html));
    
            return response.[Item](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentResponse.html#Google_Cloud_Dlp_V2_DeidentifyContentResponse_Item).[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html);
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // deidentifyTableFPE de-identifies table data with format preserving encryption.
    func deidentifyTableFPE(w io.Writer, projectID string, kmsKeyName, wrappedAESKey string) error {
    	// projectId := "your-project-id"
    	/* keyFileName :=  "projects/YOUR_PROJECT/"
    	   + "locations/YOUR_KEYRING_REGION/"
    	   + "keyRings/YOUR_KEYRING_NAME/"
    	   + "cryptoKeys/YOUR_KEY_NAME"
    	*/
    	// wrappedAESKey := "YOUR_ENCRYPTED_AES_256_KEY"
    
    	// define your table.
    	row1 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "11111"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "2015"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "$10"}},
    		},
    	}
    
    	row2 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "22222"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "2016"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "$20"}},
    		},
    	}
    
    	row3 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "33333"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "2016"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "$15"}},
    		},
    	}
    
    	table := &dlppb.Table{
    		Headers: []*dlppb.FieldId{
    			{Name: "Employee ID"},
    			{Name: "Date"},
    			{Name: "Compensation"},
    		},
    		Rows: []*dlppb.Table_Row{
    			{Values: row1.Values},
    			{Values: row2.Values},
    			{Values: row3.Values},
    		},
    	}
    
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
    
    	// Specify what content you want the service to de-identify.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Table{
    			Table: table,
    		},
    	}
    
    	// Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
    	kmsKeyDecode, err := base64.StdEncoding.DecodeString(wrappedAESKey)
    	if err != nil {
    		return fmt.Errorf("error in decoding key: %w", err)
    	}
    
    	kmsWrappedCryptoKey := &dlppb.KmsWrappedCryptoKey{
    		WrappedKey:    kmsKeyDecode,
    		CryptoKeyName: kmsKeyName,
    	}
    
    	cryptoKey := &dlppb.CryptoKey_KmsWrapped{
    		KmsWrapped: kmsWrappedCryptoKey,
    	}
    
    	// Specify how the content should be encrypted.
    	cryptoReplaceFfxFpeConfig := &dlppb.CryptoReplaceFfxFpeConfig{
    		CryptoKey: &dlppb.CryptoKey{
    			Source: cryptoKey,
    		},
    		Alphabet: &dlppb.CryptoReplaceFfxFpeConfig_CommonAlphabet{
    			CommonAlphabet: dlppb.[CryptoReplaceFfxFpeConfig_NUMERIC](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_CryptoReplaceFfxFpeConfig_FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED_CryptoReplaceFfxFpeConfig_NUMERIC_CryptoReplaceFfxFpeConfig_HEXADECIMAL_CryptoReplaceFfxFpeConfig_UPPER_CASE_ALPHA_NUMERIC_CryptoReplaceFfxFpeConfig_ALPHA_NUMERIC),
    		},
    	}
    
    	primitiveTransformation := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_CryptoReplaceFfxFpeConfig{
    			CryptoReplaceFfxFpeConfig: cryptoReplaceFfxFpeConfig,
    		},
    	}
    
    	// Specify field to be encrypted.
    	fieldId := &dlppb.FieldId{
    		Name: "Employee ID",
    	}
    
    	// Associate the encryption with the specified field.
    	fieldTransformation := &dlppb.FieldTransformation{
    		Fields: []*dlppb.FieldId{
    			fieldId,
    		},
    		Transformation: &dlppb.FieldTransformation_PrimitiveTransformation{
    			PrimitiveTransformation: primitiveTransformation,
    		},
    	}
    
    	transformations := &dlppb.RecordTransformations{
    		FieldTransformations: []*dlppb.FieldTransformation{
    			fieldTransformation,
    		},
    	}
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: &dlppb.DeidentifyConfig_RecordTransformations{
    				RecordTransformations: transformations,
    			},
    		},
    		Item: contentItem,
    	}
    
    	// Send the request.
    	resp, err := client.DeidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the results.
    	fmt.Fprintf(w, "De-identify Table after format-preserving encryption : %+v", resp.GetItem().GetTable())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.common.io.BaseEncoding;
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html);
    import com.google.privacy.dlp.v2.[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html);
    import com.google.privacy.dlp.v2.[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).[FfxCommonNativeAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html);
    import com.google.privacy.dlp.v2.[KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class DeIdentifyTableWithFpe {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String kmsKeyName =
            "projects/YOUR_PROJECT/"
                + "locations/YOUR_KEYRING_REGION/"
                + "keyRings/YOUR_KEYRING_NAME/"
                + "cryptoKeys/YOUR_KEY_NAME";
        String wrappedAesKey = "YOUR_ENCRYPTED_AES_256_KEY";
        [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify =
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder()
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Employee ID").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Date").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Compensation").build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().setStringValue("11111").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().setStringValue("2015").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().setStringValue("$10").build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().setStringValue("22222").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().setStringValue("2016").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().setStringValue("$20").build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().setStringValue("33333").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().setStringValue("2016").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().setStringValue("$15").build())
                        .build())
                .build();
        deIdentifyTableWithFpe(projectId, tableToDeIdentify, kmsKeyName, wrappedAesKey);
      }
    
      public static void deIdentifyTableWithFpe(
          String projectId, [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify, String kmsKeyName, String wrappedAesKey)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to de-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(tableToDeIdentify).build();
    
          // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it
          [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html) kmsWrappedCryptoKey =
              [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html).newBuilder()
                  .[setWrappedKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setWrappedKey_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(BaseEncoding.base64().decode(wrappedAesKey)))
                  .[setCryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setCryptoKeyName_java_lang_String_)(kmsKeyName)
                  .build();
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder().[setKmsWrapped](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setKmsWrapped_com_google_privacy_dlp_v2_KmsWrappedCryptoKey_)(kmsWrappedCryptoKey).build();
    
          // Specify how the content should be encrypted.
          [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html) cryptoReplaceFfxFpeConfig =
              [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).newBuilder()
                  .setCryptoKey(cryptoKey)
                  // Set of characters in the input text. For more info, see
                  // https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.FfxCommonNativeAlphabet
                  .[setCommonAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.Builder.html#com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_Builder_setCommonAlphabet_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_FfxCommonNativeAlphabet_)([FfxCommonNativeAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet.html).NUMERIC)
                  .build();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoReplaceFfxFpeConfig_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_)(cryptoReplaceFfxFpeConfig)
                  .build();
    
          // Specify field to be encrypted.
          [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html) fieldId = [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Employee ID").build();
    
          // Associate the encryption with the specified field.
          [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html) fieldTransformation =
              [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html).newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .addFields(fieldId)
                  .build();
          [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html) transformations =
              [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html).newBuilder().addFieldTransformations(fieldTransformation).build();
    
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder().[setRecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.Builder.html#com_google_privacy_dlp_v2_DeidentifyConfig_Builder_setRecordTransformations_com_google_privacy_dlp_v2_RecordTransformations_)(transformations).build();
    
          // Combine configurations into a request for the service.
          [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html) request =
              [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(contentItem)
                  .setDeidentifyConfig(deidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service.
          [DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html) response = dlp.deidentifyContent(request);
    
          // Print the results.
          System.out.println(
              "Table after format-preserving encryption: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getTable());
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
    // const projectId = 'my-project';
    
    // The set of characters to replace sensitive ones with
    // For more information, see https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#ffxcommonnativealphabet
    // const alphabet = 'NUMERIC';
    
    // The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key
    // const keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME';
    
    // The encrypted ('wrapped') AES-256 key to use
    // This key should be encrypted using the Cloud KMS key specified above
    // const wrappedKey = 'YOUR_ENCRYPTED_AES_256_KEY'
    
    // Table to de-identify
    const tablularData = {
      headers: [{name: 'Employee ID'}, {name: '[Date](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.type.date.html)'}, {name: 'Compensation'}],
      rows: [
        {
          values: [
            {stringValue: '11111'},
            {stringValue: '2015'},
            {stringValue: '$10'},
          ],
        },
        {
          values: [
            {stringValue: '22222'},
            {stringValue: '2016'},
            {stringValue: '$20'},
          ],
        },
        {
          values: [
            {stringValue: '33333'},
            {stringValue: '2016'},
            {stringValue: '$15'},
          ],
        },
      ],
    };
    
    async function deidentifyTableWithFpe() {
      // Specify field to be encrypted.
      const fieldIds = [{name: 'Employee ID'}];
    
      // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it
      const cryptoKeyConfig = {
        kmsWrapped: {
          wrappedKey: wrappedKey,
          cryptoKeyName: keyName,
        },
      };
    
      // Specify how the content should be encrypted.
      const cryptoReplaceFfxFpeConfig = {
        cryptoKey: cryptoKeyConfig,
        commonAlphabet: alphabet,
      };
    
      // Associate the encryption with the specified field.
      const fieldTransformations = [
        {
          fields: fieldIds,
          primitiveTransformation: {
            cryptoReplaceFfxFpeConfig,
          },
        },
      ];
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: {
          recordTransformations: {
            fieldTransformations,
          },
        },
        item: {
          table: tablularData,
        },
      };
    
      // Send the request and receive response from the service.
      const [response] = await dlp.deidentifyContent(request);
    
      // Print the results.
      console.log(
        `Table after de-identification: ${JSON.stringify(response.item.table)}`
      );
    }
    await deidentifyTableWithFpe();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoKey;
    use Google\Cloud\Dlp\V2\CryptoReplaceFfxFpeConfig;
    use Google\Cloud\Dlp\V2\CryptoReplaceFfxFpeConfig\FfxCommonNativeAlphabet;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\FieldTransformation;
    use Google\Cloud\Dlp\V2\KmsWrappedCryptoKey;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\RecordTransformations;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * De-identify table data with format-preserving encryption.
     * Demonstrates encrypting sensitive data in a table while maintaining format.
     *
    
     * @param string $callingProjectId      The Google Cloud project id to use as a parent resource.
     * @param string $inputCsvFile          The input file(csv) path  to deidentify.
     * @param string $outputCsvFile         The oupt file path to save deidentify content.
     * @param string $encryptedFieldNames   The field to be encrypted.
     * @param string $kmsKeyName            The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key.
     * Example: key_name = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
     * @param string $wrappedAesKey         The encrypted ('wrapped') AES-256 key to use.
    
     * */
    
    function deidentify_table_fpe(
        string $callingProjectId,
        string $inputCsvFile,
        string $outputCsvFile,
        string $encryptedFieldNames,
        string $kmsKeyName,
        string $wrappedAesKey
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Read a CSV file.
        $csvLines = file($inputCsvFile, FILE_IGNORE_NEW_LINES);
        $csvHeaders = explode(',', $csvLines[0]);
        $csvRows = array_slice($csvLines, 1);
    
        // Convert CSV file into protobuf objects.
        $tableHeaders = array_map(function ($csvHeader) {
            return (new FieldId)
                ->setName($csvHeader);
        }, $csvHeaders);
    
        $tableRows = array_map(function ($csvRow) {
            $rowValues = array_map(function ($csvValue) {
                return (new Value())
                    ->setStringValue($csvValue);
            }, explode(',', $csvRow));
            return (new Row())
                ->setValues($rowValues);
        }, $csvRows);
    
        // Construct the table object.
        $tableToDeIdentify = (new Table())
            ->setHeaders($tableHeaders)
            ->setRows($tableRows);
    
        // Specify the content to be de-identify.
        $content = (new ContentItem())
            ->setTable($tableToDeIdentify);
    
        // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
        $kmsWrappedCryptoKey = (new KmsWrappedCryptoKey())
            ->setWrappedKey(base64_decode($wrappedAesKey))
            ->setCryptoKeyName($kmsKeyName);
    
        $cryptoKey = (new CryptoKey())
            ->setKmsWrapped($kmsWrappedCryptoKey);
    
        // Specify how the content should be encrypted.
        $cryptoReplaceFfxFpeConfig = (new CryptoReplaceFfxFpeConfig())
            ->setCryptoKey($cryptoKey)
            ->setCommonAlphabet(FfxCommonNativeAlphabet::NUMERIC);
    
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCryptoReplaceFfxFpeConfig($cryptoReplaceFfxFpeConfig);
    
        // Specify field to be encrypted.
        $encryptedFields = array_map(function ($encryptedFieldName) {
            return (new FieldId())
                ->setName($encryptedFieldName);
        }, explode(',', $encryptedFieldNames));
    
        // Associate the encryption with the specified field.
        $fieldTransformation = (new FieldTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setFields($encryptedFields);
    
        $recordtransformations = (new RecordTransformations())
            ->setFieldTransformations([$fieldTransformation]);
    
        $deidentifyConfig = (new DeidentifyConfig())
            ->setRecordTransformations($recordtransformations);
    
        // Run request.
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($content);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print the results.
        $csvRef = fopen($outputCsvFile, 'w');
        fputcsv($csvRef, $csvHeaders);
        foreach ($response->getItem()->getTable()->getRows() as $tableRow) {
            $values = array_map(function ($tableValue) {
                return $tableValue->getStringValue();
            }, iterator_to_array($tableRow->getValues()));
            fputcsv($csvRef, $values);
        };
        printf('Table after format-preserving encryption (File Location): %s', $outputCsvFile);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    import google.cloud.dlp
    
    
    def deidentify_table_with_fpe(
        project: str,
        table_header: List[str],
        table_rows: List[List[str]],
        deid_field_names: List[str],
        key_name: str = None,
        wrapped_key: bytes = None,
        alphabet: str = None,
    ) -> None:
        """Uses the Data Loss Prevention API to de-identify sensitive data in a
          table while maintaining format.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            table_header: List of strings representing table field names.
            table_rows: List of rows representing table data.
            deid_field_names: A list of fields in table to de-identify.
            key_name: The name of the Cloud KMS key used to encrypt ('wrap') the
                AES-256 key. Example:
                key_name = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/
                keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
            wrapped_key: The decrypted ('wrapped', in bytes) AES-256 key to use. This key
                should be encrypted using the Cloud KMS key specified by key_name.
            alphabet: The set of characters to replace sensitive ones with. For
                more information, see https://cloud.google.com/dlp/docs/reference/
                rest/v2/projects.deidentifyTemplates#ffxcommonnativealphabet
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the `table`. For more details on the table schema, please see
        # https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem#Table
        headers = [{"name": val} for val in table_header]
        rows = []
        for row in table_rows:
            rows.append({"values": [{"string_value": cell_val} for cell_val in row]})
    
        table = {"headers": headers, "rows": rows}
    
        # Construct the `item` for table.
        item = {"table": table}
    
        # Specify fields to be de-identified.
        deid_field_names = [{"name": _i} for _i in deid_field_names]
    
        # Construct FPE configuration dictionary
        crypto_replace_ffx_fpe_config = {
            "crypto_key": {
                "kms_wrapped": {"wrapped_key": wrapped_key, "crypto_key_name": key_name},
            },
            "common_alphabet": alphabet,
        }
    
        # Construct deidentify configuration dictionary
        deidentify_config = {
            "record_transformations": {
                "field_transformations": [
                    {
                        "primitive_transformation": {
                            "crypto_replace_ffx_fpe_config": crypto_replace_ffx_fpe_config
                        },
                        "fields": deid_field_names,
                    }
                ]
            }
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API.
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={"parent": parent, "deidentify_config": deidentify_config, "item": item}
        )
    
        # Print out results.
        print(f"Table after de-identification: {response.item.table}")
    
    

##### Format-preserving encryption examples: re-identification

Following is sample code in several languages that demonstrates how to use Sensitive Data Protection to re-identify sensitive data that was de-identified through the [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptoreplaceffxfpeconfig) transformation method. For more information, see Format-preserving encryption on this page.

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // reidentifyFPE reidentifies the input with FPE (Format Preserving Encryption).
    // keyFileName is the file name with the KMS wrapped key and cryptoKeyName is the
    // full KMS key resource name used to wrap the key. surrogateInfoType is an
    // the identifier used during deidentification.
    // Info types can be found with the infoTypes.list method or on https://cloud.google.com/dlp/docs/infotypes-reference
    func reidentifyFPE(w io.Writer, projectID, input, kmsKeyName, wrappedAesKey, surrogateInfoType string) error {
    	// projectID := "my-project-id"
    	// input := "My SSN is 123456789"
    	// keyFileName := "projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME"
    	// cryptoKeyName := "YOUR_ENCRYPTED_AES_256_KEY"
    	// surrogateInfoType := "AGE"
    	ctx := context.Background()
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
    	kmsWrappedCryptoKey, err := base64.StdEncoding.DecodeString(wrappedAesKey)
    	if err != nil {
    		fmt.Fprintf(w, "error %v", err)
    		return err
    	}
    
    	// Specify the crypto key configuration that will used for encryption.
    	cryptoKey := &dlppb.CryptoKey{
    		Source: &dlppb.CryptoKey_KmsWrapped{
    			KmsWrapped: &dlppb.KmsWrappedCryptoKey{
    				WrappedKey:    kmsWrappedCryptoKey,
    				CryptoKeyName: kmsKeyName,
    			},
    		},
    	}
    
    	// Create a configured request.
    	req := &dlppb.ReidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		ReidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    				InfoTypeTransformations: &dlppb.InfoTypeTransformations{
    					Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    						{
    							InfoTypes: []*dlppb.InfoType{},
    							PrimitiveTransformation: &dlppb.PrimitiveTransformation{
    								Transformation: &dlppb.PrimitiveTransformation_CryptoReplaceFfxFpeConfig{
    									CryptoReplaceFfxFpeConfig: &dlppb.CryptoReplaceFfxFpeConfig{
    										CryptoKey: cryptoKey,
    										// Set the alphabet used for the encrypted fields.
    										Alphabet: &dlppb.CryptoReplaceFfxFpeConfig_CommonAlphabet{
    											CommonAlphabet: dlppb.[CryptoReplaceFfxFpeConfig_ALPHA_NUMERIC](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_CryptoReplaceFfxFpeConfig_FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED_CryptoReplaceFfxFpeConfig_NUMERIC_CryptoReplaceFfxFpeConfig_HEXADECIMAL_CryptoReplaceFfxFpeConfig_UPPER_CASE_ALPHA_NUMERIC_CryptoReplaceFfxFpeConfig_ALPHA_NUMERIC),
    										},
    										// Set the surrogate info type used during deidentification.
    										SurrogateInfoType: &dlppb.InfoType{
    											Name: surrogateInfoType,
    										},
    									},
    								},
    							},
    						},
    					},
    				},
    			},
    		},
    		// The InspectConfig must identify the surrogate info type to reidentify.
    		InspectConfig: &dlppb.InspectConfig{
    			CustomInfoTypes: []*dlppb.CustomInfoType{
    				{
    					InfoType: &dlppb.InfoType{
    						Name: surrogateInfoType,
    					},
    					Type: &dlppb.CustomInfoType_SurrogateType_{
    						SurrogateType: &dlppb.CustomInfoType_SurrogateType{},
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
    	r, err := client.ReidentifyContent(ctx, req)
    	if err != nil {
    		return fmt.Errorf("ReidentifyContent: %w", err)
    	}
    	// Print the result.
    	fmt.Fprint(w, r.GetItem().GetValue())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.common.io.BaseEncoding;
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html);
    import com.google.privacy.dlp.v2.[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html);
    import com.google.privacy.dlp.v2.[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).[FfxCommonNativeAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[SurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.SurrogateType.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class ReIdentifyWithFpe {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToReIdentify = "My SSN is SSN_TOKEN(9):731997681";
        String kmsKeyName =
            "projects/YOUR_PROJECT/"
                + "locations/YOUR_KEYRING_REGION/"
                + "keyRings/YOUR_KEYRING_NAME/"
                + "cryptoKeys/YOUR_KEY_NAME";
        String wrappedAesKey = "YOUR_ENCRYPTED_AES_256_KEY";
        reIdentifyWithFpe(projectId, textToReIdentify, kmsKeyName, wrappedAesKey);
      }
    
      public static void reIdentifyWithFpe(
          String projectId, String textToReIdentify, String kmsKeyName, String wrappedAesKey)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to re-identify
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToReIdentify).build();
    
          // Specify the type of info the inspection will re-identify. This must use the same custom
          // into type that was used as a surrogate during the initial encryption.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) surrogateInfoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("SSN_TOKEN").build();
    
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder()
                  .setInfoType(surrogateInfoType)
                  .[setSurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Builder_setSurrogateType_com_google_privacy_dlp_v2_CustomInfoType_SurrogateType_)([SurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.SurrogateType.html).getDefaultInstance())
                  .build();
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType).build();
    
          // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it
          [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html) kmsWrappedCryptoKey =
              [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html).newBuilder()
                  .[setWrappedKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setWrappedKey_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(BaseEncoding.base64().decode(wrappedAesKey)))
                  .[setCryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setCryptoKeyName_java_lang_String_)(kmsKeyName)
                  .build();
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder().[setKmsWrapped](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setKmsWrapped_com_google_privacy_dlp_v2_KmsWrappedCryptoKey_)(kmsWrappedCryptoKey).build();
    
          // Specify how to un-encrypt the previously de-identified information
          [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html) cryptoReplaceFfxFpeConfig =
              [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).newBuilder()
                  .setCryptoKey(cryptoKey)
                  // Set of characters in the input text. For more info, see
                  // https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.FfxCommonNativeAlphabet
                  .[setCommonAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.Builder.html#com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_Builder_setCommonAlphabet_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_FfxCommonNativeAlphabet_)([FfxCommonNativeAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet.html).NUMERIC)
                  .setSurrogateInfoType(surrogateInfoType)
                  .build();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoReplaceFfxFpeConfig_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_)(cryptoReplaceFfxFpeConfig)
                  .build();
          [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
              [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html).newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .addInfoTypes(surrogateInfoType)
                  .build();
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) transformations =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation).build();
    
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) reidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder().setInfoTypeTransformations(transformations).build();
    
          // Combine configurations into a request for the service.
          [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html) request =
              [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(contentItem)
                  .setInspectConfig(inspectConfig)
                  .[setReidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.Builder.html#com_google_privacy_dlp_v2_ReidentifyContentRequest_Builder_setReidentifyConfig_com_google_privacy_dlp_v2_DeidentifyConfig_)(reidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service
          [ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html) response = dlp.reidentifyContent(request);
    
          // Print the results
          System.out.println("Text after re-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html#com_google_privacy_dlp_v2_ReidentifyContentResponse_getItem__)().getValue());
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
    // const projectId = 'my-project';
    
    // The string to reidentify
    // const string = 'My SSN is PHONE_TOKEN(9):#########';
    
    // The set of characters to replace sensitive ones with
    // For more information, see https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#ffxcommonnativealphabet
    // const alphabet = 'ALPHA_NUMERIC';
    
    // The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key
    // const keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME';
    
    // The encrypted ('wrapped') AES-256 key to use
    // This key should be encrypted using the Cloud KMS key specified above
    // const wrappedKey = 'YOUR_ENCRYPTED_AES_256_KEY'
    
    // The name of the surrogate custom info type to use when reidentifying data
    // const surrogateType = 'SOME_INFO_TYPE_DEID';
    
    async function reidentifyWithFpe() {
      // Construct deidentification request
      const item = {value: string};
      const request = {
        parent: `projects/${projectId}/locations/global`,
        reidentifyConfig: {
          infoTypeTransformations: {
            transformations: [
              {
                primitiveTransformation: {
                  cryptoReplaceFfxFpeConfig: {
                    cryptoKey: {
                      kmsWrapped: {
                        wrappedKey: wrappedKey,
                        cryptoKeyName: keyName,
                      },
                    },
                    commonAlphabet: alphabet,
                    surrogateInfoType: {
                      name: surrogateType,
                    },
                  },
                },
              },
            ],
          },
        },
        inspectConfig: {
          customInfoTypes: [
            {
              infoType: {
                name: surrogateType,
              },
              surrogateType: {},
            },
          ],
        },
        item: item,
      };
    
      // Run reidentification request
      const [response] = await dlp.reidentifyContent(request);
      const reidentifiedItem = response.item;
      console.log(reidentifiedItem.value);
    }
    reidentifyWithFpe();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoKey;
    use Google\Cloud\Dlp\V2\CryptoReplaceFfxFpeConfig;
    use Google\Cloud\Dlp\V2\CryptoReplaceFfxFpeConfig\FfxCommonNativeAlphabet;
    use Google\Cloud\Dlp\V2\CustomInfoType;
    use Google\Cloud\Dlp\V2\CustomInfoType\SurrogateType;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\KmsWrappedCryptoKey;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\ReidentifyContentRequest;
    
    /**
     * Reidentify a deidentified string using Format-Preserving Encryption (FPE).
     *
     * @param string $callingProjectId  The GCP Project ID to run the API call under
     * @param string $string            The string to reidentify
     * @param string $keyName           The name of the Cloud KMS key used to encrypt (wrap) the AES-256 key
     * @param string $wrappedKey        The name of the Cloud KMS key use, encrypted with the KMS key in $keyName
     * @param string $surrogateTypeName (Optional) Surrogate custom info type to enable reidentification
     */
    function reidentify_fpe(
        string $callingProjectId,
        string $string,
        string $keyName,
        string $wrappedKey,
        string $surrogateTypeName
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // The infoTypes of information to mask
        $ssnInfoType = (new InfoType())
            ->setName('US_SOCIAL_SECURITY_NUMBER');
        $infoTypes = [$ssnInfoType];
    
        // The set of characters to replace sensitive ones with
        // For more information, see https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#ffxcommonnativealphabet
        $commonAlphabet = FfxCommonNativeAlphabet::NUMERIC;
    
        // Create the wrapped crypto key configuration object
        $kmsWrappedCryptoKey = (new KmsWrappedCryptoKey())
            ->setWrappedKey(base64_decode($wrappedKey))
            ->setCryptoKeyName($keyName);
    
        // Create the crypto key configuration object
        $cryptoKey = (new CryptoKey())
            ->setKmsWrapped($kmsWrappedCryptoKey);
    
        // Create the surrogate type object
        $surrogateType = (new InfoType())
            ->setName($surrogateTypeName);
    
        $customInfoType = (new CustomInfoType())
            ->setInfoType($surrogateType)
            ->setSurrogateType(new SurrogateType());
    
        // Create the crypto FFX FPE configuration object
        $cryptoReplaceFfxFpeConfig = (new CryptoReplaceFfxFpeConfig())
            ->setCryptoKey($cryptoKey)
            ->setCommonAlphabet($commonAlphabet)
            ->setSurrogateInfoType($surrogateType);
    
        // Create the information transform configuration objects
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCryptoReplaceFfxFpeConfig($cryptoReplaceFfxFpeConfig);
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Create the inspect configuration object
        $inspectConfig = (new InspectConfig())
            ->setCustomInfoTypes([$customInfoType]);
    
        // Create the reidentification configuration object
        $reidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations($infoTypeTransformations);
    
        $item = (new ContentItem())
            ->setValue($string);
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Run request
        $reidentifyContentRequest = (new ReidentifyContentRequest())
            ->setParent($parent)
            ->setReidentifyConfig($reidentifyConfig)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->reidentifyContent($reidentifyContentRequest);
    
        // Print the results
        $reidentifiedValue = $response->getItem()->getValue();
        print($reidentifiedValue);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    
    import google.cloud.dlp
    
    
    def reidentify_with_fpe(
        project: str,
        input_str: str,
        alphabet: str = None,
        surrogate_type: str = None,
        key_name: str = None,
        wrapped_key: str = None,
    ) -> None:
        """Uses the Data Loss Prevention API to reidentify sensitive data in a
        string that was encrypted by Format Preserving Encryption (FPE).
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to deidentify (will be treated as text).
            alphabet: The set of characters to replace sensitive ones with. For
                more information, see https://cloud.google.com/dlp/docs/reference/
                rest/v2beta2/organizations.deidentifyTemplates#ffxcommonnativealphabet
            surrogate_type: The name of the surrogate custom info type to used
                during the encryption process.
            key_name: The name of the Cloud KMS key used to encrypt ('wrap') the
                AES-256 key. Example:
                keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/
                keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
            wrapped_key: The encrypted ('wrapped') AES-256 key to use. This key
                should be encrypted using the Cloud KMS key specified by key_name.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # The wrapped key is base64-encoded, but the library expects a binary
        # string, so decode it here.
        wrapped_key = base64.b64decode(wrapped_key)
    
        # Construct Deidentify Config
        reidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {
                        "primitive_transformation": {
                            "crypto_replace_ffx_fpe_config": {
                                "crypto_key": {
                                    "kms_wrapped": {
                                        "wrapped_key": wrapped_key,
                                        "crypto_key_name": key_name,
                                    }
                                },
                                "common_alphabet": alphabet,
                                "surrogate_info_type": {"name": surrogate_type},
                            }
                        }
                    }
                ]
            }
        }
    
        inspect_config = {
            "custom_info_types": [
                {"info_type": {"name": surrogate_type}, "surrogate_type": {}}
            ]
        }
    
        # Convert string to item
        item = {"value": input_str}
    
        # Call the API
        response = dlp.[reidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_reidentify_content)(
            request={
                "parent": parent,
                "reidentify_config": reidentify_config,
                "inspect_config": inspect_config,
                "item": item,
            }
        )
    
        # Print results
        print(response.item.value)
    
    

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using static Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types;
    
    public class ReidentifyContentUsingFpe
    {
        public static ReidentifyContentResponse ReidentifyContent(
            string projectId,
            string text,
            string keyName,
            string wrappedKey,
            [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html) alphabet = [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html).Numeric,
            [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) surrogateType = null)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Specify the type of info the inspection will re-identify. This must use the same custom
            // info type that was used as a surrogate during the initial encryption.
            var infotype = surrogateType ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "SSN_TOKEN" };
    
            // Specify how to un-encrypt the previously de-identified information.
            var cryptoReplaceFfxFpeConfig = new [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.html)
            {
                CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                {
                    KmsWrapped = new [KmsWrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KmsWrappedCryptoKey.html)
                    {
                        CryptoKeyName = keyName,
                        WrappedKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromBase64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromBase64_System_String_)(wrappedKey)
                    }
                },
                CommonAlphabet = alphabet,
                SurrogateInfoType = infotype
            };
    
            // Construct reidentify config using above created crypto replace config.
            var reidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations =
                    {
                        new InfoTypeTransformations.Types.InfoTypeTransformation
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                CryptoReplaceFfxFpeConfig = cryptoReplaceFfxFpeConfig,
                            },
                            InfoTypes = { infotype }
                        }
                    }
                }
            };
    
            // Construct the inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                CustomInfoTypes =
                {
                    new [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html)
                    {
                        InfoType = infotype,
                        SurrogateType = new CustomInfoType.Types.SurrogateType()
                    }
                }
            };
    
            // Construct the request.
            var request = new [ReidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                InspectConfig = inspectConfig,
                ReidentifyConfig = reidentifyConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text },
            };
    
            // Call the API.
            var response = dlp.ReidentifyContent(request);
    
            // Inspect the response.
            Console.WriteLine($"Reidentified content: {response.Item.[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)}");
    
            return response;
        }
    }
    

##### Format-preserving encryption examples: re-identification of text

Following is sample code in several languages that demonstrates how to use Sensitive Data Protection to re-identify sensitive text that was de-identified through the [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptoreplaceffxfpeconfig) transformation method. For more information, see Format-preserving encryption on this page.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using static Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types;
    
    public class ReidentifyFreeTextFpe
    {
        public static ReidentifyContentResponse ReidentifyContent(
            string projectId,
            string text,
            string keyName,
            string wrappedKey,
            [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html) alphabet = [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html).Numeric,
            [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) surrogateType = null)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the infoType which will be used as both surrogate type and infoType.
            var infotype = surrogateType ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_TOKEN" };
    
            // Specify how to un-encrypt the previously de-identified information.
            var cryptoReplaceFfxFpeConfig = new [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.html)
            {
                CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                {
                    KmsWrapped = new [KmsWrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KmsWrappedCryptoKey.html)
                    {
                        CryptoKeyName = keyName,
                        WrappedKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromBase64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromBase64_System_String_)(wrappedKey)
                    }
                },
                CommonAlphabet = alphabet,
                SurrogateInfoType = infotype
            };
    
            // Construct re-identify config using the CryptoReplaceFfxFpeConfig transformation method.
            var reidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations =
                    {
                        new InfoTypeTransformations.Types.InfoTypeTransformation
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                CryptoReplaceFfxFpeConfig = cryptoReplaceFfxFpeConfig,
                            },
                            InfoTypes = { infotype }
                        }
                    }
                }
            };
    
            // Construct the inspect config using custom infoTypes.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                CustomInfoTypes =
                {
                    new [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html)
                    {
                        InfoType = infotype,
                        SurrogateType = new CustomInfoType.Types.SurrogateType()
                    }
                }
            };
    
            // Construct the request.
            var request = new [ReidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                InspectConfig = inspectConfig,
                ReidentifyConfig = reidentifyConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text },
            };
    
            // Call the API.
            [ReidentifyContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentResponse.html) response = dlp.ReidentifyContent(request);
    
            // Inspect the response.
            Console.WriteLine($"Reidentified content: {response.[Item](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentResponse.html#Google_Cloud_Dlp_V2_ReidentifyContentResponse_Item).[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)}");
    
            return response;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // ReidTextDataWithFPE re-identifies text data with FPE
    func reidTextDataWithFPE(w io.Writer, projectID, textToReidentify, kmsKeyName, wrappedAESKey, surrogateInfoType string) error {
    	// projectId := "my-project-id"
    	// textToReidentify := "My SSN is AGE(9):FHKByqA13"
    	/* kmsKeyName :=  "projects/YOUR_PROJECT/"
    	   + "locations/YOUR_KEYRING_REGION/"
    	   + "keyRings/YOUR_KEYRING_NAME/"
    	   + "cryptoKeys/YOUR_KEY_NAME"
    	*/
    	// wrappedAesKey := "YOUR_ENCRYPTED_AES_256_KEY"
    	// surrogateInfoType := "AGE"
    
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
    
    	// Specify what content you want the service to re-identify.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{
    			Value: textToReidentify,
    		},
    	}
    
    	// Specify the type of info the inspection will re-identify. This must use the same custom
    	// into type that was used as a surrogate during the initial encryption.
    	infotype := &dlppb.InfoType{
    		Name: surrogateInfoType,
    	}
    
    	customInfotype := &dlppb.CustomInfoType{
    		InfoType: infotype,
    		Type: &dlppb.CustomInfoType_SurrogateType_{
    			SurrogateType: &dlppb.CustomInfoType_SurrogateType{},
    		},
    	}
    
    	inspectConfig := &dlppb.InspectConfig{
    		CustomInfoTypes: []*dlppb.CustomInfoType{
    			customInfotype,
    		},
    	}
    
    	// Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
    	kmsWrappedCryptoKey, err := base64.StdEncoding.DecodeString(wrappedAESKey)
    	if err != nil {
    		return err
    	}
    
    	cryptoKey := &dlppb.CryptoKey{
    		Source: &dlppb.CryptoKey_KmsWrapped{
    			KmsWrapped: &dlppb.KmsWrappedCryptoKey{
    				WrappedKey:    kmsWrappedCryptoKey,
    				CryptoKeyName: kmsKeyName,
    			},
    		},
    	}
    
    	// Specify how to un-encrypt the previously de-identified information.
    	cryptoReplaceFfxFpeConfig := &dlppb.CryptoReplaceFfxFpeConfig{
    		CryptoKey: cryptoKey,
    		Alphabet: &dlppb.CryptoReplaceFfxFpeConfig_CommonAlphabet{
    			CommonAlphabet: dlppb.[CryptoReplaceFfxFpeConfig_ALPHA_NUMERIC](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_CryptoReplaceFfxFpeConfig_FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED_CryptoReplaceFfxFpeConfig_NUMERIC_CryptoReplaceFfxFpeConfig_HEXADECIMAL_CryptoReplaceFfxFpeConfig_UPPER_CASE_ALPHA_NUMERIC_CryptoReplaceFfxFpeConfig_ALPHA_NUMERIC),
    		},
    		SurrogateInfoType: infotype,
    	}
    
    	primitiveTransformation := &dlppb.PrimitiveTransformation_CryptoReplaceFfxFpeConfig{
    		CryptoReplaceFfxFpeConfig: cryptoReplaceFfxFpeConfig,
    	}
    
    	InfoTypeTransformations := &dlppb.InfoTypeTransformations{
    		Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    			{
    				PrimitiveTransformation: &dlppb.PrimitiveTransformation{
    					Transformation: primitiveTransformation,
    				},
    				InfoTypes: []*dlppb.InfoType{
    					infotype,
    				},
    			},
    		},
    	}
    
    	// Combine configurations into a request for the service.
    	reidentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    			InfoTypeTransformations: InfoTypeTransformations,
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.ReidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		ReidentifyConfig: reidentifyConfig,
    		Item:             contentItem,
    		InspectConfig:    inspectConfig,
    	}
    
    	// Send the request.
    	r, err := client.ReidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result.
    	fmt.Fprintf(w, "output: %v", r.GetItem().GetValue())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.common.io.BaseEncoding;
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html);
    import com.google.privacy.dlp.v2.[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html);
    import com.google.privacy.dlp.v2.[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).[FfxCommonNativeAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[SurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.SurrogateType.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class ReIdentifyTextWithFpe {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToReIdentify = "My phone number is PHONE_TOKEN(10):9617256398";
        String kmsKeyName =
            "projects/YOUR_PROJECT/"
                + "locations/YOUR_KEYRING_REGION/"
                + "keyRings/YOUR_KEYRING_NAME/"
                + "cryptoKeys/YOUR_KEY_NAME";
        String wrappedAesKey = "YOUR_ENCRYPTED_AES_256_KEY";
        reIdentifyTextWithFpe(projectId, textToReIdentify, kmsKeyName, wrappedAesKey);
      }
    
      public static void reIdentifyTextWithFpe(
          String projectId, String textToReIdentify, String kmsKeyName, String wrappedAesKey)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to re-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToReIdentify).build();
    
          // Specify the type of info the inspection will re-identify. This must use the same custom
          // into type that was used as a surrogate during the initial encryption.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) surrogateInfoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PHONE_NUMBER").build();
    
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder()
                  .setInfoType(surrogateInfoType)
                  .[setSurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Builder_setSurrogateType_com_google_privacy_dlp_v2_CustomInfoType_SurrogateType_)([SurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.SurrogateType.html).getDefaultInstance())
                  .build();
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType).build();
    
          // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
          [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html) kmsWrappedCryptoKey =
              [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html).newBuilder()
                  .[setWrappedKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setWrappedKey_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(BaseEncoding.base64().decode(wrappedAesKey)))
                  .[setCryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setCryptoKeyName_java_lang_String_)(kmsKeyName)
                  .build();
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder().[setKmsWrapped](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setKmsWrapped_com_google_privacy_dlp_v2_KmsWrappedCryptoKey_)(kmsWrappedCryptoKey).build();
    
          // Specify how to un-encrypt the previously de-identified information.
          [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html) cryptoReplaceFfxFpeConfig =
              [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).newBuilder()
                  .setCryptoKey(cryptoKey)
                  // Set of characters in the input text. For more info, see
                  // https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.FfxCommonNativeAlphabet
                  .[setCommonAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.Builder.html#com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_Builder_setCommonAlphabet_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_FfxCommonNativeAlphabet_)([FfxCommonNativeAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet.html).NUMERIC)
                  .setSurrogateInfoType(surrogateInfoType)
                  .build();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoReplaceFfxFpeConfig_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_)(cryptoReplaceFfxFpeConfig)
                  .build();
          [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
              [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html).newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .addInfoTypes(surrogateInfoType)
                  .build();
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) transformations =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation).build();
    
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) reidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder().setInfoTypeTransformations(transformations).build();
    
          // Combine configurations into a request for the service.
          [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html) request =
              [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(contentItem)
                  .setInspectConfig(inspectConfig)
                  .[setReidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.Builder.html#com_google_privacy_dlp_v2_ReidentifyContentRequest_Builder_setReidentifyConfig_com_google_privacy_dlp_v2_DeidentifyConfig_)(reidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service
          [ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html) response = dlp.reidentifyContent(request);
    
          // Print the results
          System.out.println("Text after re-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html#com_google_privacy_dlp_v2_ReidentifyContentResponse_getItem__)().getValue());
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
    // const projectId = 'my-project';
    
    // The string to reidentify
    // const string = 'My phone number is PHONE_TOKEN(10):9617256398';
    
    // The set of characters to replace sensitive ones with
    // For more information, see https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#ffxcommonnativealphabet
    // const alphabet = 'NUMERIC';
    
    // The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key
    // const keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME';
    
    // The encrypted ('wrapped') AES-256 key to use
    // This key should be encrypted using the Cloud KMS key specified above
    // const wrappedKey = 'YOUR_ENCRYPTED_AES_256_KEY'
    
    // The name of the surrogate custom info type to use when reidentifying data
    // const surrogateType = 'SOME_INFO_TYPE_DEID';
    
    async function reidentifyTextWithFpe() {
      // Construct deidentification request
      const item = {value: string};
    
      // Construt Crypto Key Configuration
      const cryptoKeyConfig = {
        kmsWrapped: {
          wrappedKey: wrappedKey,
          cryptoKeyName: keyName,
        },
      };
    
      // Construct primitive transformation configuration
      const primitiveTransformation = {
        cryptoReplaceFfxFpeConfig: {
          cryptoKey: cryptoKeyConfig,
          commonAlphabet: alphabet,
          surrogateInfoType: {
            name: surrogateType,
          },
        },
      };
    
      // Combine configurations and construct re-identify request
      const request = {
        parent: `projects/${projectId}/locations/global`,
        reidentifyConfig: {
          infoTypeTransformations: {
            transformations: [
              {
                primitiveTransformation: primitiveTransformation,
              },
            ],
          },
        },
        inspectConfig: {
          customInfoTypes: [
            {
              infoType: {
                name: surrogateType,
              },
              surrogateType: {},
            },
          ],
        },
        item: item,
      };
    
      // Run re-identification request
      const [response] = await dlp.reidentifyContent(request);
      const reidentifiedItem = response.item;
    
      // Print results
      console.log(reidentifiedItem.value);
    }
    await reidentifyTextWithFpe();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoKey;
    use Google\Cloud\Dlp\V2\CryptoReplaceFfxFpeConfig;
    use Google\Cloud\Dlp\V2\CryptoReplaceFfxFpeConfig\FfxCommonNativeAlphabet;
    use Google\Cloud\Dlp\V2\CustomInfoType;
    use Google\Cloud\Dlp\V2\CustomInfoType\SurrogateType;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\KmsWrappedCryptoKey;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\ReidentifyContentRequest;
    
    /**
     * Reidentify a deidentified string using Format-Preserving Encryption (FPE).
     *
     * @param string $callingProjectId  The GCP Project ID to run the API call under.
     * @param string $string            The string to reidentify.
     * @param string $keyName           The name of the Cloud KMS key used to encrypt (wrap) the AES-256 key.
     * @param string $wrappedKey        The name of the Cloud KMS key use, encrypted with the KMS key in $keyName.
     * @param string $surrogateTypeName Surrogate custom info type to enable reidentification.
     */
    function reidentify_text_fpe(
        string $callingProjectId,
        string $string,
        string $keyName,
        string $wrappedKey,
        string $surrogateTypeName
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Specify what content you want the service to re-identify.
        $item = (new ContentItem())
            ->setValue($string);
    
        // Specify the type of info the inspection will re-identify. This must use the same custom
        // into type that was used as a surrogate during the initial encryption.
        $surrogateType = (new InfoType())
            ->setName($surrogateTypeName);
    
        $customInfoType = (new CustomInfoType())
            ->setInfoType($surrogateType)
            ->setSurrogateType(new SurrogateType());
    
        // Create the inspect configuration object.
        $inspectConfig = (new InspectConfig())
            ->setCustomInfoTypes([$customInfoType]);
    
        // Set of characters in the input text. For more info, see
        // https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.FfxCommonNativeAlphabet
        $commonAlphabet = FfxCommonNativeAlphabet::NUMERIC;
    
        // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
        $kmsWrappedCryptoKey = (new KmsWrappedCryptoKey())
            ->setWrappedKey(base64_decode($wrappedKey))
            ->setCryptoKeyName($keyName);
    
        // Create the crypto key configuration object.
        $cryptoKey = (new CryptoKey())
            ->setKmsWrapped($kmsWrappedCryptoKey);
    
        // Specify how to un-encrypt the previously de-identified information.
        $cryptoReplaceFfxFpeConfig = (new CryptoReplaceFfxFpeConfig())
            ->setCryptoKey($cryptoKey)
            ->setCommonAlphabet($commonAlphabet)
            ->setSurrogateInfoType($surrogateType);
    
        // Create the information transform configuration objects.
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCryptoReplaceFfxFpeConfig($cryptoReplaceFfxFpeConfig);
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Create the reidentification configuration object.
        $reidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations($infoTypeTransformations);
    
        // Run request.
        $reidentifyContentRequest = (new ReidentifyContentRequest())
            ->setParent($parent)
            ->setReidentifyConfig($reidentifyConfig)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->reidentifyContent($reidentifyContentRequest);
    
        // Print the results.
        printf($response->getItem()->getValue());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    
    import google.cloud.dlp
    
    
    def reidentify_text_with_fpe(
        project: str,
        input_str: str,
        key_name: str = None,
        wrapped_key: str = None,
    ) -> None:
        """
        Uses the Data Loss Prevention API to re-identify sensitive data in a
        string using Format Preserving Encryption (FPE).
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to re-identify (will be treated as text).
            key_name: The name of the Cloud KMS key used to encrypt ('wrap') the
                AES-256 key. Example:
                key_name = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/
                keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
            wrapped_key: The encrypted ('wrapped') AES-256 key to use. This key
                should be encrypted using the Cloud KMS key specified by key_name.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # The wrapped key is base64-encoded, but the library expects a binary
        # string, so decode it here.
        wrapped_key = base64.b64decode(wrapped_key)
    
        # Specify the type of info the inspection will re-identify.
        # This must use the same custom infoType that was used as a
        # surrogate during the initial encryption.
        surrogate_info_type = {"name": "PHONE_NUMBER"}
    
        # Construct FPE configuration dictionary
        crypto_replace_ffx_fpe_config = {
            "crypto_key": {
                "kms_wrapped": {"wrapped_key": wrapped_key, "crypto_key_name": key_name}
            },
            "common_alphabet": "NUMERIC",
            "surrogate_info_type": surrogate_info_type,
        }
    
        # Construct re-identify configuration dictionary
        reidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {
                        "primitive_transformation": {
                            "crypto_replace_ffx_fpe_config": crypto_replace_ffx_fpe_config,
                        },
                        "info_types": [surrogate_info_type],
                    }
                ]
            }
        }
    
        # Construct inspect configuration dictionary
        inspect_config = {
            "custom_info_types": [{"info_type": surrogate_info_type, "surrogate_type": {}}]
        }
    
        # Construct the `item`.
        item = {"value": input_str}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API.
        response = dlp.[reidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_reidentify_content)(
            request={
                "parent": parent,
                "reidentify_config": reidentify_config,
                "inspect_config": inspect_config,
                "item": item,
            }
        )
    
        # Print results
        print(f"Text after re-identification: {response.item.value}")
    
    

##### Format-preserving encryption examples: re-identification with surrogate type

Following is sample code in several languages that demonstrates how to use Sensitive Data Protection to re-identify sensitive data that was de-identified through through the [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptoreplaceffxfpeconfig) transformation method. For more information, see Format-preserving encryption on this page.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using static Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types;
    
    public class ReidentifyFreeTextWithFpeUsingSurrogate
    {
        public static ReidentifyContentResponse ReidentifyFreeText(
            string projectId,
            string text,
            string unwrappedKey,
            [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html) alphabet = [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html).Numeric,
            [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) surrogateType = null)
        {
            // Instantiate dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the infoType which will be used as surrogate type and infoType both.
            var infoType = surrogateType ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_TOKEN" };
    
            // Construct crypto replace config using crypto key name and wrapped key.
            var cryptoReplaceFfxFpeConfig = new [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.html)
            {
                CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                {
                    Unwrapped = new [UnwrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.UnwrappedCryptoKey.html)
                    {
                        Key = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromBase64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromBase64_System_String_)(unwrappedKey)
                    }
                },
                CommonAlphabet = alphabet,
                SurrogateInfoType = infoType
            };
    
            // Construct the re-identify config using crypto replace config.
            var reidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations =
                    {
                        new InfoTypeTransformations.Types.InfoTypeTransformation
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                CryptoReplaceFfxFpeConfig = cryptoReplaceFfxFpeConfig
                            }
                        }
                    }
                }
            };
    
            // Construct the inspect config with the help of custom info type.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                CustomInfoTypes =
                {
                    new [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html)
                    {
                        InfoType = infoType,
                        SurrogateType = new CustomInfoType.Types.SurrogateType()
                    }
                }
            };
    
            // Construct the request.
            var request = new [ReidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                ReidentifyConfig = reidentifyConfig,
                InspectConfig = inspectConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text }
            };
    
            // Call the API.
            [ReidentifyContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentResponse.html) response = dlp.ReidentifyContent(request);
    
            // Inspect the response.
            Console.WriteLine($"Re-identified content: {response.[Item](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentResponse.html#Google_Cloud_Dlp_V2_ReidentifyContentResponse_Item).[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)}");
            return response;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // reidentifyFreeTextWithFPEUsingSurrogate re-identifies free text with FPE using surrogate
    func reidentifyFreeTextWithFPEUsingSurrogate(w io.Writer, projectID, inputStr, surrogateType, unWrappedKey string) error {
    	// projectId := "your-project-id"
    	// inputStr := "My phone number is PHONE_TOKEN(10):4068372189"
    	// surrogateType := "PHONE_TOKEN"
    	// unWrappedKey := "hXribiHR6kvVKmj5ptTZLRTj8+u0eBQzwcrEPwyGhe8="
    
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
    
    	// The wrapped key is base64-encoded, but the library expects a binary
    	// string, so decode it here.
    	keyBytes, err := base64.StdEncoding.DecodeString(unWrappedKey)
    	if err != nil {
    		return err
    	}
    
    	// using the unwrapped key and surrogate info type construct cryptoReplaceConfig
    	cryptoReplaceConfig := &dlppb.CryptoReplaceFfxFpeConfig{
    		CryptoKey: &dlppb.CryptoKey{
    			Source: &dlppb.CryptoKey_Unwrapped{
    				Unwrapped: &dlppb.UnwrappedCryptoKey{
    					Key: keyBytes,
    				},
    			},
    		},
    		Alphabet: &dlppb.CryptoReplaceFfxFpeConfig_CommonAlphabet{
    			CommonAlphabet: dlppb.[CryptoReplaceFfxFpeConfig_NUMERIC](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_CryptoReplaceFfxFpeConfig_FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED_CryptoReplaceFfxFpeConfig_NUMERIC_CryptoReplaceFfxFpeConfig_HEXADECIMAL_CryptoReplaceFfxFpeConfig_UPPER_CASE_ALPHA_NUMERIC_CryptoReplaceFfxFpeConfig_ALPHA_NUMERIC),
    		},
    		SurrogateInfoType: &dlppb.InfoType{
    			Name: surrogateType,
    		},
    	}
    
    	// construct infoType transformations
    	infoTypeTransformations := &dlppb.InfoTypeTransformations{
    		Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    			{
    				PrimitiveTransformation: &dlppb.PrimitiveTransformation{
    					Transformation: &dlppb.PrimitiveTransformation_CryptoReplaceFfxFpeConfig{
    						CryptoReplaceFfxFpeConfig: cryptoReplaceConfig,
    					},
    				},
    			},
    		},
    	}
    
    	// construct re-identify config
    	reIdentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    			InfoTypeTransformations: infoTypeTransformations,
    		},
    	}
    
    	// construct inspect config to pass in req
    	inspectConfig := &dlppb.InspectConfig{
    		CustomInfoTypes: []*dlppb.CustomInfoType{
    			{
    				InfoType: &dlppb.InfoType{
    					Name: surrogateType,
    				},
    				Type: &dlppb.CustomInfoType_SurrogateType_{
    					SurrogateType: &dlppb.CustomInfoType_SurrogateType{},
    				},
    			},
    		},
    	}
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.ReidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		ReidentifyConfig: reIdentifyConfig,
    		InspectConfig:    inspectConfig,
    		Item: &dlppb.ContentItem{
    			DataItem: &dlppb.ContentItem_Value{
    				Value: inputStr,
    			},
    		},
    	}
    
    	// Send the request.
    	r, err := client.ReidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result.
    	fmt.Fprintf(w, "output: %v", r.GetItem().GetValue())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.common.io.BaseEncoding;
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html);
    import com.google.privacy.dlp.v2.[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[UnwrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.UnwrappedCryptoKey.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.Base64;
    import javax.crypto.KeyGenerator;
    import javax.crypto.SecretKey;
    
    public class ReidentifyFreeTextWithFpeUsingSurrogate {
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
    
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The string to de-identify.
        String textToDeIdentify = "My phone number is 4359916731";
        // The base64-encoded AES-256 key to use.
        String base64EncodedKey = "your-base64-encoded-key";
    
        // Obtain the de-identified text.
        String textToReIdentify =
            DeidentifyFreeTextWithFpeUsingSurrogate.deIdentifyWithFpeSurrogate(
                projectId, textToDeIdentify, base64EncodedKey);
    
        reIdentifyWithFpeSurrogate(projectId, textToReIdentify, base64EncodedKey);
      }
    
      // Re-identifies sensitive data in a string that was encrypted by Format Preserving Encryption
      // (FPE) with surrogate type.
      public static void reIdentifyWithFpeSurrogate(
          String projectId, String textToReIdentify, String unwrappedKey) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to re-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToReIdentify).build();
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[SurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.SurrogateType.html) surrogateType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).SurrogateType.newBuilder().build();
    
          // Specify the surrogate type used at time of de-identification.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) surrogateInfoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PHONE_TOKEN").build();
    
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder()
                  .setInfoType(surrogateInfoType)
                  .[setSurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Builder_setSurrogateType_com_google_privacy_dlp_v2_CustomInfoType_SurrogateType_)(surrogateType)
                  .build();
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType).build();
    
          // Specify an unwrapped crypto key.
          [UnwrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.UnwrappedCryptoKey.html) unwrappedCryptoKey =
              [UnwrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.UnwrappedCryptoKey.html).newBuilder()
                  .setKey([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(BaseEncoding.base64().decode(unwrappedKey)))
                  .build();
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder().[setUnwrapped](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setUnwrapped_com_google_privacy_dlp_v2_UnwrappedCryptoKey_)(unwrappedCryptoKey).build();
    
          // Specify how to decrypt the previously de-identified information.
          [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html) cryptoReplaceFfxFpeConfig =
              [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).newBuilder()
                  .setCryptoKey(cryptoKey)
                  // Set of characters in the input text. For more info, see
                  // https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.FfxCommonNativeAlphabet
                  .[setCommonAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.Builder.html#com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_Builder_setCommonAlphabet_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_FfxCommonNativeAlphabet_)([CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).FfxCommonNativeAlphabet.NUMERIC)
                  .setSurrogateInfoType(surrogateInfoType)
                  .build();
    
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoReplaceFfxFpeConfig_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_)(cryptoReplaceFfxFpeConfig)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).InfoTypeTransformation.newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) transformations =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation).build();
    
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) reidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder().setInfoTypeTransformations(transformations).build();
    
          // Combine configurations into a request for the service.
          [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html) request =
              [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(contentItem)
                  .setInspectConfig(inspectConfig)
                  .[setReidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.Builder.html#com_google_privacy_dlp_v2_ReidentifyContentRequest_Builder_setReidentifyConfig_com_google_privacy_dlp_v2_DeidentifyConfig_)(reidentifyConfig)
                  .build();
          // Send the request and receive response from the service.
          [ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html) response = dlp.reidentifyContent(request);
    
          // Print the results.
          System.out.println("Text after re-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html#com_google_privacy_dlp_v2_ReidentifyContentResponse_getItem__)().getValue());
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
    // const projectId = 'my-project';
    
    // The string to Re-identify
    // const string = 'PHONE_TOKEN(10):########';
    
    // The set of characters to replace sensitive ones with
    // For more information, see https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#ffxcommonnativealphabet
    // const alphabet = 'NUMERIC';
    
    // InfoTypes
    // const infoTypes = [{name: 'PHONE_NUMBER'}];
    
    // Surrogate Type
    // const surrogateType = 'PHONE_TOKEN';
    
    // The base64-encoded AES-256 key to use
    // const unwrappedKey = 'YWJjZGVmZ2hpamtsbW5vcA==';
    
    async function reidentifyWithFpeSurrogate() {
      // Specify an unwrapped crypto key.
      unwrappedKey = Buffer.from(unwrappedKey, 'base64');
    
      // Specify how the info from the inspection should be encrypted.
      const cryptoReplaceFfxFpeConfig = {
        cryptoKey: {
          unwrapped: {
            key: unwrappedKey,
          },
        },
        commonAlphabet: alphabet,
        surrogateInfoType: {name: surrogateType},
      };
    
      // Construct the inspect configuration.
      const inspectConfig = {
        customInfoTypes: [
          {
            infoType: {
              name: surrogateType,
            },
            surrogateType: {},
          },
        ],
      };
    
      // Set the text to be re-identified.
      const item = {value: string};
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        reidentifyConfig: {
          infoTypeTransformations: {
            transformations: [
              {
                primitiveTransformation: {
                  cryptoReplaceFfxFpeConfig: cryptoReplaceFfxFpeConfig,
                },
              },
            ],
          },
        },
        item: item,
        inspectConfig: inspectConfig,
      };
      // Run re-identification request
      const [response] = await dlp.reidentifyContent(request);
      const reidentifiedItem = response.item;
      // Print results
      console.log(reidentifiedItem.value);
    }
    reidentifyWithFpeSurrogate();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Re-identify free text with FPE using a surrogate.
     * Uses the Cloud Data Loss Prevention API to re-identify sensitive data in a string that was
     * encrypted by format-preserving encryption (FPE) with a surrogate type. The encryption is
     * performed with an unwrapped key.
     *
     * @param string $callingProjectId  The GCP Project ID to run the API call under.
     * @param string $string            The string to reidentify.
     * @param string $unwrappedKey      The base64-encoded AES-256 key to use.
     * @param string $surrogateTypeName The name of the surrogate custom info type to used during
     * the encryption process.
     */
    function reidentify_free_text_with_fpe_using_surrogate(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $string,
        string $unwrappedKey = 'YWJjZGVmZ2hpamtsbW5vcA==',
        string $surrogateTypeName = 'PHONE_TOKEN'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Specify an unwrapped crypto key.
        $unwrapped = (new UnwrappedCryptoKey())
            ->setKey(base64_decode($unwrappedKey));
    
        $cryptoKey = (new CryptoKey())
            ->setUnwrapped($unwrapped);
    
        // Specify the surrogate type used at time of de-identification.
        $surrogateType = (new InfoType())
            ->setName($surrogateTypeName);
    
        // The set of characters to replace sensitive ones with.
        // For more information, see https://cloud.google.com/dlp/docs/reference/rest/V2/organizations.deidentifyTemplates#ffxcommonnativealphabet
        $commonAlphabet = FfxCommonNativeAlphabet::NUMERIC;
    
        // Specify how to decrypt the previously de-identified information.
        $cryptoReplaceFfxFpeConfig = (new CryptoReplaceFfxFpeConfig())
            ->setCryptoKey($cryptoKey)
            ->setCommonAlphabet($commonAlphabet)
            ->setSurrogateInfoType($surrogateType);
    
        // Create the information transform configuration objects.
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCryptoReplaceFfxFpeConfig($cryptoReplaceFfxFpeConfig);
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Create the reidentification configuration object.
        $reidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations($infoTypeTransformations);
    
        // Create the inspect configuration object.
        // Specify the type of info the inspection will look for.
        $infotype = (new InfoType())
            ->setName($surrogateTypeName);
    
        $customInfoType = (new CustomInfoType())
            ->setInfoType($infotype)
            ->setSurrogateType((new SurrogateType()));
    
        $inspectConfig = (new InspectConfig())
            ->setCustomInfoTypes([$customInfoType]);
    
        // Specify the content to be re-identify.
        $content = (new ContentItem())
            ->setValue($string);
    
        // Run request.
        $reidentifyContentRequest = (new ReidentifyContentRequest())
            ->setParent($parent)
            ->setReidentifyConfig($reidentifyConfig)
            ->setInspectConfig($inspectConfig)
            ->setItem($content);
        $response = $dlp->reidentifyContent($reidentifyContentRequest);
    
        // Print the results.
        printf($response->getItem()->getValue());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    
    import google.cloud.dlp
    
    
    def reidentify_free_text_with_fpe_using_surrogate(
        project: str,
        input_str: str,
        alphabet: str = "NUMERIC",
        surrogate_type: str = "PHONE_TOKEN",
        unwrapped_key: str = "YWJjZGVmZ2hpamtsbW5vcA==",
    ) -> None:
        """Uses the Data Loss Prevention API to reidentify sensitive data in a
        string that was encrypted by Format Preserving Encryption (FPE) with
        surrogate type. The encryption is performed with an unwrapped key.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to deidentify (will be treated as text).
            alphabet: The set of characters to replace sensitive ones with. For
                more information, see https://cloud.google.com/dlp/docs/reference/
                rest/v2beta2/organizations.deidentifyTemplates#ffxcommonnativealphabet
            surrogate_type: The name of the surrogate custom info type to used
                during the encryption process.
            unwrapped_key: The base64-encoded AES-256 key to use.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # The wrapped key is base64-encoded, but the library expects a binary
        # string, so decode it here.
        unwrapped_key = base64.b64decode(unwrapped_key)
    
        # Construct Deidentify Config
        transformation = {
            "primitive_transformation": {
                "crypto_replace_ffx_fpe_config": {
                    "crypto_key": {"unwrapped": {"key": unwrapped_key}},
                    "common_alphabet": alphabet,
                    "surrogate_info_type": {"name": surrogate_type},
                }
            }
        }
    
        reidentify_config = {
            "info_type_transformations": {"transformations": [transformation]}
        }
    
        inspect_config = {
            "custom_info_types": [
                {"info_type": {"name": surrogate_type}, "surrogate_type": {}}
            ]
        }
    
        # Convert string to item
        item = {"value": input_str}
    
        # Call the API
        response = dlp.[reidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_reidentify_content)(
            request={
                "parent": parent,
                "reidentify_config": reidentify_config,
                "inspect_config": inspect_config,
                "item": item,
            }
        )
    
        # Print results
        print(response.item.value)
    
    

##### Format-preserving encryption examples: re-identification of sensitive data in tables

Following is sample code in several languages that demonstrates how to use Sensitive Data Protection to re-identify sensitive data in tables that were de-identified through the [`CryptoReplaceFfxFpeConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptoreplaceffxfpeconfig) transformation method. For more information, see Format-preserving encryption on this page.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using static Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types;
    
    public class ReidentifyTableDataWithFpe
    {
        public static Table ReidentifyTableData(
            string projectId,
            string keyName,
            string wrappedKey,
            [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html) alphabet = [FfxCommonNativeAlphabet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.Types.FfxCommonNativeAlphabet.html).Numeric,
            [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html) tableToInspect = null)
        {
            // Instantiate a client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the table if null.
            var table = tableToInspect;
    
            if (table == null)
            {
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "28777" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Justin" }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "28778" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Gary" }
                };
    
                table = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                {
                    Headers =
                    {
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Employee ID" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Employee Name" }
                    },
                    Rows =
                    {
                        new Table.Types.Row { Values = { row1 } },
                        new Table.Types.Row { Values = { row2 } }
                    }
                };
            }
    
            // Construct the content item by providing the table.
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Table = table };
    
            // Specify how to decrypt the previously de-identified information.
            var cryptoReplaceFfxFpeConfig = new [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoReplaceFfxFpeConfig.html)
            {
                CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                {
                    KmsWrapped = new [KmsWrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KmsWrappedCryptoKey.html)
                    {
                        CryptoKeyName = keyName,
                        WrappedKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromBase64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromBase64_System_String_)(wrappedKey)
                    }
                },
                CommonAlphabet = alphabet
            };
    
            // Specify the field to be decrypted.
            var fields = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html)[] { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Employee ID" } };
    
            // Construct the re-identify config and specify the transformation.
            var reidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                RecordTransformations = new [RecordTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformations.html)
                {
                    FieldTransformations =
                    {
                        new [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.html)
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                CryptoReplaceFfxFpeConfig = cryptoReplaceFfxFpeConfig,
                            },
                            Fields = { fields }
                        }
                    }
                }
            };
    
            // Construct the request.
            var request = new [ReidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                Item = contentItem,
                ReidentifyConfig = reidentifyConfig
            };
    
            // Call the API.
            [ReidentifyContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentResponse.html) response = dlp.ReidentifyContent(request);
    
            // Inspect the response.
            Console.WriteLine($"Table after re-identification: {response.[Item](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentResponse.html#Google_Cloud_Dlp_V2_ReidentifyContentResponse_Item).[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)}");
    
            return response.[Item](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentResponse.html#Google_Cloud_Dlp_V2_ReidentifyContentResponse_Item).[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html);
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // reidTableDataWithFPE re-identifies table data with FPE
    func reidTableDataWithFPE(w io.Writer, projectID, kmsKeyName, wrappedAesKey string) error {
    	// projectId := "my-project-id"
    	/* kmsKeyName :=  "projects/YOUR_PROJECT/"
    	   + "locations/YOUR_KEYRING_REGION/"
    	   + "keyRings/YOUR_KEYRING_NAME/"
    	   + "cryptoKeys/YOUR_KEY_NAME"
    	*/
    	// wrappedAesKey := "YOUR_ENCRYPTED_AES_256_KEY"
    
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
    
    	// Specify the table data that needs to be re-identified.
    	tableToReIdentify := &dlppb.Table{
    		Headers: []*dlppb.FieldId{
    			{Name: "Employee ID"},
    		},
    		Rows: []*dlppb.Table_Row{
    			{
    				Values: []*dlppb.Value{
    					{
    						Type: &dlppb.Value_StringValue{
    							StringValue: "90511",
    						},
    					},
    				},
    			},
    		},
    	}
    
    	// Specify the content you want to re-identify.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Table{
    			Table: tableToReIdentify,
    		},
    	}
    
    	// Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
    	kmsWrappedCryptoKey, err := base64.StdEncoding.DecodeString(wrappedAesKey)
    	if err != nil {
    		return err
    	}
    
    	cryptoKey := &dlppb.CryptoKey{
    		Source: &dlppb.CryptoKey_KmsWrapped{
    			KmsWrapped: &dlppb.KmsWrappedCryptoKey{
    				WrappedKey:    kmsWrappedCryptoKey,
    				CryptoKeyName: kmsKeyName,
    			},
    		},
    	}
    
    	// Specify how to un-encrypt the previously de-identified information.
    	cryptoReplaceFfxFpeConfig := &dlppb.CryptoReplaceFfxFpeConfig{
    		CryptoKey: cryptoKey,
    		Alphabet: &dlppb.CryptoReplaceFfxFpeConfig_CommonAlphabet{
    			CommonAlphabet: dlppb.[CryptoReplaceFfxFpeConfig_NUMERIC](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_CryptoReplaceFfxFpeConfig_FFX_COMMON_NATIVE_ALPHABET_UNSPECIFIED_CryptoReplaceFfxFpeConfig_NUMERIC_CryptoReplaceFfxFpeConfig_HEXADECIMAL_CryptoReplaceFfxFpeConfig_UPPER_CASE_ALPHA_NUMERIC_CryptoReplaceFfxFpeConfig_ALPHA_NUMERIC),
    		},
    	}
    
    	primitiveTransformation := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_CryptoReplaceFfxFpeConfig{
    			CryptoReplaceFfxFpeConfig: cryptoReplaceFfxFpeConfig,
    		},
    	}
    
    	// Specify field to be decrypted.
    	fieldId := &dlppb.FieldId{
    		Name: "Employee ID",
    	}
    
    	// Associate the decryption with the specified field.
    	fieldTransformation := &dlppb.FieldTransformation{
    		Transformation: &dlppb.FieldTransformation_PrimitiveTransformation{
    			PrimitiveTransformation: primitiveTransformation,
    		},
    		Fields: []*dlppb.FieldId{
    			fieldId,
    		},
    	}
    
    	recordTransformations := &dlppb.RecordTransformations{
    		FieldTransformations: []*dlppb.FieldTransformation{
    			fieldTransformation,
    		},
    	}
    
    	deidentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: &dlppb.DeidentifyConfig_RecordTransformations{
    			RecordTransformations: recordTransformations,
    		},
    	}
    
    	// Combine configurations into a request for the service.
    	req := &dlppb.ReidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		ReidentifyConfig: deidentifyConfig,
    		Item:             contentItem,
    	}
    
    	// Send the request and receive response from the service.
    	resp, err := client.ReidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result.
    	fmt.Fprintf(w, "Table after re-identification : %v", resp.GetItem().GetTable())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.common.io.BaseEncoding;
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html);
    import com.google.privacy.dlp.v2.[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html);
    import com.google.privacy.dlp.v2.[CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).[FfxCommonNativeAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html);
    import com.google.privacy.dlp.v2.[KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class ReIdentifyTableWithFpe {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String kmsKeyName =
            "projects/YOUR_PROJECT/"
                + "locations/YOUR_KEYRING_REGION/"
                + "keyRings/YOUR_KEYRING_NAME/"
                + "cryptoKeys/YOUR_KEY_NAME";
        String wrappedAesKey = "YOUR_ENCRYPTED_AES_256_KEY";
        [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToReIdentify =
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder()
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Employee ID").build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html).newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().setStringValue("28777").build())
                        .build())
                .build();
        reIdentifyTableWithFpe(projectId, tableToReIdentify, kmsKeyName, wrappedAesKey);
      }
    
      public static void reIdentifyTableWithFpe(
          String projectId, [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToReIdentify, String kmsKeyName, String wrappedAesKey)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to re-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(tableToReIdentify).build();
    
          // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
          [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html) kmsWrappedCryptoKey =
              [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html).newBuilder()
                  .[setWrappedKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setWrappedKey_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(BaseEncoding.base64().decode(wrappedAesKey)))
                  .[setCryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setCryptoKeyName_java_lang_String_)(kmsKeyName)
                  .build();
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder().[setKmsWrapped](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setKmsWrapped_com_google_privacy_dlp_v2_KmsWrappedCryptoKey_)(kmsWrappedCryptoKey).build();
    
          // Specify how to un-encrypt the previously de-identified information.
          [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html) cryptoReplaceFfxFpeConfig =
              [CryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.html).newBuilder()
                  .setCryptoKey(cryptoKey)
                  // Set of characters in the input text. For more info, see
                  // https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.FfxCommonNativeAlphabet
                  .[setCommonAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.Builder.html#com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_Builder_setCommonAlphabet_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_FfxCommonNativeAlphabet_)([FfxCommonNativeAlphabet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoReplaceFfxFpeConfig.FfxCommonNativeAlphabet.html).NUMERIC)
                  .build();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoReplaceFfxFpeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoReplaceFfxFpeConfig_com_google_privacy_dlp_v2_CryptoReplaceFfxFpeConfig_)(cryptoReplaceFfxFpeConfig)
                  .build();
    
          // Specify field to be decrypted.
          [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html) fieldId = [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Employee ID").build();
    
          // Associate the decryption with the specified field.
          [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html) fieldTransformation =
              [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html).newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .addFields(fieldId)
                  .build();
          [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html) transformations =
              [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html).newBuilder().addFieldTransformations(fieldTransformation).build();
    
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) reidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder().[setRecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.Builder.html#com_google_privacy_dlp_v2_DeidentifyConfig_Builder_setRecordTransformations_com_google_privacy_dlp_v2_RecordTransformations_)(transformations).build();
    
          // Combine configurations into a request for the service.
          [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html) request =
              [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(contentItem)
                  .[setReidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.Builder.html#com_google_privacy_dlp_v2_ReidentifyContentRequest_Builder_setReidentifyConfig_com_google_privacy_dlp_v2_DeidentifyConfig_)(reidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service
          [ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html) response = dlp.reidentifyContent(request);
    
          // Print the results
          System.out.println("Table after re-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html#com_google_privacy_dlp_v2_ReidentifyContentResponse_getItem__)().getValue());
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
    // const projectId = 'my-project';
    
    // The set of characters to replace sensitive ones with
    // For more information, see https://cloud.google.com/dlp/docs/reference/rest/v2/organizations.deidentifyTemplates#ffxcommonnativealphabet
    // const alphabet = 'ALPHA_NUMERIC';
    
    // The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key
    // const keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME';
    
    // The encrypted ('wrapped') AES-256 key to use
    // This key should be encrypted using the Cloud KMS key specified above
    // const wrappedKey = 'YOUR_ENCRYPTED_AES_256_KEY'
    
    // The name of the surrogate custom info type to use when reidentifying data
    // const surrogateType = 'SOME_INFO_TYPE_DEID';
    
    // Table to re-identify
    const tablularData = {
      headers: [{name: 'Employee ID'}],
      rows: [{values: [{stringValue: '90511'}]}],
    };
    
    async function reidentifyTableWithFpe() {
      // Specify field to be re-identified.
      const fieldIds = [{name: 'Employee ID'}];
    
      // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it
      const cryptoKeyConfig = {
        kmsWrapped: {
          wrappedKey: wrappedKey,
          cryptoKeyName: keyName,
        },
      };
    
      // Associate transformation with crypto key congurations.
      const primitiveTransformation = {
        cryptoReplaceFfxFpeConfig: {
          cryptoKey: cryptoKeyConfig,
          commonAlphabet: alphabet,
        },
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        reidentifyConfig: {
          recordTransformations: {
            fieldTransformations: [
              {
                fields: fieldIds,
                primitiveTransformation: primitiveTransformation,
              },
            ],
          },
        },
        item: {
          table: tablularData,
        },
      };
    
      // Send the request and receive response from the service.
      const [response] = await dlp.reidentifyContent(request);
    
      // Print the results.
      console.log(
        `Table after re-identification: ${JSON.stringify(response.item.table)}`
      );
    }
    await reidentifyTableWithFpe();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoKey;
    use Google\Cloud\Dlp\V2\CryptoReplaceFfxFpeConfig;
    use Google\Cloud\Dlp\V2\CryptoReplaceFfxFpeConfig\FfxCommonNativeAlphabet;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\FieldTransformation;
    use Google\Cloud\Dlp\V2\KmsWrappedCryptoKey;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\RecordTransformations;
    use Google\Cloud\Dlp\V2\ReidentifyContentRequest;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * Re-identify table data with FPE.
     *
     * @param string $callingProjectId      The Google Cloud project id to use as a parent resource.
     * @param string $inputCsvFile          The input file(csv) path  to reidentify.
     * @param string $outputCsvFile         The oupt file path to save reidentify content.
     * @param string $encryptedFieldNames   The field to be encrypted.
     * @param string $kmsKeyName            The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key.
     * Example: key_name = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
     * @param string $wrappedAesKey         The encrypted ('wrapped') AES-256 key to use.
     *
     * */
    
    function reidentify_table_fpe(
        string $callingProjectId,
        string $inputCsvFile,
        string $outputCsvFile,
        string $encryptedFieldNames,
        string $kmsKeyName,
        string $wrappedAesKey
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Read a CSV file.
        $csvLines = file($inputCsvFile, FILE_IGNORE_NEW_LINES);
        $csvHeaders = explode(',', $csvLines[0]);
        $csvRows = array_slice($csvLines, 1);
    
        // Convert CSV file into protobuf objects.
        $tableHeaders = array_map(function ($csvHeader) {
            return (new FieldId)
                ->setName($csvHeader);
        }, $csvHeaders);
    
        $tableRows = array_map(function ($csvRow) {
            $rowValues = array_map(function ($csvValue) {
                return (new Value())
                    ->setStringValue($csvValue);
            }, explode(',', $csvRow));
            return (new Row())
                ->setValues($rowValues);
        }, $csvRows);
    
        // Construct the table object.
        $tableToDeIdentify = (new Table())
            ->setHeaders($tableHeaders)
            ->setRows($tableRows);
    
        // Specify the content to be reidentify.
        $content = (new ContentItem())
            ->setTable($tableToDeIdentify);
    
        // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
        $kmsWrappedCryptoKey = (new KmsWrappedCryptoKey())
            ->setWrappedKey(base64_decode($wrappedAesKey))
            ->setCryptoKeyName($kmsKeyName);
    
        $cryptoKey = (new CryptoKey())
            ->setKmsWrapped($kmsWrappedCryptoKey);
    
        // Specify how to un-encrypt the previously de-identified information.
        $cryptoReplaceFfxFpeConfig = (new CryptoReplaceFfxFpeConfig())
            ->setCryptoKey($cryptoKey)
            ->setCommonAlphabet(FfxCommonNativeAlphabet::NUMERIC);
    
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCryptoReplaceFfxFpeConfig($cryptoReplaceFfxFpeConfig);
    
        // Specify field to be decrypted.
        $encryptedFields = array_map(function ($encryptedFieldName) {
            return (new FieldId())
                ->setName($encryptedFieldName);
        }, explode(',', $encryptedFieldNames));
    
        // Associate the decryption with the specified field.
        $fieldTransformation = (new FieldTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setFields($encryptedFields);
    
        $recordtransformations = (new RecordTransformations())
            ->setFieldTransformations([$fieldTransformation]);
    
        $reidentifyConfig = (new DeidentifyConfig())
            ->setRecordTransformations($recordtransformations);
    
        // Run request.
        $reidentifyContentRequest = (new ReidentifyContentRequest())
            ->setParent($parent)
            ->setReidentifyConfig($reidentifyConfig)
            ->setItem($content);
        $response = $dlp->reidentifyContent($reidentifyContentRequest);
    
        // Print the results.
        $csvRef = fopen($outputCsvFile, 'w');
        fputcsv($csvRef, $csvHeaders);
        foreach ($response->getItem()->getTable()->getRows() as $tableRow) {
            $values = array_map(function ($tableValue) {
                return $tableValue->getStringValue();
            }, iterator_to_array($tableRow->getValues()));
            fputcsv($csvRef, $values);
        };
        printf('Table after re-identification (File Location): %s', $outputCsvFile);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    
    from typing import List
    
    import google.cloud.dlp
    
    
    def reidentify_table_with_fpe(
        project: str,
        table_header: List[str],
        table_rows: List[List[str]],
        reid_field_names: List[str],
        key_name: str = None,
        wrapped_key: bytes = None,
        alphabet: str = None,
    ) -> None:
        """Uses the Data Loss Prevention API to re-identify sensitive data in a
        table that was encrypted by Format Preserving Encryption (FPE).
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            table_header: List of strings representing table field names.
            table_rows: List of rows representing table data.
            reid_field_names: A list of fields in table to re-identify.
            key_name: The name of the Cloud KMS key used to encrypt ('wrap') the
                AES-256 key. Example:
                key_name = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/
                keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
            wrapped_key: The decrypted ('wrapped', in bytes) AES-256 key to use. This key
                should be encrypted using the Cloud KMS key specified by key_name.
            alphabet: The set of characters to replace sensitive ones with. For
                more information, see https://cloud.google.com/dlp/docs/reference/
                rest/v2/projects.deidentifyTemplates#ffxcommonnativealphabet
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the `table`. For more details on the table schema, please see
        # https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem#Table
        headers = [{"name": val} for val in table_header]
        rows = []
        for row in table_rows:
            rows.append({"values": [{"string_value": cell_val} for cell_val in row]})
        table = {"headers": headers, "rows": rows}
    
        # Convert table to `item`
        item = {"table": table}
    
        # Specify fields to be re-identified/decrypted.
        reid_field_names = [{"name": _i} for _i in reid_field_names]
    
        # Construct FPE configuration dictionary
        crypto_replace_ffx_fpe_config = {
            "crypto_key": {
                "kms_wrapped": {"wrapped_key": wrapped_key, "crypto_key_name": key_name}
            },
            "common_alphabet": alphabet,
        }
    
        # Construct reidentify configuration dictionary
        reidentify_config = {
            "record_transformations": {
                "field_transformations": [
                    {
                        "primitive_transformation": {
                            "crypto_replace_ffx_fpe_config": crypto_replace_ffx_fpe_config,
                        },
                        "fields": reid_field_names,
                    }
                ]
            }
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API.
        response = dlp.[reidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_reidentify_content)(
            request={
                "parent": parent,
                "reidentify_config": reidentify_config,
                "item": item,
            }
        )
    
        # Print out results.
        print(f"Table after re-identification: {response.item.table}")
    
    

#### Deterministic encryption

The deterministic encryption transformation method [`CryptoDeterministicConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptodeterministicconfig) in the DLP API takes an input value (a piece of sensitive data that Sensitive Data Protection has detected), encrypts it using [AES-SIV](https://tools.ietf.org/html/rfc5297) with a [`CryptoKey`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptokey), and then replaces the original value with a base64-encoded representation of the encrypted value.

Using the deterministic encryption transformation enables more efficient searching of encrypted data.

The input value:

  * Must be at least 1 character long.
  * Has no character set limitations.



The generated token:

  * Is a base64-encoded representation of the encrypted value.
  * Does not preserve the character set ("alphabet") or length of the input value post-encryption.
  * Is computed using AES encryption in SIV mode (AES-SIV) with a [`CryptoKey`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptokey).
  * Isn't necessarily unique, as each instance of the same input value de-identifies to the same token. This enables more efficient searching of encrypted data. You can change this behavior by using context "tweaks," as described in [Contexts](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization#contexts).
  * Is generated with a prefix added, in the form `[SURROGATE_TYPE]([LENGTH]):`, where `[SURROGATE_TYPE]` represents a [surrogate infoType](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#surrogatetype) describing the input value, and `[LENGTH]` indicates its character length. The surrogate enables the token to be re-identified using the original encryption key used for de-identification.

**Note:** For more information about surrogate types, see [Surrogate annotations](https://docs.cloud.google.com/sensitive-data-protection/docs/pseudonymization#surrogate_annotations).

Following is an example JSON configuration for de-identification using deterministic encryption. Note that we've chosen to use "PHONE_SURROGATE" as our descriptive surrogate type since we're de-identifying telephone numbers. `[CRYPTO_KEY]` represents an unwrapped cryptographic key obtained from Cloud KMS.
    
    
    {
      "deidentifyConfig":{
        "infoTypeTransformations":{
          "transformations":[
            {
              "infoTypes":[
                {
                  "name":"PHONE_NUMBER"
                }
              ],
              "primitiveTransformation":{
                "cryptoDeterministicConfig":{
                  "cryptoKey":{
                    "unwrapped":{
                      "key":"[CRYPTO_KEY]"
                    }
                  },
                  "surrogateInfoType":{
                    "name":"PHONE_SURROGATE"
                  }
                }
              }
            }
          ]
        }
      },
      "inspectConfig":{
        "infoTypes":[
          {
            "name":"PHONE_NUMBER"
          }
        ]
      },
      "item":{
        "value":"My phone number is 206-555-0574, call me"
      }
    }
    

De-identifying the string "My phone number is 206-555-0574" using this transformation results in a de-identified string such as the following:
    
    
    My phone number is PHONE_SURROGATE(36):ATZBu5OCCSwo+e94xSYnKYljk1OQpkW7qhzx, call me

To re-identify this string, you can use a JSON request like the following, where [CRYPTO_KEY] is the same cryptographic key used to de-identify the content.
    
    
    {
      "reidentifyConfig":{
        "infoTypeTransformations":{
          "transformations":[
            {
              "infoTypes":[
                {
                  "name":"PHONE_SURROGATE"
                }
              ],
              "primitiveTransformation":{
                "cryptoDeterministicConfig":{
                  "cryptoKey":{
                    "unwrapped":{
                      "key":"[CRYPTO_KEY]"
                    }
                  },
                  "surrogateInfoType":{
                    "name":"PHONE_SURROGATE"
                  }
                }
              }
            }
          ]
        }
      },
      "inspectConfig":{
        "customInfoTypes":[
          {
            "infoType":{
              "name":"PHONE_SURROGATE"
            },
            "surrogateType":{
    
            }
          }
        ]
      },
      "item":{
        "value":"My phone number is [PHONE_SURROGATE](36):ATZBu5OCCSwo+e94xSYnKYljk1OQpkW7qhzx, call me"
      }
    }
    

Re-identifying this string results in the original string:
    
    
    My phone number is 206-555-0574, call me

If you want to use a wrapped (encrypted) `CryptoKey` instead for better security, see [Quickstart: De-identifying and re-identifying sensitive text](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-de-identify) for an example. When you're ready to use a client library to de-identify content, remember to decode the wrapped key (which is a base64-encoded string by default), as demonstrated in Format-preserving encryption on this page.

##### Deterministic encryption examples: de-identification

This example uses the [`CryptoDeterministicConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptodeterministicconfig) transformation method to de-identify sensitive data. For more information, see Deterministic encryption on this page.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyWithDeterministic
    {
        public static DeidentifyContentResponse Deidentify(
            string projectId,
            string text,
            string keyName,
            string wrapperKey,
            [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) surrogateType = null,
            IEnumerable<InfoType> infoTypes = null)
        {
            // Instantiate a client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the inspect config by specifying the type of info to be inspected.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes =
                {
                    infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[] { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_NUMBER" } }
                }
            };
    
            // Construct the crypto deterministic config by providing key name, wrapped key and surrogate type.
            var cryptoDeterministicConfig = new [CryptoDeterministicConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoDeterministicConfig.html)
            {
                CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                {
                    KmsWrapped = new [KmsWrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KmsWrappedCryptoKey.html)
                    {
                        CryptoKeyName = keyName,
                        WrappedKey = Google.Protobuf.ByteString.FromBase64(wrapperKey)
                    }
                },
                SurrogateInfoType = surrogateType ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_TOKEN" }
            };
    
    
            // Construct the deidentify config using crypto deterministic config.
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations =
                    {
                        new InfoTypeTransformations.Types.InfoTypeTransformation
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                CryptoDeterministicConfig = cryptoDeterministicConfig
                            }
                        }
                    }
                }
            };
    
            // Construct the request.
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                DeidentifyConfig = deidentifyConfig,
                InspectConfig = inspectConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text }
            };
    
            // Call the API.
            [DeidentifyContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentResponse.html) response = dlp.DeidentifyContent(request);
    
            // Check the de-identified content.
            Console.WriteLine($"De-identified content: {response.[Item](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentResponse.html#Google_Cloud_Dlp_V2_DeidentifyContentResponse_Item).[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)}");
            return response;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // deIdentifyDeterministicEncryption de-identifies through deterministic encryption
    func deIdentifyDeterministicEncryption(w io.Writer, projectID, inputStr string, infoTypeNames []string, keyFileName, cryptoKeyName, surrogateInfoType string) error {
    	// projectId := "your-project-id"
    	// inputStr := "My SSN is 111111111"
    	// infoTypeNames := []string{"US_SOCIAL_SECURITY_NUMBER"}
    	/* keyFileName :=  "projects/YOUR_PROJECT/"
    	   + "locations/YOUR_KEYRING_REGION/"
    	   + "keyRings/YOUR_KEYRING_NAME/"
    	   + "cryptoKeys/YOUR_KEY_NAME"
    	*/
    	// cryptoKeyName := "YOUR_ENCRYPTED_AES_256_KEY"
    	// surrogateInfoType := "SSN_TOKEN"
    
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
    
    	// Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
    	wrappedKey, err := base64.StdEncoding.DecodeString(cryptoKeyName)
    	if err != nil {
    		return err
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
    	var infoTypes []*dlppb.InfoType
    	for _, it := range infoTypeNames {
    		infoTypes = append(infoTypes, &dlppb.InfoType{Name: it})
    	}
    
    	// Specify the key used by the encryption function for deterministic encryption.
    	cryptoReplaceDeterministicConfig := &dlppb.CryptoDeterministicConfig{
    		CryptoKey: &dlppb.CryptoKey{
    			Source: &dlppb.CryptoKey_KmsWrapped{
    				KmsWrapped: &dlppb.KmsWrappedCryptoKey{
    					WrappedKey:    wrappedKey,
    					CryptoKeyName: keyFileName,
    				},
    			},
    		},
    		SurrogateInfoType: &dlppb.InfoType{
    			Name: surrogateInfoType,
    		},
    	}
    
    	// Specifying the info-types to look for.
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes: infoTypes,
    	}
    
    	// Specify what content you want the service to de-identify.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{
    			Value: inputStr,
    		},
    	}
    
    	// Specifying the deterministic crypto.
    	primitiveTransformation := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_CryptoDeterministicConfig{
    			CryptoDeterministicConfig: cryptoReplaceDeterministicConfig,
    		},
    	}
    
    	// Construct a de-identification config for de-identify deterministic request.
    	deIdentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    			InfoTypeTransformations: &dlppb.InfoTypeTransformations{
    				Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    					{
    						PrimitiveTransformation: primitiveTransformation,
    					},
    				},
    			},
    		},
    	}
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: deIdentifyConfig,
    		InspectConfig:    inspectConfig,
    		Item:             contentItem,
    	}
    
    	// Send the request.
    	resp, err := client.DeidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the results.
    	fmt.Fprintf(w, "output : %v", resp.GetItem().GetValue())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CryptoDeterministicConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoDeterministicConfig.html);
    import com.google.privacy.dlp.v2.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    import java.util.Collections;
    import org.apache.commons.codec.binary.Base64;
    
    public class DeIdenitfyWithDeterministicEncryption {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
    
        //The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The string to de-identify.
        String textToDeIdentify = "My SSN is 372819127";
        // The encrypted ('wrapped') AES-256 key to use.
        // This key should be encrypted using the Cloud KMS key specified by key_name.
        String wrappedKey = "YOUR_ENCRYPTED_AES_256_KEY";
        // The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key.
        String kmsKeyName =
            "projects/YOUR_PROJECT/"
                + "locations/YOUR_KEYRING_REGION/"
                + "keyRings/YOUR_KEYRING_NAME/"
                + "cryptoKeys/YOUR_KEY_NAME";
        deIdentifyWithDeterministicEncryption(projectId, textToDeIdentify, wrappedKey, kmsKeyName);
      }
    
      // De-identifies sensitive data in a string using deterministic encryption. The encryption is
      // performed with a wrapped key.
      public static String deIdentifyWithDeterministicEncryption(
          String projectId, String textToDeIdentify, String wrappedKey, String key) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to de-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder()
                  .setValue(textToDeIdentify)
                  .build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder()
                  .setName("US_SOCIAL_SECURITY_NUMBER")
                  .build();
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                      .addAllInfoTypes(Collections.singletonList(infoType))
                      .build();
    
          // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
          [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html) unwrappedCryptoKey = [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html).newBuilder()
                  .[setWrappedKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setWrappedKey_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(
                          Base64.decodeBase64(wrappedKey.getBytes(StandardCharsets.UTF_8))))
                  .[setCryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setCryptoKeyName_java_lang_String_)(key)
                  .build();
    
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder()
                  .[setKmsWrapped](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setKmsWrapped_com_google_privacy_dlp_v2_KmsWrappedCryptoKey_)(unwrappedCryptoKey)
                  .build();
    
          // Specify how the info from the inspection should be encrypted.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) surrogateInfoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder()
                  .setName("SSN_TOKEN")
                  .build();
    
          [CryptoDeterministicConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoDeterministicConfig.html) cryptoDeterministicConfig = [CryptoDeterministicConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoDeterministicConfig.html).newBuilder()
                  .setSurrogateInfoType(surrogateInfoType)
                  .setCryptoKey(cryptoKey)
                  .build();
    
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation = [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoDeterministicConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoDeterministicConfig_com_google_privacy_dlp_v2_CryptoDeterministicConfig_)(cryptoDeterministicConfig)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
                  [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).InfoTypeTransformation.newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) transformations = [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder()
                  .[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation)
                  .build();
    
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig = [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder()
                  .setInfoTypeTransformations(transformations)
                  .build();
    
          // Combine configurations into a request for the service.
          [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html) request = [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(contentItem)
                  .setInspectConfig(inspectConfig)
                  .setDeidentifyConfig(deidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service.
          [DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html) response = dlp.deidentifyContent(request);
    
          // Print the results.
          System.out.println(
              "Text after de-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getValue());
    
          return response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getValue();
    
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
    // const projectId = 'my-project';
    
    // The string to deidentify
    // const string = 'My name is Alicia Abernathy, and my email address is aabernathy@example.com.';
    
    // The infoTypes of information to match
    // const infoTypes = [{ name: 'EMAIL_ADDRESS' }];
    
    // The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key
    // const keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME';
    
    // The encrypted ('wrapped') AES-256 key to use
    // This key should be encrypted using the Cloud KMS key specified above
    // const wrappedKey = 'YOUR_ENCRYPTED_AES_256_KEY'
    
    // The name of the surrogate custom info type to use
    // Only necessary if you want to reverse the deidentification process
    // Can be essentially any arbitrary string, as long as it doesn't appear
    // in your dataset otherwise.
    // const surrogateType = 'EMAIL_ADDRESS_TOKEN';
    
    async function deidentifyDeterministic() {
      // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it
      const cryptoDeterministicEncryption = {
        cryptoKey: {
          kmsWrapped: {
            wrappedKey: wrappedKey,
            cryptoKeyName: keyName,
          },
        },
        surrogateInfoType: {name: surrogateType},
      };
    
      // Construct inspect configuration to match information
      const inspectConfig = {
        infoTypes,
      };
    
      // Associate the encryption with the infotype transformation.
      const infoTypeTransformations = {
        transformations: [
          {
            infoTypes,
            primitiveTransformation: {
              cryptoDeterministicConfig: cryptoDeterministicEncryption,
            },
          },
        ],
      };
    
      // Construct item to inspect
      const item = {value: string};
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: {
          infoTypeTransformations: infoTypeTransformations,
        },
        inspectConfig,
        item: item,
      };
    
      // Run de-identification request
      const [response] = await dlp.deidentifyContent(request);
      const deidentifiedItem = response.item;
    
      // Print results
      console.log(deidentifiedItem.value);
    }
    await deidentifyDeterministic();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoDeterministicConfig;
    use Google\Cloud\Dlp\V2\CryptoKey;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\KmsWrappedCryptoKey;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    
    /**
     * De-identify content through deterministic encryption.
     * Use the Data Loss Prevention API to de-identify sensitive data in a string using deterministic encryption,
     * which is a reversible cryptographic method. The encryption is performed with a wrapped key.
     *
     * @param string $callingProjectId  The Google Cloud project id to use as a parent resource.
     * @param string $inputString       The string to deidentify (will be treated as text).
     * @param string $kmsKeyName        The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key.
     * Example: key_name = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'.
     * @param string $infoTypeName      The Info type name to be inspect.
     * @param string $surrogateTypeName The name of the surrogate custom info type to use.
     * Only necessary if you want to reverse the deidentification process. Can be essentially any arbitrary
     * string, as long as it doesn't appear in your dataset otherwise.
     * @param string $wrappedAesKey     The encrypted ('wrapped') AES-256 key to use.
     *
     * */
    
    function deidentify_deterministic(
        string $callingProjectId,
        string $kmsKeyName,
        string $wrappedAesKey,
        string $inputString = 'My PHONE NUMBER IS 731997681',
        string $infoTypeName = 'PHONE_NUMBER',
        string $surrogateTypeName = 'PHONE_TOKEN'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Specify what content you want the service to DeIdentify.
        $content = (new ContentItem())->setValue($inputString);
    
        // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
        $kmsWrappedCryptoKey = (new KmsWrappedCryptoKey())
            ->setWrappedKey(base64_decode($wrappedAesKey))
            ->setCryptoKeyName($kmsKeyName);
    
        $cryptoKey = (new CryptoKey())
            ->setKmsWrapped($kmsWrappedCryptoKey);
    
        // Specify how the info from the inspection should be encrypted.
        $cryptoDeterministicConfig = (new CryptoDeterministicConfig())
            ->setCryptoKey($cryptoKey);
    
        if (!empty($surrogateTypeName)) {
            $cryptoDeterministicConfig = $cryptoDeterministicConfig->setSurrogateInfoType((new InfoType())
                ->setName($surrogateTypeName));
        }
    
        // Specify the type of info the inspection will look for.
        $infoType = (new InfoType())
            ->setName($infoTypeName);
    
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes([$infoType]);
    
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCryptoDeterministicConfig($cryptoDeterministicConfig);
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        $deidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations($infoTypeTransformations);
    
        // Send the request and receive response from the service.
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($content)
            ->setInspectConfig($inspectConfig);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print the results.
        printf($response->getItem()->getValue());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    from typing import List
    
    import google.cloud.dlp
    
    
    def deidentify_with_deterministic(
        project: str,
        input_str: str,
        info_types: List[str],
        surrogate_type: str = None,
        key_name: str = None,
        wrapped_key: str = None,
    ) -> None:
        """Deidentifies sensitive data in a string using deterministic encryption.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to deidentify (will be treated as text).
            info_types: A list of strings representing info types to look for.
            surrogate_type: The name of the surrogate custom info type to use. Only
                necessary if you want to reverse the deidentification process. Can
                be essentially any arbitrary string, as long as it doesn't appear
                in your dataset otherwise.
            key_name: The name of the Cloud KMS key used to encrypt ('wrap') the
                AES-256 key. Example:
                key_name = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/
                keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
            wrapped_key: The encrypted ('wrapped') AES-256 key to use. This key
                should be encrypted using the Cloud KMS key specified by key_name.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # The wrapped key is base64-encoded, but the library expects a binary
        # string, so decode it here.
        wrapped_key = base64.b64decode(wrapped_key)
    
        # Construct Deterministic encryption configuration dictionary
        crypto_replace_deterministic_config = {
            "crypto_key": {
                "kms_wrapped": {"wrapped_key": wrapped_key, "crypto_key_name": key_name}
            },
        }
    
        # Add surrogate type
        if surrogate_type:
            crypto_replace_deterministic_config["surrogate_info_type"] = {
                "name": surrogate_type
            }
    
        # Construct inspect configuration dictionary
        inspect_config = {"info_types": [{"name": info_type} for info_type in info_types]}
    
        # Construct deidentify configuration dictionary
        deidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {
                        "primitive_transformation": {
                            "crypto_deterministic_config": crypto_replace_deterministic_config
                        }
                    }
                ]
            }
        }
    
        # Convert string to item
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
    
        # Print results
        print(response.item.value)
    
    

##### Deterministic encryption examples: re-identification

This example demonstrates how to re-identify sensitive data that was de-identified through the [`CryptoDeterministicConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#cryptodeterministicconfig) transformation method. For more information, see Deterministic encryption on this page.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    
    public class ReidentifyContentUsingDeterministic
    {
        public static ReidentifyContentResponse ReidentifyDeterministic(
            string projectId,
            string text,
            string keyName,
            string wrappedKey,
            [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) surrogateType = null)
        {
            // Instantiate the client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the infoType if null which will be used as surrogate type and infoType both.
            var infoType = surrogateType ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PHONE_TOKEN" };
    
            // Construct crypto deterministic config using the crypto key name and wrapped key.
            var cryptoDeterministicConfig = new [CryptoDeterministicConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoDeterministicConfig.html)
            {
                CryptoKey = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
                {
                    KmsWrapped = new [KmsWrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KmsWrappedCryptoKey.html)
                    {
                        CryptoKeyName = keyName,
                        WrappedKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromBase64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromBase64_System_String_)(wrappedKey)
                    }
                },
                SurrogateInfoType = infoType,
            };
    
            // Construct the reidentify config using crypto config.
            var reidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations =
                    {
                        new InfoTypeTransformations.Types.InfoTypeTransformation
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                CryptoDeterministicConfig = cryptoDeterministicConfig
                            }
                        }
                    }
                }
            };
    
            // Construct the inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                CustomInfoTypes =
                {
                    new [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html)
                    {
                        InfoType = infoType,
                        SurrogateType = new CustomInfoType.Types.SurrogateType()
                    }
                }
            };
    
            // Construct the request.
            var request = new [ReidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                ReidentifyConfig = reidentifyConfig,
                InspectConfig = inspectConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text },
            };
    
            // Call the API.
            [ReidentifyContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentResponse.html) response = dlp.ReidentifyContent(request);
    
            // Inspect the response.
            Console.WriteLine($"Reidentified content: {response.[Item](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReidentifyContentResponse.html#Google_Cloud_Dlp_V2_ReidentifyContentResponse_Item).[Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)}");
            return response;
        }
    }
    

### Go

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"encoding/base64"
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // reidentifyWithDeterministic re-identifies content encrypted by deterministic encryption.
    func reidentifyWithDeterministic(w io.Writer, projectID, inputStr, surrogateType, keyName, wrappedKey string) error {
    	// projectId := "my-project-id"
    	// inputStr := "EMAIL_ADDRESS_TOKEN(52):AVAx2eIEnIQP5jbNEr2j9wLOAd5m4kpSBR/0jjjGdAOmryzZbE/q"
    	// surrogateType := "EMAIL_ADDRESS_TOKEN"
    	/* keyName :=  "projects/YOUR_PROJECT/"
    	   + "locations/YOUR_KEYRING_REGION/"
    	   + "keyRings/YOUR_KEYRING_NAME/"
    	   + "cryptoKeys/YOUR_KEY_NAME"
    	*/
    	// wrappedKey := "YOUR_ENCRYPTED_AES_256_KEY"
    
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
    
    	// The wrapped key is base64-encoded, but the library expects a binary
    	// string, so decode it here.
    	keyBytes, err := base64.StdEncoding.DecodeString(wrappedKey)
    	if err != nil {
    		return err
    	}
    
    	// Create crypto deterministic config.
    	cryptoDeterministicConfig := &dlppb.CryptoDeterministicConfig{
    		CryptoKey: &dlppb.CryptoKey{
    			Source: &dlppb.CryptoKey_KmsWrapped{
    				KmsWrapped: &dlppb.KmsWrappedCryptoKey{
    					WrappedKey:    keyBytes,
    					CryptoKeyName: keyName,
    				},
    			},
    		},
    		SurrogateInfoType: &dlppb.InfoType{
    			Name: surrogateType,
    		},
    	}
    
    	// Create a config for primitive transformation.
    	primitiveTransformation := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_CryptoDeterministicConfig{
    			CryptoDeterministicConfig: cryptoDeterministicConfig,
    		},
    	}
    
    	transformation := &dlppb.DeidentifyConfig_InfoTypeTransformations{
    		InfoTypeTransformations: &dlppb.InfoTypeTransformations{
    			Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    				{
    					PrimitiveTransformation: primitiveTransformation,
    				},
    			},
    		},
    	}
    
    	// Construct config to re-identify the config.
    	reIdentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: transformation,
    	}
    
    	// Construct a config for inspection.
    	inspectConfig := &dlppb.InspectConfig{
    		CustomInfoTypes: []*dlppb.CustomInfoType{
    			{
    				InfoType: &dlppb.InfoType{
    					Name: surrogateType,
    				},
    				Type: &dlppb.CustomInfoType_SurrogateType_{
    					SurrogateType: &dlppb.CustomInfoType_SurrogateType{},
    				},
    			},
    		},
    	}
    
    	// Item to be analyzed.
    	item := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{
    			Value: inputStr,
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.ReidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		ReidentifyConfig: reIdentifyConfig,
    		InspectConfig:    inspectConfig,
    		Item:             item,
    	}
    
    	// Send the request.
    	r, err := client.ReidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result.
    	fmt.Fprintf(w, "output: %v", r.GetItem().GetValue())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CryptoDeterministicConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoDeterministicConfig.html);
    import com.google.privacy.dlp.v2.[CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.nio.charset.StandardCharsets;
    import org.apache.commons.codec.binary.Base64;
    
    public class ReidentifyWithDeterministicEncryption {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
    
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The string to de-identify.
        String textToIdentify = "My SSN is 372819127";
        // The encrypted ('wrapped') AES-256 key to use.
        // This key should be encrypted using the Cloud KMS key specified by key_name.
        String wrappedKey = "YOUR_ENCRYPTED_AES_256_KEY";
        // The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key.
        String kmsKeyName =
            "projects/YOUR_PROJECT/"
                + "locations/YOUR_KEYRING_REGION/"
                + "keyRings/YOUR_KEYRING_NAME/"
                + "cryptoKeys/YOUR_KEY_NAME";
        // The string to re-identify.
        String textToReIdentify =
            DeIdenitfyWithDeterministicEncryption.deIdentifyWithDeterministicEncryption(
                projectId, textToIdentify, wrappedKey, kmsKeyName);
        reIdentifyWithDeterminsiticEncryption(projectId, textToReIdentify, wrappedKey, kmsKeyName);
      }
    
      // Re-identifies sensitive data in a string that was previously de-identified through
      // deterministic encryption.
      public static void reIdentifyWithDeterminsiticEncryption(
          String projectId, String textToReIdentify, String wrappedKey, String key) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to re-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToReIdentify).build();
    
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[SurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.SurrogateType.html) surrogateType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).SurrogateType.newBuilder().build();
    
          // Specify the surrogate type used at time of de-identification.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) surrogateInfoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder()
                  .setName("SSN_TOKEN")
                  .build();
    
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType = [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder()
                  .setInfoType(surrogateInfoType)
                  .[setSurrogateType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Builder_setSurrogateType_com_google_privacy_dlp_v2_CustomInfoType_SurrogateType_)(surrogateType)
                  .build();
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig = [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType)
                  .build();
    
          // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
          [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html) unwrappedCryptoKey = [KmsWrappedCryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.html).newBuilder()
                  .[setWrappedKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setWrappedKey_com_google_protobuf_ByteString_)(
                      [ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(
                              Base64.decodeBase64(wrappedKey.getBytes(StandardCharsets.UTF_8))))
                  .[setCryptoKeyName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.KmsWrappedCryptoKey.Builder.html#com_google_privacy_dlp_v2_KmsWrappedCryptoKey_Builder_setCryptoKeyName_java_lang_String_)(key)
                  .build();
          [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html) cryptoKey = [CryptoKey](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.html).newBuilder()
                  .[setKmsWrapped](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoKey.Builder.html#com_google_privacy_dlp_v2_CryptoKey_Builder_setKmsWrapped_com_google_privacy_dlp_v2_KmsWrappedCryptoKey_)(unwrappedCryptoKey)
                  .build();
    
          [CryptoDeterministicConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoDeterministicConfig.html) cryptoDeterministicConfig = [CryptoDeterministicConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CryptoDeterministicConfig.html).newBuilder()
                  .setSurrogateInfoType(surrogateInfoType)
                  .setCryptoKey(cryptoKey)
                  .build();
    
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation = [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setCryptoDeterministicConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setCryptoDeterministicConfig_com_google_privacy_dlp_v2_CryptoDeterministicConfig_)(cryptoDeterministicConfig)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) infoTypeTransformation =
              [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).InfoTypeTransformation.newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
    
          [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html) transformations = [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder()
                  .[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(infoTypeTransformation)
                  .build();
    
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig = [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder()
                  .setInfoTypeTransformations(transformations)
                  .build();
    
          // Combine configurations into a request for the service.
          [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html) request = [ReidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(contentItem)
                  .setInspectConfig(inspectConfig)
                  .[setReidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentRequest.Builder.html#com_google_privacy_dlp_v2_ReidentifyContentRequest_Builder_setReidentifyConfig_com_google_privacy_dlp_v2_DeidentifyConfig_)(deidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service.
          [ReidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html) response = dlp.reidentifyContent(request);
    
          // Print the results.
          System.out.println("Text after re-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReidentifyContentResponse.html#com_google_privacy_dlp_v2_ReidentifyContentResponse_getItem__)().getValue());
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
    // const projectId = 'my-project';
    
    // The string to deidentify
    // const string = 'My name is Alicia Abernathy, and my email address is EMAIL_ADDRESS_TOKEN(52):XXXXXX';
    
    // The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key
    // const keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME';
    
    // The encrypted ('wrapped') AES-256 key to use
    // This key should be encrypted using the Cloud KMS key specified above
    // const wrappedKey = 'YOUR_ENCRYPTED_AES_256_KEY'
    
    // The name of the surrogate custom info type to use
    // Only necessary if you want to reverse the de-identification process
    // Can be essentially any arbitrary string, as long as it doesn't appear
    // in your dataset otherwise.
    // const surrogateType = 'EMAIL_ADDRESS_TOKEN';
    
    async function reidentifyDeterministic() {
      // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it
      const cryptoDeterministicEncryption = {
        cryptoKey: {
          kmsWrapped: {
            wrappedKey: wrappedKey,
            cryptoKeyName: keyName,
          },
        },
        surrogateInfoType: {name: surrogateType},
      };
    
      // Construct custom infotype to match information
      const customInfoTypes = [
        {
          infoType: {
            name: surrogateType,
          },
          surrogateType: {},
        },
      ];
    
      // Associate the encryption with the infotype transformation.
      const infoTypeTransformations = {
        transformations: [
          {
            infoTypes: [{name: surrogateType}],
            primitiveTransformation: {
              cryptoDeterministicConfig: cryptoDeterministicEncryption,
            },
          },
        ],
      };
    
      // Construct item to inspect
      const item = {value: string};
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        reidentifyConfig: {
          infoTypeTransformations: infoTypeTransformations,
        },
        inspectConfig: {customInfoTypes},
        item,
      };
    
      // Run re-identification request
      const [response] = await dlp.reidentifyContent(request);
      const deidentifiedItem = response.item;
    
      // Print results
      console.log(deidentifiedItem.value);
    }
    await reidentifyDeterministic();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoDeterministicConfig;
    use Google\Cloud\Dlp\V2\CryptoKey;
    use Google\Cloud\Dlp\V2\CustomInfoType;
    use Google\Cloud\Dlp\V2\CustomInfoType\SurrogateType;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\KmsWrappedCryptoKey;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\ReidentifyContentRequest;
    
    /**
     * Re-identify content encrypted by deterministic encryption.
     * Re-identify content that was previously de-identified through deterministic encryption.
     *
     * @param string $callingProjectId  The GCP Project ID to run the API call under.
     * @param string $string            The string to reidentify.
     * @param string $keyName           The name of the Cloud KMS key used to encrypt (wrap) the AES-256 key.
     * @param string $wrappedKey        The name of the Cloud KMS key use, encrypted with the KMS key in $keyName.
     * @param string $surrogateTypeName Surrogate custom info type to enable reidentification.
     */
    function reidentify_deterministic(
        string $callingProjectId,
        string $string,
        string $surrogateTypeName,
        string $keyName,
        string $wrappedKey
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Specify what content you want the service to Re-identify.
        $item = (new ContentItem())
            ->setValue($string);
    
        // Specify the surrogate type used at time of de-identification.
        $surrogateType = (new InfoType())
            ->setName($surrogateTypeName);
    
        $customInfoType = (new CustomInfoType())
            ->setInfoType($surrogateType)
            ->setSurrogateType(new SurrogateType());
    
        // Create the inspect configuration object.
        $inspectConfig = (new InspectConfig())
            ->setCustomInfoTypes([$customInfoType]);
    
        // Specify an encrypted AES-256 key and the name of the Cloud KMS key that encrypted it.
        $kmsWrappedCryptoKey = (new KmsWrappedCryptoKey())
            ->setWrappedKey(base64_decode($wrappedKey))
            ->setCryptoKeyName($keyName);
    
        // Create the crypto key configuration object.
        $cryptoKey = (new CryptoKey())
            ->setKmsWrapped($kmsWrappedCryptoKey);
    
        // Create the crypto deterministic configuration object.
        $cryptoDeterministicConfig = (new CryptoDeterministicConfig())
            ->setCryptoKey($cryptoKey)
            ->setSurrogateInfoType($surrogateType);
    
        // Create the information transform configuration objects.
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setCryptoDeterministicConfig($cryptoDeterministicConfig);
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Create the reidentification configuration object.
        $reidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations($infoTypeTransformations);
    
        // Run request.
        $reidentifyContentRequest = (new ReidentifyContentRequest())
            ->setParent($parent)
            ->setReidentifyConfig($reidentifyConfig)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->reidentifyContent($reidentifyContentRequest);
    
        // Print the results.
        printf($response->getItem()->getValue());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    
    import google.cloud.dlp
    
    
    def reidentify_with_deterministic(
        project: str,
        input_str: str,
        surrogate_type: str = None,
        key_name: str = None,
        wrapped_key: str = None,
    ) -> None:
        """Re-identifies content that was previously de-identified through deterministic encryption.
        Args:
            project: The Google Cloud project ID to use as a parent resource.
            input_str: The string to be re-identified. Provide the entire token. Example:
                EMAIL_ADDRESS_TOKEN(52):AVAx2eIEnIQP5jbNEr2j9wLOAd5m4kpSBR/0jjjGdAOmryzZbE/q
            surrogate_type: The name of the surrogate custom infoType used
                during the encryption process.
            key_name: The name of the Cloud KMS key used to encrypt ("wrap") the
                AES-256 key. Example:
                keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/
                keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
            wrapped_key: The encrypted ("wrapped") AES-256 key previously used to encrypt the content.
                This key must have been encrypted using the Cloud KMS key specified by key_name.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # The wrapped key is base64-encoded, but the library expects a binary
        # string, so decode it here.
        wrapped_key = base64.b64decode(wrapped_key)
    
        # Construct reidentify Configuration
        reidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {
                        "primitive_transformation": {
                            "crypto_deterministic_config": {
                                "crypto_key": {
                                    "kms_wrapped": {
                                        "wrapped_key": wrapped_key,
                                        "crypto_key_name": key_name,
                                    }
                                },
                                "surrogate_info_type": {"name": surrogate_type},
                            }
                        }
                    }
                ]
            }
        }
    
        inspect_config = {
            "custom_info_types": [
                {"info_type": {"name": surrogate_type}, "surrogate_type": {}}
            ]
        }
    
        # Convert string to item
        item = {"value": input_str}
    
        # Call the API
        response = dlp.[reidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_reidentify_content)(
            request={
                "parent": parent,
                "reidentify_config": reidentify_config,
                "inspect_config": inspect_config,
                "item": item,
            }
        )
    
        # Print results
        print(response.item.value)
    
    

### Bucketing

The bucketing transformations serve to de-identify numerical data by "bucketing" it into ranges. The resulting number range is a hyphenated string consisting of a lower bound, a hyphen, and an upper bound.

#### Fixed-size bucketing

Sensitive Data Protection can bucket numerical input values based on fixed size ranges ([`FixedSizeBucketingConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#fixedsizebucketingconfig) in the DLP API). You specify the following to configure fixed-size bucketing:

  * The lower bound value of all of the buckets. Any values less than the lower bound are grouped together in a single bucket.
  * The upper bound value of all of the buckets. Any values greater than the upper bound are grouped together in a single bucket.
  * The size of each bucket other than the minimum and maximum buckets.



For example, if the lower bound is set to 10, the upper bound is set to 89, and the bucket size is set to 10, then the following buckets would be used: -10, 10-20, 20-30, 30-40, 40-50, 50-60, 60-70, 70-80, 80-89, 89+.

For more information about the concept of bucketing, see [Generalization and Bucketing](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing).

#### Customizable bucketing

Customizable bucketing ([`BucketingConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#fixedsizebucketingconfig) in the DLP API) offers more flexibility than fixed size bucketing. Instead of specifying upper and lower bounds and an interval value with which to create equal-sized buckets, you specify the maximum and minimum values for each bucket you want created. Each maximum and minimum value pair must have the same type.

You set up customizable bucketing by specifying individual buckets. Each bucket has the following properties:

  * The lower bound of the bucket's range. Omit this value to create a bucket that has no lower bound.
  * The upper bound of the bucket's range. Omit this value to create a bucket that has no upper bound.
  * The replacement value for this bucket range. This is the value with which to replace all detected values that fall within the lower and upper bounds. If you don't provide a replacement value, a hyphenated min-max range will be generated instead.



For example, consider the following JSON configuration for this bucketing transformation:
    
    
    "bucketingConfig":{
      "buckets":[
        {
          "min":{
            "integerValue":"1"
          },
          "max":{
            "integerValue":"30"
          },
          "replacementValue":{
            "stringValue":"LOW"
          }
        },
        {
          "min":{
            "integerValue":"31"
          },
          "max":{
            "integerValue":"65"
          },
          "replacementValue":{
            "stringValue":"MEDIUM"
          }
        },
        {
          "min":{
            "integerValue":"66"
          },
          "max":{
            "integerValue":"100"
          },
          "replacementValue":{
            "stringValue":"HIGH"
          }
        }
      ]
    }
    

This defines the following behavior:

  * Integer values falling between 1 and 30 are masked by being replaced with `LOW`.
  * Integer values falling between 31-65 are masked by being replaced with `MEDIUM`.
  * Integer values falling between 66-100 are masked by being replaced with `HIGH`.



For more information about the concept of bucketing, see [Generalization and Bucketing](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing).

### Date shifting

When you use the date shifting transformation ([`DateShiftConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#dateshiftconfig) in the DLP API on a date input value, Sensitive Data Protection shifts the dates by a random number of days.

Date shifting techniques randomly shift a set of dates but preserve the sequence and duration of a period of time. Shifting dates is usually done in context to an individual or an entity. That is, you want to shift all of the dates for a specific individual using the same shift differential but use a separate shift differential for each other individual.

For more information about date shifting, see [Date shifting](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-date-shifting).

Following is sample code in several languages that demonstrates how to use the Cloud DLP API to de-identify dates using date shifting.

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.common.base.Splitter;
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[DateShiftConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DateShiftConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import com.google.type.[Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html);
    import java.io.BufferedReader;
    import java.io.BufferedWriter;
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    import java.time.LocalDate;
    import java.time.format.DateTimeFormatter;
    import java.util.Arrays;
    import java.util.List;
    import java.util.stream.Collectors;
    
    public class DeIdentifyWithDateShift {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        Path inputCsvFile = Paths.get("path/to/your/input/file.csv");
        Path outputCsvFile = Paths.get("path/to/your/output/file.csv");
        deIdentifyWithDateShift(projectId, inputCsvFile, outputCsvFile);
      }
    
      public static void deIdentifyWithDateShift(
          String projectId, Path inputCsvFile, Path outputCsvFile) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Read the contents of the CSV file into a Table
          List<FieldId> headers;
          List<Table.[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html)> rows;
          try (BufferedReader input = Files.newBufferedReader(inputCsvFile)) {
            // Parse and convert the first line into header names
            headers =
                Arrays.stream(input.readLine().split(","))
                    .map(header -> [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName(header).build())
                    .collect(Collectors.toList());
            // Parse the remainder of the file as Table.Rows
            rows =
                input.lines().map(DeIdentifyWithDateShift::parseLineAsRow).collect(Collectors.toList());
          }
          [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) table = [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder().[addAllHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addAllHeaders_java_lang_Iterable___extends_com_google_privacy_dlp_v2_FieldId__)(headers).[addAllRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addAllRows_java_lang_Iterable___extends_com_google_privacy_dlp_v2_Table_Row__)(rows).build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(table).build();
    
          // Set the maximum days to shift dates backwards (lower bound) or forward (upper bound)
          [DateShiftConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DateShiftConfig.html) dateShiftConfig =
              [DateShiftConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DateShiftConfig.html).newBuilder().[setLowerBoundDays](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DateShiftConfig.Builder.html#com_google_privacy_dlp_v2_DateShiftConfig_Builder_setLowerBoundDays_int_)(5).[setUpperBoundDays](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DateShiftConfig.Builder.html#com_google_privacy_dlp_v2_DateShiftConfig_Builder_setUpperBoundDays_int_)(5).build();
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) transformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder().[setDateShiftConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setDateShiftConfig_com_google_privacy_dlp_v2_DateShiftConfig_)(dateShiftConfig).build();
          // Specify which fields the DateShift should apply too
          List<FieldId> dateFields = Arrays.asList(headers.get(1), headers.get(3));
          [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html) fieldTransformation =
              [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html).newBuilder()
                  .[addAllFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.Builder.html#com_google_privacy_dlp_v2_FieldTransformation_Builder_addAllFields_java_lang_Iterable___extends_com_google_privacy_dlp_v2_FieldId__)(dateFields)
                  .setPrimitiveTransformation(transformation)
                  .build();
          [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html) recordTransformations =
              [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html).newBuilder().addFieldTransformations(fieldTransformation).build();
          // Specify the config for the de-identify request
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder().[setRecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.Builder.html#com_google_privacy_dlp_v2_DeidentifyConfig_Builder_setRecordTransformations_com_google_privacy_dlp_v2_RecordTransformations_)(recordTransformations).build();
    
          // Combine configurations into a request for the service.
          [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html) request =
              [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setDeidentifyConfig(deidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service
          [DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html) response = dlp.deidentifyContent(request);
    
          // Write the results to the target CSV file
          try (BufferedWriter writer = Files.newBufferedWriter(outputCsvFile)) {
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) outTable = response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getTable();
            String headerOut =
                outTable.[getHeadersList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html#com_google_privacy_dlp_v2_Table_getHeadersList__)().stream()
                    .map(FieldId::getName)
                    .collect(Collectors.joining(","));
            writer.write(headerOut + "\n");
    
            List<String> rowOutput =
                outTable.[getRowsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html#com_google_privacy_dlp_v2_Table_getRowsList__)().stream()
                    .map(row -> joinRow(row.getValuesList()))
                    .collect(Collectors.toList());
            for (String line : rowOutput) {
              writer.write(line + "\n");
            }
            System.out.println("Content written to file: " + outputCsvFile.toString());
          }
        }
      }
    
      // Convert the string from the csv file into com.google.type.Date
      public static [Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html) parseAsDate(String s) {
        LocalDate date = LocalDate.parse(s, DateTimeFormatter.ofPattern("MM/dd/yyyy"));
        return [Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html).newBuilder()
            .setDay(date.getDayOfMonth())
            .setMonth(date.getMonthValue())
            .setYear(date.getYear())
            .build();
      }
    
      // Each row is in the format: Name,BirthDate,CreditCardNumber,RegisterDate
      public static [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).[Row](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Row.html) parseLineAsRow(String line) {
        List<String> values = Splitter.on(",").splitToList(line);
        [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html) name = [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)(values.get(0)).build();
        [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html) birthDate = [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setDateValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setDateValue_com_google_type_Date_)(parseAsDate(values.get(1))).build();
        [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html) creditCardNumber = [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)(values.get(2)).build();
        [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html) registerDate = [Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setDateValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setDateValue_com_google_type_Date_)(parseAsDate(values.get(3))).build();
        return [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
            .addValues(name)
            .addValues(birthDate)
            .addValues(creditCardNumber)
            .addValues(registerDate)
            .build();
      }
    
      public static String formatDate([Date](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html) d) {
        return String.format("%s/%s/%s", d.[getMonth](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html#com_google_type_Date_getMonth__)(), d.[getDay](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html#com_google_type_Date_getDay__)(), d.[getYear](https://docs.cloud.google.com/java/docs/reference/proto-google-common-protos/latest/com.google.type.Date.html#com_google_type_Date_getYear__)());
      }
    
      public static String joinRow(List<Value> values) {
        String name = values.get(0).getStringValue();
        String birthDate = formatDate(values.get(1).getDateValue());
        String creditCardNumber = values.get(2).getStringValue();
        String registerDate = formatDate(values.get(3).getDateValue());
        return String.join(",", name, birthDate, creditCardNumber, registerDate);
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('@google-cloud/dlp');
    
    // Instantiates a client
    const dlp = new DLP.DlpServiceClient();
    
    // Import other required libraries
    const fs = require('fs');
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The path to the CSV file to deidentify
    // The first row of the file must specify column names, and all other rows
    // must contain valid values
    // const inputCsvFile = '/path/to/input/file.csv';
    
    // The path to save the date-shifted CSV file to
    // const outputCsvFile = '/path/to/output/file.csv';
    
    // The list of (date) fields in the CSV file to date shift
    // const dateFields = [{ name: 'birth_date'}, { name: 'register_date' }];
    
    // The maximum number of days to shift a date backward
    // const lowerBoundDays = 1;
    
    // The maximum number of days to shift a date forward
    // const upperBoundDays = 1;
    
    // (Optional) The column to determine date shift amount based on
    // If this is not specified, a random shift amount will be used for every row
    // If this is specified, then 'wrappedKey' and 'keyName' must also be set
    // const contextFieldId = [{ name: 'user_id' }];
    
    // (Optional) The name of the Cloud KMS key used to encrypt ('wrap') the AES-256 key
    // If this is specified, then 'wrappedKey' and 'contextFieldId' must also be set
    // const keyName = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME';
    
    // (Optional) The encrypted ('wrapped') AES-256 key to use when shifting dates
    // This key should be encrypted using the Cloud KMS key specified above
    // If this is specified, then 'keyName' and 'contextFieldId' must also be set
    // const wrappedKey = 'YOUR_ENCRYPTED_AES_256_KEY'
    
    // Helper function for converting CSV rows to Protobuf types
    const rowToProto = row => {
      const values = row.split(',');
      const convertedValues = values.map(value => {
        if (Date.parse(value)) {
          const date = new Date(value);
          return {
            dateValue: {
              year: date.getFullYear(),
              month: date.getMonth() + 1,
              day: date.getDate(),
            },
          };
        } else {
          // Convert all non-date values to strings
          return {stringValue: value.toString()};
        }
      });
      return {values: convertedValues};
    };
    
    async function deidentifyWithDateShift() {
      // Read and parse a CSV file
      const csvLines = fs
        .readFileSync(inputCsvFile)
        .toString()
        .split('\n')
        .filter(line => line.includes(','));
      const csvHeaders = csvLines[0].split(',');
      const csvRows = csvLines.slice(1);
    
      // Construct the table object
      const tableItem = {
        table: {
          headers: csvHeaders.map(header => {
            return {name: header};
          }),
          rows: csvRows.map(row => rowToProto(row)),
        },
      };
    
      // Construct DateShiftConfig
      const dateShiftConfig = {
        lowerBoundDays: lowerBoundDays,
        upperBoundDays: upperBoundDays,
      };
    
      if (contextFieldId && keyName && wrappedKey) {
        dateShiftConfig.context = {name: contextFieldId};
        dateShiftConfig.cryptoKey = {
          kmsWrapped: {
            wrappedKey: wrappedKey,
            cryptoKeyName: keyName,
          },
        };
      } else if (contextFieldId || keyName || wrappedKey) {
        throw new Error(
          'You must set either ALL or NONE of {contextFieldId, keyName, wrappedKey}!'
        );
      }
    
      // Construct deidentification request
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: {
          recordTransformations: {
            fieldTransformations: [
              {
                fields: dateFields,
                primitiveTransformation: {
                  dateShiftConfig: dateShiftConfig,
                },
              },
            ],
          },
        },
        item: tableItem,
      };
    
      // Run deidentification request
      const [response] = await dlp.deidentifyContent(request);
      const tableRows = response.item.table.rows;
    
      // Write results to a CSV file
      tableRows.forEach((row, rowIndex) => {
        const rowValues = row.values.map(
          value =>
            value.stringValue ||
            `${value.dateValue.month}/${value.dateValue.day}/${value.dateValue.year}`
        );
        csvLines[rowIndex + 1] = rowValues.join(',');
      });
      csvLines.push('');
      fs.writeFileSync(outputCsvFile, csvLines.join('\n'));
    
      // Print status
      console.log(`Successfully saved date-shift output to ${outputCsvFile}`);
    }
    
    deidentifyWithDateShift();

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import base64
    import csv
    from datetime import datetime
    from typing import List
    
    import google.cloud.dlp
    from google.cloud.dlp_v2 import [types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.html)
    
    
    def deidentify_with_date_shift(
        project: str,
        input_csv_file: str = None,
        output_csv_file: str = None,
        date_fields: List[str] = None,
        lower_bound_days: int = None,
        upper_bound_days: int = None,
        context_field_id: str = None,
        wrapped_key: str = None,
        key_name: str = None,
    ) -> None:
        """Uses the Data Loss Prevention API to deidentify dates in a CSV file by
            pseudorandomly shifting them.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_csv_file: The path to the CSV file to deidentify. The first row
                of the file must specify column names, and all other rows must
                contain valid values.
            output_csv_file: The path to save the date-shifted CSV file.
            date_fields: The list of (date) fields in the CSV file to date shift.
                Example: ['birth_date', 'register_date']
            lower_bound_days: The maximum number of days to shift a date backward
            upper_bound_days: The maximum number of days to shift a date forward
            context_field_id: (Optional) The column to determine date shift amount
                based on. If this is not specified, a random shift amount will be
                used for every row. If this is specified, then 'wrappedKey' and
                'keyName' must also be set. Example:
                contextFieldId = [{ 'name': 'user_id' }]
            key_name: (Optional) The name of the Cloud KMS key used to encrypt
                ('wrap') the AES-256 key. Example:
                key_name = 'projects/YOUR_GCLOUD_PROJECT/locations/YOUR_LOCATION/
                keyRings/YOUR_KEYRING_NAME/cryptoKeys/YOUR_KEY_NAME'
            wrapped_key: (Optional) The encrypted ('wrapped') AES-256 key to use.
                This key should be encrypted using the Cloud KMS key specified by
                key_name.
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Convert date field list to Protobuf type
        def map_fields(field: str) -> dict:
            return {"name": field}
    
        if date_fields:
            date_fields = map(map_fields, date_fields)
        else:
            date_fields = []
    
        f = []
        with open(input_csv_file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                f.append(row)
    
        #  Helper function for converting CSV rows to Protobuf types
        def map_headers(header: str) -> dict:
            return {"name": header}
    
        def map_data(value: str) -> dict:
            try:
                date = datetime.strptime(value, "%m/%d/%Y")
                return {
                    "date_value": {"year": date.year, "month": date.month, "day": date.day}
                }
            except ValueError:
                return {"string_value": value}
    
        def map_rows(row: str) -> dict:
            return {"values": map(map_data, row)}
    
        # Using the helper functions, convert CSV rows to protobuf-compatible
        # dictionaries.
        csv_headers = map(map_headers, f[0])
        csv_rows = map(map_rows, f[1:])
    
        # Construct the table dict
        table_item = {"table": {"headers": csv_headers, "rows": csv_rows}}
    
        # Construct date shift config
        date_shift_config = {
            "lower_bound_days": lower_bound_days,
            "upper_bound_days": upper_bound_days,
        }
    
        # If using a Cloud KMS key, add it to the date_shift_config.
        # The wrapped key is base64-encoded, but the library expects a binary
        # string, so decode it here.
        if context_field_id and key_name and wrapped_key:
            date_shift_config["context"] = {"name": context_field_id}
            date_shift_config["crypto_key"] = {
                "kms_wrapped": {
                    "wrapped_key": base64.b64decode(wrapped_key),
                    "crypto_key_name": key_name,
                }
            }
        elif context_field_id or key_name or wrapped_key:
            raise ValueError(
                """You must set either ALL or NONE of
            [context_field_id, key_name, wrapped_key]!"""
            )
    
        # Construct Deidentify Config
        deidentify_config = {
            "record_transformations": {
                "field_transformations": [
                    {
                        "fields": date_fields,
                        "primitive_transformation": {
                            "date_shift_config": date_shift_config
                        },
                    }
                ]
            }
        }
    
        # Write to CSV helper methods
        def write_header(header: [types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.html).storage.[FieldId](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.FieldId.html)) -> str:
            return header.name
    
        def write_data(data: [types](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.html).storage.[Value](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Value.html)) -> str:
            return data.string_value or "{}/{}/{}".format(
                data.date_value.month,
                data.date_value.day,
                data.date_value.year,
            )
    
        # Call the API
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={
                "parent": parent,
                "deidentify_config": deidentify_config,
                "item": table_item,
            }
        )
    
        # Write results to CSV file
        with open(output_csv_file, "w") as csvfile:
            write_file = csv.writer(csvfile, delimiter=",")
            write_file.writerow(map(write_header, response.item.table.headers))
            for row in response.item.table.rows:
                write_file.writerow(map(write_data, row.values))
        # Print status
        print(f"Successfully saved date-shift output to {output_csv_file}")
    
    

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
    
    // deidentifyDateShift shifts dates found in the input between lowerBoundDays and
    // upperBoundDays.
    func deidentifyDateShift(w io.Writer, projectID string, lowerBoundDays, upperBoundDays int32, input string) error {
    	// projectID := "my-project-id"
    	// lowerBoundDays := -1
    	// upperBound := -1
    	// input := "2016-01-10"
    	// Will print "2016-01-09"
    	ctx := context.Background()
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    	// Create a configured request.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    				InfoTypeTransformations: &dlppb.InfoTypeTransformations{
    					Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    						{
    							InfoTypes: []*dlppb.InfoType{}, // Match all info types.
    							PrimitiveTransformation: &dlppb.PrimitiveTransformation{
    								Transformation: &dlppb.PrimitiveTransformation_DateShiftConfig{
    									DateShiftConfig: &dlppb.DateShiftConfig{
    										LowerBoundDays: lowerBoundDays,
    										UpperBoundDays: upperBoundDays,
    									},
    								},
    							},
    						},
    					},
    				},
    			},
    		},
    		// The InspectConfig is used to identify the DATE fields.
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes: []*dlppb.InfoType{
    				{
    					Name: "DATE",
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
    

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use DateTime;
    use Exception;
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CryptoKey;
    use Google\Cloud\Dlp\V2\DateShiftConfig;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\FieldTransformation;
    use Google\Cloud\Dlp\V2\KmsWrappedCryptoKey;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\RecordTransformations;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\Value;
    use Google\Type\Date;
    
    /**
     * Deidentify dates in a CSV file by pseudorandomly shifting them.
     * If contextFieldName is not specified, a random shift amount will be used for every row.
     * If contextFieldName is specified, then 'wrappedKey' and 'keyName' must also be set.
     *
     * @param string $callingProjectId  The GCP Project ID to run the API call under
     * @param string $inputCsvFile      The path to the CSV file to deidentify
     * @param string $outputCsvFile     The path to save the date-shifted CSV file to
     * @param string $dateFieldNames    The comma-separated list of (date) fields in the CSV file to date shift
     * @param int    $lowerBoundDays    The maximum number of days to shift a date backward
     * @param int    $upperBoundDays    The maximum number of days to shift a date forward
     * @param string $contextFieldName  (Optional) The column to determine date shift amount based on
     * @param string $keyName           (Optional) The encrypted ('wrapped') AES-256 key to use when shifting dates
     * @param string $wrappedKey        (Optional) The name of the Cloud KMS key used to encrypt (wrap) the AES-256 key
     */
    function deidentify_dates(
        string $callingProjectId,
        string $inputCsvFile,
        string $outputCsvFile,
        string $dateFieldNames,
        int $lowerBoundDays,
        int $upperBoundDays,
        string $contextFieldName = '',
        string $keyName = '',
        string $wrappedKey = ''
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Read a CSV file
        $csvLines = file($inputCsvFile, FILE_IGNORE_NEW_LINES);
        $csvHeaders = explode(',', $csvLines[0]);
        $csvRows = array_slice($csvLines, 1);
    
        // Convert CSV file into protobuf objects
        $tableHeaders = array_map(function ($csvHeader) {
            return (new FieldId)->setName($csvHeader);
        }, $csvHeaders);
    
        $tableRows = array_map(function ($csvRow) {
            $rowValues = array_map(function ($csvValue) {
                if ($csvDate = DateTime::createFromFormat('m/d/Y', $csvValue)) {
                    $date = (new Date())
                        ->setYear((int) $csvDate->format('Y'))
                        ->setMonth((int) $csvDate->format('m'))
                        ->setDay((int) $csvDate->format('d'));
                    return (new Value())
                        ->setDateValue($date);
                } else {
                    return (new Value())
                        ->setStringValue($csvValue);
                }
            }, explode(',', $csvRow));
    
            return (new Row())
                ->setValues($rowValues);
        }, $csvRows);
    
        // Convert date fields into protobuf objects
        $dateFields = array_map(function ($dateFieldName) {
            return (new FieldId())->setName($dateFieldName);
        }, explode(',', $dateFieldNames));
    
        // Construct the table object
        $table = (new Table())
            ->setHeaders($tableHeaders)
            ->setRows($tableRows);
    
        $item = (new ContentItem())
            ->setTable($table);
    
        // Construct dateShiftConfig
        $dateShiftConfig = (new DateShiftConfig())
            ->setLowerBoundDays($lowerBoundDays)
            ->setUpperBoundDays($upperBoundDays);
    
        if ($contextFieldName && $keyName && $wrappedKey) {
            $contextField = (new FieldId())
                ->setName($contextFieldName);
    
            // Create the wrapped crypto key configuration object
            $kmsWrappedCryptoKey = (new KmsWrappedCryptoKey())
                ->setWrappedKey(base64_decode($wrappedKey))
                ->setCryptoKeyName($keyName);
    
            $cryptoKey = (new CryptoKey())
                ->setKmsWrapped($kmsWrappedCryptoKey);
    
            $dateShiftConfig
                ->setContext($contextField)
                ->setCryptoKey($cryptoKey);
        } elseif ($contextFieldName || $keyName || $wrappedKey) {
            throw new Exception('You must set either ALL or NONE of {$contextFieldName, $keyName, $wrappedKey}!');
        }
    
        // Create the information transform configuration objects
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setDateShiftConfig($dateShiftConfig);
    
        $fieldTransformation = (new FieldTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setFields($dateFields);
    
        $recordTransformations = (new RecordTransformations())
            ->setFieldTransformations([$fieldTransformation]);
    
        // Create the deidentification configuration object
        $deidentifyConfig = (new DeidentifyConfig())
            ->setRecordTransformations($recordTransformations);
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Run request
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($item);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Check for errors
        foreach ($response->getOverview()->getTransformationSummaries() as $summary) {
            foreach ($summary->getResults() as $result) {
                if ($details = $result->getDetails()) {
                    printf('Error: %s' . PHP_EOL, $details);
                    return;
                }
            }
        }
    
        // Save the results to a file
        $csvRef = fopen($outputCsvFile, 'w');
        fputcsv($csvRef, $csvHeaders);
        foreach ($response->getItem()->getTable()->getRows() as $tableRow) {
            $values = array_map(function ($tableValue) {
                if ($tableValue->getStringValue()) {
                    return $tableValue->getStringValue();
                }
                $protoDate = $tableValue->getDateValue();
                $date = mktime(0, 0, 0, $protoDate->getMonth(), $protoDate->getDay(), $protoDate->getYear());
                return strftime('%D', $date);
            }, iterator_to_array($tableRow->getValues()));
            fputcsv($csvRef, $values);
        };
        fclose($csvRef);
        printf('Deidentified dates written to %s' . PHP_EOL, $outputCsvFile);
    }

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.IO;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    
    public class DeidentifyWithDateShift
    {
        public static DeidentifyContentResponse Deidentify(
            string projectId,
            string inputCsvFilePath,
            int lowerBoundDays,
            int upperBoundDays,
            string dateFields,
            string contextField,
            string keyName,
            string wrappedKey)
        {
            var hasKeyName = !string.IsNullOrEmpty(keyName);
            var hasWrappedKey = !string.IsNullOrEmpty(wrappedKey);
            var hasContext = !string.IsNullOrEmpty(contextField);
            bool allFieldsSet = hasKeyName && hasWrappedKey && hasContext;
            bool noFieldsSet = !hasKeyName && !hasWrappedKey && !hasContext;
            if (!(allFieldsSet || noFieldsSet))
            {
                throw new ArgumentException("Must specify ALL or NONE of: {contextFieldId, keyName, wrappedKey}!");
            }
    
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Read file
            var csvLines = File.ReadAllLines(inputCsvFilePath);
            var csvHeaders = csvLines[0].Split(',');
            var csvRows = csvLines.Skip(1).ToArray();
    
            // Convert dates to protobuf format, and everything else to a string
            var protoHeaders = csvHeaders.Select(header => new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = header });
            var protoRows = csvRows.Select(csvRow =>
            {
                var rowValues = csvRow.Split(',');
                var protoValues = rowValues.Select(rowValue =>
                   System.[DateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime.html).TryParse(rowValue, out var parsedDate)
                   ? new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { DateValue = Google.[Type](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Type.html).[Date](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateTime.html#Google_Cloud_Dlp_V2_DateTime_Date).[FromDateTime](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html#Google_Protobuf_WellKnownTypes_Timestamp_FromDateTime_System_DateTime_)(parsedDate) }
                   : new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = rowValue });
    
                var rowObject = new Table.Types.Row();
                rowObject.Values.[Add](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ExtensionRegistry.html#Google_Protobuf_ExtensionRegistry_Add_Google_Protobuf_Extension_)(protoValues);
                return rowObject;
            });
    
            var dateFieldList = dateFields
                .Split(',')
                .Select(field => new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = field });
    
            // Construct + execute the request
            var dateShiftConfig = new [DateShiftConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DateShiftConfig.html)
            {
                LowerBoundDays = lowerBoundDays,
                UpperBoundDays = upperBoundDays
            };
    
            dateShiftConfig.Context = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = contextField };
            dateShiftConfig.[CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html) = new [CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CryptoKey.html)
            {
                KmsWrapped = new [KmsWrappedCryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.KmsWrappedCryptoKey.html)
                {
                    WrappedKey = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[FromBase64](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_FromBase64_System_String_)(wrappedKey),
                    CryptoKeyName = keyName
                }
            };
    
            var deidConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                RecordTransformations = new [RecordTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformations.html)
                {
                    FieldTransformations =
                    {
                        new [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.html)
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                DateShiftConfig = dateShiftConfig
                            },
                            Fields = { dateFieldList }
                        }
                    }
                }
            };
    
            var response = dlp.DeidentifyContent(
                new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
                {
                    Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                    DeidentifyConfig = deidConfig,
                    Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html)
                    {
                        Table = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                        {
                            Headers = { protoHeaders },
                            Rows = { protoRows }
                        }
                    }
                });
    
            return response;
        }
    }

### Time extraction

Performing time extraction ([`TimePartConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#timepartconfig) in the DLP API) object preserves a portion of a matched value that on a date, a time, or a timestamp preserves a portion of a matched value. You specify to Sensitive Data Protection what kind of time value you want to extract, including year, month, day of the month, and so on (enumerated in the [`TimePart`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.deidentifyTemplates#timepart) object).

For example, suppose you've configured a `timePartConfig` transformation by setting the time part to extract to `YEAR`. After sending the data in the first column below to Sensitive Data Protection, you'd end up with the transformed values in the second column:

Original values | Transformed values  
---|---  
`9/21/1976` | `1976`  
`6/7/1945` | `1945`  
`1/20/2009` | `2009`  
`7/4/1776` | `1776`  
`8/1/1984` | `1984`  
`4/21/1982` | `1982`  
  
**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyWithTimeExtraction
    {
        public static Table Deidentify(
            string projectId,
            [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html) tableToInspect = null)
        {
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the table if null.
            if (tableToInspect == null)
            {
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)
                    {
                        DateValue = new Google.Type.Date { Day = 10, Month = 6, Year = 2020 }
                    }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)
                    {
                        DateValue = new Google.Type.Date { Day = 23, Month = 12, Year = 2022 }
                    }
                };
                var row3 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)
                    {
                        DateValue = new Google.Type.Date { Day = 1, Month = 1, Year = 2023 }
                    }
                };
    
                tableToInspect = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                {
                    Headers = { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Date" } },
                    Rows =
                    {
                        new Table.Types.Row { Values = { row1 } },
                        new Table.Types.Row { Values = { row2 } },
                        new Table.Types.Row { Values = { row3 } }
                    }
                };
            }
    
            // Construct the table content item.
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Table = tableToInspect };
    
            // Construct the time part config to deidentify specific value from the date.
            var timePartConfig = new [TimePartConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TimePartConfig.html)
            {
                PartToExtract = [TimePart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TimePartConfig.Types.TimePart.html)Config.Types.[TimePart](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TimePartConfig.Types.TimePart.html).[Year](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.TimePartConfig.Types.TimePart.html#Google_Cloud_Dlp_V2_TimePartConfig_Types_TimePart_Year)
            };
    
            // Construct the deidentify config using time part config created above.
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                RecordTransformations = new [RecordTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformations.html)
                {
                    FieldTransformations =
                    {
                        new [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.html)
                        {
                            PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                            {
                                TimePartConfig = timePartConfig
                            }
                        }
                    }
                }
            };
    
            // Construct the request.
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                DeidentifyConfig = deidentifyConfig,
                Item = contentItem
            };
    
            // Call the API.
            var response = dlp.DeidentifyContent(request);
    
            // Inspect the response.
            Console.Write(response.Item.[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html));
    
            return response.Item.[Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html);
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
    
    // deIdentifyTimeExtract De-identifies a table by extracting specific parts
    // of the time (year in this case) from designated fields.
    func deIdentifyTimeExtract(w io.Writer, projectID string) error {
    
    	row1 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "Ann"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "01/01/1970"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "4532908762519852"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "07/21/1996"}},
    		},
    	}
    
    	row2 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "James"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "03/06/1988"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "4301261899725540"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "04/09/2001"}},
    		},
    	}
    
    	// Specify the table to de-identify.
    	tableToDeidentify := &dlppb.Table{
    		Headers: []*dlppb.FieldId{
    			{Name: "Name"},
    			{Name: "Birth Date"},
    			{Name: "Credit Card"},
    			{Name: "Register Date"},
    		},
    		Rows: []*dlppb.Table_Row{
    			{Values: row1.Values},
    			{Values: row2.Values},
    		},
    	}
    
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
    
    	// Specify what content you want the service to de-identify.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Table{
    			Table: tableToDeidentify,
    		},
    	}
    
    	// Specify the time part to extract.
    	timePartConfig := &dlppb.PrimitiveTransformation_TimePartConfig{
    		TimePartConfig: &dlppb.TimePartConfig{
    			PartToExtract: dlppb.[TimePartConfig_YEAR](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_TimePartConfig_TIME_PART_UNSPECIFIED_TimePartConfig_YEAR_TimePartConfig_MONTH_TimePartConfig_DAY_OF_MONTH_TimePartConfig_DAY_OF_WEEK_TimePartConfig_WEEK_OF_YEAR_TimePartConfig_HOUR_OF_DAY),
    		},
    	}
    
    	transformation := &dlppb.PrimitiveTransformation{
    		Transformation: timePartConfig,
    	}
    
    	// Specify which fields the TimePart should apply too.
    	dateFields := []*dlppb.FieldId{
    		{Name: "Birth Date"},
    		{Name: "Register Date"},
    	}
    
    	fieldTransformation := &dlppb.FieldTransformation{
    		Fields: dateFields,
    		Transformation: &dlppb.FieldTransformation_PrimitiveTransformation{
    			PrimitiveTransformation: transformation,
    		},
    	}
    
    	recordTransformations := []*dlppb.RecordTransformations{
    		{
    			FieldTransformations: []*dlppb.FieldTransformation{
    				fieldTransformation,
    			},
    		},
    	}
    
    	// Specify the config for the de-identify request.
    	deidentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: &dlppb.DeidentifyConfig_RecordTransformations{
    			RecordTransformations: recordTransformations[0],
    		},
    	}
    
    	// Construct the de-identification request to be sent by the client.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: deidentifyConfig,
    		Item:             contentItem,
    	}
    
    	// Send the request.
    	resp, err := client.DeidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the results.
    	fmt.Fprintf(w, "Table after de-identification : %v", resp.GetItem().GetTable())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[TimePartConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TimePartConfig.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    
    public class DeIdentifyWithTimeExtraction {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify =
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder()
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Name").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Birth Date").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Credit Card").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Register Date").build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Alex").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("01/01/1970").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("4532908762519852").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("07/21/1996").build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Charlie").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("03/06/1988").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("4301261899725540").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("04/09/2001").build())
                        .build())
                .build();
        deIdentifyWithTimeExtraction(projectId, tableToDeIdentify);
      }
    
      // De-identifies a table by extracting specific parts of the time (year in this case) from
      // designated fields.
      public static [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) deIdentifyWithTimeExtraction(String projectId, [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to de-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(tableToDeIdentify).build();
    
          // Specify the time part to extract.
          [TimePartConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TimePartConfig.html) timePartConfig =
              [TimePartConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TimePartConfig.html).newBuilder().[setPartToExtract](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TimePartConfig.Builder.html#com_google_privacy_dlp_v2_TimePartConfig_Builder_setPartToExtract_com_google_privacy_dlp_v2_TimePartConfig_TimePart_)([TimePartConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.TimePartConfig.html).TimePart.YEAR).build();
    
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) transformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder().[setTimePartConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setTimePartConfig_com_google_privacy_dlp_v2_TimePartConfig_)(timePartConfig).build();
    
          // Specify which fields the TimePart should apply too.
          List<FieldId> dateFields =
              Arrays.asList(
                  [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Birth Date").build(),
                  [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Register Date").build());
    
          [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html) fieldTransformation =
              [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html).newBuilder()
                  .[addAllFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.Builder.html#com_google_privacy_dlp_v2_FieldTransformation_Builder_addAllFields_java_lang_Iterable___extends_com_google_privacy_dlp_v2_FieldId__)(dateFields)
                  .setPrimitiveTransformation(transformation)
                  .build();
    
          [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html) recordTransformations =
              [RecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.RecordTransformations.html).newBuilder().addFieldTransformations(fieldTransformation).build();
    
          // Construct the configuration for the de-id request and list all desired transformations.
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder().[setRecordTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.Builder.html#com_google_privacy_dlp_v2_DeidentifyConfig_Builder_setRecordTransformations_com_google_privacy_dlp_v2_RecordTransformations_)(recordTransformations).build();
    
          // Combine configurations into a request for the service.
          [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html) request =
              [DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setDeidentifyConfig(deidentifyConfig)
                  .build();
    
          // Send the request and receive response from the service.
          [DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html) response = dlp.deidentifyContent(request);
          System.out.println("Table after de-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getTable());
          return response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getTable();
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
    // const projectId = 'my-project';
    
    // The string to de-identify
    // const string = 'My BirthDay is on 9/21/1976';
    
    // Table to de-identify
    const tablularData = {
      headers: [
        {name: 'Name'},
        {name: 'Birth Date'},
        {name: 'Credit Card'},
        {name: 'Register Date'},
      ],
      rows: [
        {
          values: [
            {stringValue: 'Ann'},
            {stringValue: '01/01/1970'},
            {stringValue: '4532908762519852'},
            {stringValue: '07/21/1996'},
          ],
        },
        {
          values: [
            {stringValue: 'James'},
            {stringValue: '03/06/1988'},
            {stringValue: '4301261899725540'},
            {stringValue: '04/09/2001'},
          ],
        },
      ],
    };
    
    async function deidentifyWithTimeExtraction() {
      // Specify transformation to extract a portion of date.
      const primitiveTransformation = {
        timePartConfig: {
          partToExtract: '[YEAR](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.timepartconfig.timepart.html)',
        },
      };
    
      // Specify which fields the TimePart should apply too
      const dateFields = [{name: 'Birth Date'}, {name: 'Register Date'}];
    
      // Construct de-identification request to be sent by client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: {
          recordTransformations: {
            fieldTransformations: [
              {
                fields: dateFields,
                primitiveTransformation,
              },
            ],
          },
        },
        item: {
          table: tablularData,
        },
      };
    
      // Use the client to send the API request.
      const [response] = await dlp.deidentifyContent(request);
    
      // Print results.
      console.log(
        `Table after de-identification: ${JSON.stringify(response.item.table)}`
      );
    }
    
    deidentifyWithTimeExtraction();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\FieldTransformation;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\RecordTransformations;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\TimePartConfig;
    use Google\Cloud\Dlp\V2\TimePartConfig\TimePart;
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * De-identify data using time extraction.
     * Performing time extraction object preserves a portion of a matched value that on a date, a time,
     * or a timestamp preserves a portion of a matched value. You specify to Cloud DLP what kind of
     * time value you want to extract, including year, month, day of the month, and so on.
     *
     * https://cloud.google.com/dlp/docs/concepts-bucketing#bucketing_scenario_1
     *
     * @param string $callingProjectId      The Google Cloud project id to use as a parent resource.
     * @param string $inputCsvFile          The input file(csv) path to deidentify.
     * @param string $outputCsvFile         The oupt file path to save deidentify content.
     *
     */
    function deidentify_time_extract(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $inputCsvFile = './test/data/table3.csv',
        string $outputCsvFile = './test/data/deidentify_time_extract_output.csv'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Read a CSV file.
        $csvLines = file($inputCsvFile, FILE_IGNORE_NEW_LINES);
        $csvHeaders = explode(',', $csvLines[0]);
        $csvRows = array_slice($csvLines, 1);
    
        // Convert CSV file into protobuf objects.
        $tableHeaders = array_map(function ($csvHeader) {
            return (new FieldId)
                ->setName($csvHeader);
        }, $csvHeaders);
    
        $tableRows = array_map(function ($csvRow) {
            $rowValues = array_map(function ($csvValue) {
                return (new Value())
                    ->setStringValue($csvValue);
            }, explode(',', $csvRow));
            return (new Row())
                ->setValues($rowValues);
        }, $csvRows);
    
        // Construct the table object.
        $tableToDeIdentify = (new Table())
            ->setHeaders($tableHeaders)
            ->setRows($tableRows);
    
        // Specify what content you want the service to de-identify.
        $contentItem = (new ContentItem())
            ->setTable($tableToDeIdentify);
    
        // Specify the time part to extract.
        $timePartConfig = (new TimePartConfig())
            ->setPartToExtract(TimePart::YEAR);
    
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setTimePartConfig($timePartConfig);
    
        // Specify which fields the TimePart should apply too.
        $fieldIds = [
            (new FieldId())
                ->setName('Birth_Date'),
            (new FieldId())
                ->setName('Register_Date')
        ];
    
        $fieldTransformation = (new FieldTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setFields($fieldIds);
    
        $recordTransformations = (new RecordTransformations())
            ->setFieldTransformations([$fieldTransformation]);
    
        // Construct the configuration for the de-id request and list all desired transformations.
        $deidentifyConfig = (new DeidentifyConfig())
            ->setRecordTransformations($recordTransformations);
    
        $parent = "projects/$callingProjectId/locations/global";
    
        // Send the request and receive response from the service.
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setItem($contentItem);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print the results.
        $csvRef = fopen($outputCsvFile, 'w');
        fputcsv($csvRef, $csvHeaders);
        foreach ($response->getItem()->getTable()->getRows() as $tableRow) {
            $values = array_map(function ($tableValue) {
                return $tableValue->getStringValue();
            }, iterator_to_array($tableRow->getValues()));
            fputcsv($csvRef, $values);
        };
        printf('Table after deidentify (File Location): %s', $outputCsvFile);
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import csv
    from datetime import datetime
    from typing import List
    
    import google.cloud.dlp
    
    
    def deidentify_with_time_extract(
        project: str,
        date_fields: List[str],
        input_csv_file: str,
        output_csv_file: str,
    ) -> None:
        """Uses the Data Loss Prevention API to deidentify dates in a CSV file through
         time part extraction.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            date_fields: A list of (date) fields in CSV file to de-identify
                through time extraction. Example: ['birth_date', 'register_date'].
                Date values in format: mm/DD/YYYY are considered as part of this
                sample.
            input_csv_file: The path to the CSV file to deidentify. The first row
                of the file must specify column names, and all other rows must
                contain valid values.
            output_csv_file: The output file path to save the time extracted data.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert date field list to Protobuf type.
        def map_fields(field):
            return {"name": field}
    
        if date_fields:
            date_fields = map(map_fields, date_fields)
        else:
            date_fields = []
    
        csv_lines = []
        with open(input_csv_file) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                csv_lines.append(row)
    
        #  Helper function for converting CSV rows to Protobuf types
        def map_headers(header):
            return {"name": header}
    
        def map_data(value):
            try:
                date = datetime.strptime(value, "%m/%d/%Y")
                return {
                    "date_value": {"year": date.year, "month": date.month, "day": date.day}
                }
            except ValueError:
                return {"string_value": value}
    
        def map_rows(row):
            return {"values": map(map_data, row)}
    
        # Using the helper functions, convert CSV rows to protobuf-compatible
        # dictionaries.
        csv_headers = map(map_headers, csv_lines[0])
        csv_rows = map(map_rows, csv_lines[1:])
    
        # Construct the table dictionary.
        table = {"headers": csv_headers, "rows": csv_rows}
    
        # Construct the `item` for table to de-identify.
        item = {"table": table}
    
        # Construct deidentify configuration dictionary.
        deidentify_config = {
            "record_transformations": {
                "field_transformations": [
                    {
                        "primitive_transformation": {
                            "time_part_config": {"part_to_extract": "YEAR"}
                        },
                        "fields": date_fields,
                    }
                ]
            }
        }
    
        # Write to CSV helper methods.
        def write_header(header):
            return header.name
    
        def write_data(data):
            return data.string_value or "{}/{}/{}".format(
                data.date_value.month,
                data.date_value.day,
                data.date_value.year,
            )
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={
                "parent": parent,
                "deidentify_config": deidentify_config,
                "item": item,
            }
        )
    
        # Print the result.
        print(f"Table after de-identification: {response.item.table}")
    
        # Write results to CSV file.
        with open(output_csv_file, "w") as csvfile:
            write_file = csv.writer(csvfile, delimiter=",")
            write_file.writerow(map(write_header, response.item.table.headers))
            for row in response.item.table.rows:
                write_file.writerow(map(write_data, row.values))
    
        # Print status.
        print(f"Successfully saved date-extracted output to {output_csv_file}")
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
