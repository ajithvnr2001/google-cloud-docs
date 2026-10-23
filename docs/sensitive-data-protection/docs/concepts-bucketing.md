---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing/
title: Generalization and bucketing \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:23.573977+00:00
---

# Generalization and bucketing  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-bucketing/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Generalization and bucketing Stay organized with collections  Save and categorize content based on your preferences. 

_Generalization_ is the process of taking a distinguishing value and abstracting it into a more general, less distinguishing value. Generalization attempts to preserve data utility while also reducing the identifiability of the data.

There can be many levels of generalization depending on the data type. How much generalization is needed is something that you can measure across a dataset or a real world population using techniques like those included in [Sensitive Data Protection's risk analysis](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis).

One common generalization technique that Sensitive Data Protection supports is _bucketing_. With bucketing, you group records into smaller buckets in an attempt to minimize the risk of an attacker associating sensitive information with identifying information. Doing so can retain meaning and utility, but it will also obscure the individual values that have too few participants.

## When to use generalization and bucketing

The following are some common use cases:

  * **Obfuscate numerical outliers in analytical datasets** : Group rare numerical values (such as extreme salaries, credit scores, or transaction sizes) into broader ranges to prevent individual re-identification.
  * **Preserve statistical utility in demographic research** : Replace exact age, income, or geographic identifiers with categorical intervals to support broad analytical modeling without exposing distinct individual values.
  * **Reduce quasi-identifier distinctness for k-anonymity** : Generalize quasi-identifying attributes across rows so that each distinct combination is shared by a sufficiently large cohort of individuals.
  * **Sanitize external reporting datasets** : Abstract fine-grained customer metrics into high-level tiers (such as "Low", "Medium", and "High") before sharing reports with third-party vendors or public audiences.



## Bucketing scenario 1

Consider this numerical bucketing scenario: A database stores users' satisfaction scores, which range from 0 to 100. The database looks something like the following:

user_id | score  
---|---  
1 | 100  
2 | 100  
3 | 92  
... | ...  
  
Scanning over the data, you realize that some values are rarely used by users. In fact, there are a few scores that map to only one user. For example, the majority of users pick either 0, 25, 50, 75, or 100. However, five users picked 95, and just one user picked 92. Instead of keeping the raw data, you could generalize these values into groups and eliminate having any groups with too few participants. Depending on how the data is used, generalizing data in this way could help prevent re-identification.

You could choose to remove these rows of outlier data, or you could attempt to preserve their utility by using bucketing. For this example, let's bucket all values according to the following:

  * 0-25: "Low"
  * 26-75: "Medium"
  * 76-100: "High"



Bucketing in Sensitive Data Protection is one of many primitive transformations available for de-identification. The following JSON configuration illustrates how to implement this bucketing scenario in the DLP API. This JSON could be included in a request to the [`content.deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify) method:

### C#

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    using System;
    using [Google.Api.Gax.ResourceNames](https://docs.cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.html);
    using [Google.Cloud.Dlp.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.html);
    
    public class DeidentifyTableWithPrimitiveBucketing
    {
        public static Table DeidentifyData(
            string projectId,
            [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html) tableToInspect = null)
        {
            // Instantiate dlp client.
            var dlp = [DlpServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html).[Create](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DlpServiceClient.html#Google_Cloud_Dlp_V2_DlpServiceClient_Create)();
    
            // Construct the table if null.
            if (tableToInspect == null)
            {
                var row1 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 1 },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 95 }
                };
                var row2 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 2 },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 61 }
                };
                var row3 = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html)[]
                {
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 3 },
                    new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 22 }
                };
    
                tableToInspect = new [Table](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Table.html)
                {
                    Headers =
                    {
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "user_id" },
                        new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "score" }
                    },
                    Rows =
                    {
                        new Table.Types.Row { Values = { row1 } },
                        new Table.Types.Row { Values = { row2 } },
                        new Table.Types.Row { Values = { row3 } }
                    }
                };
            }
    
            // Specify the table and construct the content item.
            var contentItem = new [ContentItem](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.ContentItem.html) { Table = tableToInspect };
    
            // Specify how the content should be de-identified.
            var bucketingConfig = new [BucketingConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.BucketingConfig.html)
            {
                Buckets =
                {
                    new BucketingConfig.Types.Bucket
                    {
                        Min = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 0 },
                        Max = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 25 },
                        ReplacementValue = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Low" }
                    },
                    new BucketingConfig.Types.Bucket
                    {
                        Min = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 25 },
                        Max = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 75 },
                        ReplacementValue = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "Medium" }
                    },
                    new BucketingConfig.Types.Bucket
                    {
                        Min = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 75 },
                        Max = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { IntegerValue = 100 },
                        ReplacementValue = new [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.Value.html) { StringValue = "High" }
                    }
                }
            };
    
            // Specify the fields to be encrypted.
            var fields = new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html)[] { new [FieldId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldId.html) { Name = "score" } };
    
    
            // Associate the de-identification with the specified field.
            var fieldTransformation = new [FieldTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.FieldTransformation.html)
            {
                PrimitiveTransformation = new [PrimitiveTransformation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.PrimitiveTransformation.html)
                {
                    BucketingConfig = bucketingConfig
                },
                Fields = { fields }
            };
    
            // Construct the de-identify config.
            var deidentifyConfig = new [DeidentifyConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.DeidentifyConfig.html)
            {
                RecordTransformations = new [RecordTransformations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dlp.V2/latest/Google.Cloud.Dlp.V2.RecordTransformations.html)
                {
                    FieldTransformations = { fieldTransformation }
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
    	"fmt"
    	"io"
    
    	dlp "cloud.google.com/go/dlp/apiv2"
    	"cloud.google.com/go/dlp/apiv2/dlppb"
    )
    
    // deIdentifyTablePrimitiveBucketing bucket sensitive data by grouping numerical values into
    // predefined ranges to generalize and protect user information.
    func deIdentifyTablePrimitiveBucketing(w io.Writer, projectID string) error {
    	// projectId := "your-project-id"
    
    	row1 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "22"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Jane Austen"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "21"}},
    		},
    	}
    
    	row2 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "101"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Charles Dickens"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "95"}},
    		},
    	}
    
    	row3 := &dlppb.Table_Row{
    		Values: []*dlppb.Value{
    			{Type: &dlppb.Value_StringValue{StringValue: "55"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "Mark Twain"}},
    			{Type: &dlppb.Value_StringValue{StringValue: "75"}},
    		},
    	}
    
    	tableToDeidentify := &dlppb.Table{
    		Headers: []*dlppb.FieldId{
    			{Name: "AGE"},
    			{Name: "PATIENT"},
    			{Name: "HAPPINESS SCORE"},
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
    			Table: tableToDeidentify,
    		},
    	}
    
    	// Specify how the content should be de-identified.
    	buckets := []*dlppb.BucketingConfig_Bucket{
    		{
    			Min: &dlppb.Value{
    				Type: &dlppb.Value_IntegerValue{
    					IntegerValue: 0,
    				},
    			},
    			Max: &dlppb.Value{
    				Type: &dlppb.Value_IntegerValue{
    					IntegerValue: 25,
    				},
    			},
    			ReplacementValue: &dlppb.Value{
    				Type: &dlppb.Value_StringValue{
    					StringValue: "low",
    				},
    			},
    		},
    		{
    			Min: &dlppb.Value{
    				Type: &dlppb.Value_IntegerValue{
    					IntegerValue: 25,
    				},
    			},
    			Max: &dlppb.Value{
    				Type: &dlppb.Value_IntegerValue{
    					IntegerValue: 75,
    				},
    			},
    			ReplacementValue: &dlppb.Value{
    				Type: &dlppb.Value_StringValue{
    					StringValue: "Medium",
    				},
    			},
    		},
    		{
    			Min: &dlppb.Value{
    				Type: &dlppb.Value_IntegerValue{
    					IntegerValue: 75,
    				},
    			},
    			Max: &dlppb.Value{
    				Type: &dlppb.Value_IntegerValue{
    					IntegerValue: 100,
    				},
    			},
    			ReplacementValue: &dlppb.Value{
    				Type: &dlppb.Value_StringValue{
    					StringValue: "High",
    				},
    			},
    		},
    	}
    
    	// Specify the BucketingConfig in primitive transformation.
    	primitiveTransformation := &dlppb.PrimitiveTransformation_BucketingConfig{
    		BucketingConfig: &dlppb.BucketingConfig{
    			Buckets: buckets,
    		},
    	}
    
    	// Specify the field of the table to be de-identified
    	feildId := &dlppb.FieldId{
    		Name: "HAPPINESS SCORE",
    	}
    
    	// Specify the field transformation which apply to input field(s) on which you want to transform.
    	fieldTransformation := &dlppb.FieldTransformation{
    		Transformation: &dlppb.FieldTransformation_PrimitiveTransformation{
    			PrimitiveTransformation: &dlppb.PrimitiveTransformation{
    				Transformation: primitiveTransformation,
    			},
    		},
    		Fields: []*dlppb.FieldId{
    			feildId,
    		},
    	}
    	// Specify the record transformation to transform the record by applying various field transformations
    	transformation := &dlppb.RecordTransformations{
    		FieldTransformations: []*dlppb.FieldTransformation{
    			fieldTransformation,
    		},
    	}
    	// Specify the deidentification config.
    	deidentifyConfig := &dlppb.DeidentifyConfig{
    		Transformation: &dlppb.DeidentifyConfig_RecordTransformations{
    			RecordTransformations: transformation,
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
    import com.google.privacy.dlp.v2.[BucketingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.html);
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
    import com.google.privacy.dlp.v2.[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class DeIdentifyTableWithBucketingConfig {
      public static void main(String[] args) throws Exception {
    
        // TODO(developer): Replace these variables before running the sample.
        // The Google Cloud project id to use as a parent resource.
        String projectId = "your-project-id";
        // Specify the table to be considered for de-identification.
        [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify =
            [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).newBuilder()
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("AGE").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("PATIENT").build())
                .[addHeaders](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addHeaders_com_google_privacy_dlp_v2_FieldId_)([FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("HAPPINESS SCORE").build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("101").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Charles Dickens").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(95).build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("22").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Jane Austen").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(21).build())
                        .build())
                .[addRows](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.Builder.html#com_google_privacy_dlp_v2_Table_Builder_addRows_com_google_privacy_dlp_v2_Table_Row_)(
                    [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html).Row.newBuilder()
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("55").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Mark Twain").build())
                        .addValues([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(75).build())
                        .build())
                .build();
    
        deIdentifyTableBucketing(projectId, tableToDeIdentify);
      }
    
      // Performs data de-identification on a table by replacing the values within each bucket with
      // predefined replacement values.
      public static [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) deIdentifyTableBucketing(String projectId, [Table](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Table.html) tableToDeIdentify)
          throws IOException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html) dlp = [DlpServiceClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.cloud.dlp.v2.DlpServiceClient.html).create()) {
          // Specify what content you want the service to de-identify.
          [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html) contentItem = [ContentItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.ContentItem.html).newBuilder().setTable(tableToDeIdentify).build();
    
          List<BucketingConfig.[Bucket](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.Bucket.html)> buckets = new ArrayList<>();
          buckets.add(
              [BucketingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.html).Bucket.newBuilder()
                  .[setMin](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.Bucket.Builder.html#com_google_privacy_dlp_v2_BucketingConfig_Bucket_Builder_setMin_com_google_privacy_dlp_v2_Value_)([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(0).build())
                  .[setMax](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.Bucket.Builder.html#com_google_privacy_dlp_v2_BucketingConfig_Bucket_Builder_setMax_com_google_privacy_dlp_v2_Value_)([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(25).build())
                  .[setReplacementValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.Bucket.Builder.html#com_google_privacy_dlp_v2_BucketingConfig_Bucket_Builder_setReplacementValue_com_google_privacy_dlp_v2_Value_)([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("low").build())
                  .build());
          buckets.add(
              [BucketingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.html).Bucket.newBuilder()
                  .[setMin](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.Bucket.Builder.html#com_google_privacy_dlp_v2_BucketingConfig_Bucket_Builder_setMin_com_google_privacy_dlp_v2_Value_)([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(25).build())
                  .[setMax](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.Bucket.Builder.html#com_google_privacy_dlp_v2_BucketingConfig_Bucket_Builder_setMax_com_google_privacy_dlp_v2_Value_)([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(75).build())
                  .[setReplacementValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.Bucket.Builder.html#com_google_privacy_dlp_v2_BucketingConfig_Bucket_Builder_setReplacementValue_com_google_privacy_dlp_v2_Value_)([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("Medium").build())
                  .build());
          buckets.add(
              [BucketingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.html).Bucket.newBuilder()
                  .[setMin](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.Bucket.Builder.html#com_google_privacy_dlp_v2_BucketingConfig_Bucket_Builder_setMin_com_google_privacy_dlp_v2_Value_)([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(75).build())
                  .[setMax](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.Bucket.Builder.html#com_google_privacy_dlp_v2_BucketingConfig_Bucket_Builder_setMax_com_google_privacy_dlp_v2_Value_)([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setIntegerValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setIntegerValue_long_)(100).build())
                  .[setReplacementValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.Bucket.Builder.html#com_google_privacy_dlp_v2_BucketingConfig_Bucket_Builder_setReplacementValue_com_google_privacy_dlp_v2_Value_)([Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.html).newBuilder().[setStringValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.Value.Builder.html#com_google_privacy_dlp_v2_Value_Builder_setStringValue_java_lang_String_)("High").build())
                  .build());
    
          [BucketingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.html) bucketingConfig = [BucketingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.html).newBuilder().[addAllBuckets](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.BucketingConfig.Builder.html#com_google_privacy_dlp_v2_BucketingConfig_Builder_addAllBuckets_java_lang_Iterable___extends_com_google_privacy_dlp_v2_BucketingConfig_Bucket__)(buckets).build();
    
          [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html) primitiveTransformation =
              [PrimitiveTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.html).newBuilder().[setBucketingConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.PrimitiveTransformation.Builder.html#com_google_privacy_dlp_v2_PrimitiveTransformation_Builder_setBucketingConfig_com_google_privacy_dlp_v2_BucketingConfig_)(bucketingConfig).build();
    
          // Specify the field of the table to be de-identified.
          [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html) fieldId = [FieldId](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldId.html).newBuilder().setName("HAPPINESS SCORE").build();
    
          [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html) fieldTransformation =
              [FieldTransformation](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.html).newBuilder()
                  .setPrimitiveTransformation(primitiveTransformation)
                  .[addFields](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.FieldTransformation.Builder.html#com_google_privacy_dlp_v2_FieldTransformation_Builder_addFields_com_google_privacy_dlp_v2_FieldId_)(fieldId)
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
          System.out.println("Table after de-identification: " + response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getTable());
          return response.[getItem](https://docs.cloud.google.com/java/docs/reference/google-cloud-dlp/latest/com.google.privacy.dlp.v2.DeidentifyContentResponse.html#com_google_privacy_dlp_v2_DeidentifyContentResponse_getItem__)().getTable();
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
    // const projectId = 'your-project-id';
    
    // Construct the tabular data
    const tablularData = {
      headers: [{name: 'AGE'}, {name: 'PATIENT'}, {name: 'HAPPINESS SCORE'}],
      rows: [
        {
          values: [
            {stringValue: '101'},
            {stringValue: 'Charles Dickens'},
            {integerValue: 95},
          ],
        },
        {
          values: [
            {stringValue: '22'},
            {stringValue: 'Jane Austen'},
            {integerValue: 21},
          ],
        },
        {
          values: [
            {stringValue: '55'},
            {stringValue: 'Mark Twain'},
            {integerValue: 75},
          ],
        },
      ],
    };
    
    async function deIdentifyTableBucketing() {
      // Construct bucket confiugrations
      const buckets = [
        {
          min: {integerValue: 0},
          max: {integerValue: 25},
          replacementValue: {stringValue: 'Low'},
        },
        {
          min: {integerValue: 25},
          max: {integerValue: 75},
          replacementValue: {stringValue: 'Medium'},
        },
        {
          min: {integerValue: 75},
          max: {integerValue: 100},
          replacementValue: {stringValue: 'High'},
        },
      ];
    
      const bucketingConfig = {
        buckets: buckets,
      };
    
      // The list of fields to be transformed.
      const fieldIds = [{name: 'HAPPINESS SCORE'}];
    
      // Associate fields with bucketing configuration.
      const fieldTransformations = [
        {
          primitiveTransformation: {bucketingConfig: bucketingConfig},
          fields: fieldIds,
        },
      ];
    
      // Specify de-identify configuration using transformation object.
      const deidentifyConfig = {
        recordTransformations: {
          fieldTransformations: fieldTransformations,
        },
      };
    
      // Combine configurations into a request for the service.
      const request = {
        parent: `projects/${projectId}/locations/global`,
        deidentifyConfig: deidentifyConfig,
        item: {
          table: tablularData,
        },
      };
      // Send the request and receive response from the service.
      const [response] = await dlp.deidentifyContent(request);
    
      // Print the results.
      console.log(
        `Table after de-identification: ${JSON.stringify(
          response.item.table,
          null,
          2
        )}`
      );
    }
    deIdentifyTableBucketing();

### PHP

To learn how to install and use the client library for Sensitive Data Protection, see [Sensitive Data Protection client libraries](https://docs.cloud.google.com/sensitive-data-protection/docs/libraries). 

To authenticate to Sensitive Data Protection, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Dlp\V2\BucketingConfig;
    use Google\Cloud\Dlp\V2\BucketingConfig\Bucket;
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
    use Google\Cloud\Dlp\V2\Value;
    
    /**
     * De-identify data using primitive bucketing.
     * https://cloud.google.com/dlp/docs/concepts-bucketing#bucketing_scenario_1
     *
     * @param string $callingProjectId      The Google Cloud project id to use as a parent resource.
     * @param string $inputCsvFile          The input file(csv) path to deidentify.
     * @param string $outputCsvFile         The oupt file path to save deidentify content.
     *
     */
    function deidentify_table_primitive_bucketing(
        // TODO(developer): Replace sample parameters before running the code.
        string $callingProjectId,
        string $inputCsvFile = './test/data/table4.csv',
        string $outputCsvFile = './test/data/deidentify_table_primitive_bucketing_output.csv'
    ): void {
        // Instantiate a client.
        $dlp = new DlpServiceClient();
    
        // Read a CSV file.
        $csvLines = file($inputCsvFile, FILE_IGNORE_NEW_LINES);
        $csvHeaders = explode(',', $csvLines[0]);
        $csvRows = array_slice($csvLines, 1);
    
        // Convert CSV file into protobuf objects.
        $tableHeaders = array_map(function ($csvHeader) {
            return (new FieldId)->setName($csvHeader);
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
    
        // Specify how the content should be de-identified.
        $buckets = [
            (new Bucket())
                ->setMin((new Value())
                    ->setIntegerValue(0))
                ->setMax((new Value())
                    ->setIntegerValue(25))
                ->setReplacementValue((new Value())
                    ->setStringValue('LOW')),
            (new Bucket())
                ->setMin((new Value())
                    ->setIntegerValue(25))
                ->setMax((new Value())
                    ->setIntegerValue(75))
                ->setReplacementValue((new Value())
                    ->setStringValue('Medium')),
            (new Bucket())
                ->setMin((new Value())
                    ->setIntegerValue(75))
                ->setMax((new Value())
                    ->setIntegerValue(100))
                ->setReplacementValue((new Value())
                    ->setStringValue('High')),
        ];
    
        $bucketingConfig = (new BucketingConfig())
            ->setBuckets($buckets);
    
        $primitiveTransformation = (new PrimitiveTransformation())
            ->setBucketingConfig($bucketingConfig);
    
        // Specify the field of the table to be de-identified.
        $fieldId = (new FieldId())
            ->setName('score');
    
        $fieldTransformation = (new FieldTransformation())
            ->setPrimitiveTransformation($primitiveTransformation)
            ->setFields([$fieldId]);
    
        $recordTransformations = (new RecordTransformations())
            ->setFieldTransformations([$fieldTransformation]);
    
        // Create the deidentification configuration object.
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
    
    
    import google.cloud.dlp
    
    
    def deidentify_table_primitive_bucketing(
        project: str,
    ) -> None:
        """Uses the Data Loss Prevention API to de-identify sensitive data in
        a table by replacing them with generalized bucket labels.
        Args:
            project: The Google Cloud project id to use as a parent resource.
        """
    
        # Instantiate a client.
        dlp = google.cloud.[dlp_v2](https://docs.cloud.google.com/python/docs/reference/dlp/latest).[DlpServiceClient](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html)()
    
        # Convert the project id into a full resource id.
        parent = f"projects/{project}/locations/global"
    
        # Dictionary representing table to de-identify.
        # The table can also be taken as input to the function.
        table_to_deid = {
            "header": ["age", "patient", "happiness_score"],
            "rows": [
                ["101", "Charles Dickens", "95"],
                ["22", "Jane Austen", "21"],
                ["90", "Mark Twain", "75"],
            ],
        }
    
        # Construct the `table`. For more details on the table schema, please see
        # https://cloud.google.com/dlp/docs/reference/rest/v2/ContentItem#Table
        headers = [{"name": val} for val in table_to_deid["header"]]
        rows = []
        for row in table_to_deid["rows"]:
            rows.append({"values": [{"string_value": cell_val} for cell_val in row]})
    
        table = {"headers": headers, "rows": rows}
    
        # Construct the `item` for table to de-identify.
        item = {"table": table}
    
        # Construct generalised bucket configuration.
        buckets_config = [
            {
                "min_": {"integer_value": 0},
                "max_": {"integer_value": 25},
                "replacement_value": {"string_value": "Low"},
            },
            {
                "min_": {"integer_value": 25},
                "max_": {"integer_value": 75},
                "replacement_value": {"string_value": "Medium"},
            },
            {
                "min_": {"integer_value": 75},
                "max_": {"integer_value": 100},
                "replacement_value": {"string_value": "High"},
            },
        ]
    
        # Construct de-identify configuration that groups values in a table field and replace those with bucket labels.
        deidentify_config = {
            "record_transformations": {
                "field_transformations": [
                    {
                        "fields": [{"name": "happiness_score"}],
                        "primitive_transformation": {
                            "bucketing_config": {"buckets": buckets_config}
                        },
                    }
                ]
            }
        }
    
        # Call the API to deidentify table data through primitive bucketing.
        response = dlp.[deidentify_content](https://docs.cloud.google.com/python/docs/reference/dlp/latest/google.cloud.dlp_v2.services.dlp_service.DlpServiceClient.html#google_cloud_dlp_v2_services_dlp_service_DlpServiceClient_deidentify_content)(
            request={
                "parent": parent,
                "deidentify_config": deidentify_config,
                "item": item,
            }
        )
    
        # Print the results.
        print(f"Table after de-identification: {response.item.table}")
    
    

### REST
    
    
    ...
    {
      "primitiveTransformation":
      {
        "bucketingConfig":
        {
          "buckets":
          [
            {
              "min":
              {
                "integerValue": "0"
              },
              "max":
              {
                "integerValue": "25"
              },
              "replacementValue":
              {
                "stringValue": "Low"
              }
            },
            {
              "min":
              {
                "integerValue": "26"
              },
              "max":
              {
                "integerValue": "75"
              },
              "replacementValue":
              {
                "stringValue": "Medium"
              }
            },
            {
              "min":
              {
                "integerValue": "76"
              },
              "max":
              {
                "integerValue": "100"
              },
              "replacementValue":
              {
                "stringValue": "High"
              }
            }
          ]
        }
      }
    }
    ...
    

## Bucketing scenario 2

Bucketing can also be used on strings or enumerated values. Suppose you wanted to share salary data and include job titles. However, some job titles, such as CEO or distinguished engineer, can be linked to one person or a small group of people. Such job titles are easily matched to the employees who hold them.

Bucketing can help here as well. Instead of including exact job titles, generalize and bucket them. For example, "Senior Engineer," "Junior Engineer," and "Distinguished Engineer" become generalized and bucketed into simply "Engineer." The following table illustrates bucketing specific job titles into job title families.

![Diagram illustrating bucketing of job titles](https://docs.cloud.google.com/static/sensitive-data-protection/docs/images/bucketing.png)

## Other scenarios

In these examples, we've applied the transformation to structured data. Bucketing can also be used on unstructured examples, as long as the value can be classified with a predefined or custom infoType. Below are some example scenarios:

  * Classify dates and bucket them into year ranges
  * Classify names and bucket them into groups based on the first letter (A-M, N-Z)



## Resources

To learn more about generalization and bucketing, see [De-identifying Sensitive Data in Text Content](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data#bucketingconfig).

For API documentation, see:

  * [`projects.content.deidentify` method](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify)
  * [`BucketingConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.BucketingConfig) transformation: Buckets values based on custom ranges.
  * [`FixedSizeBucketingConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/organizations.deidentifyTemplates#DeidentifyTemplate.BucketingConfig) transformation: Buckets values based on fixed size ranges.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
