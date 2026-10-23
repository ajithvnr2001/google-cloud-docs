---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood/
title: Customizing match likelihood \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:29.312847+00:00
---

# Customizing match likelihood  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Customizing match likelihood Stay organized with collections  Save and categorize content based on your preferences. 

Using hotword rules, you can further extend [built-in](https://docs.cloud.google.com/sensitive-data-protection/docs/infotypes-reference) and [custom](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes) infoType detectors with powerful context rules. A hotword rule instructs Sensitive Data Protection to adjust the likelihood of a finding, depending on whether a hotword occurs near that finding. A hotword rule is a kind of [inspection rule](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules), which is specified in rule sets. Each rule is applied to a set of built-in or custom infoTypes.

## Anatomy of a hotword rule

An infoType detector can have zero or more hotword rules. In your [inspection configuration](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig), you define each [`HotwordRule`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#hotwordrule) object inside the `rules` array, as follows:
    
    
    "rules":[
      {
        "hotwordRule":{
          "hotwordRegex":{
            "pattern":"REGEX_PATTERN"
          },
          "proximity":{
            "windowAfter":"NUM_CHARS_TO_CONSIDER_AFTER_FINDING",
            "windowBefore":"NUM_CHARS_TO_CONSIDER_BEFORE_FINDING"
          }
          "likelihoodAdjustment":{
            "fixedLikelihood":"LIKELIHOOD_VALUE"
                 -- OR --
            "relativeLikelihood":"LIKELIHOOD_ADJUSTMENT"
          },
        }
      },
      ...
    ]
    

Replace the following:

  * REGEX_PATTERN: a regular expression ([`Regex`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Regex) object) that defines what qualifies as a hotword.
  * NUM_CHARS_TO_CONSIDER_AFTER_FINDING: a range of characters after the finding. Sensitive Data Protection analyzes this range to determine whether a hotword occurs near the finding.
  * NUM_CHARS_TO_CONSIDER_BEFORE_FINDING: a range of characters before the finding. Sensitive Data Protection analyzes this range to determine whether a hotword occurs near the finding.

  * LIKELIHOOD_VALUE: a fixed [`Likelihood`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#Likelihood) level to set the finding to.

  * LIKELIHOOD_ADJUSTMENT: a number that indicates how much Sensitive Data Protection must increase or decrease the likelihood of the finding. A positive integer increases the likelihood level, and a negative integer decreases it. For example, if a finding would be `POSSIBLE` without the detection rule and `relativeLikelihood` is 1, then the finding is upgraded to `LIKELY`. If `relativeLikelihood` is -1, then the finding is downgraded to `UNLIKELY`. Likelihood can never drop lower than `VERY_UNLIKELY` or exceed `VERY_LIKELY`. In these cases, the likelihood level remains the same. For example, if the base likelihood is `VERY_LIKELY` and the `relativeLikelihood` is 1, the final likelihood remains to be `VERY_LIKELY`.




## Hotword example: Match medical record numbers

Suppose you want to detect a custom infoType such as a medical record number (MRN) in the form "###-#-#####". Also, you want Sensitive Data Protection to increase the match likelihood of each finding that follows the hotword "MRN".

**Example values:**

  * 123-4-56789 would match as `POSSIBLE`.
  * MRN 123-4-56789 would match as `VERY_LIKELY`.



The following JSON example and code snippets show you how to configure the hotword rule. This example uses a [custom regular expression detector](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-regex).

In this example, note the following:

  * The request defines the `C_MRN` custom infoType, which is a detector for any string that matches the regular expression `[0-9]{3}-[0-9]{1}-[0-9]{5}`.
  * The regular expression `(?i)(mrn|medical)(?-i)` defines the hotword. Sensitive Data Protection searches for this hotword within the range of characters defined in the `proximity` field.
  * For each `C_MRN` finding that has a hotword within the set `proximity`, Sensitive Data Protection sets the likelihood level to `VERY_LIKELY`.



### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using static Google.Cloud.Dlp.V2.CustomInfoType.Types;
    
    public class InspectDataWithHotwordRule
    {
        public static InspectContentResponse InspectDataHotwordRule(
            string projectId,
            string text,
            string customRegex,
            string hotwordRegex,
            [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) infoType = null)
        {
            // Instantiate dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the content item.
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html)
            {
                ByteItem = new [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html)
                {
                    Type = [ByteContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.html).[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.html).[BytesType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html).[TextUtf8](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ByteContentItem.Types.BytesType.html#Google_Cloud_Dlp_V2_ByteContentItem_Types_BytesType_TextUtf8),
                    Data = Google.Protobuf.ByteString.CopyFromUtf8(text)
                }
            };
    
            // Construct the info type if null.
            var infotype = infoType ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "C_MRN" };
    
            // Construct the custom regex detector.
            var customInfoType = new [CustomInfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.CustomInfoType.html)
            {
                InfoType = infotype,
                Regex = new Regex { Pattern = customRegex },
                Likelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Possible](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Possible)
            };
    
            // Construct hotword rule.
            var hotwordRule = new DetectionRule.Types.HotwordRule
            {
                HotwordRegex = new Regex { Pattern = hotwordRegex },
                LikelihoodAdjustment = new DetectionRule.Types.LikelihoodAdjustment
                {
                    FixedLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[VeryLikely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_VeryLikely)
                },
                Proximity = new DetectionRule.Types.Proximity
                {
                    WindowBefore = 10
                }
            };
    
            // Construct the rule set for the inspect config.
            var inspectionRuleSet = new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)
            {
                InfoTypes = { infotype },
                Rules =
                {
                    new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html)
                    {
                        HotwordRule = hotwordRule
                    }
                }
            };
    
            // Construct the inspect config.
            var inspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
            {
                CustomInfoTypes = { customInfoType },
                IncludeQuote = true,
                RuleSet = { inspectionRuleSet },
            };
    
            // Construct the request.
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                Item = contentItem,
                InspectConfig = inspectConfig
            };
    
            // Call the API.
            var response = dlp.InspectContent(request);
    
            // Inspect the response.
            Console.WriteLine($"Findings: {response.Result.Findings.Count}");
            foreach (var f in response.Result.Findings)
            {
                Console.WriteLine("Quote: " + f.Quote);
                Console.WriteLine("Info type: " + f.[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html).Name);
                Console.WriteLine("Likelihood: " + f.[Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html));
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
    
    // inspectWithHotWordRules inspects data with hot word rule, it uses custom
    // regex with a hot word rule to increase the likelihood match
    func inspectWithHotWordRules(w io.Writer, projectID, textToInspect string) error {
    	// projectID := "my-project-id"
    	// textToInspect := "Patient's MRN 444-5-22222 and just a number 333-2-33333"
    
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
    
    	// Construct the custom regex detectors
    	customInfoType := &dlppb.CustomInfoType{
    		InfoType: &dlppb.InfoType{
    			Name: "C_MRN",
    		},
    		Type: &dlppb.CustomInfoType_Regex_{
    			Regex: &dlppb.CustomInfoType_Regex{
    				Pattern: "[1-9]{3}-[1-9]{1}-[1-9]{5}",
    			},
    		},
    		Likelihood: dlppb.[Likelihood_POSSIBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    	}
    
    	// Construct hotword rule.
    	hotWordRule := &dlppb.CustomInfoType_DetectionRule_HotwordRule{
    		HotwordRegex: &dlppb.CustomInfoType_Regex{
    			Pattern: "(?i)(mrn|medical)(?-i)",
    		},
    		Proximity: &dlppb.CustomInfoType_DetectionRule_Proximity{
    			WindowBefore: int32(10),
    		},
    		LikelihoodAdjustment: &dlppb.CustomInfoType_DetectionRule_LikelihoodAdjustment{
    			Adjustment: &dlppb.CustomInfoType_DetectionRule_LikelihoodAdjustment_FixedLikelihood{
    				FixedLikelihood: dlppb.[Likelihood_VERY_LIKELY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    			},
    		},
    	}
    
    	inspectionRuleSet := &dlppb.InspectionRuleSet{
    		Rules: []*dlppb.InspectionRule{
    			{
    				Type: &dlppb.InspectionRule_HotwordRule{
    					HotwordRule: hotWordRule,
    				},
    			},
    		},
    		InfoTypes: []*dlppb.InfoType{
    			customInfoType.InfoType,
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.InspectContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item:   contentItem,
    		InspectConfig: &dlppb.InspectConfig{
    			CustomInfoTypes: []*dlppb.CustomInfoType{
    				customInfoType,
    			},
    			RuleSet: []*dlppb.InspectionRuleSet{
    				inspectionRuleSet,
    			},
    			IncludeQuote: true,
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
    		fmt.Fprintf(w, "InfoType Name: %v\n", v.GetInfoType().GetName())
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
    
    public class InspectWithHotwordRules {
    
      public static void main(String[] args) throws Exception {
        // TODO(developer): Replace these variables before running the sample.
        String projectId = "your-project-id";
        String textToInspect = "Patient's MRN 444-5-22222 and just a number 333-2-33333";
        String customRegexPattern = "[1-9]{3}-[1-9]{1}-[1-9]{5}";
        String hotwordRegexPattern = "(?i)(mrn|medical)(?-i)";
        inspectWithHotwordRules(projectId, textToInspect, customRegexPattern, hotwordRegexPattern);
      }
    
      // Inspects a BigQuery Table
      public static void inspectWithHotwordRules(
          String projectId, String textToInspect, String customRegexPattern, String hotwordRegexPattern)
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
    
          // Specify the regex pattern the inspection will look for.
          [Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html) regex = [Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html).newBuilder().[setPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)(customRegexPattern).build();
    
          // Construct the custom regex detector.
          [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html) infoType = [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName("C_MRN").build();
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html) customInfoType =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).newBuilder().setInfoType(infoType).setRegex(regex).build();
    
          // Specify hotword likelihood adjustment.
          [LikelihoodAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.html) likelihoodAdjustment =
              [LikelihoodAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.html).newBuilder().[setFixedLikelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_DetectionRule_LikelihoodAdjustment_Builder_setFixedLikelihood_com_google_privacy_dlp_v2_Likelihood_)([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).VERY_LIKELY).build();
    
          // Specify a window around a finding to apply a detection rule.
          [Proximity](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.html) proximity = [Proximity](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.html).newBuilder().[setWindowBefore](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_DetectionRule_Proximity_Builder_setWindowBefore_int_)(10).build();
    
          // Construct hotword rule.
          [HotwordRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html) hotwordRule =
              [HotwordRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html).newBuilder()
                  .setHotwordRegex([Regex](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.html).newBuilder().[setPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)(hotwordRegexPattern).build())
                  .setLikelihoodAdjustment(likelihoodAdjustment)
                  .setProximity(proximity)
                  .build();
    
          // Construct rule set for the inspect config.
          [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html) inspectionRuleSet =
              [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html).newBuilder()
                  .addInfoTypes(infoType)
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().setHotwordRule(hotwordRule))
                  .build();
    
          // Construct the configuration for the Inspect request.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .[addCustomInfoTypes](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addCustomInfoTypes_com_google_privacy_dlp_v2_CustomInfoType_)(customInfoType)
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .setMinLikelihood([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).POSSIBLE)
                  .[addRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_)(inspectionRuleSet)
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
    // const string = 'Patients MRN 444-5-22222';
    
    // The minimum likelihood required before returning a match
    // const minLikelihood = DLP.protos.google.privacy.dlp.v2.Likelihood.POSSIBLE;
    
    // The maximum number of findings to report per request (0 = server maximum)
    // const maxFindings = 0;
    
    // The infoTypes of information to match
    // See https://cloud.google.com/dlp/docs/concepts-infotypes for more information
    // about supported infoTypes.
    // const infoTypes = [{ name: 'EMAIL_ADDRESS' }];
    
    // The customInfoTypes of information to match
    // const customInfoTypes = [{ infoType: { name: 'DICT_TYPE' }, dictionary: { wordList: { words: ['foo', 'bar', 'baz']}}},
    //   { infoType: { name: 'REGEX_TYPE' }, regex: {pattern: '\\(\\d{3}\\) \\d{3}-\\d{4}'}}];
    
    // Whether to include the matching string
    // const includeQuote = true;
    
    // Custom hotword regex patten
    // const hotwordRegexPattern = '(?i)(mrn|medical)(?-i)';
    
    async function inspectWithHotwordRule() {
      // Construct item to inspect
      const item = {
        byteItem: {
          type: DLP.protos.google.privacy.dlp.v2.[ByteContentItem](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem-class.html).[BytesType](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html)
            .[TEXT_UTF8](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.bytecontentitem.bytestype.html),
          data: Buffer.from(string, 'utf-8'),
        },
      };
    
      // Construct a hot word rule
      const hotwordRule = {
        hotwordRegex: {
          pattern: hotwordRegexPattern,
        },
        proximity: {
          windowBefore: 10,
        },
        likelihoodAdjustment: {
          fixedLikelihood:
            DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[VERY_LIKELY](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
        },
      };
    
      // Construct a hotword inspection rule
      const inpectionRuleSet = [
        {
          infoTypes: customInfoTypes.map(
            customInfoType => customInfoType.infoType
          ),
          rules: [{hotwordRule: hotwordRule}],
        },
      ];
    
      // Assigns likelihood to each match
      customInfoTypes = customInfoTypes.map(customInfoType => {
        customInfoType.likelihood =
          DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[POSSIBLE](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html);
        return customInfoType;
      });
    
      // Construct request
      const request = {
        parent: `projects/${projectId}/locations/global`,
        inspectConfig: {
          infoTypes: infoTypes,
          customInfoTypes: customInfoTypes,
          minLikelihood: minLikelihood,
          includeQuote: includeQuote,
          limits: {
            maxFindingsPerRequest: maxFindings,
          },
          ruleSet: inpectionRuleSet,
        },
        item: item,
      };
    
      // Run request
      const [response] = await dlp.inspectContent(request);
      const findings = response.result.findings;
      if (findings.length > 0) {
        console.log('Findings:');
        findings.forEach(finding => {
          if (includeQuote) {
            console.log(`\tQuote: ${finding.quote}`);
          }
          console.log(`\tInfo type: ${finding.infoType.name}`);
          console.log(`\tLikelihood: ${finding.likelihood}`);
        });
      } else {
        console.log('No findings.');
      }
    }
    inspectWithHotwordRule();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType;
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
     * Inspect data with a hotword rule
     * This sample uses a custom regex with a hotword rule to increase the likelihood of match.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     * @param string $textToInspect     The string to inspect.
     */
    function inspect_hotword_rule(
        // TODO(developer): Replace sample parameters before running the code.
        string $projectId,
        string $textToInspect = "Patient's MRN 444-5-22222 and just a number 333-2-33333"
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify what content you want the service to Inspect.
        $item = (new ContentItem())
            ->setValue($textToInspect);
    
        // Specify the regex pattern the inspection will look for.
        $customRegexPattern = '[1-9]{3}-[1-9]{1}-[1-9]{5}';
        $hotwordRegexPattern = '(?i)(mrn|medical)(?-i)';
    
        // Construct the custom regex detector.
        $cMrnDetector = (new InfoType())
            ->setName('C_MRN');
        $customInfoType = (new CustomInfoType())
            ->setInfoType($cMrnDetector)
            ->setLikelihood(Likelihood::POSSIBLE)
            ->setRegex((new Regex())
                ->setPattern($customRegexPattern));
    
        // Specify hotword likelihood adjustment.
        $likelihoodAdjustment = (new LikelihoodAdjustment())
            ->setFixedLikelihood(Likelihood::VERY_LIKELY);
    
        // Specify a window around a finding to apply a detection rule.
        $proximity = (new Proximity())
            ->setWindowBefore(10);
    
        $hotwordRule = (new HotwordRule())
            ->setHotwordRegex((new Regex())
                ->setPattern($hotwordRegexPattern))
            ->setLikelihoodAdjustment($likelihoodAdjustment)
            ->setProximity($proximity);
    
        // Construct rule set for the inspect config.
        $inspectionRuleSet = (new InspectionRuleSet())
            ->setInfoTypes([$cMrnDetector])
            ->setRules([
                (new InspectionRule())
                    ->setHotwordRule($hotwordRule)
            ]);
    
        // Construct the configuration for the Inspect request.
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
    
    
    import google.cloud.dlp
    
    
    def inspect_data_w_custom_hotwords(
        project: str,
        content_string: str,
    ) -> None:
        """Uses the Data Loss Prevention API to analyze string with medical record
           number custom regex detector, with custom hotwords rules to boost finding
           certainty under some circumstances.
    
        Args:
            project: The Google Cloud project id to use as a parent resource.
            content_string: The string to inspect.
    
        Returns:
            None; the response from the API is printed to the terminal.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct a custom regex detector info type called "C_MRN",
        # with ###-#-##### pattern, where each # represents a digit from 1 to 9.
        # The detector has a detection likelihood of POSSIBLE.
        custom_info_types = [
            {
                "info_type": {"name": "C_MRN"},
                "regex": {"pattern": "[1-9]{3}-[1-9]{1}-[1-9]{5}"},
                "likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).POSSIBLE,
            }
        ]
    
        # Construct a rule set with hotwords "mrn" and "medical", with a likelohood
        # boost to VERY_LIKELY when hotwords are present within the 10 character-
        # window preceding the PII finding.
        hotword_rule = {
            "hotword_regex": {"pattern": "(?i)(mrn|medical)(?-i)"},
            "likelihood_adjustment": {
                "fixed_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).VERY_LIKELY
            },
            "proximity": {"window_before": 10},
        }
    
        rule_set = [
            {"info_types": [{"name": "C_MRN"}], "rules": [{"hotword_rule": hotword_rule}]}
        ]
    
        # Construct the configuration dictionary with the custom regex info type.
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

See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/quickstart-json) for more information about using the DLP API with JSON.

**Note:** The following example requires an [OAuth 2.0 access token](https://docs.cloud.google.com/sensitive-data-protection/docs/auth#using_a_service_account).

**HTTP method and URL:**
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/content:inspect
    

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

**JSON input:**
    
    
    {
      "item":{
        "value":"Patient's MRN 444-5-22222 and just a number 333-2-33333"
      },
      "inspectConfig":{
        "customInfoTypes":[
          {
            "infoType":{
              "name":"C_MRN"
            },
            "regex":{
              "pattern":"[0-9]{3}-[0-9]{1}-[0-9]{5}"
            },
            "likelihood":"POSSIBLE",
          }
        ],
        "ruleSet":[
            {
            "infoTypes": [{"name" : "C_MRN"}],
            "rules":[
              {
                "hotwordRule":{
                  "hotwordRegex":{
                    "pattern":"(?i)(mrn|medical)(?-i)"
                  },
                  "likelihoodAdjustment":{
                    "fixedLikelihood":"VERY_LIKELY"
                  },
                  "proximity":{
                    "windowBefore":10
                  }
                }
              }
            ]
          }
        ]
      }
    }
    

**JSON output (abbreviated):**
    
    
    {
      "result": {
        "findings": [
          {
            "infoType": {
              "name": "C_MRN"
            },
            "likelihood": "VERY_LIKELY",
            "location": {
              "byteRange": {
                "start": "14",
                "end": "25"
              },
              "codepointRange": { ... }
            }
          },
          {
            "infoType": {
              "name": "C_MRN"
            },
            "likelihood": "POSSIBLE",
              "byteRange": {
                "start": "44",
                "end": "55"
              },
              "codepointRange": { ... }
            }
          }
        ]
      }
    }
    

The output shows that Sensitive Data Protection correctly identified the medical record number using the `C_MRN` custom infoType detector. Further, because of the context matching in the hotword rule, Sensitive Data Protection assigned the first result—which had an MRN within the set `proximity`—a likelihood of `VERY_LIKELY`, as configured. The second finding lacked the context, so the `likelihood` stayed at `POSSIBLE`.

## Hotword example: Set the match likelihood of a table column

This example demonstrates how you can set the match likelihood of an entire column of data. This approach is helpful, for example, if you want to exclude a column of data from inspection results.

**Note:** The recommended approach for excluding an entire column of data from results is to use an [`ExcludeByHotword`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectConfig#excludebyhotword) exclusion rule. For more information, see [Omit findings in an entire column of data](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules#exclude-by-hotword-structured).

Consider the following table. One column contains placeholder Social Security numbers (SSNs), and another contains real SSNs.

Fake Social Security Number | Real Social Security Number  
---|---  
111-11-1111 | 222-22-2222  
  
To minimize noise in inspection results, you can exclude any findings in the `Fake Social Security Number` column. Assign a low likelihood level to this column. Then, configure the request such that matches with that likelihood level are excluded from the results.

In this example, note the following:

  * The hotword rule is applied to the `US_SOCIAL_SECURITY_NUMBER` infoType.
  * The hotword regular expression `(Fake Social Security Number)` contains the name of the column that has the placeholder values.
  * The `windowBefore` property is set to 1, which means that the hotword is in a column header, and the findings must be in the column.
  * For each `US_SOCIAL_SECURITY_NUMBER` finding in this column, Sensitive Data Protection sets the likelihood level to `VERY_UNLIKELY`.
  * The `minLikelihood` property is set to `POSSIBLE`, which means that any finding that has a [likelihood level](https://docs.cloud.google.com/sensitive-data-protection/docs/likelihood) lower than `POSSIBLE` is excluded from the inspection results.



See the [JSON quickstart](https://docs.cloud.google.com/sensitive-data-protection/docs/quickstart-json) for more information about using the DLP API with JSON.

**Note:** The following example requires an [OAuth 2.0 access token](https://docs.cloud.google.com/sensitive-data-protection/docs/auth#using_a_service_account).

**HTTP method and URL:**
    
    
    POST https://dlp.googleapis.com/v2/projects/PROJECT_ID/content:inspect
    

Replace `PROJECT_ID` with the [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#before_you_begin).

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    using System;
    using System.Collections.Generic;
    using static Google.Cloud.Dlp.V2.CustomInfoType.Types;
    
    public class InspectTableWithCustomHotwords
    {
        public static InspectResult InspectTable(
            string projectId,
            [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html) tableToInspect = null,
            IEnumerable<InfoType> infoTypes = null)
        {
            // Instantiate the dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the table if null.
            if (tableToInspect == null)
            {
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html){ StringValue = "111-11-1111" },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "222-22-2222" }
                };
                tableToInspect = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                {
                    Headers =
                    {
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Fake Social Security Number" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "Real Social Security Number" }
                    },
                    Rows =
                    {
                        new Table.Types.Row { Values = { row1 } }
                    }
                };
            }
    
            // Specify the table and construct the content item.
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Table = tableToInspect };
    
            // Specify the type of info to be inspected.
            var infotypes = infoTypes ?? new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html)[] { new [InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html) { Name = "US_SOCIAL_SECURITY_NUMBER" } };
    
            // Construct the Inspection Rule Set by specifying the hotword rule as detection rule.
            var ruleSet = new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)[]
            {
                new [InspectionRuleSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRuleSet.html)
                {
                    InfoTypes = { infotypes },
                    Rules =
                    {
                        new [InspectionRule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectionRule.html)
                        {
                            HotwordRule = new DetectionRule.Types.HotwordRule
                            {
                                HotwordRegex = new Regex
                                {
                                    Pattern = "(Fake Social Security Number)"
                                },
                                LikelihoodAdjustment = new DetectionRule.Types.LikelihoodAdjustment
                                {
                                    FixedLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[VeryUnlikely](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_VeryUnlikely)
                                },
                                Proximity = new DetectionRule.Types.Proximity
                                {
                                    WindowBefore = 1
                                }
                            }
                        }
                    }
                }
            };
    
            // Construct the request.
            var request = new [InspectContentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentRequest.html)
            {
                InspectConfig = new [InspectConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectConfig.html)
                {
                    InfoTypes = { infotypes },
                    IncludeQuote = true,
                    MinLikelihood = [Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html).[Possible](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html#Google_Cloud_Dlp_V2_Likelihood_Possible),
                    RuleSet = { ruleSet }
                },
                ParentAsLocationName = new [LocationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)(projectId, "global"),
                Item = contentItem
            };
    
            // Call the API.
            [InspectContentResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html) response = dlp.InspectContent(request);
    
            // Inspect the results.
            var resultFindings = response.[Result](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html#Google_Cloud_Dlp_V2_InspectContentResponse_Result).Findings;
    
            Console.WriteLine($"Findings: {resultFindings.Count}");
    
            foreach (var f in resultFindings)
            {
                Console.WriteLine("\tQuote: " + f.Quote);
                Console.WriteLine("\tInfo type: " + f.[InfoType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InfoType.html).Name);
                Console.WriteLine("\tLikelihood: " + f.[Likelihood](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Likelihood.html));
            }
    
            return response.[Result](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.InspectContentResponse.html#Google_Cloud_Dlp_V2_InspectContentResponse_Result);
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
    
    // inspectTableWithCustomHotword Sets the match likelihood of a table column to customize data inspection results.
    // This example showcases how you can adjust the match likelihood for an entire column of data, enabling the
    // exclusion of specific columns from inspection if needed.
    func inspectTableWithCustomHotword(w io.Writer, projectID, hotwordRegexPattern string) error {
    	// projectID := "your-project-id"
    	// hotwordRegexPattern := "(Fake Social Security Number)"
    
    	tableToInspect := &dlppb.Table{
    		Headers: []*dlppb.FieldId{
    			{Name: "Fake Social Security Number"},
    			{Name: "Real Social Security Number"},
    		},
    		Rows: []*dlppb.Table_Row{
    			{
    				Values: []*dlppb.Value{
    					{
    						Type: &dlppb.Value_StringValue{StringValue: "444-55-6666"},
    					},
    					{
    						Type: &dlppb.Value_StringValue{StringValue: "111-22-3333"},
    					},
    				},
    			},
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
    	contentItem := &dlppb.ContentItem_Table{
    		Table: tableToInspect,
    	}
    
    	// Specify the likelihood adjustment to adjust the match likelihood for your detection rule
    	// based on your needs and desired level of sensitivity in data analysis.
    	likelihoodAdjustment := &dlppb.CustomInfoType_DetectionRule_LikelihoodAdjustment{
    		Adjustment: &dlppb.CustomInfoType_DetectionRule_LikelihoodAdjustment_FixedLikelihood{
    			FixedLikelihood: dlppb.[Likelihood_VERY_UNLIKELY](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    		},
    	}
    
    	// Specify the type of info the inspection will look for.
    	// See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types.
    	infoTypes := []*dlppb.InfoType{
    		{Name: "US_SOCIAL_SECURITY_NUMBER"},
    	}
    
    	// Specify the proximity so that It helps identify sensitive information
    	// occurring near other data points, enabling more context-aware analysis.
    	proximity := &dlppb.CustomInfoType_DetectionRule_Proximity{
    		WindowBefore: 5,
    	}
    
    	// Construct hotWord rule.
    	hotwordRule := &dlppb.CustomInfoType_DetectionRule_HotwordRule{
    		HotwordRegex: &dlppb.CustomInfoType_Regex{
    			Pattern: hotwordRegexPattern,
    		},
    		Proximity:            proximity,
    		LikelihoodAdjustment: likelihoodAdjustment,
    	}
    
    	// Construct rule set for the inspect config.
    	inspectionRuleSet := &dlppb.InspectionRuleSet{
    		InfoTypes: infoTypes,
    		Rules: []*dlppb.InspectionRule{
    			{
    				Type: &dlppb.InspectionRule_HotwordRule{
    					HotwordRule: hotwordRule,
    				},
    			},
    		},
    	}
    
    	// Construct the configuration for the Inspect request.
    	config := &dlppb.InspectConfig{
    		IncludeQuote:  true,
    		InfoTypes:     infoTypes,
    		MinLikelihood: dlppb.[Likelihood_POSSIBLE](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/dlp/latest/apiv2/dlppb.html#cloud_google_com_go_dlp_apiv2_dlppb_Likelihood_LIKELIHOOD_UNSPECIFIED_Likelihood_VERY_UNLIKELY_Likelihood_UNLIKELY_Likelihood_POSSIBLE_Likelihood_LIKELY_Likelihood_VERY_LIKELY),
    		RuleSet: []*dlppb.InspectionRuleSet{
    			inspectionRuleSet,
    		},
    	}
    
    	// Construct the Inspect request to be sent by the client.
    	req := &dlppb.InspectContentRequest{
    		Parent: fmt.Sprintf("projects/%s/locations/global", projectID),
    		Item: &dlppb.ContentItem{
    			DataItem: contentItem,
    		},
    		InspectConfig: config,
    	}
    	// Send the request.
    	resp, err := client.InspectContent(ctx, req)
    	if err != nil {
    		return err
    	}
    
    	// Parse the response and process results.
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
    import com.google.privacy.dlp.v2.[ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html);
    import com.google.privacy.dlp.v2.[CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html);
    import com.google.privacy.dlp.v2.[FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html);
    import com.google.privacy.dlp.v2.[Finding](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Finding.html);
    import com.google.privacy.dlp.v2.[InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html);
    import com.google.privacy.dlp.v2.[InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html);
    import com.google.privacy.dlp.v2.[InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html);
    import com.google.privacy.dlp.v2.[InspectContentResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentResponse.html);
    import com.google.privacy.dlp.v2.[InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html);
    import com.google.privacy.dlp.v2.[InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html);
    import com.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html);
    import com.google.privacy.dlp.v2.[LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html);
    import com.google.privacy.dlp.v2.[Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html);
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import java.io.IOException;
    import java.util.List;
    import java.util.stream.Collectors;
    import java.util.stream.Stream;
    
    public class InspectTableWithCustomHotword {
    
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // Specify the table to be considered for de-identification.
        [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify =
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder()
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Some Social Security Number").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("Real Social Security Number").build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("111-11-1111").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("222-22-2222").build())
                        .build())
                .build();
        // Specify the regex pattern to be detected.
        // Refer https://github.com/google/re2/wiki/Syntax for creating regular expression.
        String hotwordRegexPattern = "Some Social Security Number";
        inspectDemotingFindingsWithHotwords(projectId, tableToDeIdentify, hotwordRegexPattern);
      }
    
      //  Inspects the provided table, excluding the findings of entire column matching regular
      // expression.
      public static void inspectDemotingFindingsWithHotwords(
          String projectId, [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify, String hotwordRegexPattern) throws IOException {
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to de-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(tableToDeIdentify).build();
    
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[DetectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.html).[LikelihoodAdjustment](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.html) likelihoodAdjustment =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).DetectionRule.LikelihoodAdjustment.newBuilder()
                  .[setFixedLikelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.LikelihoodAdjustment.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_DetectionRule_LikelihoodAdjustment_Builder_setFixedLikelihood_com_google_privacy_dlp_v2_Likelihood_)([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).VERY_UNLIKELY)
                  .build();
    
          // Specify the type of info the inspection will look for.
          // See https://cloud.google.com/dlp/docs/infotypes-reference for complete list of info types
          List<InfoType> infoTypes =
              Stream.of("US_SOCIAL_SECURITY_NUMBER")
                  .map(it -> [InfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InfoType.html).newBuilder().setName(it).build())
                  .collect(Collectors.toList());
    
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[DetectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.html).[Proximity](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.html) proximity =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).DetectionRule.Proximity.newBuilder().[setWindowBefore](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.Proximity.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_DetectionRule_Proximity_Builder_setWindowBefore_int_)(1).build();
    
          // Construct hotword rule.
          [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).[DetectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.html).[HotwordRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.DetectionRule.HotwordRule.html) hotwordRule =
              [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).DetectionRule.HotwordRule.newBuilder()
                  .setHotwordRegex(
                      [CustomInfoType](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.html).Regex.newBuilder().[setPattern](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.CustomInfoType.Regex.Builder.html#com_google_privacy_dlp_v2_CustomInfoType_Regex_Builder_setPattern_java_lang_String_)(hotwordRegexPattern).build())
                  .setLikelihoodAdjustment(likelihoodAdjustment)
                  .setProximity(proximity)
                  .build();
    
          // Construct rule set for the inspect config.
          [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html) inspectionRuleSet =
              [InspectionRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRuleSet.html).newBuilder()
                  .addAllInfoTypes(infoTypes)
                  .addRules([InspectionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectionRule.html).newBuilder().setHotwordRule(hotwordRule))
                  .build();
    
          // Construct the configuration for the Inspect request.
          [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html) config =
              [InspectConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.html).newBuilder()
                  .[setIncludeQuote](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_setIncludeQuote_boolean_)(true)
                  .setMinLikelihood([Likelihood](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Likelihood.html).POSSIBLE)
                  .[addRuleSet](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectConfig.Builder.html#com_google_privacy_dlp_v2_InspectConfig_Builder_addRuleSet_com_google_privacy_dlp_v2_InspectionRuleSet_)(inspectionRuleSet)
                  .addAllInfoTypes(infoTypes)
                  .build();
    
          // Construct the Inspect request to be sent by the client.
          [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html) request =
              [InspectContentRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.InspectContentRequest.html).newBuilder()
                  .setParent([LocationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.LocationName.html).of(projectId, "global").toString())
                  .setItem(contentItem)
                  .setInspectConfig(config)
                  .build();
    
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
    
    // Instantiates a client
    const dlp = new DLP.[DlpServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/overview.html)();
    
    // The project ID to run the API call under.
    // const projectId = "your-project-id";
    
    // Table to inspect
    const tableToInspect = {
      headers: [
        {name: 'Fake Social Security Number'},
        {name: 'Real Social Security Number'},
      ],
      rows: [
        {
          values: [{stringValue: '111-11-1111'}, {stringValue: '458-90-3124'}],
        },
      ],
    };
    
    async function inspectWithCustomHotwords() {
      // Specify the regex pattern to be detected.
      const hotwordRegexPattern = '(Fake Social Security Number)';
    
      // Specify what content you want the service to de-identify.
      const contentItem = {
        table: tableToInspect,
      };
    
      // Specify the type of info the inspection will look for.
      const infoTypes = [{name: 'US_SOCIAL_SECURITY_NUMBER'}];
    
      // Construct hotword rule.
      const hotwordRule = {
        hotwordRegex: {
          pattern: hotwordRegexPattern,
        },
        likelihoodAdjustment: {
          fixedLikelihood:
            DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[VERY_UNLIKELY](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
        },
        proximity: {
          windowBefore: 1,
        },
      };
    
      // Construct rule set for the inspect configuration.
      const inspectionRuleSet = {
        infoTypes: infoTypes,
        rules: [
          {
            hotwordRule: hotwordRule,
          },
        ],
      };
    
      // Construct the configuration for the Inspect request.
      const config = {
        infoTypes: infoTypes,
        ruleSet: [inspectionRuleSet],
        minLikelihood: DLP.protos.google.privacy.dlp.v2.[Likelihood](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html).[POSSIBLE](https://docs.cloud.google.com/nodejs/docs/reference/dlp/latest/dlp/protos.google.privacy.dlp.v2.likelihood.html),
        includeQuote: true,
      };
    
      // Construct the Inspect request to be sent by the client.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        item: contentItem,
        inspectConfig: config,
      };
    
      // Use the client to send the API request.
      const [response] = await dlp.inspectContent(request);
    
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
    inspectWithCustomHotwords();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\Client\DlpServiceClient;
    use Google\Cloud\Dlp\V2\ContentItem;
    use Google\Cloud\Dlp\V2\CustomInfoType\DetectionRule\HotwordRule;
    use Google\Cloud\Dlp\V2\CustomInfoType\DetectionRule\LikelihoodAdjustment;
    use Google\Cloud\Dlp\V2\CustomInfoType\DetectionRule\Proximity;
    use Google\Cloud\Dlp\V2\CustomInfoType\Regex;
    use Google\Cloud\Dlp\V2\FieldId;
    use Google\Cloud\Dlp\V2\InfoType;
    use Google\Cloud\Dlp\V2\InspectConfig;
    use Google\Cloud\Dlp\V2\InspectContentRequest;
    use Google\Cloud\Dlp\V2\InspectionRule;
    use Google\Cloud\Dlp\V2\InspectionRuleSet;
    use Google\Cloud\Dlp\V2\Likelihood;
    use Google\Cloud\Dlp\V2\Table;
    use Google\Cloud\Dlp\V2\Table\Row;
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * Hotword example: Set the match likelihood of a table column.
     * This example demonstrates how you can set the match likelihood of an entire column of data.
     * This approach is helpful, for example, if you want to exclude a column of data from inspection
     * results.
     *
     * @param string $projectId         The Google Cloud project id to use as a parent resource.
     */
    function inspect_column_values_w_custom_hotwords(string $projectId): void
    {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        $parent = "projects/$projectId/locations/global";
    
        // Specify the table to be inspected.
        $tableToDeIdentify = (new Table())
            ->setHeaders([
                (new FieldId())
                    ->setName('Fake Social Security Number'),
                (new FieldId())
                    ->setName('Real Social Security Number'),
            ])
            ->setRows([
                (new Row())->setValues([
                    (new Value())
                        ->setStringValue('111-11-1111'),
                    (new Value())
                        ->setStringValue('222-22-2222')
                ])
            ]);
    
        $item = (new ContentItem())
            ->setTable($tableToDeIdentify);
    
        // Specify the regex pattern the inspection will look for.
        $hotwordRegexPattern = 'Fake Social Security Number';
    
        // Specify hotword likelihood adjustment.
        $likelihoodAdjustment = (new LikelihoodAdjustment())
            ->setFixedLikelihood(Likelihood::VERY_UNLIKELY);
    
        // Specify a window around a finding to apply a detection rule.
        $proximity = (new Proximity())
            ->setWindowBefore(1);
    
        // Construct the hotword rule.
        $hotwordRule = (new HotwordRule())
            ->setHotwordRegex((new Regex())
                ->setPattern($hotwordRegexPattern))
            ->setLikelihoodAdjustment($likelihoodAdjustment)
            ->setProximity($proximity);
    
        // Construct rule set for the inspect config.
        $infotype = (new InfoType())
            ->setName('US_SOCIAL_SECURITY_NUMBER');
        $inspectionRuleSet = (new InspectionRuleSet())
            ->setInfoTypes([$infotype])
            ->setRules([
                (new InspectionRule())
                    ->setHotwordRule($hotwordRule)
            ]);
    
        // Construct the configuration for the Inspect request.
        $inspectConfig = (new InspectConfig())
            ->setInfoTypes([$infotype])
            ->setIncludeQuote(true)
            ->setRuleSet([$inspectionRuleSet])
            ->setMinLikelihood(Likelihood::POSSIBLE);
    
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
    
    
    def inspect_column_values_w_custom_hotwords(
        project: str,
        table_header: List[str],
        table_rows: List[List[str]],
        info_types: List[str],
        custom_hotword: str,
    ) -> None:
        """Uses the Data Loss Prevention API to inspect table data using built-in
        infoType detectors, excluding columns that match a custom hot-word.
        Args:
            project: The Google Cloud project id to use as a parent resource.
            table_header: List of strings representing table field names.
            table_rows: List of rows representing table values.
            info_types: The infoType for which hot-word rule is applied.
            custom_hotword: The custom regular expression used for likelihood boosting.
        """
    
        # Instantiate a client
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Construct the `table`. For more details on the table schema, please see
        # https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem#Table
        headers = [{"name": val} for val in table_header]
        rows = []
        for row in table_rows:
            rows.append({"values": [{"string_value": cell_val} for cell_val in row]})
        table = {"headers": headers, "rows": rows}
    
        # Construct the `item` for table to be inspected.
        item = {"table": table}
    
        # Prepare info_types by converting the list of strings into a list of
        # dictionaries.
        info_types = [{"name": info_type} for info_type in info_types]
    
        # Construct a rule set with caller provided hot-word, with a likelihood
        # boost to VERY_UNLIKELY when the hot-word are present
        hotword_rule = {
            "hotword_regex": {"pattern": custom_hotword},
            "likelihood_adjustment": {
                "fixed_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).VERY_UNLIKELY
            },
            "proximity": {"window_before": 1},
        }
    
        rule_set = [
            {
                "info_types": info_types,
                "rules": [{"hotword_rule": hotword_rule}],
            }
        ]
    
        # Construct the configuration dictionary, which defines the entire inspect content task.
        inspect_config = {
            "info_types": info_types,
            "rule_set": rule_set,
            "min_likelihood": google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[Likelihood](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.types.Likelihood.html).POSSIBLE,
            "include_quote": True,
        }
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Call the API
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
                try:
                    if finding.quote:
                        print(f"Quote: {finding.quote}")
                except AttributeError:
                    pass
                print(f"Info type: {finding.info_type.name}")
                print(f"Likelihood: {finding.likelihood}")
        else:
            print("No findings.")
    
    

### REST

**JSON input:**
    
    
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
                "hotwordRule": {
                  "hotwordRegex": {
                    "pattern": "(Fake Social Security Number)"
                  },
                  "likelihoodAdjustment": {
                    "fixedLikelihood": "VERY_UNLIKELY"
                  },
                  "proximity": {
                    "windowBefore": 1
                  }
                }
              }
            ]
          }
        ],
        "minLikelihood": "POSSIBLE"
      }
    }
    

**JSON output:**
    
    
    {
      "result": {
        "findings": [
          {
            "quote": "222-22-2222",
            "infoType": {
              "name": "US_SOCIAL_SECURITY_NUMBER"
            },
            "likelihood": "VERY_LIKELY",
            "location": {
              "byteRange": {
                "end": "11"
              },
              "codepointRange": {
                "end": "11"
              },
              "contentLocations": [
                {
                  "recordLocation": {
                    "fieldId": {
                      "name": "Real Social Security Number"
                    },
                    "tableLocation": {}
                  }
                }
              ]
            },
            "createTime": "TIMESTAMP",
            "findingId": "TIMESTAMP"
          }
        ]
      }
    }
    

The value 111-11-1111, which is in the `Fake Social Security Number` column, matched the hotword rule, so Sensitive Data Protection assigned to it the `VERY_UNLIKELY` likelihood level . This level is lower than the minimum likelihood set in the inspection configuration (`POSSIBLE`), so this finding is excluded from the inspection result.

You can experiment with this example by removing the rule set. Notice that Sensitive Data Protection includes 111-11-1111 in the results.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
