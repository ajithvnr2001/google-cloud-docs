---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules/
title: Modifying infoType detectors to refine scan results \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:46.428459+00:00
---

# Modifying infoType detectors to refine scan results  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Modifying infoType detectors to refine scan results Stay organized with collections  Save and categorize content based on your preferences. 

Sensitive Data Protection's [built-in infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes) are effective at finding common types of sensitive data. [Custom infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes) enable you to fully customize your own sensitive data detector. _Inspection rules_ help refine the scan results that the Sensitive Data Protection returns by modifying the detection mechanism of a given infoType detector.

If you want to exclude or include more values from the results that are returned by a built-in infoType detector, you can create a new custom infoType from scratch and define all the criteria that Sensitive Data Protection should look for. Alternatively, you can refine the findings that Sensitive Data Protection's built-in or custom detectors return according to criteria that you specify. You can do this by adding inspection rules that can help reduce noise, increase precision and recall, or adjust likelihood certainty of scan findings.

This topic discusses how to use the two types of inspection rules to either exclude certain findings or add additional findings, all according to custom criteria that you specify. Presented in this topic are several scenarios in which you might want to alter an existing infoType detector.

**Note:** The methods described in this topic are not intended to speed scans, but they can help lessen noise by reducing the volume of output and the number of findings stored.

The following types of inspection rules are available:

  * _Exclusion rules_, which help exclude false or unwanted findings.
  * _Hotword rules_, which help detect additional findings in text content.
  * _Adjustment rules_, which help adjust the likelihood of findings based on the context in which they appear.



## Target and context infoTypes

This document uses the following terms to refer to infoTypes in a ruleset.

  * _Target infoType_ : an infoType that Sensitive Data Protection excludes or adjusts when the conditions defined in the ruleset are met.
  * _Context infoType_ : an infoType that, if detected, provides context about a target infoType. Sensitive Data Protection uses context infoTypes to determine whether it must exclude or adjust a target infoType.



## Rule ordering and chaining

Sensitive Data Protection applies the rules in the order you specify them in the ruleset. Therefore, the order of your rules can affect the results of the Sensitive Data Protection operation. For an example, see Boost the likelihood of person name in a health document and exclude the health document in this document.

## Exclusion rules

