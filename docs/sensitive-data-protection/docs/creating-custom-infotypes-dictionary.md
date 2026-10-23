---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary/
title: Creating a regular custom dictionary detector \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:05.060041+00:00
---

# Creating a regular custom dictionary detector  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Creating a regular custom dictionary detector Stay organized with collections  Save and categorize content based on your preferences. 

Custom dictionaries provide the simple but powerful ability to match a list of words or phrases. You can use a custom dictionary as a detector or as an exception list for built-in detectors. You can also use custom dictionaries to augment built-in infoType detectors to match additional findings.

This section describes how to create a regular custom dictionary detector from a list of words.

**Note:** If you have a list of anywhere from several hundred to tens of millions of words that you want to scan for, consider using a _large custom dictionary detector_ instead of the regular custom dictionary detector described in this topic. For more information, see [Create a large custom dictionary detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes).

## Anatomy of a dictionary custom infoType detector

As summarized in [API overview](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes#api-overview), to create a dictionary custom infoType detector, you define a [`CustomInfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#CustomInfoType) object that contains the following:

  * The name you want to give the custom infoType detector, within in an [`InfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InfoType) object.
  * An optional [`Likelihood`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood) value. If you omit this field, matches to the dictionary items will return a default likelihood of `VERY_LIKELY`.
  * Optional [`DetectionRule`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#DetectionRule) objects, or hotword rules. These rules adjust the likelihood of findings within a given proximity of specified hotwords. Learn more about hotword rules in [Customizing match likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood).
  * An optional [`SensitivityScore`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#CustomInfoType.FIELDS.sensitivity_score) value. If you omit this field, matches to the dictionary items will return a default sensitivity level of `HIGH`.

Sensitivity scores are used in [data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles). When profiling your data, Sensitive Data Protection uses the sensitivity scores of the infoTypes to [calculate the sensitivity level](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation).

  * A [`Dictionary`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Dictionary), as either a [`WordList`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Dictionary#wordlist) containing a list of words to scan for or a [`CloudStoragePath`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/CloudStoragePath) to a single text file containing a newline-delimited list of words to scan for.




As a JSON object, a dictionary custom infoType detector that includes all optional components looks like the following. This JSON includes a path to a dictionary text file stored in Cloud Storage. To see an inline word list, see the Examples section, later in this topic.
    
    
    {
      "customInfoTypes":[
        {
          "infoType":{
            "name":"CUSTOM_INFOTYPE_NAME"
          },
          "likelihood":"LIKELIHOOD_LEVEL",
          "detectionRules":[
            {
              "hotwordRule":{
                HOTWORD_RULE
              }
            },
            ...
          ],
          "sensitivityScore":{
              "score": "SENSITIVITY_SCORE"
            },
          "dictionary":
          {
            "cloudStoragePath":
            {
              "path": "gs://PATH_TO_TXT_FILE"
            }
          }
        }
      ],
      ...
    }
    

**Note:** You can also create a regular custom dictionary detector by referencing an existing [`StoredInfoType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.storedInfoTypes) in the [`storedType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#CustomInfoType.FIELDS.stored_type) field of the `CustomInfoType` object, instead of defining the [`dictionary`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#CustomInfoType.FIELDS.dictionary) field. However, this approach requires you to first create a `StoredInfoType` of type `Dictionary`. In most cases, it's simpler to define the `Dictionary` object directly in the `dictionary` field of the `CustomInfoType` object.

## Dictionary matching specifics

Following is guidance about how Sensitive Data Protection matches dictionary words and phrases. These points apply to both regular and large custom dictionaries:

  * Dictionary words are case-insensitive. If your dictionary includes `Abby`, it will match on `abby`, `ABBY`, `Abby`, and so on.
  * All characters—in dictionaries or in content to be scanned—other than letters, digits, and other alphabetic characters contained within the Unicode [Basic Multilingual Plane](https://en.wikipedia.org/wiki/Plane_%28Unicode%29#Basic_Multilingual_Plane) are considered as whitespace when scanning for matches. If your dictionary scans for `Abby Abernathy`, it will match on `abby abernathy`, `Abby, Abernathy`, `Abby (ABERNATHY)`, and so on.
  * The characters surrounding any match must be of a different type (letters or digits) than the adjacent characters within the word. If your dictionary scans for `Abi`, it will match the first three characters of `Abi904`, but not of `Abigail`.
  * Dictionary words containing characters in the [Supplementary Multilingual Plane](https://en.wikipedia.org/wiki/Plane_%28Unicode%29#Supplementary_Multilingual_Plane) of the Unicode standard can yield unexpected findings. Examples of such characters are emojis, scientific symbols, and historical scripts. 



Letters, digits, and other alphabetic characters are defined as follows:

  * Letters: characters with general categories `Lu`, `Ll`, `Lt`, `Lm`, or `Lo` in the Unicode specification
  * Digits: characters with general category `Nd` in the Unicode specification
  * Other alphabetic characters: characters with general category `Nl` in the Unicode specification or with contributory property `Other_Alphabetic` as defined by the Unicode Standard



## Examples

### Simple word list

Suppose you have data that includes what hospital room a patient was treated in during a visit. These locations may be considered sensitive in a particular data set, but they are not something that would be picked up by Sensitive Data Protection's built-in detectors.

The rooms were listed as:

  * "RM-Orange"
  * "RM-Yellow"
  * "RM-Green"



### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyWithSimpleWordList
    {
        public static DeidentifyContentResponse Deidentify(string projectId, string text)
        {
            // Instantiate a client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text };
    
            var wordList = new CustomInfoType.Types.Dictionary.Types.WordList
            {
                Words = { new string[] { "RM-GREEN", "RM-YELLOW", "RM-ORANGE" } }
            };
    
            var infoType = new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)
            {
                Name = "CUSTOM_ROOM_ID"
            };
    
            var customInfoType = new [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html)
            {
                InfoType = infoType,
                Dictionary = new CustomInfoType.Types.Dictionary
                {
                    WordList = wordList
                }
            };
    
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                CustomInfoTypes =
                {
                    customInfoType,
                }
            };
            var primitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
            {
                ReplaceWithInfoTypeConfig = new [ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReplaceWithInfoTypeConfig.html) { }
            };
    
            var transformation = new InfoTypeTransformations.Types.InfoTypeTransformation
            {
                InfoTypes = { infoType },
                PrimitiveTransformation = primitiveTransformation
            };
    
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations = { transformation }
                }
            };
    
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                InspectConfig = inspectConfig,
                DeidentifyConfig = deidentifyConfig,
                Item = contentItem
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
    
    // deidentifyWithWordList matches against a custom simple word list to de-identify sensitive
    // data based on the input
    func deidentifyWithWordList(w io.Writer, projectID, input string, infoTypeName string, wordList []string) error {
    	// projectID := "my-project-id"
    	// input := "Patient was seen in RM-YELLOW then transferred to rm green."
    	// wordList := []string{"RM-GREEN", "RM-YELLOW", "RM-ORANGE"}
    
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
    
    	// Specify what content you want the service to DeIdentify.
    	item := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{
    			Value: input,
    		},
    	}
    
    	// Specify the word list custom info type the inspection will look for.
    	infoType := &dlppb.InfoType{
    		Name: infoTypeName,
    	}
    
    	var customInfoType = &dlppb.CustomInfoType{
    		InfoType: infoType,
    		Type: &dlppb.CustomInfoType_Dictionary_{
    			Dictionary: &dlppb.CustomInfoType_Dictionary{
    				Source: &dlppb.CustomInfoType_Dictionary_WordList_{
    					// Construct the word list to be detected
    					WordList: &dlppb.CustomInfoType_Dictionary_WordList{
    						Words: wordList,
    					},
    				},
    			},
    		},
    	}
    
    	// Define type of de-identification as replacement.
    	primitiveTransformation := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_ReplaceWithInfoTypeConfig{
    			ReplaceWithInfoTypeConfig: &dlppb.ReplaceWithInfoTypeConfig{},
    		},
    	}
    
    	infoTypeTransformation := &dlppb.InfoTypeTransformations_InfoTypeTransformation{
    		InfoTypes:               []*dlppb.InfoType{infoType},
    		PrimitiveTransformation: primitiveTransformation,
    	}
    
    	infoTypeTransformations := &dlppb.InfoTypeTransformations{
    		// Associate de-identification type with info type.
    		Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    			infoTypeTransformation,
    		},
    	}
    
    	// Create a configured request.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		InspectConfig: &dlppb.InspectConfig{
    			CustomInfoTypes: []*dlppb.CustomInfoType{
    				customInfoType,
    			},
    		},
    		// Construct the configuration for the de-identify request and list all desired transformations.
    		DeidentifyConfig: &dlppb.DeidentifyConfig{
    			Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    				InfoTypeTransformations: infoTypeTransformations,
    			},
    		},
    		// The item to analyze.
    		Item: item,
    	}
    
    	// Send the request.
    	resp, err := client.DeidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result.
    	fmt.Fprintf(w, "output : %v", resp.GetItem().GetValue())
    	return nil
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).[WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceWithInfoTypeConfig.html);
    import java.io.IOException;
    
    public class DeIdentifyWithSimpleWordList {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToDeIdentify = "Patient was seen in RM-YELLOW then transferred to rm green.";
        deidentifyWithSimpleWordList(projectId, textToDeIdentify);
      }
    
      public static void deidentifyWithSimpleWordList(String projectId, String textToDeIdentify)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Specify what content you want the service to DeIdentify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToDeIdentify).build();
    
          // Construct the word list to be detected
          [Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html) wordList =
              [Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).newBuilder()
                  .setWordList(
                      [WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html).newBuilder()
                          .[addWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Dictionary_WordList_Builder_addWords_java_lang_String_)("RM-GREEN")
                          .[addWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Dictionary_WordList_Builder_addWords_java_lang_String_)("RM-YELLOW")
                          .[addWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Dictionary_WordList_Builder_addWords_java_lang_String_)("RM-ORANGE")
                          .build())
                  .build();
    
          // Specify the word list custom info type the inspection will look for.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("CUSTOM_ROOM_ID").build();
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder().setInfoType(infoType).setDictionary(wordList).build();
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder().[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType).build();
    
          // Define type of deidentification as replacement.
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setReplaceWithInfoTypeConfig_com_google_privacy_dlp_v2_ReplaceWithInfoTypeConfig_)([ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceWithInfoTypeConfig.html).getDefaultInstance())
                  .build();
    
          // Associate deidentification type with info type.
          [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) transformation =
              [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html).newBuilder()
                  .addInfoTypes(infoType)
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
    
          // Construct the configuration for the Redact request and list all desired transformations.
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder()
                  .setInfoTypeTransformations(
                      [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(transformation))
                  .build();
    
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
              "Text after replace with infotype config: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getValue());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // TODO(developer): Replace these variables before running the sample.
    // const projectId = "your-project-id";
    
    // The string to de-identify
    // const textToInspect = 'Patient was seen in RM-YELLOW then transferred to rm green.';
    
    // Words to look for during inspection
    // const words = ['RM-GREEN', 'RM-YELLOW', 'RM-ORANGE'];
    
    // Name of the custom info type
    // const customInfoTypeName = 'CUSTOM_ROOM_ID';
    
    async function deIdentifyWithSimpleWordList() {
      // Initialize client that will be used to send requests. This client only needs to be created
      // once, and can be reused for multiple requests. After completing all of your requests, call
      // the "close" method on the client to safely clean up any remaining background resources.
      const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
      // Construct the word list to be detected
      const wordList = {
        words: words,
      };
    
      // Specify the word list custom info type the inspection will look for.
      const infoType = {
        name: customInfoTypeName,
      };
      const customInfoType = {
        infoType,
        dictionary: {
          wordList,
        },
      };
    
      // Construct de-identify configuration
      const deidentifyConfig = {
        infoTypeTransformations: {
          transformations: [
            {
              primitiveTransformation: {
                replaceWithInfoTypeConfig: {},
              },
            },
          ],
        },
      };
    
      // Construct inspect configuration
      const inspectConfig = {
        customInfoTypes: [customInfoType],
      };
    
      // Construct Item
      const item = {
        value: textToInspect,
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
      console.log(
        `Text after replace with infotype config: ${response.item.value}`
      );
    }
    
    deIdentifyWithSimpleWordList();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary\WordList;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\ReplaceWithInfoTypeConfig;
    
    /**
     * De-identify sensitive data with a simple word list
     * Matches against a custom simple word list to de-identify sensitive data.
     *
     * @param string $callingProjectId  The Google Cloud project id to use as a parent resource.
     * @param string $string            The string to deidentify (will be treated as text).
     */
    
    function deidentify_simple_word_list(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $string = 'Patient was seen in RM-YELLOW then transferred to rm green.'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$callingProjectId/locations/global";
    
        $content = (new ContentItem())
            ->setValue($string);
    
        // Construct the word list to be detected
        $wordList = (new Dictionary())
            ->setWordList((new WordList())
                ->setWords(['RM-GREEN', 'RM-YELLOW', 'RM-ORANGE']));
    
        // The infoTypes of information to mask
        $custoMRoomIdinfoType = (new InfoType())
            ->setName('CUSTOM_ROOM_ID');
        $customInfoType = (new CustomInfoType())
            ->setInfoType($custoMRoomIdinfoType)
            ->setDictionary($wordList);
    
        // Create the configuration object
        $inspectConfig = (new InspectConfig())
            ->setCustomInfoTypes([$customInfoType]);
    
        // Create the information transform configuration objects
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setReplaceWithInfoTypeConfig(new ReplaceWithInfoTypeConfig());
    
        $infoTypeTransformation = (new InfoTypeTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setInfoTypes([$custoMRoomIdinfoType]);
    
        $infoTypeTransformations = (new InfoTypeTransformations())
            ->setTransformations([$infoTypeTransformation]);
    
        // Create the deidentification configuration object
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
        printf('Deidentified content: %s', $response->getItem()->getValue());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.dlp
    
    
    def deidentify_with_simple_word_list(
        project: str,
        input_str: str,
        custom_info_type_name: str,
        word_list: list[str],
    ) -> None:
        """Uses the Data Loss Prevention API to de-identify sensitive data in a
          string by matching against custom word list.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to deidentify (will be treated as text).
            custom_info_type_name: The name of the custom info type to use.
            word_list: The list of strings to match against.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Prepare custom_info_types by parsing word lists
        word_list = {"words": word_list}
        custom_info_types = [
            {
                "info_type": {"name": custom_info_type_name},
                "dictionary": {"word_list": word_list},
            }
        ]
    
        # Construct the configuration dictionary
        inspect_config = {
            "custom_info_types": custom_info_types,
        }
    
        # Construct deidentify configuration dictionary
        deidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {"primitive_transformation": {"replace_with_info_type_config": {}}}
                ]
            }
        }
    
        # Construct the `item`.
        item = {"value": input_str}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={
                "parent": parent,
                "deidentify_config": deidentify_config,
                "inspect_config": inspect_config,
                "item": item,
            }
        )
    
        print(f"De-identified Content: {response.item.value}")
    
    

### REST

The following example JSON defines a custom dictionary that you could use to de-identify custom room numbers.

**JSON input:**
    
    
    POST https://dlp.googleapis.com/v2/projects/[PROJECT_ID]/content:deidentify?key={YOUR_API_KEY}
    
    {
      "item":{
        "value":"Patient was seen in RM-YELLOW then transferred to rm green."
      },
      "deidentifyConfig":{
        "infoTypeTransformations":{
          "transformations":[
            {
              "primitiveTransformation":{
                "replaceWithInfoTypeConfig":{
    
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
              "name":"CUSTOM_ROOM_ID"
            },
            "dictionary":{
              "wordList":{
                "words":[
                  "RM-GREEN",
                  "RM-YELLOW",
                  "RM-ORANGE"
                ]
              }
            }
          }
        ]
      }
    }
    

**JSON output:**

When we POST the JSON input to [`content:deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify), it returns the following JSON response:
    
    
    {
      "item":{
        "value":"Patient was seen in [CUSTOM_ROOM_ID] then transferred to [CUSTOM_ROOM_ID]."
      },
      "overview":{
        "transformedBytes":"17",
        "transformationSummaries":[
          {
            "infoType":{
              "name":"CUSTOM_ROOM_ID"
            },
            "transformation":{
              "replaceWithInfoTypeConfig":{
    
              }
            },
            "results":[
              {
                "count":"2",
                "code":"SUCCESS"
              }
            ],
            "transformedBytes":"17"
          }
        ]
      }
    }
    

Sensitive Data Protection has correctly identified the room numbers specified in the custom dictionary's [`WordList`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#WordList) message. Note that items are even matched when the case and the hyphen (`-`) are missing, as in the second example, "rm green."

### Exception list

Suppose you have log data that includes customer identifiers such as email addresses, and you want to redact this information. However, these logs also include the email addresses of internal developers, and you don't want to redact those.

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyWithExceptionList
    {
        public static DeidentifyContentResponse Deidentify(string projectId, string text)
        {
            // Instantiate a client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Value = text };
    
            var wordList = new CustomInfoType.Types.Dictionary.Types.WordList
            {
                Words = { new string[] { "jack@example.org", "jill@example.org" } }
            };
    
            var exclusionRule = new [ExclusionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExclusionRule.html)
            {
                MatchingType = [MatchingType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html).[FullMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html#Google_Cloud_Dlp_V2_MatchingType_FullMatch),
                Dictionary = new CustomInfoType.Types.Dictionary
                {
                    WordList = wordList
                }
            };
    
            var infoType = new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" };
    
            var inspectionRuleSet = new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)
            {
                InfoTypes = { infoType },
                Rules = { new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { ExclusionRule = exclusionRule } }
            };
    
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infoType },
                RuleSet = { inspectionRuleSet }
            };
            var primitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
            {
                ReplaceWithInfoTypeConfig = new [ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ReplaceWithInfoTypeConfig.html) { }
            };
    
            var transformation = new InfoTypeTransformations.Types.InfoTypeTransformation
            {
                InfoTypes = { infoType },
                PrimitiveTransformation = primitiveTransformation
            };
    
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                InfoTypeTransformations = new [InfoTypeTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoTypeTransformations.html)
                {
                    Transformations = { transformation }
                }
            };
    
            var request = new [DeidentifyContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                InspectConfig = inspectConfig,
                DeidentifyConfig = deidentifyConfig,
                Item = contentItem
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
    
    // deidentifyExceptionList creates an exception list for a regular custom dictionary detector.
    func deidentifyExceptionList(w io.Writer, projectID, input string) error {
    	// projectID := "my-project-id"
    	// input := "jack@example.org accessed customer record of user5@example.com"
    
    	ctx := context.Background()
    
    	// Initialize a client once and reuse it to send multiple requests. Clients
    	// are safe to use across goroutines. When the client is no longer needed,
    	// call the Close method to cleanup its resources.
    	client, err := dlp.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("dlp.NewClient: %w", err)
    	}
    
    	// Closing the client safely cleans up background resousrces.
    	defer client.[Close](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2.html#cloud_google_com_go_dlp_apiv2_Client_Close)()
    
    	// Specify what content you want the service to DeIdentify.
    	item := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_Value{
    			Value: input,
    		},
    	}
    
    	// Specify the word list custom info type and build-in info type the inspection will look for.
    	infoTypes := []*dlppb.InfoType{
    		{Name: "EMAIL_ADDRESS"},
    	}
    
    	dictionary := &dlppb.CustomInfoType_Dictionary{
    		Source: &dlppb.CustomInfoType_Dictionary_WordList_{
    			WordList: &dlppb.CustomInfoType_Dictionary_WordList{
    				Words: []string{"jack@example.org", "jill@example.org"},
    			},
    		},
    	}
    
    	exclusionRule := &dlppb.ExclusionRule{
    		MatchingType: dlppb.[MatchingType_MATCHING_TYPE_FULL_MATCH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_MatchingType_MATCHING_TYPE_UNSPECIFIED_MatchingType_MATCHING_TYPE_FULL_MATCH_MatchingType_MATCHING_TYPE_PARTIAL_MATCH_MatchingType_MATCHING_TYPE_INVERSE_MATCH_MatchingType_MATCHING_TYPE_RULE_SPECIFIC),
    		Type: &dlppb.ExclusionRule_Dictionary{
    			Dictionary: dictionary,
    		},
    	}
    
    	inspectRuleSet := &dlppb.InspectionRuleSet{
    		InfoTypes: infoTypes,
    		Rules: []*dlppb.InspectionRule{
    			{
    				Type: &dlppb.InspectionRule_ExclusionRule{
    					ExclusionRule: exclusionRule,
    				},
    			},
    		},
    	}
    
    	// Construct the configuration for the de-id request and list all desired transformations.
    	primitiveTransformation := &dlppb.PrimitiveTransformation{
    		Transformation: &dlppb.PrimitiveTransformation_ReplaceWithInfoTypeConfig{},
    	}
    
    	infoTypeTransformation := &dlppb.InfoTypeTransformations{
    		Transformations: []*dlppb.InfoTypeTransformations_InfoTypeTransformation{
    			{
    				PrimitiveTransformation: primitiveTransformation,
    			},
    		},
    	}
    
    	deIdentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: &dlppb.DeidentifyConfig_InfoTypeTransformations{
    			InfoTypeTransformations: infoTypeTransformation,
    		},
    	}
    
    	// Create a configured request.
    	req := &dlppb.DeidentifyContentRequest{
    		Parent:           fmt.Sprintf("projects/%s/locations/global", projectID),
    		DeidentifyConfig: deIdentifyConfig,
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes:       infoTypes,
    			CustomInfoTypes: []*dlppb.CustomInfoType{},
    			RuleSet:         []*dlppb.InspectionRuleSet{inspectRuleSet},
    		},
    		// The item to analyze.
    		Item: item,
    	}
    
    	// Send the request.
    	resp, err := client.DeidentifyContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Print the result.
    	fmt.Fprintf(w, "output : %v", resp.GetItem().GetValue())
    	return nil
    
    }
    

