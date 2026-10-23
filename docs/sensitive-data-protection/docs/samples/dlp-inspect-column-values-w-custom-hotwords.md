---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-column-values-w-custom-hotwords/
title: Set the match likelihood of a table column \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:52:15.363577+00:00
---

# Set the match likelihood of a table column  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/samples/dlp-inspect-column-values-w-custom-hotwords/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Samples ](https://docs.cloud.google.com/sensitive-data-protection/docs/samples)



#  Set the match likelihood of a table column Stay organized with collections  Save and categorize content based on your preferences. 

Set the match likelihood of an entire column of data. This approach is helpful, for example, if you want to exclude a column of data from inspection results.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Customizing match likelihood](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-custom-infotypes-likelihood)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=clouddatalossprevention). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
