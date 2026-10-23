---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-string-without-overlap/
title: Inspect a string for sensitive data, omitting overlapping matches on domain and email \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:00.878958+00:00
---

# Inspect a string for sensitive data, omitting overlapping matches on domain and email  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-string-without-overlap/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Inspect a string for sensitive data, omitting overlapping matches on domain and email Stay organized with collections  Save and categorize content based on your preferences. 

Omit matches on domain names that are part of email addresses in a DOMAIN_NAME detector scan.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Modifying infoType detectors to refine scan results](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-rules)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