### Java

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.dlp.v2.[DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html);
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).[WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html);
    import com.google.privacy.dlp.v2.[DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentRequest.html);
    import com.google.privacy.dlp.v2.[DeidentifyContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html);
    import com.google.privacy.dlp.v2.[ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html);
    import com.google.privacy.dlp.v2.[InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).[InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html);
    import com.google.privacy.dlp.v2.[InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html);
    import com.google.privacy.dlp.v2.[PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html);
    import com.google.privacy.dlp.v2.[ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceWithInfoTypeConfig.html);
    import java.io.IOException;
    
    public class DeIdentifyWithExceptionList {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToDeIdentify = "jack@example.org accessed customer record of user5@example.com";
        deIdentifyWithExceptionList(projectId, textToDeIdentify);
      }
    
      public static void deIdentifyWithExceptionList(String projectId, String textToDeIdentify)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
    
          // Specify what content you want the service to DeIdentify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setValue(textToDeIdentify).build();
    
          // Construct the custom word list to be detected.
          [Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html) wordList =
              [Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).newBuilder()
                  .setWordList(
                      [WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html).newBuilder()
                          .[addWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Dictionary_WordList_Builder_addWords_java_lang_String_)("jack@example.org")
                          .[addWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Dictionary_WordList_Builder_addWords_java_lang_String_)("jill@example.org")
                          .build())
                  .build();
    
          // Construct the custom dictionary detector associated with the word list.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) developerEmail = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("DEVELOPER_EMAIL").build();
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder().setInfoType(developerEmail).setDictionary(wordList).build();
    
          [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html) exclusionRule =
              [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html).newBuilder()
                  .setDictionary(wordList)
                  .setMatchingType([MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html).MATCHING_TYPE_FULL_MATCH)
                  .build();
    
          [InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html) inspectionRule =
              [InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder()
                  .[setExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.Builder.html#com_google_privacy_dlp_v2_InspectionRule_Builder_setExclusionRule_com_google_privacy_dlp_v2_ExclusionRule_)(exclusionRule)
                  .build();
    
          // Specify the word list custom info type and build-in info type the inspection will look for.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) emailAddress = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("EMAIL_ADDRESS").build();
    
          [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html) inspectionRuleSet =
              [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html).newBuilder()
                  .addInfoTypes(emailAddress)
                  .addRules(inspectionRule)
                  .build();
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addInfoTypes(emailAddress)
                  .[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType)
                  .[addRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_)(inspectionRuleSet)
                  .build();
    
          // Define type of deidentification as replacement.
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder()
                  .[setReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setReplaceWithInfoTypeConfig_com_google_privacy_dlp_v2_ReplaceWithInfoTypeConfig_)([ReplaceWithInfoTypeConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ReplaceWithInfoTypeConfig.html).getDefaultInstance())
                  .build();
    
          // Associate de-identification type with info type.
          [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html) transformation =
              [InfoTypeTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.InfoTypeTransformation.html).newBuilder()
                  .addInfoTypes(emailAddress)
                  .setPrimitiveTransformation(primitiveTransformation)
                  .build();
    
          // Construct the configuration for the de-id request and list all desired transformations.
          [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html) deidentifyConfig =
              [DeidentifyConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyConfig.html).newBuilder()
                  .setInfoTypeTransformations(
                      [InfoTypeTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.html).newBuilder().[addTransformations](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoTypeTransformations.Builder.html#com_google_privacy_dlp_v2_InfoTypeTransformations_Builder_addTransformations_com_google_privacy_dlp_v2_InfoTypeTransformations_InfoTypeTransformation_)(transformation))
                  .build();
    
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
              "Text after replace with infotype config: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getValue());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Initialize client that will be used to send requests. This client only needs to be created
    // once, and can be reused for multiple requests. After completing all of your requests, call
    // the "close" method on the client to safely clean up any remaining background resources.
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // TODO(developer): Replace these variables before running the sample.
    // const projectId = "your-project-id";
    
    // The string to deidentify
    // const textToInspect = 'jack@example.org accessed customer record of user5@example.com';
    
    // Words to exclude for during inspection
    // const words = ['jack@example.org', 'jill@example.org'];
    
    // The infoTypes of information to match
    // See https://cloud.google.com/dlp/docs/concepts-infotypes for more information
    // about supported infoTypes.
    // const infoTypes = [{ name: 'EMAIL_ADDRESS' }];
    
    async function deIdentifyWithExceptionList() {
      // Construct item to inspect
      const item = {value: textToInspect};
    
      // Construct the custom dictionary detector associated with the word list.
      const wordListDict = {
        wordList: {
          words: words,
        },
      };
    
      // Construct a rule set that will only match if the match text does not
      // contains tokens from the exclusion list.
      const ruleSet = [
        {
          infoTypes: infoTypes,
          rules: [
            {
              exclusionRule: {
                matchingType:
                  DLP.protos.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html)
                    .[MATCHING_TYPE_FULL_MATCH](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html),
                dictionary: wordListDict,
              },
            },
          ],
        },
      ];
    
      // Combine configurations to construct inspect config.
      const inspectConfig = {
        infoTypes: infoTypes,
        ruleSet: ruleSet,
      };
    
      // Define type of de-identification as replacement & associate de-identification type with info type.
      const transformation = {
        infoTypes: [],
        primitiveTransformation: {
          replaceWithInfoTypeConfig: {},
        },
      };
    
      // Construct the configuration for the de-identification request and list all desired transformations.
      const deidentifyConfig = {
        infoTypeTransformations: {
          transformations: [transformation],
        },
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        item: item,
        inspectConfig: inspectConfig,
        deidentifyConfig: deidentifyConfig,
      };
    
      // Send the request and receive response from the service.
      const [response] = await dlp.deidentifyContent(request);
    
      // Print the results
      console.log(
        `Text after replace with infotype config: ${response.item.value}`
      );
    }
    
    deIdentifyWithExceptionList();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary\WordList;
    use Google\Cloud\Dlp\V2\DeidentifyConfig;
    use Google\Cloud\Dlp\V2\DeidentifyContentRequest;
    use Google\Cloud\Dlp\V2\ExclusionRule;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations;
    use Google\Cloud\Dlp\V2\InfoTypeTransformations\InfoTypeTransformation;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectionRule;
    use Google\Cloud\Dlp\V2\InspectionRuleSet;
    use Google\Cloud\Dlp\V2\MatchingType;
    use Google\Cloud\Dlp\V2\PrimitiveTransformation;
    use Google\Cloud\Dlp\V2\ReplaceWithInfoTypeConfig;
    
    /**
     * Create an exception list for de-identification
     * Create an exception list for a regular custom dictionary detector.
     *
     * @param string $callingProjectId  The project ID to run the API call under
     * @param string $textToDeIdentify  The String you want the service to DeIdentify
     */
    function deidentify_exception_list(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $textToDeIdentify = 'jack@example.org accessed customer record of user5@example.com'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Specify what content you want the service to DeIdentify.
        $contentItem = (new ContentItem())
            ->setValue($textToDeIdentify);
    
        // Construct the custom word list to be detected.
        $wordList = (new Dictionary())
            ->setWordList((new WordList())
                ->setWords(['jack@example.org', 'jill@example.org']));
    
        // Specify the exclusion rule and build-in info type the inspection will look for.
        $exclusionRule = (new ExclusionRule())
            ->setMatchingType(MatchingType::MATCHING_TYPE_FULL_MATCH)
            ->setDictionary($wordList);
    
        $emailAddress = (new InfoType())
            ->setName('EMAIL_ADDRESS');
        $inspectionRuleSet = (new InspectionRuleSet())
            ->setInfoTypes([$emailAddress])
            ->setRules([
                (new InspectionRule())
                    ->setExclusionRule($exclusionRule)
            ]);
    
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes([$emailAddress])
            ->setRuleSet([$inspectionRuleSet]);
    
        // Define type of deidentification as replacement.
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setReplaceWithInfoTypeConfig(new ReplaceWithInfoTypeConfig());
    
        // Associate de-identification type with info type.
        $transformation = (new InfoTypeTransformation())
            ->setInfoTypes([$emailAddress])
            ->setPrimitiveTransformation($primitiveTransformation);
    
        // Construct the configuration for the de-id request and list all desired transformations.
        $deidentifyConfig = (new DeidentifyConfig())
            ->setInfoTypeTransformations(
                (new InfoTypeTransformations())
                    ->setTransformations([$transformation])
            );
    
        // Send the request and receive response from the service
        $parent = "projects/$callingProjectId/locations/global";
        $deidentifyContentRequest = (new DeidentifyContentRequest())
            ->setParent($parent)
            ->setDeidentifyConfig($deidentifyConfig)
            ->setInspectConfig($inspectConfig)
            ->setItem($contentItem);
        $response = $dlp->deidentifyContent($deidentifyContentRequest);
    
        // Print the results
        printf('Text after replace with infotype config: %s', $response->getItem()->getValue());
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    import google.cloud.dlp
    
    
    def deidentify_with_exception_list(
        project: str, content_string: str, info_types: List[str], exception_list: List[str]
    ) -> None:
        """Uses the Data Loss Prevention API to de-identify sensitive data in a
          string but ignore matches against custom list.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to deidentify (will be treated as text).
            info_types: A list of strings representing info types to look for.
                A full list of info type categories can be fetched from the API.
            exception_list: The list of strings to ignore matches on.
    
        Returns:
              None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct a list of infoTypes for DLP to locate in `content_string`. See
        # https://cloud.google.com/dlp/docs/concepts-infotypes for more information
        # about supported infoTypes.
    
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Construct a rule set that will only match on info_type
        # if the matched text is not in the exception list.
        rule_set = [
            {
                "info_types": info_types,
                "rules": [
                    {
                        "exclusion_rule": {
                            "dictionary": {"word_list": {"words": exception_list}},
                            "matching_type": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[MatchingType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.MatchingType.html).MATCHING_TYPE_FULL_MATCH,
                        }
                    }
                ],
            }
        ]
    
        # Construct the configuration dictionary
        inspect_config = {
            "info_types": info_types,
            "rule_set": rule_set,
        }
    
        # Construct deidentify configuration dictionary
        deidentify_config = {
            "info_type_transformations": {
                "transformations": [
                    {"primitive_transformation": {"replace_with_info_type_config": {}}}
                ]
            }
        }
    
        # Construct the `item`.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
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

The following JSON example creates a custom dictionary that lists a subset of email addresses within the [`WordList`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#WordList) message (jack@example.org and jill@example.org), and assigns them the custom infoType name `DEVELOPER_EMAIL`. This JSON instructs Sensitive Data Protection to ignore the specified email addresses, while replacing any other email addresses it detects with a string that corresponds to its infoType (in this case, `EMAIL_ADDRESS`):

**JSON input:**
    
    
    POST https://dlp.googleapis.com/v2/projects/[PROJECT_ID]/content:deidentify?key={YOUR_API_KEY}
    
    {
      "item":{
        "value":"jack@example.org accessed customer record of user5@example.com"
      },
      "deidentifyConfig":{
        "infoTypeTransformations":{
          "transformations":[
            {
              "primitiveTransformation":{
                "replaceWithInfoTypeConfig":{
    
                }
              },
              "infoTypes":[
                {
                  "name":"EMAIL_ADDRESS"
                }
              ]
            }
          ]
        }
      },
      "inspectConfig":{
        "customInfoTypes":[
          {
            "infoType":{
              "name":"DEVELOPER_EMAIL"
            },
            "dictionary":{
              "wordList":{
                "words":[
                  "jack@example.org",
                  "jill@example.org"
                ]
              }
            }
          }
        ],
        "infoTypes":[
          {
            "name":"EMAIL_ADDRESS"
          }
        ]
        "ruleSet": [
          {
            "infoTypes": [
              {
                "name": "EMAIL_ADDRESS"
              }
            ],
            "rules": [
              {
                "exclusionRule": {
                  "excludeInfoTypes": {
                    "infoTypes": [
                      {
                        "name": "DEVELOPER_EMAIL"
                      }
                    ]
                  },
                  "matchingType": "MATCHING_TYPE_FULL_MATCH"
                }
              }
            ]
          }
        ]
      }
    }
    

**JSON output:**

When we POST this JSON to [`content:deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify), it returns the following JSON response:
    
    
    {
      "item":{
        "value":"jack@example.org accessed customer record of [EMAIL_ADDRESS]"
      },
      "overview":{
        "transformedBytes":"17",
        "transformationSummaries":[
          {
            "infoType":{
              "name":"EMAIL_ADDRESS"
            },
            "transformation":{
              "replaceWithInfoTypeConfig":{
    
              }
            },
            "results":[
              {
                "count":"1",
                "code":"SUCCESS"
              }
            ],
            "transformedBytes":"17"
          }
        ]
      }
    }
    

The output has correctly identified user1@example.com as matched by the `EMAIL_ADDRESS` infoType detector and jack@example.org as matched by the `DEVELOPER_EMAIL` custom infoType detector. Note that because we chose to only transform `EMAIL_ADDRESS`, jack@example.org was left intact.

### Augment a built-in infotype detector

Consider a scenario in which a built-in infoType detector isn't returning the correct values. For example, you want to return matches on person names, but Sensitive Data Protection's built-in `PERSON_NAME` detector is failing to return matches on some person names that are common in your dataset.

Sensitive Data Protection allows you to augment built-in infoType detectors by including a built-in detector in the declaration for a custom infoType detector, as shown in the following example. This snippet illustrates how to configure Sensitive Data Protection so that the `PERSON_NAME` built-in infoType detector will additionally match the name "Quasimodo:"

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using [Google.Protobuf](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.html);
    using System;
    using System.Linq;
    using static Google.Cloud.Dlp.V2.CustomInfoType.Types;
    
    public class InspectDataUsingAugmentInfoTypes
    {
        public static InspectContentResponse InspectData(
            string projectId,
            string text,
            [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) infoType = null)
        {
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Specify the type of info to be inspected and construct the infotype.
            var infotype = infoType ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" };
    
            // Construct the custom infoTypes with dictionary.
            var customInfoTypes = new [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html)
            {
                InfoType = infotype,
                Dictionary = new Dictionary
                {
                    WordList = new Dictionary.Types.WordList
                    {
                        Words = { new string[] { "quasimodo" } }
                    }
                }
            };
    
            // Construct the inspect config using custom infoTypes.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                CustomInfoTypes = { customInfoTypes },
                IncludeQuote = true,
                InfoTypes = { infotype }
            };
    
            // Construct the request.
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                InspectConfig = inspectConfig,
                Item = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html)
                {
                    ByteItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
                    {
                        Data = [ByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html).[CopyFromUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html#Google_Protobuf_ByteString_CopyFromUtf8_System_String_)(text),
                        Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8)
                    }
                }
            };
    
            // Call the API.
            [InspectContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html) response = dlp.InspectContent(request);
    
            // Parse the response.
            var findings = response.[Result](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html#Google_Cloud_Dlp_V2_InspectContentResponse_Result).Findings;
            Console.WriteLine($"Finding: {findings.Count}");
    
            foreach (var f in findings)
            {
                Console.WriteLine("\tQuote: " + f.Quote);
                Console.WriteLine("\tInfo type: " + f.[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html).Name);
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
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // inspectAugmentInfoTypes performs info type augmentation using Google Cloud DLP.
    // It enhances data inspection by supplementing existing info types with custom-defined ones,
    // expanding the ability to identify sensitive information in different contexts.
    func inspectAugmentInfoTypes(w io.Writer, projectID, textToInspect string, wordList []string) error {
    	// projectID := "your-project-id"
    	// textToInspect := "The patient's name is quasimodo"
    	// wordList := []string{"quasimodo"}
    
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
    			Value: textToInspect,
    		},
    	}
    
    	// Construct the custom word list to be detected.
    	dictionary := &dlppb.CustomInfoType_Dictionary{
    		Source: &dlppb.CustomInfoType_Dictionary_WordList_{
    			WordList: &dlppb.CustomInfoType_Dictionary_WordList{
    				Words: wordList,
    			},
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
    	infoType := &dlppb.InfoType{
    		Name: "PERSON_NAME",
    	}
    
    	// Construct a custom infoType detector by augmenting the PERSON_NAME detector with a word list.
    	customInfoType := &dlppb.CustomInfoType{
    		InfoType: infoType,
    		Type: &dlppb.CustomInfoType_Dictionary_{
    			Dictionary: dictionary,
    		},
    	}
    
    	// Specify the inspect config for data inspection settings in DLP API, enabling rule
    	// specification, custom info types, and actions on sensitive data. Crucial for tailored
    	// data protection and privacy regulation compliance.
    	inspectConfig := &dlppb.InspectConfig{
    		CustomInfoTypes: []*dlppb.CustomInfoType{
    			customInfoType,
    		},
    		IncludeQuote: true,
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.InspectContentRequest{
    		Parent:        fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:          item,
    		InspectConfig: inspectConfig,
    	}
    
    	// Create the request for the job configured above.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Process the results.
    	result := resp.Result
    	fmt.Fprintf(w, "Findings: %d\n", len(result.Findings))
    	for _, f := range result.Findings {
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
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    
    public class InspectStringAugmentInfoType {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // The string to de-identify.
        String textToInspect = "The patient's name is quasimodo";
        // The string to be additionally matched.
        List<String> wordList = Arrays.asList("quasimodo");
        inspectStringAugmentInfoType(projectId, textToInspect, wordList);
      }
    
      // Inspects the text using new custom words added to the dictionary.
      public static void inspectStringAugmentInfoType(
          String projectId, String textToInspect, List<String> wordList) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type and content to be inspected.
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).BytesType.TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(textToInspect))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build();
    
          // Construct the custom word list to be detected.
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html) dictionary =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).Dictionary.newBuilder()
                  .setWordList(
                      [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).Dictionary.WordList.newBuilder().[addAllWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Dictionary_WordList_Builder_addAllWords_java_lang_Iterable_java_lang_String__)(wordList).build())
                  .build();
    
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME").build();
          // Construct a custom infotype detector by augmenting the PERSON_NAME detector with a word
          // list.
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder().setInfoType(infoType).setDictionary(dictionary).build();
    
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) inspectConfig =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(inspectConfig)
                  .build();
    
          // Use the client to send the API request.
          [InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html) response = dlp.inspectContent(request);
    
          // Parse the response and process results
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
    
    
    // Imports the Google Cloud client library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The string to inspect
    // const string = "The patient's name is quasimodo";
    
    // Word list
    // const words = ['quasimodo'];
    
    async function inspectStringAugmentInfoType() {
      // Specify the type and content to be inspected.
      const byteItem = {
        type: 'BYTES',
        data: Buffer.from(string),
      };
      const item = {byteItem: byteItem};
    
      // Construct the custom word list to be detected.
      const dictionary = {
        wordList: {
          words: words,
        },
      };
    
      // Construct a custom infotype detector by augmenting the PERSON_NAME detector with a word list.
      const customInfoType = {
        infoType: {name: 'PERSON_NAME'},
        dictionary: dictionary,
      };
    
      const inspectConfig = {
        customInfoTypes: [customInfoType],
        includeQuote: true,
      };
    
      // Construct the Inspect request to be sent by the client.
      const inspectRequest = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: inspectConfig,
        item: item,
      };
    
      // Use the client to send the API request.
      const [response] = await dlp.inspectContent(inspectRequest);
    
      // Print Findings.
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
    inspectStringAugmentInfoType();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary\WordList;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\Likelihood;
    
    /**
     * Augment a built-in infotype detector.
     * Consider a scenario in which a built-in infoType detector isn’t returning the correct values.
     * For example, you want to return matches on person names, but Cloud DLP's built-in
     * PERSON_NAME detector is failing to return matches on some person names that are common in your dataset.
     * Cloud DLP allows you to augment built-in infoType detectors by including a built-in detector in the
     * declaration for a custom infoType detector, as shown in the following example. This snippet
     * illustrates how to configure Cloud DLP so that the PERSON_NAME built-in infoType detector will
     * additionally match the name “Quasimodo:”.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect     The string to inspect.
     * @param array  $matchWordList     Specify the set of words to match.
     */
    function inspect_augment_infotypes(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $textToInspect = 'Smith and Quasimodo are good cricketer',
        array  $matchWordList = ['quasimodo']
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new ContentItem())
            ->setValue($textToInspect);
    
        // The infoTypes of information to match.
        $personNameInfoType = (new InfoType())
            ->setName('PERSON_NAME');
    
        // Construct the word list to be detected.
        $wordList = (new Dictionary())
            ->setWordList((new WordList())
                ->setWords($matchWordList));
    
        // Construct the custom infotype detector.
        $customInfoType = (new CustomInfoType())
            ->setInfoType($personNameInfoType)
            ->setLikelihood(Likelihood::POSSIBLE)
            ->setDictionary($wordList);
    
        // Construct the configuration for the Inspect request.
        $inspectConfig = (new InspectConfig())
            ->setCustomInfoTypes([$customInfoType])
            ->setIncludeQuote(true);
    
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
                printf('  Quote: %s' . PHP_EOL, $finding->getQuote());
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
    
    
    def inspect_string_augment_infotype(
        project: str,
        input_str: str,
        info_type: str,
        word_list: List[str],
    ) -> None:
        """Uses the Data Loss Prevention API to augment built-in infoType
        detector and inspect the content string with augmented infoType.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            input_str: The string to inspect using augmented infoType
                (will be treated as text).
            info_type: A string representing built-in infoType to augment.
                A full list of infoType categories can be fetched from the API.
            word_list: List of words or phrases to be added to extend the behaviour
                of built-in infoType.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the custom infoTypes dictionary with declaration of a built-in detector.
        custom_info_types = [
            {
                "info_type": {"name": info_type},
                "dictionary": {"word_list": {"words": word_list}},
            }
        ]
    
        # Construct inspect configuration dictionary with the custom info type.
        inspect_config = {
            "custom_info_types": custom_info_types,
            "include_quote": True,
        }
    
        # Construct the `item` to be inspected.
        item = {"value": input_str}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={
                "parent": parent,
                "inspect_config": inspect_config,
                "item": item,
            }
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Quote: {finding.quote}")
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood} \n")
        else:
            print("No findings.")
    
    

### REST
    
    
    ...
      "inspectConfig":{
        "customInfoTypes":[
          {
            "infoType":{
              "name":"PERSON_NAME"
            },
            "dictionary":{
              "wordList":{
                "words":[
                  "quasimodo"
                ]
              }
            }
          }
        ]
      }
    ...
    

## What's next

Learn about [large custom dictionaries](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