Exclusion rules are useful in situations like the following:

  * You want to exclude duplicate scan matches in results that are caused by overlapping infoType detectors. For example, you're scanning for email addresses and phone numbers, but you are receiving two hits for email addresses with phone numbers in them, such as "206-555-0764@example.org."
  * You're experiencing noise in your scan results. For example, you're seeing the same dummy email address (such as example@example.com") or domain (such as "example.com") returned an inordinate number of times by a scan for legitimate email addresses.
  * You have a list of terms, phrases, or combination of characters that you want to exclude from results.
  * You want to exclude an entire column of data from results.
  * You want to exclude findings that are near a string that matches a regular expression.
  * You want to exclude findings in images based on their spatial relationship with other detected findings in the image.



### Exclusion rules API overview

Sensitive Data Protection defines an exclusion rule in the [`ExclusionRule`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#exclusionrule) object. Within `ExclusionRule` you specify one of the following:

  * A [`Dictionary`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Dictionary) object, which contains a list of strings to exclude from the results.
  * A [`Regex`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex) object, which defines a regular expression pattern. Strings that match the pattern are excluded from the results.
  * An [`ExcludeInfoTypes`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#excludeinfotypes) object, which contains an array of infoType detectors. If a finding is matched by any of the infoType detectors listed here, the finding is excluded from the results.
  * An [`ExcludeByHotword`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#excludebyhotword) object, which contains the following:

    * A regular expression that defines the _hotword_.
    * A _proximity_ value that defines how near the hotword must be to the finding.

If the finding is within the set proximity, that finding is excluded from the results. For tables, this exclusion rule type lets you exclude an entire column of data from the results.

  * An [`ExcludeByImageFindings`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#excludebyimagefindings) object, which contains the following:

    * A list of context infoTypes, which are used to determine whether to exclude a target infoType finding.

    * An [`ImageContainmentType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#imagecontainmenttype) object that specifies the required spatial relationship between the bounding boxes of the target and context findings. If this requirement isn't met, Sensitive Data Protection doesn't exclude the target infoType finding.

Sensitive Data Protection excludes a target infoType finding if the bounding box of a context infoType has the specified relationship with the target infoType finding. When using [`ExcludeByImageFindings`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#excludebyimagefindings), you must set the [`matchingType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#matchingtype) field to `MATCHING_TYPE_RULE_SPECIFIC`.




### Exclusion rule example scenarios

Each of the following JSON snippets illustrates how to configure Sensitive Data Protection for the given scenario.

#### Omit specific email address from EMAIL_ADDRESS detector scan

The following JSON snippet and code in several languages illustrates how to indicate to Sensitive Data Protection using an [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) that it should avoid matching on "example@example.com" in a scan that uses the infoType detector `EMAIL_ADDRESS`:

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class InspectStringWithExclusionDict
    {
        public static InspectContentResponse Inspect(string projectId, string textToInspect, List<String> excludedMatchList)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var byteContentItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
            {
                Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8),
                Data = Google.Protobuf.ByteString.CopyFromUtf8(textToInspect)
            };
    
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { ByteItem = byteContentItem };
    
            var infoTypes = new string[] { "PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER" }.Select(it => new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = it });
    
            var exclusionRule = new [ExclusionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExclusionRule.html)
            {
                MatchingType = [MatchingType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html).[FullMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html#Google_Cloud_Dlp_V2_MatchingType_FullMatch),
                Dictionary = new CustomInfoType.Types.Dictionary
                {
                    WordList = new CustomInfoType.Types.Dictionary.Types.WordList
                    {
                        Words = { excludedMatchList }
                    }
                }
            };
    
            var ruleSet = new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)
            {
                InfoTypes = { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" } },
                Rules = { new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { ExclusionRule = exclusionRule } }
            };
    
            var config = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infoTypes },
                IncludeQuote = true,
                RuleSet = { ruleSet }
            };
    
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                Item = contentItem,
                InspectConfig = config
            };
    
            var response = dlp.InspectContent(request);
    
            Console.WriteLine($"Findings: {response.Result.Findings.Count}");
            foreach (var f in response.Result.Findings)
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
    
    // inspectStringWithExclusionDictionary inspects a string for sensitive data
    // using exclusion dictionary, here the function omits a specific email address
    // from an EMAIL_ADDRESS detector scan with an exclusion dictionary
    func inspectStringWithExclusionDictionary(w io.Writer, projectID, textToInspect string, excludedMatchList []string) error {
    	// projectID := "my-project-id"
    	// textToInspect := "Some email addresses: gary@example.com, example@example.com"
    	// excludedMatchList := []string{"example@example.com"}
    
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
    
    	// Specify the type and content to be inspected.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_ByteItem{
    			ByteItem: &dlppb.ByteContentItem{
    				Type: dlppb.[ByteContentItem_TEXT_UTF8](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL),
    				Data: []byte(textToInspect),
    			},
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
    	infoTypes := []*dlppb.InfoType{
    		{Name: "PHONE_NUMBER"},
    		{Name: "EMAIL_ADDRESS"},
    		{Name: "CREDIT_CARD_NUMBER"},
    	}
    
    	// Exclude matches from the specified excludedMatchList.
    	exclusionRule := &dlppb.ExclusionRule{
    		Type: &dlppb.ExclusionRule_Dictionary{
    			Dictionary: &dlppb.CustomInfoType_Dictionary{
    				Source: &dlppb.CustomInfoType_Dictionary_WordList_{
    					WordList: &dlppb.CustomInfoType_Dictionary_WordList{
    						Words: excludedMatchList,
    					},
    				},
    			},
    		},
    		MatchingType: dlppb.[MatchingType_MATCHING_TYPE_FULL_MATCH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_MatchingType_MATCHING_TYPE_UNSPECIFIED_MatchingType_MATCHING_TYPE_FULL_MATCH_MatchingType_MATCHING_TYPE_PARTIAL_MATCH_MatchingType_MATCHING_TYPE_INVERSE_MATCH_MatchingType_MATCHING_TYPE_RULE_SPECIFIC),
    	}
    
    	// Construct a ruleset that applies the exclusion rule to the EMAIL_ADDRESSES infoType.
    	ruleSet := &dlppb.InspectionRuleSet{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: "EMAIL_ADDRESS"},
    		},
    		Rules: []*dlppb.InspectionRule{
    			{
    				Type: &dlppb.InspectionRule_ExclusionRule{
    					ExclusionRule: exclusionRule,
    				},
    			},
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.InspectContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:   contentItem,
    		// Construct the configuration for the Inspect request, including the ruleSet.
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes:    infoTypes,
    			IncludeQuote: true,
    			RuleSet: []*dlppb.InspectionRuleSet{
    				ruleSet,
    			},
    		},
    	}
    
    	// Send the request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Process the results.
    	fmt.Fprintf(w, "Findings: %v\n", len(resp.Result.Findings))
    	for _, v := range resp.GetResult().Findings {
    		fmt.Fprintf(w, "Quote: %v\n", v.GetQuote())
    		fmt.Fprintf(w, "Infotype Name: %v\n", v.GetInfoType().GetName())
    		fmt.Fprintf(w, "Likelihood: %v\n", v.GetLikelihood())
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
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).[WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html);
    import com.google.privacy.dlp.v2.[ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html);
    import com.google.privacy.dlp.v2.[InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.List;
    
    public class InspectStringWithExclusionDict {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "Some email addresses: gary@example.com, example@example.com";
        List<String> excludedMatchList = Arrays.asList("example@example.com");
        inspectStringWithExclusionDict(projectId, textToInspect, excludedMatchList);
      }
    
      // Inspects the provided text, avoiding matches specified in the exclusion list.
      public static void inspectStringWithExclusionDict(
          String projectId, String textToInspect, List<String> excludedMatchList) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type and content to be inspected.
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(textToInspect))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
          List<InfoType> infoTypes = new ArrayList<>();
          for (String typeName : new String[] {"PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER"}) {
            infoTypes.add([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(typeName).build());
          }
    
          // Exclude matches from the specified excludedMatchList.
          [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html) exclusionRule =
              [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html).newBuilder()
                  .setMatchingType([MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html).MATCHING_TYPE_FULL_MATCH)
                  .setDictionary(
                      [Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).newBuilder()
                          .setWordList([WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html).newBuilder().[addAllWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Dictionary_WordList_Builder_addAllWords_java_lang_Iterable_java_lang_String__)(excludedMatchList)))
                  .build();
    
          // Construct a ruleset that applies the exclusion rule to the EMAIL_ADDRESSES infotype.
          [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html) ruleSet =
              [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html).newBuilder()
                  .addInfoTypes([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("EMAIL_ADDRESS"))
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().[setExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.Builder.html#com_google_privacy_dlp_v2_InspectionRule_Builder_setExclusionRule_com_google_privacy_dlp_v2_ExclusionRule_)(exclusionRule))
                  .build();
    
          // Construct the configuration for the Inspect request, including the ruleset.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .[addRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_)(ruleSet)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(config)
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The string to inspect
    // const string = 'Some email addresses: gary@example.com, example@example.com';
    
    // The infoTypes of information to match
    // const infoTypes = [{ name: 'EMAIL_ADDRESS' }];
    
    // Words to exclude
    // const excludedWords = ['gary@example.com'];
    
    async function inspectStringWithExclusionDict() {
      // Specify the type and content to be inspected.
      const item = {
        byteItem: {
          type: DLP.protos.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem-class.html).[BytesType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html)
            .[TEXT_UTF8](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html),
          data: Buffer.from(string, 'utf-8'),
        },
      };
    
      // Exclude matches from the specified excludedWords.
      const exclusionRule = {
        dictionary: {
          wordList: {
            words: excludedWords,
          },
        },
        matchingType:
          DLP.protos.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html).[MATCHING_TYPE_FULL_MATCH](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html),
      };
    
      // Construct a ruleset that applies the exclusion rule to the specified infotype.
      const ruleSet = [
        {
          infoTypes: infoTypes,
          rules: [
            {
              exclusionRule: exclusionRule,
            },
          ],
        },
      ];
    
      // Construct the configuration for the Inspect request, including the ruleset.
      const inspectConfig = {
        infoTypes: infoTypes,
        ruleSet: ruleSet,
        includeQuote: true,
      };
    
      // Construct the Inspect request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: inspectConfig,
        item: item,
      };
    
      // Use the client to send the API request.
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
    inspectStringWithExclusionDict();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary\WordList;
    use Google\Cloud\Dlp\V2\ExclusionRule;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\InspectionRule;
    use Google\Cloud\Dlp\V2\InspectionRuleSet;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\MatchingType;
    
    /**
     * Inspect a string for sensitive data, using exclusion dictionary
     * Omit a specific email address from an EMAIL_ADDRESS detector scan with an exclusion dictionary.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect     The string to inspect.
     */
    function inspect_string_with_exclusion_dict(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $textToInspect = 'Some email addresses: gary@example.com, example@example.com'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new ContentItem())
            ->setValue($textToInspect);
    
        // Specify the type of info the inspection will look for.
        $infotypes = [
            (new InfoType())->setName('PHONE_NUMBER'),
            (new InfoType())->setName('EMAIL_ADDRESS'),
            (new InfoType())->setName('CREDIT_CARD_NUMBER'),
        ];
    
        // Exclude matches from the specified excludedMatchList.
        $excludedMatchList = (new Dictionary())
            ->setWordList((new WordList())
                ->setWords(['example@example.com']));
        $matchingType = MatchingType::MATCHING_TYPE_FULL_MATCH;
        $exclusionRule = (new ExclusionRule())
            ->setMatchingType($matchingType)
            ->setDictionary($excludedMatchList);
    
        // Construct a ruleset that applies the exclusion rule to the EMAIL_ADDRESSES infotype.
        $emailAddress = (new InfoType())
            ->setName('EMAIL_ADDRESS');
        $inspectionRuleSet = (new InspectionRuleSet())
            ->setInfoTypes([$emailAddress])
            ->setRules([
                (new InspectionRule())
                    ->setExclusionRule($exclusionRule),
            ]);
    
        // Construct the configuration for the Inspect request, including the ruleset.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes($infotypes)
            ->setIncludeQuote(true)
            ->setRuleSet([$inspectionRuleSet]);
    
        // Run request
        $inspectContentRequest = (new InspectContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->inspectContent($inspectContentRequest);
    
        // Print the results
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
    
    
    def inspect_string_with_exclusion_dict(
        project: str,
        content_string: str,
        exclusion_list: List[str] = ["example@example.com"],
    ) -> None:
        """Inspects the provided text, avoiding matches specified in the exclusion list
    
        Uses the Data Loss Prevention API to omit matches on EMAIL_ADDRESS if they are
        in the specified exclusion list.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
            exclusion_list: The list of strings to ignore matches on
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct a list of infoTypes for DLP to locate in `content_string`. See
        # https://cloud.google.com/dlp/docs/concepts-infotypes for more information
        # about supported infoTypes.
        info_types_to_locate = [{"name": "EMAIL_ADDRESS"}]
    
        # Construct a rule set that will only match on EMAIL_ADDRESS
        # if the match text is not in the exclusion list.
        rule_set = [
            {
                "info_types": info_types_to_locate,
                "rules": [
                    {
                        "exclusion_rule": {
                            "dictionary": {"word_list": {"words": exclusion_list}},
                            "matching_type": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[MatchingType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.MatchingType.html).MATCHING_TYPE_FULL_MATCH,
                        }
                    }
                ],
            }
        ]
    
        # Construct the configuration dictionary
        inspect_config = {
            "info_types": info_types_to_locate,
            "rule_set": rule_set,
            "include_quote": True,
        }
    
        # Construct the `item`.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={"parent": parent, "inspect_config": inspect_config, "item": item}
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Quote: {finding.quote}")
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

### REST

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.
    
    
    ...
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"EMAIL_ADDRESS"
            }
          ],
          "ruleSet":[
            {
              "infoTypes":[
                {
                  "name":"EMAIL_ADDRESS"
                }
              ],
              "rules":[
                {
                  "exclusionRule":{
                    "dictionary":{
                      "wordList":{
                        "words":[
                          "example@example.com"
                        ]
                      }
                    },
                    "matchingType": "MATCHING_TYPE_FULL_MATCH"
                  }
                }
              ]
            }
          ]
        }
    ...
    

#### Omit email addresses ending with a specific domain from EMAIL_ADDRESS detector scan

The following JSON snippet and code in several languages illustrates how to indicate to Sensitive Data Protection using an [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) that it should avoid matching on any email addresses that end with "@example.com" in a scan that uses the infoType detector `EMAIL_ADDRESS`:

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class InspectStringWithExclusionRegex
    {
        public static InspectContentResponse Inspect(string projectId, string textToInspect, string excludedRegex)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var byteContentItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
            {
                Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8),
                Data = Google.Protobuf.ByteString.CopyFromUtf8(textToInspect)
            };
    
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { ByteItem = byteContentItem };
    
            var infoTypes = new string[] { "PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER" }.Select(it => new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = it });
    
            var exclusionRule = new [ExclusionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExclusionRule.html)
            {
                MatchingType = [MatchingType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html).[FullMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html#Google_Cloud_Dlp_V2_MatchingType_FullMatch),
                Regex = new CustomInfoType.Types.Regex { Pattern = excludedRegex }
            };
    
            var ruleSet = new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)
            {
                InfoTypes = { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" } },
                Rules = { new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { ExclusionRule = exclusionRule } }
            };
    
            var config = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infoTypes },
                IncludeQuote = true,
                RuleSet = { ruleSet }
            };
    
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                Item = contentItem,
                InspectConfig = config
            };
    
            var response = dlp.InspectContent(request);
    
            Console.WriteLine($"Findings: {response.Result.Findings.Count}");
            foreach (var f in response.Result.Findings)
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
    
    // inspectStringWithExclusionRegex inspects a string excluding REGEX matches
    // in this function specifically the function omits email addresses ending with a specific
    // domain from EMAIL_ADDRESS detector scan.
    func inspectStringWithExclusionRegex(w io.Writer, projectID, textToInspect, excludedRegex string) error {
    	// projectID := "my-project-id"
    	// textToInspect := "Some email addresses: gary@example.com, bob@example.org"
    	// excludedRegex := ".+@example.com"
    
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
    
    	// Specify the type and content to be inspected.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_ByteItem{
    			ByteItem: &dlppb.ByteContentItem{
    				Type: dlppb.[ByteContentItem_TEXT_UTF8](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL),
    				Data: []byte(textToInspect),
    			},
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
    	infoTypes := []*dlppb.InfoType{
    		{Name: "PHONE_NUMBER"},
    		{Name: "EMAIL_ADDRESS"},
    		{Name: "CREDIT_CARD_NUMBER"},
    	}
    
    	// Exclude matches from the specified excludedMatchList.
    	exclusionRule := &dlppb.ExclusionRule{
    		Type: &dlppb.ExclusionRule_Regex{
    			Regex: &dlppb.CustomInfoType_Regex{
    				Pattern: excludedRegex,
    			},
    		},
    		MatchingType: dlppb.[MatchingType_MATCHING_TYPE_FULL_MATCH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_MatchingType_MATCHING_TYPE_UNSPECIFIED_MatchingType_MATCHING_TYPE_FULL_MATCH_MatchingType_MATCHING_TYPE_PARTIAL_MATCH_MatchingType_MATCHING_TYPE_INVERSE_MATCH_MatchingType_MATCHING_TYPE_RULE_SPECIFIC),
    	}
    
    	// Construct a ruleset that applies the exclusion rule to the EMAIL_ADDRESSES infotype.
    	ruleSet := &dlppb.InspectionRuleSet{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: "EMAIL_ADDRESS"},
    		},
    		Rules: []*dlppb.InspectionRule{
    			{
    				Type: &dlppb.InspectionRule_ExclusionRule{
    					ExclusionRule: exclusionRule,
    				},
    			},
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.InspectContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:   contentItem,
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes:    infoTypes,
    			IncludeQuote: true,
    			RuleSet: []*dlppb.InspectionRuleSet{
    				ruleSet,
    			},
    		},
    	}
    
    	// Send the request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Process the results.
    	fmt.Fprintf(w, "Findings: %v\n", len(resp.Result.Findings))
    	for _, v := range resp.GetResult().Findings {
    		fmt.Fprintf(w, "Quote: %v\n", v.GetQuote())
    		fmt.Fprintf(w, "Infotype Name: %v\n", v.GetInfoType().GetName())
    		fmt.Fprintf(w, "Likelihood: %v\n", v.GetLikelihood())
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
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html);
    import com.google.privacy.dlp.v2.[ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html);
    import com.google.privacy.dlp.v2.[InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class InspectStringWithExclusionRegex {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "Some email addresses: gary@example.com, bob@example.org";
        String excludedRegex = ".+@example.com";
        inspectStringWithExclusionRegex(projectId, textToInspect, excludedRegex);
      }
    
      // Inspects the provided text, avoiding matches specified in the exclusion list.
      public static void inspectStringWithExclusionRegex(
          String projectId, String textToInspect, String excludedRegex) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type and content to be inspected.
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(textToInspect))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
          List<InfoType> infoTypes = new ArrayList<>();
          for (String typeName : new String[] {"PHONE_NUMBER", "EMAIL_ADDRESS", "CREDIT_CARD_NUMBER"}) {
            infoTypes.add([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(typeName).build());
          }
    
          // Exclude matches from the specified excludedMatchList.
          [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html) exclusionRule =
              [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html).newBuilder()
                  .setMatchingType([MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html).MATCHING_TYPE_FULL_MATCH)
                  .setRegex([Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html).newBuilder().[setPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)(excludedRegex))
                  .build();
    
          // Construct a ruleset that applies the exclusion rule to the EMAIL_ADDRESSES infotype.
          [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html) ruleSet =
              [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html).newBuilder()
                  .addInfoTypes([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("EMAIL_ADDRESS"))
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().[setExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.Builder.html#com_google_privacy_dlp_v2_InspectionRule_Builder_setExclusionRule_com_google_privacy_dlp_v2_ExclusionRule_)(exclusionRule))
                  .build();
    
          // Construct the configuration for the Inspect request, including the ruleset.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .[addRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_)(ruleSet)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(config)
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The string to inspect
    // const string = 'Some email addresses: gary@example.com, bob@example.org';
    
    // Exclusion Regex
    // const exclusionRegex = '.+@example.com';
    
    async function inspectStringMultipleRules() {
      // Specify the type and content to be inspected.
      const item = {
        byteItem: {
          type: DLP.protos.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem-class.html).[BytesType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html)
            .[TEXT_UTF8](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html),
          data: Buffer.from(string, 'utf-8'),
        },
      };
    
      // Info Types for inspection
      const infoTypes = [{name: 'EMAIL_ADDRESS'}];
    
      // Construct a exclusion rule that uses a regex pattern
      const exclusionRule = {
        regex: {pattern: exclusionRegex},
        matchingType:
          DLP.protos.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html).[MATCHING_TYPE_FULL_MATCH](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html),
      };
    
      // Construct a ruleset that applies the exclusion rule to the EMAIL_ADDRESSES infotype.
      const ruleSet = [
        {
          infoTypes: infoTypes,
          rules: [
            {
              exclusionRule: exclusionRule,
            },
          ],
        },
      ];
    
      // Construct the configuration for the Inspect request, including the ruleset.
      const inspectConfig = {
        infoTypes: infoTypes,
        ruleSet: ruleSet,
        includeQuote: true,
      };
    
      // Construct the Inspect request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: inspectConfig,
        item: item,
      };
    
      // Use the client to send the API request.
      const [response] = await dlp.inspectContent(request);
    
      // Print findings.
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
    inspectStringMultipleRules();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType\Regex;
    use Google\Cloud\Dlp\V2\ExclusionRule;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\InspectionRule;
    use Google\Cloud\Dlp\V2\InspectionRuleSet;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\MatchingType;
    
    /**
     * Inspect a string, excluding REGEX matches
     * Omit email addresses ending with a specific domain from an EMAIL_ADDRESS detector scan.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect     The string to inspect.
     */
    function inspect_string_with_exclusion_regex(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $textToInspect = 'Some email addresses: gary@example.com, bob@example.org'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new ContentItem())
            ->setValue($textToInspect);
    
        // Specify the type of info the inspection will look for.
        $infotypes = [
            (new InfoType())->setName('PHONE_NUMBER'),
            (new InfoType())->setName('EMAIL_ADDRESS'),
            (new InfoType())->setName('CREDIT_CARD_NUMBER'),
        ];
    
        // Exclude matches from the specified excludedRegex.
        $excludedRegex = '.+@example.com';
        $exclusionRule = (new ExclusionRule())
            ->setMatchingType(MatchingType::MATCHING_TYPE_FULL_MATCH)
            ->setRegex((new Regex())
                ->setPattern($excludedRegex));
    
        // Construct a ruleset that applies the exclusion rule to the EMAIL_ADDRESSES infotype.
        $inspectionRuleSet = (new InspectionRuleSet())
            ->setInfoTypes([
                (new InfoType())
                    ->setName('EMAIL_ADDRESS')
            ])
            ->setRules([
                (new InspectionRule())
                    ->setExclusionRule($exclusionRule),
            ]);
    
        // Construct the configuration for the Inspect request, including the ruleset.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes($infotypes)
            ->setIncludeQuote(true)
            ->setRuleSet([$inspectionRuleSet]);
    
        // Run request
        $inspectContentRequest = (new InspectContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->inspectContent($inspectContentRequest);
    
        // Print the results
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
    
    
    import google.cloud.dlp
    
    
    def inspect_string_with_exclusion_regex(
        project: str, content_string: str, exclusion_regex: str = ".+@example.com"
    ) -> None:
        """Inspects the provided text, avoiding matches specified in the exclusion regex
    
        Uses the Data Loss Prevention API to omit matches on EMAIL_ADDRESS if they match
        the specified exclusion regex.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
            exclusion_regex: The regular expression to exclude matches on
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct a list of infoTypes for DLP to locate in `content_string`. See
        # https://cloud.google.com/dlp/docs/concepts-infotypes for more information
        # about supported infoTypes.
        info_types_to_locate = [{"name": "EMAIL_ADDRESS"}]
    
        # Construct a rule set that will only match on EMAIL_ADDRESS
        # if the specified regex doesn't also match.
        rule_set = [
            {
                "info_types": info_types_to_locate,
                "rules": [
                    {
                        "exclusion_rule": {
                            "regex": {"pattern": exclusion_regex},
                            "matching_type": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[MatchingType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.MatchingType.html).MATCHING_TYPE_FULL_MATCH,
                        }
                    }
                ],
            }
        ]
    
        # Construct the configuration dictionary
        inspect_config = {
            "info_types": info_types_to_locate,
            "rule_set": rule_set,
            "include_quote": True,
        }
    
        # Construct the `item`.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={"parent": parent, "inspect_config": inspect_config, "item": item}
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Quote: {finding.quote}")
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

### REST

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.
    
    
    ...
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"EMAIL_ADDRESS"
            }
          ],
          "ruleSet":[
            {
              "infoTypes":[
                {
                  "name":"EMAIL_ADDRESS"
                }
              ],
              "rules":[
                {
                  "exclusionRule":{
                    "regex":{
                      "pattern":".+@example.com"
                    },
                    "matchingType": "MATCHING_TYPE_FULL_MATCH"
                  }
                }
              ]
            }
          ]
        }
    ...
    

#### Omit scan matches that include the substring "TEST"

The following JSON snippet and code in several languages illustrates how to indicate to Sensitive Data Protection using an [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) that it should exclude any findings that include the token "TEST" from the specified list of infoTypes.

Note that this matches on "TEST" as a token, not a substring, so that although something like "TEST@email.com" will match, "TESTER@email.com" will not. If matching on a substring is desired, use a regex in the exclusion rule instead of a dictionary.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class InspectStringWithExclusionDictSubstring
    {
        public static InspectContentResponse Inspect(string projectId, string textToInspect, List<String> excludedSubstringList)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var byteItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
            {
                Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8),
                Data = Google.Protobuf.ByteString.CopyFromUtf8(textToInspect)
            };
    
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { ByteItem = byteItem };
    
            var infoTypes = new string[]
            {
                "EMAIL_ADDRESS",
                "DOMAIN_NAME",
                "PHONE_NUMBER",
                "PERSON_NAME"
            }.Select(it => new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = it });
    
            var exclusionRule = new [ExclusionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExclusionRule.html)
            {
                MatchingType = [MatchingType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html).[PartialMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html#Google_Cloud_Dlp_V2_MatchingType_PartialMatch),
                Dictionary = new CustomInfoType.Types.Dictionary
                {
                    WordList = new CustomInfoType.Types.Dictionary.Types.WordList
                    {
                        Words = { excludedSubstringList }
                    }
                }
            };
    
            var ruleSet = new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)
            {
                InfoTypes = { infoTypes },
                Rules = { new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { ExclusionRule = exclusionRule } }
            };
    
            var config = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infoTypes },
                IncludeQuote = true,
                RuleSet = { ruleSet }
            };
    
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                Item = contentItem,
                InspectConfig = config
            };
    
            var response = dlp.InspectContent(request);
    
            Console.WriteLine($"Findings: {response.Result.Findings.Count}");
            foreach (var f in response.Result.Findings)
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
    
    // inspectStringWithExclusionDictSubstring inspects a string
    // with an exclusion dictionary substring
    func inspectStringWithExclusionDictSubstring(w io.Writer, projectID, textToInspect string, excludedSubString []string) error {
    	// projectID := "my-project-id"
    	// textToInspect := "Some email addresses: gary@example.com, TEST@example.com"
    	// excludedSubString := []string{"TEST"}
    
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
    
    	// Specify the type and content to be inspected.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_ByteItem{
    			ByteItem: &dlppb.ByteContentItem{
    				Type: dlppb.[ByteContentItem_TEXT_UTF8](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL),
    				Data: []byte(textToInspect),
    			},
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
    	infoTypes := []*dlppb.InfoType{
    		{Name: "EMAIL_ADDRESS"},
    		{Name: "DOMAIN_NAME"},
    		{Name: "PHONE_NUMBER"},
    		{Name: "PERSON_NAME"},
    	}
    
    	// Exclude partial matches from the specified excludedSubstringList.
    	exclusionRule := &dlppb.ExclusionRule{
    		Type: &dlppb.ExclusionRule_Dictionary{
    			Dictionary: &dlppb.CustomInfoType_Dictionary{
    				Source: &dlppb.CustomInfoType_Dictionary_WordList_{
    					WordList: &dlppb.CustomInfoType_Dictionary_WordList{
    						Words: excludedSubString,
    					},
    				},
    			},
    		},
    		MatchingType: dlppb.[MatchingType_MATCHING_TYPE_PARTIAL_MATCH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_MatchingType_MATCHING_TYPE_UNSPECIFIED_MatchingType_MATCHING_TYPE_FULL_MATCH_MatchingType_MATCHING_TYPE_PARTIAL_MATCH_MatchingType_MATCHING_TYPE_INVERSE_MATCH_MatchingType_MATCHING_TYPE_RULE_SPECIFIC),
    	}
    
    	// Construct a ruleSet that applies the exclusion rule to the EMAIL_ADDRESSES infoType.
    	ruleSet := &dlppb.InspectionRuleSet{
    		InfoTypes: infoTypes,
    		Rules: []*dlppb.InspectionRule{
    			{
    				Type: &dlppb.InspectionRule_ExclusionRule{
    					ExclusionRule: exclusionRule,
    				},
    			},
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.InspectContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:   contentItem,
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes:    infoTypes,
    			IncludeQuote: true,
    			RuleSet: []*dlppb.InspectionRuleSet{
    				ruleSet,
    			},
    		},
    	}
    
    	// Send the request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Process the results.
    	fmt.Fprintf(w, "Findings: %v\n", len(resp.Result.Findings))
    	for _, v := range resp.GetResult().Findings {
    		fmt.Fprintf(w, "Quote: %v\n", v.GetQuote())
    		fmt.Fprintf(w, "Infotype Name: %v\n", v.GetInfoType().GetName())
    		fmt.Fprintf(w, "Likelihood: %v\n", v.GetLikelihood())
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
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).[WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html);
    import com.google.privacy.dlp.v2.[ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html);
    import com.google.privacy.dlp.v2.[InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.Arrays;
    import java.util.List;
    
    public class InspectStringWithExclusionDictSubstring {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "Some email addresses: gary@example.com, TEST@example.com";
        List<String> excludedSubstringList = Arrays.asList("TEST");
        inspectStringWithExclusionDictSubstring(projectId, textToInspect, excludedSubstringList);
      }
    
      // Inspects the provided text, avoiding matches specified in the exclusion list.
      public static void inspectStringWithExclusionDictSubstring(
          String projectId, String textToInspect, List<String> excludedSubstringList)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type and content to be inspected.
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(textToInspect))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
          List<InfoType> infoTypes = new ArrayList<>();
          for (String typeName :
              new String[] {"EMAIL_ADDRESS", "DOMAIN_NAME", "PHONE_NUMBER", "PERSON_NAME"}) {
            infoTypes.add([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(typeName).build());
          }
    
          // Exclude partial matches from the specified excludedSubstringList.
          [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html) exclusionRule =
              [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html).newBuilder()
                  .setMatchingType([MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html).MATCHING_TYPE_PARTIAL_MATCH)
                  .setDictionary(
                      [Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).newBuilder()
                          .setWordList([WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html).newBuilder().[addAllWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Dictionary_WordList_Builder_addAllWords_java_lang_Iterable_java_lang_String__)(excludedSubstringList)))
                  .build();
    
          // Construct a ruleset that applies the exclusion rule to the EMAIL_ADDRESSES infotype.
          [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html) ruleSet =
              [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().[setExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.Builder.html#com_google_privacy_dlp_v2_InspectionRule_Builder_setExclusionRule_com_google_privacy_dlp_v2_ExclusionRule_)(exclusionRule))
                  .build();
    
          // Construct the configuration for the Inspect request, including the ruleset.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .[addRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_)(ruleSet)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(config)
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The string to inspect
    // const string = 'Some email addresses: gary@example.com, TEST@example.com';
    
    // List of substrings to be used for exclusion
    // const excludedSubstringList = ['Test'];
    
    async function inspectStringExclusionDictSubstr() {
      // Specify the type and content to be inspected.
      const item = {
        byteItem: {
          type: DLP.protos.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem-class.html).[BytesType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html)
            .[TEXT_UTF8](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html),
          data: Buffer.from(string, 'utf-8'),
        },
      };
    
      // Specify the type of info the inspection will look for.
      // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
      const infoTypes = [
        {name: 'EMAIL_ADDRESS'},
        {name: 'DOMAIN_NAME'},
        {name: 'PHONE_NUMBER'},
        {name: 'PERSON_NAME'},
      ];
    
      // Exclude partial matches from the specified excludedSubstringList.
      const exclusionRule = {
        dictionary: {wordList: {words: excludedSubstringList}},
        matchingType:
          DLP.protos.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html)
            .[MATCHING_TYPE_PARTIAL_MATCH](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html),
      };
    
      // Construct a ruleset that applies the exclusion rule to the EMAIL_ADDRESSES infotype.
      const ruleSet = [
        {
          infoTypes: infoTypes,
          rules: [
            {
              exclusionRule: exclusionRule,
            },
          ],
        },
      ];
    
      // Construct the configuration for the Inspect request, including the ruleset.
      const inspectConfig = {
        infoTypes: infoTypes,
        ruleSet: ruleSet,
        includeQuote: true,
      };
    
      // Construct the Inspect request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: inspectConfig,
        item: item,
      };
    
      // Use the client to send the API request.
      const [response] = await dlp.inspectContent(request);
    
      // Print findings.
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
    inspectStringExclusionDictSubstr();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary\WordList;
    use Google\Cloud\Dlp\V2\ExclusionRule;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\InspectionRule;
    use Google\Cloud\Dlp\V2\InspectionRuleSet;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\MatchingType;
    
    /**
     * Inspect a string with an exclusion dictionary substring
     * Omit scan matches that include the substring "TEST".
     *
     * @param string $projectId                 The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect             The string to inspect.
     * @param array  $excludedSubStringArray    The sub string to excluded.
     */
    function inspect_string_with_exclusion_dict_substring(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $textToInspect = 'Some email addresses: gary@example.com, TEST@example.com',
        array  $excludedSubStringArray = ['Test']
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new ContentItem())
            ->setValue($textToInspect);
    
        // Specify the type of info the inspection will look for.
        $infotypes = [
            (new InfoType())->setName('PHONE_NUMBER'),
            (new InfoType())->setName('EMAIL_ADDRESS'),
            (new InfoType())->setName('DOMAIN_NAME'),
            (new InfoType())->setName('PERSON_NAME'),
        ];
    
        // Exclude matches from the specified excludedSubstringList.
        $excludedSubstringList = (new Dictionary())
            ->setWordList((new WordList())
                ->setWords($excludedSubStringArray));
    
        $exclusionRule = (new ExclusionRule())
            ->setMatchingType(MatchingType::MATCHING_TYPE_PARTIAL_MATCH)
            ->setDictionary($excludedSubstringList);
    
        // Construct a ruleset that applies the exclusion rule to the EMAIL_ADDRESSES infotype.
        $inspectionRuleSet = (new InspectionRuleSet())
            ->setInfoTypes($infotypes)
            ->setRules([
                (new InspectionRule())
                    ->setExclusionRule($exclusionRule),
            ]);
    
        // Construct the configuration for the Inspect request, including the ruleset.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes($infotypes)
            ->setIncludeQuote(true)
            ->setRuleSet([$inspectionRuleSet]);
    
        // Run request
        $inspectContentRequest = (new InspectContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->inspectContent($inspectContentRequest);
    
        // Print the results
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
    
    
    def inspect_string_with_exclusion_dict_substring(
        project: str, content_string: str, exclusion_list: List[str] = ["TEST"]
    ) -> None:
        """Inspects the provided text, avoiding matches that contain excluded tokens
    
        Uses the Data Loss Prevention API to omit matches if they include tokens
        in the specified exclusion list.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
            exclusion_list: The list of strings to ignore partial matches on
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct a list of infoTypes for DLP to locate in `content_string`. See
        # https://cloud.google.com/dlp/docs/concepts-infotypes for more information
        # about supported infoTypes.
        info_types_to_locate = [{"name": "EMAIL_ADDRESS"}, {"name": "DOMAIN_NAME"}]
    
        # Construct a rule set that will only match if the match text does not
        # contains tokens from the exclusion list.
        rule_set = [
            {
                "info_types": info_types_to_locate,
                "rules": [
                    {
                        "exclusion_rule": {
                            "dictionary": {"word_list": {"words": exclusion_list}},
                            "matching_type": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[MatchingType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.MatchingType.html).MATCHING_TYPE_PARTIAL_MATCH,
                        }
                    }
                ],
            }
        ]
    
        # Construct the configuration dictionary
        inspect_config = {
            "info_types": info_types_to_locate,
            "rule_set": rule_set,
            "include_quote": True,
        }
    
        # Construct the `item`.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={"parent": parent, "inspect_config": inspect_config, "item": item}
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Quote: {finding.quote}")
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

### REST

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.
    
    
    ...
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"EMAIL_ADDRESS"
            },
            {
              "name":"DOMAIN_NAME"
            },
            {
              "name":"PHONE_NUMBER"
            },
            {
              "name":"PERSON_NAME"
            }
          ],
          "ruleSet":[
            {
              "infoTypes":[
                {
                  "name":"EMAIL_ADDRESS"
                },
                {
                  "name":"DOMAIN_NAME"
                },
                {
                  "name":"PHONE_NUMBER"
                },
                {
                  "name":"PERSON_NAME"
                }
              ],
              "rules":[
                {
                  "exclusionRule":{
                    "dictionary":{
                      "wordList":{
                        "words":[
                          "TEST"
                        ]
                      }
                    },
                    "matchingType": "MATCHING_TYPE_PARTIAL_MATCH"
                  }
                }
              ]
            }
          ]
        }
    ...
    

#### Omit scan matches that include the substring "Jimmy" from a custom infoType detector scan

The following JSON snippet and code in several languages illustrates how to indicate to Sensitive Data Protection using an [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) that it should avoid matching on the name "Jimmy" in a scan that uses the specified custom regex detector:

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Collections.Generic;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class InspectStringCustomExcludingSubstring
    {
        public static InspectContentResponse Inspect(string projectId, string textToInspect, string customDetectorPattern, List<String> excludedSubstringList)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var byteContentItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
            {
                Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8),
                Data = Google.Protobuf.ByteString.CopyFromUtf8(textToInspect)
            };
    
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { ByteItem = byteContentItem };
    
            var infoType = new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)
            {
                Name = "CUSTOM_NAME_DETECTOR"
            };
            var customInfoType = new [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html)
            {
                InfoType = infoType,
                Regex = new CustomInfoType.Types.Regex { Pattern = customDetectorPattern }
            };
    
            var exclusionRule = new [ExclusionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExclusionRule.html)
            {
                MatchingType = [MatchingType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html).[PartialMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html#Google_Cloud_Dlp_V2_MatchingType_PartialMatch),
                Dictionary = new CustomInfoType.Types.Dictionary
                {
                    WordList = new CustomInfoType.Types.Dictionary.Types.WordList
                    {
                        Words = { excludedSubstringList }
                    }
                }
            };
    
            var ruleSet = new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)
            {
                InfoTypes = { infoType },
                Rules = { new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { ExclusionRule = exclusionRule } }
            };
    
            var config = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                CustomInfoTypes = { customInfoType },
                IncludeQuote = true,
                RuleSet = { ruleSet }
            };
    
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                Item = contentItem,
                InspectConfig = config
            };
    
            var response = dlp.InspectContent(request);
    
            Console.WriteLine($"Findings: {response.Result.Findings.Count}");
            foreach (var f in response.Result.Findings)
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
    
    // inspectStringCustomExcludingSubstring inspects a string for sensitive data, excluding a custom substring
    func inspectStringCustomExcludingSubstring(w io.Writer, projectID, textToInspect, customDetectorPattern string, excludedSubstringList []string) error {
    	// projectId := "your-project-id"
    	// textToInspect := "Name: Doe, John. Name: Example, Jimmy"
    	// customDetectorPattern := "[A-Z][a-z]{1,15}, [A-Z][a-z]{1,15}"
    	// excludedSubstringList := []string{"Jimmy"}
    
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
    
    	// Specify the type and content to be inspected.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_ByteItem{
    			ByteItem: &dlppb.ByteContentItem{
    				Type: dlppb.[ByteContentItem_TEXT_UTF8](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL),
    				Data: []byte(textToInspect),
    			},
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	infoType := &dlppb.InfoType{
    		Name: "CUSTOM_NAME_DETECTOR",
    	}
    
    	customInfotype := &dlppb.CustomInfoType{
    		InfoType: infoType,
    		Type: &dlppb.CustomInfoType_Regex_{
    			Regex: &dlppb.CustomInfoType_Regex{
    				Pattern: customDetectorPattern,
    			},
    		},
    	}
    
    	// Exclude partial matches from the specified excludedSubstringList.
    	exclusionRule := &dlppb.ExclusionRule{
    		Type: &dlppb.ExclusionRule_Dictionary{
    			Dictionary: &dlppb.CustomInfoType_Dictionary{
    				Source: &dlppb.CustomInfoType_Dictionary_WordList_{
    					WordList: &dlppb.CustomInfoType_Dictionary_WordList{
    						Words: excludedSubstringList,
    					},
    				},
    			},
    		},
    		MatchingType: dlppb.[MatchingType_MATCHING_TYPE_PARTIAL_MATCH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_MatchingType_MATCHING_TYPE_UNSPECIFIED_MatchingType_MATCHING_TYPE_FULL_MATCH_MatchingType_MATCHING_TYPE_PARTIAL_MATCH_MatchingType_MATCHING_TYPE_INVERSE_MATCH_MatchingType_MATCHING_TYPE_RULE_SPECIFIC),
    	}
    
    	// Construct a ruleset that applies the exclusion rule to the EMAIL_ADDRESSES infoType.
    	ruleSet := &dlppb.InspectionRuleSet{
    		InfoTypes: []*dlppb.InfoType{
    			infoType,
    		},
    		Rules: []*dlppb.InspectionRule{
    			{
    				Type: &dlppb.InspectionRule_ExclusionRule{
    					ExclusionRule: exclusionRule,
    				},
    			},
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.InspectContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:   contentItem,
    		InspectConfig: &dlppb.InspectConfig{
    			CustomInfoTypes: []*dlppb.CustomInfoType{
    				customInfotype,
    			},
    			IncludeQuote: true,
    			RuleSet: []*dlppb.InspectionRuleSet{
    				ruleSet,
    			},
    		},
    	}
    
    	// Send the request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Process the results.
    	fmt.Fprintf(w, "Findings: %v\n", len(resp.Result.Findings))
    	for _, v := range resp.GetResult().Findings {
    		fmt.Fprintf(w, "Quote: %v\n", v.GetQuote())
    		fmt.Fprintf(w, "Infotype Name: %v\n", v.GetInfoType().GetName())
    		fmt.Fprintf(w, "Likelihood: %v\n", v.GetLikelihood())
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
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).[WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html);
    import com.google.privacy.dlp.v2.[ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html);
    import com.google.privacy.dlp.v2.[InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    
    public class InspectStringCustomExcludingSubstring {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "Name: Doe, John. Name: Example, Jimmy";
        String customDetectorPattern = "[A-Z][a-z]{1,15}, [A-Z][a-z]{1,15}";
        List<String> excludedSubstringList = Arrays.asList("Jimmy");
        inspectStringCustomExcludingSubstring(
            projectId, textToInspect, customDetectorPattern, excludedSubstringList);
      }
    
      // Inspects the provided text, avoiding matches specified in the exclusion list.
      public static void inspectStringCustomExcludingSubstring(
          String projectId,
          String textToInspect,
          String customDetectorPattern,
          List<String> excludedSubstringList)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type and content to be inspected.
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(textToInspect))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build();
    
          // Specify the type of info the inspection will look for.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("CUSTOM_NAME_DETECTOR").build();
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder()
                  .setInfoType(infoType)
                  .setRegex([Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html).newBuilder().[setPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)(customDetectorPattern))
                  .build();
    
          // Exclude partial matches from the specified excludedSubstringList.
          [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html) exclusionRule =
              [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html).newBuilder()
                  .setMatchingType([MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html).MATCHING_TYPE_PARTIAL_MATCH)
                  .setDictionary(
                      [Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).newBuilder()
                          .setWordList([WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html).newBuilder().[addAllWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Dictionary_WordList_Builder_addAllWords_java_lang_Iterable_java_lang_String__)(excludedSubstringList)))
                  .build();
    
          // Construct a ruleset that applies the exclusion rule to the EMAIL_ADDRESSES infotype.
          [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html) ruleSet =
              [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html).newBuilder()
                  .addInfoTypes(infoType)
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().[setExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.Builder.html#com_google_privacy_dlp_v2_InspectionRule_Builder_setExclusionRule_com_google_privacy_dlp_v2_ExclusionRule_)(exclusionRule))
                  .build();
    
          // Construct the configuration for the Inspect request, including the ruleset.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .[addRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_)(ruleSet)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(config)
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The string to inspect
    // const string = 'Name: Doe, John. Name: Example, Jimmy';
    
    // Words to exclude
    // const excludedWords = ['Jimmy'];
    
    async function inspectStringCustomExclusionDict() {
      // Specify the content to be inspected.
      const item = {value: string};
    
      // Specify the type of info the inspection will look for.
      const customInfoTypes = [
        {
          infoType: {name: 'CUSTOM_NAME_DETECTOR'},
          regex: {pattern: '[A-Z][a-z]{1,15}, [A-Z][a-z]{1,15}'},
        },
      ];
    
      // Exclude partial matches from the specified excludedSubstringList.
      const exclusionRUle = {
        dictionary: {wordList: {words: excludedWords}},
        matchingType:
          DLP.protos.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html)
            .[MATCHING_TYPE_PARTIAL_MATCH](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html),
      };
    
      // Construct a rule set that will only match if the match text does not
      // contains tokens from the exclusion list.
      const ruleSet = [
        {
          infoTypes: [{name: 'CUSTOM_NAME_DETECTOR'}],
          rules: [
            {
              exclusionRule: exclusionRUle,
            },
          ],
        },
      ];
    
      // Construct the configuration for the Inspect request, including the ruleset.
      const inspectConfig = {
        customInfoTypes: customInfoTypes,
        ruleSet: ruleSet,
        includeQuote: true,
      };
    
      // Construct the Inspect request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: inspectConfig,
        item: item,
      };
    
      // Use the client to send the API request.
      const [response] = await dlp.inspectContent(request);
    
      // Print findings.
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
    inspectStringCustomExclusionDict();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary\WordList;
    use Google\Cloud\Dlp\V2\CustomInfoType\Regex;
    use Google\Cloud\Dlp\V2\ExclusionRule;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\InspectionRule;
    use Google\Cloud\Dlp\V2\InspectionRuleSet;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\MatchingType;
    
    /**
     * Inspect a string for sensitive data, excluding a custom substring
     * Illustrates how to use an InspectConfig to instruct Cloud DLP to avoid matching on the name "Jimmy" in a scan that uses the specified custom regular expression detector.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect     The string to inspect.
     */
    function inspect_string_custom_excluding_substring(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $textToInspect = 'Name: Doe, John. Name: Example, Jimmy'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
        $customDetectorPattern = '[A-Z][a-z]{1,15}, [A-Z][a-z]{1,15}';
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new ContentItem())
            ->setValue($textToInspect);
    
        // Specify the type of info the inspection will look for.
        $customerNameDetector = (new InfoType())
            ->setName('CUSTOM_NAME_DETECTOR');
        $customInfoType = (new CustomInfoType())
            ->setInfoType($customerNameDetector)
            ->setRegex((new Regex())
                ->setPattern($customDetectorPattern));
    
        // Exclude partial matches from the specified excludedSubstringList.
        $excludedSubstringList = (new Dictionary())
            ->setWordList((new WordList())
                ->setWords(['Jimmy']));
    
        $exclusionRule = (new ExclusionRule())
            ->setMatchingType(MatchingType::MATCHING_TYPE_PARTIAL_MATCH)
            ->setDictionary($excludedSubstringList);
    
        // Construct a ruleset that applies the exclusion rule.
        $inspectionRuleSet = (new InspectionRuleSet())
            ->setInfoTypes([$customerNameDetector])
            ->setRules([
                (new InspectionRule())
                    ->setExclusionRule($exclusionRule),
            ]);
    
        // Construct the configuration for the Inspect request, including the ruleset.
        $inspectConfig = (new InspectConfig())
            ->setCustomInfoTypes([$customInfoType])
            ->setIncludeQuote(true)
            ->setRuleSet([$inspectionRuleSet]);
    
        // Run request
        $inspectContentRequest = (new InspectContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->inspectContent($inspectContentRequest);
    
        // Print the results
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
    
    
    def inspect_string_custom_excluding_substring(
        project: str, content_string: str, exclusion_list: List[str] = ["jimmy"]
    ) -> None:
        """Inspects the provided text with a custom detector, avoiding matches on specific tokens
    
        Uses the Data Loss Prevention API to omit matches on a custom detector
        if they include tokens in the specified exclusion list.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
            exclusion_list: The list of strings to ignore matches on
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct a custom regex detector for names
        custom_info_types = [
            {
                "info_type": {"name": "CUSTOM_NAME_DETECTOR"},
                "regex": {"pattern": "[A-Z][a-z]{1,15}, [A-Z][a-z]{1,15}"},
            }
        ]
    
        # Construct a rule set that will only match if the match text does not
        # contains tokens from the exclusion list.
        rule_set = [
            {
                "info_types": [{"name": "CUSTOM_NAME_DETECTOR"}],
                "rules": [
                    {
                        "exclusion_rule": {
                            "dictionary": {"word_list": {"words": exclusion_list}},
                            "matching_type": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[MatchingType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.MatchingType.html).MATCHING_TYPE_PARTIAL_MATCH,
                        }
                    }
                ],
            }
        ]
    
        # Construct the configuration dictionary
        inspect_config = {
            "custom_info_types": custom_info_types,
            "rule_set": rule_set,
            "include_quote": True,
        }
    
        # Construct the `item`.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={"parent": parent, "inspect_config": inspect_config, "item": item}
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Quote: {finding.quote}")
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

### REST

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.
    
    
    ...
        "inspectConfig":{
          "customInfoTypes":[
            {
              "infoType":{
                "name":"CUSTOM_NAME_DETECTOR"
              },
              "regex":{
                "pattern":"[A-Z][a-z]{1,15}, [A-Z][a-z]{1,15}"
              }
            }
          ],
          "ruleSet":[
            {
              "infoTypes":[
                {
                  "name":"CUSTOM_NAME_DETECTOR"
                }
              ],
              "rules":[
                {
                  "exclusionRule":{
                    "dictionary":{
                      "wordList":{
                        "words":[
                          "Jimmy"
                        ]
                      }
                    },
                    "matchingType": "MATCHING_TYPE_PARTIAL_MATCH"
                  }
                }
              ]
            }
          ]
        }
    ...
    

#### Omit scan matches from a PERSON_NAME detector scan that overlap with a custom detector

In this scenario, the user does not want a match from a Sensitive Data Protection scan using the `PERSON_NAME` built-in detector returned if the match would also be matched in a scan using the custom regex detector defined in the first part of the snippet.

The following JSON snippet and code in several languages specifies both a custom regex detector and an exclusion rule in the [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig). The custom regex detector specifies the names to exclude from results. The exclusion rule specifies that if any results returned from a scan for `PERSON_NAME` would also be matched by the custom regex detector, they are omitted. Note that `VIP_DETECTOR` in this case is marked as `EXCLUSION_TYPE_EXCLUDE`, so it will not produce results itself. It will only affect results produced by the `PERSON_NAME` detector.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using static Google.Cloud.Dlp.V2.CustomInfoType.Types;
    
    public class InspectStringCustomOmitOverlap
    {
        public static InspectContentResponse Inspect(string projectId, string textToInspect)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var byteItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
            {
                Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8),
                Data = Google.Protobuf.ByteString.CopyFromUtf8(textToInspect)
            };
    
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { ByteItem = byteItem };
    
            var customInfoType = new [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html)
            {
                InfoType = new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "VIP_DETECTOR" },
                Regex = new CustomInfoType.Types.Regex { Pattern = "Larry Page|Sergey Brin" },
                ExclusionType = ExclusionType.[Exclude](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.ExclusionType.html#Google_Cloud_Dlp_V2_CustomInfoType_Types_ExclusionType_Exclude)
            };
    
            var exclusionRule = new [ExclusionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExclusionRule.html)
            {
                ExcludeInfoTypes = new [ExcludeInfoTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExcludeInfoTypes.html) { InfoTypes = { customInfoType.[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) } },
                MatchingType = [MatchingType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html).[FullMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html#Google_Cloud_Dlp_V2_MatchingType_FullMatch)
            };
    
            var ruleSet = new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)
            {
                InfoTypes = { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" } },
                Rules = { new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { ExclusionRule = exclusionRule } }
            };
    
            var config = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" } },
                CustomInfoTypes = { customInfoType },
                IncludeQuote = true,
                RuleSet = { ruleSet }
            };
    
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                Item = contentItem,
                InspectConfig = config
            };
    
            var response = dlp.InspectContent(request);
    
            Console.WriteLine($"Findings: {response.Result.Findings.Count}");
            foreach (var f in response.Result.Findings)
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
    
    // inspectStringCustomOmitOverlap inspects a string for sensitive data with omitting custom matches
    func inspectStringCustomOmitOverlap(w io.Writer, projectID, textToInspect, customInfoTypeName, infoTypeName, regex string) error {
    	// projectID := "my-project-id"
    	// textToInspect := "Name: Jane Doe. Name: Larry Page."
    	// customInfoTypeName := "VIP_DETECTOR"
    	// infoTypeName := "PERSON_NAME"
    	// regex := "Larry Page|Sergey Brin"
    
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
    
    	// Specify the type and content to be inspected.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_ByteItem{
    			ByteItem: &dlppb.ByteContentItem{
    				Type: dlppb.[ByteContentItem_TEXT_UTF8](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL),
    				Data: []byte(textToInspect),
    			},
    		},
    	}
    	// Construct the custom infoType.
    	customInfotype := &dlppb.CustomInfoType{
    		InfoType: &dlppb.InfoType{
    			Name: customInfoTypeName,
    		},
    		Type: &dlppb.CustomInfoType_Regex_{
    			Regex: &dlppb.CustomInfoType_Regex{
    				Pattern: regex,
    			},
    		},
    		ExclusionType: dlppb.[CustomInfoType_EXCLUSION_TYPE_EXCLUDE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_CustomInfoType_EXCLUSION_TYPE_UNSPECIFIED_CustomInfoType_EXCLUSION_TYPE_EXCLUDE),
    	}
    
    	// Exclude matches that also match the custom infoType.
    	exclusionRule := &dlppb.ExclusionRule{
    		Type: &dlppb.ExclusionRule_ExcludeInfoTypes{
    			ExcludeInfoTypes: &dlppb.ExcludeInfoTypes{
    				InfoTypes: []*dlppb.InfoType{
    					customInfotype.GetInfoType(),
    				},
    			},
    		},
    		MatchingType: dlppb.[MatchingType_MATCHING_TYPE_FULL_MATCH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_MatchingType_MATCHING_TYPE_UNSPECIFIED_MatchingType_MATCHING_TYPE_FULL_MATCH_MatchingType_MATCHING_TYPE_PARTIAL_MATCH_MatchingType_MATCHING_TYPE_INVERSE_MATCH_MatchingType_MATCHING_TYPE_RULE_SPECIFIC),
    	}
    
    	// Construct a ruleSet that applies the exclusion rule to the PERSON_NAME infoType.
    	ruleSet := &dlppb.InspectionRuleSet{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: infoTypeName},
    		},
    		Rules: []*dlppb.InspectionRule{
    			{
    				Type: &dlppb.InspectionRule_ExclusionRule{
    					ExclusionRule: exclusionRule,
    				},
    			},
    		},
    	}
    
    	// Construct the configuration for the Inspect request, including the ruleSet.
    	config := &dlppb.InspectConfig{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: infoTypeName},
    		},
    		CustomInfoTypes: []*dlppb.CustomInfoType{
    			customInfotype,
    		},
    		IncludeQuote: true,
    		RuleSet: []*dlppb.InspectionRuleSet{
    			ruleSet,
    		},
    	}
    
    	// Create a configured request.
    	req := &dlppb.InspectContentRequest{
    		Parent:        fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:          contentItem,
    		InspectConfig: config,
    	}
    
    	// Send the request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Parse the response and process results
    	fmt.Fprintf(w, "Findings: %v\n", len(resp.Result.Findings))
    	for _, v := range resp.GetResult().Findings {
    		fmt.Fprintf(w, "Quote: %v\n", v.GetQuote())
    		fmt.Fprintf(w, "Infotype Name: %v\n", v.GetInfoType().GetName())
    		fmt.Fprintf(w, "Likelihood: %v\n", v.GetLikelihood())
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
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[ExclusionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.ExclusionType.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html);
    import com.google.privacy.dlp.v2.[ExcludeInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExcludeInfoTypes.html);
    import com.google.privacy.dlp.v2.[ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html);
    import com.google.privacy.dlp.v2.[InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class InspectStringCustomOmitOverlap {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "Name: Jane Doe. Name: Larry Page.";
        inspectStringCustomOmitOverlap(projectId, textToInspect);
      }
    
      // Inspects the provided text, avoiding matches specified in the exclusion list.
      public static void inspectStringCustomOmitOverlap(String projectId, String textToInspect)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type and content to be inspected.
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(textToInspect))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build();
    
          // Construct the custom infotype.
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder()
                  .setInfoType([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("VIP_DETECTOR"))
                  .setRegex([Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html).newBuilder().[setPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)("Larry Page|Sergey Brin"))
                  .[setExclusionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Builder_setExclusionType_com_google_privacy_dlp_v2_CustomInfoType_ExclusionType_)([ExclusionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.ExclusionType.html).EXCLUSION_TYPE_EXCLUDE)
                  .build();
    
          // Exclude matches that also match the custom infotype.
          [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html) exclusionRule =
              [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html).newBuilder()
                  .setExcludeInfoTypes(
                      [ExcludeInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExcludeInfoTypes.html).newBuilder().addInfoTypes(customInfoType.[getInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html#com_google_privacy_dlp_v2_CustomInfoType_getInfoType__)()))
                  .setMatchingType([MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html).MATCHING_TYPE_FULL_MATCH)
                  .build();
    
          // Construct a ruleset that applies the exclusion rule to the PERSON_NAME infotype.
          [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html) ruleSet =
              [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html).newBuilder()
                  .addInfoTypes([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME"))
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().[setExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.Builder.html#com_google_privacy_dlp_v2_InspectionRule_Builder_setExclusionRule_com_google_privacy_dlp_v2_ExclusionRule_)(exclusionRule))
                  .build();
    
          // Construct the configuration for the Inspect request, including the ruleset.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addInfoTypes([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME"))
                  .[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .[addRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_)(ruleSet)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(config)
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The string to inspect
    // const string = 'Name: Jane Doe. Name: Larry Page.';
    
    async function inspectStringCustomOmitOverlap() {
      // Construct item to inspect
      const item = {value: string};
    
      // Construct a custom regex detector for names
      const customInfoTypes = [
        {
          infoType: {name: 'VIP_DETECTOR'},
          regex: {pattern: 'Larry Page|Sergey Brin'},
          exclusionType:
            DLP.protos.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.custominfotype-class.html).[ExclusionType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.custominfotype.exclusiontype.html)
              .[EXCLUSION_TYPE_EXCLUDE](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.custominfotype.exclusiontype.html),
        },
      ];
    
      // Construct a exclusion rule
      const exclusionRule = {
        excludeInfoTypes: {
          infoTypes: [{name: 'VIP_DETECTOR'}],
        },
        matchingType:
          DLP.protos.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html).[MATCHING_TYPE_FULL_MATCH](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html),
      };
    
      // Construct a rule set that will only match if the match text does not
      // contains Info type matches.
      const ruleSet = [
        {
          infoTypes: [{name: 'PERSON_NAME'}],
          rules: [
            {
              exclusionRule: exclusionRule,
            },
          ],
        },
      ];
    
      // Construct the inspect configuration
      const inspectConfig = {
        infoTypes: [{name: 'PERSON_NAME'}],
        customInfoTypes: customInfoTypes,
        ruleSet: ruleSet,
        includeQuote: true,
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: inspectConfig,
        item: item,
      };
    
      // Run request
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
    inspectStringCustomOmitOverlap();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType;
    use Google\Cloud\Dlp\V2\CustomInfoType\ExclusionType;
    use Google\Cloud\Dlp\V2\CustomInfoType\Regex;
    use Google\Cloud\Dlp\V2\ExcludeInfoTypes;
    use Google\Cloud\Dlp\V2\ExclusionRule;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\InspectionRule;
    use Google\Cloud\Dlp\V2\InspectionRuleSet;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\MatchingType;
    
    /**
     * Inspect a string for sensitive data, omitting custom matches
     * Omit scan matches from a PERSON_NAME detector scan that overlap with a custom detector.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect     The string to inspect.
     */
    function inspect_string_custom_omit_overlap(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $textToInspect = 'Name: Jane Doe. Name: Larry Page.'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new ContentItem())
            ->setValue($textToInspect);
    
        // Specify the type of info the inspection will look for.
        $vipDetector = (new InfoType())
            ->setName('VIP_DETECTOR');
        $pattern = 'Larry Page|Sergey Brin';
        $customInfoType = (new CustomInfoType())
            ->setInfoType($vipDetector)
            ->setRegex((new Regex())
                ->setPattern($pattern))
            ->setExclusionType(ExclusionType::EXCLUSION_TYPE_EXCLUDE);
    
        // Exclude matches that also match the custom infotype.
        $exclusionRule = (new ExclusionRule())
            ->setMatchingType(MatchingType::MATCHING_TYPE_FULL_MATCH)
            ->setExcludeInfoTypes((new ExcludeInfoTypes())
                    ->setInfoTypes([$customInfoType->getInfoType()])
            );
    
        // Construct a ruleset that applies the exclusion rule to the PERSON_NAME infotype.
        $personName = (new InfoType())
            ->setName('PERSON_NAME');
        $inspectionRuleSet = (new InspectionRuleSet())
            ->setInfoTypes([$personName])
            ->setRules([
                (new InspectionRule())
                    ->setExclusionRule($exclusionRule),
            ]);
    
        // Construct the configuration for the Inspect request, including the ruleset.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes([$personName])
            ->setCustomInfoTypes([$customInfoType])
            ->setIncludeQuote(true)
            ->setRuleSet([$inspectionRuleSet]);
    
        // Run request
        $inspectContentRequest = (new InspectContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->inspectContent($inspectContentRequest);
    
        // Print the results
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
    
    
    import google.cloud.dlp
    
    
    def inspect_string_custom_omit_overlap(project: str, content_string: str) -> None:
        """Matches PERSON_NAME and a custom detector,
        but if they overlap only matches the custom detector
    
        Uses the Data Loss Prevention API to omit matches on a built-in detector
        if they overlap with matches from a custom detector
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct a custom regex detector for names
        custom_info_types = [
            {
                "info_type": {"name": "VIP_DETECTOR"},
                "regex": {"pattern": "Larry Page|Sergey Brin"},
                "exclusion_type": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[CustomInfoType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CustomInfoType.html).[ExclusionType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CustomInfoType.ExclusionType.html).EXCLUSION_TYPE_EXCLUDE,
            }
        ]
    
        # Construct a rule set that will exclude PERSON_NAME matches
        # that overlap with VIP_DETECTOR matches
        rule_set = [
            {
                "info_types": [{"name": "PERSON_NAME"}],
                "rules": [
                    {
                        "exclusion_rule": {
                            "exclude_info_types": {
                                "info_types": [{"name": "VIP_DETECTOR"}]
                            },
                            "matching_type": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[MatchingType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.MatchingType.html).MATCHING_TYPE_FULL_MATCH,
                        }
                    }
                ],
            }
        ]
    
        # Construct the configuration dictionary
        inspect_config = {
            "info_types": [{"name": "PERSON_NAME"}],
            "custom_info_types": custom_info_types,
            "rule_set": rule_set,
            "include_quote": True,
        }
    
        # Construct the `item`.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={"parent": parent, "inspect_config": inspect_config, "item": item}
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Quote: {finding.quote}")
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

### REST

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.
    
    
    ...
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"PERSON_NAME"
            }
          ],
          "customInfoTypes":[
            {
              "infoType":{
                "name":"VIP_DETECTOR"
              },
              "regex":{
                "pattern":"Dana Williams|Quinn Garcia"
              },
              "exclusionType":"EXCLUSION_TYPE_EXCLUDE"
            }
          ],
          "ruleSet":[
            {
              "infoTypes":[
                {
                  "name":"PERSON_NAME"
                }
              ],
              "rules":[
                {
                  "exclusionRule":{
                    "excludeInfoTypes":{
                      "infoTypes":[
                        {
                          "name":"VIP_DETECTOR"
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
    ...
    

#### Omit matches on PERSON_NAME detector if also matched by EMAIL_ADDRESS detector

The following JSON snippet and code in several languages illustrate how to indicate to Sensitive Data Protection using an [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) that it should only return one match in the case that matches for the `PERSON_NAME` detector overlap with matches for the `EMAIL_ADDRESS` detector. Doing this is to avoid the situation where an email address such as "james@example.com" matches on both the `PERSON_NAME` and `EMAIL_ADDRESS` detectors.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class InspectStringOmitOverlap
    {
        public static InspectContentResponse Inspect(string projectId, string textToInspect)
        {
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests. After completing all of your requests, call
            // the "close" method on the client to safely clean up any remaining background resources.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Specify the type and content to be inspected.
            var byteItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
            {
                Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8),
                Data = Google.Protobuf.ByteString.CopyFromUtf8(textToInspect)
            };
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { ByteItem = byteItem };
    
            // Specify the type of info the inspection will look for.
            // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
            var infoTypes = new string[] { "PERSON_NAME", "EMAIL_ADDRESS" }.Select(it => new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = it });
    
            // Exclude EMAIL_ADDRESS matches
            var exclusionRule = new [ExclusionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExclusionRule.html)
            {
                ExcludeInfoTypes = new [ExcludeInfoTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExcludeInfoTypes.html) { InfoTypes = { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" } } },
                MatchingType = [MatchingType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html).[PartialMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html#Google_Cloud_Dlp_V2_MatchingType_PartialMatch)
            };
    
            // Construct a ruleset that applies the exclusion rule to the PERSON_NAME infotype.
            // If a PERSON_NAME match overlaps with an EMAIL_ADDRESS match, the PERSON_NAME match will
            // be excluded.
            var ruleSet = new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)
            {
                InfoTypes = { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" } },
                Rules = { new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { ExclusionRule = exclusionRule } }
            };
    
            // Construct the configuration for the Inspect request, including the ruleset.
            var config = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infoTypes },
                IncludeQuote = true,
                RuleSet = { ruleSet }
            };
    
            // Construct the Inspect request to be sent by the client.
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                Item = contentItem,
                InspectConfig = config
            };
    
            // Use the client to send the API request.
            var response = dlp.InspectContent(request);
    
            // Parse the response and process results
            Console.WriteLine($"Findings: {response.Result.Findings.Count}");
            foreach (var f in response.Result.Findings)
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
    
    // inspectStringOmitOverlap inspects a string for sensitive data and
    // omitting overlapping matches on person and email
    func inspectStringOmitOverlap(w io.Writer, projectID, textToInspect string) error {
    	// projectID := "my-project-id"
    	// textToInspect := "gary@example.com"
    
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
    
    	// Specify the type and content to be inspected.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_ByteItem{
    			ByteItem: &dlppb.ByteContentItem{
    				Type: dlppb.[ByteContentItem_TEXT_UTF8](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL),
    				Data: []byte(textToInspect),
    			},
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
    	infoTypes := []*dlppb.InfoType{
    		{Name: "PERSON_NAME"},
    		{Name: "EMAIL_ADDRESS"},
    	}
    
    	// Exclude EMAIL_ADDRESS matches
    	exclusionRule := &dlppb.ExclusionRule{
    		Type: &dlppb.ExclusionRule_ExcludeInfoTypes{
    			ExcludeInfoTypes: &dlppb.ExcludeInfoTypes{
    				InfoTypes: []*dlppb.InfoType{
    					{Name: "EMAIL_ADDRESS"},
    				},
    			},
    		},
    		MatchingType: dlppb.[MatchingType_MATCHING_TYPE_PARTIAL_MATCH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_MatchingType_MATCHING_TYPE_UNSPECIFIED_MatchingType_MATCHING_TYPE_FULL_MATCH_MatchingType_MATCHING_TYPE_PARTIAL_MATCH_MatchingType_MATCHING_TYPE_INVERSE_MATCH_MatchingType_MATCHING_TYPE_RULE_SPECIFIC),
    	}
    
    	// Construct a ruleSet that applies the exclusion rule to the PERSON_NAME infoType.
    	// If a PERSON_NAME match overlaps with an EMAIL_ADDRESS match, the PERSON_NAME match will
    	// be excluded.
    	ruleSet := &dlppb.InspectionRuleSet{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: "PERSON_NAME"},
    		},
    		Rules: []*dlppb.InspectionRule{
    			{
    				Type: &dlppb.InspectionRule_ExclusionRule{
    					ExclusionRule: exclusionRule,
    				},
    			},
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.InspectContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:   contentItem,
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes:    infoTypes,
    			IncludeQuote: true,
    			RuleSet: []*dlppb.InspectionRuleSet{
    				ruleSet,
    			},
    		},
    	}
    
    	// Send the request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Process the results.
    	fmt.Fprintf(w, "Findings: %v\n", len(resp.Result.Findings))
    	for _, v := range resp.GetResult().Findings {
    		fmt.Fprintf(w, "Quote: %v\n", v.GetQuote())
    		fmt.Fprintf(w, "Infotype Name: %v\n", v.GetInfoType().GetName())
    		fmt.Fprintf(w, "Likelihood: %v\n", v.GetLikelihood())
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
    import com.google.privacy.dlp.v2.[ExcludeInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExcludeInfoTypes.html);
    import com.google.privacy.dlp.v2.[ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html);
    import com.google.privacy.dlp.v2.[InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class InspectStringOmitOverlap {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "james@example.com";
        inspectStringOmitOverlap(projectId, textToInspect);
      }
    
      // Inspects the provided text, avoiding matches specified in the exclusion list.
      public static void inspectStringOmitOverlap(String projectId, String textToInspect)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type and content to be inspected.
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(textToInspect))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
          List<InfoType> infoTypes = new ArrayList<>();
          for (String typeName : new String[] {"PERSON_NAME", "EMAIL_ADDRESS"}) {
            infoTypes.add([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(typeName).build());
          }
    
          // Exclude EMAIL_ADDRESS matches
          [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html) exclusionRule =
              [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html).newBuilder()
                  .setExcludeInfoTypes(
                      [ExcludeInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExcludeInfoTypes.html).newBuilder()
                          .addInfoTypes([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("EMAIL_ADDRESS")))
                  .setMatchingType([MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html).MATCHING_TYPE_PARTIAL_MATCH)
                  .build();
    
          // Construct a ruleset that applies the exclusion rule to the PERSON_NAME infotype.
          // If a PERSON_NAME match overlaps with an EMAIL_ADDRESS match, the PERSON_NAME match will
          // be excluded.
          [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html) ruleSet =
              [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html).newBuilder()
                  .addInfoTypes([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME"))
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().[setExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.Builder.html#com_google_privacy_dlp_v2_InspectionRule_Builder_setExclusionRule_com_google_privacy_dlp_v2_ExclusionRule_)(exclusionRule))
                  .build();
    
          // Construct the configuration for the Inspect request, including the ruleset.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .[addRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_)(ruleSet)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(config)
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The string to inspect
    // const string = 'james@example.com';
    
    async function inspectStringWithoutOverlapPersonEmail() {
      // Construct item to inspect
      const item = {
        byteItem: {
          type: DLP.protos.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem-class.html).[BytesType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html)
            .[TEXT_UTF8](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html),
          data: Buffer.from(string, 'utf-8'),
        },
      };
    
      // Specify the type of info the inspection will look for.
      const infoTypes = [{name: 'PERSON_NAME'}, {name: 'EMAIL_ADDRESS'}];
    
      // Exclude EMAIL_ADDRESS matches
      const exclusionRule = {
        excludeInfoTypes: {
          infoTypes: [{name: 'EMAIL_ADDRESS'}],
        },
        matchingType:
          DLP.protos.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html)
            .[MATCHING_TYPE_PARTIAL_MATCH](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html),
      };
    
      // Construct a ruleset that applies the exclusion rule to the PERSON_NAME infotype.
      // If a PERSON_NAME match overlaps with an EMAIL_ADDRESS match, the PERSON_NAME match will
      // be excluded.
      const ruleSet = [
        {
          infoTypes: [{name: 'PERSON_NAME'}],
          rules: [
            {
              exclusionRule: exclusionRule,
            },
          ],
        },
      ];
    
      // Construct the configuration for the Inspect request, including the ruleset.
      const inspectConfig = {
        infoTypes: infoTypes,
        ruleSet: ruleSet,
        includeQuote: true,
      };
    
      // Construct the Inspect request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: inspectConfig,
        item: item,
      };
    
      // Run request
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
    inspectStringWithoutOverlapPersonEmail();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\ExcludeInfoTypes;
    use Google\Cloud\Dlp\V2\ExclusionRule;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\InspectionRule;
    use Google\Cloud\Dlp\V2\InspectionRuleSet;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\MatchingType;
    
    /**
     * Inspect a string for sensitive data, omitting overlapping matches on person and email
     * Omit matches on a PERSON_NAME detector if also matched by an EMAIL_ADDRESS detector.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect     The string to inspect.
     */
    function inspect_string_omit_overlap(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $textToInspect = 'james@example.org is an email.'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new ContentItem())
            ->setValue($textToInspect);
    
        // Specify the type of info the inspection will look for.
        $personName = (new InfoType())
            ->setName('PERSON_NAME');
        $emailAddress = (new InfoType())
            ->setName('EMAIL_ADDRESS');
        $infoTypes = [$personName, $emailAddress];
    
        // Exclude EMAIL_ADDRESS matches
        $exclusionRule = (new ExclusionRule())
            ->setMatchingType(MatchingType::MATCHING_TYPE_PARTIAL_MATCH)
            ->setExcludeInfoTypes((new ExcludeInfoTypes())
                    ->setInfoTypes([$emailAddress])
            );
    
        // Construct a ruleset that applies the exclusion rule to the PERSON_NAME infotype.
        // If a PERSON_NAME match overlaps with an EMAIL_ADDRESS match, the PERSON_NAME match will
        // be excluded.
        $inspectionRuleSet = (new InspectionRuleSet())
            ->setInfoTypes([$personName])
            ->setRules([
                (new InspectionRule())
                    ->setExclusionRule($exclusionRule),
            ]);
    
        // Construct the configuration for the Inspect request, including the ruleset.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes($infoTypes)
            ->setIncludeQuote(true)
            ->setRuleSet([$inspectionRuleSet]);
    
        // Run request
        $inspectContentRequest = (new InspectContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->inspectContent($inspectContentRequest);
    
        // Print the results
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
    
    
    import google.cloud.dlp
    
    
    def inspect_string_omit_overlap(
        project: str,
        content_string: str,
    ) -> None:
        """Matches PERSON_NAME and EMAIL_ADDRESS, but not both.
    
        Uses the Data Loss Prevention API omit matches on PERSON_NAME if the
        EMAIL_ADDRESS detector also matches.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct a list of infoTypes for DLP to locate in `content_string`. See
        # https://cloud.google.com/dlp/docs/concepts-infotypes for more information
        # about supported infoTypes.
        info_types_to_locate = [{"name": "PERSON_NAME"}, {"name": "EMAIL_ADDRESS"}]
    
        # Construct the configuration dictionary that will only match on PERSON_NAME
        # if the EMAIL_ADDRESS doesn't also match. This configuration helps reduce
        # the total number of findings when there is a large overlap between different
        # infoTypes.
        inspect_config = {
            "info_types": info_types_to_locate,
            "rule_set": [
                {
                    "info_types": [{"name": "PERSON_NAME"}],
                    "rules": [
                        {
                            "exclusion_rule": {
                                "exclude_info_types": {
                                    "info_types": [{"name": "EMAIL_ADDRESS"}]
                                },
                                "matching_type": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[MatchingType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.MatchingType.html).MATCHING_TYPE_PARTIAL_MATCH,
                            }
                        }
                    ],
                }
            ],
            "include_quote": True,
        }
    
        # Construct the `item`.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={"parent": parent, "inspect_config": inspect_config, "item": item}
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Quote: {finding.quote}")
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

### REST

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.
    
    
    ...
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"PERSON_NAME"
            },
            {
              "name":"EMAIL_ADDRESS"
            }
          ],
          "ruleSet":[
            {
              "infoTypes":[
                {
                  "name":"PERSON_NAME"
                }
              ],
              "rules":[
                {
                  "exclusionRule":{
                    "excludeInfoTypes":{
                      "infoTypes":[
                        {
                          "name":"EMAIL_ADDRESS"
                        }
                      ]
                    },
                    "matchingType": "MATCHING_TYPE_PARTIAL_MATCH"
                  }
                }
              ]
            }
          ]
        }
    ...
    

#### Omit matches on domain names that are part of email addresses in a DOMAIN_NAME detector scan

The following JSON snippet and code in several languages illustrate how to indicate to Sensitive Data Protection using an [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) that it should only return matches for a `DOMAIN_NAME` detector scan if the match does not overlap with a match in an `EMAIL_ADDRESS` detector scan. In this scenario, the main scan is a `DOMAIN_NAME` detector scan. The user does not want a domain name match returned in findings if the domain name is used in an email address:

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System.Linq;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using static Google.Cloud.Dlp.V2.CustomInfoType.Types;
    
    public class InspectStringWithoutOverlap
    {
        public static InspectContentResponse Inspect(string projectId, string textToInspect)
        {
            // Initialize client that will be used to send requests. This client only needs to be created
            // once, and can be reused for multiple requests. After completing all of your requests, call
            // the "close" method on the client to safely clean up any remaining background resources.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Specify the type and content to be inspected.
            var byteContentItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
            {
                Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8),
                Data = Google.Protobuf.ByteString.CopyFromUtf8(textToInspect)
            };
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html)
            {
                ByteItem = byteContentItem
            };
    
            // Specify the type of info the inspection will look for.
            // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
            var infoTypes = new string[] { "DOMAIN_NAME", "EMAIL_ADDRESS" }.Select(it => new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = it });
    
            // Define a custom info type to exclude email addresses
            var customInfoType = new [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html)
            {
                InfoType = new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" },
                ExclusionType = ExclusionType.[Exclude](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.Types.ExclusionType.html#Google_Cloud_Dlp_V2_CustomInfoType_Types_ExclusionType_Exclude)
            };
    
            // Exclude EMAIL_ADDRESS matches
            var exclusionRule = new [ExclusionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExclusionRule.html)
            {
                ExcludeInfoTypes = new [ExcludeInfoTypes](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExcludeInfoTypes.html)
                {
                    InfoTypes = { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "EMAIL_ADDRESS" } }
                },
                MatchingType = [MatchingType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html).[PartialMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html#Google_Cloud_Dlp_V2_MatchingType_PartialMatch)
            };
    
            // Construct a ruleset that applies the exclusion rule to the DOMAIN_NAME infotype.
            // If a DOMAIN_NAME match is part of an EMAIL_ADDRESS match, the DOMAIN_NAME match will
            // be excluded.
            var ruleSet = new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)
            {
                InfoTypes = { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "DOMAIN_NAME" } },
                Rules = { new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { ExclusionRule = exclusionRule } }
            };
    
            // Construct the configuration for the Inspect request, including the ruleset.
            var config = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infoTypes },
                CustomInfoTypes = { customInfoType },
                IncludeQuote = true,
                RuleSet = { ruleSet }
            };
    
            // Construct the Inspect request to be sent by the client.
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                Item = contentItem,
                InspectConfig = config
            };
    
            // Use the client to send the API request.
            var response = dlp.InspectContent(request);
    
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
    
    // inspectStringWithoutOverlap inspects a string for sensitive data
    // and omit overlapping matches on domain and email
    func inspectStringWithoutOverlap(w io.Writer, projectID, textToInspect string) error {
    	// projectID := "my-project-id"
    	// textToInspect := "example.com is a domain, james@example.org is an email."
    
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
    
    	// Specify the type and content to be inspected.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_ByteItem{
    			ByteItem: &dlppb.ByteContentItem{
    				Type: dlppb.[ByteContentItem_TEXT_UTF8](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL),
    				Data: []byte(textToInspect),
    			},
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
    	infoTypes := []*dlppb.InfoType{
    		{Name: "DOMAIN_NAME"},
    		{Name: "EMAIL_ADDRESS"},
    	}
    
    	// Define a custom info type to exclude email addresses
    	customInfotype := &dlppb.CustomInfoType{
    		InfoType: &dlppb.InfoType{
    			Name: "EMAIL_ADDRESS",
    		},
    		ExclusionType: dlppb.[CustomInfoType_EXCLUSION_TYPE_EXCLUDE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_CustomInfoType_EXCLUSION_TYPE_UNSPECIFIED_CustomInfoType_EXCLUSION_TYPE_EXCLUDE),
    	}
    
    	// Exclude EMAIL_ADDRESS matches
    	exclusionRule := &dlppb.ExclusionRule{
    		Type: &dlppb.ExclusionRule_ExcludeInfoTypes{
    			ExcludeInfoTypes: &dlppb.ExcludeInfoTypes{
    				InfoTypes: []*dlppb.InfoType{
    					{Name: "EMAIL_ADDRESS"},
    				},
    			},
    		},
    		MatchingType: dlppb.[MatchingType_MATCHING_TYPE_PARTIAL_MATCH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_MatchingType_MATCHING_TYPE_UNSPECIFIED_MatchingType_MATCHING_TYPE_FULL_MATCH_MatchingType_MATCHING_TYPE_PARTIAL_MATCH_MatchingType_MATCHING_TYPE_INVERSE_MATCH_MatchingType_MATCHING_TYPE_RULE_SPECIFIC),
    	}
    
    	// Construct a ruleSet that applies the exclusion rule to the DOMAIN_NAME infoType.
    	// If a DOMAIN_NAME match is part of an EMAIL_ADDRESS match, the DOMAIN_NAME match will
    	// be excluded.
    	ruleSet := &dlppb.InspectionRuleSet{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: "DOMAIN_NAME"},
    		},
    		Rules: []*dlppb.InspectionRule{
    			{
    				Type: &dlppb.InspectionRule_ExclusionRule{
    					ExclusionRule: exclusionRule,
    				},
    			},
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.InspectContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:   contentItem,
    		// Construct the Inspect request to be sent by the client.
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes: infoTypes,
    			CustomInfoTypes: []*dlppb.CustomInfoType{
    				customInfotype,
    			},
    			IncludeQuote: true,
    			RuleSet: []*dlppb.InspectionRuleSet{
    				ruleSet,
    			},
    		},
    	}
    
    	// Send the request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Process the results.
    	fmt.Fprintf(w, "Findings: %v\n", len(resp.Result.Findings))
    	for _, v := range resp.GetResult().Findings {
    		fmt.Fprintf(w, "Quote: %v\n", v.GetQuote())
    		fmt.Fprintf(w, "Infotype Name: %v\n", v.GetInfoType().GetName())
    		fmt.Fprintf(w, "Likelihood: %v\n", v.GetLikelihood())
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
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[ExclusionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.ExclusionType.html);
    import com.google.privacy.dlp.v2.[ExcludeInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExcludeInfoTypes.html);
    import com.google.privacy.dlp.v2.[ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html);
    import com.google.privacy.dlp.v2.[InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class InspectStringWithoutOverlap {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "example.com is a domain, james@example.org is an email.";
        inspectStringWithoutOverlap(projectId, textToInspect);
      }
    
      // Inspects the provided text, avoiding matches specified in the exclusion list.
      public static void inspectStringWithoutOverlap(String projectId, String textToInspect)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type and content to be inspected.
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(textToInspect))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
          List<InfoType> infoTypes = new ArrayList<>();
          for (String typeName : new String[] {"DOMAIN_NAME", "EMAIL_ADDRESS"}) {
            infoTypes.add([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(typeName).build());
          }
    
          // Define a custom info type to exclude email addresses
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder()
                  .setInfoType([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("EMAIL_ADDRESS"))
                  .[setExclusionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Builder_setExclusionType_com_google_privacy_dlp_v2_CustomInfoType_ExclusionType_)([ExclusionType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.ExclusionType.html).EXCLUSION_TYPE_EXCLUDE)
                  .build();
    
          // Exclude EMAIL_ADDRESS matches
          [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html) exclusionRule =
              [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html).newBuilder()
                  .setExcludeInfoTypes(
                      [ExcludeInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExcludeInfoTypes.html).newBuilder()
                          .addInfoTypes([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("EMAIL_ADDRESS")))
                  .setMatchingType([MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html).MATCHING_TYPE_PARTIAL_MATCH)
                  .build();
    
          // Construct a ruleset that applies the exclusion rule to the DOMAIN_NAME infotype.
          // If a DOMAIN_NAME match is part of an EMAIL_ADDRESS match, the DOMAIN_NAME match will
          // be excluded.
          [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html) ruleSet =
              [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html).newBuilder()
                  .addInfoTypes([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("DOMAIN_NAME"))
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().[setExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.Builder.html#com_google_privacy_dlp_v2_InspectionRule_Builder_setExclusionRule_com_google_privacy_dlp_v2_ExclusionRule_)(exclusionRule))
                  .build();
    
          // Construct the configuration for the Inspect request, including the ruleset.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .[addRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_)(ruleSet)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(config)
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The string to inspect
    // const string = 'example.com is a domain, james@example.org is an email.';
    
    async function inspectStringWithoutOverlap() {
      // Construct item to inspect
      const item = {value: string};
    
      // The infoTypes of information to match
      const infoTypes = [{name: 'DOMAIN_NAME'}, {name: 'EMAIL_ADDRESS'}];
    
      // Define a custom info type to exclude email addresses
      const customInfoTypes = [
        {
          infoType: {name: 'EMAIL_ADDRESS'},
          exclusionType:
            DLP.protos.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.custominfotype-class.html).[ExclusionType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.custominfotype.exclusiontype.html)
              .[EXCLUSION_TYPE_EXCLUDE](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.custominfotype.exclusiontype.html),
        },
      ];
    
      // Construct a exclusion rule
      const exclusionRule = {
        excludeInfoTypes: {
          infoTypes: [{name: 'EMAIL_ADDRESS'}],
        },
        matchingType:
          DLP.protos.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html)
            .[MATCHING_TYPE_PARTIAL_MATCH](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html),
      };
    
      // Construct a rule set with exclusions
      const ruleSet = [
        {
          infoTypes: [{name: 'DOMAIN_NAME'}],
          rules: [
            {
              exclusionRule: exclusionRule,
            },
          ],
        },
      ];
    
      // Construct the inspect configuration
      const inspectConfig = {
        infoTypes: infoTypes,
        customInfoTypes: customInfoTypes,
        ruleSet: ruleSet,
        includeQuote: true,
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: inspectConfig,
        item: item,
      };
    
      // Run request
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
    inspectStringWithoutOverlap();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType;
    use Google\Cloud\Dlp\V2\CustomInfoType\ExclusionType;
    use Google\Cloud\Dlp\V2\ExcludeInfoTypes;
    use Google\Cloud\Dlp\V2\ExclusionRule;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\InspectionRule;
    use Google\Cloud\Dlp\V2\InspectionRuleSet;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\MatchingType;
    
    /**
     * Inspect a string for sensitive data, omitting overlapping matches on domain and email
     * Omit matches on domain names that are part of email addresses in a DOMAIN_NAME detector scan.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect     The string to inspect.
     */
    function inspect_string_without_overlap(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $textToInspect = 'example.com is a domain, james@example.org is an email.'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new ContentItem())
            ->setValue($textToInspect);
    
        // Specify the type of info the inspection will look for.
        $domainName = (new InfoType())
            ->setName('DOMAIN_NAME');
        $emailAddress = (new InfoType())
            ->setName('EMAIL_ADDRESS');
        $infoTypes = [$domainName, $emailAddress];
    
        // Define a custom info type to exclude email addresses
        $customInfoType = (new CustomInfoType())
            ->setInfoType($emailAddress)
            ->setExclusionType(ExclusionType::EXCLUSION_TYPE_EXCLUDE);
    
        // Exclude EMAIL_ADDRESS matches
        $matchingType = MatchingType::MATCHING_TYPE_PARTIAL_MATCH;
    
        $exclusionRule = (new ExclusionRule())
            ->setMatchingType($matchingType)
            ->setExcludeInfoTypes((new ExcludeInfoTypes())
                ->setInfoTypes([$customInfoType->getInfoType()])
            );
    
        // Construct a ruleset that applies the exclusion rule to the DOMAIN_NAME infotype.
        // If a DOMAIN_NAME match is part of an EMAIL_ADDRESS match, the DOMAIN_NAME match will
        // be excluded.
        $inspectionRuleSet = (new InspectionRuleSet())
            ->setInfoTypes([$domainName])
            ->setRules([
                (new InspectionRule())
                    ->setExclusionRule($exclusionRule),
            ]);
    
        // Construct the configuration for the Inspect request, including the ruleset.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes($infoTypes)
            ->setCustomInfoTypes([$customInfoType])
            ->setIncludeQuote(true)
            ->setRuleSet([$inspectionRuleSet]);
    
        // Run request
        $inspectContentRequest = (new InspectContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->inspectContent($inspectContentRequest);
    
        // Print the results
        $findings = $response->getResult()->getFindings();
        if (count($findings) == 0) {
            printf('No findings.' . PHP_EOL);
        } else {
            printf('Findings:' . PHP_EOL);
            foreach ($findings as $finding) {
                printf('  Quote: %s' . PHP_EOL, $finding->getQuote());
                printf('  Info type: %s' . PHP_EOL, $finding->getInfoType()->getName());
                printf(
                    '  Likelihood: %s' . PHP_EOL,
                    Likelihood::name($finding->getLikelihood()));
            }
        }
    }

### Python

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import google.cloud.dlp
    
    
    def inspect_string_without_overlap(project: str, content_string: str) -> None:
        """Matches EMAIL_ADDRESS and DOMAIN_NAME, but DOMAIN_NAME is omitted
        if it overlaps with EMAIL_ADDRESS
    
        Uses the Data Loss Prevention API to omit matches of one infotype
        that overlap with another.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct a list of infoTypes for DLP to locate in `content_string`. See
        # https://cloud.google.com/dlp/docs/concepts-infotypes for more information
        # about supported infoTypes.
        info_types_to_locate = [{"name": "DOMAIN_NAME"}, {"name": "EMAIL_ADDRESS"}]
    
        # Define a custom info type to exclude email addresses
        custom_info_types = [
            {
                "info_type": {"name": "EMAIL_ADDRESS"},
                "exclusion_type": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[CustomInfoType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CustomInfoType.html).[ExclusionType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.CustomInfoType.ExclusionType.html).EXCLUSION_TYPE_EXCLUDE,
            }
        ]
    
        # Construct a rule set that will exclude DOMAIN_NAME matches
        # that overlap with EMAIL_ADDRESS matches
        rule_set = [
            {
                "info_types": [{"name": "DOMAIN_NAME"}],
                "rules": [
                    {
                        "exclusion_rule": {
                            "exclude_info_types": {
                                "info_types": [{"name": "EMAIL_ADDRESS"}]
                            },
                            "matching_type": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[MatchingType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.MatchingType.html).MATCHING_TYPE_PARTIAL_MATCH,
                        }
                    }
                ],
            }
        ]
    
        # Construct the configuration dictionary
        inspect_config = {
            "info_types": info_types_to_locate,
            "custom_info_types": custom_info_types,
            "rule_set": rule_set,
            "include_quote": True,
        }
    
        # Construct the `item`.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={"parent": parent, "inspect_config": inspect_config, "item": item}
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Quote: {finding.quote}")
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

### REST

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.
    
    
    ...
        "inspectConfig":{
          "infoTypes":[
            {
              "name":"DOMAIN_NAME"
            },
            {
              "name":"EMAIL_ADDRESS"
            }
          ],
          "customInfoTypes":[
            {
              "infoType":{
                "name":"EMAIL_ADDRESS"
              },
              "exclusionType":"EXCLUSION_TYPE_EXCLUDE"
            }
          ],
          "ruleSet":[
            {
              "infoTypes":[
                {
                  "name":"DOMAIN_NAME"
                }
              ],
              "rules":[
                {
                  "exclusionRule":{
                    "excludeInfoTypes":{
                      "infoTypes":[
                        {
                          "name":"EMAIL_ADDRESS"
                        }
                      ]
                    },
                    "matchingType": "MATCHING_TYPE_PARTIAL_MATCH"
                  }
                }
              ]
            }
          ]
        }
    ...
    

#### Omit matches if they are located near a string

The following example illustrates how to exclude matches on the `US_SOCIAL_SECURITY_NUMBER` infoType detector if the word "SKU" is within 10 characters before or 10 characters after the finding.

Because of the exclusion rule, this example doesn't classify `222-22-2222` as a possible US Social Security number.
    
    
    {
      "item": {
        "value": "The customer sent the product SKU 222-22-2222"
      },
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "US_SOCIAL_SECURITY_NUMBER"
          }
        ],
        "ruleSet": [
          {
            "infoTypes": [
              {
                "name": "US_SOCIAL_SECURITY_NUMBER"
              }
            ],
            "rules": [
              {
                "exclusionRule": {
                  "excludeByHotword": {
                    "hotwordRegex": {
                      "pattern": "(SKU)"
                    },
                    "proximity": {
                      "windowBefore": 10,
                      "windowAfter": 10
                    }
                  },
                  "matchingType": "MATCHING_TYPE_FULL_MATCH"
                }
              }
            ]
          }
        ],
        "includeQuote": true
      }
    }
    

#### Omit findings in an entire column of data

The following example illustrates how to exclude findings in an entire column of tabular data if the name of that column matches a regular expression. Here, any finding that matches the `US_SOCIAL_SECURITY_NUMBER` infoType detector is excluded from results if that finding is in the **Fake Social Security Number** column.

This example returns only `222-22-2222`, because `111-11-1111` is in the **Fake Social Security Number** column.
    
    
    {
      "item": {
        "table": {
          "headers": [
            {
              "name": "Fake Social Security Number"
            },
            {
              "name": "Real Social Security Number"
            }
          ],
          "rows": [
            {
              "values": [
                {
                  "stringValue": "111-11-1111"
                },
                {
                  "stringValue": "222-22-2222"
                }
              ]
            }
          ]
        }
      },
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "US_SOCIAL_SECURITY_NUMBER"
          }
        ],
        "includeQuote": true,
        "ruleSet": [
          {
            "infoTypes": [
              {
                "name": "US_SOCIAL_SECURITY_NUMBER"
              }
            ],
            "rules": [
              {
                "exclusionRule": {
                  "excludeByHotword": {
                    "hotwordRegex": {
                      "pattern": "(Fake Social Security Number)"
                    },
                    "proximity": {
                      "windowBefore": 1
                    }
                  },
                  "matchingType": "MATCHING_TYPE_FULL_MATCH"
                }
              }
            ]
          }
        ],
        "minLikelihood": "POSSIBLE"
      }
    }
    

#### Omit findings in images based on spatial relationships

The following JSON snippets illustrate how to configure Sensitive Data Protection to exclude findings in images based on their spatial relationship with other detected objects.

#### Exclude a person finding if it is part of a passport

This rule excludes person findings (`OBJECT_TYPE/PERSON`) when they are contained within a passport finding (`OBJECT_TYPE/PERSON/PASSPORT`).
    
    
    {
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "OBJECT_TYPE/PERSON"
          },
          {
            "name": "OBJECT_TYPE/PERSON/PASSPORT"
          }
        ],
        "ruleSet": [
          {
            "infoTypes": [
              {
                "name": "OBJECT_TYPE/PERSON"
              }
            ],
            "rules": [
              {
                "exclusionRule": {
                  "excludeByImageFindings": {
                    "infoTypes": [
                      {
                        "name": "OBJECT_TYPE/PERSON/PASSPORT"
                      }
                    ],
                    "imageContainmentType": {
                      "encloses": {}
                    }
                  },
                  "matchingType": "MATCHING_TYPE_RULE_SPECIFIC"
                }
              }
            ]
          }
        ]
      }
    }
    

#### Exclude a license plate finding if it contains a VIN

This rule excludes a finding of a license plate (`OBJECT_TYPE/LICENSE_PLATE`) if a `VEHICLE_IDENTIFICATION_NUMBER` finding is fully inside it.
    
    
    {
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "OBJECT_TYPE/LICENSE_PLATE"
          },
          {
            "name": "VEHICLE_IDENTIFICATION_NUMBER"
          }
        ],
        "ruleSet": [
          {
            "infoTypes": [
              {
                "name": "OBJECT_TYPE/LICENSE_PLATE"
              }
            ],
            "rules": [
              {
                "exclusionRule": {
                  "excludeByImageFindings": {
                    "infoTypes": [
                      {
                        "name": "VEHICLE_IDENTIFICATION_NUMBER"
                      }
                    ],
                    "imageContainmentType": {
                      "fullyInside": {}
                    }
                  },
                  "matchingType": "MATCHING_TYPE_RULE_SPECIFIC"
                }
              }
            ]
          }
        ]
      }
    }
    

## Hotword rules

Hotword rules are useful in situations like the following:

  * You want to change likelihood values assigned to scan matches based on the match's proximity to a hotword. For example, you want to set the likelihood value higher for matches on patient names depending on the names' proximity to the word "patient."
  * When inspecting structured, tabular data, you want to change likelihood values assigned to matches [based on a column header name](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood#match-column-values). For example, you want to set the likelihood value higher for `US_SOCIAL_SECURITY_NUMBER` when found in a column with header `ACCOUNT_ID`.



### Hotword rules API overview

Within Sensitive Data Protection's [`InspectionRule`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#InspectionRule) object, you specify a [`HotwordRule`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#HotwordRule) object, which adjusts the likelihood of findings within a certain proximity of hotwords.

`InspectionRule` objects are grouped as a "rule set" in an `InspectionRuleSet` object, along with a list of infoType detectors the rule set applies to. Rules within a rule set are applied in the order specified.

### Hotword rule example scenarios

The following code snippet illustrates how to configure a hotword rule.

#### Increase the likelihood of a PERSON_NAME match if there is the hotword "patient" nearby

The following JSON snippet and code in several languages illustrate using the [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) property for the purpose of scanning a medical database for patient names. You can use Sensitive Data Protection's built-in `PERSON_NAME` infoType detector, but that will cause Sensitive Data Protection to match on all names of people, not just names of patients. To fix this, you can include a hotword rule that looks for the word "patient" within a certain character proximity from the first character of potential matches. You can then assign findings matching this pattern a [likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood) of "very likely," since they correspond to your special criteria. Setting the minimum [`Likelihood`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood) to `VERY_LIKELY` within [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) ensures that only matches to this configuration are returned in findings.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using System;
    using static Google.Cloud.Dlp.V2.CustomInfoType.Types;
    
    public class InspectStringCustomHotword
    {
        public static InspectContentResponse Inspect(string projectId, string textToInspect, string customHotword)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var byteContentItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
            {
                Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8),
                Data = Google.Protobuf.ByteString.CopyFromUtf8(textToInspect)
            };
    
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html)
            {
                ByteItem = byteContentItem
            };
    
            var hotwordRule = new DetectionRule.Types.HotwordRule
            {
                HotwordRegex = new Regex { Pattern = customHotword },
                Proximity = new DetectionRule.Types.Proximity { WindowBefore = 50 },
                LikelihoodAdjustment = new DetectionRule.Types.LikelihoodAdjustment { FixedLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[VeryLikely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_VeryLikely) }
            };
    
            var infoType = new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" };
    
            var inspectionRuleSet = new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)
            {
                InfoTypes = { infoType },
                Rules = { new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { HotwordRule = hotwordRule } }
            };
    
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infoType },
                IncludeQuote = true,
                RuleSet = { inspectionRuleSet },
                MinLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[VeryLikely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_VeryLikely)
            };
    
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                Item = contentItem,
                InspectConfig = inspectConfig
            };
    
            var response = dlp.InspectContent(request);
    
            Console.WriteLine($"Findings: {response.Result.Findings.Count}");
            foreach (var f in response.Result.Findings)
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
    
    // inspectStringCustomHotWord inspects a string from sensitive data by using a custom hot word
    func inspectStringCustomHotWord(w io.Writer, projectID, textToInspect, customHotWord, infoTypeName string) error {
    	// projectID := "my-project-id"
    	// textToInspect := "patient name: John Doe"
    	// customHotWord := "patient"
    	// infoTypeName := "PERSON_NAME"
    
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
    
    	// Specify the type and content to be inspected.
    	contentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_ByteItem{
    			ByteItem: &dlppb.ByteContentItem{
    				Type: dlppb.[ByteContentItem_TEXT_UTF8](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL),
    				Data: []byte(textToInspect),
    			},
    		},
    	}
    
    	// Increase likelihood of matches that have customHotword nearby
    	hotwordRule := &dlppb.InspectionRule_HotwordRule{
    
    		HotwordRule: &dlppb.CustomInfoType_DetectionRule_HotwordRule{
    			HotwordRegex: &dlppb.CustomInfoType_Regex{
    				Pattern: customHotWord,
    			},
    			Proximity: &dlppb.CustomInfoType_DetectionRule_Proximity{
    				WindowBefore: 50,
    			},
    			LikelihoodAdjustment: &dlppb.CustomInfoType_DetectionRule_LikelihoodAdjustment{
    				Adjustment: &dlppb.CustomInfoType_DetectionRule_LikelihoodAdjustment_FixedLikelihood{
    					FixedLikelihood: dlppb.[Likelihood_VERY_LIKELY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    				},
    			},
    		},
    	}
    
    	// Construct a ruleset that applies the hotword rule to the PERSON_NAME infotype.
    	ruleSet := &dlppb.InspectionRuleSet{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: infoTypeName}, //"PERSON_NAME"
    		},
    		Rules: []*dlppb.InspectionRule{
    			{
    				Type: &dlppb.InspectionRule_HotwordRule{
    					HotwordRule: hotwordRule.HotwordRule,
    				},
    			},
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.InspectContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:   contentItem,
    		InspectConfig: &dlppb.InspectConfig{
    			InfoTypes: []*dlppb.InfoType{
    				{Name: infoTypeName}, //"PERSON_NAME"
    			},
    			IncludeQuote:  true,
    			MinLikelihood: dlppb.[Likelihood_VERY_LIKELY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    			RuleSet: []*dlppb.InspectionRuleSet{
    				ruleSet,
    			},
    		},
    	}
    
    	// Send the request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Parse the response and process results
    	fmt.Fprintf(w, "Findings: %v\n", len(resp.Result.Findings))
    	for _, v := range resp.GetResult().Findings {
    		fmt.Fprintf(w, "Quote: %v\n", v.GetQuote())
    		fmt.Fprintf(w, "Infotype Name: %v\n", v.GetInfoType().GetName())
    		fmt.Fprintf(w, "Likelihood: %v\n", v.GetLikelihood())
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
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[DetectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.html).[HotwordRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[DetectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.html).[LikelihoodAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[DetectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.html).[Proximity](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html);
    import com.google.privacy.dlp.v2.[InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class InspectStringCustomHotword {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "patient name: John Doe";
        String customHotword = "patient";
        inspectStringCustomHotword(projectId, textToInspect, customHotword);
      }
    
      // Inspects the provided text.
      public static void inspectStringCustomHotword(
          String projectId, String textToInspect, String customHotword) throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type and content to be inspected.
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(textToInspect))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build();
    
          // Increase likelihood of matches that have customHotword nearby
          [HotwordRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html) hotwordRule =
              [HotwordRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html).newBuilder()
                  .setHotwordRegex([Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html).newBuilder().[setPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)(customHotword))
                  .setProximity([Proximity](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.html).newBuilder().[setWindowBefore](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_DetectionRule_Proximity_Builder_setWindowBefore_int_)(50))
                  .setLikelihoodAdjustment(
                      [LikelihoodAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.html).newBuilder().[setFixedLikelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_DetectionRule_LikelihoodAdjustment_Builder_setFixedLikelihood_com_google_privacy_dlp_v2_Likelihood_)([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).VERY_LIKELY))
                  .build();
    
          // Construct a ruleset that applies the hotword rule to the PERSON_NAME infotype.
          [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html) ruleSet =
              [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html).newBuilder()
                  .addInfoTypes([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME").build())
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().setHotwordRule(hotwordRule))
                  .build();
    
          // Construct the configuration for the Inspect request.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addInfoTypes([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME").build())
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .[addRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_)(ruleSet)
                  .setMinLikelihood([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).VERY_LIKELY)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(config)
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The string to inspect
    // const string = 'patient name: John Doe';
    
    // Custom hotward
    // const customHotword = 'patient';
    
    async function inspectStringCustomHotword() {
      // Specify the type and content to be inspected.
      const item = {
        byteItem: {
          type: DLP.protos.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem-class.html).[BytesType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html)
            .[TEXT_UTF8](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html),
          data: Buffer.from(string, 'utf-8'),
        },
      };
    
      // Increase likelihood of matches that have customHotword nearby.
      const hotwordRule = {
        hotwordRegex: {
          pattern: customHotword,
        },
        proximity: {
          windowBefore: 50,
        },
        likelihoodAdjustment: {
          fixedLikelihood:
            DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[VERY_LIKELY](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
        },
      };
    
      // Construct a ruleset that applies the hotword rule to the PERSON_NAME infotype.
      const ruleSet = [
        {
          infoTypes: [{name: 'PERSON_NAME'}],
          rules: [
            {
              hotwordRule: hotwordRule,
            },
          ],
        },
      ];
    
      // Construct the configuration for the Inspect request.
      const inspectConfig = {
        infoTypes: [{name: 'PERSON_NAME'}],
        ruleSet: ruleSet,
        includeQuote: true,
      };
    
      // Construct the Inspect request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: inspectConfig,
        item: item,
      };
    
      // Use the client to send the API request.
      const [response] = await dlp.inspectContent(request);
    
      // Print findings.
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
    inspectStringCustomHotword();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType\DetectionRule\HotwordRule;
    use Google\Cloud\Dlp\V2\CustomInfoType\DetectionRule\LikelihoodAdjustment;
    use Google\Cloud\Dlp\V2\CustomInfoType\DetectionRule\Proximity;
    use Google\Cloud\Dlp\V2\CustomInfoType\Regex;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\InspectionRule;
    use Google\Cloud\Dlp\V2\InspectionRuleSet;
    use Google\Cloud\Dlp\V2\Likelihood;
    
    /**
     * Inspect a string from sensitive data by using a custom hotword
     * Increase the likelihood of a PERSON_NAME match if there is the hotword "patient" nearby. Illustrates using the InspectConfig property for the purpose of scanning a medical database for patient names. You can use Cloud DLP's built-in PERSON_NAME infoType detector, but that causes Cloud DLP to match on all names of people, not just names of patients. To fix this, you can include a hotword rule that looks for the word "patient" within a certain character proximity from the first character of potential matches. You can then assign findings that match this pattern a likelihood of "very likely," since they correspond to your special criteria. Setting the minimum likelihood to VERY_LIKELY within InspectConfig ensures that only matches to this configuration are returned in findings.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect     The string to inspect.
     */
    function inspect_string_custom_hotword(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $textToInspect = 'patient name: John Doe'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new ContentItem())
            ->setValue($textToInspect);
    
        // Construct hotword rules
        $hotwordRule = (new HotwordRule())
            ->setHotwordRegex(
                (new Regex())
                    ->setPattern('patient')
            )
            ->setProximity(
                (new Proximity())
                    ->setWindowBefore(50)
            )
            ->setLikelihoodAdjustment(
                (new LikelihoodAdjustment())
                    ->setFixedLikelihood(Likelihood::VERY_LIKELY)
            );
    
        // Construct a ruleset that applies the hotword rule to the PERSON_NAME infotype.
        $personName = (new InfoType())
            ->setName('PERSON_NAME');
        $inspectionRuleSet = (new InspectionRuleSet())
            ->setInfoTypes([$personName])
            ->setRules([
                (new InspectionRule())
                    ->setHotwordRule($hotwordRule),
            ]);
    
        // Construct the configuration for the Inspect request, including the ruleset.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes([$personName])
            ->setIncludeQuote(true)
            ->setRuleSet([$inspectionRuleSet])
            ->setMinLikelihood(Likelihood::VERY_LIKELY);
    
        // Run request
        $inspectContentRequest = (new InspectContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->inspectContent($inspectContentRequest);
    
        // Print the results
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
    
    
    import google.cloud.dlp
    
    
    def inspect_string_w_custom_hotword(
        project: str, content_string: str, custom_hotword: str = "patient"
    ) -> None:
        """Uses the Data Loss Prevention API increase likelihood for matches on
           PERSON_NAME if the user specified custom hot-word is present. Only
           includes findings with the increased likelihood by setting a minimum
           likelihood threshold of VERY_LIKELY.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
            custom_hotword: The custom hot-word used for likelihood boosting.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct a rule set with caller provided hotword, with a likelihood
        # boost to VERY_LIKELY when the hotword are present within the 50 character-
        # window preceding the PII finding.
        hotword_rule = {
            "hotword_regex": {"pattern": custom_hotword},
            "likelihood_adjustment": {
                "fixed_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).VERY_LIKELY
            },
            "proximity": {"window_before": 50},
        }
    
        rule_set = [
            {
                "info_types": [{"name": "PERSON_NAME"}],
                "rules": [{"hotword_rule": hotword_rule}],
            }
        ]
    
        # Construct the configuration dictionary with the custom regex info type.
        inspect_config = {
            "rule_set": rule_set,
            "min_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).VERY_LIKELY,
            "include_quote": True,
        }
    
        # Construct the `item`.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={"parent": parent, "inspect_config": inspect_config, "item": item}
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Quote: {finding.quote}")
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

### REST

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.
    
    
    ...
      "inspectConfig":{
        "infoTypes":[
          {
            "name":"PERSON_NAME"
          }
        ],
        "ruleSet":[
          {
            "infoTypes":[
              {
                "name":"PERSON_NAME"
              }
            ],
            "rules":[
              {
                "hotwordRule":{
                  "hotwordRegex":{
                    "pattern":"patient"
                  },
                  "proximity":{
                    "windowBefore":50
                  },
                  "likelihoodAdjustment":{
                    "fixedLikelihood":"VERY_LIKELY"
                  }
                }
              }
            ]
          }
        ],
        "minLikelihood":"VERY_LIKELY"
      }
    ...
    

For more detailed information about hotwords, see [Customizing match likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood).

## Adjustment rules

Adjustment rules can help you refine detection accuracy by increasing (also called _boosting_) or decreasing the likelihood values of findings based on the context in which they appear.

Adjustment rules are useful in situations like the following:

  * You want to change the likelihood value of a target infoType finding if the finding overlaps with a context infoType finding. For example, increase the likelihood values of `PERSON_NAME` findings that are detected in documents that match `DOCUMENT_TYPE/CONTEXT/HEALTH`.

  * You want to change the likelihood value of a target infoType finding based on its spatial relationship with other detected findings in the image. For example, increase the likelihood values of `GENERIC_ID` findings that are detected within images that match `OBJECT_TYPE/PERSON/PHOTO_ID_CARD`.




### Adjustment rules API overview

Sensitive Data Protection defines an adjustment rule in the [`AdjustmentRule`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#adjustmentrule) object. Within `AdjustmentRule`, you specify the following:

  * One of the following:

    * An [`AdjustByMatchingInfoTypes`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#adjustbymatchinginfotypes) object, which adjusts the likelihood value of a target infoType finding if that finding overlaps a finding of a context infoType. This object contains the following:

      * A list of context infoTypes, which are used to determine whether to adjust the target infoType finding.
      * A `min_likelihood` value for the context infoTypes. If the likelihood value of any detected context finding is lower than this value, Sensitive Data Protection doesn't adjust the likelihood of the target finding.
      * A [`matching_type`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#matchingtype) value which must be set to `MATCHING_TYPE_PARTIAL_MATCH`.
    * An [`AdjustByImageFindings`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#adjustbyimagefindings) object, which adjusts the likelihood value of a target infoType finding if the bounding box of a context infoType has the specified relationship with the target infoType finding. This object contains the following:

      * A list of context infoTypes, which are used to determine whether to adjust the target infoType finding.

      * An [`ImageContainmentType`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#imagecontainmenttype) object, which specifies the required spatial relationship between the bounding boxes of the target and context findings. If this requirement isn't met, Sensitive Data Protection doesn't adjust the likelihood of the target infoType finding.

      * A `min_likelihood` value for the context infoTypes. If the likelihood value of any detected context finding is lower than this value, Sensitive Data Protection doesn't adjust the likelihood of the target finding.

  * A [`likelihood_adjustment`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#likelihoodadjustment) object, which specifies the new likelihood as either a fixed value or a relative adjustment.




### Adjustment rule example scenarios

The following JSON snippets illustrate how to configure adjustment rules for various scenarios.

#### Boost the likelihood of person name when used in health document

The following example boosts the likelihood value of a `PERSON_NAME` finding to `VERY_LIKELY` if the finding overlaps with a `DOCUMENT_TYPE/CONTEXT/HEALTH` finding.
    
    
    {
      "parent": "projects/PROJECT_ID",
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "PERSON_NAME"
          },
          {
            "name": "DOCUMENT_TYPE/CONTEXT/HEALTH"
          }
        ],
        "ruleSet": [
          {
            "infoTypes": [
              {
                "name": "PERSON_NAME"
              }
            ],
            "rules": [
              {
                "adjustmentRule": {
                  "adjustByMatchingInfoTypes": {
                    "infoTypes": [
                      {
                        "name": "DOCUMENT_TYPE/CONTEXT/HEALTH"
                      }
                    ],
                    "minLikelihood": "POSSIBLE",
                    "matchingType": "MATCHING_TYPE_PARTIAL_MATCH"
                  },
                  "likelihoodAdjustment": {
                    "fixedLikelihood": "VERY_LIKELY"
                  }
                }
              }
            ]
          }
        ]
      },
      "item": {
        "value": "My name is John and my arm is broken."
      }
    }
    

Replace `PROJECT_ID` with the ID of the project associated with your request.

#### Boost the likelihood of person name in a health document and exclude the health document

The following example boosts the likelihood value of a `PERSON_NAME` finding to `VERY_LIKELY` if the finding overlaps with a `DOCUMENT_TYPE/CONTEXT/HEALTH` finding. To reduce noise, this example specifies a second rule, which excludes `DOCUMENT_TYPE/CONTEXT/HEALTH` findings from inspection results.

The order in which the rules in a ruleset are specified is important. In this example, the adjustment rule is specified before the exclusion rule, so that the `DOCUMENT_TYPE/CONTEXT/HEALTH` findings can be used to provide context to the adjustment rule. If you specify the exclusion rule first, then the `DOCUMENT_TYPE/CONTEXT/HEALTH` findings are excluded from the result set before they can be used to provide context to the adjustment rule.
    
    
    {
      "parent": "projects/PROJECT_ID",
      "inspectConfig": {
        "infoTypes": [{
          "name": "PERSON_NAME"
        }, {
          "name": "DOCUMENT_TYPE/CONTEXT/HEALTH"
        }],
        "minLikelihood": "VERY_UNLIKELY",
        "ruleSet": [{
          "infoTypes": [{
            "name": "PERSON_NAME"
          }],
          "rules": [{
            "adjustmentRule": {
              "adjustByMatchingInfoTypes": {
                "infoTypes": [{
                  "name": "DOCUMENT_TYPE/CONTEXT/HEALTH"
                }],
                "minLikelihood": "VERY_UNLIKELY",
                "matchingType": "MATCHING_TYPE_PARTIAL_MATCH"
              },
              "likelihoodAdjustment": {
                "fixedLikelihood": "VERY_LIKELY"
              }
            }
          }]
        }, {
          "infoTypes": [{
            "name": "DOCUMENT_TYPE/CONTEXT/HEALTH"
          }],
          "rules": [{
            "exclusionRule": {
              "excludeInfoTypes": {
                "infoTypes": [{
                  "name": "DOCUMENT_TYPE/CONTEXT/HEALTH"
                }]
              },
              "matchingType": "MATCHING_TYPE_PARTIAL_MATCH"
            }
          }]
        }]
      },
      "item": {
        "value": "My name is John and my arm is broken."
      }
    }
    

Replace `PROJECT_ID` with the ID of the project associated with your request.

#### Boost the likelihood of a person on a photo ID card

The following example boosts the likelihood value of an `OBJECT_TYPE/PERSON` finding to `VERY_LIKELY` if it appears within the bounding box of an `OBJECT_TYPE/PERSON/PHOTO_ID_CARD` finding.
    
    
    ...
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "OBJECT_TYPE/PERSON"
          },
          {
            "name": "OBJECT_TYPE/PERSON/PHOTO_ID_CARD"
          }
        ],
        "ruleSet": [
          {
            "infoTypes": [
              {
                "name": "OBJECT_TYPE/PERSON"
              }
            ],
            "rules": [
              {
                "adjustmentRule": {
                  "adjustByImageFindings": {
                    "infoTypes": [
                      {
                        "name": "OBJECT_TYPE/PERSON/PHOTO_ID_CARD"
                      }
                    ],
                    "imageContainmentType": {
                      "encloses": {}
                    },
                    "minLikelihood": "POSSIBLE"
                  },
                  "likelihoodAdjustment": {
                    "fixedLikelihood": "VERY_LIKELY"
                  }
                }
              }
            ]
          }
        ]
      }
    ...
    

#### Boost the likelihood of a passport that contains personal identifiers

The following example boosts the likelihood value of an `OBJECT_TYPE/PERSON/PASSPORT` finding to `VERY_LIKELY` if a `PERSON_NAME` or `DATE_OF_BIRTH` finding is fully inside it.
    
    
    ...
      "inspectConfig": {
        "infoTypes": [
          {
            "name": "OBJECT_TYPE/PERSON/PASSPORT"
          },
          {
            "name": "PERSON_NAME"
          },
          {
            "name": "DATE_OF_BIRTH"
          }
        ],
        "ruleSet": [
          {
            "infoTypes": [
              {
                "name": "OBJECT_TYPE/PERSON/PASSPORT"
              }
            ],
            "rules": [
              {
                "adjustmentRule": {
                  "adjustByImageFindings": {
                    "infoTypes": [
                      {
                        "name": "PERSON_NAME"
                      },
                      {
                        "name": "DATE_OF_BIRTH"
                      }
                    ],
                    "imageContainmentType": {
                      "fullyInside": {}
                    },
                    "minLikelihood": "POSSIBLE"
                  },
                  "likelihoodAdjustment": {
                    "fixedLikelihood": "VERY_LIKELY"
                  }
                }
              }
            ]
          }
        ]
      }
    ...
    

## Multiple inspection rules scenario

The following [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) JSON snippet and code in several languages illustrate applying both exclusion and hotword rules. This snippet's rule set includes both hotword rules and dictionary and regex exclusion rules. Notice that the four rules are specified in an array within the `rules` element.

**Important:** The code on this page requires that you first set up a Sensitive Data Protection client. For more information about installing and creating a Sensitive Data Protection client, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/libraries). (Sending JSON to Sensitive Data Protection REST endpoints does not require a client library.)

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using System.Text.RegularExpressions;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using static Google.Cloud.Dlp.V2.CustomInfoType.Types;
    
    public class InspectStringMultipleRules
    {
        public static InspectContentResponse Inspect(string projectId, string textToInspect)
        {
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            var byteContentItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
            {
                Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8),
                Data = Google.Protobuf.ByteString.CopyFromUtf8(textToInspect)
            };
    
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html)
            {
                ByteItem = byteContentItem
            };
    
            var patientRule = new DetectionRule.Types.HotwordRule
            {
                HotwordRegex = new CustomInfoType.Types.Regex { Pattern = "patient" },
                Proximity = new DetectionRule.Types.Proximity { WindowBefore = 10 },
                LikelihoodAdjustment = new DetectionRule.Types.LikelihoodAdjustment { FixedLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[VeryLikely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_VeryLikely) }
            };
    
            var doctorRule = new DetectionRule.Types.HotwordRule
            {
                HotwordRegex = new CustomInfoType.Types.Regex { Pattern = "doctor" },
                Proximity = new DetectionRule.Types.Proximity { WindowBefore = 10 },
                LikelihoodAdjustment = new DetectionRule.Types.LikelihoodAdjustment { FixedLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Unlikely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Unlikely) }
            };
    
            // Construct exclusion rules
            var quasimodoRule = new [ExclusionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExclusionRule.html)
            {
                Dictionary = new Dictionary { WordList = new Dictionary.Types.WordList { Words = { "Quasimodo" } } },
                MatchingType = [MatchingType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html).[PartialMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html#Google_Cloud_Dlp_V2_MatchingType_PartialMatch)
            };
    
            var redactedRule = new [ExclusionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ExclusionRule.html)
            {
                Regex = new CustomInfoType.Types.Regex { Pattern = "REDACTED" },
                MatchingType = [MatchingType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html).[PartialMatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.MatchingType.html#Google_Cloud_Dlp_V2_MatchingType_PartialMatch)
            };
    
            var infoType = new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "PERSON_NAME" };
    
            var inspectionRuleSet = new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)
            {
                InfoTypes = { infoType },
                Rules =
                {
                    new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { HotwordRule = patientRule },
                    new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { HotwordRule = doctorRule},
                    new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { ExclusionRule = quasimodoRule },
                    new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html) { ExclusionRule = redactedRule }
                }
            };
    
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                InfoTypes = { infoType },
                IncludeQuote = true,
                RuleSet = { inspectionRuleSet }
            };
    
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                Parent = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global").ToString(),
                Item = contentItem,
                InspectConfig = inspectConfig
            };
    
            var response = dlp.InspectContent(request);
    
            Console.WriteLine($"Findings: {response.Result.Findings.Count}");
            foreach (var f in response.Result.Findings)
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
    
    // inspectStringMultipleRules inspects the provided text,
    // avoiding matches specified in the exclusion list.
    // this function implements the both exclusion and hot word rules.
    func inspectStringMultipleRules(w io.Writer, projectID, textToInspect string) error {
    	// projectID := "my-project-id"
    	// textToInspect := "patient: Jane Doe"
    
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
    
    	// Specify the type and content to be inspected.
    	ContentItem := &dlppb.ContentItem{
    		DataItem: &dlppb.ContentItem_ByteItem{
    			ByteItem: &dlppb.ByteContentItem{
    				Type: dlppb.[ByteContentItem_TEXT_UTF8](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_ByteContentItem_BYTES_TYPE_UNSPECIFIED_ByteContentItem_IMAGE_ByteContentItem_IMAGE_JPEG_ByteContentItem_IMAGE_BMP_ByteContentItem_IMAGE_PNG_ByteContentItem_IMAGE_SVG_ByteContentItem_TEXT_UTF8_ByteContentItem_WORD_DOCUMENT_ByteContentItem_PDF_ByteContentItem_POWERPOINT_DOCUMENT_ByteContentItem_EXCEL_DOCUMENT_ByteContentItem_AVRO_ByteContentItem_CSV_ByteContentItem_TSV_ByteContentItem_AUDIO_ByteContentItem_VIDEO_ByteContentItem_EXECUTABLE_ByteContentItem_AI_MODEL),
    				Data: []byte(textToInspect),
    			},
    		},
    	}
    
    	// Construct the rule that adjust the likelihood of findings
    	// within a certain proximity of hot-word("patient").
    	patientRule := &dlppb.InspectionRule_HotwordRule{
    		HotwordRule: &dlppb.CustomInfoType_DetectionRule_HotwordRule{
    			HotwordRegex: &dlppb.CustomInfoType_Regex{
    				Pattern: "patient",
    			},
    			Proximity: &dlppb.CustomInfoType_DetectionRule_Proximity{
    				WindowBefore: 10,
    			},
    			LikelihoodAdjustment: &dlppb.CustomInfoType_DetectionRule_LikelihoodAdjustment{
    				Adjustment: &dlppb.CustomInfoType_DetectionRule_LikelihoodAdjustment_FixedLikelihood{
    					FixedLikelihood: dlppb.[Likelihood_VERY_LIKELY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    				},
    			},
    		},
    	}
    
    	// Construct the rule that adjust the likelihood of findings
    	// within a certain proximity of hot-word("doctor").
    	doctorRule := &dlppb.InspectionRule_HotwordRule{
    		HotwordRule: &dlppb.CustomInfoType_DetectionRule_HotwordRule{
    			HotwordRegex: &dlppb.CustomInfoType_Regex{
    				Pattern: "doctor",
    			},
    			Proximity: &dlppb.CustomInfoType_DetectionRule_Proximity{
    				WindowBefore: 10,
    			},
    			LikelihoodAdjustment: &dlppb.CustomInfoType_DetectionRule_LikelihoodAdjustment{
    				Adjustment: &dlppb.CustomInfoType_DetectionRule_LikelihoodAdjustment_FixedLikelihood{
    					FixedLikelihood: dlppb.[Likelihood_UNLIKELY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    				},
    			},
    		},
    	}
    
    	// Construct the exclusion rule that avoids the matches for the specified word list.
    	quasimodoRule := &dlppb.ExclusionRule{
    		Type: &dlppb.ExclusionRule_Dictionary{
    			Dictionary: &dlppb.CustomInfoType_Dictionary{
    				Source: &dlppb.CustomInfoType_Dictionary_WordList_{
    					WordList: &dlppb.CustomInfoType_Dictionary_WordList{
    						Words: []string{"Quasimodo"},
    					},
    				},
    			},
    		},
    		MatchingType: dlppb.[MatchingType_MATCHING_TYPE_PARTIAL_MATCH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_MatchingType_MATCHING_TYPE_UNSPECIFIED_MatchingType_MATCHING_TYPE_FULL_MATCH_MatchingType_MATCHING_TYPE_PARTIAL_MATCH_MatchingType_MATCHING_TYPE_INVERSE_MATCH_MatchingType_MATCHING_TYPE_RULE_SPECIFIC),
    	}
    
    	// Construct the exclusion rule that avoids the matches for the specified regex pattern.
    	redactedRule := &dlppb.ExclusionRule{
    		Type: &dlppb.ExclusionRule_Regex{
    			Regex: &dlppb.CustomInfoType_Regex{
    				Pattern: "REDACTED",
    			},
    		},
    		MatchingType: dlppb.[MatchingType_MATCHING_TYPE_PARTIAL_MATCH](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_MatchingType_MATCHING_TYPE_UNSPECIFIED_MatchingType_MATCHING_TYPE_FULL_MATCH_MatchingType_MATCHING_TYPE_PARTIAL_MATCH_MatchingType_MATCHING_TYPE_INVERSE_MATCH_MatchingType_MATCHING_TYPE_RULE_SPECIFIC),
    	}
    
    	// Construct a ruleSet that applies the rules to the PERSON_NAME infoType.
    	ruleSet := &dlppb.InspectionRuleSet{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: "PERSON_NAME"},
    		},
    		Rules: []*dlppb.InspectionRule{
    			{Type: &dlppb.InspectionRule_HotwordRule{HotwordRule: doctorRule.HotwordRule}},
    			{Type: &dlppb.InspectionRule_HotwordRule{HotwordRule: patientRule.HotwordRule}},
    			{Type: &dlppb.InspectionRule_ExclusionRule{ExclusionRule: quasimodoRule}},
    			{Type: &dlppb.InspectionRule_ExclusionRule{ExclusionRule: redactedRule}},
    		},
    	}
    
    	// Construct the configuration for the Inspect request, including the ruleSet.
    	inspectConfig := &dlppb.InspectConfig{
    		InfoTypes: []*dlppb.InfoType{
    			{Name: "PERSON_NAME"},
    		},
    		IncludeQuote: true,
    		RuleSet: []*dlppb.InspectionRuleSet{
    			ruleSet,
    		},
    	}
    
    	// Create and send the request.
    	req := &dlppb.InspectContentRequest{
    		Parent:        fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:          ContentItem,
    		InspectConfig: inspectConfig,
    	}
    
    	// Send the request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Process the results.
    	fmt.Fprintf(w, "Findings: %v\n", len(resp.Result.Findings))
    	for _, v := range resp.GetResult().Findings {
    		fmt.Fprintf(w, "Quote: %v\n", v.GetQuote())
    		fmt.Fprintf(w, "Infotype Name: %v\n", v.GetInfoType().GetName())
    		fmt.Fprintf(w, "Likelihood: %v\n", v.GetLikelihood())
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
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[DetectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.html).[HotwordRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[DetectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.html).[LikelihoodAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[DetectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.html).[Proximity](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).[WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html);
    import com.google.privacy.dlp.v2.[ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html);
    import com.google.privacy.dlp.v2.[InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    
    public class InspectStringMultipleRules {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "patient: Jane Doe";
        inspectStringMultipleRules(projectId, textToInspect);
      }
    
      // Inspects the provided text, avoiding matches specified in the exclusion list.
      public static void inspectStringMultipleRules(String projectId, String textToInspect)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify the type and content to be inspected.
          [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html) byteItem =
              [ByteContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.html).newBuilder()
                  .setType([BytesType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.BytesType.html).TEXT_UTF8)
                  .[setData](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ByteContentItem.Builder.html#com_google_privacy_dlp_v2_ByteContentItem_Builder_setData_com_google_protobuf_ByteString_)([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFromUtf8](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFromUtf8_java_lang_String_)(textToInspect))
                  .build();
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) item = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setByteItem(byteItem).build();
    
          // Construct hotword rules
          [HotwordRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html) patientRule =
              [HotwordRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html).newBuilder()
                  .setHotwordRegex([Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html).newBuilder().[setPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)("patient"))
                  .setProximity([Proximity](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.html).newBuilder().[setWindowBefore](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_DetectionRule_Proximity_Builder_setWindowBefore_int_)(10))
                  .setLikelihoodAdjustment(
                      [LikelihoodAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.html).newBuilder().[setFixedLikelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_DetectionRule_LikelihoodAdjustment_Builder_setFixedLikelihood_com_google_privacy_dlp_v2_Likelihood_)([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).VERY_LIKELY))
                  .build();
    
          [HotwordRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html) doctorRule =
              [HotwordRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html).newBuilder()
                  .setHotwordRegex([Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html).newBuilder().[setPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)("doctor"))
                  .setProximity([Proximity](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.html).newBuilder().[setWindowBefore](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_DetectionRule_Proximity_Builder_setWindowBefore_int_)(10))
                  .setLikelihoodAdjustment(
                      [LikelihoodAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.html).newBuilder().[setFixedLikelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_DetectionRule_LikelihoodAdjustment_Builder_setFixedLikelihood_com_google_privacy_dlp_v2_Likelihood_)([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).UNLIKELY))
                  .build();
    
          // Construct exclusion rules
          [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html) quasimodoRule =
              [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html).newBuilder()
                  .setDictionary(
                      [Dictionary](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.html).newBuilder().setWordList([WordList](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.html).newBuilder().[addWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Dictionary.WordList.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Dictionary_WordList_Builder_addWords_java_lang_String_)("Quasimodo")))
                  .setMatchingType([MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html).MATCHING_TYPE_PARTIAL_MATCH)
                  .build();
    
          [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html) redactedRule =
              [ExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ExclusionRule.html).newBuilder()
                  .setRegex([Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html).newBuilder().[setPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)("REDACTED"))
                  .setMatchingType([MatchingType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.MatchingType.html).MATCHING_TYPE_PARTIAL_MATCH)
                  .build();
    
          // Construct a ruleset that applies the rules to the PERSON_NAME infotype.
          [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html) ruleSet =
              [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html).newBuilder()
                  .addInfoTypes([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME"))
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().setHotwordRule(patientRule))
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().setHotwordRule(doctorRule))
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().[setExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.Builder.html#com_google_privacy_dlp_v2_InspectionRule_Builder_setExclusionRule_com_google_privacy_dlp_v2_ExclusionRule_)(quasimodoRule))
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().[setExclusionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.Builder.html#com_google_privacy_dlp_v2_InspectionRule_Builder_setExclusionRule_com_google_privacy_dlp_v2_ExclusionRule_)(redactedRule))
                  .build();
    
          // Construct the configuration for the Inspect request, including the ruleset.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .addInfoTypes([InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("PERSON_NAME"))
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .[addRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_)(ruleSet)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(item)
                  .setInspectConfig(config)
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
    
    
    // Imports the Google Cloud Data Loss Prevention library
    const DLP = require('[@google-cloud/dlp](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)');
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under
    // const projectId = 'my-project';
    
    // The string to inspect
    // const string = 'patient: Jane Doe';
    
    async function inspectStringMultipleRules() {
      // Construct item to inspect
      const item = {value: string};
    
      // Construct hotword rules
      const patientRule = {
        hotwordRegex: {pattern: 'patient'},
        proximity: {windowBefore: 10},
        likelihoodAdjustment: {
          fixedLikelihood:
            DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[VERY_LIKELY](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
        },
      };
    
      const doctorRule = {
        hotwordRegex: {pattern: 'doctor'},
        proximity: {windowBefore: 10},
        likelihoodAdjustment: {
          fixedLikelihood: DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[UNLIKELY](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
        },
      };
    
      // Construct exclusion rules
      const quasimodoRule = {
        dictionary: {wordList: {words: ['quasimodo']}},
        matchingType:
          DLP.protos.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html)
            .[MATCHING_TYPE_PARTIAL_MATCH](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html),
      };
    
      const redactedRule = {
        regex: {pattern: 'REDACTED'},
        matchingType:
          DLP.protos.google.privacy.dlp.v2.[MatchingType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html)
            .[MATCHING_TYPE_PARTIAL_MATCH](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.matchingtype.html),
      };
    
      // The infoTypes of information to match
      const infoTypes = [{name: 'PERSON_NAME'}];
    
      // Construct a ruleset that applies the rules to the PERSON_NAME infotype.
      const ruleSet = [
        {
          infoTypes: infoTypes,
          rules: [
            {hotwordRule: patientRule},
            {hotwordRule: doctorRule},
            {exclusionRule: quasimodoRule},
            {exclusionRule: redactedRule},
          ],
        },
      ];
    
      // Construct the configuration for the Inspect request, including the ruleset.
      const inspectConfig = {
        infoTypes: infoTypes,
        ruleSet: ruleSet,
        includeQuote: true,
      };
    
      // Construct the Inspect request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: inspectConfig,
        item: item,
      };
    
      // Use the client to send the API request.
      const [response] = await dlp.inspectContent(request);
    
      // Print findings.
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
    inspectStringMultipleRules();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType\DetectionRule\HotwordRule;
    use Google\Cloud\Dlp\V2\CustomInfoType\DetectionRule\LikelihoodAdjustment;
    use Google\Cloud\Dlp\V2\CustomInfoType\DetectionRule\Proximity;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary;
    use Google\Cloud\Dlp\V2\CustomInfoType\Dictionary\WordList;
    use Google\Cloud\Dlp\V2\CustomInfoType\Regex;
    use Google\Cloud\Dlp\V2\ExclusionRule;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\InspectionRule;
    use Google\Cloud\Dlp\V2\InspectionRuleSet;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\MatchingType;
    
    /**
     * Inspect a string for sensitive data by using multiple rules
     * Illustrates applying both exclusion and hotword rules. This snippet's rule set includes both hotword rules and dictionary and regex exclusion rules. Notice that the four rules are specified in an array within the rules element.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect     The string to inspect.
     */
    function inspect_string_multiple_rules(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $textToInspect = 'patient: Jane Doe'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new ContentItem())
            ->setValue($textToInspect);
    
        // Construct hotword rules
        $patientRule = (new HotwordRule())
            ->setHotwordRegex((new Regex())
                ->setPattern('patient'))
            ->setProximity((new Proximity())
                ->setWindowBefore(10))
            ->setLikelihoodAdjustment((new LikelihoodAdjustment())
                ->setFixedLikelihood(Likelihood::VERY_LIKELY));
    
        $doctorRule = (new HotwordRule())
            ->setHotwordRegex((new Regex())
                ->setPattern('doctor'))
            ->setProximity((new Proximity())
                ->setWindowBefore(10))
            ->setLikelihoodAdjustment((new LikelihoodAdjustment())
                ->setFixedLikelihood(Likelihood::VERY_UNLIKELY));
    
        // Construct exclusion rules
        $wordList = (new Dictionary())
            ->setWordList((new WordList())
                ->setWords(['Quasimodo']));
    
        $quasimodoRule = (new ExclusionRule())
            ->setMatchingType(MatchingType::MATCHING_TYPE_PARTIAL_MATCH)
            ->setDictionary($wordList);
    
        $redactedRule = (new ExclusionRule())
            ->setMatchingType(MatchingType::MATCHING_TYPE_PARTIAL_MATCH)
            ->setRegex((new Regex())
                ->setPattern('REDACTED'));
    
        // Specify the exclusion rule and build-in info type the inspection will look for.
        $personName = (new InfoType())
            ->setName('PERSON_NAME');
        $inspectionRuleSet = (new InspectionRuleSet())
            ->setInfoTypes([$personName])
            ->setRules([
                (new InspectionRule())
                    ->setHotwordRule($patientRule),
                (new InspectionRule())
                    ->setHotwordRule($doctorRule),
                (new InspectionRule())
                    ->setExclusionRule($quasimodoRule),
                (new InspectionRule())
                    ->setExclusionRule($redactedRule),
            ]);
    
        // Construct the configuration for the Inspect request, including the ruleset.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes([$personName])
            ->setIncludeQuote(true)
            ->setRuleSet([$inspectionRuleSet]);
    
        // Run request
        $inspectContentRequest = (new InspectContentRequest())
            ->setParent($parent)
            ->setInspectConfig($inspectConfig)
            ->setItem($item);
        $response = $dlp->inspectContent($inspectContentRequest);
    
        // Print the results
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
    
    
    import google.cloud.dlp
    
    
    def inspect_string_multiple_rules(project: str, content_string: str) -> None:
        """Uses the Data Loss Prevention API to modify likelihood for matches on
           PERSON_NAME combining multiple hotword and exclusion rules.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct hotword rules
        patient_rule = {
            "hotword_regex": {"pattern": "patient"},
            "proximity": {"window_before": 10},
            "likelihood_adjustment": {
                "fixed_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).VERY_LIKELY
            },
        }
        doctor_rule = {
            "hotword_regex": {"pattern": "doctor"},
            "proximity": {"window_before": 10},
            "likelihood_adjustment": {
                "fixed_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).UNLIKELY
            },
        }
    
        # Construct exclusion rules
        quasimodo_rule = {
            "dictionary": {"word_list": {"words": ["quasimodo"]}},
            "matching_type": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[MatchingType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.MatchingType.html).MATCHING_TYPE_PARTIAL_MATCH,
        }
        redacted_rule = {
            "regex": {"pattern": "REDACTED"},
            "matching_type": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[MatchingType](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.MatchingType.html).MATCHING_TYPE_PARTIAL_MATCH,
        }
    
        # Construct the rule set, combining the above rules
        rule_set = [
            {
                "info_types": [{"name": "PERSON_NAME"}],
                "rules": [
                    {"hotword_rule": patient_rule},
                    {"hotword_rule": doctor_rule},
                    {"exclusion_rule": quasimodo_rule},
                    {"exclusion_rule": redacted_rule},
                ],
            }
        ]
    
        # Construct the configuration dictionary
        inspect_config = {
            "info_types": [{"name": "PERSON_NAME"}],
            "rule_set": rule_set,
            "include_quote": True,
        }
    
        # Construct the `item`.
        item = {"value": content_string}
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}"
    
        # Call the API.
        response = dlp.[inspect_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_inspect_content)(
            request={"parent": parent, "inspect_config": inspect_config, "item": item}
        )
    
        # Print out the results.
        if response.result.findings:
            for finding in response.result.findings:
                print(f"Quote: {finding.quote}")
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

### REST

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/inspect-sensitive-text-api) for more information about using the DLP API with JSON.
    
    
    ...
      "inspectConfig":{
        "infoTypes":[
          {
            "name":"PERSON_NAME"
          }
        ],
        "ruleSet":[
          {
            "infoTypes":[
              {
                "name":"PERSON_NAME"
              }
            ],
            "rules":[
              {
                "hotwordRule":{
                  "hotwordRegex":{
                    "pattern":"patient"
                  },
                  "proximity":{
                    "windowBefore":10
                  },
                  "likelihoodAdjustment":{
                    "fixedLikelihood":"VERY_LIKELY"
                  }
                }
              },
              {
                "hotwordRule":{
                  "hotwordRegex":{
                    "pattern":"doctor"
                  },
                  "proximity":{
                    "windowBefore":10
                  },
                  "likelihoodAdjustment":{
                    "fixedLikelihood":"UNLIKELY"
                  }
                }
              },
              {
                "exclusionRule":{
                  "dictionary":{
                    "wordList":{
                      "words":[
                        "Quasimodo"
                      ]
                    }
                  },
                  "matchingType": "MATCHING_TYPE_PARTIAL_MATCH"
                }
              },
              {
                "exclusionRule":{
                  "regex":{
                    "pattern":"REDACTED"
                  },
                  "matchingType": "MATCHING_TYPE_PARTIAL_MATCH"
                }
              }
            ]
          }
        ]
      }
    ...
    

## Overlapping infoType detectors

It is possible to define a custom infoType detector that has the same name as a built-in infoType detector. As shown in the example in the "Hotword rule example scenarios" section, when you create a custom infoType detector with the same name as a built-in infoType, any findings detected by the new infoType detector are added to those detected by the built-in detector. This is only true as long as the built-in infoType is specified in the list of infoTypes in the [`InspectConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig) object.

When creating new custom infoType detectors, test them thoroughly on example content to ensure they work as you intend.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
