---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-exception-list/
title: Create an exception list for de-identification \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:15.725277+00:00
---

# Create an exception list for de-identification  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-deidentify-exception-list/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Create an exception list for de-identification Stay organized with collections  Save and categorize content based on your preferences. 

Create an exception list for a regular custom dictionary detector.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Creating a regular custom dictionary detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-dictionary)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
